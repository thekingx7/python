# الخصم بالنسبة المئوية
addnum = int(input("how much money ? :"))# ادخل المبلغ او تكلفه المنتج
discount = int(input("how much discount % :") )# ادخل الخصم بدون علامه %

num = addnum / 100 * discount # عملية حساب الخصم
num2 = addnum - num
#طباعة الناتج
print(f"Price before discount {addnum},The price after discount {num2} , total discount {num} . see you later")