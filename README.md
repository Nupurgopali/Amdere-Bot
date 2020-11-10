# Inspiration
Depression is a common mental disorder. Globally, more than 264 million people of all ages suffer from depression. It is a leading cause of disability worldwide. Especially in this current pandemic, the rate of depression and anxiety has increased exponentially. At present, it is even difficult to attend physical therapy. This motivated us to create a bot that can not only answer trivia but is also trained to answer questions related to depression and will help people suffering from depression and anxiety. Not only this it can even aid the suicide helplines by talking to the person until one of their workers is free to attend the call.

# What it does
It brings positivity to a depressed person's life by giving him/her the assurance that he longs for. Often people have tried to reach out to their friends and family to overcome this disorder but they fear being judged and abstain from letting out their thoughts. This bot provides a way for the user to talk their mind out in a one to one session where there is no fear of judgment since the user remains completely anonymous and no data whatsoever about them is stored. It answers all the technical doubts related to depression and even suggests ways the user can control their anxiety. It even tries to cheer the user by sending messages of hope.

# How we built it
We used web-scraping tools such as beautiful soup to procure data and even used twitter's sentiment analysis data to analyze the most common words used by depressed persons. Once the data was ready and converted to a .yml file we further preprocessed the data in order to make it ready for training, we converted all the text into lowercase and removed the punctuation marks we then build a sequence-to-sequence lstm model using TensorFlow and Keras ( build encoder and decoder model). Then we trained the model on our data and then tested it.To deploy the model we build a website using HTML, CSS, js and the backend was build using flask.

# Challenges we ran into
The main challenge we ran into was for procuring data since there is no data readily available online about how a depressed person talks, we had to search a lot and build the data with correct answers. Then the next challenge was building a sequence to sequence model that could predict the answer for a given question. After several tries, we were able to create a model with decent training accuracy(93%).

# What's next for Amdere Bot
Any human being would love to have a personal touch when they are on the receiving end of answers, our main aim will be to train the bot to store some data that the user shares during the session and answer the upcoming questions accordingly. Apart from that if a user really likes chatting with the bot, we aim to create user profiles, to allow the bot to store some data about them through which the sessions can get more interactive. Amdere bot needs to be provided as a safe space to its users so securing the collected data will be the top priority after storing it. The bot currently lacks the ability to play music and videos for the user, with that added feature the User experience can be enhanced. Broader research on Depression needs to be performed to be able to help the users better. Presently the bot can answer limited questions, with added research it will be able to answer a wide variety of questions. A multi-language feature needs to be added to enhance functionality.

# DEMO

![WhatsApp Video 2020-11-08 at 10 04 34 PM (1)](https://user-images.githubusercontent.com/53776611/98711003-6de3f300-23aa-11eb-8d2f-6ffb2ed87e15.gif)

