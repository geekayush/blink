import config
from twilio.rest import Client


def send(msg):
    account_sid = config.account_sid
    auth_token = config.auth_token
    to = "whatsapp:" + config.whatsapp_to
    from_ = "whatsapp:" + config.whatsapp_from
    if not msg:
        msg = "Get a check on him!"
    client = Client(account_sid, auth_token)
    if msg:
        client.messages.create(
            to=to,
            from_=from_,
            body=msg)
