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


# 名前・体力・攻撃力・防御力の順に渡して、インスタンスを作る
gokuu = Fighter("悟空", 1000, 100, 50)
vegita = Fighter("ベジータ", 1000, 80, 100)
