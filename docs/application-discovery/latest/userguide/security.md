AWS Application Discovery Service will discontinue onboarding new customers starting November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. Alternatively, use AWS Transform which provides similar capabilities. For more information, see [AWS Application Discovery Service availability change](application-discovery-service-availability-change.md "application-discovery-service-availability-change.md").

# Security in AWS Application Discovery Service

Cloud security at AWS is the highest priority. As an AWS customer, you benefit from a
data center and network architecture that are built to meet the requirements of the most
security-sensitive organizations.

Security is a shared responsibility between AWS and you. The [shared responsibility
model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/") describes this as security _of_ the cloud and security
_in_ the cloud:

- **Security of the cloud** – AWS is
  responsible for protecting the infrastructure that runs AWS services in the AWS
  Cloud. AWS also provides you with services that you can use securely. The
  effectiveness of our security is regularly tested and verified by third-party
  auditors as part of the [AWS
  compliance programs](https://aws.amazon.com/compliance/programs/ "https://aws.amazon.com/compliance/programs/").
- **Security in the cloud** – Your responsibility
  is determined by the AWS service that you use. You are also responsible for other
  factors including the sensitivity of your data, your organization’s requirements,
  and applicable laws and regulations.
  To use the AWS Application Discovery Agent or the Application Discovery Service Agentless Collector you must provide
  access keys to your AWS account. This information is then stored on your local infrastructure. As
  part of the shared responsibility model, you are responsible for securing access to
  your infrastructure.

This documentation will help you understand how to apply the shared responsibility model
when using Application Discovery Service. The following topics show you how to configure Application Discovery Service to
meet your security and compliance objectives. You'll also learn how to use other AWS
services that can help you to monitor and secure your Application Discovery Service resources.

###### Topics

- [Identity and Access Management for AWS Application Discovery Service](security-iam.md "security-iam.md")
- [Logging Application Discovery Service API calls with AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md")
