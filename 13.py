print()
ticket = int(input("Какое колличество билетов Вы желаете приобрести?\nВведите колличество: "))

age = int(input("Введите Ваш возраст: "))
if age < 18:
    print("Бесплатно")

elif 18 <= age <= 25:
    print("Цена за 1 билет:", 990)
    print("К оплате: ", 990 * ticket)
    if ticket >= 3:
      print("К оплате, с учетом скидки 10%: ", int((990 * ticket) * 0.9))

elif age > 25:
    print("Цена за 1 билет:", 1390)
    print(1390 * ticket)
    if ticket >= 3:
      print("К оплате, с учетом скидки 10%: ", int((1390 * ticket) * 0.9))
