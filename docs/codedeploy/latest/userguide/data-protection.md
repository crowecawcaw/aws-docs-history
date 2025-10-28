# Data protection in AWS CodeDeploy

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/")
applies to data protection in AWS CodeDeploy. As described in this model, AWS is
responsible for protecting the global infrastructure that runs all of the AWS Cloud. You are
responsible for maintaining control over your content that is hosted on this infrastructure.
You are also responsible for the security configuration and management tasks for the AWS services
that you use. For more information about data privacy, see the [Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq/ "https://aws.amazon.com/compliance/data-privacy-faq/"). For information about data protection in Europe, see the [AWS Shared
Responsibility Model and GDPR](https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/ "https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/") blog post on the _AWS Security
Blog_.

For data protection purposes, we recommend that you protect AWS account
credentials and set up individual users with AWS IAM Identity Center or AWS Identity and Access Management (IAM). That way, each user is given only the permissions necessary to fulfill their job duties. We also recommend that you secure your data in the following ways:

- Use multi-factor authentication (MFA) with each account.
- Use SSL/TLS to communicate with AWS resources. We require TLS 1.2 and recommend TLS 1.3.
- Set up API and user activity logging with AWS CloudTrail. For information about using CloudTrail trails to capture AWS activities, see [Working with CloudTrail trails](../../../awscloudtrail/latest/userguide/cloudtrail-trails.md "../../../awscloudtrail/latest/userguide/cloudtrail-trails.md") in the _AWS CloudTrail User Guide_.
- Use AWS encryption solutions, along with all default security controls within AWS services.
- Use advanced managed security services such as Amazon Macie, which assists in discovering
  and securing sensitive data that is stored in Amazon S3.
- If you require FIPS 140-3 validated cryptographic modules when accessing AWS through
  a command line interface or an API, use a FIPS endpoint. For more information about the
  available FIPS endpoints, see [Federal
  Information Processing Standard (FIPS) 140-3](https://aws.amazon.com/compliance/fips/ "https://aws.amazon.com/compliance/fips/").
  We strongly recommend that you never put confidential or sensitive information, such as your
  customers' email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with CodeDeploy or other AWS services
  using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into
  tags or free-form text fields used for names may be used for billing or diagnostic logs. If you
  provide a URL to an external server, we strongly recommend that you do not include credentials
  information in the URL to validate your request to that server.

## Internetwork traffic privacy

CodeDeploy is a fully managed deployment service that supports EC2 instances, Lambda
functions, Amazon ECS, and on-premises servers. For EC2 instances and on-premises servers,
a host-based agent communicates with CodeDeploy using TLS.

Currently, communication from the agent to the service requires an outbound internet
connection so the agent can communicate with the public CodeDeploy and Amazon S3 service endpoints. In a
virtual private cloud, this can be accomplished with an internet gateway, site to site VPN
connection to your corporate network, or direct connect.

The CodeDeploy agent supports HTTP proxies.

Amazon VPC endpoints, powered by AWS PrivateLink, are available for CodeDeploy in certain regions. For
details, see [Use CodeDeploy with Amazon Virtual Private Cloud](vpc-endpoints.md "vpc-endpoints.md").

###### Note

The CodeDeploy agent is required only if you deploy to an Amazon EC2/On-premises compute platform.
The agent is not required for deployments that use the Amazon ECS or AWS Lambda compute
platform.

## Encryption at rest

Customer code is not stored in CodeDeploy. As a deployment service, CodeDeploy is dispatching
commands to the CodeDeploy agent running on EC2 instances or on-premises servers. The CodeDeploy agent
then executes the commands using TLS. Service model data for deployments, deployment
configuration, deployment groups, applications, and application revisions are stored in
Amazon DynamoDB and encrypted at rest using an AWS owned key, owned and managed by CodeDeploy. For more
information, see [AWS owned keys](../../../kms/latest/developerguide/concepts.md#aws-owned-cmk "../../../kms/latest/developerguide/concepts.md#aws-owned-cmk").

## Encryption in transit

The CodeDeploy agent initiates all communication with CodeDeploy over port 443. The agent polls
CodeDeploy and listens for a command. The CodeDeploy agent is open source. All service-to-service and
client-to-service communication is encrypted in transit using TLS. This protects customer data
in transit between CodeDeploy and other services like Amazon S3.

## Encryption key management

There are no encryption keys for you to manage. The CodeDeploy service model data is encrypted
using an AWS owned key, owned and managed by CodeDeploy. For more information, see [AWS owned keys](../../../kms/latest/developerguide/concepts.md#aws-owned-cmk "../../../kms/latest/developerguide/concepts.md#aws-owned-cmk").
