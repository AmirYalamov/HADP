# Hackers Against Dumb Posts (HADP)

## Abstract

Social media presence and public image is **huge** these days.

Everyone is familiar with the incident of the twitter NASA girl who lost her internship due to vulgar and inappropriate tweets:
<br/>
<p align="center">
  <img width="412.1" height="370.5" src="https://i.dailymail.co.uk/i/newpix/2018/08/23/10/4F5352F900000578-6090055-image-m-9_1535017175115.jpg">
</p>

This could have easily been avoided if she took a moment to think about what she was posting. And this was not the only instance of a dumb post our team has seen. "Why isn't there anything to prevent this?" we thought. Thus the idea for Hackers Against Dumb Posts (HADP) was born.

HADP is an assistant that uses machine learning and sentiment analysis to advise people on their social media postings.

## Tech Stack

We created an android keyboard Gradle build that connects to our **REST API** (built with **Flask** and **PyTorch**). The API connects to our sentiment analysis algorithm and machine learning classifier. We also made an image recognition program using the **Clarifai API** to warn users about potentially controversial images they might be posting, which also uses our sentiment analysis program. The machine learning classifier is built with **Keras**, **Pandas** and **Tensorflow** and essentially it scrapes weekly top headlines to find potential controversial topics.

## Future of the Project

This project is fully functional, which is often a rarity when it comes to hackathon projects.

In the future we want to deploy machine learning into our project in order to more accurately analyse posts and media.

