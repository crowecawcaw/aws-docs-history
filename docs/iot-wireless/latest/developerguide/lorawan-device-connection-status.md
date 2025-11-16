# Connect your LoRaWAN device and

verify its connection status

Before you can check the device connection status, you must have already added
your device and connected it to AWS IoT Core for LoRaWAN. For information about how to add your
device, see [Add your wireless device to
AWS IoT Core for LoRaWAN](lorawan-end-devices-add.md "lorawan-end-devices-add.md").

After you've added your device, refer to your device's user manual to learn how to
initiate sending an uplink message from your LoRaWAN device.

## Wireless device destination

payload

The following code shows the payload received at the destination for your
wireless device. It shows a sample payload when using your own private LoRaWAN
gateway, and when you use a public network. It also shows the payload format if
you exclude the gateway metadata information. The following shows a sample
payload.

```
HTTP/1.1 200
Content-type: application/json

{
  "LastUplinkReceivedAt": "2021-03-24T23:13:08.476015749Z",
  "LoRaWAN": {
        "DataRate": 5,
        "DevEui": "647fda0000006420",
        "Frequency": 868100000,
        "Gateways": [
         {
            "GatewayEui": "c0ee40ffff29df10",
            "Rssi": -67,
            "Snr": 9.75
         }
      ],
  "WirelessDeviceId": "30cbdcf3-86de-4291-bfab-5bfa2b12bad5"
}
```

This example uses a private LoRaWAN gateway to show the gateway
metadata information in the uplink message. The metadata consists of the
gateway EUI, SNR (signal to noise ratio), and RSSI (Received signal to
strength indicator). These values can help you determine the strength of
your gateway channel and whether to switch to a stronger channel.

```
{
    "MessageId": "d8374454-f361-4907-9f3f-ca53233bb281",
    "WirelessDeviceId": "d7c96c47-6058-46d6-a033-c67d28c2243c",
    "PayloadData": "wOr7P9SI8tsIgMl0=",
    "WirelessMetadata":
    {
        "LoRaWAN":
        {
            "ADR": false,
            "Bandwidth": 125,
            "ClassB": false,
            "CodeRate": "4/5",
            "DataRate": "0",
            "DevAddr": "725dd3eb",
            "DevEui": "ac1f09fffe081943",
            "FCnt": 5,
            "FOptLen": 0,
            "FPort": 1,
            "Frequency": "868300000",
            "Gateways": [
                {
                 "GatewayEui": "2cf7f11053100080",
                 "Rssi": -34,
                 "Snr": 9.5
                }
            ],
            "MIC": "9eb0337c",
            "MType": "UnconfirmedDataUp",
            "Major": "LoRaWANR1",
            "Modulation": "LORA",
            "PolarizationInversion": false,
            "SpreadingFactor": 12,
            "Timestamp": "2023-12-01T16:16:11Z"
        }
    }
}
```

You can also connect to the public network instead of your own private
LoRaWAN gateway. The public network is provided and operated as a
service directly by Everynet. The following example shows the public
LoRaWAN network metadata in the message. The metadata consists of the ID
of the gateway and the network provider (Everynet), whether downlink is
allowed, and the SNR and RSSI values. For more infrrmation about the
public network, see [Managing LoRaWAN traffic from public networks
(Everynet)](iot-lorawan-roaming.md "iot-lorawan-roaming.md").

###### Note

The uplink message will mention `PublicGateways` to
indicate that it's received from the public network and not a
private LoRaWAN gateway.

```
{
    "MessageId": "d8374454-f361-4907-9f3f-ca53233bb281",
    "WirelessDeviceId": "d7c96c47-6058-46d6-a033-c67d28c2243c",
    "PayloadData": "wOr7P9SI8tsIgMl0=",
    "WirelessMetadata":
    {
        "LoRaWAN":
        {
            "ADR": false,
            "Bandwidth": 125,
            "ClassB": false,
            "CodeRate": "4/5",
            "DataRate": "0",
            "DevAddr": "725dd3eb",
            "DevEui": "ac1f09fffe081943",
            "FCnt": 5,
            "FOptLen": 0,
            "FPort": 1,
            "Frequency": "868300000",
            "PublicGateways": [
                {
                    "DlAllowed": true,
                    "Id": "3abe094",
                    "ProviderNetId": "0x0000b",
                    "RfRegion": "US915",
                    "Rssi": -12,
                    "Snr": 6.75
                }
            ],
            "MIC": "9eb0337c",
            "MType": "UnconfirmedDataUp",
            "Major": "LoRaWANR1",
            "Modulation": "LORA",
            "PolarizationInversion": false,
            "SpreadingFactor": 12,
            "Timestamp": "2023-12-01T16:16:11Z"
        }
    }
}
```

If you want to exclude the gateway metadata information from your
uplink metadata, disable the **AddGwMetadata**
parameter when you create the service profile. For information about
disabling this parameter, see [Add service profiles](lorawan-define-profiles.md#lorawan-service-profiles "lorawan-define-profiles.md#lorawan-service-profiles").

In this case, you won't see the `Gateways` section in the
uplink metadata, as illustrated in the following example.

```
{
    "MessageId": "d8374454-f361-4907-9f3f-ca53233bb281",
    "WirelessDeviceId": "d7c96c47-6058-46d6-a033-c67d28c2243c",
    "PayloadData": "wOr7P9SI8tsIgMl0=",
    "WirelessMetadata":
    {
        "LoRaWAN":
        {
            "ADR": false,
            "Bandwidth": 125,
            "ClassB": false,
            "CodeRate": "4/5",
            "DataRate": "0",
            "DevAddr": "725dd3eb",
            "DevEui": "ac1f09fffe081943",
            "FCnt": 5,
            "FOptLen": 0,
            "FPort": 1,
            "Frequency": "868300000",
            "MIC": "9eb0337c",
            "MType": "UnconfirmedDataUp",
            "Major": "LoRaWANR1",
            "Modulation": "LORA",
            "PolarizationInversion": false,
            "SpreadingFactor": 12,
            "Timestamp": "2023-12-01T16:16:11Z"
        }
    }
}
```

## Check device connection

status

The following sections show you how to check the connection status using the
AWS Management Console and the AWS CLI.

To check the connection status using the console, navigate to the
[**Devices**](https://console.aws.amazon.com/iot/home#/wireless/devices "https://console.aws.amazon.com/iot/home#/wireless/devices") page of the AWS IoT console
and choose the device you've added. In the **Details**
section of the Wireless devices details page, you'll see the date and
time the last uplink was received.

To check the connection status using the API, use the [`GetWirelessDeviceStatistics` API](../apireference/API_GetWirelessDeviceStatistics.md "../apireference/API_GetWirelessDeviceStatistics.md"). This API doesn't have a
request body and only contains a response body that shows when the last uplink
was received. The response from the API also indicates whether it's received
from a public network or a private LoRaWAN gateway.

## Next steps

Now that you have connected your device and verified the connection status,
you can observe the format of the uplink metadata recieved from the device by
using the [MQTT test
client](https://console.aws.amazon.com/iot/home#/test "https://console.aws.amazon.com/iot/home#/test") on the **Test** page of the AWS IoT console.
For more information, see [View format of uplink messages sent
from LoRaWAN devices](lorawan-uplink-metadata-format.md "lorawan-uplink-metadata-format.md").
