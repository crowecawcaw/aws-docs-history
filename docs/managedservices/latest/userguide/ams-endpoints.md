

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# AMS VPC endpoints
<a name="ams-endpoints"></a>

A VPC endpoint lets you privately connect your VPC to AWS services without requiring an Internet gateway. Instances in your VPC do not require public IP addresses to communicate with resources in the service.

Endpoints are virtual devices. They are horizontally scaled, redundant, and highly available VPC components that allow communication between instances in your VPC and services without imposing availability risks or bandwidth constraints on your network traffic. To learn more, see [VPC Endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints.html).

There are two types of VPC endpoints: interface endpoints and gateway endpoints.
+ Gateway endpoints: The VPC in the account has an Amazon S3 Gateway endpoint enabled by default.
+ Interface endpoints: Instances in your AMS environment can talk to supported services without leaving the Amazon network. This is optional for **single-account landing zone** and it is not enabled in the account by default; submit a service request to AMS operations to get this enabled. However, for **multi-account landing zone**, interface endpoints are enabled by default in the Shared Services account.

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