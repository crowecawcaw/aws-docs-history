# Calling the API by making HTTP Query requests

This section contains general information about using the Query API for AWS Account Management. For
details about the API operations and errors, see the [API Reference](api-reference.md "api-reference.md").

###### Note

Instead of making direct calls to the AWS Account Management Query API, you can use one of the
AWS SDKs. The AWS SDKs consist of libraries and sample code for various programming
languages and platforms (Java, Ruby, .NET, iOS, Android, and more). The SDKs provide a
convenient way to create programmatic access to AWS Account Management and AWS. For example, the
SDKs take care of tasks such as cryptographically signing requests, managing errors, and
retrying requests automatically. For information about the AWS SDKs, including how to
download and install them, see [Tools for
Amazon Web Services](https://aws.amazon.com/tools "https://aws.amazon.com/tools").

With the Query API for AWS Account Management, you can call service actions. Query API requests are
HTTPS requests that must contain an `Action` parameter to indicate the operation
to be performed. AWS Account Management supports `GET` and `POST` requests for all
operations. That is, the API doesn't require you to use `GET` for some actions
and `POST` for others. However, `GET` requests are subject to the
limitation size of a URL. Although this limit is browser dependent, a typical limit is 2,048
bytes. Therefore, for Query API requests that require larger sizes, you must use a
`POST` request.

The response is an XML document. For details about the response, see the individual action
pages in the [API Reference](api-reference.md "api-reference.md").

###### Topics

- [Endpoints](#endpoints "#endpoints")
- [HTTPS required](#IAMHTTPSRequired "#IAMHTTPSRequired")
- [Signing AWS Account Management API requests](#SigVersion "#SigVersion")

## Endpoints

AWS Account Management has a single global API endpoint that is hosted in the US East (N. Virginia)
AWS Region.

For more information about AWS endpoints and Regions for all services, see [Regions and Endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md")
in the _AWS General Reference_.

## HTTPS required

Because the Query API can return sensitive information such as security credentials,
you must use HTTPS to encrypt all API requests.

## Signing AWS Account Management API requests

Requests must be signed using an access key ID and a secret access key. We strongly
recommend that you don't use your AWS root account credentials for everyday work with
AWS Account Management. You can use the credentials for an AWS Identity and Access Management (IAM) user or temporary
credentials such as you use with an IAM role.

To sign your API requests, you must use AWS Signature Version 4. For information
about using Signature Version 4, see [Signing AWS API requests](../../../IAM/latest/UserGuide/reference_aws-signing.md "../../../IAM/latest/UserGuide/reference_aws-signing.md")
in the _IAM User Guide_.

For more information, see the following:

- [AWS
  Security Credentials](../../../IAM/latest/UserGuide/security-creds.md "../../../IAM/latest/UserGuide/security-creds.md") – Provides general information about the
  types of credentials that you can use to access AWS.
- [Security
  best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") – Offers suggestions for using the
  IAM service to help secure your AWS resources, including those in
  AWS Account Management.
- [Temporary security credentials in IAM](../../../IAM/latest/UserGuide/id_credentials_temp.md "../../../IAM/latest/UserGuide/id_credentials_temp.md") – Describes how to
  create and use temporary security credentials.
