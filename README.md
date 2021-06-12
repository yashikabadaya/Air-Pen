# Air-Pen
# Human Computer Interaction Project
A teach-by-demonstration system which can not only interact with a user by accurately recognizing gestures but also can learn new gestures given few examples and update its understanding of gestures it already knows in an interactive manner.

# Introduction
Efforts are always made to find different methods for convenient human -machine interaction. Gesture recognition is emerging as desirable technology, as it allows more easy way of humans and machine interface. There are two main types of gesture recognition approaches which are getting more focus from researchers, Vision based approach and capture of motion by sensors which is implemented in many new kinds of technologies on Human-Computer Interaction (HCI) these years, such as speech recognition, vision-based gesture recognition and tablet types of devices, and they are much more effective and efficient than the traditional manner. Thus, users could interact with computing devices more freely and directly without keyboards. However, there exist some innate drawbacks in them. For example, it is impolite to communicate with a computer in some quiet public places for speech recognition users, and firmly fixing a camera outside a user is very inconvenient too. As compared to sensor based approach Vision based approach is expensive, needs large data processing and slower dynamic response.
Henceforth, here we present a solution, Air Pen. 

# Aim of the project
We aim to present a gesture recognition system which can interactively recognize gestures and learn new gestures with as few examples. The goal is to make a teach-by-demonstration system which can not only interact with a user by accurately recognizing gestures, but which can learn new gestures and update its understanding of gestures it already knows in an interactive manner. This simplifies the teaching process because it more closely resembles the manner of instruction.

# Working
For character /alphabet recognition due to minute variation and partial similarity in shapes of different alphabets for same user, and there is considerable variation in data for same character if it written by different users, recognition becomes challenging.
For this project, continuous gestures are used. A continuous gesture is a gesture that requires no pauses between each performance and can be performed in continuous fashion. With continuous gestures, it is possible to detect periodicity and form templates.

We have created an app which acts as the user interface. The user trains and tests the model via the app hence making it user friendly. On testing the app with a trained gesture, the recognized gesture is spoken into a Bluetooth set which will be with other person with whom the user desires to direct.
Our concept of interactive training is currently based on the following general procedure:
1. The user trains the app with few examples of a series of gestures.
2. The model learns and finds a threshold point of each gesture.
3. In the testing mode, 
(a) If the test sample achieves a classification within the calculated threshold by the model then it is certain about its classification of a gesture, it immediately performs an action associated with 
that gesture (if one has been specified). Here the recognized gesture is spoken into a Bluetooth set which will be with other person with whom the user desires to direct.
(b) If the test sample doesn’t achieve a classification within the calculated threshold by the model then it’s unsure about its classification of a gesture, it queries the user for conformation of its classification. If that gesture isn’t present in trained samples then user can train the model and hence add new gesture to the vocabulary.
Thereby, this provides the system with a truly interactive character.

# Use Case
1. If we are to fully harness the potential of robotic technology, we will have to move beyond simple keyboard/mouse/teach-pendant style robot programming and create comprehensive frameworks for productive real time interaction between robots and humans. Much effort is being directed toward the research of systems for gesture/observation-based programming of robot systems. Most gesture recognition systems either require some explicit programming, or in the case of neural-nets, require online training of model parameters. Such systems become unsuitable for interactive applications.
For example, a user controlling a robot through the gesture system could perform a gesture which the system has not seen before, and the system would immediately respond by asking what kind of gesture it is. The user could respond that it is a halt" gesture, and that the robot should stop its current motion when that gesture is made. The next time the user performs that gesture, the system should recognize it and immediately halt the motion of the robot.

2. This prototype can be used for recognition of multivariate temporal musical gestures. Musicians commonly use body movements such as hand, arm and head gestures to communicate with other performers live on stage. This method of interaction is still difficult, however, between a musician and a computer it can be used to recognize such gestures.

3. This can also be used as mode of communication between two blind and dumb people who can deliver simple messages to other person by making a gesture with phone which being recognized and spoken in a Bluetooth device with other person thus signaling that person.



