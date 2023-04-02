# # Download the helper library from https://www.twilio.com/docs/python/install
# import os
# from twilio.rest import Client

# # Set environment variables for your credentials
# # Read more at http://twil.io/secure
# account_sid = "AC8f8a230be0ac360c170fb81eba74673e"
# auth_token = "c11104cde487302c517d53d7a195d624"
# verify_sid = "VA0c3c0c754f56c22625c03b1cb47a16a6"
# verified_number = "+996770810003"

# client = Client(account_sid, auth_token)

# verification = client.verify.v2.services(verify_sid) \
#   .verifications \
#   .create(to=verified_number, channel="sms")
# print(verification.status)

# otp_code = input("Please enter the OTP:")

# verification_check = client.verify.v2.services(verify_sid) \
#   .verification_checks \
#   .create(to=verified_number, code=otp_code)
# print(verification_check.status)
# import os
# from twilio.rest import Client

# # Set environment variables for your credentials
# # Read more at http://twil.io/secure
# account_sid = "AC8f8a230be0ac360c170fb81eba74673e"
# auth_token = 'c11104cde487302c517d53d7a195d624'
# verify_sid = "VA0c3c0c754f56c22625c03b1cb47a16a6"
# verified_number = "+996770810003"

# client = Client(account_sid, auth_token)

# verification = client.verify.v2.services(verify_sid) \
#   .verifications \
#   .create(to=verified_number, channel="sms")
# print(verification.status)

# otp_code = input("Please enter the OTP:")

# verification_check = client.verify.v2.services(verify_sid) \
#   .verification_checks \
#   .create(to=verified_number, code=otp_code)
# print(verification_check.status)
# import os
# from twilio.rest import Client

# # Set environment variables for your credentials
# # Read more at http://twil.io/secure
# account_sid = "AC8f8a230be0ac360c170fb81eba74673e"
# auth_token = "c11104cde487302c517d53d7a195d624"
# verify_sid = "VA0c3c0c754f56c22625c03b1cb47a16a6"
# verified_number = "+996770810003"

# client = Client(account_sid, auth_token)

# verification = client.verify.v2.services(verify_sid) \
#   .verifications \
#   .create(to=verified_number, channel="sms")
# print(verification.status)

# otp_code = input("Please enter the OTP:")

# verification_check = client.verify.v2.services(verify_sid) \
#   .verification_checks \
#   .create(to=verified_number, code=otp_code)
# print(verification_check.status)
# import os
# from twilio.rest import Client

# # Set environment variables for your credentials
# # Read more at http://twil.io/secure
# account_sid = "AC8f8a230be0ac360c170fb81eba74673e"
# auth_token = 'c11104cde487302c517d53d7a195d624'
# verify_sid = "VA0c3c0c754f56c22625c03b1cb47a16a6"
# verified_number = "+996770810003"

# client = Client(account_sid, auth_token)

# verification = client.verify.v2.services(verify_sid) \
#   .verifications \
#   .create(to=verified_number, channel="sms")
# print(verification.status)

# otp_code = input("Please enter the OTP:")

# verification_check = client.verify.v2.services(verify_sid) \
#   .verification_checks \
#   .create(to=verified_number, code=otp_code)
# print(verification_check.status)
# import os
# from twilio.rest import Client

# # Set environment variables for your credentials
# # Read more at http://twil.io/secure
# account_sid = "AC8f8a230be0ac360c170fb81eba74673e"
# auth_token = "c11104cde487302c517d53d7a195d624"
# verify_sid = "VA0c3c0c754f56c22625c03b1cb47a16a6"
# verified_number = "+996770810003"

# client = Client(account_sid, auth_token)

# verification = client.verify.v2.services(verify_sid) \
#   .verifications \
#   .create(to=verified_number, channel="sms")
# print(verification.status)

# otp_code = input("Please enter the OTP:")

# verification_check = client.verify.v2.services(verify_sid) \
#   .verification_checks \
#   .create(to=verified_number, code=otp_code)
# print(verification_check.status)
# import os
# from twilio.rest import Client

# # Set environment variables for your credentials
# # Read more at http://twil.io/secure
# account_sid = "AC8f8a230be0ac360c170fb81eba74673e"
# auth_token =  'c11104cde487302c517d53d7a195d624'
# verify_sid = "VA0c3c0c754f56c22625c03b1cb47a16a6"
# verified_number = "+996770810003"

# client = Client(account_sid, auth_token)

# verification = client.verify.v2.services(verify_sid) \
#   .verifications \
#   .create(to=verified_number, channel="sms")
# print(verification.status)

# otp_code = input("Please enter the OTP:")

# verification_check = client.verify.v2.services(verify_sid) \
#   .verification_checks \
#   .create(to=verified_number, code=otp_code)
# print(verification_check.status)


# from twilio.rest import Client

# def send_sms_code(phone_number, verification_code):
  
#     client = Client(account_sid, auth_token)

#     message = client.messages.create(
#         body=f'Код подтверждения: {verification_code}',
#         from_='+996770810003',
#         to=phone_number
#     )

#     print(message.sid)