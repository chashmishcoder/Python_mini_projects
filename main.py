from twilio.rest import Client
import otp_application
import random
import datetime
otp = random.randint(10000,99999)
today = datetime.date.today()


client  = Client(otp_application.account_sid,otp_application.auth_token)

message = client.messages.create(
    body=str(otp)+" is your OTP generated at "+str(today)+ " DO NOT SHARE WITH ANYONE. If not requested by you, call xyz immediately ",
    from_=otp_application.tw_number,
    to=otp_application.my_phone_number


)

print(message.body)
