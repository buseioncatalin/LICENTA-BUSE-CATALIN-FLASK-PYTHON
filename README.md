## Sentiment Analysis on movie reviews using Python
***
For my diploma project, I wanted to develop an application that would help me decide if a movie is worth watching, removing my need to read lots of reviews beforehand.

Since I was already thinking about this specific application as becoming something that would be widely used by people on a daily basis, I wanted it to be easily accessible and user-friendly so I chose to make it a web app, instead of a desktop app with a GUI that I was already familiar with. So in order to fully develop it I had to dabble a bit in Flask. 


***
I can see the app is still online, so you can access and try it here: https://catalin147.eu.pythonanywhere.com/

**input = empty search** => the list of movies you can check

**input = movie name or bits from its name** => the desired result after analysing the reviews
***
In its current state, the application analyses the top rated 10 reviews of a movie using both TextBlob and VaderSentiment, which were, at that time at least, perceived as the best, in order to render a rule-based sentiment analysis of the reviews. Simply put, the app was able to check if some given piece of text(the reviews, in this case) was saying something positive or negative about something(the movies, in this case).
***
When I started this project, it was supposed to have no limitations and work on any movie. Initally, I had built a web scrapper that was used to get the reviews(not all of them since I would cause unnecessary loads on their servers, but at least more than 10) of any movie I wanted to search for on the IMDb platform. 

Unfortunately, shortly after that, I actually read their terms and conditions and I found out that they forbid users to scrap their pages. I even sent them an email explaining that this was actually going to be my diploma project and it was going to be purely academic if they give me access to their API or at least give me the consent to scrap the pages. As you can see, that did not work out and I got stuck with only a handful of movies that I had to manually add to my pseudo-database, a JSON file.
