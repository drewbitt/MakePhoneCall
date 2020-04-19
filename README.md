# MakePhoneCall

Make a phone call from an audio clip url with Twilio

Requires python 3

## Usage

Create a file in the project directory called `config.ini` with the following format:

```ini
[DEFAULT]
account_sid = ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
auth_token = your_auth_token
```

Run:

```bash
python main.py --from "+18881001000" -to "+188810010001" --audio_url "http://demo.twilio.com/docs/classic.mp3"
```
