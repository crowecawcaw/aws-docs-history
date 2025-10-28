# Connect your LoRaWAN gateway and

verify its connection status

Before you can check the gateway connection status, you must have already added
your gateway and connected it to AWS IoT Core for LoRaWAN. For information about how to add
your gateway, see [Add a gateway to AWS IoT Core for LoRaWAN](lorawan-onboard-gateway-add.md "lorawan-onboard-gateway-add.md").

###### Note

AWS IoT Core for LoRaWAN supports communication using both the IPv4 and IPv6 address format.
To enable IPv6 support for your account-specific CUPS and LNS endpoints, if you've
already onboarded your LoRaWAN gateways before December 1st, 2024, you must request
IPv6 activation. For more information, see [IPv6 activation for data plane endpoints](wireless-ipv6-access.md#iot-wireless-ipv6-activation "wireless-ipv6-access.md#iot-wireless-ipv6-activation").

## Connect your gateway to

AWS IoT Core for LoRaWAN

After you've added your gateway, connect to the configuration interface of
your gateway to enter the configuration information and trust
certificates.

After adding the gateway's information to AWS IoT Core for LoRaWAN, add some
AWS IoT Core for LoRaWAN information to the gateway device. The documentation provided by
the gateway's vendor should describe the process for uploading the certificate
files to the gateway and configuring the gateway device to communicate with
AWS IoT Core for LoRaWAN.

###### Gateways qualified for use with AWS IoT Core for LoRaWAN

For instructions on how to configure your LoRaWAN gateway, refer to the
[configure gateway device](https://iotwireless.workshop.aws/en/200_gateway/400_configuregateway.html "https://iotwireless.workshop.aws/en/200_gateway/400_configuregateway.html") section of the AWS IoT Core for LoRaWAN
workshop. Here, you'll find information about instructions for connecting
gateways that are qualified for use with AWS IoT Core for LoRaWAN.

###### Gateways that support CUPS protocol

The following instructions show how you can connect your gateways that
support the CUPS protocol.

1. Upload the following files that you obtained when adding your
   gateway.
   - Gateway device certificate and private key files.
   - Trust certificate file for CUPS endpoint,
     `cups.trust`.

2. Specify the CUPS endpoint URL that you obtained previously. The
   endpoint will be of the format
   ``prefix`.cups.lorawan.`region`.amazonaws.com:443`.

For details about how to obtain this information, see [Add a gateway to AWS IoT Core for LoRaWAN](lorawan-onboard-gateway-add.md "lorawan-onboard-gateway-add.md").

###### Gateways that support LNS protocol

The following instructions show how you can connect your gateways that
support the LNS protocol.

1. Upload the following files that you obtained when adding your
   gateway.
   - Gateway device certificate and private key files.
   - Trust certificate file for LNS endpoint,
     `lns.trust`.

2. Specify the LNS endpoint URL that you obtained previously. The
   endpoint will be of the format
   https://``prefix`.lns.lorawan.`region`.amazonaws.com:443`.

For details about how to obtain this information, see [Add a gateway to AWS IoT Core for LoRaWAN](lorawan-onboard-gateway-add.md "lorawan-onboard-gateway-add.md").

After that you've connected your gateway to AWS IoT Core for LoRaWAN, you can check the
status of your connection and get information about when the last uplink was
received by using the console or the API.

## Check gateway connection

status using the console

To check the connection status using the console, navigate to the [**Gateways**](https://console.aws.amazon.com/iot/home#/wireless/gateways "https://console.aws.amazon.com/iot/home#/wireless/gateways") page of the AWS IoT console and
choose the gateway you've added. In the **LoRaWAN specific
details** section of the Gateway details page, you'll see the
connection status and the date and time the last uplink was received.

## Check gateway connection status

using the API

To check the connection status using the API, use the
`GetWirelessGatewayStatistics` API. This API doesn't have a
request body and only contains a response body that shows whether the gateway is
connected and when the last uplink was received.

```
HTTP/1.1 200
Content-type: application/json

{
    "ConnectionStatus": "Connected",
    "LastUplinkReceivedAt": "2021-03-24T23:13:08.476015749Z",
    "WirelessGatewayId": "30cbdcf3-86de-4291-bfab-5bfa2b12bad5"
}
```

## Enable connection status

events

You can also enable connection status events to receive notications about status
updates to your gateway connection. You will be notified when a gateway becomes
connected, or when it's disconnected. For more information about these events and
how to enable them, see [Enable notifications for LoRaWAN
gateway connection status events](iot-lorawan-gateway-events.md "iot-lorawan-gateway-events.md").
