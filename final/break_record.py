def his_high_3():
    import csv
    fh1 = open('his_high.csv', 'r', newline = '', encoding = 'utf-8') #newline 參數指定 open()不對換行字元做額外處理
    csv1 = csv.DictReader(fh1) 
    cname1 = csv1.fieldnames #csv1.fieldnames 中為原始檔案第一列中的欄位名稱

    list = []
    for aline in csv1:
        list1 = [aline[cname1[0]].strip() , aline[cname1[1]].strip(), aline[cname1[2]].strip()]
        list.append(list1)
    # print(list)
    his_high = (list[0][1],list[0][2])
    fh1.close()
    return list
his_list = his_high_3()

def break_record():
    import csv
    if score > int(his_list[2][2]):
        if score > int(his_list[1][2]):
            if score > int(his_list[0][2]):
                his_list[2] = [3,his_list[1][1],his_list[1][2]]
                his_list[1] = [2,his_list[0][1],his_list[0][2]]
                his_list[0] = [1,user,score]
            else:
                his_list[2] = [3,his_list[1][1],his_list[1][2]]
                his_list[1] = [2,user,score]
                
        else:
            his_list[2] = [(3,user,score)]

    with open('his_high.csv', 'w', newline='', encoding = 'utf-8') as csvfile:
        # 建立 CSV 檔寫入器
        writer = csv.writer(csvfile)

        # 寫入一列資料
        writer.writerow(['#', 'user', 'score'])

        # 寫入另外幾列資料
        writer.writerow(his_list[0])
        writer.writerow(his_list[1])
        writer.writerow(his_list[2])
    csvfile.close()

score = 300
user ='te'
break_record()
