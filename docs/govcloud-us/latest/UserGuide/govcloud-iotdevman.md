# AWS IoT Device Management in AWS GovCloud (US)

AWS IoT Device Management is a cloud-based device management service that makes it easy for customers to securely manage IoT devices throughout their lifecycle. Customers can use AWS IoT Device Management to onboard device information and configuration, organize their device inventory, monitor their fleet of devices, and remotely manage devices deployed across many locations. This remote management includes over-the-air (OTA) updates to device software.

## How AWS IoT Device Management differs for AWS GovCloud (US)

- Use of Amazon Cognito Identities to grant permissions to users of your AWS IoT applications, via your own
  identity provider or other popular identity providers, is not supported. For
  more information, see [Common Amazon Cognito scenarios](../../../cognito/latest/developerguide/cognito-scenarios.md#scenario-identity-pool "../../../cognito/latest/developerguide/cognito-scenarios.md#scenario-identity-pool").
- AWS IoT Device Management Fleet Hub is not available. For more information, see [What is
  Fleet Hub for AWS IoT Device Management?](../../../iot/latest/fleethubuserguide/what-is-aws-iot-monitor.md "../../../iot/latest/fleethubuserguide/what-is-aws-iot-monitor.md")
- FreeRTOS over-the-air (OTA) updates using MQTT-based file delivery via a
  stream is not supported. For more information, see [OTA Update Manager
  service](../../../freertos/latest/userguide/ota-manager.md "../../../freertos/latest/userguide/ota-manager.md") and [MQTT-based
  file delivery](../../../iot/latest/developerguide/mqtt-based-file-delivery.md "../../../iot/latest/developerguide/mqtt-based-file-delivery.md").

## Documentation for AWS IoT Device Management

[AWS IoT Device Management documentation](https://aws.amazon.com/documentation/iot-device-management "https://aws.amazon.com/documentation/iot-device-management").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains
how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings.
The list can be used as a guide to help meet applicable customer compliance obligations.
Data not included in the following list remains within the AWS GovCloud (US) Regions.

- Message topics and topic filters
- Thing names
- Thing types
- Thing group names
- Rule definitions (including SQL statements and actions)
