
__all__ = ["RegistryWrapper"]

class RegistryWrapper(object):
    def __init__(self, registry_loader):
        self._registry_loader = registry_loader

    @property
    def _acl(self):
        return self._registry_loader.get_acl()

    def reload(self):
        self._acl = self._registry_loader.reload()

    def add_role(self, role, parents=[]):
        return self._acl.add_role(role=role, parents=parents)

    def add_resource(self, resource, parents=[]):
        return self._acl.add_resource(resource=resource, parents=parents)

    def allow(self, role, operation, resource, assertion=None):
        return self._acl.allow(role=role, operation=operation, assertion=assertion)

    def deny(self, role, operation, resource, assertion=None):
        return self._acl.deny(role=role, operation=operation, resource=resource, assertion=assertion)

    def is_allowed(self, role, operation, resource):
        return self._acl.is_allowed(role=role, operation=operation, resource=resource)

    def is_any_allowed(self, roles, operation, resource):
        return self._acl.is_any_allowed(roles=roles, operation=operation, resource=resource)
