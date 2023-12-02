# pynaim
A WIP python module to control naim amps (targeted at Naim Uniti Atom)

NOT FINISHED!!

# Examples

### Turn amp on:
```python
from naim import naim
client = naim("ip address of amp")
client.set_power(True)
```

### Turn amp off:
```python
from naim import naim
client = naim("ip address of amp")
client.set_power(False)
```

### Get amp current source:
```python
from naim import naim
client = naim("ip address of amp")
print(client.get_source())
```

# Functions
## naim.power_status
arguments: none  
returns: "off": str, "on": str, False: bool  
notes: n/a  

## naim.set_power
arguments: state: bool  
returns: bool  
notes: returns True if the state changed after the request was sent (the amp actually changed), False if it didn't change. Argument True for on, False for off  

## naim.get_source
arguments: none  
returns: str  
notes: returns whatever the amp api returns. ex. ```inputs/hdmi```



