from twisted.internet import reactor

from json_rbac.registry_wrapper import RegistryWrapper
from json_rbac.watching_json_registry_loader import WatchingJsonRegistryLoader


resources = {
    "course": [],
    "senior-course": ["course"]
}

registry_loader = WatchingJsonRegistryLoader("roles.json", resources)

acl = RegistryWrapper(registry_loader)


def check_permissions():
    # Check permissions

    if acl.is_allowed("student", "view", "course"):
        print("Students could view courses.")
    else:
        print("Students could not view courses.")

    if acl.is_allowed("junior-student", "learn", "senior-course"):
        print("Junior students could learn senior courses.")
    else:
        print("Junior students could not learn senior courses.")

    reactor.callLater(3, check_permissions)

check_permissions()

reactor.run()
