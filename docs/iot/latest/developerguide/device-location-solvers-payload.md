# Location solvers and device

payload

Location solvers are algorithms that can be used to resolve the location of your IoT
devices. AWS IoT Core Device Location supports the following location solvers. You'll see examples of the
JSON payload format for these measurement types, the devices supported by the solver,
and how the location is resolved.

To resolve the device location, specify one or more of these measurement data types. A
single, resolved location will be returned for all measurement data combined.

###### Topics

- [Wi-Fi based solver](#location-solvers-wifi "#location-solvers-wifi")
- [Cellular based solver](#location-solvers-cellular "#location-solvers-cellular")
- [IP reverse lookup solver](#location-solvers-ip "#location-solvers-ip")
- [GNSS solver](#location-solvers-gnss "#location-solvers-gnss")

## Wi-Fi based solver

Use the Wi-Fi based solver to resolve the location using the scan information from
Wi-Fi access points. The solver supports the WLAN technology, and it can be used to
compute the device location for general IoT devices and LoRaWAN wireless devices.

The LoRaWAN devices must have the LoRa Edge chipset, which can decode the incoming
Wi-Fi scan information. LoRa Edge is an ultra-low power platform that integrates a
long-range LoRa transceiver, multi-constellation GNSS scanner, and passive Wi-Fi MAC
scanner targeting geolocation applications. When an uplink message is received from
the device, the Wi-Fi scan data is sent to AWS IoT Core Device Location, and the location is estimated
based on the Wi-Fi scan results. The decoded information is then passed to the Wi-Fi
based solver to retrieve the location information.

The following code shows an example of the JSON payload from the device
that contains the measurement data. When AWS IoT Core Device Location receives this data as
input, it sends an HTTP request to the solver provider to resolve the
location information. To retrieve the information, specify values for the
MAC Address and RSS (received signal strength). To do this, either provide
the JSON payload using this format, or use the [WiFiAccessPoints
object](../../../iot-wireless/2020-11-22/apireference/API_WiFiAccessPoint.md "../../../iot-wireless/2020-11-22/apireference/API_WiFiAccessPoint.md") parameter of the [GetPositionEstimate](../../../iot-wireless/2020-11-22/apireference/API_GetPositionEstimate.md "../../../iot-wireless/2020-11-22/apireference/API_GetPositionEstimate.md") API operation.

```
{
    "Timestamp": `1664313161`,    // optional
    "WiFiAccessPoints": [
        {
            "MacAddress": "`A0:EC:F9:1E:32:C1`",  // required
            "Rss": `-75`                          // required
        }
    ]
}
```

## Cellular based solver

You can use the cellular based solver to resolve the location using measurement
data obtained from cellular radio towers. The solver supports the following
technologies. A single resolved location information is obtained, even if you
include measurement data from any or all of these technologies.

- GSM
- CDMA
- WCDMA
- TD-SCDMA
- LTE

### Cellular based solver

payload examples

The following code shows examples of the JSON payload from the device that
contains cellular measurement data. When AWS IoT Core Device Location receives this data as input, it
sends an HTTP request to the solver provider to resolve the location
information. To retrieve the information, you either provide the JSON payload
using this format in the console, or specify values for the [CellTowers](../../../iot-wireless/2020-11-22/apireference/API_GetPositionEstimate.md#iotwireless-GetPositionEstimate-request-CellTowers "../../../iot-wireless/2020-11-22/apireference/API_GetPositionEstimate.md#iotwireless-GetPositionEstimate-request-CellTowers") parameter of the [GetPositionEstimate](../../../iot-wireless/2020-11-22/apireference/API_GetPositionEstimate.md "../../../iot-wireless/2020-11-22/apireference/API_GetPositionEstimate.md") API operation. You can provide the measurement
data by specifying values for parameters using any or all of these cellular
technologies.

When you use this measurement data, you must specify information such
as the network and country code of the mobile network, and optional
additional parameters including information about the local ID. The
following code shows an example of the payload format. For more
information about these parameters, see [LTE
object](../../../iot-wireless/2020-11-22/apireference/API_LteObj.md "../../../iot-wireless/2020-11-22/apireference/API_LteObj.md").

```
{
    "Timestamp": `1664313161`,           // optional
    "CellTowers": {
        "Lte": [
        {
          "Mcc": int,                   // required
          "Mnc": int,                   // required
          "EutranCid": int,             // required. Make sure that you use int for EutranCid.
          "Tac": int,                   // optional
          "LteLocalId": {               // optional
              "Pci": int,               // required
              "Earfcn": int,            // required
          },
          "LteTimingAdvance": int,      // optional
          "Rsrp": int,                  // optional
          "Rsrq": float,                // optional
          "NrCapable": boolean,         // optional
          "LteNmr": [                   // optional
                {
                    "Pci": int,         // required
                    "Earfcn": int,      // required
                    "EutranCid": int,   // required
                    "Rsrp": int,        // optional
                    "Rsrq": float       // optional
                }
            ]
         }
      ]
   }
}
```

When you use this measurement data, you must specify information such
as the network and country code of the mobile network, the base station
information, and optional additional parameters. The following code
shows an example of the payload format. For more information about these
parameters, see [GSM
object](../../../iot-wireless/2020-11-22/apireference/API_GsmObj.md "../../../iot-wireless/2020-11-22/apireference/API_GsmObj.md").

```
{
    "Timestamp": `1664313161`,           // optional
    "CellTowers": {
        "Gsm": [
        {
          "Mcc": int,                   // required
          "Mnc": int,                   // required
          "Lac": int,                   // required
          "GeranCid": int,              // required
          "GsmLocalId": {               // optional
              "Bsic": int,              // required
              "Bcch": int,              // required
          },
          "GsmTimingAdvance": int,      // optional
          "RxLevel": int,               // optional
          "GsmNmr": [                   // optional
            {
                "Bsic": int,            // required
                "Bcch": int,            // required
                "RxLevel": int,         // optional
                "GlobalIdentity": {
                    "Lac": int,         // required
                    "GeranCid": int     // required
                }
             }
          ]
       }
    ]
}
```

When you use this measurement data, you must specify information such
as the signal power and identification information, the base station
information, and optional additional parameters. The following code
shows an example of the payload format. For more information about these
parameters, see [CDMA
object](../../../iot-wireless/2020-11-22/apireference/API_CdmaObj.md "../../../iot-wireless/2020-11-22/apireference/API_CdmaObj.md").

```
{
    "Timestamp": `1664313161`,               // optional
    "CellTowers": {
        "Cdma": [
        {
            "SystemId": int,                // required
            "NetworkId": int,               // required
            "BaseStationId": int,           // required
            "RegistrationZone": int,        // optional
            "CdmaLocalId": {                // optional
              "PnOffset": int,              // required
              "CdmaChannel": int,           // required
            },
            "PilotPower": int,              // optional
            "BaseLat": float,               // optional
            "BaseLng": float,               // optional
            "CdmaNmr": [                    // optional
                {
                    "PnOffset": int,        // required
                    "CdmaChannel": int,     // required
                    "PilotPower": int,      // optional
                    "BaseStationId": int    // optional
                }
             ]
          }
       ]
    }
}
```

When you use this measurement data, you must specify information such
as the network and country code, signal power and identification
information, the base station information, and optional additional
parameters. The following code shows an example of the payload format.
For more information about these parameters, see [CDMA
object](../../../iot-wireless/2020-11-22/apireference/API_CdmaObj.md "../../../iot-wireless/2020-11-22/apireference/API_CdmaObj.md").

```
{
    "Timestamp": `1664313161`,           // optional
    "CellTowers": {
        "Wcdma": [
        {
          "Mcc": int,                   // required
          "Mnc": int,                   // required
          "UtranCid": int,              // required
          "Lac": int,                   // optional
          "WcdmaLocalId": {             // optional
              "Uarfcndl": int,          // required
              "Psc": int,               // required
          },
          "Rscp": int,                  // optional
          "Pathloss": int,              // optional
          "WcdmaNmr": [                 // optional
                {
                  "Uarfcndl": int,      // required
                  "Psc": int,           // required
                  "UtranCid": int,      // required
                  "Rscp": int,          // optional
                  "Pathloss": int,      // optional
                }
             ]
          }
       ]
    }
}
```

When you use this measurement data, you must specify information such
as the network and country code, signal power and identification
information, the base station information, and optional additional
parameters. The following code shows an example of the payload format.
For more information about these parameters, see [CDMA
object](../../../iot-wireless/2020-11-22/apireference/API_CdmaObj.md "../../../iot-wireless/2020-11-22/apireference/API_CdmaObj.md").

```
{
    "Timestamp": `1664313161`,           // optional
    "CellTowers": {
        "Tdscdma": [
        {
          "Mcc": int,                   // required
          "Mnc": int,                   // required
          "UtranCid": int,              // required
          "Lac": int,                   // optional
          "TdscdmaLocalId": {           // optional
              "Uarfcn": int,            // required
              "CellParams": int,        // required
          },
          "TdscdmaTimingAdvance": int,  // optional
          "Rscp": int,                  // optional
          "Pathloss": int,              // optional
          "TdscdmaNmr": [               // optional
                {
                  "Uarfcn": int,        // required
                  "CellParams": int,    // required
                  "UtranCid": int,      // optional
                  "Rscp": int,          // optional
                  "Pathloss": int,      // optional
                }
             ]
         }
      ]
   }
}
```

## IP reverse lookup solver

You can use the IP reverse lookup solver to resolve the location using the IP
address as input. The solver can obtain the location information from devices that
have been provisioned with AWS IoT. Specify the IP address information using a format
that's either the IPv4 or IPv6 standard pattern, or the IPv6 hex compressed pattern.
You then obtain the resolved location estimate, including additional information
such as city and country where the device is located.

###### Note

By using the IP reverse lookup, you agree not to use it for the purpose of
identifying or locating a specific household or street address.

The following code shows an example of the JSON payload from the device
that contains the measurement data. When AWS IoT Core Device Location receives the IP address
information in the measurement data, it looks up this information in the
solver provider's database, which is then used to resolve the location
information. To retrieve the information, either provide the JSON payload
using this format, or specify values for the [Ip](../../../iot-wireless/2020-11-22/apireference/API_GetPositionEstimate.md#iotwireless-GetPositionEstimate-request-Ip "../../../iot-wireless/2020-11-22/apireference/API_GetPositionEstimate.md#iotwireless-GetPositionEstimate-request-Ip") parameter of the [GetPositionEstimate](../../../iot-wireless/2020-11-22/apireference/API_GetPositionEstimate.md "../../../iot-wireless/2020-11-22/apireference/API_GetPositionEstimate.md") API operation.

###### Note

When this solver is used, the city, state, country, and postal code
where the device is located is also reported in addition to the
coordinates. For an example, see [Resolving device location
(console)](device-location-resolve-solvers.md#location-resolve-console "device-location-resolve-solvers.md#location-resolve-console").

```
{
    "Timestamp": `1664313161`,
    "Ip":{
        "IpAddress":`"54.240.198.35"`
      }
}
```

## GNSS solver

Use the GNSS (Global Navigation Satellite System) solver to retrieve the device
location using the information contained in the GNSS scan result messages or NAV
messages. You can optionally provide additional GNSS assistance information, which
reduces the number of variables that the solver must use to search for signals. By
providing this assistance information, which includes the position, altitude, and
the capture time and accuracy information, the solver can easily identify the
satellites in view and compute the device location.

This solver can be used with LoRaWAN devices, and other devices that have been
provisioned with AWS IoT. For general IoT devices, if the devices support location
estimation using GNSS, when the GNSS scan information is received from the device,
the transceivers resolve the location information. For LoRaWAN devices, the devices
must have the LoRa Edge chipset. When an uplink message is received from the device,
the GNSS scan data is sent to AWS IoT Core for LoRaWAN, and the location is estimated based on
the scan results from the transceivers.

The following code shows an example of the JSON payload from the device
that contains the measurement data. When AWS IoT Core Device Location receives the GNSS scan
information containing the payload in the measurement data, it uses the
transceivers and any additional assistance information included to search
for signals and resolve the location information. To retrieve the
information, either provide the JSON payload using this format, or specify
values for the [Gnss](../../../iot-wireless/2020-11-22/apireference/API_GetPositionEstimate.md#iotwireless-GetPositionEstimate-request-Gnss "../../../iot-wireless/2020-11-22/apireference/API_GetPositionEstimate.md#iotwireless-GetPositionEstimate-request-Gnss") parameter of the [GetPositionEstimate](../../../iot-wireless/2020-11-22/apireference/API_GetPositionEstimate.md "../../../iot-wireless/2020-11-22/apireference/API_GetPositionEstimate.md") API operation.

###### Note

Before AWS IoT Core Device Location can resolve the device location, you must remove the
destination byte from the payload.

```
{
    "Timestamp": `1664313161`,                  // optional
    "Gnss": {
        "AssistAltitude": `number`,             // optional
        "AssistPosition": `[ number ]`,         // optional
        "CaptureTime": `number`,                // optional
        "CaptureTimeAccuracy": `number`,        // optional
        "Payload": "`string`",                  // required
        "Use2DSolver": `boolean`                // optional
   }
}
```
