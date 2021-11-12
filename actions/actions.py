# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

import os
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

# This is a global variable. 
# I know its not the best coding practice, but I keep getting an error if I don't make it global in each function
image_display = 'link'

class ActionShowNSFW(Action):

    def name(self) -> Text:
        return "action_show_nsfw"

    def run(self, dispatcher, tracker, domain):
        age = tracker.get_slot('age')
        
        if int(age) >= 18:
            dispatcher.utter_message(text="Don't worry, this is just a demonstration of bot's ability to gather user info and the comic isn't actually NSFW. ")
            dispatcher.utter_message(image="https://img.buzzfeed.com/buzzfeed-static/static/2019-01/2/16/asset/buzzfeed-prod-web-02/sub-buzz-15566-1546465806-1.jpg")
        else:
            dispatcher.utter_message(response="utter_too_young")

        return []

class ActionShowComic(Action):
    
    def name(self) -> Text:
        return "action_utter_comic"
        
    def run(self, dispatcher, tracker, domain):
        comic_link = 'https://imgs.xkcd.com/comics/egg_drop_failure.png'
        
        dispatcher.utter_message(response="utter_comic")
        
        global image_display 
        if image_display == 'link':
            dispatcher.utter_message(text=comic_link)
            
        elif image_display == 'chrome':
            os.system(f'start chrome {comic_link}')
            
        elif image_display == 'firefox':
            os.system(f'start firefox {comic_link}')   
            
        elif image_display == 'edge':
            os.system(f'start msedge {comic_link}')            
       
       
       
       
       
       
       
class ActionUseChrome(Action):
    def name(self) -> Text:
        return "action_use_chrome"
        
    def run(self, dispatcher, tracker, domain):
        global image_display
        if image_display == 'chrome':
            dispatcher.utter_message(text="You are already using Google Chrome. Nothing has changed.")
        else:
            image_display = 'chrome'
            dispatcher.utter_message(text="Alright, now comics will automatically open up in Google Chrome (you can change this at any time).")
            
class ActionUseFirefox(Action):
    def name(self) -> Text:
        return "action_use_firefox"
        
    def run(self, dispatcher, tracker, domain):
        global image_display
        if image_display == 'firefox':
            dispatcher.utter_message(text="You are already using Firefox. Nothing has changed.")
        else:
            image_display = 'firefox'
            dispatcher.utter_message(text="Alright, now comics will automatically open up in Firefox (you can change this at any time).")
            
class ActionUseEdge(Action):
    def name(self) -> Text:
        return "action_use_edge"
        
    def run(self, dispatcher, tracker, domain):
        global image_display
        if image_display == 'edge':
            dispatcher.utter_message(text="You are already using Microsoft Edge. Nothing has changed.")
        else:
            image_display = 'edge'
            dispatcher.utter_message(text="Alright, now comics will automatically open up in Microsoft Edge (you can change this at any time).")
            
class ActionUseLink(Action):
    def name(self) -> Text:
        return "action_use_link"
        
    def run(self, dispatcher, tracker, domain):
        global image_display
        if image_display == 'link':
            dispatcher.utter_message(text="I am already giving you a link to each comic. Nothing has changed.")
        else:
            image_display = 'link'
            dispatcher.utter_message(text="Alright, now I'll give you the link to each comic in the chat here (you can change this at any time).") 
        