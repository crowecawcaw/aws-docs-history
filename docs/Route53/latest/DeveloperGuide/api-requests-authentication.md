

# Signing Amazon Route 53 API Requests
<a name="api-requests-authentication"></a>

Requests must be signed using an access key ID and a secret access key. We strongly recommend that you do not use your AWS account credentials for everyday work with Route 53. You can use the credentials for a user or you can use AWS STS to generate temporary security credentials.

To sign your API requests, we recommend that you use AWS Signature Version 4. For more information, see [Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html) in the *IAM User Guide*. 

In addition, you might also be interested in the following topics:
+ [AWS Security Credentials](https://docs.aws.amazon.com/general/latest/gr/aws-security-credentials.html) – Provides general information about the types of credentials used for accessing AWS.
+ [IAM Best Practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/IAMBestPractices.html) – Presents a list of suggestions for using IAM service to help secure your AWS resources.
+ [Temporary Security Credentials](https://docs.aws.amazon.com/STS/latest/UsingSTS/) – Describes how to create and use temporary security credentials. 