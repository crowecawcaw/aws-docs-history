# Prerequisites

The following sections describe the prerequisites required to use the AWS Transfer Family service. At
a minimum, you need to create an Amazon Simple Storage Service (Amazon S3) bucket and provide access to that bucket
through an AWS Identity and Access Management (IAM) role. Your role also needs to establish a trust relationship.
This trust relationship allows Transfer Family to assume the IAM role to access your bucket so that
it can service your users' file transfer requests.

For information about IPv6 support for AWS Transfer Family servers, see [IPv6 support for Transfer Family servers](ipv6-support.md "ipv6-support.md") in the Managing servers chapter.

###### Topics

- [Supported AWS Regions, endpoints and quotas for Transfer Family
  servers](#regions "#regions")
- [Sign up for AWS](requirements-aws-signup.md "requirements-aws-signup.md")
- [Configure storage to use with AWS Transfer Family
  servers](configure-storage.md "configure-storage.md")
- [Create an IAM role and policy](requirements-roles.md "requirements-roles.md")

## Supported AWS Regions, endpoints and quotas for Transfer Family

servers

To connect programmatically to an AWS service, you use an endpoint. For example, the
endpoint for customers in US East (Ohio) region (`us-east-2`), is
`transfer.us-east-2.amazonaws.com`. Service quotas, also referred
to as limits, are the maximum number of service resources or operations for your
AWS account. In this guide, you can find quotas in [AS2 quotas](create-b2b-server.md#as2-quotas "create-b2b-server.md#as2-quotas") and [Quotas for SFTP
connectors](scale-and-limits-sftp-connector.md#limits-sftp-connector "scale-and-limits-sftp-connector.md#limits-sftp-connector").

For more information about supported AWS Regions, endpoints, and service quotas, see
[AWS Transfer Family
endpoints and quotas](../../../general/latest/gr/transfer-service.md "../../../general/latest/gr/transfer-service.md") in the _Amazon Web Services General Reference_.

For Transfer Family web apps, the supported regions are listed in [AWS Regions for Transfer Family web apps](web-app.md#webapp-regions "web-app.md#webapp-regions"). For quotas that pertain to Transfer Family web apps, see
[Web app quotas](webapp-end-users.md#end-user-quotas "webapp-end-users.md#end-user-quotas").
