# Customizing your Billing preferences

You can use the **AWS Billing preferences** page to manage your invoice
delivery, alerts, credit sharing, Reserved Instances (RI) and Savings Plans discount sharing, and
detailed billing (legacy) reports. For some sections, only the payer account can update
them.

You can assign user permissions to view the **Billing
preferences** page. For more information, see [Using fine-grained AWS Billing actions](migrate-granularaccess-whatis.md#migrate-user-permissions "migrate-granularaccess-whatis.md#migrate-user-permissions").

The Billing preferences page contains the following sections.

###### Contents

- [Invoice delivery preferences](billing-pref.md#invoice-delivery-preferences "billing-pref.md#invoice-delivery-preferences")
  - [Additional invoice email](billing-pref.md#additional-invoice-emails "billing-pref.md#additional-invoice-emails")

- [Alert preferences](billing-pref.md#alert-preferences "billing-pref.md#alert-preferences")
- [Credit sharing preferences](billing-pref.md#credit-sharing-preferences "billing-pref.md#credit-sharing-preferences")
- [Reserved Instances and
  Savings Plans discount sharing preferences](billing-pref.md#reserved-instances-savings-plans-preferences "billing-pref.md#reserved-instances-savings-plans-preferences")
- [Detailed billing reports
  (legacy)](billing-pref.md#detailed-reports-legacy-preferences "billing-pref.md#detailed-reports-legacy-preferences")

## Invoice delivery preferences

You can choose to receive a PDF copy of your monthly invoice by email. The monthly
invoices are sent to the emails registered as the AWS account root user and the alternate billing
contact. For information about updating these email addresses, see [Setting up your tax information](manage-account-payment.md "manage-account-payment.md").

###### To opt in or out of receiving monthly PDF invoices by

email

1. Open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Billing
   preferences**.
3. In the **Invoice delivery preferences** section, choose
   **Edit**.
4. Select or clear **PDF invoices delivery by email**.
5. Choose **Update**.

Depending on the purchase, AWS sends monthly
or daily invoices to the following contacts:

- The AWS account root user
- The billing contacts on the **Payment preferences**
  page
- The alternate billing contacts on the **Account** page

### Additional invoice email

In addition to the PDF invoice email, AWS sends monthly or daily email with your
invoice details to the [contact list](#billing-contacts-invoices "#billing-contacts-invoices")
in the previous section.

###### Note

If you specify a billing contact on the **Payment preferences**
page, the root user won't receive the PDF invoice or the additional invoice by
email.

## Alert preferences

You can receive email alerts when your AWS service usage is approaching or has
exceeded the AWS Free Tier usage limits.

###### To opt in or out of receiving AWS Free Tier usage alerts

1. Open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Billing
   preferences**.
3. In the **Alert preferences** section, choose
   **Edit**.
4. Select or clear **Receive AWS Free Tier usage alerts**.
5. (Optional) In the **Additional email address to receive
   alerts**, enter any email addresses that aren't already registered
   as a root user or alternate billing contact.
6. Choose **Update**.

You can also use Amazon CloudWatch billing alerts to receive email notifications when your
charges reach a specified threshold.

###### To receive CloudWatch billing alerts

1. Open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Billing
   preferences**.
3. In the **Alert preferences** section, choose
   **Edit**.
4. Select **Receive CloudWatch billing alerts**.

###### Important

This preference can't be deactivated at a later time. 5. Choose **Update**.

To manage your CloudWatch billing alerts, see your [CloudWatch dashboard](https://console.aws.amazon.com/cloudwatch "https://console.aws.amazon.com/cloudwatch") or view your [AWS Budgets](https://console.aws.amazon.com/budgets "https://console.aws.amazon.com/budgets"). For more information, see the [Create a billing alarm to monitor your estimated AWS charges](../../../AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.md "../../../AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.md") in the
_Amazon CloudWatch User Guide_.

## Credit sharing preferences

You can use this section to activate sharing credits across member accounts in your
billing family. You can select specific accounts or enable sharing for all accounts.

###### Note

This section is only available for the management account (payer account) as part
of AWS Organizations.

###### To manage credit sharing for member accounts

1. Open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Billing
   preferences**.
3. In the **Credit sharing preferences** section, choose
   **Edit**.
4. To activate or deactivate credit sharing for specific accounts, select them
   from the table and, then choose **Activate** or
   **Deactivate**.
5. To activate or deactivate credit sharing for all accounts, choose
   **Actions**, and then choose **Activate
   All** or **Deactivate All**.
6. Choose **Update**.

###### Tip

- To activate credit sharing for new accounts that join your organization,
  select **Default sharing for newly created member
  accounts**.
- To download a history of your credit sharing preferences, choose
  **Download preference history (CSV)**.

For more information about AWS credits, see [Applying AWS credits](useconsolidatedbilling-credits.md "useconsolidatedbilling-credits.md").

## Reserved Instances and

Savings Plans discount sharing preferences

You can use this section to activate sharing Reserved Instances and Savings Plan
discounts across accounts in your billing family. You can select specific accounts or
enable sharing for all accounts.

To share the Savings Plans discount, the Savings Plans owner account must be active in the RI and Savings Plans discount sharing preferences. This enables the discount usage across other eligible linked accounts in the organization.

###### Note

This section is only available for the management account (payer account) as part
of AWS Organizations.

###### To manage Reserved Instances and Savings Plans discount sharing for member

accounts

1. Open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Billing
   preferences**.
3. In the **Reserved Instances and Savings Plans discount sharing
   preference** section, choose **Edit**.
4. To activate or deactivate discount sharing for specific accounts, select them
   from the table, and then choose **Activate** or
   **Deactivate**.
5. To activate or deactivate discount sharing for all accounts, choose
   **Actions**, and then choose **Activate
   All** or **Deactivate All**.
6. Choose **Update**.

###### Tip

- To activate credit sharing for new accounts that join your organization,
  select **Default sharing for newly created member
  accounts**.
- To download a history of your credit sharing preferences, choose
  **Download preference history (CSV)**.

## Detailed billing reports

(legacy)

You can receive legacy billing reports that are offered outside of the AWS Cost and Usage Reports
console page. However, we strongly recommend that you use AWS Cost and Usage Reports instead because it
provides the most comprehensive billing information. Also, these legacy reporting
methods will not be supported at a later date.

For more information about detailed billing reports, see [Detailed Billing Reports](../../../cur/latest/userguide/detailed-billing.md "../../../cur/latest/userguide/detailed-billing.md") in
the _AWS Cost and Usage Reports User Guide_.

For more information about transferring your reports to AWS Cost and Usage Reports, see [Migrating from Detailed Billing Reports to AWS Cost and Usage Reports](../../../cur/latest/userguide/detailed-billing-migrate.md "../../../cur/latest/userguide/detailed-billing-migrate.md").

###### Notes

- This section is only visible if you use AWS Organizations.
- To download a CSV from the **Bills** page, first activate
  monthly reports.

###### To edit your detailed billing reports (legacy) settings

1. Open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Billing
   preferences**.
3. In the **Detailed billing reports (legacy)** section, choose
   **Edit**.
4. To set the Amazon S3 bucket for report delivery, select **Legacy report
   delivery to Amazon S3** and **Configure**.
5. In the **Configure Amazon S3 Bucket** section, select an existing
   Amazon S3 bucket to receive the AWS Cost and Usage Reports, or create a new bucket.
6. Choose **Update**.
7. To configure the granularity of the reports to show your AWS usage, select
   the reports to activate.
8. In the **Report activation** section, choose
   **Activate**.
