# Enabling ABAC in DynamoDB

For most of the AWS accounts, ABAC is enabled by default. Using the [DynamoDB console](https://console.aws.amazon.com/dynamodb/ "https://console.aws.amazon.com/dynamodb/"), you can confirm if ABAC is enabled for your account. To do this, make sure that you open the DynamoDB console with a role that has the [dynamodb:GetAbacStatus](#required-permissions-abac "#required-permissions-abac") permission. Then, open the **Settings** page of the DynamoDB console.

If you don’t see the **Attribute-based access control** card or if the card displays a status of **On**, it means ABAC is enabled for your account. However, if you see the **Attribute-based access control** card with a status of **Off**, as shown in the following image, ABAC isn’t enabled for your account.

![Settings page on the DynamoDB console that shows the Attribute-based access control card.](images/ddb-console-settings-page.png)
ABAC isn't enabled for AWS accounts for which tag-based conditions specified in their identity-based policies or other policies still need to be audited. If ABAC isn't enabled for your account, the tag-based conditions in your policies that are intended to act on DynamoDB tables or indexes are evaluated as if no tags are present for your resources or API requests. When ABAC is enabled for your account, the tag-based conditions in the policies of your account are evaluated considering the tags attached to your tables or API requests.

To enable ABAC for your account, we recommend that you first audit your policies as described in the [Policy audit](#policy-audit-for-abac "#policy-audit-for-abac") section. Then, include the [required permissions for ABAC](#required-permissions-abac "#required-permissions-abac") in your IAM policy. Finally, perform the steps described in [Enabling ABAC in console](#abac-enable-console "#abac-enable-console") to enable ABAC for your account in the current Region. After you enable ABAC, you can opt out within the next seven calendar days of opting in.

###### Topics

- [Auditing your policies before enabling ABAC](#policy-audit-for-abac "#policy-audit-for-abac")
- [IAM permissions required to enable ABAC](#required-permissions-abac "#required-permissions-abac")
- [Enabling ABAC in console](#abac-enable-console "#abac-enable-console")

## Auditing your policies before enabling ABAC

Before you enable ABAC for your account, audit your policies to confirm that the tag-based conditions which might exist in the policies within your account are set up as intended. Auditing your policies will help avoid surprises from authorization changes with your DynamoDB workflows after ABAC is enabled. To view examples of using attribute-based conditions with tags, and the before and after behavior of ABAC implementation, see [Examples for using ABAC with DynamoDB tables and indexes](abac-example-use-cases.md "abac-example-use-cases.md").

## IAM permissions required to enable ABAC

You need the `dynamodb:UpdateAbacStatus` permission to enable ABAC for your account in the current Region. To confirm if ABAC is enabled for your account, you must also have the `dynamodb:GetAbacStatus` permission. With this permission, you can view the ABAC status for an account in any Region. You need these permissions in addition to the permission needed for accessing the DynamoDB console.

The following IAM policy grants the permission to enable ABAC and view its status for an account in the current Region.

```
{
"version": "2012-10-17",&TCX5-2025-waiver;
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "dynamodb:UpdateAbacStatus",
                "dynamodb:GetAbacStatus"
             ],
            "Resource": "*"
        }
    ]
}
```

## Enabling ABAC in console

1. Sign in to the AWS Management Console and open the DynamoDB console at
   [https://console.aws.amazon.com/dynamodb/](https://console.aws.amazon.com/dynamodb/ "https://console.aws.amazon.com/dynamodb/").
2. From the top navigation pane, choose the Region for which you want to enable ABAC.
3. On the left navigation pane, choose **Settings**.
4. On the **Settings** page, do the following:
   1. In the **Attribute-based access control** card, choose **Enable**.
   2. In the **Confirm attribute-based access control setting** box, choose **Enable** to confirm your choice.

   This enables ABAC for the current Region and the **Attribute-based access control** card shows the status of **On**.

   If you want to opt out after enabling ABAC on the console, you can do so within the next seven calendar days of opting in. To opt out, choose **Disable** in the **Attribute-based access control** card on the **Settings** page.

   ###### Note

   Updating the status of ABAC is an asynchronous operation. If the tags in your policies aren't evaluated right away, you might need to wait for some time because the application of the changes is eventually consistent.
