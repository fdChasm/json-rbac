import rbac.acl

def acl_from_dict(d):
    acl = rbac.acl.Registry()

    for role, parents in d.get("roles", {}).iteritems():
        acl.add_role(role, parents)

    for resource, parents in d.get("resources", {}).iteritems():
        acl.add_resource(resource, parents)

    for allow in d.get("allow", []):
        role = allow['role']
        operation = allow['operation']
        resource = allow['resource']

        acl.allow(role, operation, resource)

    for deny in d.get("deny", []):
        role = deny['role']
        operation = deny['operation']
        resource = deny['resource']

        acl.deny(role, operation, resource)

    return acl
