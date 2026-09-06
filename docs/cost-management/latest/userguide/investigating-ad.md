

# Investigating anomaly root causes with Amazon Q Developer
<a name="investigating-ad"></a>

You can use Amazon Q Developer to investigate the root cause of a detected cost anomaly. When you investigate an anomaly, Amazon Q Developer analyzes your cost data and CloudTrail events to identify what changed, when, where, who triggered the change, and why it happened.

Cost investigation is available at no additional charge for customers using AWS Cost Anomaly Detection. Investigation might incur standard charges for the underlying services it uses on your behalf, such as CloudWatch Logs Insights queries on your CloudTrail data. For details, see [CloudWatch Logs pricing](https://aws.amazon.com/cloudwatch/pricing/).

**Topics**
+ [How cost investigation works](#investigating-ad-how-it-works)
+ [Prerequisites](#investigating-ad-prerequisites)
+ [Investigating an anomaly](#investigating-ad-investigating)
+ [Understanding investigation results](#investigating-ad-results)
+ [Continuing the investigation](#investigating-ad-continuing)
+ [Cross-account investigation](#investigating-ad-cross-account)
+ [Limitations](#investigating-ad-limitations)

## How cost investigation works
<a name="investigating-ad-how-it-works"></a>

When you investigate an anomaly, Amazon Q Developer performs the following analysis:

1. **Identifies what changed** in your cost data by breaking the anomaly down into its largest contributing dimensions (service, account, region, usage type).

1. **Determines whether the change is usage-driven or rate-driven.** A usage-driven change means more resources or activity at the same per-unit price (for example, a new deployment scaling up). A rate-driven change means similar usage at a different per-unit price (for example, a Savings Plans reallocation or a tiered pricing reset).

1. **For usage-driven changes, correlates with CloudTrail** to attribute the cost change to specific API calls and the IAM principals that made them.

1. **For rate-driven changes, attempts to explain the cost composition** by identifying what shifted in pricing or applied discounts.

The investigation output adapts to the anomaly. A simple anomaly with one root cause produces a concise narrative. A complex anomaly with multiple independent causes produces a per-cause breakdown with a synthesis.

## Prerequisites
<a name="investigating-ad-prerequisites"></a>

To use cost investigation, you need the following:
+ **Amazon Q Developer access.** Users must have Amazon Q Developer permissions (`q:StartConversation`, `q:SendMessage`) and the `q:PassRequest` permission. The quickest way to grant access is to use the `AmazonQFullAccess` managed policy. For detailed permission configurations, see [Security for cost management capabilities in Amazon Q Developer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-q-security.html).
+ **(Recommended) An organization-wide CloudTrail trail with management events logging enabled and CloudWatch Logs delivery.** For cross-account investigation, the capability discovers your organization trail automatically and queries CloudWatch Logs Insights to find events across all member accounts. If no organization trail is configured, the investigation completes with the cost data available and tells you what to enable for a fuller answer. For information about creating an organization trail, see [Creating a trail for an organization](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-trail-organization.html) in the *AWS CloudTrail User Guide*.

## Investigating an anomaly
<a name="investigating-ad-investigating"></a>

You can start an investigation from the following locations: the Cost Anomaly Detection console or an Amazon Q Developer conversation.

### From the Cost Anomaly Detection console
<a name="investigating-ad-from-cad-console"></a>

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, choose **Cost Anomaly Detection**.

1. Choose the **Detected anomalies** tab.

1. Select an anomaly to view its details.

1. Choose **Investigate with Amazon Q Developer**.

Amazon Q Developer opens and begins the investigation automatically. Results typically appear within minutes.

### From an Amazon Q Developer conversation
<a name="investigating-ad-from-q-conversation"></a>

When you ask Amazon Q Developer a question about your AWS costs that is best answered by an investigation, Amazon Q Developer might invoke the investigation capability automatically as part of the conversation.

## Understanding investigation results
<a name="investigating-ad-results"></a>

Investigation results might include the following dimensions of a cost change, depending on the data available:
+ **What changed.** The contributing service, account, region, and usage type. The investigation identifies the largest cost drivers, not just the top-level service total.
+ **When.** The timeline of events leading up to the anomaly, anchored to the day the cost change started and the deployment or configuration events that preceded it.
+ **Where.** The accounts and regions involved. For organizations with multiple linked accounts, the investigation identifies the specific account where the change originated.
+ **Who.** The IAM principal that triggered the API call, whether that was a user, a role, or an automated process.
+ **Why.** A plain-language explanation that ties the above together. For example: "An AWS Lambda function in account 111122223333 increased its invocation rate starting May 15 after a deployment by IAM role `deploy-prod`, driving a cost increase in us-east-1."

### When a definitive root cause cannot be identified
<a name="investigating-ad-no-root-cause"></a>

Not every cost change maps to a single API call. Pricing-only changes (such as Savings Plans reallocations or tiered pricing resets) and demand-driven scaling can produce anomalies without a corresponding CloudTrail event. When the investigation cannot identify a definitive root cause, it surfaces what it did find and tells you what additional context would help. It does not fabricate an explanation.

## Continuing the investigation
<a name="investigating-ad-continuing"></a>

After the initial analysis, you can ask follow-up questions in the same Amazon Q Developer conversation to drill deeper or change direction. For example:
+ "Break down the cost increase by service and region."
+ "Is the cost concentrated in a single account or spread across the organization?"
+ "How does this anomaly compare to recent cost changes in this account?"

Amazon Q Developer maintains the conversation context, so each follow-up builds on the prior analysis.

## Cross-account investigation
<a name="investigating-ad-cross-account"></a>

Cost Anomaly Detection monitors that are created in the management (payer) account detect anomalies from spending across the organization. When you investigate an anomaly, the root cause often originates in a linked account within your organization. Cost Explorer aggregates billing data at the payer level, but CloudTrail event data is scoped to the account where the API call was made.

To bridge this gap, the investigation capability automatically discovers your organization-wide CloudTrail trail and queries the CloudWatch Logs location where the trail's events are stored. No configuration is required inside Cost Anomaly Detection or the investigation capability itself. Once the trail exists, the capability discovers and uses it automatically.

If your organization does not have an organization-wide trail with CloudWatch Logs delivery configured, the investigation completes with the data available in the payer account and tells you what to enable for cross-account attribution.

**Note**  
When investigating anomalies using an organization trail delivered to CloudWatch Logs, the capability queries CloudWatch Logs Insights on your behalf, which incurs standard CloudWatch Logs Insights charges based on data scanned. For details, see [Analyzing log data with CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html).

## Limitations
<a name="investigating-ad-limitations"></a>
+ The investigation can identify which user or role triggered cost changes that come from configuration changes (such as launching an EC2 instance, deploying a Lambda function, or creating an S3 bucket). It cannot identify which user or role triggered cost changes that come from data operations (such as Amazon S3 `GetObject` calls or Amazon DynamoDB `GetItem` calls) because CloudTrail does not capture those operations by default.
+ CloudTrail event availability depends on your trail's retention configuration. Older anomalies might have limited or no CloudTrail attribution if events have aged out.
+ Resource-level cost data from Cost Explorer is available only for the last 14 days. For older anomalies, the investigation uses service-level and account-level data.
+ Anomaly data archives after 90 days. Investigations of archived anomalies might have limited data available.