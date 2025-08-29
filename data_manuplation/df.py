import yaml


with open('data.yaml','r') as f:
    r = yaml.safe_load(f)

print(r,type(r))
print(r['config_1']['test'])
print(r['config_1']['is_there'])
