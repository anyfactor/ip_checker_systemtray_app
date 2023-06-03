# IP Checker Systemtray app

- Uses [`pystray`](https://pystray.readthedocs.io/en/latest/index.html) to show an icon of [IPinfo.io](https://ipinfo.io) on the Windows system tray
- If you click on the icone an API call is made to IPinfo. No token needed.
- You can set up VPN detection via IP country. The section is uncommented at line 18. You can also set that using your original IP address.
- Install the requirements via `pip install -r requirements.txt`
- Recommend running the program with `pyw`
- Exit: Left click to get menu and exit.

![IP Checker Systemtray app](./demo.gif)

Thanks to: NeuralNine for their video: [System Tray Icon in Python](https://www.youtube.com/watch?v=BdQOFOyHgfk)