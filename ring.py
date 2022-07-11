import json
import os
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Optional

from pyicloud import PyiCloudService


def ring(icloud_id: str, icloud_password: str, device_name: Optional[str] = None):
    api = PyiCloudService(icloud_id, icloud_password)

    if device_name is None:
        device = api.iphone
    else:
        devices = {_.data['name']: _ for _ in api.devices.values()}
        try:
            device = devices[device_name]
        except KeyError:
            raise KeyError(f"No device named {device_name!r}. Found devices: {devices}")

    device.play_sound()


def main():
    icloud_id = os.getenv("icloud_id")
    icloud_password = os.getenv("icloud_password")
    device_name = os.getenv("device_name")
    if icloud_id is None or icloud_password is None:
        raise ValueError("Env variables 'icloud_id' or 'icloud_password' not set.")
    ring(icloud_id, icloud_password, device_name)


def serve(port: int):
    host = ('0.0.0.0', port)

    class Resquest(BaseHTTPRequestHandler):
        def do_GET(self):
            try:
                main()
            except Exception as e:
                self.send_response(500)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(f"{e}\n".encode())
            else:
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                data = {'result': 'Rung.'}
                self.wfile.write(json.dumps(data).encode())

    server = HTTPServer(host, Resquest)
    print("Starting ring-me-up server, listen at: %s:%s" % host)
    server.serve_forever()


def cli():
    args = sys.argv[1:]
    if len(args) == 0:
        main()
    else:
        if args[0] == "serve":
            try:
                port = int(args[1])
            except IndexError:
                port = 80
            serve(port)
        else:
            raise ValueError("invalid args")


if __name__ == "__main__":
    cli()
