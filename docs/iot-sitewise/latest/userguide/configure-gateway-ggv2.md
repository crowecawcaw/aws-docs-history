# AWS IoT SiteWise Edge self-hosted gateway

requirements

AWS IoT SiteWise Edge gateways run on AWS IoT Greengrass V2 as a set of AWS IoT Greengrass components
that support data collection, processing, and publishing on premises. To configure a
SiteWise Edge gateway that runs on AWS IoT Greengrass V2, create a gateway in the AWS Cloud and run the
SiteWise Edge gateway software to set up your local device. When you use the AWS Management Console to
create the SiteWise Edge gateway, an installation script is provided. Run this script on your
target gateway device to set up necessary software and dependencies.

## Local device

requirements

Local devices must meet the following requirements to install and run the SiteWise Edge
gateway software.

- Supports AWS IoT Greengrass V2 Core software version [v2.3.0](../../../greengrass/v2/developerguide/greengrass-release-2021-06-29.md "../../../greengrass/v2/developerguide/greengrass-release-2021-06-29.md") or
  newer. For more information, see [Requirements](../../../greengrass/v2/developerguide/setting-up.md#greengrass-v2-requirements "../../../greengrass/v2/developerguide/setting-up.md#greengrass-v2-requirements") in the
  _AWS IoT Greengrass Version 2 Developer Guide_.
- One of the following supported platforms:
  - OS: Ubuntu 20.04 or later

  Architecture: x86_64 (AMD64) or ARMv8 (Aarch64)
  - OS: Red Hat Enterprise Linux (RHEL) 8

  Architecture: x86_64 (AMD64) or ARMv8 (Aarch64)
  - OS: Amazon Linux 2

  Architecture: x86_64 (AMD64) or ARMv8 (Aarch64)
  - OS: Debian 11

  Architecture: x86_64 (AMD64) or ARMv8 (Aarch64)
  - OS: Windows Server 2019 and later

  Architecture: x86_64 (AMD64)

###### Note

ARM platforms support SiteWise Edge gateways with Data Collection Pack only.
The data processing pack is not supported.

- Minimum 4 GB RAM.
- Minimum 10 GB disk space available for the SiteWise Edge gateway
  software.
- Configure your local device to make sure that the proper ports are
  accessible. For a full list of the required outbound service endpoints, see
  [Required service endpoints for AWS IoT SiteWise Edge gateways](../../../prescriptive-guidance/latest/endpoints-for-iot-sitewise-edge-gateways/required-endpoints.md "../../../prescriptive-guidance/latest/endpoints-for-iot-sitewise-edge-gateways/required-endpoints.md").
- Java Runtime Environment (JRE) version 11 or higher. Java must be
  available on the `PATH` environment variable on the device. To
  use Java to develop custom components, you must install a Java Development
  Kit (JDK). We recommend that you use [Amazon Corretto](../../../corretto.md "../../../corretto.md") or [OpenJDK](https://openjdk.org/projects/jdk/ "https://openjdk.org/projects/jdk/").

### Amazon S3 buckets to allowlist for local devices

Configure your local device to provide firewall access the following Amazon S3
bucket. Configure access based on the respective regions for your devices.

| Region                   | Endpoint                                                                                                                                                       |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Asia Pacific (Tokyo)     | https://iot-sitewise-gateway-ap-northeast-1-785558802005.s3.ap-northeast-1.amazonaws.com                                                                       |
| Asia Pacific (Seoul)     | https://iot-sitewise-gateway-ap-northeast-2-310055672453.s3.ap-northeast-2.amazonaws.com                                                                       |
| Asia Pacific (Mumbai)    | https://iot-sitewise-gateway-ap-south-1-677656657204.s3.ap-south-1.amazonaws.com                                                                               |
| Asia Pacific (Singapore) | https://iot-sitewise-gateway-ap-southeast-1-475191558554.s3.ap-southeast-1.amazonaws.com                                                                       |
| Asia Pacific (Sydney)    | https://iot-sitewise-gateway-ap-southeast-2-396319432685.s3.ap-southeast-2.amazonaws.com                                                                       |
| Canada (Central)         | https://iot-sitewise-gateway-ca-central-1-842060018567.s3.ca-central-1.amazonaws.com                                                                           |
| China (Beijing)          | https://iot-sitewise-gateway-cn-north-1-237124890262.s3.cn-north-1.amazonaws.com.cn                                                                            |
| Europe (Frankfurt)       | https://iot-sitewise-gateway-eu-central-1-748875242063.s3.eu-central-1.amazonaws.com                                                                           |
| Europe (Ireland)         | https://iot-sitewise-gateway-eu-west-1-383414315062.s3.eu-west-1.amazonaws.com                                                                                 |
| US East (N. Virginia)    | https://iot-sitewise-gateway-us-east-1-223558168232.s3.us-east-1.amazonaws.com<br>and<br>https://iot-sitewise-gateway-us-east-1-223558168232.s3.amazonaws.com/ |
| US East (Ohio)           | https://iot-sitewise-gateway-us-east-2-005072661813.s3.us-east-2.amazonaws.com                                                                                 |
| AWS GovCloud (US-West)   | https://iot-sitewise-gateway-us-gov-west-1-599984565679.s3.us-gov-west-1.amazonaws.com/                                                                        |
| US West (Oregon)         | https://iot-sitewise-gateway-us-west-2-502577205460.s3.us-west-2.amazonaws.com                                                                                 |

## Data processing pack requirements

###### Note

The data processing pack (DPP) feature will no longer be open to new customers starting November 7, 2025 . If you would like to use DPP,
sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see
[Data processing pack availability change](../appguide/iotsitewise-dpp-availability-change.md "../appguide/iotsitewise-dpp-availability-change.md").

- If you plan to use the data processing pack at the edge with AWS IoT SiteWise, your
  local device must also meet the following requirements:
  - Has an x86 64 bit quad-core processor.
  - Has at least 16 GB of RAM.
  - Has at least 32 GB for RAM if using Microsoft
    Windows.
  - Had at least 256 GB of free disk space.
  - The local device must allow network inbound traffic on port
  443.
  - The following ports are reserved for use by AWS IoT SiteWise: 80, 443, 3001,
    4569, 4572, 8000, 8081, 8082, 8084, 8085, 8445, 8086, 9000, 9500,
    11080, and 50010. Using a reserved port for traffic can result in a
    terminated connection.

  ###### Note

  The AWS IoT Greengrass V2 Stream manager component has its own requirements.
  For more information, see [Configuration](../../../greengrass/v2/developerguide/stream-manager-component.md#stream-manager-component-configuration "../../../greengrass/v2/developerguide/stream-manager-component.md#stream-manager-component-configuration") in the
  _AWS IoT Greengrass Version 2 Developer Guide_.

- The minimum disk space and compute capacity requirements depend on a
  variety of factors that are unique to your implementation and use
  case.
  - The disk space required for caching data for intermittent internet
    connectivity depends on the following factors:
    - Number of data streams uploaded
    - Data points per data stream per second
    - Size of each data point
    - Communication speeds
    - Expected network downtime

  - The compute capacity required to poll and upload data depends on
    the following factors:
    - Number of data streams uploaded
    - Data points per data stream per second

## Configure permissions to use SiteWise Edge

gateways

You must have the following permissions to use SiteWise Edge gateways:

###### Note

If you use the AWS IoT SiteWise console to create your SiteWise Edge gateway, these permissions
are added for you.

- The IAM role for your SiteWise Edge gateway must allow you to use an SiteWise Edge
  gateway on an AWS IoT Greengrass V2 device to process asset model data and asset
  data.

The role allows the following service to assume the role:
`credentials.iot.amazonaws.com`.

**Permissions details**

The role must have the following permissions:

    + `iotsitewise` – Allows principals to retrieve
     asset model data and asset data at the edge.
    + `iot` – Allows your AWS IoT Greengrass V2 devices to interact
     with AWS IoT.
    + `logs` – Allows your AWS IoT Greengrass V2 devices to send logs
     to Amazon CloudWatch Logs.
    + `s3` – Allows your AWS IoT Greengrass V2 devices to download
     custom component artifacts from Amazon S3.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "iotsitewise:BatchPutAssetPropertyValue",
 "iotsitewise:List*",
 "iotsitewise:Describe*",
 "iotsitewise:Get*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "iot:DescribeCertificate",
 "logs:CreateLogGroup",
 "logs:CreateLogStream",
 "logs:PutLogEvents",
 "logs:DescribeLogStreams",
 "s3:GetBucketLocation",
 "s3:GetObject",
 "iot:Connect",
 "iot:Publish",
 "iot:Subscribe",
 "iot:Receive",
 "iot:DescribeEndpoint"
 ],
 "Resource": "*"
 }
 ]
}`

```
