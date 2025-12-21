# How to use the affected policies

tool

###### Note

The following AWS Identity and Access Management (IAM) actions have reached the end of standard support on July 2023:

- `*aws-portal*` namespace
- `*purchase-orders:ViewPurchaseOrders*`
- `*purchase-orders:ModifyPurchaseOrders*`
  If you're using AWS Organizations, you can use the [bulk policy migrator scripts](migrate-iam-permissions.md "migrate-iam-permissions.md") or bulk policy migrator to update
  polices from your payer account. You can also use the [old to granular action
  mapping reference](migrate-granularaccess-iam-mapping-reference.md "migrate-granularaccess-iam-mapping-reference.md") to verify the IAM actions that need to be added.

If you have an AWS account, or are a part of an AWS Organizations created on or after
March 6, 2023, 11:00 AM (PDT), the fine-grained actions are already in effect in your
organization.

You can use the **Affected policies**
tool in the Billing console to identify IAM policies (excluding SCPs), and reference
the IAM actions affected by this migration. Use the **Affected
policies** tool to do the following tasks:

- Identify IAM policies and reference the IAM actions
  affected by this migration
- Copy the updated policy to your clipboard
- Open the affected policy in IAM policy editor
- Save the updated policy for your account
- Turn on the fine-grained permissions and disable the old actions
  This tool operates within the boundaries of the AWS account you're signed into, and
  information regarding other AWS Organizations accounts are not disclosed.

###### To use the Affected policies tool

1. Sign in to the AWS Management Console and open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. Paste the following URL into your browser to access the **Affected
   policies** tool: [https://console.aws.amazon.com/poliden/home?region=us-east-1#/](https://console.aws.amazon.com/poliden/home?region=us-east-1#/ "https://console.aws.amazon.com/poliden/home?region=us-east-1#/").

###### Note

You must have the `iam:GetAccountAuthorizationDetails`
permission to view this page. 3. Review the table that lists the affected IAM policies. Use the
**Deprecated IAM actions** column to review specific
IAM actions referenced in a policy. 4. Under the **Copy updated policy** column, choose
**Copy** to copy the updated policy to your clipboard. The
updated policy contains the existing policy and the suggested fine-grained
actions appended to it as a separate `Sid` block. This block has the
prefix `AffectedPoliciesMigrator` at the end of the policy. 5. Under the **Edit Policy in IAM Console** column, choose
**Edit** to go to IAM policy editor. You will see the
JSON of your existing policy. 6. Replace the entire existing policy with the updated policy that you copied in
step 4. You can make any other changes as needed. 7. Choose **Next** and then choose **Save
changes**. 8. Repeat steps 3 to 7 for all affected policies. 9. After you update your policies, refresh the **Affected
policies** tool to confirm there are no affected policies listed.
The **New IAM Actions Found** column should have
**Yes** for all policies and the **Copy**
and **Edit** buttons will be disabled. Your affected policies
are updated.

###### To enable fine-grained actions for your account

After you update your policies, follow this procedure to enable the fine-grained
actions for your account.

Only the management account (payer) of an organization or individual accounts can
use the **Manage New IAM Actions** section. An individual account
can enable the new actions for itself. A management account can enable new actions
for the entire organization or a subset of member accounts. If you're a
management account, update the affected policies for all member accounts and enable
the new actions for your organization. For more information, see the [How to toggle accounts between new fine-grained actions or
existing IAM actions?](https://aws.amazon.com/blogs/aws-cloud-financial-management/changes-to-aws-billing-cost-management-and-account-consoles-permissions/#How-to-toggle-accounts-between-new-fine-grained-actions-or-existing-IAM-Actions "https://aws.amazon.com/blogs/aws-cloud-financial-management/changes-to-aws-billing-cost-management-and-account-consoles-permissions/#How-to-toggle-accounts-between-new-fine-grained-actions-or-existing-IAM-Actions") section in the AWS blog post.

###### Note

To do this, you must have the following permissions:

- `aws-portal:GetConsoleActionSetEnforced`
- `aws-portal:UpdateConsoleActionSetEnforced`
- `ce:GetConsoleActionSetEnforced`
- `ce:UpdateConsoleActionSetEnforced`
- `purchase-orders:GetConsoleActionSetEnforced`
- `purchase-orders:UpdateConsoleActionSetEnforced`
  If you don't see the **Manage New IAM Actions** section, this
  means your account has already enabled the fine-grained IAM actions.

1. Under **Manage New IAM Actions**, the **Current
   Action Set Enforced** setting will have the
   **Existing** status.

Choose **Enable New actions (Fine Grained)** and then choose
**Apply changes**. 2. In the dialog box, choose **Yes**. The **Current
Action Set Enforced** status will change to **Fine
Grained**. This means the new actions are enforced for your
AWS account or for your organization. 3. (Optional) You can then update your existing policies to remove any of the old
actions.

###### Example: Before and after IAM policy

The following IAM policy has the old `aws-portal:ViewPaymentMethods`
action.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "aws-portal:ViewPaymentMethods"
            ],
            "Resource": "*"
        }
    ]
}
```

After you copy the updated policy, the following example has the new
`Sid` block with the fine-grained actions.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "aws-portal:ViewPaymentMethods"
            ],
            "Resource": "*"
        },
        {
            "Sid": "AffectedPoliciesMigrator0",
            "Effect": "Allow",
            "Action": [
                "account:GetAccountInformation",
                "invoicing:GetInvoicePDF",
                "payments:GetPaymentInstrument",
                "payments:GetPaymentStatus",
                "payments:ListPaymentPreferences"
            ],
            "Resource": "*"
        }
    ]
}
```

## Related resources

For more information, see [Sid](../../../IAM/latest/UserGuide/reference_policies_elements_sid.md "../../../IAM/latest/UserGuide/reference_policies_elements_sid.md") in
the _IAM User Guide_.

For more information about the new fine-grained actions, see the [Mapping fine-grained IAM actions reference](migrate-granularaccess-iam-mapping-reference.md "migrate-granularaccess-iam-mapping-reference.md") and [Using
fine-grained Billing actions](migrate-granularaccess-whatis.md#migrate-user-permissions "migrate-granularaccess-whatis.md#migrate-user-permissions").
