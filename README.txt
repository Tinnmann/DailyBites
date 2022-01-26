About the DailyBites app:

This Python application automates the retrieval and sending of some small daily tasks carried out whenever I browse the internet.
It collects news headlines by webscraping one of the news sites I frequent, uses the Openweathermap api to get the weather forecast 
for every 3 hours over the next 24 hours, and selects some food recipes I may be interested to try out, using the Tasty API. Once the
information has been retrieved, it emails it to an email address of my choosing. In order to successfully schedule a daily email from 
the app, a scheduling class was created to run on a separate thread from the main thread. Also, this daily emailing will only happen 
as long as the Python application is left running in the background.

How To Use:
 ** Before you can run the script on your own local environment, you need to register an acount and obtain an api key from each of the following:
 - Openweathermap.org
 - rapidapi.com(for the tasty api)

 Once you have obtined these private keys, add the first one to line 29 where it says "api_key", and the second to line 55 next to "x-rapidapi-key"

 Lastly, run the bite_gui.py file and the admin gui will pop up. This means the application is working and you can now select which content you would
 like to have included, which email to send from and what emails will receive the message, as well as the daily recurring time for this to happen. When
 complete, you simply click on the Update Settings button. The app also allows you to send the message manually if you would like to do that immediately. 