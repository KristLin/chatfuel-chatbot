# Intro:
- A simple dentist chatbot based on RiveScript and Chatfuel.
- This project is just for learning.

# Technology Stack:
- **Python3**
- **Flask**
- **SwaggerDoc**
- **RiveScript**
- **Docker**

# To Deploy
### Build 3 docker images
```
docker build -t chatbot .
docker build -t dentist .
docker build -t timeslot .
```
### Create docker network
``` docker network create my_network ```
### Run containers
```
docker run --name chatbot -p 5000:5000 --network my_network -t chatbot 
docker run --name dentist -p 4000:4000 --network my_network -t dentist 
docker run --name timeslot -p 3000:3000 --network my_network -t timeslot
```
### Test Endpoint
- ***chatbot***:  http://127.0.0.1:5000/static/swagger-ui/index.html
- ***dentist***:  http://127.0.0.1:4000/static/swagger-ui/index.html
- ***timeslot***:  http://127.0.0.1:3000/static/swagger-ui/index.html

# Examples
### Greeting & Basic Conversation
- hi
- hello
- thanks
- thank you
- who are you
- my name is Krist
### Ask Weather
- what is the weather like in Sydney
- how is the weather in Beijing
- weather in London?
### Ask for dentists
- how many dentists are there?
- show me all the dentists
### Ask for dentist's info
- tell me more about jack
- show me the info of wang
### Ask for dentist's available time
- tell me janis available time
- show me jack time
### Book appointment
- can you book jack on 30/03/2020 9-10 for me
- book janis 30/03/2020 10-11
### Cancel appointment
- can you cancel jack on 30/03/2019 9-10 for me
- cancel appointment with id 5558
- cancel appointment 5558

## License

[CC0 1.0 (Public Domain)](LICENSE.md)
