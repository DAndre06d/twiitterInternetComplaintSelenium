from complaintSel import InternetSpeedTwitterBot

PROMISED_DOWN= 50
PROMISED_UP = 50

bot = InternetSpeedTwitterBot()
speed = bot.get_internet_speed()
if speed[0] < 50 or speed[1] < 50:
    mess = f"Why is my internet only has downSpeed - {round(speed[0])}, upSpeed - {round(speed[0])} @enjoyGlobe"
    bot.tweet_at_provider(mess)
else:
    print("Your internet speed is good.")

