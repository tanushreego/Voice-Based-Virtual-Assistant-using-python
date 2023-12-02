import subprocess as sbp
from datetime import datetime
import dateparser
from movie_database import movie_database
from sp_engine import speak, take_user_input


def open_application(app_name):
    try:
        sbp.run(['open', '-a', app_name])
        return f"Opening {app_name}."
    except Exception as e:
        print(e)  # Print the error for debugging purposes
        return f"Sorry, either the application '{app_name}' does not exist or you provided an incorrect name."


def close_application(app_name):
    try:
        sbp.run(['osascript', '-e', f'tell application "{app_name}" to quit'])
        return f"Closing {app_name}."
    except Exception as e:
        print(e)  # Print the error for debugging purposes
        return f"Sorry, either the application '{app_name}' is not running or you provided an incorrect name."


def say_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    return current_time


def notes(note_content):
    # AppleScript to create a new note with the provided content
    applescript_code = f'tell application "Notes" to tell account "iCloud"\n' \
                       f'    make new note with properties {{body:"{note_content}"}}\n' \
                       f'end tell'

    # Execute the AppleScript code to create a new note with the provided content
    sbp.run('open -a "Notes"', shell=True)


def set_alarm_in_clock(alarm_time):
    # Format the alarm time as required by Clock app (HH:MM AM/PM format)
    formatted_time = alarm_time.strftime("%I:%M %p")
    # Set the alarm using AppleScript
    sbp.run(f'osascript -e \'tell application "Clock" to open\'', shell=True)
    sbp.run(f'osascript -e \'tell application "System Events" to tell process "Clock" '
            f'to click button 3 of window 1\'', shell=True)  # Click the "Alarm" tab
    sbp.run(f'osascript -e \'tell application "System Events" to tell process "Clock" '
            f'to click button 2 of scroll area 1 of window 1\'', shell=True)  # Click the "Edit" button
    sbp.run(f'osascript -e \'tell application "System Events" to tell process "Clock" '
            f'to set value of text field 1 of group 2 of window 1 to "{formatted_time}"\'',
            shell=True)  # Set the alarm time
    sbp.run(f'osascript -e \'tell application "System Events" to tell process "Clock" '
            f'to click button 1 of group 1 of window 1\'', shell=True)  # Click the "Save" button
    sbp.run(f'osascript -e \'tell application "Clock" to activate\'',  shell=True)


def set_reminder_in_calendar(reminder_date_text, reminder_description, calendar_name="Home"):  # Default calendar name is "Home", change as needed
    # Parse the date from the reminder text
    date = dateparser.parse(reminder_date_text, settings={'PREFER_DATES_FROM': 'future'})
    if not date:
        return "Sorry, I couldn't understand the date."

    # Format the date as required by the Calendar app
    formatted_date = date.strftime("%Y-%m-%d")  # Format changed to YYYY-MM-DD for AppleScript

    # AppleScript command to create a new event on the given date with the given description
    applescript_command = f'''
    tell application "Calendar"
        tell calendar "{calendar_name}"
            make new event at end with properties {{summary:"{reminder_description}", start date:date "{formatted_date}", end date:date "{formatted_date}"}} 
        end tell
    end tell
    '''

    try:
        # Run the AppleScript command to create a new reminder
        sbp.run(['osascript', '-e', applescript_command])
        # Open the Calendar app to the specified date
        sbp.run(f'open -a Calendar "ical://?view=c&date={formatted_date}"', shell=True)
        return f"Reminder for '{reminder_description}' set for {date.strftime('%B %d, %Y')} and Calendar opened."
    except Exception as e:
        return f"An error occurred while setting the reminder: {e}"


def open_calendar_to_date(event_date):
    # Format the event date as required by Calendar (assuming MM/DD/YYYY format)
    formatted_date = event_date.strftime("%m/%d/%Y")

    # Open Calendar app and navigate to the specified date
    sbp.run(f'open -a Calendar "calshow:{formatted_date}"', shell=True)


def show_movie_details(movie_name):
    for category, movies in movie_database.items():
        for movie in movies:
            if movie['name'].lower() == movie_name.lower():
                print(f"Details for {movie_name}:")
                print(f"Category: {category.capitalize()}")
                print(f"theater: {movie['theater']}")
                print(f"Timing: {movie['timing']}")
                speak(f"Details for {movie_name}:")
                speak(f"Category: {category.capitalize()}")
                speak(f"theater: {movie['theater']}")
                speak(f"Timing: {movie['timing']}")
                return True
    speak(f"Sorry, {movie_name} details not found.")
    return False


def book_movie(movie_name):
    if show_movie_details(movie_name):
        speak("Do you want to book tickets for this movie?")
        user_response = take_user_input().lower()
        if 'yes' in user_response or 'yeah' in user_response or 'go ahead' in user_response:
            print(f"Booking confirmed for {movie_name}. Enjoy your movie!")
            speak(f"Booking confirmed for {movie_name}. Enjoy your movie!")
        else:
            speak("Booking canceled.")
    else:
        speak("Cannot proceed with the booking. Movie details not found.")