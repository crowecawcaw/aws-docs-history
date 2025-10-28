# AWS managed policies for

AWS Support App in Slack

###### Note

To access and view support cases in the AWS Support Center Console, see [Manage access to AWS Support Center](accessing-support.md "accessing-support.md").

AWS Support App has the following managed policies.

###### Contents

- [AWS managed policy:
  AWSSupportAppFullAccess](support-app-managed-policies.md#security-iam-awsmanpol-support-app-full-access "support-app-managed-policies.md#security-iam-awsmanpol-support-app-full-access")
- [AWS managed policy:
  AWSSupportAppReadOnlyAccess](support-app-managed-policies.md#security-iam-support-app-read-only "support-app-managed-policies.md#security-iam-support-app-read-only")
- [AWS Support App updates to
  AWS managed policies](support-app-managed-policies.md#security-iam-awsmanpol-updates-aws-support-app "support-app-managed-policies.md#security-iam-awsmanpol-updates-aws-support-app")

## AWS managed policy:

AWSSupportAppFullAccess

You can use the [AWSSupportAppFullAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSSupportAppFullAccess$jsonEditor "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSSupportAppFullAccess$jsonEditor") managed policy to grant the IAM
role the permissions to your Slack channel configurations. You can also attach the
AWSSupportAppFullAccess policy to your IAM entities.

For more information, see [AWS Support App in Slack](aws-support-app-for-slack.md "aws-support-app-for-slack.md").

To view the permissions for this policy, see [AWSSupportAppFullAccess](../../../aws-managed-policy/latest/reference/AWSSupportAppFullAccess.md#AWSSupportAppFullAccess-json.html "../../../aws-managed-policy/latest/reference/AWSSupportAppFullAccess.md#AWSSupportAppFullAccess-json.html") in the _AWS Managed Policy Reference_.

**Permissions details**

This policy includes the following permissions:

- `servicequotas` – Describes your existing service quotas and
  requests, and creates service quota increases for your account.
- `support` – Creates, updates, and resolves your support cases.
  Updates and describes information about your cases, such as file attachments,
  correspondences, and severity levels. Initiates live chat sessions with a support
  agent.
- `iam` – Creates a service-linked role for Service Quotas.

For more information, see [Managing access to the AWS Support App](support-app-permissions.md "support-app-permissions.md").

## AWS managed policy:

AWSSupportAppReadOnlyAccess

The [AWSSupportAppReadOnlyAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSSupportAppReadOnlyAccess$jsonEditor "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSSupportAppReadOnlyAccess$jsonEditor") policy grants permissions that
allow the entity to perform read-only AWS Support App actions. For more information, see [AWS Support App in Slack](aws-support-app-for-slack.md "aws-support-app-for-slack.md").

To view the permissions for this policy, see [AWSSupportAppReadOnlyAccess](../../../aws-managed-policy/latest/reference/AWSSupportAppReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/AWSSupportAppReadOnlyAccess.md") in the _AWS Managed Policy Reference_.

**Permissions details**

This policy includes the following permissions:

- `support` – Describes support case details and communications
  added to the support cases.

## AWS Support App updates to

AWS managed policies

View details about updates to AWS managed policies for AWS Support App since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe
to the RSS feed on the [Document history](History.md "History.md") page.

The following table describes important updates to the AWS Support App managed policies
since August 17, 2022.

| AWS Support App                                                                                                                                                                                                                                                                            | Change                                                                                                                                                                                                                            | Description     | Date |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- | ---- |
| [AWSSupportAppFullAccess](#security-iam-awsmanpol-support-app-full-access "#security-iam-awsmanpol-support-app-full-access") and [AWSSupportAppReadOnlyAccess](#security-iam-support-app-read-only "#security-iam-support-app-read-only") New AWS managed policies for the AWS Support App | You can use these policies for the IAM role that you configure for your Slack channel configuration. For more information, see [Managing access to the AWS Support App](support-app-permissions.md "support-app-permissions.md"). | August 19, 2022 |
| Change log published                                                                                                                                                                                                                                                                       | Change log for the AWS Support App managed policies.                                                                                                                                                                              | August 19, 2022 |
