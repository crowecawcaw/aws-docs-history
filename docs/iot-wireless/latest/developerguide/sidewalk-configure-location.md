

# Configuring the position of wireless resources with AWS IoT Core for Amazon Sidewalk
<a name="sidewalk-configure-location"></a>

You can use AWS IoT Core for Amazon Sidewalk to configure the position of your Sidewalk devices and retrieve location data in real time. Geolocation is handled by the Amazon Sidewalk stack on the end device and triggered by the end device itself. The device collects location data and sends it to AWS IoT Core for Amazon Sidewalk, where you can retrieve it using AWS services.

**Note**  
To use location capabilities with Sidewalk devices, ensure you are using Amazon Sidewalk SDK version 1.19 or later on your end device. For details on implementing geolocation on the device side, see the [Amazon Sidewalk Location Library Developer Guide](https://docs.sidewalk.amazon/assets/pdf/Amazon_Sidewalk_Location_Library_Developer_Guide-1.0-rev-A.pdf).

## How positioning works for Sidewalk devices
<a name="sidewalk-location-solver"></a>

Sidewalk devices support three methods for resolving device location. The location resolution method used depends on your device's capabilities and configuration. Your end device determines which method to use based on its hardware capabilities and the Amazon Sidewalk SDK configuration.

Wi-Fi based location  
The device scans nearby Wi-Fi access points and sends their BSSID information and signal strengths. AWS uses this information to estimate the device's location based on known Wi-Fi access point locations.

GNSS (Global Navigation Satellite System) based location  
The device captures raw GNSS signals from GPS or other satellite navigation systems and sends this data to the cloud, where AWS solves for the device's position.

BLE (Bluetooth Low Energy) based location  
For Bluetooth Low Energy based location, AWS IoT returns location coordinates based on the approximate location of nearby Amazon Sidewalk Gateways that are connected to Amazon Sidewalk and have the Community Finding feature enabled.

**Important**  
Gateway Location Data is proprietary AWS Content and is subject to the following restrictions:  
It is provided solely to help you locate devices connected to Amazon Sidewalk.
You must only access location data through the interfaces and functionality that AWS makes generally available.
You must not attempt to re-identify, reverse engineer, or re-map any Gateway location data provided by AWS.

## Configuring your resource position
<a name="sidewalk-location-how"></a>

You can configure the position of your Sidewalk device using the AWS Management Console, the AWS IoT Wireless API, or the AWS CLI.

When you enable positioning for your Sidewalk device, you must also specify a destination for the location data. The destination describes the AWS IoT rule that processes the device's position information.

**Important**  
If you enable device location for the Sidewalk-enabled device, your raw uplink payload won't be propagated to the uplink destination. Location data will be sent to the location destination instead.

**Topics**
+ [How positioning works for Sidewalk devices](#sidewalk-location-solver)
+ [Configuring your resource position](#sidewalk-location-how)
+ [Configuring the position of Sidewalk devices](sidewalk-location-devices.md)