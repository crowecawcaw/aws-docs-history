

# Creating billing groups
<a name="create-billing-group"></a>

## Using Billing Conductor as a standalone service
<a name="create-billing-group-standalone"></a>

You can use AWS Billing Conductor to create billing groups to organize your accounts. By default, payer accounts with admin permissions can create billing groups. Each billing group is mutually exclusive. This means that an account can only belong to one billing group in a given billing period. Although you can see the billing group segmentation immediately, it takes up to 24 hours after creating a billing group to see the group's custom rates reflected.

**Note**  
Moving accounts across billing groups in the middle of the month will initiate the recomputation of both billing groups back to the start of the billing period. Moving accounts mid-month doesn't affect previous billing periods.

**To create a billing group**

1. Sign in to the AWS Management Console and open AWS Billing Conductor at [https://console.aws.amazon.com/billingconductor/](https://console.aws.amazon.com/billingconductor/).

1. In the navigation pane, choose **Billing groups**.

1. Choose **Create billing group**.

1. For **Billing group details**, enter the name of the billing group. For naming restrictions, see [Quotas and restrictions](limits.md).

1. (Optional) For **Description**, enter a description for the billing group.

1. Choose `Standard` as the **billing group type**.

1. For **Pricing plan**, choose a pricing plan to associate with the billing group. To create a pricing plan, see [Creating pricing plans](create-pricingplan.md).
   + Alternatively, you can use AWS managed `BasicPricingPlan`, which is available in the pricing plan dropdown list. The `BasicPricingPlan` calculates gross cloud costs from AWS. You cannot edit or delete this pricing plan.

1. (Optional) For **Additional settings**, you can enable automatic account association for the billing group.
**Notes**  
Only *one billing group* can have automatic account association.
Once you enable this feature, accounts that are created or added to your organization will be automatically associated to this billing group. You will also receive email notification when the automatic association happens.
If you currently have a CloudTrail logging trail, you can review your automatic account associations in your CloudTrail log.

1. Under **Accounts**, choose one or more accounts to add to the billing group *or* choose **Import organizational unit ** to automatically select the accounts that are within an organizational unit. For a policy example to grant access to the import OU feature, see [Granting Billing Conductor access to the import organizational unit feature](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-ABCaccessOU).

   You can use the table filter to sort by account names, account IDs, or the root email address that's associated with an account.

1. The primary account inherits the ability to see pro forma cost and usage across the billing group, and can generate a pro forma Cost and Usage Reports (AWS CUR) for the billing group.

   If you choose a primary account that joined your organization during the current month, the pro forma costs for all accounts in that billing group will only include cost and usage accrued since the primary account joined the organization. To check the join date, choose **Validate joined date**. For more information, see [Understanding how the primary account join and leave date affect pro forma billing](best-practices.md#understand-primary-account-join-date).

1. Choose **Create billing group**.
**Notes**  
You must select your primary account in step 9. You can't change your primary account after the billing group is created. To assign a new primary account, delete the billing group and regroup your accounts. While a payer account can be included within a billing group, a payer account can't be assigned the role of the primary account.
If the primary account of a billing group leaves your organization and this billing group has automatic account association enabled, it will continue to automatically associate accounts until the end of the month. Then, the billing group will be automatically deleted. You can enable automatic account association for an existing billing group or create another one.

## Using Billing Conductor with billing transfer
<a name="create-billing-group-tandem"></a>

In one-level transfers, the console will create a new billing group with selected pricing configuration and assign it to the AWS organization of the bill source account, when the transfer begins. The billing group status appears as 'pending' until the billing transfer date begins.

**Note**  
If you set up billing transfers programmatically using the billing transfer APIs through the AWS SDK and AWS CLI, you must also call Billing Conductor APIs to create billing groups and associate pricing plans. This ensures that bill source accounts can view pro forma billing data in their billing and cost management console.

In two-level transfers, the bill transfer (bill receiver) account must configure a billing group manually on the bill source accounts' AWS Organizations through Billing Conductor. This step enables the bill transfer account to view the costs of their bill source accounts as allocated by the bill transfer (bill receiver) account. For users in the APN Distribution programs, this enables downstream sellers to see how much they owe their distributor for their end-customers' usage.

**Important**  
If a billing group is not assigned to the AWS organization of the bill source account, all the accounts in that AWS organization may not have access to the pro forma cost data when accessing Billing and Cost Management tools.  
Usage data will always remain available to the bill source account and the accounts in its AWS organizations via CloudWatch.

### Automatically creating billing groups for two-level transfers
<a name="auto-billing-group-creation-preference"></a>

You may enable the auto billing group creation preference for a billing transfer in the Billing Transfer invite details, to automatically create billing groups when you operate with two-level transfers. When the preference is enabled, AWS Billing Conductor automatically creates a billing group for each new account that indirectly transfers its bill to your account, applying the pricing plan that you selected. Automatically created billing groups are named `AutoCreated-` followed by the bill source account ID, the ID of the account that transfers its bill to it, and the billing transfer ID.

The preference is disabled by default, and it applies to individual transfers. You configure it on each inbound billing transfer where you want automatic creation, so enabling it on one billing transfer doesn't affect any other billing transfer.

Enabling this preference only applies to future transfers – it doesn't create billing groups for indirect billing transfers that were accepted before the preference was enabled. For pre-existing transfers, you need to create the billing groups manually. For more information, see [Creating a billing group manually](#create-billing-group-manual).

**Note**  
This preference uses a service-linked role in your account to create billing groups. For more information, see [Using service-linked roles for Billing Conductor](using-service-linked-roles.md).

When you disable the preference, the billing groups that AWS Billing Conductor already created remain in your account, and only future automatic creation stops. Changing the pricing plan works the same way: the new pricing plan applies to the billing groups that are created afterward, and existing billing groups keep the pricing plan that they were created with.

**Note**  
Shortly after a billing transfer becomes active, AWS Billing Conductor might retry the automatic billing group creation for that billing transfer, as a safeguard in case an earlier attempt was missed. If a billing group already exists, no new billing group is created. However, if you delete an automatically created billing group during this time while the preference is still enabled, a retry can recreate it. To stop automatic creation for a billing transfer, disable the preference rather than deleting the billing group.  
For the same reason, if you have a CloudTrail trail, you might see additional `GetBillingTransferPreference` and `CreateBillingGroup` events made by the service-linked role, even when no new billing group is created.

If a pricing plan is selected in an auto billing group creation preference, you can't delete that pricing plan. To delete that pricing plan, select a different pricing plan within the preference settings, or disable the preference.

To set or view the preference, you need permissions for the `billingconductor:UpdateBillingTransferPreference`, `billingconductor:GetBillingTransferPreference`, and `organizations:DescribeResponsibilityTransfer` actions. Enabling the preference also requires the `iam:CreateServiceLinkedRole` permission. To control which pricing plans can be selected, use the `billingconductor:PricingPlanArn` condition key. For more information, see [Condition keys](security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies-conditionkeys).

**Note**  
In a one-level transfer, the preference can still be enabled, but it has no effect.

**To enable automatic billing group creation for a billing transfer**

1. Open the AWS Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, under **Preferences and Settings**, choose **Billing Transfer**.

1. Choose the **Inbound billing** tab, and then select the billing transfer that you want to change.

1. Go to the **Edit preference** page through the details page or through **Actions**.
**Note**  
**Edit preference** is available while the billing transfer is active. A billing transfer is active when the invitation is pending, when the transfer is accepted, or when the transfer is withdrawn but hasn't ended yet. It's also available for a limited time after an invitation is declined, canceled, or expired, so that you can disable the preference and release the pricing plan that it selected.

1. For **Enable auto billing group creation**, turn on the toggle.

1. For **Pricing plan for automatically created billing groups**, choose the pricing plan to apply to every billing group that this preference creates. To create a pricing plan, see [Creating pricing plans](create-pricingplan.md).

1. Choose **Save**.

You can also enable the preference while you send a billing transfer invitation, using the **Preferences** section on the invitation page.

To review the current preference, choose the name of the billing transfer to open its details page, and then find the **Preferences** section. This section shows the **Status** of the auto billing group creation preference and the **Pricing plan** that's applied to the billing groups that it creates.

To manage the preference programmatically, use the `UpdateBillingTransferPreference` and `GetBillingTransferPreference` operations. For more information, see the [AWS Billing Conductor API Reference](https://docs.aws.amazon.com/billingconductor/latest/APIReference/Welcome.html).

### Creating a billing group manually
<a name="create-billing-group-manual"></a>

**To create a billing group manually for billing transfer recovery or two-level transfers**

Use this procedure when the console doesn't create the billing group during billing transfer setup, or for two-level transfers when the auto billing group creation preference isn't turned on.

1. Sign in to the AWS Management Console and open AWS Billing Conductor at [https://console.aws.amazon.com/billingconductor/](https://console.aws.amazon.com/billingconductor/).

1. In the navigation pane, choose **Billing groups**.

1. Choose **Create billing group**.

1. For **Billing group details**, enter the name of the billing group. For naming restrictions, see [Quotas and restrictions](limits.md).

1. (Optional) For **Description**, enter a description for the billing group.

1. Choose `Standard` as the **billing group type**.

1. Choose an individual AWS Organizations that's transferring its bills for which you want to create a billing group.

   1. If you're using billing transfer with two-level transfers, expand the transfer name to view the organizations available for billing group creation.

   1. The list displays only organizations that aren't associated with a billing group. Organizations that already have an associated billing group don't appear in this list.

1. For **Pricing plan**, choose a pricing plan to associate with the billing group. To create a pricing plan, see [Creating pricing plans](create-pricingplan.md).

1. Choose **Create billing group**.