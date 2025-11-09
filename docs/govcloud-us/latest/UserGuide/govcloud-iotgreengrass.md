# AWS IoT Greengrass Version 1 in ?AWS GovCloud (US)

AWS IoT Greengrass seamlessly extends AWS to edge devices so they can act locally on the data they generate, while still using the cloud for management, analytics, and durable storage. With AWS IoT Greengrass, connected devices can run AWS Lambda functions, execute predictions based on machine learning models, keep device data in sync, and communicate with other devices securely even when not connected to the Internet.

## How AWS IoT Greengrass V1 differs for AWS GovCloud (US)

- AWS IoT Greengrass Core software v1.9.2 is the minimum supported version.
- The following minimum versions of the AWS IoT Greengrass Core SDK are supported.

| ​            | Language or platform | Minimum version |
| ------------ | -------------------- | --------------- |
| Python 3.7   | 1.4.0                |
| Java 8       | 1.3.1                |
| Node.js 8.10 | 1.4.0                |
| C, C++       | 1.1.0                |

- The following connectors are supported in AWS GovCloud (US-East):
  - Cloudwatch Metrics, v4
  - Device Defender, v3
  - Docker Application Deployment, v6
  - Kinesis Firehose, v5
  - SNS, v4
  - Modbus-RTU Protocol Adapter, v3
  - Raspberry Pi GPIO, v4
  - Serial Stream, v3

- The following connectors are supported in AWS GovCloud (US-West):
  - Modbus-RTU Protocol Adapter, v2
  - Raspberry Pi GPIO, v2
  - Serial Stream, v2

- For over-the-air (OTA) updates, the IAM role used to presign the Amazon S3 URL (that links to the Greengrass software update) must allow access in the appropriate AWS Region.

The following example policy includes the minimum required permissions that must be attached to the role for AWS GovCloud (US-West) Region support.

- AWS IoT Greengrass operations use three endpoints that have different support for FIPS 140-3.

      + The endpoint for Greengrass control plane operations provides FIPS access only.
      + The endpoint for Greengrass discovery operations does not yet support FIPS. This endpoint provides non-FIPS access only.
      + The endpoint for AWS IoT device operations does not yet support FIPS. This endpoint provides non-FIPS access only.

  For more information, see [Service Endpoints](using-govcloud-endpoints.md "using-govcloud-endpoints.md"). Only Amazon Trust Services (ATS) server authentication is supported, so you must use ATS-signed root CA certificates and ATS endpoints. For more information, see [Server Authentication](../../../iot/latest/developerguide/managing-device-certs.md#server-authentication "../../../iot/latest/developerguide/managing-device-certs.md#server-authentication") in the _AWS IoT Developer Guide_.

- The default limit for the maximum number of transactions per second (TPS) on the AWS IoT Greengrass API is 10 TPS. For more information, see [AWS IoT Greengrass Limits](../../../general/latest/gr/aws_service_limits.md#limits_greengrass "../../../general/latest/gr/aws_service_limits.md#limits_greengrass") in the _Amazon Web Services General Reference_ .

## Documentation for AWS IoT Greengrass

[AWS IoT Greengrass documentation](https://aws.amazon.com/documentation/greengrass "https://aws.amazon.com/documentation/greengrass").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.

- Message topics and topic filters
- Customer-defined names and IDs of Greengrass resources:
  - Connectors
  - Cores
  - Devices
  - Functions
  - Groups
  - Loggers
  - Resources (local and machine learning)
  - Subscriptions
