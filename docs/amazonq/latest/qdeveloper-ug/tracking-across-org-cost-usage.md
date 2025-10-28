# Amazon Q Developer Pro subscription billing

Billing information for the Pro tier varies depending on whether you're an end-user with a
personal account (Builder ID), or you're an administrator of IAM Identity Center workforce users.

## Personal account (Builder ID) users

If you subscribed to the Pro tier with a personal account (Builder ID), you will be billed
monthly. The AWS account that is linked to your Builder ID gets the bill.

The very first month you are subscribed, you are charged a prorated fee. For example, if you
subscribe April 15th, you'll be charged half the subscription fee. After that, you'll be
charged the full amount.

If you unsubscribe, billing stops at the end of the billing cycle. For more information, see
[Unsubscribing from Amazon Q Developer Pro](q-admin-setup-unsubscribe.md "q-admin-setup-unsubscribe.md").

## IAM Identity Center workforce users

If you're an administrator who has subscribed a set of IAM Identity Center workforce users to the Pro
tier, you will be billed monthly for each user that you subscribe. For more information, see
[Amazon Q Developer pricing](https://aws.amazon.com/q/developer/pricing "https://aws.amazon.com/q/developer/pricing").

If your business has [AWS Organizations](../../../organizations/latest/userguide/orgs_introduction.md "../../../organizations/latest/userguide/orgs_introduction.md") set up,
billing for Amazon Q Developer Pro usage is per AWS organization. The management account gets the
bill. If the same user is subscribed to Amazon Q Developer in multiple accounts within the same
organization, you will not be double-billed.

If you don't have AWS Organizations set up, the AWS account under which your users are subscribed
gets the bill.

You can view your bill in the Billing and Cost Management console. The Amazon Q expenses are listed on the
**Charges by service** tab, under **Q**. For more
information about the Billing and Cost Management console, see [What is AWS Billing and Cost Management?](../../../awsaccountbilling/latest/aboutv2/billing-what-is.md "../../../awsaccountbilling/latest/aboutv2/billing-what-is.md") in
the _AWS Billing User Guide_.

You can identify the cost of Amazon Q subscriptions for specific users with resource IDs through
AWS Billing and Cost Management. To do so, in the Billing and Cost Management console under [Data Exports](https://console.aws.amazon.com/costmanagement/home#/bcm-data-exports "https://console.aws.amazon.com/costmanagement/home#/bcm-data-exports"), create either a standard
data export or a legacy CUR export with the **Include resource IDs** option
selected. To learn more, refer to [Creating data exports](../../../cur/latest/userguide/dataexports-create.md "../../../cur/latest/userguide/dataexports-create.md") in the _AWS Data Exports User Guide_.

If you unsubscribe users, billing stops at the end of the billing cycle. For more
information, see [Unsubscribing from Amazon Q Developer Pro](q-admin-setup-unsubscribe.md "q-admin-setup-unsubscribe.md").
