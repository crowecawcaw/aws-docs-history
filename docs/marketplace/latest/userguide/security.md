# AWS Marketplace security

Cloud security at AWS is the highest priority. As an AWS customer, you benefit from a
data center and network architecture that is built to meet the requirements of the most
security-sensitive organizations.

Security is a shared responsibility between AWS and you. The [shared responsibility
model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/") describes this as security _of_ the cloud and security
_in_ the cloud:

- **Security of the cloud** – AWS is responsible for
  protecting the infrastructure that runs AWS services in the AWS Cloud. AWS also
  provides you with services that you can use securely. The effectiveness of our security is
  regularly tested and verified by third-party auditors as part of the [AWS compliance programs](https://aws.amazon.com/compliance/programs/ "https://aws.amazon.com/compliance/programs/"). To learn
  about the compliance programs that apply to AWS Marketplace, see [AWS Services in Scope by Compliance
  Program](https://aws.amazon.com/compliance/services-in-scope/ "https://aws.amazon.com/compliance/services-in-scope/").
- **Security in the cloud** – Your responsibility is
  determined by the AWS service that you use. You're also responsible for other factors
  including the sensitivity of your data, your organization’s requirements, and applicable
  laws and regulations.
  This documentation helps you understand how to apply the shared responsibility model when
  using AWS Marketplace. The following topics show you how to configure AWS Identity and Access Management to manage access to
  AWS Marketplace in order to meet your security and compliance objectives. You can also learn how to
  use other AWS services that can help you to monitor and secure your AWS Marketplace
  resources.

To learn more about security and other policies regarding the products that you offer in AWS Marketplace, see
the following topics:

- [AMI-based product requirements for AWS Marketplace](product-and-ami-policies.md "product-and-ami-policies.md")
- [Container-based product requirements for AWS Marketplace](container-product-policies.md "container-product-policies.md")
- [Requirements and best practices for
  creating machine learning products](ml-listing-requirements-and-best-practices.md "ml-listing-requirements-and-best-practices.md")
- [SaaS product guidelines for AWS Marketplace](saas-guidelines.md "saas-guidelines.md")
- [Requirements for professional services products on AWS Marketplace](proserv-product-guidelines.md "proserv-product-guidelines.md")

###### Note

To learn about security on AWS Data Exchange for data products, see [Security](../../../data-exchange/latest/userguide/security.md "../../../data-exchange/latest/userguide/security.md") in the _AWS Data Exchange
User Guide_.

To learn about security for buyers in AWS Marketplace, see [Security on AWS Marketplace](../buyerguide/buyer-security.md "../buyerguide/buyer-security.md") in the
_AWS Marketplace Buyer Guide_.

###### Topics

- [Controlling access to
  AWS Marketplace Management Portal](marketplace-management-portal-user-access.md "marketplace-management-portal-user-access.md")
- [Policies and permissions for AWS Marketplace
  sellers](detailed-management-portal-permissions.md "detailed-management-portal-permissions.md")
- [AWS managed policies for AWS Marketplace sellers](security-iam-awsmanpol.md "security-iam-awsmanpol.md")
- [AWS Marketplace Commerce Analytics Service account permissions](set-aws-iam-cas-permissions.md "set-aws-iam-cas-permissions.md")
- [Amazon SQS permissions](set-aws-iam-sqs-permissions.md "set-aws-iam-sqs-permissions.md")
- [AWS Marketplace metering and entitlement
  API permissions](iam-user-policy-for-aws-marketplace-actions.md "iam-user-policy-for-aws-marketplace-actions.md")
- [Using service-linked roles for Resale Authorization
  with AWS Marketplace](using-roles-for-resale-authorization.md "using-roles-for-resale-authorization.md")
- [Logging AWS Marketplace API calls with
  AWS CloudTrail](cloudtrail-logging.md "cloudtrail-logging.md")
