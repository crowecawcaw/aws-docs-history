# AWS prerequisites

Complete the following steps in your AWS account.

###### To set up the AWS side of the federation

1. ###### Enable outbound web identity federation

Enable outbound web identity federation in your AWS account IAM
settings. This allows AWS to issue OIDC tokens that Azure can
verify.

In the IAM console, navigate to **Account
settings** and enable **Outbound web
identity federation**. Alternatively, use the AWS CLI:

```
aws iam enable-outbound-web-identity-federation
```

2. ###### Note the OIDC issuer URL

After enabling outbound web identity federation, note the AWS OIDC
issuer URL for your account. The URL has the following format:

```
https://`UNIQUE_ID`.tokens.sts.global.api.aws
```

You will need this URL when configuring the federated identity credential
in Azure.
