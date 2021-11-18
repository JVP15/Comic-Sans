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
        return "action_utter_nsfw"
    
    def open_comic(self, dispatcher, comic_link):
        global image_display 
        if image_display == 'link':
            dispatcher.utter_message(text=comic_link)
            
        elif image_display == 'chrome':
            os.system(f'start chrome {comic_link}')
            
        elif image_display == 'firefox':
            os.system(f'start firefox {comic_link}')   
            
        elif image_display == 'edge':
            os.system(f'start msedge {comic_link}')
            
    def run(self, dispatcher, tracker, domain):
        age = tracker.get_slot('age')
        
        if int(age) >= 18:
            dispatcher.utter_message(text="Don't worry, this is just a demonstration of bot's ability to gather user info and the comic isn't actually NSFW. ")
            self.open_comic(dispatcher, "https://img.buzzfeed.com/buzzfeed-static/static/2019-01/2/16/asset/buzzfeed-prod-web-02/sub-buzz-15566-1546465806-1.jpg")
        else:
            dispatcher.utter_message(response="utter_too_young")

        return []
        
        
class ActionUtterComic(Action):
    # Okay, in the future, I can just use the 'tracker.last_intent' to determine what comic is being asked of us so that I don't have to use a bajillion rules 
    def name(self) -> Text:
        return "action_utter_comic"
    
    def open_comic(self, dispatcher, comic_link):
        global image_display 
        if image_display == 'link':
            dispatcher.utter_message(text=comic_link)
            
        elif image_display == 'chrome':
            os.system(f'start chrome {comic_link}')
            
        elif image_display == 'firefox':
            os.system(f'start firefox {comic_link}')   
            
        elif image_display == 'edge':
            os.system(f'start msedge {comic_link}')
    
    def print_message(self, dispatcher, message):
        dispatcher.utter_message(text=message)
        
    def run(self, dispatcher, tracker, domain):
        intent = tracker.get_intent_of_latest_message()
        
        if intent == 'machine_learning':
            self.print_message(dispatcher, "Here's a comic about machine learning. As an AI based program, I feel like it his a bit too close to home for me.")
            
            self.open_comic(dispatcher, "https://xkcd.com/1838/")
        
        elif intent == 'work_life_video_game_balance':
            
            show_dino_comics = tracker.get_slot('show_dinosaur_comics')
            
            if show_dino_comics:
            
                self.print_message(dispatcher, "Here's a Dinosaur Comic that I bet will match what you are looking for.")
            
                self.open_comic(dispatcher, "https://qwantz.com/index.php?comic=3817")
            
            else:
                self.print_message(dispatcher, "I was going to send you a Dinosaur Comic, but since you don't like them, I've substituted it for soemthing else.")
            
                self.open_comic(dispatcher, "https://www.cakeburger.com/comic/a-healthy-worklife-balance/")
       
        elif intent == 'shoot_for_the_moon': 
            self.print_message(dispatcher, "You wanted a comic about motivational speeches right? Well the moon has got your back (in this case, literally)")
            
            self.open_comic(dispatcher, "https://xkcd.com/1291/")
        
        elif intent == 'markdown': 
            self.print_message(dispatcher, "Personally, I wouldn't use that last text editor.")
            
            self.open_comic(dispatcher, "https://xkcd.com/1341/")
            
        elif intent == 'gnu_man_page': 
            self.print_message(dispatcher, "This comic is for those who find the Gnu man page as frusterating as I do.")
            
            self.open_comic(dispatcher, "https://xkcd.com/912/")
            
        elif intent == 'security': 
            self.print_message(dispatcher, "This is another one of XKCD's apt comics about security.")
            
            self.open_comic(dispatcher, "https://xkcd.com/538") 
        
        elif intent =='statisticians': 
            self.print_message(dispatcher, "I'll be honest, I don't know what a fat tail is, but hopefully you do.")
            
            self.open_comic(dispatcher, "https://www.smbc-comics.com/comic/tail") 
        
        elif intent == 'server_rooms': 
            self.print_message(dispatcher, "Hopefully this comic about datacenters is what you are looking for.")
            
            self.open_comic(dispatcher, "https://xkcd.com/1439/") 
        
        elif intent == 'unicode': 
            self.print_message(dispatcher, "There are plenty more unicode comics where that comes from. This was the closest one I had on hand.")
            
            self.open_comic(dispatcher, "https://xkcd.com/1953/") 
       
        return []
       
       
       
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
        