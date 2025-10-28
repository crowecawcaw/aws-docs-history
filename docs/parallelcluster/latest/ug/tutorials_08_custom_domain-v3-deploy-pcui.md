# Deploy PCUI

Complete the following steps to create, or update, your AWS ParallelCluster UI (PCUI) deployment so that it will use your custom domain.

In this example we assume that you want to deploy PCUI with a custom domain `xyz.example.com` and the Amazon Cognito interface with a custom domain `auth-xyz.example.com`.

###### Note

Please note that customizing the Amazon Cognito domain is not required and can be left with the default value. We include this customization for completeness.

###### Note

Custom domains for Amazon Cognito are not supported in the AWS GovCloud (US) Regions.

To accomplish this, deploy the PCUI stack with the following parameters:

- **CustomDomain:** `xyz.example.com`.
- **CustomDomainCertificateArn:** the ACM certificate Amazon Resource Name (ARN) for `xyz.example.com`.
- **CognitoCustomDomain:** `auth-xyz.example.com`.
- **CognitoCustomDomainCertificateArn** to the ACM certificate Amazon Resource Name (ARN) for `xyz.example.com`.
