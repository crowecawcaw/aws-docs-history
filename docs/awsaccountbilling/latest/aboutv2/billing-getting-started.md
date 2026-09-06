

# Getting set up with Billing
<a name="billing-getting-started"></a>

Use this section to get started with the AWS Billing and Cost Management console. Prerequisites include signing up for AWS, setting up IAM users, and reviewing your AWS bills.

**Topics**
+ [Sign up for an AWS account](#sign-up-for-aws)
+ [Learn more about Billing features](#billing-gs-features)
+ [What do I do next?](#what-next)
+ [Setting up your tax information](manage-account-payment.md)
+ [Customizing your Billing preferences](billing-pref.md)
+ [Customizing your AWS payment preferences](manage-payment-method.md)
+ [Setting up your India billing](manage-account-payment-aispl.md)
+ [Finding the seller of record](finding-the-seller-of-record.md)
+ [Reviewing your monthly billing best practices](monthly-billing-checklist.md)

## Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

## Step 1: (Prerequisite) Sign up for AWS and create an IAM user
<a name="billing-gs-review"></a>

### Activating IAM access to the AWS Billing and Cost Management console
<a name="activating-iam-access-to-billing-console"></a>

By default, IAM roles within an AWS account can't access the Billing and Cost Management console. This is true even if the IAM user or role has IAM policies that grant access to specific Billing features. The root user can allow IAM users and roles access to Billing and Cost Management console by using the **Activate IAM access** setting.

**To provide access to the Billing and Cost Management console**

1. Sign in to the **Account** page in the Billing and Cost Management console at [https://console.aws.amazon.com/billing/home?\#/account](https://console.aws.amazon.com/billing/home?#/account).

1. Under **IAM user and role access to Billing information**, choose **Edit**.

1. Select **Activate IAM access**. 

1. Choose **Update**.

For more information about this feature, see [Activating access to the Billing and Cost Management console](control-access-billing.md#ControllingAccessWebsite-Activate).

## Step 2: Review your bills and usage
<a name="step-3"></a>

Use features in the Billing and Cost Management console to view your current AWS charges and AWS usage.

**To open the Billing and Cost Management console and view your usage and charges**

1. Sign into the AWS Management Console and open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. Choose **Bills** to see details about your current charges.

1. Choose **Payments** to see your historical payment transactions.

1. Choose **AWS Cost and Usage Reports** to see reports that break down your costs.

For more information about setting up and using AWS Cost and Usage Reports, see the [AWS Cost and Usage Reports User Guide](https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html).

## Step 3: Download or print your bill
<a name="billing-gs-download"></a>

AWS Billing closes the billing period at midnight on the last day of each month and calculates your bill. Most bills are ready for you to download by the seventh accounting day of the month.

**To download or print your bill**

1. Sign into the AWS Management Console and open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/). 

1. On the navigation pane, choose **Bills**.

1. For **Date**, choose the month of the bill you want to work with.

1. Choose **Download CSV** to download a comma-separated variable file or choose **Print**.

### Adding or updating alternate contacts
<a name="manage-account-payment-alternate-contacts"></a>

Alternate contacts allows AWS to contact another person about issues with your account, even if you're unavailable. The alternate contact doesn't have to be a specific person. You could instead add an email distribution list if you have a team that manages billing, operations and security related issues. 

**Examples for alternate contacts**

AWS will reach out to each contact type in the following scenarios:
+ **Billing** – When your monthly invoice is available, or your payment method needs to be updated. If you enabled **Receive PDF Invoice By Email** in your **Billing preferences**, your alternate billing contact also receives the PDF invoices. Notifications can be from AWS service teams.
+ **Operations** – When your service is, or will be, temporarily unavailable in one of more AWS Regions. Your contacts will also receive any notification related to operations. Notifications can be from AWS service teams
+ **Security** – When you have notifications from the AWS Security, AWS Trust and Safety, or AWS service teams. These notifications might include security issues or potential abusive or fraudulent activities on your AWS account. Notifications can be from AWS service teams concerning security related topics associated with your AWS account usage. Don't include sensitive information in the subject line or full name fields since this might be used in email communications to you.

For more information about managing your alternate account contacts, see [Alternate account contacts](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-contact-alternate.html) in the *AWS Account Management* Reference Guide.

## Learn more about Billing features
<a name="billing-gs-features"></a>

Understand the features available to you in the Billing and Cost Management console.
+ **AWS Free Tier**: [Explore AWS services with AWS Free Tier](free-tier.md)
+ **Payments**: [Managing your AWS payments](manage-payments.md)
+ **Viewing your bills**: [Understanding your bill](getting-viewing-bill.md)
+ **AWS Cost Categories**: [Organizing costs using AWS Cost Categories](manage-cost-categories.md)
+ **Cost Allocation Tags**: [Organizing and tracking costs using AWS cost allocation tags](cost-alloc-tags.md)
+ **AWS Purchase Orders**: [Managing your purchase orders](manage-purchaseorders.md)
+ **AWS Cost and Usage Reports**: [Using AWS Cost and Usage Reports](https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html)
+ **Using AWS CloudTrail**: [Logging Billing and Cost Management API calls with AWS CloudTrail](logging-using-cloudtrail.md)
+ **Consolidated billing**: [Consolidating billing for AWS Organizations](consolidated-billing.md)

## What do I do next?
<a name="what-next"></a>

Now that you can view and pay your AWS bill, you're ready to use the features available to you. The rest of this guide helps you navigate your journey using the console.

### Optimize your spending using AWS Cost Management features
<a name="Billing-CMG"></a>

Use the AWS Cost Management features to budget and forecast costs so you can optimize your AWS spends and reduce your overall AWS bill. Combine and use the Billing and Cost Management console resources to manage your payments, while using AWS Cost Management features to optimize your future costs.

For more information about AWS Cost Management features, see the [AWS Cost Management User Guide](https://docs.aws.amazon.com/cost-management/latest/userguide/what-is-costmanagement.html).

### Using the Billing and Cost Management API
<a name="Billing-API"></a>

Use the [AWS Billing and Cost Management API Reference](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/Welcome.html) to programmatically use some AWS Cost Management features.

### Learn more
<a name="Billing-tutorials"></a>

You can find more information about Billing features including presentations, virtual workshops, and blog posts on the marketing page [Cloud Financial Management with AWS](https://aws.amazon.com/aws-cost-management/).

You can find virtual workshops by choosing the **Services** dropdown list and selecting your feature.

### Get help
<a name="Billing-gethelp"></a>

If you have questions about any Billing features, there are many resources available for you. To learn more, see [Getting help with your bills and payments](billing-get-answers.md).