# Resolving location of IoT

devices

Use AWS IoT Core Device Location to decode the measurement data from your devices, and resolve the device
location using third-party solvers. The resolved location is generated as a GeoJSON
payload with the geo coordinates and accuracy information. You can resolve the location
of your device from the AWS IoT console, the AWS IoT Wireless API, or AWS CLI.

###### Topics

- [Resolving device location
  (console)](#location-resolve-console "#location-resolve-console")
- [Resolving device location (API)](#location-resolve-api "#location-resolve-api")
- [Troubleshooting errors when
  resolving the location](#location-resolve-troubleshoot "#location-resolve-troubleshoot")

## Resolving device location

(console)

To resolve the device location (console)

1. Go to the [Device Location](https://console.aws.amazon.com/iot/home#/device-location-test "https://console.aws.amazon.com/iot/home#/device-location-test") page in the AWS IoT console.
2. Obtain the payload measurement data from your device logs or from CloudWatch Logs,
   and enter it in the **Resolve position via payload**
   section.

The following code shows a sample JSON payload. The payload contains
cellular and Wi-Fi measurement data. If your payload contains additional
types of measurement data, the solver with the best accuracy will be used.
For more information and payload examples, see [Location solvers and device
payload](device-location-solvers-payload.md "device-location-solvers-payload.md").

###### Note

The JSON payload must contain at least one type of measurement
data.

```
{
    "Timestamp": `1664313161`,
    "Ip":{
        "IpAddress": `"54.240.198.35"`
    },
    "WiFiAccessPoints": [{
        "MacAddress": `"A0:EC:F9:1E:32:C1"`,
        "Rss": `-77`
    }],
    "CellTowers": {
        "Gsm": [{
            "Mcc": `262`,
            "Mnc": `1`,
            "Lac": `5126`,
            "GeranCid": `16504`,
            "GsmLocalId": {
                "Bsic": `6`,
                "Bcch": `82`
            },
            "GsmTimingAdvance": `1`,
            "RxLevel": `-110`,
            "GsmNmr": [{
                "Bsic": `7`,
                "Bcch": `85`,
                "RxLevel": `-100`,
                "GlobalIdentity": {
                    "Lac": `1`,
                    "GeranCid": `1`
                }
            }]
        }],
        "Wcdma": [{
            "Mcc": `262`,
            "Mnc": `7`,
            "Lac": `65535`,
            "UtranCid": `14674663`,
            "WcdmaNmr": [{
                    "Uarfcndl": `10786`,
                    "UtranCid": `14674663`,
                    "Psc": `149`
                },
                {
                    "Uarfcndl": `10762`,
                    "UtranCid": `14674663`,
                    "Psc": `211`
                }
            ]
        }],
        "Lte": [{
            "Mcc": `262`,
            "Mnc": `2`,
            "EutranCid": `2898945`,
            "Rsrp": `-50`,
            "Rsrq": `-5`,
            "LteNmr": [{
                    "Earfcn": `6300`,
                    "Pci": `237`,
                    "Rsrp": `-60`,
                    "Rsrq": `-6`,
                    "EutranCid": `2898945`
                },
                {
                    "Earfcn": `6300`,
                    "Pci": `442`,
                    "Rsrp": `-70`,
                    "Rsrq": `-7`,
                    "EutranCid": `2898945`
                }
            ]
        }]
    }
}
```

3. To resolve the location information, choose
   **Resolve**.

The location information is of type blob and returned as a payload that
uses the GeoJSON format, which is a format used for encoding geographical
data structures. The payload contains:

    * The WGS84 geo coordinates, which include the latitude and
     longitude information. It might also include an altitude
     information.
    * The type of location information reported, such as
     **Point**. A point location type represents the
     location as a WGS84 latitude and longitude, encoded as a [GeoJSON
     point](https://geojson.org/geojson-spec.html#point "https://geojson.org/geojson-spec.html#point").
    * The horizontal and vertical accuracy information, which indicates
     the difference, in meters, between the location information
     estimated by the solvers and the actual device location.
    * The confidence level, which indicates the uncertainty in the
     location estimate response. The default value is 0.68, which
     indicates a 68% probability that the actual device location is
     within the uncertainty radius of the estimated location.
    * The city, state, country, and postal code where the device is
     located. This information will be reported only when the IP reverse
     lookup solver is used.
    * The timestamp information, which corresponds to the date and time
     at which the location was resolved. It uses the Unix timestamp
     format.

The following code shows a sample GeoJSON payload returned by resolving
the location.

###### Note

If AWS IoT Core Device Location reports errors when attempting to resolve the location, you
can troubleshoot the errors and resolve the location. For more
information, see [Troubleshooting errors when
resolving the location](#location-resolve-troubleshoot "#location-resolve-troubleshoot").

```
{
    "coordinates": [
        13.376076698303223,
        52.51823043823242
    ],
    "type": "Point",
    "properties": {
        "verticalAccuracy": 45,
        "verticalConfidenceLevel": 0.68,
        "horizontalAccuracy": 303,
        "horizontalConfidenceLevel": 0.68,
        "country": "USA",
        "state": "CA",
        "city": "Sunnyvalue",
        "postalCode": "91234",
        "timestamp": "2022-11-18T12:23:58.189Z"
    }
}
```

4. Go to the **Resource location** section and verify the
   geolocation information reported by AWS IoT Core Device Location . You can copy the payload for
   use with other applications and AWS services. For example, you can use the
   [Location](location-rule-action.md "location-rule-action.md") to send your geographical
   location data to Amazon Location Service.

## Resolving device location (API)

To resolve the device location using the AWS IoT Wireless API, use the [GetPositionEstimate](../../../iot-wireless/latest/apireference/API_GetPositionEstimate.md "../../../iot-wireless/latest/apireference/API_GetPositionEstimate.md") API operation or the [get-position-estimate](../../../cli/latest/reference/iotwireless/get-position-estimate.md "../../../cli/latest/reference/iotwireless/get-position-estimate.md") CLI command. Specify the payload measurement data
as input, and run the API operation to resolve the device location.

###### Note

The `GetPositionEstimate` API operation doesn't store any device or
state information and can't be used retrieve historical location data. It
performs a one-time operation that resolves the measurement data and produces
the estimated location. To retrieve the location information, you must specify
the payload information every time you perform this API operation.

The following command shows an example of how to resolve the location using this
API operation.

###### Note

When running the `get-position-estimate` CLI command, you must
specify the output JSON file as the first input. This JSON file will store the
estimated location information obtained as response from the CLI in GeoJSON
format. For example, the following command stores the location information in
the `locationout.json` file.

```
aws iotwireless get-position-estimate `locationout.json` \
    --ip IpAddress="`"54.240.198.35"`" \
    --wi-fi-access-points \
        MacAddress="`A0:EC:F9:1E:32:C1`",Rss=`-75` \
        MacAddress="`A0:EC:F9:15:72:5E`",Rss=`-67`
```

This example includes both Wi-Fi access points and IP address as the measurement
types. AWS IoT Core Device Location chooses between the Wi-Fi solver and the IP reverse lookup solver,
and it selects the solver with the higher accuracy.

The resolved location is returned as a payload that uses the GeoJSON format, which
is a format used for encoding geographical data structures. It is then stored in the
`locationout.json` file. The payload contains the WGS84
latitude and longitude coordinates, accuracy and confidence level information, the
location data type, and the timestamp at which the location was resolved.

```
{
    "coordinates": [
        13.37704086303711,
        52.51865005493164
    ],
    "type": "Point",
    "properties": {
        "verticalAccuracy": 707,
        "verticalConfidenceLevel": 0.68,
        "horizontalAccuracy": 389,
        "horizontalConfidenceLevel": 0.68,
        "country": "USA",
        "state": "CA",
        "city": "Sunnyvalue",
        "postalCode": "91234",
        "timestamp": "2022-11-18T14:03:57.391Z"
    }
}
```

## Troubleshooting errors when

resolving the location

When you attempt to resolve the location, you might see any of the following error
codes. AWS IoT Core Device Location might generate an error when using the
`GetPositionEstimate` API operation, or else refer to the line number
corresponding to the error in the AWS IoT console.

- ###### 400 error

This error indicates that the format of the device payload JSON can't
be validated by AWS IoT Core Device Location. The error might occur because:

    + The JSON measurement data is formatted incorrectly.
    + The payload contains only the timestamp information.
    + The measurement data parameters, such as the IP address, are not
     valid.

To resolve this error, check whether your JSON is formatted correctly and
contains data from one or more measurement types as input. If the IP address
is invalid, for information about how you can provide a valid IP address to
resolve the error, see [IP reverse lookup solver](device-location-solvers-payload.md#location-solvers-ip "device-location-solvers-payload.md#location-solvers-ip").

- ###### 403 error

This error indicates that you don't have the permissions to perform
the API operation or to use the AWS IoT console to retrieve the device
location. To resolve this error, verify that you have the required
permissions to perform this action. This error might occur if your
AWS Management Console session or your AWS CLI session token have expired. To resolve
this error, refresh the session token to use the AWS CLI, or log out of
the AWS Management Console and then log in using your credentials.

- ###### 404 error

This error indicates that no location information was found or solved
by AWS IoT Core Device Location. The error might occur due to cases such as insufficient data
in the measurement data input. For example:

    + The MAC address or cellular tower information is not
     sufficient.
    + The IP address is not available to look up and retrieve the
     location.
    + The GNSS payload is not sufficient.

To resolve the error in such cases, check whether your measurement data
contains sufficient information required to resolve the device
location.

- ###### 500 error

This error indicates that an internal server exception occurred when
AWS IoT Core Device Location attempted to resolve the location. To attempt to fix this error,
refresh the session and retry sending the measurement data to be
resolved.
