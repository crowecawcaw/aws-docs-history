

# AWS IoT Core for Amazon Sidewalk
<a name="iot-sidewalk"></a>

AWS IoT Core for Amazon Sidewalk provides the cloud services that you can use to connect your Sidewalk-enabled devices to the AWS Cloud and use other AWS services.

Amazon Sidewalk is a secure community network that uses Amazon Sidewalk Gateways (also called Sidewalk Bridges), such as compatible Amazon Echo and Ring devices, to provide cloud connectivity for IoT; endpoint devices. Amazon Sidewalk enables low-bandwidth and long-range connectivity at home and beyond using Bluetooth Low Energy for short-distance communication and LoRa and FSK radio protocols at 900MHz frequencies to cover longer distances.

AWS IoT Core for AWS IoT Core for Amazon Sidewalk acts as a bridge to move data between your Sidewalk -enabled devices and AWS Cloud services.

**Topics**
+ [Features of AWS IoT Core for Amazon Sidewalk](#sidewalk-features)
+ [Accessing AWS IoT Core for Amazon Sidewalk](#sidewalk-how-use)
+ [AWS IoT Core for Amazon Sidewalk Regions and endpoints](#sidewalk-regions-endpoints)
+ [AWS IoT Core for Amazon Sidewalk pricing](#iot-sidewalk-pricing)
+ [What is AWS IoT Core for Amazon Sidewalk?](what-is-iot-sidewalk.md)
+ [Get started using AWS IoT Core for Amazon Sidewalk](sidewalk-getting-started.md)
+ [Connecting to AWS IoT Core for Amazon Sidewalk](iot-sidewalk-onboard.md)
+ [Configuring the position of wireless resources with AWS IoT Core for Amazon Sidewalk](sidewalk-configure-location.md)
+ [Bulk provisioning devices with AWS IoT Core for Amazon Sidewalk](sidewalk-bulk-provisioning.md)

## Features of AWS IoT Core for Amazon Sidewalk
<a name="sidewalk-features"></a>

Using AWS IoT Core for Amazon Sidewalk, you can:
+ Onboard your Sidewalk end devices to AWS IoT using the AWS IoT console, AWS IoT Core for Amazon Sidewalk API operations, or AWS CLI commands.
+ Leverage the capabilities offered by the AWS Cloud.
+ Create a destination that uses AWS IoT rules to process incoming payload messages and to route the messages to over 20 AWS services and third-party applications.
+ Enable event notifications to receive messages about events such as when your Sidewalk end device has been provisioned or registered, or whether a downlink message has been successfully delivered to your device.
+ Log and monitor your Sidewalk end devices in real time, obtain useful insights, and identify and troubleshoot errors.
+ Associate your Sidewalk end devices with an AWS IoT thing, which helps you store a representation of your device on the cloud. Things in AWS IoT make it easier to search and manage your features, and access other AWS IoT Core features.
+ Enable "Position" to resolve the location data of your Amazon Sidewalk enabled devices in the cloud. For more information, see [Introduction to onboarding your Sidewalk devices](sidewalk-getting-started.md#sidewalk-gs-workflow)..

## Accessing AWS IoT Core for Amazon Sidewalk
<a name="sidewalk-how-use"></a>

You can onboard your Sidewalk end devices to AWS IoT by using the console or the AWS IoT Wireless API operations. After your devices are onboarded, their messages are sent to AWS IoT Core. You can then start developing your business applications on the AWS Cloud, which uses the data from your Amazon Sidewalk end devices.

**Using the console**  
To onboard your Sidewalk end devices, sign in to the AWS Management Console and navigate to the [Devices](https://console.aws.amazon.com/iot/home#/wireless/devices) page on the AWS IoT console. After your devices are onboarded, you can view and manage them on this page of the IoT console.

**Using the API or CLI**  
You can onboard both Sidewalk and LoRaWAN devices by using the [AWS IoT Wireless API operations](https://docs.aws.amazon.com/iot-wireless/latest/apireference/). The AWS IoT Wireless APIs are part of the AWS IoT Core and are supported by the AWS SDK. For more information, see [AWS SDKs and Toolkits](https://aws.amazon.com/developer/tools/). 

You can use the AWS CLI to run commands for onboarding and managing your Sidewalk end devices. For more information, see [AWS IoT Wireless CLI reference](https://docs.aws.amazon.com/cli/latest/reference/iotwireless/index.html). 

## AWS IoT Core for Amazon Sidewalk Regions and endpoints
<a name="sidewalk-regions-endpoints"></a>

Amazon Sidewalk is only available in the `us-east-1` AWS Region. AWS IoT Core for Amazon Sidewalk provides support for control plane and data plane API endpoints in this Region. The data plane API endpoints are specific to your AWS account. For more information, see see [AWS IoT Wireless Service endpoints](https://docs.aws.amazon.com/general/latest/gr/iot-core.html#iot-wireless_region) in the *AWS General Reference*.

AWS IoT Core for Amazon Sidewalk has quotas that apply to device data that is transmitted between the device and the AWS Cloud, and the maximum TPS for the AWS IoT Wireless API operations. For more information, see [AWS IoT Wireless quotas](https://docs.aws.amazon.com/general/latest/gr/iot-core.html#wireless-limits) in the *AWS General Reference*.

## AWS IoT Core for Amazon Sidewalk pricing
<a name="iot-sidewalk-pricing"></a>

When you sign up for AWS, you can get started with AWS IoT Core for Amazon Sidewalk for no charge by using the [AWS Free Tier](https://aws.amazon.com/free/). 

For more information about general product overview and pricing, see [AWS IoT Core pricing](https://aws.amazon.com/iot-core/pricing/).