

# Amazon SNS SMS activity monitoring
<a name="sms_stats"></a>

By monitoring your SMS activity, you can keep track of destination phone numbers, successful or failed deliveries, reasons for failure, costs, and other information. Amazon SNS helps by summarizing statistics in the console, sending information to Amazon CloudWatch, and sending daily SMS usage reports to an Amazon S3 bucket that you specify.

## Viewing monthly SMS usage reports from Amazon SNS
<a name="sms_stats_usage_monthly"></a>

Track your monthly SMS usage by country.

**Topics**
+ [Monthly usage report information](#monthly_usage_info)
+ [Viewing monthly usage reports](#monthly-usage-reports)

### Monthly usage report information
<a name="monthly_usage_info"></a>

The usage report includes the following information for each SMS message that you send from your account:

The report doesn't include messages sent to recipients who have opted out.
+ Monthly usage cost (in USD)
+ Number of SMS messages published as a request to Amazon SNS
+ Number of times Amazon SNS called AWS End User Messaging SMS
+ Cost incurred for delivering to each country

### Viewing monthly usage reports
<a name="monthly-usage-reports"></a>

**To view monthly usage reports**

1. Sign in to the AWS Management Console and open the AWS Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. On the navigation panel, choose **Cost Explorer**.

1. On the **Report parameters** panel, for the **Service** field, choose **Pinpoint**.
**Note**  
If this is your first time accessing AWS Cost Management, you receive the following message:  
Since this is your first visit, it takes some time to prepare your cost and usage data. Check back in 24 hours.

1. For the **Usage type** field, choose the unit type you want to measure.

   The Cost and Usage graph displays the output of your selections.

1. (Optional) Choose **Save report to library** to .