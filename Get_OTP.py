
from twilio.rest import Client
from db import Update,Read

#Twilio Account SID and Auth Token
account_sid = "ACd3d48576c3e99c34116f716f44e27a91"
auth_token = "3aa615119a25b5c6a216cd76b0305841"

def get_OTP(Mo_No,otp):
    
    # Create a Twilio client
    client = Client(account_sid, auth_token)

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
    except Exception as e:
        print(e)
