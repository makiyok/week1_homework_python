"""問題：おこづかい帳
①残高を持つ Wallet クラスを作成する（最初の残高は 1000円）
②ターミナルで「1: 入金」「2: 支払い」「3: 終了」を選べるようにする
③入金・支払いの金額は入力で決め、残高より多い支払いは「残高が足りません」と出力する
④「3」が入力されるまでくり返し、終了するときに最後の残高を出力する
"""


class Wallet:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount}円を入金しました。残高: {self.balance}円")

    def pay(self, amount):
        if amount > self.balance:
            print("もっと働こう")
        else:
            self.balance -= amount
            print(f"{amount}円を支払いました。残高: {self.balance}円")


def show_menu():
    print("1: 入金 / 2: 支払い / 3: 終了")


wallet = Wallet(1000)

while True:
    show_menu()
    choice = input("番号を入力：")
    if choice == "1":
        amount = int(input("入金する金額："))
        wallet.deposit(amount)
    elif choice == "2":
        amount = int(input("支払う金額："))
        wallet.pay(amount)
    elif choice == "3":
        print(f"終了します。最後の残高: {wallet.balance}円")
        break
    else:
        print("1〜3の番号を入力してください")
