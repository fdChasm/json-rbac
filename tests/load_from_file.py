from json_rbac.config_loader import config_loader


data, referenced_configs = config_loader("test.json")

print data, referenced_configs
