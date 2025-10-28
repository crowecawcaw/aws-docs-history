# Creating billing groups

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
6. For **Pricing plan**, choose a pricing plan to associate with the billing
   group. To create a pricing plan, see [Creating pricing plans](create-pricingplan.md "create-pricingplan.md").
   - Alternatively, you can use AWS managed `BasicPricingPlan`, which is available in the pricing plan dropdown list. The `BasicPricingPlan` calculates gross cloud costs from AWS. You cannot edit or delete this pricing plan.

7. (Optional) For **Additional settings**, you can enable automatic account
   association for the billing group.

###### Notes

    * Only *one billing group* can have automatic account
     association.
    * Once you enable this feature, accounts that are created or added to your organization
     will be automatically associated to this billing group.
    * If you currently have a CloudTrail logging trail, you can review your automatic account associations in your CloudTrail log.

8. Under **Accounts**, choose one or more accounts to add to the billing
   group _or_ choose **Import organizational unit** to
   automatically select the accounts that are within an organizational unit. For a policy example
   to grant access to the import OU feature, see [Granting Billing Conductor
   access to the import organizational unit feature](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-ABCaccessOU "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-ABCaccessOU").

You can use the table filter to sort by account names, account IDs, or the root email
address that's associated with an account. 9. The primary account inherits the ability to see pro forma cost and usage across the billing
group, and can generate a pro forma Cost and Usage Reports (AWS CUR) for the billing group.

If you choose a primary account that joined your organization during the current month,
the pro forma costs for all accounts in that billing group will only include cost and usage
accrued since the primary account joined the organization. To check the join date, choose
**Validate joined date**. For more information, see [Understanding how the primary account join and leave date affect pro forma billing](best-practices.md#understand-primary-account-join-date "best-practices.md#understand-primary-account-join-date"). 10. Choose **Create billing group**.

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
