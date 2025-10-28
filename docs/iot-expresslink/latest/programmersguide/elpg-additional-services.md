# 11 Additional services

 

## 11.1.1 TIME?   »Request current time information«

ExpressLink modules _must_ provide time information as available
from SNTP, GPS or cellular network sources. Devices can choose to maintain a time
reference internally even when disconnected or in sleep mode, depending on implementation
specific software or hardware capabilities.

###### Returns:

`11.1.1.1`   `OK *{date YYYY/MM/DD} {time hh:mm:ss.xx} {source}*`

If time information is available and recently obtained, the module
returns 'OK' followed by that information.

`11.1.1.2`   `ERR15 TIME NOT AVAILABLE`

A recent time fix could not be obtained.

## 11.1.2 WHERE?   »Request location information«

ExpressLink modules can optionally provide last location information as available
from GPS, GNSS, cellular network or other triangulation method. A time stamp is
provided to allow the host determine whether the information is current. The
implementation of this command is optional.

###### Returns:

`11.1.2.1`   `OK *{date} {time} {lat} {long} {elev} {accuracy} {source}*`

If location coordinates could be obtained at date/time, the module
returns 'OK' followed by the information.

`11.1.2.2`   `ERR16 LOCATION NOT AVAILABLE`

A location fix could not be obtained.
