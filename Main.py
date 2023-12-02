from sp_engine import greet_user, take_user_input, speak
from online_ops import my_ip, youtube, google_search, wa_msg, tell_a_joke
from offline_ops import say_time, notes, open_application, close_application, set_alarm_in_clock, book_movie, set_reminder_in_calendar, open_calendar_to_date
from datetime import datetime
from dateparser.search import search_dates

if __name__ == '__main__':
    greet_user()
while True:
    query = str(take_user_input()).lower()

    if 'open application' in query:
        speak("Which app would you like to open?")
        app_name = take_user_input().lower()
        result = open_application(app_name)
        speak(result)

    elif 'close application' in query:
        speak("Which application would you like to close?")
        app_name = take_user_input().lower()
        response = (
            close_application(app_name))
        speak(response)

    elif 'ip address' in query:
        ip_address = my_ip()
        speak(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen .')
        print(f'Your IP Address is {ip_address}')

    elif 'youtube' in query:
        speak('What do you want to play on Youtube?')
        video = take_user_input().lower()
        youtube(video)

    elif 'search on google' in query or 'search' in query or 'google' in query:
        speak('What do you want to search on Google?')
        query = take_user_input().lower()
        google_search(query)

    elif "whatsapp" in query:
        speak('To what number should I send the message ? Please enter in the console: ')
        number = input("Enter the whatsapp number: ")
        speak("What is the message?")
        message = take_user_input().lower()
        wa_msg(number, message)
        speak("The message has been sent.")

    elif 'joke' in query:
        speak("Hope you like this one")
        joke = tell_a_joke()
        speak(joke)
        speak("For your convenience, I am printing it on the screen.")
        print(joke)

    elif 'time' in query:
        speak("The time is ")
        speak(say_time())

    elif 'take a note' in query or 'note down' in query or 'write this down' in query:
        speak('What would you like me to write in the note?')
        note_content = take_user_input()
        notes(note_content)
        speak("I have taken down the note for you.")

    elif 'set alarm' in query:
        speak("Please type the alarm time in HH:MM AM/PM format and press Enter.")
        alarm_time_input = input("Alarm Time: ")
        try:
            # Attempt to parse the input as time
            alarm_time = datetime.strptime(alarm_time_input, "%I:%M %p")
            # Set the alarm in Clock app and open Clock
            set_alarm_in_clock(alarm_time)
        except ValueError:
            speak("Sorry, I couldn't understand the time format. Please try again.")

    elif 'set reminder' in query or 'create event' in query or 'schedule event' in query:
        speak("What date should I set the reminder for?")
        date_input = take_user_input().lower()  # Get the date as spoken input
        speak("What would you like the reminder to say?")
        reminder_description = take_user_input()  # Get the reminder description as spoken input
        response = set_reminder_in_calendar(date_input, reminder_description)
        speak(response)

    elif 'book movie' in query or 'movie' in query:
        speak("Sure, which movie would you like to book?")
        movie_name = take_user_input()
        book_movie(movie_name)

