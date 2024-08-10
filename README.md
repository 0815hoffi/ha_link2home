## Installation

### Manual installation

- Copy RolloL2H.py to /config folder of Homeassistant.
- set permissions   #chmod 766 RolloL2H.py 
-
  -rwxrw-rw-    1 1000     users         1351 Aug 10 06:55 RolloL2H.py

- Add to configuration.yaml and change IP-Addr and MAC_Addr to your device ( Get it from your router )

```
  command_line:
  - cover:
      name: RolloTisch
      unique_id: rollotisch
      command_open: python3 /config/RolloL2H.py -i "IP-Addr" -m "MAC_Addr" up
      command_close: python3 /config/RolloL2H.py -i "IP-Addr" -m "MAC_Addr" down
      command_stop: python3 /config/RolloL2H.py -i "IP-Addr" -m "MAC_Addr" stop
```
- Example
```
  command_line:
  - cover:
      name: RolloTisch
      unique_id: rollotisch
      command_open: python3 /config/RolloL2H.py -i "192.168.178.135" -m "98D873364881" up
      command_close: python3 /config/RolloL2H.py -i "192.168.178.135" -m "98D873364881" down
      command_stop: python3 /config/RolloL2H.py -i "192.168.178.135" -m "98D873364881" stop
```

- Restart HA, Refresh your HA Browser window

- ![cover](https://github.com/user-attachments/assets/c925c368-8daf-4702-a2f5-a0d654b47e59)
