x = 15
print(x>10)
print(not x>10 and x <=15)
today_temp = int(input("Enter Today's Temperature :"))
if today_temp >= 35:
    print("Today feels like extream  hot")
elif today_temp >= 30 and today_temp <35:
    print("Today feels like hot")
elif today_temp >= 25 and today_temp <30:
    print("Today feels pleasant")
elif today_temp >= 10 and today_temp <25:
    print("Today feels cold")
else:
    print("Today feels too cold")






