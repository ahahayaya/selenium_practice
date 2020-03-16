import yaml,sys,os
sys.path.append(os.getcwd())
def get_data():
    data_list = []
    with open('G/web/Data/login_data.yaml','r',encoding='utf-8') as f:
        readdata = f.read()
        data = yaml.load(readdata).get("data")
        print(data)
    for i in data:
        for o in i.keys():
            data_list.append((i.get(o).get('uname'),i.get(o).get('pwd')))
    return data_list

