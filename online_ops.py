import pywhatkit as kit
import speech_recognition as sr
import requests
import webbrowser
import urllib.parse
from sp_engine import take_user_input, speak


def my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]


def youtube(video):
    kit.playonyt(video)


def google_search(query):
    kit.search(query)


def wa_msg(number, message):
    kit.sendwhatmsg_instantly(f"+91{number}", message)


def tell_a_joke():
    headers = {
        'Accept': 'application/json'
    }
    result = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return result["joke"]

