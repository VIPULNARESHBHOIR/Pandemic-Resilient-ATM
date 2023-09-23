
from twilio.rest import Client
import random
from db import Update,Read


# Your Twilio Account SID and Auth Token
account_sid = "ACd3d48576c3e99c34116f716f44e27a91"
auth_token = "b1c0417c859ae876cbff7820dbb5927d"

def get_OTP(Mo_No):
    Mo_No="7057997137"
    # Create a Twilio client
    client = Client(account_sid, auth_token)

    # Generate a random 6-digit OTP
    otp = ''.join(random.choices('0123456789', k=6))

    # The recipient's phone number (in E.164 format)
    recipient_phone_number = "+91"+str(Mo_No)  # Replace with the recipient's actual phone number

    # Message to send
    message_body = f"Your one time OTP is: {otp}"

    # Send the OTP
    try:
        message = client.messages.create(
        to=recipient_phone_number,
        from_="+14055637844",  # Replace with your Twilio phone number
        body=message_body
        )
        print(f"OTP sent to {recipient_phone_number}")
        return otp
    except:
        print("Conn. err")

