# AMS VPC endpoints

A VPC endpoint lets you privately connect your VPC to AWS services without requiring an Internet gateway.
Instances in your VPC do not require
public IP addresses to communicate with resources in the service.

Endpoints are virtual devices. They are horizontally scaled, redundant, and highly available VPC components that
allow communication between instances in your VPC and services without imposing availability risks or bandwidth constraints on your network traffic.
To learn more, see
[VPC Endpoints](../../../vpc/latest/userguide/vpc-endpoints.md "../../../vpc/latest/userguide/vpc-endpoints.md").

There are two types of VPC endpoints: interface endpoints and gateway endpoints.

- Gateway endpoints: The VPC in the account has an Amazon S3 Gateway endpoint enabled by default.
- Interface endpoints: Instances in your AMS environment can talk to supported services
  without leaving the Amazon network. This is optional for **single-account landing zone** and it is not
  enabled in the account by default; submit a service request to AMS operations to get this enabled.
  However, for **multi-account landing zone**, interface endpoints are enabled by default in the Shared Services account.

List of interface endpoints supported by AMS:

    + AWS CloudFormation
    + AWS CloudTrail
    + AWS Config
    + Amazon EC2 API
    + AWS Key Management Service
    + Amazon CloudWatch
    + Amazon CloudWatch Events
    + Amazon CloudWatch Logs
    + AWS Secrets Manager
    + Amazon SNS
    + AWS Systems Manager
    + AWS Security Token Service
