# AWS IoT Core for LoRaWAN

AWS IoT Core for LoRaWAN is a fully managed LoRaWAN network server (LNS) that provides gateway
management using the Configuration and Update Server (CUPS) and Firmware Updates Over-The-Air
(FUOTA) capabilities. You can replace your private LNS with AWS IoT Core for LoRaWAN and connect your Long
Range Wide Area Network (LoRaWAN) devices and gateways to AWS IoT Core. By doing so, you'll reduce
the maintenance, operational costs, setup time, and overhead costs.

###### Note

AWS IoT Core for LoRaWAN supports communication using both the IPv4 and IPv6 address format. See [AWS services
that support IPv6](../../../general/latest/gr/aws-ipv6-support.md#ipv6-service-support "../../../general/latest/gr/aws-ipv6-support.md#ipv6-service-support").

## Introduction

LoRaWAN devices are long-range, low-power, battery-operated devices that use the LoRaWAN
protocol to operate in a license-free radio spectrum. LoRaWAN is a Low Power Wide Area Network
(LPWAN) communication protocol that is built on LoRa. LoRa is the physical layer protocol that
enables low power, wide-area communication between devices.

To connect your LoRaWAN devices to AWS IoT, you must use a LoRaWAN gateway. The gateway acts
as a bridge to connect your device to AWS IoT Core for LoRaWAN and to exchange messages. AWS IoT Core for LoRaWAN uses
the AWS IoT rules engine to route the messages from your LoRaWAN devices to other AWS IoT services.

To reduce development effort and quickly onboard your devices to AWS IoT Core for LoRaWAN, we recommend
that you use LoRaWAN-certified end devices. For more information, see the [AWS IoT Core for LoRaWAN product overview](https://aws.amazon.com/iot-core/lorawan "https://aws.amazon.com/iot-core/lorawan") page. For information about
getting your devices LoRaWAN certified, see [Certifying LoRaWAN products](https://lora-alliance.org/lorawan-certification/ "https://lora-alliance.org/lorawan-certification/").

## Features of AWS IoT Core for LoRaWAN

With AWS IoT Core for LoRaWAN, you can:

- Onboard and connect LoRaWAN devices and gateways to AWS IoT without the need to set up and
  manage a private LNS.
- Connect LoRaWAN devices that comply to 1.0.x or 1.1 LoRaWAN specifications standardized by
  LoRa Alliance. These devices can operate in class A, class B, or class C mode.
- Use LoRaWAN gateways that support LoRa Basics Station version 2.0.4 or later. All gateways
  that are qualified for AWS IoT Core for LoRaWAN run a compatible version of LoRa Basics Station.
- Connect your LoRaWAN devices to the cloud using publicly available LoRaWAN networks, which
  reduces the time to deployment, and eliminates the need for managing a private LoRaWAN network,
  thereby saving time and cost.
- Monitor signal strength, bandwidth, and spreading factor by using AWS IoT Core for LoRaWAN's adaptive
  data rate, and optimize the data rate if needed. You can also use network analyzer to monitor
  your LoRaWAN resources in real-time.
- Update LoRaWAN gateways' firmware using the CUPS service and the firmware of LoRaWAN
  devices using Firmware Updates Over-The-Air (FUOTA).

## Accessing AWS IoT Core for LoRaWAN

You can quickly onboard your LoRaWAN devices and gateways to AWS IoT Core for LoRaWAN by using the
console or the AWS IoT Wireless API.

###### Using the console

To onboard your LoRaWAN devices and gateways by using the AWS Management Console, sign in to the
AWS Management Console and navigate to the [AWS IoT Core for LoRaWAN](https://console.aws.amazon.com/iot/home#/wireless/landing "https://console.aws.amazon.com/iot/home#/wireless/landing") page in the AWS IoT console. You can then use the
**Intro** section to add your gateways and devices to AWS IoT Core for LoRaWAN. For more
information, see [Using the console to onboard your device and gateway
to AWS IoT Core for LoRaWAN](lorawan-getting-started.md#lorawan-console "lorawan-getting-started.md#lorawan-console").

###### Using the API or CLI

You can onboard both LoRaWAN and
Sidewalk
devices by using the [AWS IoT Wireless](../apireference.md "../apireference.md") API. The
AWS IoT Wireless API that AWS IoT Core for LoRaWAN is built on is supported by the AWS SDK. For more
information, see [AWS SDKs and
Toolkits](https://aws.amazon.com/developer/tools/ "https://aws.amazon.com/developer/tools/").

You can use the AWS CLI to run commands for onboarding and managing your LoRaWAN gateways and
devices. For more information, see [AWS IoT Wireless CLI reference](../../../cli/latest/reference/iotwireless/index.md "../../../cli/latest/reference/iotwireless/index.md").

## AWS IoT Core for LoRaWAN Regions and

endpoints

AWS IoT Core for LoRaWAN provides support for control plane and data plane API endpoints that are
specific to your AWS Region. The data plane API endpoints are specific to your AWS account
and AWS Region. For more information about the AWS IoT Core for LoRaWAN endpoints, see [AWS IoT Core for LoRaWAN
Endpoints](../../../general/latest/gr/iot-core.md#iot-wireless_region "../../../general/latest/gr/iot-core.md#iot-wireless_region") in the _AWS General Reference_.

For more secure communication between your devices and AWS IoT, you can connect your devices
to AWS IoT Core for LoRaWAN through AWS PrivateLink in your virtual private cloud (VPC), instead of connecting
over the public internet. For more information, see [AWS IoT Core for LoRaWAN and interface VPC endpoints
(AWS PrivateLink)](vpc-interface-endpoints.md "vpc-interface-endpoints.md").

AWS IoT Core for LoRaWAN has quotas that apply to device data that is transmitted between the devices
and the maximum TPS for the AWS IoT Wireless API operations. For more information, see [AWS IoT Core for LoRaWAN
quotas](../../../general/latest/gr/iot-core.md#wireless-limits "../../../general/latest/gr/iot-core.md#wireless-limits") in the _AWS General Reference_.

## AWS IoT Core for LoRaWAN pricing

If you're a new customer, when you sign up for AWS, you can get started with AWS IoT Core for LoRaWAN
for free by using the [AWS Free Tier](https://aws.amazon.com/free/ "https://aws.amazon.com/free/"). With
AWS IoT Core for LoRaWAN, you only pay for what you use. For more information about general product overview
and pricing, see [AWS IoT Core
pricing](https://aws.amazon.com/iot-core/pricing/ "https://aws.amazon.com/iot-core/pricing/").
