# Creating a service-linked role for AWS Marketplace

AWS Marketplace creates the service-linked role for you when you set up integration with
AWS License Manager.

You can specify that AWS Marketplace create the service-linked role for all accounts in
your organization at once, or you can create the service-linked role for one account
at a time. The option to create service-linked roles across all accounts is only
available if your organization has **All features** enabled. For
more details, see [Enabling all features in your organization](../../../organizations/latest/userguide/orgs_manage_org_support-all-features.md "../../../organizations/latest/userguide/orgs_manage_org_support-all-features.md") in the _AWS Organizations
User Guide_.

###### To create service-linked roles across all accounts

1. In [AWS Marketplace
   console](https://console.aws.amazon.com/marketplace/ "https://console.aws.amazon.com/marketplace/"), sign in and choose
   **Settings**.
2. In the **AWS Marketplace procurement insights integration** section, select
   **View setting details**.
3. On the **Create AWS Marketplace procurement insights integration** page, select
   **Enable trusted access across your organization**,
   then choose **Create integration**.

###### Note

This setting enables trust within AWS Organizations. As a result, in addition
to the current action, future accounts that are added to the
organization have the service-linked role added automatically.

###### To create service-linked roles for the current account

1. In [AWS Marketplace
   console](https://console.aws.amazon.com/marketplace/ "https://console.aws.amazon.com/marketplace/"), sign in and choose
   **Settings**.
2. In the **AWS License Manager integration** section, select
   **View setting details**.
3. On the **Create AWS License Manager integration** page, under **Enable AWS Marketplace to manage licenses for your AWS Organizations accounts**, select
   **AWS Marketplace license management service-linked role for this account**, then choose **Create
   integration**.

###### Important

If you create the service-linked role only for the current account, you do not enable trusted access across your organization, and you must repeat
these steps for each account that wants to share (giving or receiving) licenses
in AWS Marketplace. This includes all future accounts.
