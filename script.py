print("==================================================")
print("Hello, World!")
print('Hello, World!')
print(777)
print("\n")


money = 100
apple_price = 100
if money > apple_price:
    print('りんごを買うことができます')
elif money == apple_price:
    print("りんごを買うことができますが所持金が0になります")
else:
    print('お金が足りません')
print("\n")


x = 20
if x >= 10 and x <= 30:
    print("xは10以上30以下です")
y = 60
if y < 10 or y > 30:
    print("yは10未満または30より大きいです")
z = 55
if z != 77:
    print("zは77ではありません_v1")
if not z == 77:
    print("zは77ではありません_v2")
print("\n")


# elifとint()とstr()
apple_price = 200
money = 1000
input_count = input("購入するりんごの個数を入力してください：")
count = int(input_count)
total_price = apple_price * count
print('購入するりんごの個数は' + str(count) + '個です')
print('支払い金額は' + str(total_price) + '円です')
if money > total_price:
    print("りんごを"+str(count)+"個買いました")
    print("残金は"+str(money-total_price)+"円です")
elif money == total_price:
    print("りんごを"+str(count)+"個買いました")
    print("財布が空になりました")
else:
    print("お金が足りません")
    print("りんごを買えませんでした")
print("\n")


# 配列リスト
fruits = ['apple', 'banana', 'orange']
fruits.append("grape")
print(fruits)
fruits[0] = "cherry"
print(fruits[0])
for fruit in fruits:
    print("好きな果物は"+fruit+"です")
print("\n")


# ハッシュ辞書
fruits = {'apple': 100, 'banana': 200, 'orange': 400}
fruits["banana"] = 300
fruits["grape"] = 500
print(fruits)
fruits = {'apple': 'りんご', 'banana': 'バナナ', 'grape': 'ぶどう'}
for fruit_key in fruits:
    print(fruit_key+"は"+fruits[fruit_key]+"という意味です")
print("\n")


x = 10
while x > 0:
    print(x)
    x -= 1
print("\n")


# breakとcontinue
numbers = [765, 921, 777, 256]
for number in numbers:
    print(number)
    if number == 777:
        print("777が見つかったので処理を終了します")
        break
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    if number % 3 == 0:
        continue
    print(number)
print("\n")


# bill
money = 1000
items = {'apple': 100, 'banana': 200, 'orange': 400}
for item_name in items:
    print('--------------------------------------------------')
    print('財布には' + str(money) + '円入っています')
    print(item_name + 'は1個' + str(items[item_name]) + '円です')
    input_count = input('購入する' + item_name + 'の個数を入力してください：')
    print('購入する' + item_name + 'の個数は' + input_count + '個です')
    count = int(input_count)
    total_price = items[item_name] * count
    print('支払い金額は' + str(total_price) + '円です')
    if money >= total_price:
        print(item_name + 'を' + input_count + '個買いました')
        money -= total_price
        if money == 0:
            print("財布が空になりました")
            break
    else:
        print('お金が足りません')
        print(item_name + 'を買えませんでした')
print("残金は"+str(money)+"円です")
print("\n")
