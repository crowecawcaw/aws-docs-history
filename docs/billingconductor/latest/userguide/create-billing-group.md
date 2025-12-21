# Creating billing groups

## Using Billing Conductor as a standalone service

You can use AWS Billing Conductor to create billing groups to organize your accounts. By default, payer
accounts with admin permissions can create billing groups. Each billing group is mutually
exclusive. This means that an account can only belong to one billing group in a given billing
period. Although you can see the billing group segmentation immediately, it takes up to 24 hours
after creating a billing group to see the group’s custom rates reflected.

###### Note

Moving accounts across billing groups in the middle of the month will initiate the
recomputation of both billing groups back to the start of the billing period. Moving
accounts mid-month doesn't affect previous billing periods.

###### To create a billing group

1. Sign in to the AWS Management Console and open AWS Billing Conductor at
   [https://console.aws.amazon.com/billingconductor/](https://console.aws.amazon.com/billingconductor/ "https://console.aws.amazon.com/billingconductor/").
2. In the navigation pane, choose **Billing groups**.
3. Choose **Create billing group**.
4. For **Billing group details**, enter the name of the billing group. For
   naming restrictions, see [Quotas and restrictions](limits.md "limits.md").
5. (Optional) For **Description**, enter a description for the billing
   group.
6. Choose `Standard` as the **billing group type**.
7. For **Pricing plan**, choose a pricing plan to associate with the billing
   group. To create a pricing plan, see [Creating pricing plans](create-pricingplan.md "create-pricingplan.md").
   - Alternatively, you can use AWS managed `BasicPricingPlan`, which is available in the pricing plan dropdown list. The `BasicPricingPlan` calculates gross cloud costs from AWS. You cannot edit or delete this pricing plan.

8. (Optional) For **Additional settings**, you can enable automatic account
   association for the billing group.

###### Notes

    * Only *one billing group* can have automatic account
     association.
    * Once you enable this feature, accounts that are created or added to your organization
     will be automatically associated to this billing group. You will also receive email notification
     when the automatic association happens.
    * If you currently have a CloudTrail logging trail, you can review your automatic account associations in your CloudTrail log.

9. Under **Accounts**, choose one or more accounts to add to the billing
   group _or_ choose **Import organizational unit** to
   automatically select the accounts that are within an organizational unit. For a policy example
   to grant access to the import OU feature, see [Granting Billing Conductor
   access to the import organizational unit feature](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-ABCaccessOU "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-ABCaccessOU").

You can use the table filter to sort by account names, account IDs, or the root email
address that's associated with an account. 10. The primary account inherits the ability to see pro forma cost and usage across the billing
group, and can generate a pro forma Cost and Usage Reports (AWS CUR) for the billing group.

If you choose a primary account that joined your organization during the current month,
the pro forma costs for all accounts in that billing group will only include cost and usage
accrued since the primary account joined the organization. To check the join date, choose
**Validate joined date**. For more information, see [Understanding how the primary account join and leave date affect pro forma billing](best-practices.md#understand-primary-account-join-date "best-practices.md#understand-primary-account-join-date"). 11. Choose **Create billing group**.

###### Notes

    * You must select your primary account in step 9. You can't change your primary account
     after the billing group is created. To assign a new primary account, delete the billing
     group and regroup your accounts. While a payer account can be included within a billing
     group, a payer account can't be assigned the role of the primary account.
    * If the primary account of a billing group leaves your organization and this billing
     group has automatic account association enabled, it will continue to automatically associate
     accounts until the end of the month. Then, the billing group will be automatically deleted.
     You can enable automatic account association for an existing billing group or create another
     one.

## Using Billing Conductor with billing transfer

In one-level transfers, the console will create a new billing group with selected pricing configuration and assign it to the AWS organization of the bill source account, when the transfer begins. The billing group status appears as 'pending' until the billing transfer date begins.

###### Note

If you set up billing transfers programmatically using the billing transfer APIs through the AWS SDK and AWS CLI, you must also call Billing Conductor APIs to create billing groups and associate pricing plans. This ensures that bill source accounts can view pro forma billing data in their billing and cost management console.

In two-level transfers, the bill transfer (bill receiver) account must configure a billing group manually on the bill source accounts' AWS Organizations through Billing Conductor. This step enables the bill transfer account to view the costs of their bill source accounts as allocated by the bill transfer (bill receiver) account. For users in the APN Distribution programs, this enables downstream sellers to see how much they owe their distributor for their end-customers' usage.

For support with automating this action, contact Support.

###### Important

If a billing group is not assigned to the AWS organization of the bill source account, all the accounts in that AWS organization may not have access to the pro forma cost data when accessing Billing and Cost Management tools.

Usage data will always remain available to the bill source account and the accounts in its AWS organizations via CloudWatch.

###### To create a billing group manually for billing transfer recovery or two-level transfers

Use this procedure when automatic billing group creation fails during billing transfer setup or when using two-level transfers.

1. Sign in to the AWS Management Console and open AWS Billing Conductor at
   [https://console.aws.amazon.com/billingconductor/](https://console.aws.amazon.com/billingconductor/ "https://console.aws.amazon.com/billingconductor/").
2. In the navigation pane, choose **Billing groups**.
3. Choose **Create billing group**.
4. For **Billing group details**, enter the name of the billing group. For
   naming restrictions, see [Quotas and restrictions](limits.md "limits.md").
5. (Optional) For **Description**, enter a description for the billing
   group.
6. Choose `Standard` as the **billing group type**.
7. Choose an individual AWS Organizations that's transferring its bills for which you want to create a billing group.
   1. If you're using billing transfer with two-level transfers, expand the transfer name to view the organizations available for billing group creation.
   2. The list displays only organizations that aren't associated with a billing group. Organizations that already have an associated billing group don't appear in this list.

8. For **Pricing plan**, choose a pricing plan to associate with the billing
   group. To create a pricing plan, see [Creating pricing plans](create-pricingplan.md "create-pricingplan.md").
9. Choose **Create billing group**.
