# Data Dictionary

This section defines all telemetry fields, data types, units, and valid ranges used in the Connected Mobility guidance.

## Vehicle Identity Fields

| Field     | Type   | Description                                      | Required |
| --------- | ------ | ------------------------------------------------ | -------- |
| vin       | String | Vehicle Identification Number (17 characters)    | Yes      |
| vehicleId | String | Internal vehicle identifier (UUID or VIN)        | Yes      |
| fid       | String | Fleet ID for fleet assignment                    | No       |
| vt        | String | Vehicle Type: I=In-transit, P=Parked, D=Delivery | No       |

## Location and Movement Fields

| Field     | Type    | Description                              | Unit     | Range          |
| --------- | ------- | ---------------------------------------- | -------- | -------------- |
| ts        | Integer | Unix timestamp (seconds since epoch)     | seconds  | >0             |
| timestamp | String  | ISO 8601 timestamp                       | ISO 8601 | Valid datetime |
| lat       | Number  | Latitude in decimal degrees              | degrees  | -90 to 90      |
| lon       | Number  | Longitude in decimal degrees             | degrees  | -180 to 180    |
| alt       | Number  | Altitude above sea level                 | feet     | Any            |
| spd       | Number  | Vehicle speed                            | mph      | 0 to 200       |
| hdg       | Number  | Heading/bearing                          | degrees  | 0 to 360       |
| gps_qual  | Integer | GPS quality: 1=Poor, 2=Good, 3=Excellent | enum     | 1, 2, 3        |

## Vehicle State Fields

| Field         | Type    | Description                              | Unit    | Range      |
| ------------- | ------- | ---------------------------------------- | ------- | ---------- |
| odo           | Number  | Odometer reading                         | miles   | >=0        |
| eng           | Number  | Engine hours                             | hours   | >=0        |
| gear          | Integer | Current gear (0=neutral/park, 1-6=drive) | enum    | 0 to 6     |
| brk           | Number  | Brake pedal position                     | percent | 0 to 100   |
| acc           | Number  | Accelerator pedal position               | percent | 0 to 100   |
| ignitionOn    | Boolean | Ignition status                          | boolean | true/false |
| parking_brake | Integer | Parking brake engaged                    | boolean | 0, 1       |

## Driver Behavior Fields

| Field          | Type    | Description                       | Unit    | Range      |
| -------------- | ------- | --------------------------------- | ------- | ---------- |
| harsh_brk      | Integer | Harsh braking event count         | count   | >=0        |
| harsh_acc      | Integer | Harsh acceleration event count    | count   | >=0        |
| harsh_turn     | Integer | Harsh turning event count         | count   | >=0        |
| speed_viol     | Integer | Speed violation flag              | boolean | 0, 1       |
| idle_time      | Integer | Idle time                         | seconds | >=0        |
| drv_score      | Integer | Driver safety score               | score   | 0 to 100   |
| phone_use      | Integer | Phone usage detected              | boolean | 0, 1       |
| seatbelt       | Integer | Seatbelt fastened                 | boolean | 0, 1       |
| seatbeltStatus | Boolean | Seatbelt status (alternate field) | boolean | true/false |

## Fuel and Energy Fields

| Field     | Type    | Description                          | Unit    | Range    |
| --------- | ------- | ------------------------------------ | ------- | -------- |
| fuel_rate | Number  | Fuel consumption rate (ICE vehicles) | mpg     | >0       |
| fuel_lvl  | Integer | Fuel level percentage (ICE vehicles) | percent | 0 to 100 |
| fuelLevel | Number  | Fuel level (alternate field)         | percent | 0 to 100 |
| soc       | Number  | State of charge (EV vehicles)        | percent | 0 to 100 |
| volt      | Number  | High voltage battery voltage (EV)    | volts   | >0       |
| regen_pwr | Number  | Regenerative braking power (EV)      | kW      | Any      |

## Diagnostic Fields

| Field            | Type    | Description                           | Unit       | Range    |
| ---------------- | ------- | ------------------------------------- | ---------- | -------- |
| eng_temp         | Integer | Engine temperature                    | Fahrenheit | 0 to 300 |
| engineTemp       | Number  | Engine temperature (alternate)        | Fahrenheit | 0 to 300 |
| oil_press        | Integer | Oil pressure                          | PSI        | 0 to 100 |
| oilPressure      | Number  | Oil pressure (alternate)              | PSI        | 0 to 100 |
| oil_temp         | Integer | Oil temperature                       | Fahrenheit | 0 to 300 |
| coolant_temp     | Integer | Coolant temperature                   | Fahrenheit | 0 to 300 |
| trans_temp       | Integer | Transmission temperature              | Fahrenheit | 0 to 300 |
| oil_life         | Integer | Oil life remaining                    | percent    | 0 to 100 |
| brake_wear       | Integer | Brake pad life remaining              | percent    | 0 to 100 |
| filter_life      | Integer | Air filter life remaining             | percent    | 0 to 100 |
| dtc_codes_active | Integer | Active diagnostic trouble codes count | count      | >=0      |

## Tire Fields

| Field         | Type    | Description                  | Unit       | Range    |
| ------------- | ------- | ---------------------------- | ---------- | -------- |
| tire_fl       | Number  | Front left tire pressure     | PSI        | 0 to 60  |
| tire_fr       | Number  | Front right tire pressure    | PSI        | 0 to 60  |
| tire_rl       | Number  | Rear left tire pressure      | PSI        | 0 to 60  |
| tire_rr       | Number  | Rear right tire pressure     | PSI        | 0 to 60  |
| tire_temp_max | Integer | Maximum tire temperature     | Fahrenheit | 0 to 200 |
| tire_tread_fl | Number  | Front left tire tread depth  | mm         | 0 to 15  |
| tire_tread_fr | Number  | Front right tire tread depth | mm         | 0 to 15  |
| tire_tread_rl | Number  | Rear left tire tread depth   | mm         | 0 to 15  |
| tire_tread_rr | Number  | Rear right tire tread depth  | mm         | 0 to 15  |

## Safety System Fields

| Field       | Type    | Description                            | Unit    | Range   |
| ----------- | ------- | -------------------------------------- | ------- | ------- |
| aeb_en      | Integer | Automatic Emergency Braking enabled    | boolean | 0, 1    |
| aeb_sens    | Integer | AEB sensitivity level                  | enum    | 1, 2, 3 |
| aeb_act     | Integer | AEB activated                          | boolean | 0, 1    |
| abs_act     | Integer | ABS activated                          | boolean | 0, 1    |
| esc_act     | Integer | Electronic Stability Control activated | boolean | 0, 1    |
| airbag_warn | Integer | Airbag warning light                   | boolean | 0, 1    |

## Electrical System Fields

| Field             | Type   | Description                 | Unit  | Range   |
| ----------------- | ------ | --------------------------- | ----- | ------- |
| battery_voltage   | Number | 12V battery voltage         | volts | 0 to 16 |
| batteryVoltage    | Number | Battery voltage (alternate) | volts | 0 to 16 |
| alternator_output | Number | Alternator output voltage   | volts | 0 to 16 |

## Trip Context Fields

| Field    | Type    | Description               | Required |
| -------- | ------- | ------------------------- | -------- |
| tripId   | String  | Unique trip identifier    | No       |
| driverId | String  | Driver identifier         | No       |
| in_trip  | Boolean | Vehicle currently in trip | No       |

## Metadata Fields

| Field           | Type    | Description                      | Required |
| --------------- | ------- | -------------------------------- | -------- |
| data_source     | String  | Origin: iot_core, fleetwise, oem | Yes      |
| auto_registered | Boolean | Vehicle was auto-registered      | No       |
| messageType     | String  | Message type identifier          | No       |
