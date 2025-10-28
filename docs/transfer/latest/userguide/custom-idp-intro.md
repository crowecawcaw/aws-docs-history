# Working with custom identity providers

AWS Transfer Family offers several options for custom identity providers to authenticate and
authorize users for secure file transfers. Here are the main approaches:

- [Custom identity provider solution](custom-idp-toolkit.md "custom-idp-toolkit.md")—This
  topic describes the Transfer Family custom identity provider solution, using a toolkit hosted
  in GitHub.

###### Note

For most use cases, this is the recommended option. Specifically, if you need
to support more than 100 Active Directory groups, the custom identity provider
solution offers a scalable alternative without group limitations. This solution
is described in the blog post, [Simplify Active Directory authentication with a custom identity provider
for AWS Transfer Family](https://aws.amazon.com/blogs/storage/simplify-active-directory-authentication-with-a-custom-identity-provider-for-aws-transfer-family/ "https://aws.amazon.com/blogs/storage/simplify-active-directory-authentication-with-a-custom-identity-provider-for-aws-transfer-family/").

- [Using Amazon API Gateway to integrate your identity
  provider](authentication-api-gateway.md "authentication-api-gateway.md")—This topic describes how to
  use an AWS Lambda function to back an Amazon API Gateway method.

You can provide a RESTful interface with a single Amazon API Gateway method. Transfer Family calls
this method to connect to your identity provider, which authenticates and authorizes
your users for access to Amazon S3 or Amazon EFS. Use this option if you need a RESTful API to
integrate your identity provider or if you want to use AWS WAF to leverage its
capabilities for geo-blocking or rate-limiting requests. For details, see [Using Amazon API Gateway to integrate your identity
provider](authentication-api-gateway.md "authentication-api-gateway.md").

- [Dynamic permission management
  approaches](dynamic-permission-management.md "dynamic-permission-management.md")—This topic describes
  approaches for managing user permissions dynamically using session policies.

To authenticate your users, you can use your existing identity provider with
AWS Transfer Family. You integrate your identity provider using an AWS Lambda
function, which authenticates and authorizes your users for access to
Amazon S3 or Amazon Elastic File System (Amazon EFS). For details, see [Using AWS Lambda to integrate your identity
provider](custom-lambda-idp.md "custom-lambda-idp.md"). You can also
access CloudWatch graphs for metrics such as number of files and bytes transferred in the
AWS Transfer Family Management Console, giving you a single pane of glass to monitor file
transfers using a centralized dashboard.

- Transfer Family provides a blog post and a workshop that walk you through building a file transfer
  solution. This solution leverages AWS Transfer Family for managed SFTP/FTPS endpoints and
  Amazon Cognito and DynamoDB for user management.

The blog post is available at [Using Amazon Cognito as an identity provider with AWS Transfer Family and
Amazon S3](https://aws.amazon.com/blogs/storage/using-amazon-cognito-as-an-identity-provider-with-aws-transfer-family-and-amazon-s3/ "https://aws.amazon.com/blogs/storage/using-amazon-cognito-as-an-identity-provider-with-aws-transfer-family-and-amazon-s3/").
You can view the details for the workshop
[here](https://catalog.workshops.aws/transfer-family-sftp/en-US "https://catalog.workshops.aws/transfer-family-sftp/en-US").

###### Note

For custom identity providers, the username must be a minimum of 3 and a maximum of 100 characters. You can use the following
characters in the username: a–z, A-Z, 0–9, underscore '\_',
hyphen '-', period '.' and at sign '@'. The username can't start with
a hyphen '-', period '.' or at sign '@'.

When implementing a custom identity provider, consider the following best
practices:

- Deploy the solution in the same AWS account and region as your Transfer Family
  servers.
- Implement the principle of least privilege when configuring IAM roles and
  policies.
- Use features like IP allow-listing and standardized logging for enhanced
  security.
- Test your custom identity provider thoroughly in a non-production environment
  before deployment.

###### Topics

- [Custom identity provider solution](custom-idp-toolkit.md "custom-idp-toolkit.md")
- [Using AWS Lambda to integrate your identity
  provider](custom-lambda-idp.md "custom-lambda-idp.md")
- [Using Amazon API Gateway to integrate your identity
  provider](authentication-api-gateway.md "authentication-api-gateway.md")
- [Using multiple authentication methods](custom-idp-mfa.md "custom-idp-mfa.md")
- [IPv6 support for custom identity providers](custom-idp-ipv6.md "custom-idp-ipv6.md")
