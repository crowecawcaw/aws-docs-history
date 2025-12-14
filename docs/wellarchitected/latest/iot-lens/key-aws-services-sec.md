# Key AWS services

The essential AWS security services in IoT are the
[AWS IoT Core](https://aws.amazon.com/iot-core/ "https://aws.amazon.com/iot-core/"),

[AWS IoT Device Management](https://aws.amazon.com/iot-device-management/ "https://aws.amazon.com/iot-device-management/"),

[AWS IoT Device Defender](https://aws.amazon.com/iot-device-defender/ "https://aws.amazon.com/iot-device-defender/"),

[AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/ "https://aws.amazon.com/iam/"), and

[Amazon Cognito](https://aws.amazon.com/pm/cognito/ "https://aws.amazon.com/pm/cognito/"). In combination, these services along with other
AWS security services allow you to securely control access to IoT
devices, AWS services, IoT applications and resources for your
users. Additional AWS services such as
[AWS IoT Greengrass](https://aws.amazon.com/greengrass/ "https://aws.amazon.com/greengrass/"),

[Amazon S3](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/"),

[Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/"), and

[Amazon Relational Database Service](https://aws.amazon.com/rds/ "https://aws.amazon.com/rds/") are often used in IoT applications.
The following services and features support IoT security:

**Design**: The AWS Device
Qualification Program provides IoT endpoint and edge hardware that
has been pre-tested for interoperability with AWS IoT. Tests
include mutual authentication and OTA support for remote patching.

**Asset inventory:**
[AWS IoT Device Management](https://aws.amazon.com/iot-device-management/ "https://aws.amazon.com/iot-device-management/") can be used as an inventory for IoT
devices and AWS Systems Manager Inventory can be used to provide
visibility into on premises computing resources and edge gateways.

**AWS Identity and Access Management
(IAM):** Device credentials (X.509 certificates, IAM,
Amazon Cognito identity pools and Amazon Cognito user pools, or
custom authorization tokens) enable you to securely control device
and external user access to AWS resources. AWS IoT policies add
the ability to implement fine grained access to IoT devices.
[AWS Private Certificate Authority](https://aws.amazon.com/private-ca/ "https://aws.amazon.com/private-ca/") provides a cloud-based approach to
creating and managing device certificates. Use AWS IoT thing
groups to manage IoT permissions at the group level instead of
individually. Use the AWS IoT credentials endpoint to obtain
temporary IAM credentials in an IoT device in order to use AWS
services from the IoT device.

**Detective controls**:
[AWS IoT Device Defender](https://aws.amazon.com/iot-device-defender/ "https://aws.amazon.com/iot-device-defender/") records device communication and cloud
side metrics from

[AWS IoT Core](https://aws.amazon.com/iot-core/ "https://aws.amazon.com/iot-core/").

[AWS IoT Device Defender](https://aws.amazon.com/iot-device-defender/ "https://aws.amazon.com/iot-device-defender/") can automate security responses by
sending notifications through

[Amazon Simple Notification Service (SNS)](https://aws.amazon.com/pm/sns/ "https://aws.amazon.com/pm/sns/") to internal systems or
administrators.

[AWS CloudTrail](https://aws.amazon.com/cloudtrail/ "https://aws.amazon.com/cloudtrail/") logs provide administrative actions of your IoT
application.

[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/") is a monitoring service with integration with

[AWS IoT Core](https://aws.amazon.com/iot-core/ "https://aws.amazon.com/iot-core/") and can trigger CloudWatch Events to automate security
responses. CloudWatch captures detailed logs related to
connectivity and security events between IoT edge components and
cloud services.

**Infrastructure protection**:
[AWS IoT Core](https://aws.amazon.com/iot-core/ "https://aws.amazon.com/iot-core/") is a cloud service that lets connected devices easily
and securely interact with cloud applications and other devices.
The AWS IoT rules engine in
[AWS IoT Core](https://aws.amazon.com/iot-core/ "https://aws.amazon.com/iot-core/") uses IAM permissions to communicate with other
downstream AWS services. AWS has created a wide selection of
industry leading IoT silicon vendors, device manufacturers, and
gateway partners who have integrated
[AWS IoT Greengrass](https://aws.amazon.com/greengrass/ "https://aws.amazon.com/greengrass/") into their software and hardware offerings.
Customers have the option to store their device private key on a
hardware secure element and store sensitive device information at
the edge with
[AWS IoT Greengrass](https://aws.amazon.com/greengrass/ "https://aws.amazon.com/greengrass/") Secrets Manager and encrypt secrets using
private keys for root of trust security.

**Data protection**:
[AWS IoT Core](https://aws.amazon.com/iot-core/ "https://aws.amazon.com/iot-core/") includes encryption capabilities for devices over TLS
to protect your data in transit.

[AWS IoT Core](https://aws.amazon.com/iot-core/ "https://aws.amazon.com/iot-core/") integrates directly with services, such as

[Amazon S3](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/") and

[Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/"), which support encryption at rest. In addition,

[AWS Key Management Service (KMS)](https://aws.amazon.com/kms/ "https://aws.amazon.com/kms/") supports the ability for you to create and
control keys used for encryption. On devices, you can use AWS edge
offerings such as

[FreeRTOS](https://aws.amazon.com/freertos/ "https://aws.amazon.com/freertos/"),

[AWS IoT Greengrass](https://aws.amazon.com/greengrass/ "https://aws.amazon.com/greengrass/"), or the AWS IoT Embedded C SDK to support secure
communication.

**Patch management:** Implement
patch management to fix device vulnerabilities and define
appropriate update mechanisms for software and firmware updates
using
[AWS IoT Device Management](https://aws.amazon.com/iot-device-management/ "https://aws.amazon.com/iot-device-management/") Jobs service and

[AWS Systems Manager](https://aws.amazon.com/systems-manager/ "https://aws.amazon.com/systems-manager/") Patch Manager. Perform deployment of
patches only after testing the patches in a test environment
before implementing them in production and verify the integrity of
the software before starting to run it making sure that it comes
from a reliable source (signed by the vendor) and that it is
obtained in a secure manner.

**Incident response**:
[AWS IoT Device Defender](https://aws.amazon.com/iot-device-defender/ "https://aws.amazon.com/iot-device-defender/") allows you to create security profiles
that can be used to detect deviations from normal device behavior
and trigger automated responses including Serverless Computing -[AWS Lambda](https://aws.amazon.com/pm/lambda/ "https://aws.amazon.com/pm/lambda/").

[AWS IoT Device Management](https://aws.amazon.com/iot-device-management/ "https://aws.amazon.com/iot-device-management/") should be used to group devices that
need remediation and then using AWS IoT Jobs to deploy fixes to
devices.
[AWS Security Hub CSPM](https://aws.amazon.com/security-hub/ "https://aws.amazon.com/security-hub/") can be used to aggregate security alerts from
various AWS services and partner products to help you analyze your
security trends and identify the highest priority security issues.
[AWS Security Hub CSPM](https://aws.amazon.com/security-hub/ "https://aws.amazon.com/security-hub/") provides you with a comprehensive view of your
security state within AWS and your compliance with security
standards and best practices and enables automated remediation.
[AWS Security Hub CSPM](https://aws.amazon.com/security-hub/ "https://aws.amazon.com/security-hub/") has out-of-the-box integrations with
ticketing, chat, Security Information and Event Management (SIEM),
Security Orchestration Automation and Response (SOAR), threat
investigation, Governance Risk and Compliance (GRC), and incident
management tools to provide users with a complete security
operations workflow.

**Business continuity and
recovery**: To backup IoT data at the edge and in the
cloud, customers can use
[AWS IoT Greengrass](https://aws.amazon.com/greengrass/ "https://aws.amazon.com/greengrass/") stream manager to locally buffer data and send
data to local storage destinations and other life cycle management
features available in
[AWS IoT Greengrass](https://aws.amazon.com/greengrass/ "https://aws.amazon.com/greengrass/") to support your data resiliency and backup
needs.

[AWS Backup](https://aws.amazon.com/backup/ "https://aws.amazon.com/backup/") can be used to centrally manage and automate backups
across AWS services and on premise IoT systems.
