per_cent = {'ТКБ': 5.6,
            'СКБ': 5.9,
            'ВТБ': 4.28,
            'СБЕР': 4.0}
money = int(input('Введите сумму: '))
tkb = int((per_cent['ТКБ']) * (money / 100))
skb = int((per_cent['СКБ']) * (money / 100))
vtb = int((per_cent['ВТБ']) * (money / 100))
sber = int((per_cent['СБЕР']) * (money / 100))
deposit = ['ТКБ:', tkb, 'СКБ:', skb, 'ВТБ:', vtb, 'СБЕР:',sber]
print(deposit)
