import midtransclient
from user.models.User import Users
import requests
import base64

server_key = "SB-Mid-server-dY0SSXtJamUYuoMTM2Uy3fr7"
# Create Snap API instance
snap = midtransclient.Snap(
    # Set to true if you want Production Environment (accept real transaction).
    is_production=False,
    server_key=server_key
)
# Build API parameter

def midtrans(request, gross_amount, order_id):
    param = {
        "transaction_details": {
            "order_id": order_id,
            "gross_amount": gross_amount
        }, "credit_card":{
            "secure" : True
        }, "customer_details":{
            "first_name": request.user.first_name,
            "last_name": request.user.last_name,
            "email": request.user.email,
            "phone": Users.objects.get(user=request.user).phone
        }
    }

    transaction = snap.create_transaction(param)
    return transaction['redirect_url'], transaction['token']

def status(order_id):
# Encode the authentication string in Base64
    auth_string = base64.b64encode(f"{server_key}:".encode()).decode()

    # Set the API endpoint URL
    url = f'https://api.sandbox.midtrans.com/v2/{order_id}/status'  # Replace with your actual API endpoint

    # Set the headers
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Basic {auth_string}"
    }

    # Make the HTTP request
    response = requests.get(url, headers=headers)

    # Print the response
    return response.json()
