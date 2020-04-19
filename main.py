# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import configparser
import argparse

def main(audio_url, toNumber, fromNumber):
    config = configparser.ConfigParser()
    config.read('config.ini')

    # Your Account Sid and Auth Token from twilio.com/console
    # DANGER! This is insecure. See http://twil.io/secure
    account_sid = config['DEFAULT']['account_sid']
    auth_token = config['DEFAULT']['auth_token']
    client = Client(account_sid, auth_token)

    call = client.calls.create(
                            twiml='''<Response>
    <Play>{}</Play>
    </Response>'''.format(audio_url),
                            to=toNumber,
                            from_=fromNumber
                        )

    print(call.sid)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Make a call from audio using Twilio')
    parser.add_argument('--audio_url', help='Url to audio file', required=True)
    parser.add_argument('--to', help='Phone number to call', required=True)
    parser.add_argument('--from', dest='fromNumber', help='Phone number the call comes from', required=True)

    args = parser.parse_args()

    main(args.audio_url, args.to, args.fromNumber)