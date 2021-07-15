dic1 = {"A001":"小熊軟糖,20元","A002":"冰棒,25元","A004":"王子麵","A006":"汽水,30元"}
x = (input("請輸入你要查的貨號:"))
if x in dic1:
    d = dic1.pop(x)
    print(d)
else:
    print("您輸入的貨號無相對應的商品喔!")
    new = (input("請問您要新增的貨品名稱,價格為?"))
    update = {x:new}
    dic1.update(update)
    print(dic1)
