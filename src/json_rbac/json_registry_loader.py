from json_rbac.acl_from_dict import acl_from_dict
from json_rbac.config_loader import config_loader


class JsonRegistryLoader(object):
    def __init__(self, filename, resources):
        self._filename = filename
        self._resources = resources

        self._load_acl()

    def _load_acl(self):
        data, self._referenced_filenames = config_loader(self._filename)
        data['resources'] = self._resources
        self._acl = acl_from_dict(data)

    def get_acl(self):
        return self._acl

    def get_referenced_filenames(self):
        return self._referenced_filenames[:]

    def reload(self):
        self._load_acl()
