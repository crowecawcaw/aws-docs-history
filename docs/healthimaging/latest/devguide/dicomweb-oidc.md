

# OIDC authentication for DICOMweb APIs
<a name="dicomweb-oidc"></a>

AWS HealthImaging supports [OAuth 2.0](https://oauth.net/2/)-based authentication for DICOMweb API requests using [OpenID Connect (OIDC)](https://openid.net/specs/openid-connect-core-1_0.html), in addition to the existing [AWS Signature Version 4 (SigV4)](https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html) authentication. OIDC enables you to integrate HealthImaging directly with external identity providers (IdPs) and enables you to provide standards-based applications access to your medical imaging data through HealthImaging DICOMweb endpoints without requiring each application to have AWS credentials.

**Topics**
+ [Custom Token Verification with Lambda Authorizers](dicomweb-oidc-how.md)
+ [Set up an AWS Lambda authorizer for OIDC authentication](dicomweb-oidc-requirements.md)