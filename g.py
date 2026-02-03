import random

def guess_game():
    number = random.randint(1, 100)
    attempts = 0
    print("--- مرحباً بك في لعبة تخمين الرقم ---")
    print("لقد اخترت رقماً بين 1 و 100. هل يمكنك معرفته؟")

    while True:
        try:
            user_guess = int(input("أدخل تخمينك: "))
            attempts += 1

            if user_guess < number:
                print("أكبر قليلاً! ⬆️")
            elif user_guess > number:
                print("أصغر قليلاً! ⬇️")
            else:
                print(f"🎉 عبقري! لقد عرفت الرقم {number} في {attempts} محاولات.")
                break
        except ValueError:
            print("الرجاء إدخال رقم صحيح فقط!")

guess_game()