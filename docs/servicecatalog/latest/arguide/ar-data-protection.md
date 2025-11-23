# Data protection in AppRegistry

In the [AWS shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/"),
you're responsible
for **_security in the cloud_**
while AWS is responsible
for **_security of the cloud_**.
AWS protects the cloud infrastructure,
and you protect the content
that's hosted
in the cloud infrastructure.
For information
about data privacy
and information
about data protection
in Europe,
see the following:

- [Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq/ "https://aws.amazon.com/compliance/data-privacy-faq/")
- [AWS Shared Responsibility Model and GDPR](https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/ "https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/")

You can use AWS Identity and Access Management (IAM)
to set up user accounts and protect AWS account credentials.
This grants users the required permissions
to perfom work-related duties.
As a best practice,
we recommend
that users create roles
to access resources
in AWS.
For information
about creating a role,
see [Creating a role to delegate permissions to an AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the _IAM User Guide_.
Other ways
to secure data
inlclude the following:

- Using multi-factor authentication (MFA)
  with each account.
- Using SSL/TLS
  to communicate
  with AWS resources.
  (TLS 1.2 or later recommended)
- Setting up API and user activity logging
  with AWS CloudTrail.
- Using AWS encryption solutions,
  including all default security controls
  within AWS services.
- Using an FIPS endpoint
  when accessing AWS
  through the command line interface or an API
  and
  if you need FIPS 140-2 validated cryptographic modules.
  For information
  about the available FIPS endpoints,
  see [Federal Information Processing Standard (FIPS) 140-2](https://aws.amazon.com/compliance/fips/ "https://aws.amazon.com/compliance/fips/").

###### Note

Data
that you enter
into AppRegistry and other AWS services can get picked up
for inclusion
in diagnostic logs.

We recommend
that you don't put sensitive or identifying information,
such as customer account numbers,
into free-form fields
like `Name`.
The same is true
when using AppRegistry and other AWS services
from the AWS Management Console,
through the AWS CLI,
by using an API, or
by using one
of the AWS SDKs.

As a best practice,
when you provide a URL
to an external server,
don't include information
about credentials
in the URL
to validate
your request.

## Protecting Data with Encryption

**Encryption at rest**

AppRegistry uses Amazon DynamoDB databases
that are encrypted
at rest using Amazon-managed keys.
For more information,
refer
to information
about encryption
at rest
provided
by Amazon DynamoDB.

**Encryption in transit**

AppRegistry uses Transport Layer Security (TLS) and client-side encryption
of information
in transit
between the caller and AWS.

You can privately access AppRegistry APIs
from Amazon Virtual Private Cloud (Amazon VPC)
by creating VPC endpoints.
With VPC endpoints,
the routing
between the VPC and AppRegistry is handled
by the AWS network
without the need
for an internet gateway, NAT gateway, or VPN connection.

AWS PrivateLink powers the latest generation
of VPC endpoints
that AppRegistry uses.
AWS PrivateLink
is an AWS technology
that enables the private connectivity
between AWS services
using Elastic Network Interfaces (ENIs)
with private IPs
in your VPCs.
