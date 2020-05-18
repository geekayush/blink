
# Blink-To-Tell

The purpose of this project is to build a real-time interactive web app that allows paralysed people to easily express themselves, via eye blinks.

## Problem Statement
  
Paralyzed people cannot control muscle function in one or more muscle groups. The condition can be caused by stroke, ALS, multiple sclerosis, and many other diseases. Locked-in Syndrome (LIS) is a form of paralysis where patients have lost control of nearly all voluntary muscles. These people are unable to control any part of their body, besides eye movement and blinking. Due to their condition, these people are unable to talk, text, and communicate in general. Even though people that have LIS are cognitively aware, their thoughts and ideas are locked inside of them. These people depend on eye blinks to communicate. They rely on nurses and caretakers to interpret and decode their blinking. Whenever LIS patients do not have a person to read their eye blinks available, they have no means of self-expression.  

## Objective

- Allow paralysis victims to communicate independently
- Be accessible to people with financial constraints

#### Feautures

- Type with eye blinks

- Recite

- Autocomplete

- Send text through WhatsApp and SMS

- Emergency alert via WhatsApp, SMS and audio siren

## Development

#### Language

- Python

  

#### Tools used

- OpenCV

- PyQt

- Pyttsx

#### Run locally
Prerequisite:
- [Python 3](https://www.python.org/downloads/)

After having the prerequisite installed [create](https://docs.python.org/3/library/venv.html) a virtual environment:

```
python3 -m venv venv
```

Activate the virtual environment:

```
source venv/bin/activate
```

Clone the repository:

```
git clone https://github.com/geekayush/blink.git
```

Get into the project folder:

```
cd blink
```

Install the python modules:

```
pip install -r requirements.txt
```

Configure the project:

```
cp config_template.py config.py
```

Add the values in the configuration file after setting up a project in [Twilio](https://www.twilio.com/):

- **account_sid** is your account's ID
- **auth_token** is your authentication token
- **sms_to** is the number which will receive the SMS
- **sms_from** is the number generated on Twilio for sending SMS
- **whatsapp_to** is the number which will receive the WhatsApp messages
- **whatsapp_from** is the number of Twilio for sending WhatsApp messages

Finally, Run the project:

```
python main.py
```