# Comic-Sans
Comic Sans is here to help you find the right comic for every situation. The intent is that you describe a situation and Comic Sans provides a comic that is related to the description you gave. Currently, it supports 10 different situations. More information about it can be found in the Comic Queries section of this document. 

## Running the chatbot


### Create Virtual Env
``` 
python3 -m venv ./venv
```

### Activate Virtual Env
If you are on Windows, you should use:
```
.\venv\Scripts\activate
```

If you are on Linux or Mac, you should use the following command:
```
source ./venv/bin/activate
```

### Dependencies
The only dependancy for this project is Rasa version 2.8.12. If you are on Windows like I am, then you may encounter some error messages installing Rasa. I haven't discovered any problems that arose because of those errors. 
```
pip3 install rasa==2.8.12
```

### Start Actions Server
Before interacting with Comic Sans, you must run the action server. I recommend running it in a different console than the one that you'll use to interact with Comic Sans. 
```
rasa run actions
```

### Run the interactive Shell
```
rasa shell
```


## Comic Queries

Comic Sans currently 10 comics for 10 different situations, so go ahead and ask for a comic about:

* machine learning
* work/life balance
* shooting for the moon
* the gnu manual
* text editors
* security
* statisticians
* server rooms/datacenters
* unicode
* nsfw (It's not actually nsfw, but it will show off the age verification feature)

For example, you may say: 'Give me a comic about machine learning'

## Viewing Comics

Typically, Comic Sans will provide a link to each comic in the shell window. However, Comic Sans can open a comic automatically in the browser of your choice (currently only supports Chrome, Firefox, and Edge). Simply tell Comic Sans which browser you would like to use by saying something like 'I want to use Google Chrome'


## Riddles 

Comic Sans also likes to tell riddles (well, one riddle really), so ask Comic Sans to ask you a riddle! If you don't get it, Comic Sans will explain it to you. The conversation may look like:

- User:  Ask me a riddle
- Comic Sans: So you want a riddle huh? Well here you go. Judi's parents have 4 kids. Their first is named Carter, their second is named Tiffany, and their third one is named Andrew. What is the name of their 4th kid? 
- User: I don't know
- Comic Sans: <explains the riddle>
- User: I understand now
- Comic Sans: That's great!

## Dinosaur Comics

Dinosaur Comics, by Ryan North, are beloved by Comic Sans, but they aren't for everyone. If you don't like Dinosaur Comics, let Comic Sans know but be sure to explain yourself. Comic Sans requires a good explanation, like hating Ryan North for kicking your dog (are you sure it was Ryan North? He seems like such a nice guy), and if you give a suitable explanation, it'll take your feelings into account when sending you comics. 

A sample conversation may look like:

- User:  I don't like dinosaur comics
- Comic Sans: What, you don't like Dinosaur Comics? Why not?
- User: I'm afraid of dinosaurs
- Comic Sans: Well, I've lived in constant fear of being attacked by a Velociraptor, so I understand. I won't send you any more Dinosaur Comics. 
