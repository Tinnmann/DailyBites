import bite_content
import ssl #to establish a connection with the gmail server
from email.message import EmailMessage
import smtplib #to send the email
import datetime


class DailyBitesEmail:

    def __init__(self):
        self.content = {
            'news': {'include': True, 'content': bite_content.get_news()},
            'weather': {'include': True, 'content': bite_content.get_forecast()},
            'recipes': {'include': True, 'content': bite_content.get_recipe()}
        }

        # recipients email list. I hid the ones used.
        self.recipients = [
            'abc@example.com', #these are fake emails, please add your own to test
            'def@example.com'
        ]

        #credentials for sender email. I used my own, hidden from here
        self.credentials = {
            'email':'ghi@example.com', # fake credentials, please use own
            'password': 'password'
         }

    def send_email(self):
        message = EmailMessage()
        message['Subject'] = f'Daily Bites - {datetime.date.today().strftime("%d %b %Y")}'
        message['From'] = self.credentials['email']
        message['To'] = ', '.join(self.recipients)

        # add HTML content
        message_body = self.format_message()
    
        message.set_content(message_body['html'], subtype='html')

        # secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
            server.login(self.credentials['email'],
                        self.credentials['password'])
            server.send_message(message)

    def format_message(self):
        # the html 

        html = f"""<html>
    <body>
    <center>
        <h1>Daily Bites - {datetime.date.today().strftime('%d %b %Y')}</h1>
        """

        # format news
        if self.content['news']['include'] and self.content['news']['content']:
            html += f"""
        <h2>Headlines from Fox News</h2>
        <table>
        """
            for headline in self.content['news']['content']:
                html+= f"""

            <tr>
                <td>
                   <a href="{headline['link']}"> {headline['title']}</a>
                </td>
            </tr>   
        </table>
        """

        # format weather forecast
        if self.content['weather']['include'] and self.content['weather']['content']:
            html += f"""
        <h2>Forecast for {self.content['weather']['content']['city']}, {self.content['weather']['content']['country']}</h2> 
        <table>
                    """

            for forecast in self.content['weather']['content']['periods']:
                html += f"""
            <tr>
                <td>
                    {forecast['timestamp'].strftime('%d %b %H%M')}
                </td>
                <td>
                    <img src="{forecast['icon']}">
                </td>
                <td>
                    {forecast['temp']}\u00B0C | {forecast['description']}
                </td>
            </tr>
                        """               

            html += """
        </table>
                    """

        # format recipes
        if self.content['recipes']['include'] and self.content['recipes']['content']:
            html += f"""
        <h2>Daily Food Recipes</h2>
        <h3>Try out something new!</h3>
        <table>
        """
            for recipe in self.content['recipes']['content']:
                html += f"""
            <tr>
                <td><a href="{recipe['url']}">{recipe['name']}</a> Number of servings: {recipe['servings']}</td>
            </tr>
        </table>
                    """

        # footer
        html += """
    </center>
    </body>
</html>
                """

        return {'html': html}

if __name__ == '__main__':
    #test
    email = DailyBitesEmail()

    # test format_message()
    print('\nTesting email body...')
    message = email.format_message()

    # print Plaintext and HTML messages
  
    print('\nHTML email body is...')
    print(message['html'])


    # test send_email()
    print('\nSending test email...')
    email.send_email()