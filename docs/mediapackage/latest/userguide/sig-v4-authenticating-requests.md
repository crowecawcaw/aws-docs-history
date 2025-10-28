# Authenticating Requests (AWS Signature Version 4)

Every interaction with MediaPackage is either authenticated or anonymous. This section explains
request authentication with the AWS Signature Version 4 algorithm.

###### Note

If you use the AWS SDKs or AWS CLI to send your requests, you don't need to read this section
because these tools authenticate your requests by using access keys that you
provide. You must only sign AWS API requests as described in this documentation if you do
not use an AWS SDK or AWS CLI to send AWS API requests.

When you send API requests to AWS, you must sign them so that AWS can identify the sender. For security,
most requests are signed using your AWS security credentials.

When MediaPackage receives an authenticated request, it recreates the signature using the
authentication information contained in the request. If the signatures match, MediaPackage
processes the request. Otherwise, it rejects the request.

AWS Signature Version 4 is the AWS signing protocol. AWS also supports an extension,
Signature Version 4A, which supports signatures for multi-Region API requests.

For additional information about AWS Signature Version 4, see:

- [Signing AWS
  API requests](../../../IAM/latest/UserGuide/reference_aws-signing.md "../../../IAM/latest/UserGuide/reference_aws-signing.md") in the _IAM User Guide_
- [Authenticating Requests (AWS Signature Version 4)](../../../AmazonS3/latest/API/sig-v4-authenticating-requests.md "../../../AmazonS3/latest/API/sig-v4-authenticating-requests.md") in the _Amazon Simple Storage Service API Reference_

## Creating a signed AWS API request

For steps to create a signed AWS API request, see:

- [Create a signed AWS
  API request](../../../IAM/latest/UserGuide/create-signed-request.md "../../../IAM/latest/UserGuide/create-signed-request.md") in the _IAM User Guide_
- [Signature Calculations for the Authorization
  Headers: Transferring Payload in a Single Chunk](../../../AmazonS3/latest/API/sig-v4-header-based-auth.md "../../../AmazonS3/latest/API/sig-v4-header-based-auth.md") in the _Amazon Simple Storage Service API Reference_

## Troubleshooting signed AWS

API requests

For troubleshooting help with your signed requests, see [Troubleshoot signed requests for AWS
APIs](../../../IAM/latest/UserGuide/signature-v4-troubleshooting.md "../../../IAM/latest/UserGuide/signature-v4-troubleshooting.md") in the _IAM User Guide_.
