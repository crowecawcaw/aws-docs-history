

# What is Amazon WorkSpaces Advisor?
<a name="workspaces-advisor"></a>

Amazon WorkSpaces Advisor is an AI-powered feature that helps you identify and resolve issues impacting your WorkSpaces Personal resources. WorkSpaces Advisor reviews telemetry, knowledge bases, and best practices to surface issues with recommended remediation actions — directly in the Amazon WorkSpaces console.

With WorkSpaces Advisor, you can:
+ Investigate a WorkSpace and receive a list of identified issues
+ Review supporting telemetry data, including Amazon CloudWatch metrics, for each issue
+ Take recommended remediation actions
+ Chat with WorkSpaces Advisor for follow-up questions through Amazon Q Developer
+ Create a support case pre-populated with investigation context

WorkSpaces Advisor is available in all AWS Regions that support Amazon WorkSpaces Personal at no additional cost.

**Topics**
+ [How investigations work](#workspaces-advisor-how-it-works)
+ [Investigate a WorkSpace](#workspaces-advisor-investigate)
+ [Required permissions](#workspaces-advisor-permissions)
+ [Cross-Region Inference](#workspaces-advisor-cross-region-inference)
+ [Opting out of using your data for service improvement](#workspaces-advisor-opt-out)

## How investigations work
<a name="workspaces-advisor-how-it-works"></a>

When you initiate an investigation, WorkSpaces Advisor deploys AI agents to analyze data from the selected WorkSpace over the past 3 days. The analysis typically completes in under 60 seconds.

WorkSpaces Advisor returns a list of identified issues ordered by severity. For each issue, WorkSpaces Advisor provides at least one recommended action along with alternatives. Each action includes a severity level (Critical, High, Medium, or Low) and describes the risk and impact to your resources.

If WorkSpaces Advisor does not identify your issue, you can provide feedback through the console or create a support case with AWS Support.

### Investigation limits
<a name="workspaces-advisor-limits"></a>
+ You can investigate one WorkSpace at a time.

### Issue severity levels
<a name="workspaces-advisor-severity"></a>

WorkSpaces Advisor categorizes issues by the following severity levels (for example):
+ **Critical** — The user cannot connect to the WorkSpace or the WorkSpace is unresponsive.
+ **High** — The user experience is significantly degraded (for example, high latency or frequent disconnections).
+ **Medium** — The WorkSpace is functional but performance is below optimal levels (for example, elevated CPU or memory usage).
+ **Low** — A potential issue or configuration gap that may not currently affect the user.

### Data accessed by WorkSpaces Advisor
<a name="workspaces-advisor-data"></a>

WorkSpaces Advisor accesses the following data to perform investigations:
+ [Amazon CloudWatch metrics](https://docs.aws.amazon.com/workspaces/latest/adminguide/cloudwatch-metrics.html) (for example, CPU usage, memory usage, and disk usage)
+ WorkSpaces resource configuration (WorkSpace ID, VPC, subnet, bundle type)
+ Service telemetry
+ Application names running on the WorkSpace, including their CPU and memory usage
+ AWS documentation and knowledge bases

## Investigate a WorkSpace
<a name="workspaces-advisor-investigate"></a>

1. Open the [Amazon WorkSpaces console](https://console.aws.amazon.com/workspaces/v2/home).

1. In the navigation pane, choose **WorkSpaces**, then **Personal**.

1. Select the WorkSpace that you want to investigate.

1. Choose **Investigate**.

1. Review the list of identified issues. Choose an issue to view details, including supporting telemetry and recommended actions.

1. Review the risk and impact information for the recommended action, then choose the action to initiate it.

### Get additional help with Amazon Q Developer
<a name="workspaces-advisor-additional-help"></a>
+ **Chat with WorkSpaces Advisor** — Choose **Chat with WorkSpaces Advisor** on the issue details page to ask follow-up questions through AWS Console chat. The chat session automatically includes the full context of the issue.
+ **Create a support case** — Choose **Create support case** to contact AWS Support. The support case is pre-populated with the investigation context.
+ In both cases you will need [permissions to use Amazon Q Developer](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_permissions.html) in the console. For more information about using Amazon Q Developer, see [Chatting with Amazon Q Developer about AWS](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/chat-with-q.html).

## Required permissions
<a name="workspaces-advisor-permissions"></a>

WorkSpaces Advisor uses [Forward access sessions (FAS)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_forward_access_sessions.html) to perform actions using your IAM identity and permissions.

### Permissions for investigations
<a name="workspaces-advisor-permissions-read"></a>

Your IAM role must have the following [permissions for WorkSpaces Advisor](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonworkspaces.html) to initiate investigations and retrieve recommendations. These include `workspaces:InvokeTroubleshootingInvestigation`, `workspaces:GetTroubleshootingRecommendation`, and `workspaces:ListTroubleshootingRecommendations`.

Your IAM role must have read permissions for WorkSpaces and Amazon CloudWatch APIs, such as `workspaces:DescribeWorkSpaces` and `cloudwatch:GetMetricData`. If your role is missing permissions for specific checks, WorkSpaces Advisor skips those checks and displays a message so you can update your permissions.

### Permissions for remediation actions
<a name="workspaces-advisor-permissions-write"></a>

Your IAM role must have permission to perform the specific action (for example, `workspaces:RebootWorkSpaces` or `workspaces:ModifyWorkSpaceProperties`). If your role does not have the required permission, WorkSpaces Advisor returns an error.

## Cross-Region Inference
<a name="workspaces-advisor-cross-region-inference"></a>

Model inference is the process of a model generating an output (response) from a given input (prompt). To use an optimal model for each feature, WorkSpaces Advisor may use [cross-region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html) for data processing. This means WorkSpaces Advisor will automatically select the optimal AWS Region to process inference requests. The available AWS Regions vary based on the region of your WorkSpaces resource. All data is transmitted encrypted across Amazon's secure network and does not traverse the public internet.

The following table lists the inference regions that WorkSpaces Advisor may use:


| Amazon WorkSpaces resource Region | Inference Regions | 
| --- | --- | 
| US East (N. Virginia) (us-east-1)<br />US East (Ohio) (us-east-2)<br />US West (Oregon) (us-west-2) | US East (N. Virginia) (us-east-1)<br />US East (Ohio) (us-east-2)<br />US West (Oregon) (us-west-2) | 
| Africa (Cape Town) (af-south-1) | Africa (Cape Town) (af-south-1)<br />[Commercial AWS Regions](https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html#available-regions) | 
| Asia Pacific (Malaysia) (ap-southeast-5) | Asia Pacific (Malaysia) (ap-southeast-5)<br />[Commercial AWS Regions](https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html#available-regions) | 
| Asia Pacific (Mumbai) (ap-south-1) | Asia Pacific (Mumbai) (ap-south-1)<br />[Commercial AWS Regions](https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html#available-regions) | 
| Asia Pacific (Seoul) (ap-northeast-2) | Asia Pacific (Seoul) (ap-northeast-2)<br />[Commercial AWS Regions](https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html#available-regions) | 
| Asia Pacific (Singapore) (ap-southeast-1) | Asia Pacific (Singapore) (ap-southeast-1)<br />[Commercial AWS Regions](https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html#available-regions) | 
| Asia Pacific (Sydney) (ap-southeast-2) | Asia Pacific (Sydney) (ap-southeast-2)<br />[Commercial AWS Regions](https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html#available-regions) | 
| Asia Pacific (Tokyo) (ap-northeast-1) | Asia Pacific (Tokyo) (ap-northeast-1)<br />[Commercial AWS Regions](https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html#available-regions) | 
| Canada (Central) (ca-central-1) | Canada (Central) (ca-central-1)<br />US East (N. Virginia) (us-east-1)<br />US East (Ohio) (us-east-2)<br />US West (Oregon) (us-west-2) | 
| Europe (Frankfurt) (eu-central-1)<br />Europe (Ireland) (eu-west-1)<br />Europe (Paris) (eu-west-3) | Europe (Frankfurt) (eu-central-1)<br />Europe (Ireland) (eu-west-1)<br />Europe (Milan) (eu-south-1)<br />Europe (Paris) (eu-west-3)<br />Europe (Spain) (eu-south-2)<br />Europe (Stockholm) (eu-north-1) | 
| Europe (London) (eu-west-2) | Europe (London) (eu-west-2)<br />Europe (Frankfurt) (eu-central-1)<br />Europe (Ireland) (eu-west-1)<br />Europe (Milan) (eu-south-1)<br />Europe (Paris) (eu-west-3)<br />Europe (Spain) (eu-south-2)<br />Europe (Stockholm) (eu-north-1) | 
| Israel (Tel Aviv) (il-central-1) | Israel (Tel Aviv) (il-central-1)<br />[Commercial AWS Regions](https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html#available-regions) | 
| South America (Sao Paulo) (sa-east-1) | South America (Sao Paulo) (sa-east-1)<br />[Commercial AWS Regions](https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html#available-regions) | 

## Opting out of using your data for service improvement
<a name="workspaces-advisor-opt-out"></a>

You can choose to opt out of having your data used to develop and improve WorkSpaces Advisor and its underlying technology by using the AWS Organizations opt-out policy. You can choose to opt out even if WorkSpaces Advisor doesn't currently collect any such data. For more information about how to opt out, see [AI services opt-out policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_ai-opt-out.html) in the *AWS Organizations User Guide*.

**Note**  
For you to use the opt-out policy, your AWS accounts must be centrally managed by AWS Organizations. If you haven't already created an organization for your AWS accounts, see [Creating and managing an organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org.html) in the *AWS Organizations User Guide*.

Opting out has the following effects:
+ WorkSpaces Advisor will delete the data that it collected and stored for service improvement purposes prior to your opt out (if any).
+ After you opt out, WorkSpaces Advisor will no longer collect or store this data for service improvement purposes.