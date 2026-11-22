

# Setting up AWS Abuse Signal API

With AWS Abuse Signal API, you can programmatically submit and track reports of suspected abuse of AWS resources. Before you submit abuse reports, set up an AWS account and an AWS Identity and Access Management (IAM) identity that can sign requests and call the `abuse:` actions. After you complete the steps on this page, continue to [Getting started with AWS Abuse Signal API](getting-started.md).

**Topics**
+ [Sign up for AWS](#setting-up-aws-sign-up)
+ [Create an IAM identity](#setting-up-create-identity)
+ [Grant AWS Abuse Signal API permissions](#setting-up-permissions)

## Sign up for AWS
<a name="setting-up-aws-sign-up"></a>

If you do not have an AWS account, complete the following steps to create one.

1. Open the [AWS sign-up page](https://portal.aws.amazon.com/billing/signup).

1. Follow the online instructions.

   Part of the sign-up procedure involves receiving a phone call and entering a verification code on the phone keypad.

## Create an IAM identity
<a name="setting-up-create-identity"></a>

To call AWS Abuse Signal API, use an IAM identity that you control, such as an IAM user, an IAM role, or a federated identity. Administrative access is not required. Grant the identity only the `abuse:` permissions that it needs, as described in [Grant AWS Abuse Signal API permissions](#setting-up-permissions).

For IAM security best practices, such as using roles with short-lived credentials and securing the root user, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the *IAM User Guide*.

## Grant AWS Abuse Signal API permissions
<a name="setting-up-permissions"></a>

To call AWS Abuse Signal API, an identity needs IAM permissions for the actions it uses:
+  `abuse:CreateAbuseReport` – Submit a new abuse report.
+  `abuse:GetAbuseReportStatus` – Retrieve the status of an abuse report.
+  `abuse:ListAbuseReportStatuses` – List abuse report statuses.

Following least privilege, grant `abuse:CreateAbuseReport` to reporting identities and grant the read actions only where status tracking is needed. For ready-to-use least-privilege policies, see [AWS Abuse Signal API identity-based policy examples](security-iam-id-based-policy-examples.md).

**Note**  
Sign every request with SigV4 or SigV4a using the service signing name `abuse`. For multi-Region use, sign with SigV4a (see [Choosing SigV4 or SigV4a](regions-endpoints.md#regions-endpoints-signing)). For more information, see [Identity and access management for AWS Abuse Signal API](security-iam.md).