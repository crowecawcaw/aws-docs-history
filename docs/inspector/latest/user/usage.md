# Monitoring Usage and Cost in Amazon Inspector

You can use the Amazon Inspector console and API to project monthly Amazon Inspector costs for your environment.
If you're the Amazon Inspector administrator for a multiple-account environment, you can view the total cost for your environment and cost metrics for all member accounts.
This section describes how to access usage statistics and calculate usage costs.

## Using the usage console

You can assess usage and projected cost for Amazon Inspector from the console.

###### To access usage statistics

1. Sign in using your credentials, and then open the Amazon Inspector console at [https://console.aws.amazon.com/inspector/v2/home](https://console.aws.amazon.com/inspector/v2/home "https://console.aws.amazon.com/inspector/v2/home").
2. By using the AWS Region selector in the upper-right corner of the page, select
   the Region you want to monitor costs in.
3. In the navigation pane, choose **Usage**.

In the **By account** tab you will see the projected total cost based on the 30 day period listed under **Account usage**.
In the table under the **Projected cost** column select a value to see a breakdown of usage by scan type for that account. In this detail pane you can also see which scan types have a free trial active for that account.

If you are the delegated administrator for an organization you will see a row in the
table for each account within your organization. If an account in your organization is
disassociated the console shows it's projected cost as a **-**.

In the **By scan type** tab you can see a break down of actual usage so far in the current 30 day period by scan type. This is the information used to calculate the projected costs in the **By account** tab.

If you are the delegated administrator for an organization you can see the usage for each account in your organization.

In this tab, you can expand any of the following panes for usage statistics:

**Amazon EC2 scanning**

The Amazon Inspector usage console tracks the following metrics for agent-based scanning and agentless scanning:

- **Instances (Avg)** — Amazon Inspector uses the coverage hours to calculate the
  average number of resources for EC2 instance scanning. The average is the total
  coverage hours divided by 720 hours (the number of hours in a 30 day
  period).
- **Coverage hours** — for Amazon EC2 scanning this is the sum
  total number of hours within the last 30 days that Amazon Amazon Inspector provided active
  coverage for each EC2 instance in an account. For EC2 instances, coverage hours
  are the hours from when Amazon Inspector discovered the instance until it's terminated or
  stopped, or excluded from scans by tags. (when you restart a stopped instance or remove an exclusion tag, Amazon Inspector resumes coverage and coverage
  hours for that instance will continue to accrue).

**CIS instance Scans** — The total number of CIS scans performed for instances in the account.

**Amazon ECR scanning**

**Initial scans** — The sum total of first time scans of images in the account within the last 30 days.

**Rescans** — The sum total of rescans for images in
the account within the last 30 days. A rescan is any scan done on an ECR image
that Amazon Inspector has previously scanned. If you have configured your ECR repository for continuous scanning, rescans occur automatically when Amazon Inspector adds a new Common Vulnerabilities and Exposures (CVE) to it's
database.

**Lambda scanning**

The Amazon Inspector usage console tracks the following metrics for Lambda standard scanning and Lambda code scanning:

- **Number of Lambda functions (Avg)** — Amazon Inspector uses the coverage hours to calculate the
  average number of functions for Lambda function scanning. Average is the total
  coverage hours divided by 720 hours (the number of hours in a 30 day
  period).
- **Coverage hours** — For Lambda function scanning this
  is the sum total number of hours within the last 30 days that Amazon Amazon Inspector
  provided active coverage for each Lambda function in an account. For AWS Lambda
  functions the coverage hours are calculated from when Amazon Inspector discovers a function
  until when it's deleted or excluded from scans. If an excluded function is
  included again, coverage hours for that function will continue to accrue.

## Understanding how Amazon Inspector calculates usage costs

The costs provided by Amazon Inspector are estimates, not actual costs, so they may differ from those in your AWS Billing console.

Note the following about how Amazon Inspector calculates cost on the **Usage**
page:

- The usage cost reflects the current region only. Prices per scan type vary by AWS Region, to review exact prices per region, see the [Pricing](https://aws.amazon.com//inspector/pricing/ "https://aws.amazon.com//inspector/pricing/") for Amazon Inspector
- All usage projections are rounded to the nearest US dollar.
- Discounts aren't included in the projected costs.
- The projected cost represent the total cost for the 30 day usage period per scan type. If there has been less than 30 days of usage for an account, Amazon Inspector projects the cost after 30 days as if any currently covered resources will remain covered for the rest of the 30 day period.
- The cost per scan type is calculated based on the following:
  - EC2 scanning: cost reflects the average number of EC2 instances covered by Amazon Inspector in the last 30 days.
  - ECR container scanning: cost reflects the sum of the number of initial image scans + image rescans in the last 30 days.
  - Lambda standard scanning: cost reflects the average number of Lambda functions covered by Amazon Inspector in the last 30 days.
  - Lambda code scanning: cost reflects the average number of Lambda functions covered by Amazon Inspector in the last 30 days.

## About the Amazon Inspector free trial

In Amazon Inspector, each [scan type](scanning-resources.md#scan-types "scanning-resources.md#scan-types") has a free trail.
When you activate a scan type, you automatically enroll in a 15-day free trial for that scan type.
Once the free trial starts, it automatically expires in 15 days, even if you deactivate the scan type.

###### Note

The free trial does not apply to [CIS scanning](scanning-cis.md "scanning-cis.md").
