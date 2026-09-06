

# AWS IoT Greengrass Version 1 in AWS GovCloud (US)
<a name="govcloud-iotgreengrass"></a>

AWS IoT Greengrass seamlessly extends AWS to edge devices so they can act locally on the data they generate, while still using the cloud for management, analytics, and durable storage. With AWS IoT Greengrass, connected devices can run AWS Lambda functions, execute predictions based on machine learning models, keep device data in sync, and communicate with other devices securely even when not connected to the Internet.

## Region availability
<a name="_region_availability"></a>

This service is available in the following AWS GovCloud (US) Regions:
+  AWS GovCloud (US-West) 
+  AWS GovCloud (US-East) 

## How AWS IoT Greengrass V1 differs
<a name="govcloud-iot-diffs"></a>

The following differences apply to AWS IoT Greengrass V1:
+  AWS IoT Greengrass Core software v1.9.2 is the minimum supported version.
+ The following minimum versions of the AWS IoT Greengrass Core SDK are supported.  
**​**    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-iotgreengrass.html)
+ The following connectors are supported in AWS GovCloud (US-East):
  + Cloudwatch Metrics, v4
  + Device Defender, v3
  + Docker Application Deployment, v6
  + Kinesis Firehose, v5
  + SNS, v4
  + Modbus-RTU Protocol Adapter, v3
  + Raspberry Pi GPIO, v4
  + Serial Stream, v3
+ The following connectors are supported in AWS GovCloud (US-West):
  + Modbus-RTU Protocol Adapter, v2
  + Raspberry Pi GPIO, v2
  + Serial Stream, v2
+ For over-the-air (OTA) updates, the IAM role used to presign the Amazon S3 URL (that links to the Greengrass software update) must allow access in the appropriate AWS Region.

  The following example policy includes the minimum required permissions that must be attached to the role for AWS GovCloud (US-West) Region support.
+  AWS IoT Greengrass operations use three endpoints that have different support for FIPS 140-3.
  + The endpoint for Greengrass control plane operations provides FIPS access only.
  + The endpoint for Greengrass discovery operations does not yet support FIPS. This endpoint provides non-FIPS access only.
  + The endpoint for AWS IoT device operations does not yet support FIPS. This endpoint provides non-FIPS access only.

  For more information, see [Service Endpoints](using-govcloud-endpoints.md). Only Amazon Trust Services (ATS) server authentication is supported, so you must use ATS-signed root CA certificates and ATS endpoints. For more information, see [Server Authentication](https://docs.aws.amazon.com/iot/latest/developerguide/managing-device-certs.html#server-authentication) in the *AWS IoT Developer Guide*.
+ The default limit for the maximum number of transactions per second (TPS) on the AWS IoT Greengrass API is 10 TPS. For more information, see [AWS IoT Greengrass Limits](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html#limits_greengrass) in the * Amazon Web Services General Reference *.

## Documentation
<a name="govcloud-iot-docs-2"></a>
+  [AWS IoT Greengrass documentation](https://docs.aws.amazon.com/documentation/greengrass) 

## Export-controlled content
<a name="govcloud-iotgreengrass-itar"></a>

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.
+ Message topics and topic filters
+ Customer-defined names and IDs of Greengrass resources:
  + Connectors
  + Cores
  + Devices
  + Functions
  + Groups
  + Loggers
  + Resources (local and machine learning)
  + Subscriptions