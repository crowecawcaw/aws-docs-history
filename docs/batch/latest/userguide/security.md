

# Security in AWS Batch
<a name="security"></a>

Cloud security at AWS is the highest priority. As an AWS customer, you benefit from data centers and network architectures that are built to meet the requirements of the most security sensitive organizations.

Security is a shared responsibility between AWS and you. The [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) describes this as security *of* the cloud and security *in* the cloud:
+ **Security of the cloud** – AWS is responsible for protecting the infrastructure that runs AWS services in the AWS Cloud. AWS also provides you with services that you can use securely. Third-party auditors regularly test and verify the effectiveness of our security as part of the [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/). To learn about the compliance programs that apply to AWS Batch, see [AWS Services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/).
+ **Security in the cloud** – Your responsibility is determined by the AWS service that you use. You are also responsible for other factors including the sensitivity of your data, your company's requirements, and applicable laws and regulations. 

This documentation helps you understand how to apply the shared responsibility model when using AWS Batch. The following topics show you how to configure AWS Batch to meet your security and compliance objectives. You also learn how to use other AWS services that help you to monitor and secure your AWS Batch resources. 

**Topics**
+ [Identity and Access Management for AWS Batch](security-iam.md)
+ [AWS Batch IAM policies, roles, and permissions](IAM_policies.md)
+ [AWS Batch IAM execution role](execution-IAM-role.md)
+ [Create a virtual private cloud](create-public-private-vpc.md)
+ [Use an interface endpoint to Access AWS Batch](vpc-interface-endpoints.md)
+ [Compliance validation for AWS Batch](compliance.md)
+ [Infrastructure security in AWS Batch](infrastructure-security.md)
+ [Cross-service confused deputy prevention](cross-service-confused-deputy-prevention.md)
+ [Logging AWS Batch API calls with AWS CloudTrail](logging-using-cloudtrail.md)
+ [Troubleshoot AWS Batch IAM](security_iam_troubleshoot.md)