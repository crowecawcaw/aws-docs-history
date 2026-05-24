# Signing Amazon Route 53 API Requests

Requests must be signed using an access key ID and a secret access key. We strongly recommend that you do not use your
AWS account credentials for everyday work with Route 53. You can use the credentials for a user or you can use AWS STS
to generate temporary security credentials.

To sign your API requests, we recommend that you use AWS Signature Version 4. For more information, see
[Access Management](../../../IAM/latest/UserGuide/reference_aws-signing.md "../../../IAM/latest/UserGuide/reference_aws-signing.md") in the _IAM User Guide_.

In addition, you might also be interested in the following topics:

- [AWS Security Credentials](../../../general/latest/gr/aws-security-credentials.md "../../../general/latest/gr/aws-security-credentials.md") – Provides
  general information about the types of credentials used for accessing AWS.
- [IAM Best Practices](../../../IAM/latest/UserGuide/IAMBestPractices.md "../../../IAM/latest/UserGuide/IAMBestPractices.md") – Presents a list of suggestions
  for using IAM service to help secure your AWS resources.
- [Temporary Security Credentials](../../../STS/latest/UsingSTS.md "../../../STS/latest/UsingSTS.md") – Describes how to create and use
  temporary security credentials.
