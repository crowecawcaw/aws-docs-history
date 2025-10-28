# Configuring position of LoRaWAN

devices

When you add your device to AWS IoT Core for LoRaWAN, you can specify the static position
information, optionally activate positioning, and specify a destination. The destination
describes the IoT rule that processes the device's position information and routes the
updated position to Amazon Location Service. After you configure your device position, the position
data is displayed on an Amazon Location map with the accuracy information, and the destination
that you specified.

You can configure the position of your device using the AWS Management Console, the
AWS IoT Wireless API, or the AWS CLI.

## Frame ports and format of

uplink messages

If you activate positioning, you must specify the geolocation frame port for
communicating the Wi-Fi and GNSS scan data from the device to AWS IoT Core for LoRaWAN. The
position information is communicated to AWS IoT Core for LoRaWAN using this frame port.

The LoRaWAN specification provides a data delivery field (FRMPayload) and a Port
field (FPort) to distinguish between different types of messages. To communicate the
position information, you can specify a value anywhere between 1 and 223 for the
frame port. FPort 0 is reserved for MAC messages, FPort 224 is reserved for MAC
compliance testing, and ports 225-255 are reserved for future standardized
application extensions.

### Uplink message from

AWS IoT Core for LoRaWAN to rules engine

When you add a destination, it creates an AWS IoT rule to route the data to
Amazon Location Service using the rules engine. The updated position information is then
displayed on an Amazon Location map. If you haven't activated positioning, the
destination routes the position data when you update the static position
coordinates of your device.

The following code shows the format of the uplink message sent from
AWS IoT Core for LoRaWAN with the position information, accuracy, solver configuration, and
the wireless metadata. The fields highlighted below are optional. If there's no
vertical accuracy information, the value is `null`.

```
{
    // Position configuration parameters for given wireless device
    "WirelessDeviceId": `"5b58245e-146c-4c30-9703-0ca942e3ff35"`,

    // Position information for a device in GeoJSON format. Altitude
    // is optional. If no vertical accuracy information is available
    // or positioning isn't activated, the value is set to null.
    // The position information coordinates are listed in the order
    // [longitude, latitude, altitude].
    "coordinates": [`33.33000183105469, -22.219999313354492`, 99.0],
    "type": "Point",
    "properties": {
         "horizontalAccuracy": `number`,
         "verticalAccuracy": number",
         "timestamp": "2022-08-19T03:08:35.061Z"
    },

    //Parameters controlled by AWS IoT Core for LoRaWAN
    "WirelessMetadata":
    {
        "LoRaWAN":
        {
            "ADR": false,
            "Bandwidth": `125`,
            "ClassB": false,
            "CodeRate": "`4/5`",
            "DataRate": "0",
            "DevAddr": "`00b96cd4`",
            "DevEui": "`58a0cb000202c99`",
            "FOptLen": 2,
            "FCnt": 1,
            "Fport": `136`,
            "Frequency": "`868100000`",
            "Gateways": [
             {
                    "GatewayEui": "`80029cfffe5cf1cc`",
                    "Snr": `-29`,
                    "Rssi": `9.75`
             }
             ],
            "MIC": "`7255cb07`",
            "MType": "UnconfirmedDataUp",
            "Major": "LoRaWANR1",
            "Modulation": "LORA",
            "PolarizationInversion": false,
            "SpreadingFactor": `12`,
            "Timestamp": "`2021-05-03T03:24:29Z`"

        }
    }
}
```

## Configuring position of your

devices using the console

To configure and manage the position of your devices by using the AWS Management Console, first
sign in to the console and then go to the [**Devices**](https://console.aws.amazon.com/iot/home#/wireless/devices "https://console.aws.amazon.com/iot/home#/wireless/devices") hub page of the AWS IoT console.

###### Add position information

To add position information for your device:

1. In the **Devices** hub page, choose **Add
   wireless device**.
2. Enter the wireless device specification, device and service profiles, and
   the destination that defines the IoT rule for routing the data to other
   AWS services. For more information, see [Onboard your devices to
   AWS IoT Core for LoRaWAN](lorawan-onboard-end-devices.md "lorawan-onboard-end-devices.md").
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

## Configure device position using the

API

You can specify the position information, configure the device position, and
activate optional geolocation using the AWS IoT Wireless API or the AWS CLI.

###### Important

The API actions [UpdatePosition](../../2020-11-22/apireference/API_UpdatePosition.md "../../2020-11-22/apireference/API_UpdatePosition.md"), [GetPosition](../../2020-11-22/apireference/API_GetPosition.md "../../2020-11-22/apireference/API_GetPosition.md"), [PutPositionConfiguration](../../2020-11-22/apireference/API_PutPositionConfiguration.md "../../2020-11-22/apireference/API_PutPositionConfiguration.md"), [GetPositionConfiguration](../../2020-11-22/apireference/API_GetPositionConfiguration.md "../../2020-11-22/apireference/API_GetPositionConfiguration.md"), and [ListPositionConfigurations](../../2020-11-22/apireference/API_ListPositionConfigurations.md "../../2020-11-22/apireference/API_ListPositionConfigurations.md") are no longer supported. Calls to update
and retrieve the position information should use the [GetResourcePosition](../../2020-11-22/apireference/API_GetResourcePosition.md "../../2020-11-22/apireference/API_GetResourcePosition.md") and [UpdateResourcePosition](../../2020-11-22/apireference/API_UpdateResourcePosition.md "../../2020-11-22/apireference/API_UpdateResourcePosition.md") API operations instead.

### Add position information and

configuration

To add the position information for a given wireless device, specify the
coordinates using the [UpdateResourcePosition](../../2020-11-22/apireference/API_UpdateResourcePosition.md "../../2020-11-22/apireference/API_UpdateResourcePosition.md") API operation or the [update-resource-position](../../../cli/latest/reference/iotwireless/update-resource-position.md "../../../cli/latest/reference/iotwireless/update-resource-position.md") CLI command. Specify
`WirelessDevice` as the `ResourceType`, the ID of the
wireless device to be updated as the `ResourceIdentifier`, and the
position information.

```
aws iotwireless update-resource-position \
    --resource-type WirelessDevice \
    --resource-id `"1ffd32c8-8130-4194-96df-622f072a315f"` \
    --position [33.33, -33.33, 10.0]
```

The following shows the contents of the
`deviceposition.json` file. To
specify the FPort values for sending the geolocation data, use the [Positioning](../../2020-11-22/apireference/API_Positioning.md "../../2020-11-22/apireference/API_Positioning.md") object
with the [CreateWirelessDevice](../../2020-11-22/apireference/API_CreateWirelessDevice.md "../../2020-11-22/apireference/API_CreateWirelessDevice.md") and [UpdateWirelessDevice](../../2020-11-22/apireference/API_UpdateWirelessDevice.md "../../2020-11-22/apireference/API_UpdateWirelessDevice.md") API operations.

**Contents of deviceposition.json**

```
{
     "type": "Point",
     "coordinates": `[33.3318, -22.2155, 13.123]`,
     "properties": {
          "verticalAccuracy": 707,
          "horizontalAccuracy":
          "timestamp": `"2018-11-30T18:35:24Z"`
      }
}
```

Running this command doesn't produce any output. To see the position
information that you specified, use the `GetResourcePosition` API
operation.

### Get position information and

configuration

To get the position information for a given wireless device, use the [GetResourcePosition](../../2020-11-22/apireference/API_GetResourcePosition.md "../../2020-11-22/apireference/API_GetResourcePosition.md") API or the [get-resource-position](../../../cli/latest/reference/iotwireless/get-resource-position.md "../../../cli/latest/reference/iotwireless/get-resource-position.md") CLI command. Specify
`WirelessDevice` as the `resourceType` and provide the
ID of the wireless device as the `resourceIdentifier`.

```
aws iotwireless get-resource-position \
    --resource-type WirelessDevice \
    --resource-id "`1ffd32c8-8130-4194-96df-622f072a315f`"
```

Running this command displays the position information of your wireless device
as a GeoJSON payload. You'll see information about the position coordinates, the
location type, and properties which can include the accuracy information and the
timestamp which corresponds to the last known position of the device.

```
{
     "type": "Point",
     "coordinates": `[33.3318, -22.2155, 13.123]`,
     "properties": {
          "verticalAccuracy": 707,
          "horizontalAccuracy": 389,
          "horizontalConfidenceLevel": 0.68,
          "verticalConfidenceLevel": 0.68,
          "timestamp": `"2018-11-30T18:35:24Z"`
      }
}
```
