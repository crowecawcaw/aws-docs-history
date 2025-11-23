# Customizing your Billing preferences

You can use the **AWS Billing preferences** page to manage your invoice
delivery, alerts, credit sharing, Reserved Instances (RI) and Savings Plans discount sharing, and
detailed billing (legacy) reports. For some sections, only the payer account can update
them. If you use billing transfer, the preferences set up in the bill transfer account apply to all AWS Organizations that transfer their bills.

You can assign user permissions to view the **Billing
preferences** page. For more information, see [Using fine-grained AWS Billing actions](migrate-granularaccess-whatis.md#migrate-user-permissions "migrate-granularaccess-whatis.md#migrate-user-permissions").

The Billing preferences page contains the following sections.

###### Contents

- [Invoice delivery preferences](billing-pref.md#invoice-delivery-preferences "billing-pref.md#invoice-delivery-preferences")
  - [Additional invoice email](billing-pref.md#additional-invoice-emails "billing-pref.md#additional-invoice-emails")

- [Alert preferences](billing-pref.md#alert-preferences "billing-pref.md#alert-preferences")
- [Procurement portal settings](billing-pref.md#procurement-portal "billing-pref.md#procurement-portal")
  - [Next steps](billing-pref.md#procurement-portal-next "billing-pref.md#procurement-portal-next")

- [Credit sharing preferences](billing-pref.md#credit-sharing-preferences "billing-pref.md#credit-sharing-preferences")
- [Savings Plans and Reserved Instances
  discount sharing preferences](billing-pref.md#reserved-instances-savings-plans-preferences "billing-pref.md#reserved-instances-savings-plans-preferences")
  - [Understanding Sharing Options](billing-pref.md#understanding-sharing-options "billing-pref.md#understanding-sharing-options")
  - [Managing Basic Discount Sharing](billing-pref.md#managing-basic-discount-sharing "billing-pref.md#managing-basic-discount-sharing")
  - [Setting Up Group Sharing](billing-pref.md#setting-up-group-sharing "billing-pref.md#setting-up-group-sharing")
  - [Modifying Existing Groups](billing-pref.md#modifying-existing-groups "billing-pref.md#modifying-existing-groups")

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

## Procurement portal settings

Using AWS e-invoice delivery, customer using SAP Business Network and Coupa portals can automatically retrieve purchase orders (PO) from SAP Business Network and Coupa portals. This allows for accurate POs associated with delivered invoices. AWS e-invoice is an optional, opt-in billing feature that automatically sends your AWS invoices to your procurement portal on the same day it is generated. This feature integrates with SAP Business Network and Coupa procurement portals.

###### Benefits

**Eliminates manual tasks for customers**

You can automate receiving AWS invoices, matching them with purchase orders, and uploading them to your procurement portal. This eliminates the need for manual processing.

**Same-day invoice delivery**

Receive AWS invoices in your procurement portal on the same day it is generated.

**Reduced processing errors**

By automating the invoice delivery process, you can reduce errors that can occur with manual processing.

**Enhanced visibility**

Track and monitor all invoice activities—including delivery status and approvals—directly in your procurement portal.

**PDF invoice support**

Access both PDF invoices and electronic invoices in your procurement portal.

###### Supported platforms

The following platforms integrates with the AWS e-invoice delivery feature.

- SAP Business Network
- Coupa

###### To receive AWS e-invoices

1. Open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Billing
   preferences**.
3. In the **Procurement portal settings** section under **Portal connections**, choose **Add connection**.
4. On the **Request activating features** page, choose
   **E-invoice delivery** and choose
   **Next**.
5. In the **Choose procurement portal** section, choose your procurement portal.
6. Enter the procurement portal connection details and choose **Next**.
7. Complete the e-invoice delivery preferences and choose **Next**.
8. Choose a testing option:
   - **Production environment**: Live invoice delivery to your procurement system. You can manually test by verifying text invoices and purchase orders in your portal or console.
   - **Testing environment**: Tests all features using a separate testing environment. This validates invoice delivery without affecting live transactions.

9. Enter your preferred contact name and email address. This information is used to set up your procurement portal and contact you during testing and support.
10. Select the checkbox to agree with AWS contacting you for setup.
11. Choose **Next**.
12. Review the information and choose **Submit**.

### Next steps

1. AWS contacts you within 24 hours to verify your account.
2. After verification is complete, we establish the connection to your procurement portal and begin testing.
3. After testing is successful, we enable your account for AWS e-invoice delivery.

## Credit sharing preferences

You can use this section to activate sharing credits across member accounts in your
billing family. You can select specific accounts or enable sharing for all accounts.

###### Note

- This section is only available for the management account (payer account) as part
  of AWS Organizations.
- If you use billing transfer, the bill source account (not the bill transfer account) controls the credit sharing preferences.

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

###### Important

Changing the sharing preferences of Reserved Instances and Savings Plans in your AWS organization, will impact your AWS bills. This also applies to customers opted in Billing Conductor or billing transfer.

## Savings Plans and Reserved Instances

discount sharing preferences

Reserved Instances (RI) and (SP) discount sharing allows you to control how commitment-based discounts
are distributed across accounts in your AWS Organizations. This feature helps you align cost savings with your
organizational structure and business requirements.

###### Note

This section is only available for the management account (payer account) in AWS Organizations.

If you use billing transfer, the management account (not the bill transfer account) controls the credit sharing preferences.

### Understanding Sharing Options

You can choose from three sharing preference options:

| Sharing Type              | Description                                                                                                                                       | Use Case                                                         |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| Open sharing              | Discounts are available to all sharing-activated accounts within the organization (default)                                                       | Cost optimization across your entire organization                |
| Prioritized group sharing | Discounts apply to the purchasing account first, then within defined groups, then to remaining sharing-activated accounts within the organization | Balance between group control and organization-wide optimization |
| Restricted group sharing  | Discounts are exclusively shared within defined groups only                                                                                       | Strict cost allocation by business unit or department            |

### Managing Basic Discount Sharing

###### To activate or deactivate discount sharing for accounts:

1. Open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Billing preferences**
3. In the **Reserved Instances and Savings Plans discount sharing preference** section, choose **Edit**
4. Select accounts from the table and choose **Activate** or **Deactivate**
5. Choose **Update**

###### Tip

- **Default sharing for newly created member accounts**: Automatically activates sharing for new accounts joining your organization
- **Download preference history (CSV)**: Export a history of your sharing preference changes

### Setting Up Group Sharing

Group sharing requires creating Cost Categories to define your sharing groups.

###### Step 1: Configure sharing preferences

1. Open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Billing preferences**
3. In the **Reserved Instances and Savings Plans discount sharing preferences** section, choose **Edit**
4. Select either:
   - **Prioritized group sharing** (first within groups, then beyond)
   - **Restricted group sharing** (only within groups)

###### Step 2: Create Cost Categories for sharing groups

1. Under **Cost Category**, select an existing category or click **Create Cost Categories**
2. If creating a new Cost Category:
   1. Enter a **Cost category name** (e.g., "Business Units", "Geographic Regions")
   2. For each sharing group, add a rule:
      1. Select the **Linked accounts** for this group
      2. Enter a **SP/RI group sharing name** (e.g., "Research and Development", "EMEA Operations") in the **Then group costs together as field**
      3. Click **Create Rule**

   3. Use **Add new rule** for additional groups
   4. Click **Next** through the remaining steps without making changes
   5. Click **Create cost category**

3. Return to **Billing preferences** and select your Cost Category
4. Review the impact warning and choose **Proceed**
5. Select your implementation preference:
   - **Create estimate and update later**: Simulate impact before applying
   - **Update and create estimate later**: Apply changes immediately

6. Choose **Update**

###### Important Considerations

###### Group Configuration Rules

- Each account can belong to only one sharing group
- The management account cannot belong to any sharing group
- Groups must be mutually exclusive with no overlapping accounts

###### Billing Impact

- **Optimization trade-off**: Group sharing may reduce overall discount optimization as it prioritizes group allocation over maximum savings
- **Timing**: You can change your preference at any time. Each estimated bill is computed by using the last set of preferences. The final bill for the month is calculated based on the preferences set at 23:59:59 UTC time on the last day of the month.
- **Savings Plans requirement**: The Savings Plans owner account must be active in discount sharing preferences

###### Best Practices

- Use the Pricing Calculator integration to simulate billing impact before implementation
- Start with open sharing to maximize savings, then move to group sharing if organizational requirements demand it
- Regularly review and adjust groups as your organization evolves

### Modifying Existing Groups

1. Open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Cost Categories**.
3. Click on the Cost Category you want to modify
4. Click **Edit**
5. Update group membership or create new groups following the same process above

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
- If you use billing transfer, the detailed billing report (legacy) isn't available for AWS Organizations that transfer their bills or for the bill transfer account.
- If you use billing transfer, the detailed billing report (legacy) isn't available for AWS Organizations that transfer their bills or for the bill transfer account.

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
