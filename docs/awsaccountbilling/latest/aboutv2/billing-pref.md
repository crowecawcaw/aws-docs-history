

# Customizing your Billing preferences

Use the **AWS Billing preferences** page to manage invoice delivery, alerts, procurement portal settings, credit sharing, Reserved Instances (RI) and Savings Plans discount sharing, and detailed billing reports (legacy). Some sections can be updated only by the payer account. If you use billing transfer, the preferences set in the bill transfer account apply to all organizations that transfer their bills to it.

You can assign user permissions to view the **Billing preferences** page. For more information, see [Using fine-grained AWS Billing actions](migrate-granularaccess-whatis.md#migrate-user-permissions).

The Billing preferences page contains the following sections.

**Contents**
+ [Invoice delivery preferences](#invoice-delivery-preferences)
  + [Additional invoice email](#additional-invoice-emails)
+ [Alert preferences](#alert-preferences)
+ [Procurement portal settings](#procurement-portal)
  + [Next steps](#procurement-portal-next)
+ [Credit sharing preferences](#credit-sharing-preferences)
+ [Savings Plans and Reserved Instances discount sharing preferences](#reserved-instances-savings-plans-preferences)
+ [Detailed billing reports (legacy)](#detailed-reports-legacy-preferences)

## Invoice delivery preferences
<a name="invoice-delivery-preferences"></a>

You can choose to receive a PDF copy of your monthly invoice by email. The monthly invoices are sent to the emails registered as the AWS account root user and the alternate billing contact. For information about updating these email addresses, see [Setting up your tax information](manage-account-payment.md).

**To opt in or out of receiving monthly PDF invoices by email**

1. Open the AWS Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, choose **Billing preferences**.

1. In the **Invoice delivery preferences** section, choose **Edit**.

1. Select or clear **PDF invoices delivery by email**.

1. Choose **Update**.

Depending on the purchase, AWS sends monthly or daily invoices to the following contacts: 
+ The AWS account root user
+ The billing contacts on the **Payment preferences** page
+ The alternate billing contacts on the **Account** page

### Additional invoice email
<a name="additional-invoice-emails"></a>

In addition to the PDF invoice email, AWS sends monthly or daily email with your invoice details to the [contact list](#billing-contacts-invoices) in the previous section.

**Note**  
If you specify a billing contact on the **Payment preferences** page, the root user won't receive the PDF invoice or the additional invoice by email.

## Alert preferences
<a name="alert-preferences"></a>

You can receive email alerts when your AWS service usage is approaching or has exceeded the AWS Free Tier usage limits. 

**To opt in or out of receiving AWS Free Tier usage alerts**

1. Open the AWS Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, choose **Billing preferences**.

1. In the **Alert preferences** section, choose **Edit**.

1. Select or clear **Receive AWS Free Tier usage alerts**.

1. (Optional) In the **Additional email address to receive alerts**, enter any email addresses that aren't already registered as a root user or alternate billing contact.

1. Choose **Update**.

You can also use Amazon CloudWatch billing alerts to receive email notifications when your charges reach a specified threshold.

**To receive CloudWatch billing alerts**

1. Open the AWS Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, choose **Billing preferences**.

1. In the **Alert preferences** section, choose **Edit**.

1. Select **Receive CloudWatch billing alerts**.
**Important**  
This preference can't be deactivated at a later time.

1. Choose **Update**.

To manage your CloudWatch billing alerts, see your [CloudWatch dashboard](https://console.aws.amazon.com/cloudwatch) or view your [AWS Budgets](https://console.aws.amazon.com/budgets). For more information, see the [Create a billing alarm to monitor your estimated AWS charges](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.html) in the *Amazon CloudWatch User Guide*.

## Procurement portal settings
<a name="procurement-portal"></a>

Using AWS e-invoice delivery, customer using SAP Business Network and Coupa portals can automatically retrieve purchase orders (PO) from SAP Business Network and Coupa portals. This allows for accurate POs associated with delivered invoices. AWS e-invoice is an optional, opt-in billing feature that automatically sends your AWS invoices to your procurement portal on the same day it is generated. This feature integrates with SAP Business Network and Coupa procurement portals.Benefits

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

**Supported platforms**

The following platforms integrates with the AWS e-invoice delivery feature.
+ SAP Business Network
+ Coupa

**To receive AWS e-invoices**

1. Open the AWS Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, choose **Billing preferences**.

1. In the **Procurement portal settings** section under **Portal connections**, choose **Add connection**.

1. On the **Request activating features** page, choose **E-invoice delivery** and choose **Next**.

1. In the **Choose procurement portal** section, choose your procurement portal.

1. Enter the procurement portal connection details and choose **Next**.

1. Complete the e-invoice delivery preferences and choose **Next**.

1. Choose a testing option:
   + **Production environment**: Live invoice delivery to your procurement system. You can manually test by verifying text invoices and purchase orders in your portal or console.
   + **Testing environment**: Tests all features using a separate testing environment. This validates invoice delivery without affecting live transactions.

1. Enter your preferred contact name and email address. This information is used to set up your procurement portal and contact you during testing and support.

1. Select the checkbox to agree with AWS contacting you for setup.

1. Choose **Next**.

1. Review the information and choose **Submit**.

### Next steps
<a name="procurement-portal-next"></a>

1. AWS contacts you within 24 hours to verify your account.

1. After verification is complete, we establish the connection to your procurement portal and begin testing.

1. After testing is successful, we enable your account for AWS e-invoice delivery.

## Credit sharing preferences
<a name="credit-sharing-preferences"></a>

Use the **Credit sharing preferences** section to activate credit sharing for accounts and to choose a group sharing mode for credits. For how credit sharing works, including credit-level sharing preferences, see [Step 4: Sharing AWS credits](useconsolidatedbilling-credits.md#credit-sharing).<a name="credit-group-sharing"></a>

**To set up group sharing for credits**

1. Open the AWS Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, choose **Billing preferences**.

1. In the **Credit sharing preferences** section, choose **Edit**.

1. Choose **Prioritized sharing group** or **Restricted sharing group**.

1. For **Cost category**, select a Cost Category with the Benefit group sharing association, or choose **Create cost category**. If you don't see a Cost Category that you just created, choose the refresh button.

1. Review the impact warning, and then save your preference.

## Savings Plans and Reserved Instances discount sharing preferences
<a name="reserved-instances-savings-plans-preferences"></a>

Use the **Reserved Instances and Savings Plans discount sharing preference** section to activate discount sharing for accounts and to choose a group sharing mode. For sharing modes, level sharing and the steps to set them up, see [Reserved Instances and Savings Plans discount sharing](ri-turn-off.md).

## Detailed billing reports (legacy)
<a name="detailed-reports-legacy-preferences"></a>

You can receive legacy billing reports that are offered outside of the AWS Cost and Usage Reports console page. However, we strongly recommend that you use AWS Cost and Usage Reports instead because it provides the most comprehensive billing information. Also, these legacy reporting methods will not be supported at a later date. 

For more information about detailed billing reports, see [Detailed Billing Reports](https://docs.aws.amazon.com/cur/latest/userguide/detailed-billing.html) in the *AWS Cost and Usage Reports User Guide*. 

For more information about transferring your reports to AWS Cost and Usage Reports, see [Migrating from Detailed Billing Reports to AWS Cost and Usage Reports](https://docs.aws.amazon.com/cur/latest/userguide/detailed-billing-migrate.html).

**Notes**  
This section is only visible if you use AWS Organizations.
To download a CSV from the **Bills** page, first activate monthly reports.
If you use billing transfer, the detailed billing report (legacy) isn't available for AWS Organizations that transfer their bills or for the bill transfer account.
If you use billing transfer, the detailed billing report (legacy) isn't available for AWS Organizations that transfer their bills or for the bill transfer account.

**To edit your detailed billing reports (legacy) settings**

1. Open the AWS Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, choose **Billing preferences**.

1. In the **Detailed billing reports (legacy)** section, choose **Edit**.

1. To set the Amazon S3 bucket for report delivery, select **Legacy report delivery to Amazon S3** and **Configure**.

1. In the **Configure Amazon S3 Bucket** section, select an existing Amazon S3 bucket to receive the AWS Cost and Usage Reports, or create a new bucket.

1. Choose **Update**.

1. To configure the granularity of the reports to show your AWS usage, select the reports to activate.

1. In the **Report activation** section, choose **Activate**.