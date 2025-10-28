# Onboard AWS IoT Core for LoRaWAN data plane API

endpoints

AWS IoT Core for LoRaWAN data plane endpoints consist of the following endpoints. You get these
endpoints when adding your gateway to AWS IoT Core for LoRaWAN. For more information, see [Add a gateway to AWS IoT Core for LoRaWAN](lorawan-onboard-gateway-add.md "lorawan-onboard-gateway-add.md").

- ###### LoRaWAN Network Server (LNS) endpoints

The LNS endpoints are of the format
``account-specific-prefix`.lns.lorawan.`region`.amazonaws.com`.
You can use this endpoint to establish a connection for exchanging LoRa
uplink and downlink messages.

- ###### Configuration and Update Server (CUPS) endpoints

The CUPS endpoints are of the format
``account-specific-prefix`.cups.lorawan.`region`.amazonaws.com`.
You can use this endpoint for credentials management, remote configuration,
and firmware update of gateways.
For more information, see [Using CUPS and LNS protocols](lorawan-manage-gateways.md#lorawan-cups-lns-protocols "lorawan-manage-gateways.md#lorawan-cups-lns-protocols").

To find the Data Plane API endpoints for your AWS account and Region, use the [**get-service-endpoint**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/get-service-endpoint.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/get-service-endpoint.html") CLI command shown here, or the
[`GetServiceEndpoint`](../../../iotwireless/latest/apireference/API_GetServiceEndpoint.md "../../../iotwireless/latest/apireference/API_GetServiceEndpoint.md") REST API. For more
information, see [AWS IoT Core for LoRaWAN Data Plane API Endpoints](../../../general/latest/gr/iot-core.md#iot-core.html#iot-wireless-data-plane-endpoints "../../../general/latest/gr/iot-core.md#iot-core.html#iot-wireless-data-plane-endpoints").

You can connect your LoRaWAN gateway on premises to communicate with AWS IoT Core for LoRaWAN
endpoints. To establish this connection, first connect your on premises gateway to your
AWS account in your VPC by using a VPN connection. You can then communicate with the
data plane interface endpoints in the AWS IoT Core for LoRaWAN VPC that are powered by
privatelink.

###### The following shows how to onboard these endpoints.

- [Create VPC interface endpoint and private
  hosted zone](create-vpc-lns-cups.md "create-vpc-lns-cups.md")
- [Use VPN to connect LoRa gateways to
  your AWS account](lorawan-vpc-vpn-connection.md "lorawan-vpc-vpn-connection.md")
