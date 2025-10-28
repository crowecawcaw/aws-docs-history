# View format of uplink messages sent

from LoRaWAN devices

To faciliate seamless connection between your LoRaWAN devices and the cloud, you can
use AWS IoT Core for LoRaWAN. The AWS IoT Core for LoRaWAN service provides secure and reliable data exchange
between your LoRaWAN devices and AWS IoT Core. It acts as a bridge, translating the LoRaWAN
protocol into MQTT messages that can be seamlessly ingested by AWS IoT Core. You can use
this capability in applications, such as real-time data processing, device state
management, and integration with other AWS services.

After you've connected your LoRaWAN device to AWS IoT Core for LoRaWAN, your devices can start
sending messages to the cloud. Uplink messages are messages that are sent from your
device and received by AWS IoT Core for LoRaWAN. Your LoRaWAN devices can send uplink messages at
any time, which are then forwarded to other AWS services and cloud-hosted
applications. Messages that are sent from AWS IoT Core for LoRaWAN and other AWS services and
applications to your devices are called downlink messages.

This topic shows how you can observe the format of the uplink message that you'll
receive from your wireless device.

## Before you can observe

the uplink messages

You must have onboarded your wireless device and connected your device to
AWS IoT so that it can transmit and receive data. For information about onboarding
your device to AWS IoT Core for LoRaWAN, see [Onboard your devices to
AWS IoT Core for LoRaWAN](lorawan-onboard-end-devices.md "lorawan-onboard-end-devices.md").

## What do the uplink messages

contain?

LoRaWAN devices connect to AWS IoT Core for LoRaWAN by using LoRaWAN gateways. The
uplink message that you receive from the device will contain the following
information.

- Payload data that corresponds to the encrypted payload message that is
  sent from the wireless device.
- Wireless metadata that includes:

      + Device information such as DevEui, the data rate, and the
       frequency channel in which the device is operating.
      + Optional additional parameters and the gateway information for
       gateways that are connected to the device. The gateway
       parameters include the gateway's EUI, the SNR, and RSSi.

  By using the wireless metadata, you can obtain useful information
  about the wireless device and the data that is transmitted between your
  device and AWS IoT. For example, you can use the
  `AckedMessageId` parameter to check whether the last
  confirmed downlink message has been received by the device. Optionally,
  if you choose to include the gateway information, you can identify
  whether you want to switch to a stronger gateway channel that's closer
  to your device.

## How to observe the uplink

messages?

After you've onboarded your device, you can use the [MQTT test client](https://console.aws.amazon.com/iot/home#/test "https://console.aws.amazon.com/iot/home#/test") on
the **Test** page of the AWS IoT console to subscribe to the
topic that you specified when creating your destination. You'll start to see
messages after your device is connected and starts sending payload data.

This diagram identifies the key elements in a LoRaWAN system connected to
AWS IoT Core for LoRaWAN, which shows the primary data plane and how data flows through the
system.

![Image showing how AWS IoT Core for LoRaWAN data is passed from a wireless device to AWS IoT and other services.](/images/iot-wireless/latest/developerguide/images/iot-lorawan-data-flow.png)

When the wireless device starts sending uplink data, AWS IoT Core for LoRaWAN wraps the
wireless metadata information with the payload and then sends it to your AWS
applications.

## Uplink message

examples

The following examples show the format of the uplink message received from
your device. The format includes the gateway metadata that varies depending on
whether you're using the public network, or your own private LoRaWAN gateway
that you onboarded to AWS IoT Core for LoRaWAN.

This example uses a private LoRaWAN gateway to show the gateway
metadata information in the uplink message. The metadata consists of the
gateway EUI, SNR (signal to noise ratio), and RSSI (Received signal to
strength indicator). These values can help you determine the strength of
your gateway channel and whether to switch to a stronger channel.

In the metadata, the field:

- `Battery` indicates the battery level reported by
  the device. It ranges from 0 to 255. 0 indicates that the device
  is connected to an external power source. 1 and 254 are the
  minimum and maximum battery levels. A value of 255 indicates
  that the device cannot measure the battery level.
- `Margin` represents the demodulation SNR
  (signal-to-noise ratio) in dB rounded to the nearest integer
  value. It ranges from -32 to +31.

```
{
    "WirelessDeviceId": "5b58245e-146c-4c30-9703-0ca942e3ff35",
    "PayloadData": "Cc48AAAAAAAAAAA=",
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
            "Battery": 210,
            "Margin": -6,
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
            "Timestamp": "2021-05-03T03:24:29Z"

        }
    }
}
```

You can also connect to the public network instead of your own private
LoRaWAN gateway. The public network is provided and operated as a
service directly by Everynet. The following example shows the public
LoRaWAN network metadata in the uplink message. The metadata consists of
the ID of the gateway and the network provider (Everynet), whether
downlink is allowed, and the SNR and RSSI values. For more infrrmation
about the public network, see [Managing LoRaWAN traffic from public networks
(Everynet)](iot-lorawan-roaming.md "iot-lorawan-roaming.md").

###### Note

The uplink message will mention `PublicGateways` to
indicate that it's received from the public network and not a
private LoRaWAN gateway.

```
{
    "WirelessDeviceId": "5b58245e-146c-4c30-9703-0ca942e3ff35",
    "PayloadData": "Cc48AAAAAAAAAAA=",
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
            "PublicGateways": [
                {
                    "DlAllowed": true,
                    "Id": "0x3abe094",
                    "ProviderNetId": "0x0000b",
                    "RfRegion": "US915",
                    "Rssi": -12,
                    "Snr": 6.75
                }
            ],
            "MIC": "7255cb07",
            "MType": "UnconfirmedDataUp",
            "Major": "LoRaWANR1",
            "Modulation": "LORA",
            "PolarizationInversion": false,
            "SpreadingFactor": 12,
            "Timestamp": "2021-05-03T03:24:29Z"

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
    "WirelessDeviceId": "0d9a439b-e77a-4573-a791-49d5c0f4db95",
    "PayloadData": "AAAAAAAA8=",
    "WirelessMetadata": {
        "LoRaWAN": {
            "ClassB": false,
            "CodeRate": "4/5",
            "DataRate": "1",
            "DevAddr": "01920f27",
            "DevEui": "ffffff10000163b0",
            "FCnt": 1,
            "FPort": 5,
            "Battery": 125,
            "Margin": -12,
            "Timestamp": "2021-04-29T05:19:43.646Z"
    }
  }
}
```
