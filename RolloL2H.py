import socket
import argparse

def send_command(mac, state, relay, broadcast_ip, port):
    """Send a command to the Link2Home socket via UDP."""
    command_prefix = "a104"
    command_suffix = {
        1: "000901f202d171500101",
        2: "000901f202d171500102"
    }
    state_codes = {
        'up': 'FF',
        'down': '00',
        'stop': '02'
    }

    command = f"{command_prefix}{mac}{command_suffix[relay]}{state_codes[state]}"
    message = bytes.fromhex(command)
    
    # Set up the socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.sendto(message, (broadcast_ip, port))
        print(f"Command sent to {mac}: {state}")

def main():
    # Command line arguments parsing
    parser = argparse.ArgumentParser(description="Control Link2Home Sockets")
    parser.add_argument('-p', action="store",dest="relayport")
    parser.add_argument('-i', action="store",dest="relayip")
    parser.add_argument('-m', action="store",dest="relaymac")
    parser.add_argument("state", choices=["up", "down", "stop"], help="State of the relay (up/down/stop)")
    args = parser.parse_args()

    port = 35932
    channel = 1
    
    send_command(args.relaymac, args.state, channel, args.relayip, port)
    
if __name__ == "__main__":
    main()
