# Configuring the position of LoRaWAN devices

When you add your device to AWS IoT Core for LoRaWAN, you can specify the static position
information, optionally activate positioning, and specify a destination. The destination
describes the IoT rule that processes the device's position information and routes the
updated position to Amazon Location Service. After you configure your device position, the position
data is displayed on an Amazon Location map with the accuracy information, and the destination
that you specified.

You can configure the position of your device using the AWS Management Console, the
AWS IoT Wireless API, or the AWS CLI.

## Uplink message from AWS IoT Core for LoRaWAN to rules engine

###### Note

If you activate positioning, you must specify the geolocation frame port for
communicating the Wi-Fi and GNSS scan data from the device to AWS IoT Core for LoRaWAN. The
position information is communicated to AWS IoT Core for LoRaWAN using this frame port.

The LoRaWAN specification provides a data delivery field (FRMPayload) and a Port
field (FPort) to distinguish between different types of messages. To communicate the
position information, you can specify a value anywhere between 1 and 223 for the
frame port. FPort 0 is reserved for MAC messages, FPort 224 is reserved for MAC
compliance testing, and ports 225-255 are reserved for future standardized
application extensions.

### Uplink message from AWS IoT Core for LoRaWAN to rules engine

You can subscribe to an MQTT topic to receive location data as it becomes
available from your LoRaWAN device. This method allows you to process
location data in real-time using AWS IoT rules.

1. ###### Create a destination for location data

Create a destination with an AWS IoT rule that processes location data.
For information about creating destinations, see [Add destinations to AWS IoT Core for LoRaWAN](lorawan-create-destinations.md "lorawan-create-destinations.md"). 2. ###### Subscribe to the MQTT topic

Go to the AWS IoT console, then navigate to **Test** > the
[MQTT test client](https://console.aws.amazon.com/iot/home#/test "https://console.aws.amazon.com/iot/home#/test").
Enter the topic name that you specified in your location destination rule
(for example, `project/sensor/location`),
and then choose **Subscribe**. 3. ###### View location messages

When your device sends location data, you'll see messages published to
the topic. The following shows an example of a location message:

**Contents of deviceposition.json**

```
{
    "WirelessDeviceId": `"5b58245e-146c-4c30-9703-0ca942e3ff35"`,

    "coordinates": [
        `33.33000183105469`,
        `-22.219999313354492`,
        99.0
    ],
    "type": "Point",
    "properties": {
        "measurementType": `"GNSS" | "Wi-Fi"`,
        "horizontalAccuracy": `34`,
        "verticalAccuracy": 18.5,
        "timestamp": `"2026-01-01T00:00:00Z"`
    },

    //Parameters controlled by AWS IoT Core for LoRaWAN
    "WirelessMetadata":
    {
        "LoRaWAN":
        {
            "ADR": false,
            "Bandwidth": 125,
            "ClassB": false,
            "CodeRate": "4/5",
            "DataRate": "0",
            "DevAddr": "00b96cd4",
            "DevEui": "58a0cb000202c99",
            "FOptLen": 2,
            "FCnt": 1,
            "Fport": 136,
            "Frequency": "868100000",
            "Gateways": [
             {
                "GatewayEui": "80029cfffe5cf1cc",
                "Snr": -29,
                "Rssi": 9.75
             }
             ],
            "MIC": "7255cb07",
            "MType": "UnconfirmedDataUp",
            "Major": "LoRaWANR1",
            "Modulation": "LORA",
            "PolarizationInversion": false,
            "SpreadingFactor": 12,
            "Timestamp": "2026-01-01T00:00:00Z"
        }
    }
}
```

###### Note

The coordinates (position information for a device in GeoJSON format)
are ordered as `[longitude, latitude, altitude]`, and altitude is optional if vertical accuracy information is unavailable.
Please see more details on [Resolved location metadata parameters](#lorawan-location-devices-metadata "#lorawan-location-devices-metadata").

For WirelessMetadata, please refer to wireless device destination payload for regular uplink [Wireless device destination payload](lorawan-device-connection-status.md#lorawan-device-connection-payload "lorawan-device-connection-status.md#lorawan-device-connection-payload").

## Configuring the position of your devices using the console

To configure and manage the position of your devices by using the AWS Management Console, first
sign in to the console and then go to the [**Devices**](https://console.aws.amazon.com/iot/home#/wireless/devices "https://console.aws.amazon.com/iot/home#/wireless/devices") hub page of the AWS IoT console.

###### Add position information

To add position information for your device:

1. In the **Devices** hub page, choose **Add
   wireless device**.
2. Enter the wireless device specification, device and service profiles, and
   the destination that defines the IoT rule for routing the data to other
   AWS services. For more information, see [Onboard your devices to AWS IoT Core for LoRaWAN](lorawan-onboard-end-devices.md "lorawan-onboard-end-devices.md").
3. Enter the position information, optionally activate geolocation, and
   specify a position data destination that you want to use for routing
   messages.
   - ###### Position information

   Specify the position data for your device using the latitude
   and longitude coordinates, and an optional altitude coordinate.
   The position information is based on the WGS84 coordinate
   system.
   - ###### Geolocation

   Activate positioning if you want AWS IoT Core for LoRaWAN to use
   geolocation for computing the device position. It uses
   third-party GNSS and Wi-Fi solvers to identify the position of
   your device in real time.

   To enter the geolocation information, choose **Activate
   positioning**, and enter the geolocation frame port for
   communicating the GNSS and Wi-Fi scan data to AWS IoT Core for LoRaWAN. You'll
   see default FPorts populated for your reference. However, you can
   choose a different value anywhere between 1 and 223.
   - ###### Position data destination

   Choose a destination to describe the AWS IoT rule that processes
   the device's position data and forwards it to AWS IoT Core for LoRaWAN. Use
   this destination only to route position data. It must be
   different from the destination that you use for routing device
   data to other AWS services.

###### View device's position configuration

After you've configured your device's position, AWS IoT Core for LoRaWAN creates an
Amazon Location map called `iotwireless.map`. You can see this map in the
details page of your device on the **Position** tab. Based on
the position coordinates that you specified or the position computed by the
third-party solvers, the position of your device will be displayed as a marker
on the map. You can zoom in or zoom out to clearly view the position of your
device on the map. In the device's details page, on the
**Position** tab, you'll also see the accuracy information,
the timestamp at which your device's position was determined, and the position
data destination that you specified.

###### Note

If you haven't activated Amazon Location Service maps, you'll see a message indicating that
you'll have to use Amazon Location Service to access the map and view the position. Using
Amazon Location Service maps may incur additional charges to your AWS account. For more
information, see [AWS IoT Core
pricing](https://aws.amazon.com/iot-core/pricing/ "https://aws.amazon.com/iot-core/pricing/").

The map, `iotwireless.map`, acts as a source of map data which is
accessed using `Get` API operations, such as [`GetMapTile`](../../../location-maps/latest/APIReference/API_GetMapTile.md "../../../location-maps/latest/APIReference/API_GetMapTile.md"). For information about `Get`
APIs used with maps, see [Amazon Location Service API
reference](../../../location-maps/latest/APIReference/Welcome.md "../../../location-maps/latest/APIReference/Welcome.md").

To get additional details about this map, go to the Amazon Location Service console, choose
**maps**, and then choose [iotwireless.map](https://console.aws.amazon.com/location/maps/home#/describe/iotwireless.map "https://console.aws.amazon.com/location/maps/home#/describe/iotwireless.map"). For
more information, see [Maps](../../../location/latest/developerguide/map-concepts.md "../../../location/latest/developerguide/map-concepts.md") in the
_Amazon Location Service developer guide_.

###### Update device's position configuration

To change the device's position configuration, in the device details page,
choose **Edit** and then update the position information, any
geolocation settings, and the destination.

###### Note

Information about historical position data isn't available. When you update
the device's position coordinates, it overwrites the previously reported
position data. After you've updated the position, in the
**Position** tab of the device details, you'll see the new
position information. The change in timestamp indicates that it corresponds to
the last known position of the device.

## Configure the position of your devices using API or CLI

You can specify the position information, configure the device position, and
activate optional geolocation using the AWS IoT Wireless API or the AWS CLI.

###### Important

The API actions [UpdatePosition](../apireference/API_UpdatePosition.md "../apireference/API_UpdatePosition.md"), [GetPosition](../apireference/API_GetPosition.md "../apireference/API_GetPosition.md"), [PutPositionConfiguration](../apireference/API_PutPositionConfiguration.md "../apireference/API_PutPositionConfiguration.md"), [GetPositionConfiguration](../apireference/API_GetPositionConfiguration.md "../apireference/API_GetPositionConfiguration.md"), and [ListPositionConfigurations](../apireference/API_ListPositionConfigurations.md "../apireference/API_ListPositionConfigurations.md") are no longer supported. Calls to update
and retrieve the position information should use the [GetResourcePosition](../apireference/API_GetResourcePosition.md "../apireference/API_GetResourcePosition.md") and [UpdateResourcePosition](../apireference/API_UpdateResourcePosition.md "../apireference/API_UpdateResourcePosition.md") API operations instead.

### Update position information

To update the position information for a given wireless device, specify the
coordinates using the [UpdateResourcePosition](../apireference/API_UpdateResourcePosition.md "../apireference/API_UpdateResourcePosition.md") API operation or the [update-resource-position](../../../cli/latest/reference/iotwireless/update-resource-position.md "../../../cli/latest/reference/iotwireless/update-resource-position.md") CLI command. Specify
`WirelessDevice` as the `ResourceType`, the ID of the
wireless device to be updated as the `ResourceIdentifier`, and the
position information.

**Sample of the UpdateResourcePosition API operation**

```
PATCH /resource-positions/`ResourceIdentifier`?resourceType=WirelessDevice HTTP/1.1
{
     "coordinates": [
        `33.33`,
        `-22.22`,
        `11.11`
     ],
     "type": "Point"
}
```

**Sample of the update-resource-position CLI command**

```
echo '{"coordinates": [33.33, -22.22, 11.11], "type": "Point"}' > /tmp/position.json
aws iotwireless update-resource-position \
    --resource-type WirelessDevice \
    --resource-id `"5b58245e-146c-4c30-9703-0ca942e3ff35"` \
    --geo-json-payload fileb:///tmp/position.json
```

The following shows the contents of the
`deviceposition.json` file,
which is the uplink message from AWS IoT Core for LoRaWAN to rules engine

To specify the FPort values for sending the geolocation data, use the [Positioning](../apireference/API_Positioning.md "../apireference/API_Positioning.md") object
with the [CreateWirelessDevice](../apireference/API_CreateWirelessDevice.md "../apireference/API_CreateWirelessDevice.md") and [UpdateWirelessDevice](../apireference/API_UpdateWirelessDevice.md "../apireference/API_UpdateWirelessDevice.md") API operations.

**Contents of deviceposition.json**

```
{
     "coordinates": [
        `33.33`,
        `-22.22`,
        `11.11`
     ],
     "WirelessDeviceId": `"5b58245e-146c-4c30-9703-0ca942e3ff35"`,
     "type": "Point",
     "properties": {
        "measurementType": "UserInput",
        "horizontalAccuracy": 0,
        "verticalAccuracy": 0,
        "timestamp": `"2026-01-01T00:00:00Z"`
      }
}
```

###### Note

This command returns no response body (`204 No Content`).
To verify the updated position, use the `GetResourcePosition` API operation.

### Get position information

To get the position information for a given wireless device, use the [GetResourcePosition](../apireference/API_GetResourcePosition.md "../apireference/API_GetResourcePosition.md") API or the [get-resource-position](../../../cli/latest/reference/iotwireless/get-resource-position.md "../../../cli/latest/reference/iotwireless/get-resource-position.md") CLI command. Specify
`WirelessDevice` as the `resourceType` and provide the
ID of the wireless device as the `resourceIdentifier`.

**Sample of the GetResourcePosition API operation**

```
GET /resource-positions/`ResourceIdentifier`?resourceType=WirelessDevice HTTP/1.1
```

**Sample of the get-resource-position CLI command**

```
aws iotwireless get-resource-position \
    --resource-type WirelessDevice \
    --resource-id `"5b58245e-146c-4c30-9703-0ca942e3ff35"` \
    /dev/stdout
```

###### Note

This command returns the position information of your wireless device as a GeoJSON payload (`200 OK`).

The contents of the `get-resource-position-api-response.json` file
includes the position coordinates, geolocation type, and properties such as measurement type, accuracy,
and the timestamp when the device position was resolved. The wireless device ID is
not included in the API response.

**Contents of get-resource-position-api-response.json**

```
{
     "coordinates": [
        `33.33`,
        `-22.22`,
        `11.11`
     ],
     "type": "Point",
     "properties": {
        "measurementType": `"GNSS" | "Wi-Fi" | "UserInput"`,
        "horizontalAccuracy": `number`,
        "verticalAccuracy": number,
        "timestamp": `"Thu Jan 01 00:00:00 UTC 2026"`
      }
}
```

## Resolved location metadata parameters

The following table shows a definition of the different parameters in the resolved location
metadata. The `WirelessDeviceId` is the ID of the
wireless device, such as `5b58245e-146c-4c30-9703-0ca942e3ff35` and the
`measurementType` is the positioning method used to calculate the location.

| LoRaWAN resolved location metadata parameters | Parameter                                                                                                                                                                                                           | Description | Type |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ---- |
| `coordinates`                                 | The resolved coordinates of the LoRaWAN device.<br>Coordinates are ordered as `[longitude, latitude, altitude]`.                                                                                                    | Array       |
| `WirelessDeviceId`                            | The identifier of the wireless device that sends the location uplink data                                                                                                                                           | String      |
| `type`                                        | GeoJSON type. Currently supports the `"Point"` type.                                                                                                                                                                | String      |
| `measurementType`                             | The measurement type for resolved location metadata.<br>For LoRaWAN devices, the supported values are<br>`"GNSS"` and `"Wi-Fi"`.<br>If triggered by update-resource-position API or CLI, it would be `"UserInput"`. | String      |
| `horizontalAccuracy`                          | The horizontal accuracy of the resolved position, in meters.                                                                                                                                                        | Number      |
| `verticalAccuracy`                            | The vertical accuracy of the resolved position, in meters.                                                                                                                                                          | Number      |
| `timestamp`                                   | The timestamp when the LoRaWAN device location was resolved.                                                                                                                                                        | Timestamp   |
