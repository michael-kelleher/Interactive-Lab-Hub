from pushsafer import Client
import base64

encoded = base64.b64encode(open("Images/img2.png", "rb").read()).decode('ascii')
encoded = 'data:image/png;base64,{}'.format(encoded)
print(encoded)
client = Client("0zStwJjFb4kOA08KxMe1")
resp = client.send_message("Mess Detected", "It may be time for some cleaning", "58896", "136", "48", "2", "", "", "0", "2", "60", "600", "1", encoded, "")
print(resp)

