# Security

## Shared responsibility model

This [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/") reduces your operational burden because AWS operates, manages, and controls the components including the host operating system, the virtualization layer, and the physical security of the facilities in which the services operate. For more information about AWS security, visit [AWS Cloud Security](http://aws.amazon.com/security/ "http://aws.amazon.com/security/").

## Security features

Security is built into every layer of the Connected Mobility guidance:

**Device Authentication** - X.509 certificates provide mutual authentication between vehicles and AWS IoT Core, ensuring only authorized devices can connect.

**Data in Transit** - All communication uses TLS encryption, including MQTT over TLS for vehicle communication and SASL_SSL for Kafka communication.

**Access Control** - IAM roles and policies provide fine-grained access control for all AWS services, following the principle of least privilege.

**Credential Management** - SCRAM credentials for MSK are securely stored in AWS Secrets Manager with automatic rotation capabilities.

**Network Security** - MSK clusters deploy in private subnets with security groups restricting access to authorized components only.

**Data at Rest** - DynamoDB tables and S3 buckets use AWS KMS encryption for data at rest protection.
