from flask import Flask
import socket

app = Flask(__name__)


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't have to be reachable; used to determine outbound IP
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        try:
            ip = socket.gethostbyname(socket.gethostname())
        except Exception:
            ip = "127.0.0.1"
    finally:
        s.close()
    return ip


@app.route("/")
def index():
    hostname = socket.gethostname()
    ip_address = get_ip()
    return f"Hostname: {hostname}<br>IP Address: {ip_address}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
