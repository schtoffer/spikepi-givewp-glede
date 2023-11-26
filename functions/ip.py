import socket

def get_ip_address():
    try:
        # Attempt to connect to an external host to determine the local IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))  # Google's DNS server
        ip_address = s.getsockname()[0]
        s.close()
    except Exception as e:
        ip_address = "Unable to determine IP address: " + str(e)

    return ip_address


