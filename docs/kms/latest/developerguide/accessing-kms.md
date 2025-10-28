# Accessing AWS Key Management Service

You can work with AWS KMS in the following ways:

###### Topics

- [AWS Management Console](#kms-console "#kms-console")
- [AWS Command Line Interface](#kms-cli "#kms-cli")
- [AWS KMS REST API](#kms-api "#kms-api")
- [AWS SDKs](#kms-sdk "#kms-sdk")
- [Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md")
- [AWS Encryption SDK](#crypto-sdk "#crypto-sdk")
- [AWS KMS eventual consistency](#programming-eventual-consistency "#programming-eventual-consistency")
- [Using hybrid post-quantum TLS with AWS KMS](pqtls.md "pqtls.md")
- [Connect to AWS KMS through a VPC endpoint](kms-vpc-endpoint.md "kms-vpc-endpoint.md")
- [Dual-stack endpoint support](ipv6-kms.md "ipv6-kms.md")

## AWS Management Console

The console is a web-based user interface for managing AWS KMS and AWS resources. If
you've signed up for an AWS account, you can access the AWS KMS console by signing into the
AWS Management Console and choosing AWS KMS from the AWS Management Console home page.

### Permissions required to use the AWS KMS console

To work with the AWS KMS console, users must have a minimum set of permissions that allow
them to work with the AWS KMS resources in their AWS account. In addition to these AWS KMS
permissions, users must also have permissions to list IAM users and IAM roles. If you
create an IAM policy that is more restrictive than the minimum required permissions, the
AWS KMS console won't function as intended for users with that IAM policy.

For the minimum permissions required to allow a user read-only access to the AWS KMS
console, see [Allow a user to view KMS keys in
the AWS KMS console](customer-managed-policies.md#iam-policy-example-read-only-console "customer-managed-policies.md#iam-policy-example-read-only-console").

To allow users to work with the AWS KMS console to create and manage KMS keys, attach
the **AWSKeyManagementServicePowerUser** managed policy to the
user, as described in [AWS managed policies for AWS Key Management Service](security-iam-awsmanpol.md "security-iam-awsmanpol.md").

You don't need to allow minimum console permissions for users that are working with the
AWS KMS API through the [AWS SDKs](https://aws.amazon.com/tools/#sdk "https://aws.amazon.com/tools/#sdk"), [AWS Command Line Interface](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md"), or [AWS Tools for PowerShell](../../../powershell/latest/userguide.md "../../../powershell/latest/userguide.md"). However, you do
need to grant these users permission to use the API. For more information, see [Permissions reference](kms-api-permissions-reference.md "kms-api-permissions-reference.md").

## AWS Command Line Interface

You can use the AWS CLI tools to issue commands or build scripts at your system's command
line to perform AWS (including AWS KMS) tasks.

For more information about using AWS KMS through the AWS CLI, see the [AWS CLI Command Reference](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/index.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/index.html")

## AWS KMS REST API

The architecture of AWS KMS is designed to be programming language-neutral. The REST
API is an HTTP interface to AWS KMS. With the REST API, you use
standard HTTP requests to create, fetch, and delete keys.

For more information on using the AWS KMS REST API, see the [AWS Key Management Service API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md")

## AWS SDKs

AWS provides SDKs (software development kits) that consist of libraries and sample code
for common programming languages and platforms (Java, JavaScript, C, Python, and so on). The
AWS SDKs provide a convenient way to create programmatic access to AWS KMS and AWS. AWS KMS is
a REST service. You can send requests to AWS KMS using the AWS SDK libraries,
which wrap the underlying AWS KMS REST API and simplify your
programming tasks. For information about the AWS SDKs, including how to
download and install them, see [Tools to Build on
AWS](https://aws.amazon.com/developer/tools "https://aws.amazon.com/developer/tools").

The [Code examples for AWS KMS using AWS SDKs](service_code_examples.md "service_code_examples.md") provides
a good starting point for using AWS KMS through the AWS SDKs.

## AWS Encryption SDK

The AWS Encryption SDK is a tool for implementing client-side encryption in your application.
It does not provide full access to KMS, but instead it integrates with AWS KMS, or can be used
as a stand-alone SDK without referencing KMS keys. Libraries are available for Java,
JavaScript, C, Python, and other programming languages.

For more information, see the [AWS Encryption SDK Developer Guide](../../../encryption-sdk/latest/developer-guide/introduction.md "../../../encryption-sdk/latest/developer-guide/introduction.md").

AWS KMS key policies and IAM policies

## AWS KMS eventual consistency

The AWS KMS API follows an [eventual consistency](https://en.wikipedia.org/wiki/Eventual_consistency "https://en.wikipedia.org/wiki/Eventual_consistency") model due to the distributed nature of the system. As a
result, changes to AWS KMS resources might not be immediately visible to the subsequent
commands you run.

When you perform AWS KMS API calls, there might be a brief delay before the change is
available throughout AWS KMS. It typically takes less than a few seconds for the change to
propagate throughout the system, but in some cases it can take several minutes. You might get
unexpected errors, such as a `NotFoundException` or an
`InvalidStateException`, during this time. For example, AWS KMS might return a
`NotFoundException` if you call `GetParametersForImport`
immediately after calling `CreateKey`.

We recommend that you configure a retry strategy on your AWS KMS clients to automatically
retry operations after a brief waiting period. For more information, see [Retry behavior](../../../sdkref/latest/guide/feature-retry-behavior.md "../../../sdkref/latest/guide/feature-retry-behavior.md") in the
AWS SDKs and Tools Reference Guide.

For grant related API calls, you can [use a grant
token](using-grant-token.md "using-grant-token.md") to avoid any potential delay and use the permissions in a grant
immediately. For more information, see [Eventual
consistency (for grants)](grants.md#terms-eventual-consistency "grants.md#terms-eventual-consistency").
