def reject_defective_items(weight_list,min_w=98.0,max_w=102.2):
    filtered=[]
    wrong=[]
    
    for i in weight_list:
        if min_w<=i<=max_w:
            filtered.append(i)
        else:
            wrong.append(i)
            continue
    return filtered, wrong

def get_weight_distribution(weight_list,min_w=98.0,max_w=102.0):
    weight_dic = {
        "легкие":0,
        "нормальные":0,
        "тяжелые":0
    }
    for i in weight_list:
        if i < min_w: weight_dic["легкие"]+=1
        if min_w <= i <=max_w: weight_dic["нормальные"]+=1
        else: weight_dic["тяжелые"]+=1
    return weight_dic
def get_sample_pack(weight_list, step):
    return weight_list[::step]


