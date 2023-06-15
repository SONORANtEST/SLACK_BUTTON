from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from tkinter import Tk, Button
from dotenv import load_dotenv # import load_dotenv function
import os # import os module

load_dotenv() # load environment variables

token = os.environ["TOKEN"] # get token from environment variable
client = WebClient(token=token)


def set_slack_status(status_text, status_emoji):
    try:
        response = client.users_profile_set(
            profile={
                "status_text": status_text,
                "status_emoji": status_emoji,
            }
        )
        if response["ok"]:
            print("Slack status updated successfully!")
        else:
            print("Failed to update Slack status.")
    except SlackApiError as e:
        print(f"Error updating Slack status: {e.response['error']}")

def set_status_available():
    set_slack_status("Available", ":phone:")

def set_status_lunch():
    set_slack_status("Lunch", ":sandwich:")

def set_status_available_remotely():
    set_slack_status("Available Remotely", ":house_with_garden:")

def set_status_bathroom():
    set_slack_status("Bathroom", ":toilet:")  # You can replace ":toilet:" with the correct emoji

def set_status_Working_In_Warehouse():
    set_slack_status("Working In Warehouse", ":department_store:")

# GUI setup
root = Tk()
root.geometry('300x200')

b1 = Button(root, text="Available", command=set_status_available)
b1.pack()

b2 = Button(root, text="Lunch", command=set_status_lunch)
b2.pack()

b3 = Button(root, text="Available Remotely", command=set_status_available_remotely)
b3.pack()

b4 = Button(root, text="Restroom", command=set_status_bathroom)
b4.pack()

b5 = Button(root, text="Working In Warehouse", command=set_status_Working_In_Warehouse)
b5.pack()

root.mainloop()
