#!/use/bin/env python3
#encoding: utf-8
#__author: "Digital-Galaxy"
#date: 2017-8-14 4:00 PM

menu = {
    '北京':{
        '朝阳':{
            '国贸':{
                'CICC': {},
                'HP': {},
                '渣打银行': {},
                'CCTV': {},
            },
            '望京':{
                '陌陌': {},
                '奔驰': {},
                '360': {},
            },
            '三里屯':{
                '优衣库': {},
                'apple': {},
            },
        },
        '昌平':{
            '沙河': {
                '老男孩': {},
                '阿泰包子': {},
            },
            '天通苑': {
                '链家': {},
                '我爱我家': {},
            },
            '回龙观': {},
        },
        '海淀':{
            '五道口': {
                'google': {},
                '网易': {},
                '搜狐': {},
                '搜狗': {},
                '快手': {},
            },
            '中关村': {
                'youku': {},
                '爱奇艺': {},
                '汽车之家': {},
                '新东方总部': {},
                '腾讯': {},
            },
        },
    },
    '上海':{
        '浦东': {
            '陆家嘴': {
                '高盛': {},
                'CICC': {},
                '摩根': {},
            },
            '外滩': {},
        },
        '闵行': {},
        '闸北区': {},
        '静安区': {},
    },
    '山东':{
        '济南': {},
        '泰安': {},
        '德州': {
            '乐陵': {
                '丁乌镇': {},
                '城区': {},
            },
            '平原县': {},
        },
    },
}

current_layer = menu
parrent_layers = []
while True:
    for key in current_layer:
        print(key)
    choice = input(">>>:").strip()
    if len(choice) == 0:
        continue
    if choice in current_layer:
        # parrent_layer = current_layer
        parrent_layers.append(current_layer)
        current_layer = current_layer[choice]
    elif choice == 'b':
        # current_layer = parrent_layer
        if parrent_layers:
            current_layer = parrent_layers.pop()
    else:
        print("无此项")
