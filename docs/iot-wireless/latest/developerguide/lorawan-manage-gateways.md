# Managing gateways with AWS IoT Wireless

Following are some important considerations when using your gateways with AWS IoT Core for LoRaWAN.
For information about how to add your gateway to AWS IoT Core for LoRaWAN, see [Onboard your gateways to
AWS IoT Core for LoRaWAN](lorawan-onboard-gateways.md "lorawan-onboard-gateways.md").

## LoRa Basics Station software

requirement

To connect to AWS IoT Core for LoRaWAN, your LoRaWAN gateway must have software called [LoRa Basics Station](https://doc.sm.tc/station/ "https://doc.sm.tc/station/") running on it. LoRa
Basics Station is an open source software that is maintained by Semtech Corporation and
distributed by their [GitHub](https://github.com/lorabasics/basicstation "https://github.com/lorabasics/basicstation") repository. AWS IoT Core for LoRaWAN supports LoRa Basics Station version 2.0.4
and later. The latest version is 2.0.6.

## Using qualified gateways from the AWS

Partner Device Catalog

The [AWS
Partner Device Catalog](https://devices.amazonaws.com/search?page=1&sv=iotclorawan "https://devices.amazonaws.com/search?page=1&sv=iotclorawan") contains gateways and developer kits that are
qualified for use with AWS IoT Core for LoRaWAN. We recommend that you use these qualified gateways
because you don't have to modify the embedding software for connecting the gateways to
AWS IoT Core. These gateways already have a version of the BasicStation software compatible
with AWS IoT Core for LoRaWAN.

###### Note

If you have a gateway that is not listed in the Partner Catalog as a qualified
gateway with AWS IoT Core for LoRaWAN, you might still be able to use it if the gateway is
running LoRa Basics Station software with version 2.0.4 and later. Make sure that
you use **TLS Server and Client Authentication** for authenticating
your LoRaWAN gateway.

## Using CUPS and LNS protocols

LoRa Basics Station software contains two sub protocols for connecting gateways to
network servers, LoRaWAN Network Server (LNS) and Configuration and Update Server
(CUPS) protocols.

The LNS protocol establishes a data connection between a LoRa Basics Station
compatible gateway and a network server. LoRa uplink and downlink messages are exchanged
through this data connection over secure WebSockets.

The CUPS protocol enables credentials management, and remote configuration and
firmware update of gateways. AWS IoT Core for LoRaWAN provides both LNS and CUPS endpoints for
LoRaWAN data ingestion and remote gateway management respectively.

For more information, see [LNS
protocol](https://doc.sm.tc/station/tcproto.html "https://doc.sm.tc/station/tcproto.html") and [CUPS
protocol](https://doc.sm.tc/station/cupsproto.html "https://doc.sm.tc/station/cupsproto.html").

###### Topics

- [Configure beaconing for your
  LoRaWAN gateways](lorawan-gateway-beaconing.md "lorawan-gateway-beaconing.md")
- [Configure subbands and filtering
  capabilities of your LoRaWAN gateways](lorawan-subband-filter-configuration.md "lorawan-subband-filter-configuration.md")
- [Choosing gateways to receive the LoRaWAN
  downlink data traffic](lorawan-gateway-participate.md "lorawan-gateway-participate.md")
- [Update gateway firmware using CUPS service
  with AWS IoT Core for LoRaWAN](lorawan-update-firmware.md "lorawan-update-firmware.md")
