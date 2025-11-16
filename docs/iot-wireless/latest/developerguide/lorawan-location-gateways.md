# Configuring the position of LoRaWAN

gateways

When you add your gateway to AWS IoT Core for LoRaWAN, you can specify the static position data.
If you've activated Amazon Location Service maps, the position data is displayed on an Amazon Location map.

###### Note

The third-party solvers can't be used with LoRaWAN gateways. For gateways, you
can still specify the static position coordinates. When solvers aren't used to
compute the position, such as in the case of gateways, the accuracy information will
be reported as `0.0`.

You can configure the gateway position using the AWS Management Console, the AWS IoT Wireless
API, or the AWS CLI.

## Configuring position of your

gateway using the console

To configure the position of your gateway resources by using the AWS Management Console, first
sign in to the console and then go to the [**Gateways**](https://console.aws.amazon.com/iot/home#/wireless/gateways "https://console.aws.amazon.com/iot/home#/wireless/gateways") hub page of the AWS IoT console.

###### Add position information

To add a position configuration for your gateway

1. In the **Gateways** hub page, choose **Add
   gateway**.
2. Enter the gateway's EUI, frequency band (RFRegion), and any additional
   gateway details and LoRaWAN configuration information. For more
   information, see [Add a gateway using the
   console](lorawan-onboard-gateway-add.md#lorawan-onboard-gateway-console "lorawan-onboard-gateway-add.md#lorawan-onboard-gateway-console").
3. Go to the **Position information - Optional** section,
   and enter the position information for your gateway using the latitude and
   longitude coordinates, and an optional altitude coordinate. The position
   information is based on the WGS84 coordinate system.

###### View gateway's position

After you've configured your gateway's position, AWS IoT Core for LoRaWAN creates an
Amazon Location map called `iotwireless.map`. You can see this map in the
details page of your gateway on the **Position** tab. Based on
the position coordinates that you specified, the position of your gateway will
be displayed as a marker on the map. You can zoom in or zoom out to clearly view
the position of your gateway on the map. On the **Position**
tab, you'll also see the accuracy information and the timestamp at which your
gateway's position was determined.

###### Note

If you don't have Amazon Location Service maps installed, you'll see a message indicating
that you must use Amazon Location Service to access the map and view the gateway position.
Using Amazon Location Service maps may incur additional charges to your AWS account. For more
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

###### Update gateway's position configuration

To change the gateway's position configuration, in the gateway details page,
choose **Edit** and then update the position information and
the destination.

###### Note

Information about historical position data isn't available. When you update
the gateway's position coordinates, it overwrites the previously reported
position data. After you've updated the position, in the
**Position** tab of the gateway details, you'll see the new
position information. The change in timestamp indicates that it corresponds to
the last known position of the gateway.

## Configure position of your gateway

using the API

You can specify the position information and configure the gateway position using
the AWS IoT Wireless API or the AWS CLI.

###### Important

The API actions [UpdatePosition](../apireference/API_UpdatePosition.md "../apireference/API_UpdatePosition.md"), [GetPosition](../apireference/API_GetPosition.md "../apireference/API_GetPosition.md"), [PutPositionConfiguration](../apireference/API_PutPositionConfiguration.md "../apireference/API_PutPositionConfiguration.md"), [GetPositionConfiguration](../apireference/API_GetPositionConfiguration.md "../apireference/API_GetPositionConfiguration.md"), and [ListPositionConfigurations](../apireference/API_ListPositionConfigurations.md "../apireference/API_ListPositionConfigurations.md") are no longer supported. Calls to update
and retrieve the position information should use the [GetResourcePosition](../apireference/API_GetResourcePosition.md "../apireference/API_GetResourcePosition.md") and [UpdateResourcePosition](../apireference/API_UpdateResourcePosition.md "../apireference/API_UpdateResourcePosition.md") API operations instead.

### Add position

information

To add the static position information for a given wireless gateway, specify
the coordinates using the [UpdateResourcePosition](../apireference/API_UpdateResourcePosition.md "../apireference/API_UpdateResourcePosition.md") API operation or the [update-resource-position](../../../cli/latest/reference/iotwireless/update-resource-position.md "../../../cli/latest/reference/iotwireless/update-resource-position.md") CLI command. Specify
`WirelessGateway` as the `ResourceType`, the ID of the
wireless gateway to be updated as the `ResourceIdentifier`, and the
position information as a GeoJSON payload.

```
aws iotwireless update-resource-position \
    --resource-type WirelessGateway \
    --resource-id `"12345678-a1b2-3c45-67d8-e90fa1b2c34d"` \
    --cli-input-json `file://gatewayposition.json`
```

The following shows the contents of the
`gatewayposition.json`
file.

**Contents of gatewayposition.json**

```
{
     "type": "Point",
     "coordinates": `[33.3318, -22.2155, 13.123]`,
     "properties": {
          "timestamp": `"2018-11-30T18:35:24Z"`
      }
}
```

Running this command doesn't produce any output. To see the position
information that you specified, use the `GetResourcePosition` API
operation.

### Get position

information

To get the position information for a given wireless gateway, use the [GetResourcePosition](../apireference/API_GetResourcePosition.md "../apireference/API_GetResourcePosition.md") API operation or the [get-resource-position](../../../cli/latest/reference/iotwireless/get-position.md "../../../cli/latest/reference/iotwireless/get-position.md") CLI command. Specify
`WirelessGateway` as the `resourceType` and provide
the ID of the wireless gateway as the `resourceIdentifier`.

```
aws iotwireless get-resource-position \
    --resource-type WirelessGateway \
    --resource-id `"12345678-a1b2-3c45-67d8-e90fa1b2c34d"`
```

Running this command displays the position information of your wireless
gateway as a GeoJSON payload. You'll see information about the position
coordinates, the type of position information, and additional properties, such
as the timestamp which corresponds to the last known position of the
gateway.

```
{
    {
    "type": "Point",
     "coordinates": [33.3318,-22.2155,13.123],
     "properties": {
         "timestamp": "2018-11-30T18:35:24Z"
         }
    }
}
```
