

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# AWS prerequisites
<a name="cloud-connector-prereqs-aws"></a>

Complete the following steps in your AWS account.

**To set up the AWS side of the federation**

1. 

**Enable outbound web identity federation**

   Enable outbound web identity federation in your AWS account IAM settings. This allows AWS to issue OIDC tokens that Azure can verify.

   In the IAM console, navigate to **Account settings** and enable **Outbound web identity federation**. Alternatively, use the AWS CLI:

   ```
   aws iam enable-outbound-web-identity-federation
   ```

1. 

**Note the OIDC issuer URL**

   After enabling outbound web identity federation, note the AWS OIDC issuer URL for your account. The URL has the following format:

   ```
   https://{{UNIQUE_ID}}.tokens.sts.global.api.aws
   ```

   You need this URL when configuring the federated identity credential in Azure.