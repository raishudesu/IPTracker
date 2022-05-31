import tkinter as tk
import requests

HEIGHT = 700
WIDTH = 500
font = 'Arial', 18

api = "http://ip-api.com/json/"


def format_response(coordinates):
    try:
        country = coordinates['country']
        region_name = coordinates['regionName']
        city = coordinates['city']
        zip = coordinates['zip']
        lat = coordinates['lat']
        lon = coordinates['lon']
        time_zone = coordinates['timezone']
        isp = coordinates['isp']

        final_str = 'Country: %s \nRegion Name: %s \nCity: %s \nZip Code: %s \nLatitude: %s\nLongitude: %s ' \
                    '\nTime zone: %s \nISP: %s' % (country, region_name, city, zip, lat, lon, time_zone, isp)
    except:
        final_str = 'Invalid IP or Host Name'

    return final_str


def get_ip(int_prot):
    url = api + int_prot
    response = requests.get(url)
    coordinates = response.json()


    label1['text'] = format_response(coordinates)


app = tk.Tk()
app.title("IP Tracker")

canvas = tk.Canvas(app, height=HEIGHT, width=WIDTH)
canvas.pack()

bg_image = tk.PhotoImage(file='abstract-technology-binary-code-background-digital-binary-data-secure-data-concept_139523-236.png')
bg_label = tk.Label(app, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

label = tk.Label(app, text='Internet Protocol Tracker', bg='black', font=('arial', 12), foreground='green')
label.place(relx=0.5, relwidth=0.75, relheight=0.1, anchor='n')

lower_label = tk.Label(app, text='Enter the IP Address e.g. 157.240.22.35', bg='#003300', font=('arial', 12), foreground='white')
lower_label.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.05, anchor='n')

frame = tk.Frame(app, bg='black', bd=5)
frame.place(relx=0.5, rely=0.15, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=12, bg='light gray')
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Track", font=('arial', 12), bg='light gray', command=lambda: get_ip(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(app, bg='#003300', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label1 = tk.Label(lower_frame, bg='black', font=('arial', 12), foreground='white')
label1.place(relwidth=1, relheight=1)

app.bind('<Return>', lambda event: get_ip(entry.get()))

app.mainloop()