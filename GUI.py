from tkinter import *
import requests

API = 'https://www.trackcorona.live/api/countries'


def init_values():
    data['country'].set('INDIA')
    data['confirmed'].set('N/A')
    data['dead'].set('N/A')
    data['recovered'].set('N/A')


def get_country_number(country_name, received_data):
    number = 0
    for data in received_data['data']:
        if country_name == data['location']:
            # print(data)
            return number
        number += 1


def get_data():
    print('Fetching Data..... Please be patient...')
    covid_data = requests.get(API).json()
    country_name = 'India'
    country_num = get_country_number(country_name, covid_data)
    data['confirmed'].set(covid_data['data'][country_num]['confirmed'])
    data['dead'].set(covid_data['data'][country_num]['dead'])
    data['recovered'].set(covid_data['data'][country_num]['recovered'])


# -- GUI ---
root = Tk()
root.title("World Covid Cases")
root.geometry("480x234")
root.maxsize(480,234)
root.minsize(480,234)

root.iconbitmap('virus.ico')

# Constant Lables
Label(root, text='COVID CASES', font='Comicsansms 16 bold',pady=5).grid(row=0, pady=5)
Label(root, text='Country :', font='Comicsansms 13').grid(row=1, column=0)
Label(root, text='Confirmed : ', font='Comicsansms 13').grid(row=2, column=0)
Label(root, text='Dead : ', font='Comicsansms 13').grid(row=3, column=0)
Label(root, text='Recovered : ', font='Comicsansms 13').grid(row=4, column=0)

# tkinter variables
data = {
    'country': StringVar(),
    'confirmed': StringVar(),
    'dead': StringVar(),
    'recovered': StringVar(),
}

init_values()

# Entry for Country Name
Entry(root, textvariable=data['country'], font='Comicsansms 13').grid(row=1, column=1)

# updating Labels
# Label(root, textvariable=data['country'], font='Comicsansms 13').grid(row=1, column=1)
Label(root, textvariable=data['confirmed'], font='Comicsansms 13').grid(row=2, column=1)
Label(root, textvariable=data['dead'], font='Comicsansms 13').grid(row=3, column=1)
Label(root, textvariable=data['recovered'], font='Comicsansms 13').grid(row=4, column=1)


# Button
Button(root, text="Fetch Data", command=get_data,
       padx=5, pady=5).grid(row=5, column=3)

root.mainloop()
