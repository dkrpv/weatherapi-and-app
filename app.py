import weatherapi as api
import time
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.core.window import Window
from kivy.uix.image import Image


def getState():
    city = "Tampere"
    kelvin = api.weather(city, "temp")
    temp = api.toCelsius(kelvin, "kelvin")
    temp = round(temp)
    mytime = time.localtime()
    if mytime.tm_hour > 16:
        wimg = Image(source='night.png')
    elif temp >= 10:
        wimg = Image(source='sunny.png')
    else:
        wimg = Image(source='notsunny.png')
    return wimg


class WeatherPage(AnchorLayout):
    def __init__(self, **kwargs):
        super(WeatherPage, self).__init__(**kwargs)
        with self.canvas.before:
            Window.clearcolor = (1, 1, 1, 1)
        city = "Tampere"
        kelvin = api.weather(city, "temp")
        temp = api.toCelsius(kelvin, "kelvin")
        temp = round(temp)
        wimg = getState()
        self.add_widget(wimg)
        self.add_widget(Label(text=f'{temp} °C', font_size='50sp'))
        self.add_widget(Label(text=f'\n\n{city}', font_size='30sp'))


class MyApp(App):
    def build(self):
        return WeatherPage()


if __name__ == '__main__':
    MyApp().run()
