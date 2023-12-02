# pynaim
Python module to control naim amps

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



