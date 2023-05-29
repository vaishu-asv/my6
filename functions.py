import utils

def conversion_pr(html,node_data,main,parent_top,parent_left,from_main):
    # print(node_data)
    # print("##############")
    no_div = False
    brd = "''"
    radius_dt = ""
    RGB = ""
    pos = "absolute"

    if node_data['fills']:
        if 'color' in node_data['fills'][0].keys():
            RGB = str((node_data['fills'][0]['color']['r'])*255)+','+str((node_data['fills'][0]['color']['g'])*255)+','+str((node_data['fills'][0]['color']['b'])*255)+','+str(node_data['fills'][0]['color']['a'])
        else:
            pass
    elif 'backgroundColor' in node_data.keys():
        RGB = str((node_data['backgroundColor']['r'])*255)+','+str((node_data['backgroundColor']['g'])*255)+','+str((node_data['backgroundColor']['b'])*255)+','+str(node_data['backgroundColor']['a'])
    else:
        pass
    if main:
        pos = "''"
        
        parent_top = node_data['absoluteBoundingBox']['y']
        parent_left = node_data['absoluteBoundingBox']['x']
        no_div = True
    else :
        tp = int(node_data['absoluteBoundingBox']['y'])
        lf = int(node_data['absoluteBoundingBox']['x'])
        no_div = False
        if 'cornerRadius' in node_data.keys():
            radius_dt = ";border-style: ridge;border-radius: "+str(node_data['cornerRadius'])+"px;"
        
        t = int(parent_top)
        l = int(parent_left)
        parent_top = abs(int(parent_top) - (tp))
        parent_left = abs(int(parent_left) - lf)
        print(node_data['name'])
        if node_data['name'] == 'text':
            print("===================")
            no_div = True
            
            txt_html = utils.text_tags(node_data,html,abs(t),abs(l),from_main)

            html += txt_html
            return html,no_div

    html += '<div name='+node_data['name']+' style="position:'+pos+' ;width: ' + str(node_data['absoluteBoundingBox']['width']) + 'px; height: ' + str(node_data['absoluteBoundingBox']['height']) + 'px;' + ' background-color: ' + 'rgba('+ RGB +');top:'+ str(parent_top) + 'px; left: ' + str(parent_left) + 'px'+str(radius_dt)+'">\n'

    
    return html,no_div


def group_list(json_data,html,from_main):
    # print(json_data)
    # print("**************")
    from_main = False
    parent_top = json_data['absoluteBoundingBox']['y']
    parent_left = json_data['absoluteBoundingBox']['x']
    main = False
    html,no_div = conversion_pr(html,json_data,main,parent_top,parent_left,from_main)
    if 'children' in json_data.keys():

        for dt in json_data['children']:
            main =False
            # print(dt)
            if dt == "Group":
                group_list(dt,html)
            else:
                html,no_div = conversion_pr(html,dt,main,parent_top,parent_left,from_main)

                if no_div:
                    html += '\n'
                else: 
                    html += '</div>\n'
            # print("===============")
    
    html += '</div>\n'
    
    