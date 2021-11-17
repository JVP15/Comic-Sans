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

class ActionUtterComic(Action):
    # Okay, in the future, I can just use the 'tracker.last_intent' to determine what comic is being asked of us so that I don't have to use a bajillion rules 
    def name(self) -> Text:
        return "action_utter_comic"
    
    def open_comic(comic_link):
        global image_display 
        if image_display == 'link':
            dispatcher.utter_message(text=comic_link)
            
        elif image_display == 'chrome':
            os.system(f'start chrome {comic_link}')
            
        elif image_display == 'firefox':
            os.system(f'start firefox {comic_link}')   
            
        elif image_display == 'edge':
            os.system(f'start msedge {comic_link}')
    
    def print_message(message):
        dispatcher.utter_message(text=message)
        
    def run(self, dispatcher, tracker, domain):
        intent = tracker.get_intent_of_latest_message()
        
        if intent is 'nsfw':
            age = tracker.get_slot('age')
            
            if int(age) >= 18:
            
                self.print_message("Don't worry, this is just a demonstration of bot's ability to gather user info and the comic isn't actually NSFW.")
            
                self.open_comic("https://img.buzzfeed.com/buzzfeed-static/static/2019-01/2/16/asset/buzzfeed-prod-web-02/sub-buzz-15566-1546465806-1.jpg")
            
            else:
                dispatcher.utter_message(response="utter_too_young")
        
        elif intent is 'machine_learning':
            
            self.print_message("Here's a comic about machine learning. As an AI based program, I feel like it his a bit too close to home for me.")
            
            self.open_comic("https://xkcd.com/1838/")
        
        elif intent is 'work_life_video_game_balance':
            
            show_dino_comics = tracker.get_slot('show_dinosaur_comics')
            
            if show_dino_comics.lower() is 'true':
            
                self.print_message("Here's a Dinosaur Comic that I bet will match what you are looking for.")
            
                self.open_comic("https://qwantz.com/index.php?comic=3817")
            
            else:
                self.print_message("I was going to send you a Dinosaur Comic, but since you don't like them, I've substituted it for soemthing else.")
            
                self.open_comic("https://www.cakeburger.com/comic/a-healthy-worklife-balance/")
       
        elif intent is 'shoot_for_the_moon': 
            self.print_message("You wanted a comic about motivational speeches right? Well the moon has got your back (in this case, literally)")
            
            self.open_comic("https://xkcd.com/1291/")
        
        elif intent is 'markdown': 
            self.print_message("Personally, I wouldn't use that last text editor.")
            
            self.open_comic("https://xkcd.com/1341/")
            
        elif intent is 'gnu_man_page': 
            self.print_message("This comic is for those who find the Gnu man page as frusterating as I do.")
            
            self.open_comic("https://xkcd.com/912/")
            
        elif intent is 'security': 
            self.print_message("This is another one of XKCD's apt comics about security.")
            
            self.open_comic("https://xkcd.com/538") 
        
        elif intent is 'statisticians': 
            self.print_message("I'll be honest, I don't know what a fat tail is, but hopefully you do.")
            
            self.open_comic("https://www.smbc-comics.com/comic/tail") 
        
        elif intent is 'server_rooms': 
            self.print_message("Hopefully this comic about datacenters is what you are looking for.")
            
            self.open_comic("https://xkcd.com/1439/") 
        
        elif intent is 'unicode': 
            self.print_message("There are plenty more unicode comics where that comes from. This was the closest one I had on hand.")
            
            self.open_comic("https://xkcd.com/1953/") 
       
       
       
       
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
        