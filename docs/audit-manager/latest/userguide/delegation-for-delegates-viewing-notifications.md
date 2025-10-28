# Viewing your notifications

for incoming delegation requests

When an audit owner requests your assistance with reviewing a control set, you receive a
notification that informs you of the control set that they delegated to you.

## Prerequisites

Make sure your IAM identity has appropriate permissions to view notifications in
AWS Audit Manager. Two suggested policies that grant these permissions are [Allow users full administrator access to
AWS Audit Manager](security_iam_id-based-policy-examples.md#example-2 "security_iam_id-based-policy-examples.md#example-2") and [Allow users management access to
AWS Audit Manager](security_iam_id-based-policy-examples.md#management-access "security_iam_id-based-policy-examples.md#management-access").

## Procedure

###### To view your notifications

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home "https://console.aws.amazon.com/auditmanager/home").
2. Choose **Notifications** in the left navigation pane.
3. On the **Notifications** page, review the list of control sets that
   have been delegated to you for review. The table includes the following
   information:

| Name            | Description                                                        |
| --------------- | ------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Date**        | The date when the control set was delegated.                       |
| **Assessment**  | The name of the assessment that's associated with the control set. |
| **Control set** | The name of the control set.                                       |
| **Source**      | The user or role that delegated the control set to you.            |
| **Description** | Instructions that are provided by the audit owner.                 | ###### Tip You can also subscribe to an SNS topic to receive email alerts when a control set is delegated to you for review. For more information, see [Notifications in AWS Audit Manager](notifications.md "notifications.md"). ## Next steps When you're ready to start reviewing the controls that were delegated to you, see [Reviewing the delegated control set and its related evidence](delegation-for-delegates-reviewing-control-set-and-evidence.md "delegation-for-delegates-reviewing-control-set-and-evidence.md"). |
