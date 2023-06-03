import pystray
import PIL.Image
import requests
import time

image = PIL.Image.open("icon.png")

def exit_program(icon, item):
    icon.stop()
    exit()

def check_ip(icon, item):
    print("Checking IP")
    r = requests.get('https://ipinfo.io/json').json()
    vpn_status = ""
    # Uncomment this section and add your original country. The country code format: https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2
    # if r['country'] != "JP":
    #     vpn_status = "VPN On!!"
    # else:
    #     vpn_status = "VPN Off!!"
    message = f"{vpn_status}\nIP: {r['ip']}\nLocation: {r['city']}, {r['region']}, {r['country']}"
    icon.notify(message)
    time.sleep(5)
    icon.remove_notification()
    

icon = pystray.Icon(
    "IPinfo", image, menu=pystray.Menu(
                        pystray.MenuItem(text="Check IP",action=check_ip,default=True),
                        pystray.MenuItem(text="Exit", action=exit_program)
                    )
)

icon.run()