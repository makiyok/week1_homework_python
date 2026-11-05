class Fighter:
    def __init__(self, name, hp, attack, defense):
        # 引数で受け取った値を、インスタンスの属性に入れる
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense

    def super_saiyan(self):
        # 今の攻撃力を2倍にして、属性に入れ直す
        self.attack = self.attack * 2

    def punch(self, opponent):
        # self が攻撃する側、opponent が攻撃される側
        damage = self.attack - opponent.defense
        opponent.hp -= damage
        # HP がマイナスにならないよう、0 にそろえる
        if opponent.hp < 0:
            opponent.hp = 0
        print(f"{self.name}の攻撃! {opponent.name}に{damage}のダメージ! ({opponent.name}のHP: {opponent.hp})")


gokuu = Fighter("悟空", 1000, 100, 50)
vegita = Fighter("ベジータ", 1000, 80, 100)

# 戦う前に、悟空をスーパーサイヤ人に変身させる
gokuu.super_saiyan()
print(f"{gokuu.name}はスーパーサイヤ人に変身した! 攻撃力: {gokuu.attack}")

turn = 1
# 何ターンで終わるか分からないので、break するまでずっとくり返す
while True:
    print(f"--- ターン{turn} ---")

    # 悟空の攻撃。ベジータの HP が 0 になったら、ターンの途中でも終わる
    gokuu.punch(vegita)
    if vegita.hp == 0:
        print(f"{vegita.name}は倒れた! {gokuu.name}の勝利!")
        break

    # ベジータの攻撃。悟空の HP が 0 になったら終わる
    vegita.punch(gokuu)
    if gokuu.hp == 0:
        print(f"{gokuu.name}は倒れた! {vegita.name}の勝利!")
        break

    turn += 1
