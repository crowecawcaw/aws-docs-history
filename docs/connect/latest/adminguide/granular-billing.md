

# Set up granular billing for a detailed view of your Connect Customer usage
<a name="granular-billing"></a>

By default bills for Connect Customer channels (voice calls, chat, tasks, and emails) are summarized at the AWS account level by usage type. For example:
+ Voice calls - by outbound (telephony) / inbound (telephony) / service minutes
+ Chat – by messages
+ Task - by units
+ Email - by messages

To obtain a more detailed view of your bill and usage, you can add cost allocation tags (key:value pairs) to contacts, and then use the tags to aggregate and analyze the data in the AWS Billing and Cost Management console. 
+ Connect Customer automatically adds the following system-defined tags to each contact:
  + **aws:connect:instanceId**: This represents the ID of the Connect Customerinstance. If you have multiple instances under multiple AWS accounts for each line-of-business, you can view usage bills aggregated against different instances.
  +  (**aws:connect:systemEndpoint**): This represents the your contact center number (the endpoint) that the customer reaches (inbound) or is reached from (outbound). 

    This AWS generated tag helps if you have multiple phone numbers used within your contact center. With this tag, you can group the costs associated against different phone numbers. For example, group inbound phone numbers for incoming calls, and group outbound numbers that are used for making outbound calls. 
  + **aws:connect:transferredFromEndpoint**: This represents the outbound caller ID that the call was transferred from. You can see the third-party transfer call's usage bills aggregated against the telephone numbers that the calls were transferred from. Currently, this AWS generated tag is only added to contacts for third-party external transfer calls. 
+ You can add up to 6 user-defined tags. For example, department, cost center, or business unit. Use these tags to organize your AWS bill to reflect your own cost structure.

The following image shows two user-defined tags on the **Contact details** page: CostCenter and Department. It also shows two system-defined tags: instance ID and the contact center phone number (aws:connect:systemEndpoint). 

![Contact tags on a Contact details page.](http://docs.aws.amazon.com/connect/latest/adminguide/images/granularbilling-contactdetails.png)


This topic explains how to add tags to contacts, activate the cost allocation tags, and view them in the AWS Billing dashboard. 

**Topics**
+ [Things to know about user-defined tags](#about-user-defined-tags)
+ [Step 1: Add user-defined tags to contacts](#step1-tagcontacts)
+ [Step 2: Activate cost allocation tags](#step2-activate-tags)
+ [Step 3: View cost and usage trends using cost allocation tags](#step3-view-billingapp)
+ [(Optional) Step 4: Enable Cost and Usage reports in the AWS Billing and Cost Management console](#step4-cost-and-usage-reports)
+ [More reporting options](#step5-contactlevel-cost-and-usage-reports)

## Things to know about user-defined tags
<a name="about-user-defined-tags"></a>
+ Connect Customer automatically applies user-defined tags to new contact segments for scenarios like transfers or contact re-hydration (for example, persistent chat, and tasks related to contacts).
+ Use the [DescribeContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeContact.html) API to list the tags on a contact.
+ You can remove or overwrite the tags by using the [Contact tags](contact-tags-block.md) block or the [TagContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_TagContact.html) and [UntagContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_UntagContact.html)APIs.
+ By using the [TagContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_TagContact.html) and [UntagContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_UntagContact.html) APIs, you can update user-defined tags for a contact up to 3 hours after the contact was disconnected. However, any future updates on the contact tags are not reflected in the billing system. For example, you make a change to the value of a tag within 3 hours after the contact was disconnected. The AWS Billing console will show the old value of the tag, but the S3 bucket and contact record have the new value.
+ After you add tags to Connect Customer, they are available across all contact interfaces: contact records, contact events, and the **Contact details** page. You can also access them by using the `$.Tags` JSONPath Reference, and by using [Connect Customer Streams](https://github.com/aws/amazon-connect-streams).
+ You cannot use tags as filters on the **Contact search** page. In addition, they cannot be included in any of the analytics or reporting pages. 
+ Contact tags only function as cost allocations tags. You cannot use them for tag-based access controls on contacts.
+ Tags are available in the Connect Customer data lake [Contact record table](data-lake-contact-data.md#data-lake-contacts-record) under tags\_references\_items.

## Step 1: Add user-defined tags to contacts
<a name="step1-tagcontacts"></a>

To add user-defined tags like Department and Cost Center to contacts, you have two options: 
+ Use the [TagContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_TagContact.html) API.
+ Add a [Contact tags](contact-tags-block.md) block to your flow.

The following image shows an example of a **Properties** page of a **Contact tags** block that is configured with a tag named **Department**. Its value is set manually to **Finance**.

![The properties page of a Contact tags block.](http://docs.aws.amazon.com/connect/latest/adminguide/images/granularbilling-contacttags-properties.png)


**Important**  
Do not store personally identifiable information (PII) or other confidential or sensitive information in tags. We use contact tags to provide you with billing services. Tags are not intended to be used for private or sensitive data.

## Step 2: Activate cost allocation tags in the AWS Billing console
<a name="step2-activate-tags"></a>

**Tip**  
It takes up to 24 hours for the tags to activate.

To enable AWS billing applications to organize your billing information according to resources with the same tag key values (either for system-defined and user-defined contact tags), you must activate the tags. Perform the following steps.

1. Open the AWS Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the left navigation menu, choose **Cost Allocation Tags**.

1. Select the system-defined and user-defined tags, and then choose **Activate**. It can take up to 24 hours for tags to activate.

   The following image shows an example tag on the **Cost allocation tags** page.  
![Contact tags on the cost allocation tags page.](http://docs.aws.amazon.com/connect/latest/adminguide/images/granularbilling-costallocationtags.png)

## Step 3: View cost and usage trends using cost allocation tags
<a name="step3-view-billingapp"></a>

You can view the month-over-month trends at the granular level by using cost allocation tags. 

1. Open the AWS Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the left navigation, choose **AWS Cost Explorer**.

1. On the **Cost Explorer** page, choose **Tags**, and then select the tags you want to view, for example, department or inbound telephone number.

   The following image of AWS Cost Explorer shows a sample report where **department** is a filtered cost allocation tag.  
![The AWS Cost Explorer, Connect Customer cost and usage trends.](http://docs.aws.amazon.com/connect/latest/adminguide/images/granularbilling-awscostmanagement.png)

If you use the AWS account level bill summary to view the service level cost breakdown in the AWS Billing dashboard, you won't see any changes on the dashboard after implementing contact tags. The following image shows an example AWS Billing dashboard.

![The AWS billing dashboard, a sample Connect Customer bill.](http://docs.aws.amazon.com/connect/latest/adminguide/images/granularbilling-billingdashboard.png)


For more information about using AWS Cost Explorer, see [Analyzing your costs with AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html) in the *AWS Cost Management User Guide*. 

## (Optional) Step 4: Enable Cost and Usage reports in the AWS Billing and Cost Management console
<a name="step4-cost-and-usage-reports"></a>

You can enable AWS Cost and Usage reports on the AWS Billing and Cost Management console, and configure your S3 bucket to export data to along with time granularity for reports (hourly, daily, monthly). After you set this up, you will receive reports with tags in additional columns. By default reports are aggregated by usage-type and tags.

For instructions, see [Creating Cost and Usage Reports](https://docs.aws.amazon.com/cur/latest/userguide/creating-cur.html) in the *AWS Data Exports User Guide*.

The following image shows what a Cost and Usage report looks like with columns for system and user-defined tags.

![An Connect Customer cost and usage report with tags.](http://docs.aws.amazon.com/connect/latest/adminguide/images/granularbilling-after-cur.png)


The following image shows what a cost and usage report looks likes without system or user-defined tags.

![An Connect Customer cost and usage report without granular billing.](http://docs.aws.amazon.com/connect/latest/adminguide/images/granularbilling-before-cur.png)


## More reporting options
<a name="step5-contactlevel-cost-and-usage-reports"></a>

Another option is to view usage data for each contact. You can enable contact resource IDs to appear on your cost and usage reports in the AWS Billing and Cost Management console. After choosing this option, you will receive detailed reports in your S3 buckets, and the data will be categorized by each contact resource ID. You can use the reports for analysis by third-party applications. 

**Note**  
Including resource IDs creates individual line items for each of your resources. This might increase the size of your Cost and Usage Reports files significantly, based on your AWS usage.

The following image shows where you enable **Include resource IDs** on the AWS Billing console.

![The AWS Billing console.](http://docs.aws.amazon.com/connect/latest/adminguide/images/granularbilling-contactlevel-usagedata.png)


The following image shows a sample cost and usage report when **Include resource IDs** is enabled.

![A sample cost and usage report with resource IDs.](http://docs.aws.amazon.com/connect/latest/adminguide/images/granularbilling-includeresourceids.png)


For instructions for this option, see [Creating Cost and Usage Reports](https://docs.aws.amazon.com/cur/latest/userguide/cur-create.html) in the *AWS Data Exports User Guide*.