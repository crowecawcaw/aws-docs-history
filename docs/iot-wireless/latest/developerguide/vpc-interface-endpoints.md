

# AWS IoT Core for LoRaWAN and interface VPC endpoints (AWS PrivateLink)
<a name="vpc-interface-endpoints"></a>

You can connect directly to AWS IoT Core for LoRaWAN through [ Interface VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/vpc/latest/privatelink/vpce-interface.html) in your Virtual Private Cloud (VPC) instead of connecting over the public internet. When you use a VPC interface endpoint, communication between your VPC and AWS IoT Core for LoRaWAN is conducted entirely and securely within the AWS network.

AWS IoT Core for LoRaWAN supports Amazon Virtual Private Cloud interface endpoints that are powered by AWS PrivateLink. Each VPC endpoint is represented by one or more [Elastic Network Interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) with private IP addresses in your VPC subnets. For more information, see [Interface VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html) in the *Amazon VPC User Guide*.

**Note**  
AWS IoT Core for LoRaWAN support both IPv6 and IPv4 address formats when communicating with the interface VPC endpoints using AWS PrivateLink. See [AWS services that support IPv6](https://docs.aws.amazon.com/general/latest/gr/aws-ipv6-support.html#ipv6-service-support).

For more information about VPC and endpoints, see [What is Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html#what-is-privatelink).

For more information about AWS PrivateLink, see [AWS PrivateLink and VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/endpoint-services-overview.html). 

## Considerations for AWS IoT Wireless VPC endpoints
<a name="vpc-endpoint-considerations"></a>

Before you set up an interface VPC endpoint for AWS IoT Wireless, ensure that you review [Interface endpoint properties and limitations](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#vpce-interface-limitations) in the *Amazon VPC User Guide*.

AWS IoT Wireless supports making calls to all of its API actions from your VPC. VPC endpoint policies are not supported for AWS IoT Wireless. By default, full access to AWS IoT Wireless is allowed through the endpoint. For more information, see [Controlling access to services with VPC endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-access.html) in the *Amazon VPC User Guide*. 

## AWS IoT Core for LoRaWAN privatelink architecture
<a name="vpc-endpoint-architecture"></a>

The following diagram shows the privatelink architecture of AWS IoT Core for LoRaWAN. The architecture uses a Transit Gateway and Route 53 Resolver to share the AWS PrivateLink interface endpoints between your VPC, the AWS IoT Core for LoRaWAN VPC, and an on-premises environment. You'll find a more detailed architecture diagram when setting up the connection to the VPC interface endpoints.

![Image showing how you can use AWS PrivateLink to connect to AWS IoT Core for LoRaWAN endpoints.](http://docs.aws.amazon.com/iot-wireless/latest/developerguide/images/iot-lorawan-privatelink-architecture.png)


## AWS IoT Core for LoRaWAN endpoints
<a name="vpc-lorawan-endpoints"></a>

AWS IoT Core for LoRaWAN has three public endpoints. Each public endpoint has a corresponding VPC interface endpoint. The public endpoints can be classified into control plane and data plane endpoints. For information about these endpoints, see [AWS IoT Core for LoRaWAN API endpoints](https://docs.aws.amazon.com/general/latest/gr/iot-core.html#iot-wireless_region).
+ 

**Control plane API endpoints**  
 You can use control plane API endpoints to interact with the AWS IoT Wireless APIs. These endpoints can be accessed from a client that is hosted in your Amazon VPC by using AWS PrivateLink.
+ 

**Data plane API endpoints**  
Data plane API endpoints are LoRaWAN Network Server (LNS) and Configuration and Update Server (CUPS) endpoints that you can use to interact with the AWS IoT Core for LoRaWAN LNS and CUPS endpoints. These endpoints can be accessed from your LoRa gateways on premises by using Site-to-Site VPN or AWS Direct Connect. You get these endpoints when onboarding your gateway to AWS IoT Core for LoRaWAN. For more information, see [Add a gateway to AWS IoT Core for LoRaWAN](lorawan-onboard-gateway-add.md).

**Topics**
+ [Considerations for AWS IoT Wireless VPC endpoints](#vpc-endpoint-considerations)
+ [AWS IoT Core for LoRaWAN privatelink architecture](#vpc-endpoint-architecture)
+ [AWS IoT Core for LoRaWAN endpoints](#vpc-lorawan-endpoints)
+ [Onboard AWS IoT Core for LoRaWAN control plane API endpoint](lorawan-onboard-control-endpoint.md)
+ [Onboard AWS IoT Core for LoRaWAN data plane API endpoints](onboard-lns-cups-endpoints.md)