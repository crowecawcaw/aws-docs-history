

# AWS IoT Device Management in AWS GovCloud (US)
<a name="govcloud-iotdevman"></a>

AWS IoT Device Management is a cloud-based device management service that makes it easy for customers to securely manage IoT devices throughout their lifecycle. Customers can use AWS IoT Device Management to onboard device information and configuration, organize their device inventory, monitor their fleet of devices, and remotely manage devices deployed across many locations. This remote management includes over-the-air (OTA) updates to device software.

## Region availability
<a name="_region_availability"></a>

This service is available in the following AWS GovCloud (US) Regions:
+  AWS GovCloud (US-West) 
+  AWS GovCloud (US-East) 

## How AWS IoT Device Management differs
<a name="govcloud-iotdevman-diffs"></a>

The following differences apply to AWS IoT Device Management:
+ Use of Amazon Cognito Identities to grant permissions to users of your AWS IoT applications, via your own identity provider or other popular identity providers, is not available. For more information, see [Common Amazon Cognito scenarios](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-scenarios.html#scenario-identity-pool).
+  AWS IoT Device Management Fleet Hub is not available. For more information, see [What is Fleet Hub for AWS IoT Device Management?](https://docs.aws.amazon.com/iot/latest/fleethubuserguide/what-is-aws-iot-monitor.html) 
+  FreeRTOS over-the-air (OTA) updates using MQTT-based file delivery via a stream is not available. For more information, see [OTA Update Manager service](https://docs.aws.amazon.com/freertos/latest/userguide/ota-manager.html) and [MQTT-based file delivery](https://docs.aws.amazon.com/iot/latest/developerguide/mqtt-based-file-delivery.html).

## Documentation
<a name="govcloud-iotdevman-docs"></a>
+  [AWS IoT Device Management documentation](https://docs.aws.amazon.com/documentation/iot-device-management) 

## Export-controlled content
<a name="govcloud-iotdevman-itar-6"></a>

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.
+ Message topics and topic filters
+ Thing names
+ Thing types
+ Thing group names
+ Rule definitions (including SQL statements and actions)