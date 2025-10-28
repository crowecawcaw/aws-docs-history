# AWS IoT Greengrass Version 2 in AWS GovCloud (US)

AWS IoT Greengrass seamlessly extends AWS to edge devices so they can act locally on the data they generate, while still using the cloud for management, analytics, and durable storage. With AWS IoT Greengrass, connected devices can run AWS Lambda functions, execute predictions based on machine learning models, keep device data in sync, and communicate with other devices securely even when not connected to the Internet.

## How AWS IoT Greengrass V2 differs for AWS GovCloud (US)

- Secret manager v2.0.5 is the minimum supported version in the
  AWS GovCloud (US) Regions.

## Documentation for AWS IoT Greengrass V2

[AWS IoT Greengrass documentation](../../../greengrass/v2/developerguide/what-is-iot-greengrass.md "../../../greengrass/v2/developerguide/what-is-iot-greengrass.md").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains
how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings.
The list can be used as a guide to help meet applicable customer compliance obligations.
Data not included in the following list remains within the AWS GovCloud (US) Regions.

- Message topics and topic filters
- Customer-defined names and IDs of Greengrass resources:
  - CoreDevices
  - Components
  - Deployments
