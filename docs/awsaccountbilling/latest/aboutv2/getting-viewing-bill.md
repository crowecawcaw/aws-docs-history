# Understanding your bill

|                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **_For questions about your AWS bills or to appeal your charges, contact Support to address your inquiries immediately. To get help, see [Getting help with your bills and payments](billing-get-answers.md "billing-get-answers.md"). To understand your bills page contents, see [Using the Bills page to understand your monthly charges and<br>invoice](#invoice "#invoice")._** |

You receive AWS invoices monthly for usage charges and recurring fees. For one-time
fees, such as fees for purchasing an All Upfront Reserved Instance, you're charged
immediately.

At any time, you can view estimated charges for the current month and final charges for
previous months. This topic describes how to view your monthly bill and past bills, how to
receive and read billing reports, and how to download invoices. To make a payment, see [Making payments](manage-making-a-payment.md "manage-making-a-payment.md").

###### Topics

- [Viewing your monthly charges](#accessing-your-monthly-charges "#accessing-your-monthly-charges")
- [Using the Bills page to understand your monthly charges and
  invoice](#invoice "#invoice")
- [Downloading a PDF of your invoice](#downloading-pdf-invoices "#downloading-pdf-invoices")
- [Downloading a monthly report](#download-monthy-report "#download-monthy-report")
- [Viewing and correcting your AWS invoices](#view-invoices "#view-invoices")
- [Understanding unexpected charges](checklistforunwantedcharges.md "checklistforunwantedcharges.md")

## Viewing your monthly charges

Follow this procedure to view your monthly charges from the Billing and Cost Management console.

###### To view your monthly charges

1. Sign in to the AWS Management Console and open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Bills**.
3. Choose a **Billing period** (for example, August
   2023).
4. View your AWS bill summary.

###### To view your monthly charges

1. Sign in to the AWS Management Console and open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose [Bills](https://console.aws.amazon.com/billing/home#/bill "https://console.aws.amazon.com/billing/home#/bill").
3. For **Billing period**, choose a month.

The **Summary** section displays a summary and
details of your charges for that month.

###### Note

The summary isn't an invoice until the month's activity closes and
AWS calculates the final charges.

If you use the consolidated billing feature in AWS Organizations, the
**Bills** page lists totals for all accounts on the
**Charges by account** tab. Choose the account ID
to see the activity for each account in the organization. For more
information about consolidated billing, see [Consolidating billing for AWS Organizations](consolidated-billing.md "consolidated-billing.md").

## Using the Bills page to understand your monthly charges and

invoice

At the end of a monthly billing period, or when you incur a one-time fee, AWS issues
an invoice as a PDF file. If you're paying by credit card, AWS also charges the credit
card that you have on file at this time.

To download invoices and view your monthly charge details, you can use the
**Bills** page in the AWS Billing and Cost Management console.

###### Note

IAM users need explicit permission to access some of the pages in the Billing and Cost Management
console. For more information, see [Overview of managing access permissions](control-access-billing.md "control-access-billing.md").

**Bills page**

You can use the **Bills** page to see your monthly
chargeable costs, along with details of your AWS services and purchases
made through AWS Marketplace. Invoices are generated when a monthly billing period
closes (the billing status appears as **Issued**), or when
subscriptions or one-time purchases are made. For monthly billing periods
that haven't closed (the billing status appears as
**Pending**), this page shows the most recent estimated
charges based on your AWS services metered to date.

If you're signed in as the management account of your AWS Organizations, you can see
the consolidated charges for your member accounts. You can use the
**Charges by account** to also view account-level
details.

Say you're an AWS Billing Conductor user and are
signed in as a management account. You can turn on a [pro
forma](../../../billingconductor/latest/userguide/understanding-abc.md "../../../billingconductor/latest/userguide/understanding-abc.md") view by choosing the gear icon on the top of the page.
Choose the month and year to specify your billing period.

To customize the visible sections, choose the gear icon at the top of the
page. These preferences are saved for ongoing visits to the
**Bills** page.

**AWS bill summary**

The **AWS bill summary** section shows an overview of
your monthly charges. The information shows your invoice totals for the
closed billing periods (the billing status appears as
**Issued**).

Billing periods that haven't closed have the
**Pending** billing status. The totals show the most
recent estimated charges based on your AWS services metered to date.
Totals are shown in US dollars (USD). If your invoices are issued in another
currency, the total in the other currency is also shown.

**Payment information**

The **Payment information**
section lists invoices for the selected billing period that AWS received
payments for. You can find the service provider, charge types, document
types, invoice IDs, payment status, the date AWS received the payments,
and the total amount in USD. If your invoices are issued in another
currency, the total in the other currency is also shown. For more
information, see [Managing Your Payments](manage-payments.md "manage-payments.md").

**Highest cost by service provider**

The **Highest cost by service provider** section
identifies your account's service and AWS Region with the highest cost for
the billing period, and shows the month-over-month trends for each. For
pending billing periods, the month-over-month trend compares the
month-to-date spend in the current billing period with the equivalent
portion of the previous billing period.

**Charges by service**

The **Charges by service** tab
shows your spend in each AWS service. You can sort by service name or
amount in USD, and filter by service name and Region. Choose the
`+` icon next to each service to see the charges for that
service by **Region**. Choose a **Region**
to see charge details.

**Charges by account**

If you use AWS Organizations and signed in to your
management account, the **Charges by account** tab shows the
spend of each of your member accounts. You can sort by account ID, account
name, or amount in USD, and filter by account ID or account name. Choose the
`+` icon next to each account to see charges for that account
by service provider. Choose the `+` icon next to each line item
to see charges by service and Region. Choose a **Region**
to see charge details.

**Invoices**

The **Invoices** tab lists the
invoices for each service provider that you transacted with during the
selected billing period. This includes details such as charge type, invoice
date, and total in USD. If your invoices are issued in another currency, the
total in the other currency is also shown. To view and download a PDF format
for individual invoices, choose the **Invoice ID**.

**Savings**

The **Savings** tab summarizes
your savings during the billing period as the outcome of Savings Plans, credits, or
other discount programs. These savings are also reflected in the
**Charges by service**, **Charges by
account**, and **Invoices** tabs. Choose each
savings type to see the details by service.

**Taxes by service**

The **Taxes by service** tab
shows the pre-tax, tax, and post-tax charges for each service that was
charged taxes. You can sort by service name, post-tax charge, pre-tax
charge, or tax in USD, and filter by service name.

**Tax Invoices and Supplemental Documents**

The **Tax Invoices and Supplemental
Documents** section lists tax invoices and other supplemental
documents for the selected billing period. Not all service providers issue
tax invoices. The **Invoice ID** column shows the
associated commercial invoice associated with that tax invoice. To view and
download a PDF format for individual invoices, choose the **Document
ID**.

## Downloading a PDF of your invoice

Follow this procedure to download a PDF of your monthly invoice.

###### To download a copy of your charges as a PDF document

1. Open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. On the **Bills** page, select a month for the
   **Billing period**.
3. Under the **AWS bill summary** section, confirm that the
   **Bill status** appears as
   **Issued**.
4. Choose the **Invoices** tab.
5. Choose the **Invoice ID** of the document that you want to
   download.
6. (For service providers other than AWS EMEA SARL) To download a copy of a
   particular tax invoice, in the **Tax Invoices and Supplemental
   Documents** section, choose the **Document
   ID**.
7. (For AWS EMEA SARL) To download a copy of a particular tax invoice, in the
   **AWS EMEA SARL charges** section, choose the
   **Document ID**.

###### To download a copy of your charges as a PDF document

1. Open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. On the **Bills** page, select a month from the
   **Date** list that all activity is closed
   for.
3. Under **Total**, choose **Amazon Web
   Services, Inc. - Service Charges**.
4. Choose **Invoice <invoiceID>**.
5. (For entities other than AWS EMEA SARL) To download a copy of a
   particular tax invoice, choose the **Invoice
   <invoiceID>** in the **Tax
   Invoices** section.
6. (For AWS EMEA SARL) To download a copy of a particular tax invoice,
   choose the **Invoice <invoiceID>** in the
   **Amazon Web Services EMEA SARL – Service Charges**
   section.

## Downloading a monthly report

You can download CSV files for any future billing _after_ you turn
on monthly reports. This feature delivers your reports to an Amazon S3 bucket.

###### Note

Starting November 1, 2025, the **Download all to CSV** button will no longer be available on the **Bills** page. If you previously configured delivery of the eCSV report, you can get this report from the Amazon S3 bucket that you specified during configuration. To configure additional reports, visit the [**Data Exports**](https://console.aws.amazon.com/costmanagement/home#/bcm-data-exports "https://console.aws.amazon.com/costmanagement/home#/bcm-data-exports") console page.

###### To download CSV files for a monthly report

1. Open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. On the navigation pane, choose **Billing
   preferences**.
3. Under **Detailed billing reports (legacy)**, choose
   **Edit**, and then select **Legacy report delivery
   to S3**.
4. Choose **Configure an S3 bucket to activate** to specify
   where your reports are delivered.
5. In the **Configure S3 Bucket** dialog box, choose one of the
   following options:
   - To use an existing S3 bucket, choose **Use an existing S3
     bucket**, and then select the S3 bucket.
   - To create a new S3 bucket, choose **Create a new S3
     bucket**, and then for **S3 bucket name**,
     enter the name, and then choose the **Region**.

6. Choose **Next**.
7. Verify the default IAM policy and then select **I have confirmed
   that this policy is correct**.
8. Choose **Save**.
9. On the **Bills** page, choose **Download all to
   CSV**.

## Viewing and correcting your AWS invoices

You can view your AWS invoices in the Billing and Cost Management console. You can also correct invoice information such as business name, business address, and purchase order on your AWS invoice.

###### To view your AWS invoices

1. Open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. On the navigation pane, choose **Bills**.
3. On the **Bills** page for **Billing period**, choose the period to view your AWS bill summary.
4. Choose the **Invoices** tab.

From here, you can view a list of AWS invoices for the chosen billing period. 5. (Optional) To download the invoice and review details, choose the vertical ellipsis icon (
![3 vertical ellipsis on the Billing and Cost Management console.](images/vertical-ellipsis.png)
) next to the invoice and choose **Download invoice**.

###### To correct your AWS invoices

1. Open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. On the navigation pane, choose **Bills**.
3. On the **Bills** page for **Billing period**, choose the period to view your AWS bill summary.
4. Choose the **Invoices** tab.
5. Choose the vertical ellipsis icon (
   ![3 vertical ellipsis on the Billing and Cost Management console.](images/vertical-ellipsis.png)
   ) next to the invoice that you want to edit.
6. Do one of the following:
   - Choose **Update company and address for account**.
     1. Update the information for your company name or address.

   - Choose **Update purchase order**.
     1. Select an existing purchase order to associate with the invoice.
     2. (Optional) You can choose to create a new purchase order at this time to associate with the invoice.

7. Choose **Update and reprocess** to refresh the invoice.
8. To check the status of your invoice update, see the **Update status** column in the **Invoices** tab.

###### Note

To change other invoice attributes, contact Support. For more information, see [Contacting Support](billing-get-answers.md#billing-support "billing-get-answers.md#billing-support").
