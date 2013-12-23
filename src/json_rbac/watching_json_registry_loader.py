from twisted.internet import inotify
import twisted.internet
from twisted.internet.inotify import IN_WATCH_MASK
from twisted.python import filepath

from json_rbac.json_registry_loader import JsonRegistryLoader


class WatchingJsonRegistryLoader(object):

    reactor = twisted.internet.reactor

    def __init__(self, filename, resources):
        self._filename = filename
        self._resources = resources

        self._notifier = inotify.INotify()
        self._notifier.startReading()
        self._watched_paths = []

        self._pending_reload = None

        self._load_acl()

    def _load_acl(self):
        self._json_registry_loader = JsonRegistryLoader(self._filename, self._resources)
        self._setup_watches()

    def _setup_watches(self):
        while self._watched_paths:
            self._notifier.ignore(self._watched_paths.pop())
        for referenced_filename in self._json_registry_loader.get_referenced_filenames():
            self._notifier.watch(filepath.FilePath(referenced_filename), mask=IN_WATCH_MASK, callbacks=[self._on_config_change])

    def _on_config_change(self, _watch, filepath, mask):
        # mask_name = ', '.join(inotify.humanReadableMask(mask))
        # print "config change event {!r} on {!r}".format(mask_name, filepath)
        self._queue_reload()

    def _queue_reload(self):
        if self._pending_reload: self._pending_reload.cancel()
        def reload_acl():
            self._pending_reload = None
            self.reload()
        self._pending_reload = self.reactor.callLater(1.0, reload_acl)

    def get_acl(self):
        return self._json_registry_loader.get_acl()

    def reload(self):
        self._load_acl()
