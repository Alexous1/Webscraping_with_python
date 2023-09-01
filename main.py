# import all librairy
import requests
from bs4 import BeautifulSoup
from plyer import notification
import pywhatkit as kit
import datetime

date = datetime.datetime.now()

# get the html code of the page
url = 'https://blox-fruits.fandom.com/wiki/Blox_Fruits_%22Stock%22'
response = requests.get(url)

# create a fruit list
fruit = ['Kilo',
         'Spin',
         'Chop',
         'Spring',
         'Bomb',
         'Smoke',
         'Spike',
         'Flame',
         'Falcon',
         'Ice',
         'Sand',
         'Dark',
         'Revive',
         'Diamond',
         'Light',
         'Rubber',
         'Barrier',
         'Magma',
         'Quake',
         'Buddha',
         'Love',
         'Spider',
         'Phenix',
         'Portal',
         'Rumble',
         'Paw',
         'Blizzard',
         'Gravity',
         'Dough',
         'Shadow',
         'Venom',
         'Control',
         'Spirit',
         'Dragon',
         'Leopard']

# creation of a list with the desired fruit
fruit_like = ['Buddha',
              'Dough',
              'Shadow',
              'Venom',
              'Control',
              'Spirit',
              'Sand',
              'Light',
              'Dragon']

running = True

if response.ok:

    while running:
        links = []
        # get the html code of the page
        soup = BeautifulSoup(response.text, features="html.parser")
        # get a certain balise "table" with a selector css
        table = soup.find('div', attrs= {'id' : "mw-customcollapsible-current"})
        # get all of the span in the table
        title = table.findAll('span')

        # retrieve the span text for each span
        for span in title:
            span_value = span.text

            # test if the span value is equal to the desired fruit
            for test in fruit_like:
                if test == span_value:
                    print(f"le fruit {span_value} est disponible dans la boutique")

                    # setup the variables of time
                    date = datetime.datetime.now()
                    datem = date.minute
                    dateh = date.hour

                    # The line to send a message on WhatsApp must know what time to send it, these lines of code pay
                    # attention to what if the minutes are equal to 59, it changes the time(+ one hour) and minutes (= 0 minute)
                    if datem == 59:
                        datem = 0
                        dateh += 1
                        print(dateh + datem)

                    # add one minute on the variable minute
                    else:
                        datem += 1

                    # send a notification on the laptop
                    notification.notify(title="ALERT!!!", message=f"le fruit {span_value} que vous désirez tant est disponible dans la boutique", timeout=10)
                    # send a message with WhatsApp web to the user
                    kit.sendwhatmsg("", f"le fruit {span_value} que vous désirez tant est disponible dans la boutique", dateh, datem)