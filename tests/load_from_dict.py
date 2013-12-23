from json_rbac.acl_from_dict import acl_from_dict


resources = {
    "course": [],
    "senior-course": ["course"]
}

d = {
    "roles": {
        "member": [],
        "student": ["member"],
        "teacher": ["member"],
        "junior-student": ["student"],
    },
    "allow": [
        {
            "role": "member",
            "operation": "view",
            "resource": "course"
        },
        {
            "role": "student",
            "operation": "learn",
            "resource": "course"
        },
        {
            "role": "teacher",
            "operation": "teach",
            "resource": "course"
        }
    ],
    "deny": [
        {
            "role": "junior-student",
            "operation": "learn",
            "resource": "senior-course"
        }
    ]
}



d['resources'] = resources

acl = acl_from_dict(d)

# Check permissions

if acl.is_allowed("student", "view", "course"):
    print("Students chould view courses.")
else:
    print("Students chould not view courses.")

if acl.is_allowed("junior-student", "learn", "senior-course"):
    print("Junior students chould learn senior courses.")
else:
    print("Junior students chould not learn senior courses.")
