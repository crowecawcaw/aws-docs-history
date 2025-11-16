# Configure beaconing for your

LoRaWAN gateways

If you onboard class B wireless devices to AWS IoT Core for LoRaWAN, the devices receive downlink
messages in scheduled time slots. The devices open these slots based on
time-synchronized beacons that are transmitted by the gateway. For your gateways to
transmit these time-synchronous beacons, you can use AWS IoT Core for LoRaWAN to configure certain
beaconing-related parameters for the gateways.

To configure these beaconing parameters, your gateway must be running LoRa Basics
Station software version 2.0.6. See [Using qualified gateways from the AWS
Partner Device Catalog](lorawan-manage-gateways.md#lorawan-qualified-gateways "lorawan-manage-gateways.md#lorawan-qualified-gateways").

## How to configure the beaconing

parameters

###### Note

You only need to configure the beaconing parameters for your gateway if it's
communicating with a class B wireless device.

You configure the beaconing parameters when adding your gateway to AWS IoT Core for LoRaWAN
using the [`CreateWirelessGateway`](../apireference/API_CreateWirelessGateway.md "../apireference/API_CreateWirelessGateway.md") API operation. When you invoke
the API operation, specify the following parameters using the `Beaconing`
object for your gateways. After you configure the parameters, the gateways will send
the beacons to your devices at a 128-second interval.

- `DataRate`: The data rate for the gateways that are
  transmitting the beacons.
- `Frequencies`: The list of frequencies for the gateways to
  transmit the beacons.

The following example shows how you configure these parameters for the gateway.
The `input.json` file will contain additional details, such as the
gateway certificate and provisioning credentials. For more information about adding
your gateway to AWS IoT Core for LoRaWAN using the `CreateWirelessGateway` API
operation, see [Add a gateway by using the
API](lorawan-onboard-gateway-add.md#lorawan-onboard-gateway-api "lorawan-onboard-gateway-add.md#lorawan-onboard-gateway-api").

###### Note

The beaconing parameters aren't available when you add your gateway to
AWS IoT Core for LoRaWAN using the AWS IoT console.

```
aws iotwireless create-wireless-gateway \
    --name "`myLoRaWANGateway`" \
    --cli-input-json `file://input.json`
```

The following shows the contents of the `input.json` file.

**Contents of input.json**

```
{
    "Description": `"My LoRaWAN gateway"`,
    "LoRaWAN": {
        "Beaconing": {
          "DataRate": `8`,
          "Frequencies": `[923300000,923900000]`
        },
        "GatewayEui": "`a1b2c3d4567890ab`",
        "RfRegion": `US915`,
        "JoinEuiFilters": `[
 ["0000000000000001", "00000000000000ff"],
 ["000000000000ff00", "000000000000ffff"]
 ]`,
        "NetIdFilters": `["000000", "000001"]`,
        "RfRegion": "US915",
        "SubBands": `[2]`
    }
}
```

The following code shows a sample output of running this command.

```
{
    "Arn": "arn:aws:iotwireless:`us-east-1`:`400232685877aa`:WirelessGateway/`a01b2c34-d44e-567f-abcd-0123e445663a`",
    "Id": `a01b2c34-d44e-567f-abcd-0123e445663a`"
}
```

## Get information about the beaconing

parameters

You can get information about the beaconing parameters for your gateway using the
[`GetWirelessGateway`](../apireference/API_GetWirelessGateway.md "../apireference/API_GetWirelessGateway.md") API operation.

###### Note

If a gateway has already been onboarded, you can't use the
`UpdateWirelessGateway` API operation to configure the beaconing
parameters. To configure the parameters, you must delete the gateway and then
specify the parameters when adding your gateway using the
`CreateWirelessGateway` API operation.

```
aws iotwireless get-wireless-gateway \
    --identifier "12345678-a1b2-3c45-67d8-e90fa1b2c34d" \
    --identifier-type WirelessGatewayId
```

Running this command returns information about your gateway and the beaconing
parameters.
