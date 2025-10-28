# Data protection in AWS Elemental MediaLive

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/")
applies to data protection in AWS Elemental MediaLive. As described in this model, AWS is
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
  customers' email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with MediaLive or other AWS services
  using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into
  tags or free-form text fields used for names may be used for billing or diagnostic logs. If you
  provide a URL to an external server, we strongly recommend that you do not include credentials
  information in the URL to validate your request to that server.

If you provide a URL to an external server, MediaLive requires that you do
not include credentials information in the URL to validate your request to
that server. If a URL to an external server requires credentials, we recommend
that you use the Parameter Store feature in AWS Systems Manager. For more information,
and the steps to implement AWS Systems Manager Parameter Store, see [Requirements for AWS Systems Manager—creating password parameters in
Parameter Store](requirements-for-EC2.md "requirements-for-EC2.md").

AWS Elemental MediaLive doesn't require that you supply any customer data. There are no
fields in channels, devices, inputs, input security groups, multiplexes, or
reservations, where there is an expectation that you will provide customer
data.

MediaLive includes features such as the AWS Systems Manager Parameter Store that
provide you with a secure way to handle sensitive information. You should
always use these features to pass a password; you should not circumvent them
by including a password in a URL.

## Deleting data in

MediaLive

You can delete data from AWS Elemental MediaLive by deleting the object, for example,
the channel or input. You can delete data using the console, REST API, AWS CLI,
or AWS SDKs. The data will be deleted; no further steps are required after
you delete data by completing a delete operation.

To delete data using the console, see the following sections:

- [Deleting a channel](editing-deleting-channel.md#deleting-a-channel "editing-deleting-channel.md#deleting-a-channel")
- [Working with Link input device](eml-devices.md "eml-devices.md")
- [Deleting an input](delete-input.md "delete-input.md")
- [Deleting an input security group](delete-input-security-group.md "delete-input-security-group.md")
- [Deleting multiplexes, programs, and channels](delete-multiplex-program.md "delete-multiplex-program.md")
- [Deleting an expired
  reservation](deleting-reservations.md "deleting-reservations.md")
