import csv
import json
import copy
def csv2json():
    class_list = [[], [], [], []]
    with open(r'E:\Workspace\数据转换\history.csv', 'r',encoding='utf-8') as opener:
        reader = csv.reader(opener)
        for ind, row in enumerate(reader):
            index = 0
            now_list = []
            now_dict = {}
            clas_index=4
            for index_2,each in enumerate(reversed(row)):
                if each:
                    clas_index-=1

                    now_dict = {each: now_list}
                    now_list = [now_dict]
                else:
                    index += 1
            class_list[index].append((ind,now_dict))

            s_dict=copy.copy(now_dict)
            while str(s_dict.values())!='dict_values([[]])':
                # print(str(s_dict.values()))
                #将不同的子集添加到不同的部分
                for k,v in s_dict.items():
                    if v:

                        clas_index+=1
                        # print('this is vo', end=':')
                        # print((clas_index, v[0]))
                        class_list[clas_index].append((ind,v[0]))
                        s_dict=v[0]


    class_list.reverse()
    #遍历每一个等级的
    for index, list in enumerate(class_list[:len(class_list) - 1]):
        while list:
            each=list.pop()
        # for each in list:
            min = 10
            min_index = 0
            for ind, sd in enumerate(class_list[index + 1]):
                # 找出index最近的

                if each[0] - sd[0] >=0 and each[0] - sd[0] < min:
                    min_index = ind
                    min = each[0] - sd[0]
            result_dict = class_list[index + 1][min_index][1]

            is_exist=False
            json_dict=json.dumps(result_dict,ensure_ascii=False)
            each_dict=json.dumps(each[1],ensure_ascii=False)

            if each_dict not in json_dict:
                for k, v in result_dict.items():
                        v.append(each[1])

    class_list.reverse()

    with open('reslt.json','w') as opener:

        opener.write(json.dumps(class_list[0][0][1],ensure_ascii=False))


    return class_list[0][0][1]

isfound=0

def find(key):
    if key=="奴隶社会":
        print(key)
        return
    data = csv2json()
    value_list = data['奴隶社会']
    label_list = [(0, '奴隶社会')]
    index_list = [0]
    result = dfs(value_list, key, label_list, index_list, 0)
    if isfound==0:
        print("不存在关键字:{}".format(key))

def dfs(dict_list, key, label_list, index_list, cls):
    for index, dict in enumerate(dict_list):
        for k, v in dict.items():
            label_list.append((cls + 1, k))

            if k == key:
                label_list.reverse()
                have_seen = []
                label_out = []
                for each in label_list:
                    if each[0] not in have_seen and each[0] <= cls + 1:
                        label_out.append(each[1])
                        have_seen.append(each[0])
                label_out.reverse()
                print('.'.join(i for i in label_out))
                global isfound
                isfound=1

                return True
            else:
                index_list.append(index)
                new_list = index_list * 1
                # dicts[k] = v
                dfs(v, key, label_list, new_list, cls + 1)


json_formate=csv2json()
# find('奴隶社会')
lablelist = find("汉谟拉比法典")
lablelist = find("美洲")

