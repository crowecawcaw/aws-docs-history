

# Security Hub CSPM controls for Amazon CloudWatch
<a name="cloudwatch-controls"></a>

These AWS Security Hub CSPM controls evaluate the Amazon CloudWatch service and resources. The controls might not be available in all AWS Regions. For more information, see [Availability of controls by Region](securityhub-regions.md#securityhub-regions-control-support).

## [CloudWatch.1] A log metric filter and alarm should exist for usage of the "root" user
<a name="cloudwatch-1"></a>

**Related requirements:** CIS AWS Foundations Benchmark v1.2.0/1.1,CIS AWS Foundations Benchmark v1.2.0/3.3, CIS AWS Foundations Benchmark v1.4.0/1.7,CIS AWS Foundations Benchmark v1.4.0/4.3, NIST.800-171.r2 3.14.6, NIST.800-171.r2 3.14.7, PCI DSS v3.2.1/7.2.1

**Category:** Detect > Detection services

**Severity:** Low

**Resource type:** `AWS::Logs::MetricFilter`, `AWS::CloudWatch::Alarm`, `AWS::CloudTrail::Trail`, `AWS::SNS::Topic`

**AWS Config rule:** None (custom Security Hub CSPM rule)

**Schedule type:** Periodic

**Parameters:** None

The root user has unrestricted access to all services and resources in an AWS account. We highly recommend that you avoid using the root user for daily tasks. Minimizing the use of the root user and adopting the principle of least privilege for access management reduces the risk of accidental changes and unintended disclosure of highly privileged credentials.

As a best practice, use your root user credentials only when required to [ perform account and service management tasks](https://docs.aws.amazon.com/general/latest/gr/aws_tasks-that-require-root.html). Apply AWS Identity and Access Management (IAM) policies directly to groups and roles but not users. For a tutorial on how to set up an administrator for daily use, see [ Creating your first IAM admin user and group](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html) in the *IAM User Guide*

To run this check, Security Hub CSPM uses custom logic to perform the exact audit steps prescribed for control 1.7 in the [CIS AWS Foundations Benchmark v1.4.0](https://acrobat.adobe.com/link/track?uri=urn:aaid:scds:US:2e5fec5c-5e99-4fb5-b08d-bb46b14754c1#pageNum=1). This control fails if the exact metric filters prescribed by CIS are not used. Additional fields or terms cannot be added to the metric filters.

**Note**  
When Security Hub CSPM performs the check for this control, it looks for CloudTrail trails that the current account uses. These trails might be organization trails that belong to another account. Multi-Region trails also might be based in a different Region.  
The check results in `FAILED` findings in the following cases:  
No trail is configured.
The available trails that are in the current Region and that are owned by current account do not meet the control requirements.
The check results in a control status of `NO_DATA` in the following cases:  
A multi-Region trail is based in a different Region. Security Hub CSPM can only generate findings in the Region where the trail is based.
A multi-Region trail belongs to a different account. Security Hub CSPM can only generate findings for the account that owns the trail.  
As a best practice, use organization trails to log events from many accounts in an organization. Organization trails are multi-Region trails by default and can only be managed by the AWS Organizations management account or the CloudTrail delegated administrator account. Using an organization trail results in a control status of `NO_DATA` for controls evaluated in organization member accounts. In member accounts, Security Hub CSPM only generates findings for member-owned resources. Findings that pertain to organization trails are generated in the resource owner's account. You can see these findings in your Security Hub CSPM delegated administrator account by using cross-Region aggregation.
For the alarm, the current account must either own the referenced Amazon SNS topic, or must get access to the Amazon SNS topic by calling `ListSubscriptionsByTopic`. Otherwise Security Hub CSPM generates `WARNING` findings for the control.

### Remediation
<a name="cloudwatch-1-remediation"></a>

To pass this control, follow these steps to create an Amazon SNS topic, an AWS CloudTrail trail, a metric filter, and an alarm for the metric filter.

1. Create an Amazon SNS topic. For instructions, see [Getting started with Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/sns-getting-started.html#CreateTopic) in the *Amazon Simple Notification Service Developer Guide*. Create a topic that receives all CIS alarms, and create at least one subscription to the topic.

1. Create a CloudTrail trail that applies to all AWS Regions. For instructions, see [Creating a trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.html) in the *AWS CloudTrail User Guide*.

   Make note of the name of the CloudWatch Logs log group that you associate with the CloudTrail trail. You create the metric filter for that log group in the next step.

1. Create a metric filter. For instructions, see [Create a metric filter for a log group](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CreateMetricFilterProcedure.html) in the *Amazon CloudWatch User Guide*. Use the following values:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html)

1. Create an alarm based on the filter. For instructions, see [Create a CloudWatch alarm based on a log group-metric filter](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Alarm-On-Logs.html) in the *Amazon CloudWatch User Guide*. Use the following values:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html)

## [CloudWatch.2] Ensure a log metric filter and alarm exist for unauthorized API calls
<a name="cloudwatch-2"></a>

**Related requirements:** CIS AWS Foundations Benchmark v1.2.0/3.1, NIST.800-171.r2 3.13.1, NIST.800-171.r2 3.14.6, NIST.800-171.r2 3.14.7

**Category:** Detect > Detection services

**Severity:** Low

**Resource type:** `AWS::Logs::MetricFilter`, `AWS::CloudWatch::Alarm`, `AWS::CloudTrail::Trail`, `AWS::SNS::Topic`

**AWS Config rule:** None (custom Security Hub CSPM rule)

**Schedule type:** Periodic

**Parameters:** None

You can do real-time monitoring of API calls by directing CloudTrail logs to CloudWatch Logs and establishing corresponding metric filters and alarms.

CIS recommends that you create a metric filter and alarm for unauthorized API calls. Monitoring unauthorized API calls helps reveal application errors and might reduce time to detect malicious activity.

To run this check, Security Hub CSPM uses custom logic to perform the exact audit steps prescribed for control 3.1 in the [CIS AWS Foundations Benchmark v1.2](https://d1.awsstatic.com/whitepapers/compliance/AWS_CIS_Foundations_Benchmark.pdf). This control fails if the exact metric filters prescribed by CIS are not used. Additional fields or terms cannot be added to the metric filters.

**Note**  
When Security Hub CSPM performs the check for this control, it looks for CloudTrail trails that the current account uses. These trails might be organization trails that belong to another account. Multi-Region trails also might be based in a different Region.  
The check results in `FAILED` findings in the following cases:  
No trail is configured.
The available trails that are in the current Region and that are owned by current account do not meet the control requirements.
The check results in a control status of `NO_DATA` in the following cases:  
A multi-Region trail is based in a different Region. Security Hub CSPM can only generate findings in the Region where the trail is based.
A multi-Region trail belongs to a different account. Security Hub CSPM can only generate findings for the account that owns the trail.  
As a best practice, use organization trails to log events from many accounts in an organization. Organization trails are multi-Region trails by default and can only be managed by the AWS Organizations management account or the CloudTrail delegated administrator account. Using an organization trail results in a control status of `NO_DATA` for controls evaluated in organization member accounts. In member accounts, Security Hub CSPM only generates findings for member-owned resources. Findings that pertain to organization trails are generated in the resource owner's account. You can see these findings in your Security Hub CSPM delegated administrator account by using cross-Region aggregation.
For the alarm, the current account must either own the referenced Amazon SNS topic, or must get access to the Amazon SNS topic by calling `ListSubscriptionsByTopic`. Otherwise Security Hub CSPM generates `WARNING` findings for the control.

### Remediation
<a name="cloudwatch-2-remediation"></a>

To pass this control, follow these steps to create an Amazon SNS topic, an AWS CloudTrail trail, a metric filter, and an alarm for the metric filter.

1. Create an Amazon SNS topic. For instructions, see [Getting started with Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/sns-getting-started.html#CreateTopic) in the *Amazon Simple Notification Service Developer Guide*. Create a topic that receives all CIS alarms, and create at least one subscription to the topic.

1. Create a CloudTrail trail that applies to all AWS Regions. For instructions, see [Creating a trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.html) in the *AWS CloudTrail User Guide*.

   Make note of the name of the CloudWatch Logs log group that you associate with the CloudTrail trail. You create the metric filter for that log group in the next step.

1. Create a metric filter. For instructions, see [Create a metric filter for a log group](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CreateMetricFilterProcedure.html) in the *Amazon CloudWatch User Guide*. Use the following values:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html)

1. Create an alarm based on the filter. For instructions, see [Create a CloudWatch alarm based on a log group-metric filter](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Alarm-On-Logs.html) in the *Amazon CloudWatch User Guide*. Use the following values:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html)

## [CloudWatch.3] Ensure a log metric filter and alarm exist for Management Console sign-in without MFA
<a name="cloudwatch-3"></a>

**Related requirements:** CIS AWS Foundations Benchmark v1.2.0/3.2

**Category:** Detect > Detection services

**Severity:** Low

**Resource type:** `AWS::Logs::MetricFilter`, `AWS::CloudWatch::Alarm`, `AWS::CloudTrail::Trail`, `AWS::SNS::Topic`

**AWS Config rule:** None (custom Security Hub CSPM rule)

**Schedule type:** Periodic

**Parameters:** None

You can do real-time monitoring of API calls by directing CloudTrail logs to CloudWatch Logs and establishing corresponding metric filters and alarms.

CIS recommends that you create a metric filter and alarm console logins that aren't protected by MFA. Monitoring for single-factor console logins increases visibility into accounts that aren't protected by MFA. 

To run this check, Security Hub CSPM uses custom logic to perform the exact audit steps prescribed for control 3.2 in the [CIS AWS Foundations Benchmark v1.2](https://d1.awsstatic.com/whitepapers/compliance/AWS_CIS_Foundations_Benchmark.pdf). This control fails if the exact metric filters prescribed by CIS are not used. Additional fields or terms cannot be added to the metric filters.

**Note**  
When Security Hub CSPM performs the check for this control, it looks for CloudTrail trails that the current account uses. These trails might be organization trails that belong to another account. Multi-Region trails also might be based in a different Region.  
The check results in `FAILED` findings in the following cases:  
No trail is configured.
The available trails that are in the current Region and that are owned by current account do not meet the control requirements.
The check results in a control status of `NO_DATA` in the following cases:  
A multi-Region trail is based in a different Region. Security Hub CSPM can only generate findings in the Region where the trail is based.
A multi-Region trail belongs to a different account. Security Hub CSPM can only generate findings for the account that owns the trail.  
As a best practice, use organization trails to log events from many accounts in an organization. Organization trails are multi-Region trails by default and can only be managed by the AWS Organizations management account or the CloudTrail delegated administrator account. Using an organization trail results in a control status of `NO_DATA` for controls evaluated in organization member accounts. In member accounts, Security Hub CSPM only generates findings for member-owned resources. Findings that pertain to organization trails are generated in the resource owner's account. You can see these findings in your Security Hub CSPM delegated administrator account by using cross-Region aggregation.
For the alarm, the current account must either own the referenced Amazon SNS topic, or must get access to the Amazon SNS topic by calling `ListSubscriptionsByTopic`. Otherwise Security Hub CSPM generates `WARNING` findings for the control.

### Remediation
<a name="cloudwatch-3-remediation"></a>

To pass this control, follow these steps to create an Amazon SNS topic, an AWS CloudTrail trail, a metric filter, and an alarm for the metric filter.

1. Create an Amazon SNS topic. For instructions, see [Getting started with Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/sns-getting-started.html#CreateTopic) in the *Amazon Simple Notification Service Developer Guide*. Create a topic that receives all CIS alarms, and create at least one subscription to the topic.

1. Create a CloudTrail trail that applies to all AWS Regions. For instructions, see [Creating a trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.html) in the *AWS CloudTrail User Guide*.

   Make note of the name of the CloudWatch Logs log group that you associate with the CloudTrail trail. You create the metric filter for that log group in the next step.

1. Create a metric filter. For instructions, see [Create a metric filter for a log group](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CreateMetricFilterProcedure.html) in the *Amazon CloudWatch User Guide*. Use the following values:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html)

1. Create an alarm based on the filter. For instructions, see [Create a CloudWatch alarm based on a log group-metric filter](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Alarm-On-Logs.html) in the *Amazon CloudWatch User Guide*. Use the following values:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html)

## [CloudWatch.4] Ensure a log metric filter and alarm exist for IAM policy changes
<a name="cloudwatch-4"></a>

**Related requirements:** CIS AWS Foundations Benchmark v1.2.0/3.4, CIS AWS Foundations Benchmark v1.4.0/4.4, NIST.800-171.r2 3.14.6, NIST.800-171.r2 3.14.7

**Category:** Detect > Detection services

**Severity:** Low

**Resource type:** `AWS::Logs::MetricFilter`, `AWS::CloudWatch::Alarm`, `AWS::CloudTrail::Trail`, `AWS::SNS::Topic`

**AWS Config rule:** None (custom Security Hub CSPM rule)

**Schedule type:** Periodic

**Parameters:** None

This control checks whether you monitor API calls in real time by directing CloudTrail logs to CloudWatch Logs and establishing corresponding metric filters and alarms.

CIS recommends that you create a metric filter and alarm for changes made to IAM policies. Monitoring these changes helps ensure that authentication and authorization controls remain intact.

**Note**  
When Security Hub CSPM performs the check for this control, it looks for CloudTrail trails that the current account uses. These trails might be organization trails that belong to another account. Multi-Region trails also might be based in a different Region.  
The check results in `FAILED` findings in the following cases:  
No trail is configured.
The available trails that are in the current Region and that are owned by current account do not meet the control requirements.
The check results in a control status of `NO_DATA` in the following cases:  
A multi-Region trail is based in a different Region. Security Hub CSPM can only generate findings in the Region where the trail is based.
A multi-Region trail belongs to a different account. Security Hub CSPM can only generate findings for the account that owns the trail.  
As a best practice, use organization trails to log events from many accounts in an organization. Organization trails are multi-Region trails by default and can only be managed by the AWS Organizations management account or the CloudTrail delegated administrator account. Using an organization trail results in a control status of `NO_DATA` for controls evaluated in organization member accounts. In member accounts, Security Hub CSPM only generates findings for member-owned resources. Findings that pertain to organization trails are generated in the resource owner's account. You can see these findings in your Security Hub CSPM delegated administrator account by using cross-Region aggregation.
For the alarm, the current account must either own the referenced Amazon SNS topic, or must get access to the Amazon SNS topic by calling `ListSubscriptionsByTopic`. Otherwise Security Hub CSPM generates `WARNING` findings for the control.

### Remediation
<a name="cloudwatch-4-remediation"></a>

**Note**  
Our recommended filter pattern in these remediation steps differs from the filter pattern in the CIS guidance. Our recommended filters target only events coming from IAM API calls.

To pass this control, follow these steps to create an Amazon SNS topic, an AWS CloudTrail trail, a metric filter, and an alarm for the metric filter.

1. Create an Amazon SNS topic. For instructions, see [Getting started with Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/sns-getting-started.html#CreateTopic) in the *Amazon Simple Notification Service Developer Guide*. Create a topic that receives all CIS alarms, and create at least one subscription to the topic.

1. Create a CloudTrail trail that applies to all AWS Regions. For instructions, see [Creating a trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.html) in the *AWS CloudTrail User Guide*.

   Make note of the name of the CloudWatch Logs log group that you associate with the CloudTrail trail. You create the metric filter for that log group in the next step.

1. Create a metric filter. For instructions, see [Create a metric filter for a log group](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CreateMetricFilterProcedure.html) in the *Amazon CloudWatch User Guide*. Use the following values:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html)

1. Create an alarm based on the filter. For instructions, see [Create a CloudWatch alarm based on a log group-metric filter](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Alarm-On-Logs.html) in the *Amazon CloudWatch User Guide*. Use the following values:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html)

## [CloudWatch.5] Ensure a log metric filter and alarm exist for CloudTrail configuration changes
<a name="cloudwatch-5"></a>

**Related requirements:** CIS AWS Foundations Benchmark v1.2.0/3.5, CIS AWS Foundations Benchmark v1.4.0/4.5, NIST.800-171.r2 3.3.8, NIST.800-171.r2 3.14.6, NIST.800-171.r2 3.14.7

**Category:** Detect > Detection services

**Severity:** Low

**Resource type:** `AWS::Logs::MetricFilter`, `AWS::CloudWatch::Alarm`, `AWS::CloudTrail::Trail`, `AWS::SNS::Topic`

**AWS Config rule:** None (custom Security Hub CSPM rule)

**Schedule type:** Periodic

**Parameters:** None

You can do real-time monitoring of API calls by directing CloudTrail logs to CloudWatch Logs and establishing corresponding metric filters and alarms.

CIS recommends that you create a metric filter and alarm for changes to CloudTrail configuration settings. Monitoring these changes helps ensure sustained visibility to activities in the account.

To run this check, Security Hub CSPM uses custom logic to perform the exact audit steps prescribed for control 4.5 in the [CIS AWS Foundations Benchmark v1.4.0](https://acrobat.adobe.com/link/track?uri=urn:aaid:scds:US:2e5fec5c-5e99-4fb5-b08d-bb46b14754c1#pageNum=1). This control fails if the exact metric filters prescribed by CIS are not used. Additional fields or terms cannot be added to the metric filters.

**Note**  
When Security Hub CSPM performs the check for this control, it looks for CloudTrail trails that the current account uses. These trails might be organization trails that belong to another account. Multi-Region trails also might be based in a different Region.  
The check results in `FAILED` findings in the following cases:  
No trail is configured.
The available trails that are in the current Region and that are owned by current account do not meet the control requirements.
The check results in a control status of `NO_DATA` in the following cases:  
A multi-Region trail is based in a different Region. Security Hub CSPM can only generate findings in the Region where the trail is based.
A multi-Region trail belongs to a different account. Security Hub CSPM can only generate findings for the account that owns the trail.  
As a best practice, use organization trails to log events from many accounts in an organization. Organization trails are multi-Region trails by default and can only be managed by the AWS Organizations management account or the CloudTrail delegated administrator account. Using an organization trail results in a control status of `NO_DATA` for controls evaluated in organization member accounts. In member accounts, Security Hub CSPM only generates findings for member-owned resources. Findings that pertain to organization trails are generated in the resource owner's account. You can see these findings in your Security Hub CSPM delegated administrator account by using cross-Region aggregation.
For the alarm, the current account must either own the referenced Amazon SNS topic, or must get access to the Amazon SNS topic by calling `ListSubscriptionsByTopic`. Otherwise Security Hub CSPM generates `WARNING` findings for the control.

### Remediation
<a name="cloudwatch-5-remediation"></a>

To pass this control, follow these steps to create an Amazon SNS topic, an AWS CloudTrail trail, a metric filter, and an alarm for the metric filter.

1. Create an Amazon SNS topic. For instructions, see [Getting started with Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/sns-getting-started.html#CreateTopic) in the *Amazon Simple Notification Service Developer Guide*. Create a topic that receives all CIS alarms, and create at least one subscription to the topic.

1. Create a CloudTrail trail that applies to all AWS Regions. For instructions, see [Creating a trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.html) in the *AWS CloudTrail User Guide*.

   Make note of the name of the CloudWatch Logs log group that you associate with the CloudTrail trail. You create the metric filter for that log group in the next step.

1. Create a metric filter. For instructions, see [Create a metric filter for a log group](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CreateMetricFilterProcedure.html) in the *Amazon CloudWatch User Guide*. Use the following values:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html)

1. Create an alarm based on the filter. For instructions, see [Create a CloudWatch alarm based on a log group-metric filter](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Alarm-On-Logs.html) in the *Amazon CloudWatch User Guide*. Use the following values:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html)

## [CloudWatch.6] Ensure a log metric filter and alarm exist for AWS Management Console authentication failures
<a name="cloudwatch-6"></a>

**Related requirements:** CIS AWS Foundations Benchmark v1.2.0/3.6, CIS AWS Foundations Benchmark v1.4.0/4.6, NIST.800-171.r2 3.14.6, NIST.800-171.r2 3.14.7

**Category:** Detect > Detection services

**Severity:** Low

**Resource type:** `AWS::Logs::MetricFilter`, `AWS::CloudWatch::Alarm`, `AWS::CloudTrail::Trail`, `AWS::SNS::Topic`

**AWS Config rule:** None (custom Security Hub CSPM rule)

**Schedule type:** Periodic

**Parameters:** None

You can do real-time monitoring of API calls by directing CloudTrail logs to CloudWatch Logs and establishing corresponding metric filters and alarms.

CIS recommends that you create a metric filter and alarm for failed console authentication attempts. Monitoring failed console logins might decrease lead time to detect an attempt to brute-force a credential, which might provide an indicator, such as source IP, that you can use in other event correlations. 

To run this check, Security Hub CSPM uses custom logic to perform the exact audit steps prescribed for control 4.6 in the [CIS AWS Foundations Benchmark v1.4.0](https://acrobat.adobe.com/link/track?uri=urn:aaid:scds:US:2e5fec5c-5e99-4fb5-b08d-bb46b14754c1#pageNum=1). This control fails if the exact metric filters prescribed by CIS are not used. Additional fields or terms cannot be added to the metric filters.

**Note**  
When Security Hub CSPM performs the check for this control, it looks for CloudTrail trails that the current account uses. These trails might be organization trails that belong to another account. Multi-Region trails also might be based in a different Region.  
The check results in `FAILED` findings in the following cases:  
No trail is configured.
The available trails that are in the current Region and that are owned by current account do not meet the control requirements.
The check results in a control status of `NO_DATA` in the following cases:  
A multi-Region trail is based in a different Region. Security Hub CSPM can only generate findings in the Region where the trail is based.
A multi-Region trail belongs to a different account. Security Hub CSPM can only generate findings for the account that owns the trail.  
As a best practice, use organization trails to log events from many accounts in an organization. Organization trails are multi-Region trails by default and can only be managed by the AWS Organizations management account or the CloudTrail delegated administrator account. Using an organization trail results in a control status of `NO_DATA` for controls evaluated in organization member accounts. In member accounts, Security Hub CSPM only generates findings for member-owned resources. Findings that pertain to organization trails are generated in the resource owner's account. You can see these findings in your Security Hub CSPM delegated administrator account by using cross-Region aggregation.
For the alarm, the current account must either own the referenced Amazon SNS topic, or must get access to the Amazon SNS topic by calling `ListSubscriptionsByTopic`. Otherwise Security Hub CSPM generates `WARNING` findings for the control.

### Remediation
<a name="cloudwatch-6-remediation"></a>

To pass this control, follow these steps to create an Amazon SNS topic, an AWS CloudTrail trail, a metric filter, and an alarm for the metric filter.

1. Create an Amazon SNS topic. For instructions, see [Getting started with Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/sns-getting-started.html#CreateTopic) in the *Amazon Simple Notification Service Developer Guide*. Create a topic that receives all CIS alarms, and create at least one subscription to the topic.

1. Create a CloudTrail trail that applies to all AWS Regions. For instructions, see [Creating a trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.html) in the *AWS CloudTrail User Guide*.

   Make note of the name of the CloudWatch Logs log group that you associate with the CloudTrail trail. You create the metric filter for that log group in the next step.

1. Create a metric filter. For instructions, see [Create a metric filter for a log group](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CreateMetricFilterProcedure.html) in the *Amazon CloudWatch User Guide*. Use the following values:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html)

1. Create an alarm based on the filter. For instructions, see [Create a CloudWatch alarm based on a log group-metric filter](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Alarm-On-Logs.html) in the *Amazon CloudWatch User Guide*. Use the following values:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html)

## [CloudWatch.7] Ensure a log metric filter and alarm exist for disabling or scheduled deletion of customer managed keys
<a name="cloudwatch-7"></a>

**Related requirements:** CIS AWS Foundations Benchmark v1.2.0/3.7, CIS AWS Foundations Benchmark v1.4.0/4.7, NIST.800-171.r2 3.13.10, NIST.800-171.r2 3.13.16, NIST.800-171.r2 3.14.6, NIST.800-171.r2 3.14.7

**Category:** Detect > Detection services

**Severity:** Low

**Resource type:** `AWS::Logs::MetricFilter`, `AWS::CloudWatch::Alarm`, `AWS::CloudTrail::Trail`, `AWS::SNS::Topic`

**AWS Config rule:** None (custom Security Hub CSPM rule)

**Schedule type:** Periodic

**Parameters:** None

You can do real-time monitoring of API calls by directing CloudTrail logs to CloudWatch Logs and establishing corresponding metric filters and alarms.

CIS recommends that you create a metric filter and alarm for customer managed keys that have changed state to disabled or scheduled deletion. Data encrypted with disabled or deleted keys is no longer accessible.

To run this check, Security Hub CSPM uses custom logic to perform the exact audit steps prescribed for control 4.7 in the [CIS AWS Foundations Benchmark v1.4.0](https://acrobat.adobe.com/link/track?uri=urn:aaid:scds:US:2e5fec5c-5e99-4fb5-b08d-bb46b14754c1#pageNum=1). This control fails if the exact metric filters prescribed by CIS are not used. Additional fields or terms cannot be added to the metric filters. The control also fails if `ExcludeManagementEventSources` contains `kms.amazonaws.com`.

**Note**  
When Security Hub CSPM performs the check for this control, it looks for CloudTrail trails that the current account uses. These trails might be organization trails that belong to another account. Multi-Region trails also might be based in a different Region.  
The check results in `FAILED` findings in the following cases:  
No trail is configured.
The available trails that are in the current Region and that are owned by current account do not meet the control requirements.
The check results in a control status of `NO_DATA` in the following cases:  
A multi-Region trail is based in a different Region. Security Hub CSPM can only generate findings in the Region where the trail is based.
A multi-Region trail belongs to a different account. Security Hub CSPM can only generate findings for the account that owns the trail.  
As a best practice, use organization trails to log events from many accounts in an organization. Organization trails are multi-Region trails by default and can only be managed by the AWS Organizations management account or the CloudTrail delegated administrator account. Using an organization trail results in a control status of `NO_DATA` for controls evaluated in organization member accounts. In member accounts, Security Hub CSPM only generates findings for member-owned resources. Findings that pertain to organization trails are generated in the resource owner's account. You can see these findings in your Security Hub CSPM delegated administrator account by using cross-Region aggregation.
For the alarm, the current account must either own the referenced Amazon SNS topic, or must get access to the Amazon SNS topic by calling `ListSubscriptionsByTopic`. Otherwise Security Hub CSPM generates `WARNING` findings for the control.

### Remediation
<a name="cloudwatch-7-remediation"></a>

To pass this control, follow these steps to create an Amazon SNS topic, an AWS CloudTrail trail, a metric filter, and an alarm for the metric filter.

1. Create an Amazon SNS topic. For instructions, see [Getting started with Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/sns-getting-started.html#CreateTopic) in the *Amazon Simple Notification Service Developer Guide*. Create a topic that receives all CIS alarms, and create at least one subscription to the topic.

1. Create a CloudTrail trail that applies to all AWS Regions. For instructions, see [Creating a trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.html) in the *AWS CloudTrail User Guide*.

   Make note of the name of the CloudWatch Logs log group that you associate with the CloudTrail trail. You create the metric filter for that log group in the next step.

1. Create a metric filter. For instructions, see [Create a metric filter for a log group](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CreateMetricFilterProcedure.html) in the *Amazon CloudWatch User Guide*. Use the following values:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html)

1. Create an alarm based on the filter. For instructions, see [Create a CloudWatch alarm based on a log group-metric filter](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Alarm-On-Logs.html) in the *Amazon CloudWatch User Guide*. Use the following values:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html)

## [CloudWatch.8] Ensure a log metric filter and alarm exist for S3 bucket policy changes
<a name="cloudwatch-8"></a>

**Related requirements:** CIS AWS Foundations Benchmark v1.2.0/3.8, CIS AWS Foundations Benchmark v1.4.0/4.8, NIST.800-171.r2 3.14.6, NIST.800-171.r2 3.14.7

**Category:** Detect > Detection services

**Severity:** Low

**Resource type:** `AWS::Logs::MetricFilter`, `AWS::CloudWatch::Alarm`, `AWS::CloudTrail::Trail`, `AWS::SNS::Topic`

**AWS Config rule:** None (custom Security Hub CSPM rule)

**Schedule type:** Periodic

**Parameters:** None

You can do real-time monitoring of API calls by directing CloudTrail logs to CloudWatch Logs and establishing corresponding metric filters and alarms.

CIS recommends that you create a metric filter and alarm for changes to S3 bucket policies. Monitoring these changes might reduce time to detect and correct permissive policies on sensitive S3 buckets.

To run this check, Security Hub CSPM uses custom logic to perform the exact audit steps prescribed for control 4.8 in the [CIS AWS Foundations Benchmark v1.4.0](https://acrobat.adobe.com/link/track?uri=urn:aaid:scds:US:2e5fec5c-5e99-4fb5-b08d-bb46b14754c1#pageNum=1). This control fails if the exact metric filters prescribed by CIS are not used. Additional fields or terms cannot be added to the metric filters.

**Note**  
When Security Hub CSPM performs the check for this control, it looks for CloudTrail trails that the current account uses. These trails might be organization trails that belong to another account. Multi-Region trails also might be based in a different Region.  
The check results in `FAILED` findings in the following cases:  
No trail is configured.
The available trails that are in the current Region and that are owned by current account do not meet the control requirements.
The check results in a control status of `NO_DATA` in the following cases:  
A multi-Region trail is based in a different Region. Security Hub CSPM can only generate findings in the Region where the trail is based.
A multi-Region trail belongs to a different account. Security Hub CSPM can only generate findings for the account that owns the trail.  
As a best practice, use organization trails to log events from many accounts in an organization. Organization trails are multi-Region trails by default and can only be managed by the AWS Organizations management account or the CloudTrail delegated administrator account. Using an organization trail results in a control status of `NO_DATA` for controls evaluated in organization member accounts. In member accounts, Security Hub CSPM only generates findings for member-owned resources. Findings that pertain to organization trails are generated in the resource owner's account. You can see these findings in your Security Hub CSPM delegated administrator account by using cross-Region aggregation.
For the alarm, the current account must either own the referenced Amazon SNS topic, or must get access to the Amazon SNS topic by calling `ListSubscriptionsByTopic`. Otherwise Security Hub CSPM generates `WARNING` findings for the control.

### Remediation
<a name="cloudwatch-8-remediation"></a>

To pass this control, follow these steps to create an Amazon SNS topic, an AWS CloudTrail trail, a metric filter, and an alarm for the metric filter.

1. Create an Amazon SNS topic. For instructions, see [Getting started with Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/sns-getting-started.html#CreateTopic) in the *Amazon Simple Notification Service Developer Guide*. Create a topic that receives all CIS alarms, and create at least one subscription to the topic.

1. Create a CloudTrail trail that applies to all AWS Regions. For instructions, see [Creating a trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.html) in the *AWS CloudTrail User Guide*.

   Make note of the name of the CloudWatch Logs log group that you associate with the CloudTrail trail. You create the metric filter for that log group in the next step.

1. Create a metric filter. For instructions, see [Create a metric filter for a log group](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CreateMetricFilterProcedure.html) in the *Amazon CloudWatch User Guide*. Use the following values:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html)

1. Create an alarm based on the filter. For instructions, see [Create a CloudWatch alarm based on a log group-metric filter](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Alarm-On-Logs.html) in the *Amazon CloudWatch User Guide*. Use the following values:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html)

## [CloudWatch.9] Ensure a log metric filter and alarm exist for AWS Config configuration changes
<a name="cloudwatch-9"></a>

**Related requirements:** CIS AWS Foundations Benchmark v1.2.0/3.9, CIS AWS Foundations Benchmark v1.4.0/4.9, NIST.800-171.r2 3.3.8, NIST.800-171.r2 3.14.6, NIST.800-171.r2 3.14.7

**Category:** Detect > Detection services

**Severity:** Low

**Resource type:** `AWS::Logs::MetricFilter`, `AWS::CloudWatch::Alarm`, `AWS::CloudTrail::Trail`, `AWS::SNS::Topic`

**AWS Config rule:** None (custom Security Hub CSPM rule)

**Schedule type:** Periodic

**Parameters:** None

You can do real-time monitoring of API calls by directing CloudTrail logs to CloudWatch Logs and establishing corresponding metric filters and alarms.

CIS recommends that you create a metric filter and alarm for changes to AWS Config configuration settings. Monitoring these changes helps ensure sustained visibility of configuration items in the account.

To run this check, Security Hub CSPM uses custom logic to perform the exact audit steps prescribed for control 4.9 in the [CIS AWS Foundations Benchmark v1.4.0](https://acrobat.adobe.com/link/track?uri=urn:aaid:scds:US:2e5fec5c-5e99-4fb5-b08d-bb46b14754c1#pageNum=1). This control fails if the exact metric filters prescribed by CIS are not used. Additional fields or terms cannot be added to the metric filters.

**Note**  
When Security Hub CSPM performs the check for this control, it looks for CloudTrail trails that the current account uses. These trails might be organization trails that belong to another account. Multi-Region trails also might be based in a different Region.  
The check results in `FAILED` findings in the following cases:  
No trail is configured.
The available trails that are in the current Region and that are owned by current account do not meet the control requirements.
The check results in a control status of `NO_DATA` in the following cases:  
A multi-Region trail is based in a different Region. Security Hub CSPM can only generate findings in the Region where the trail is based.
A multi-Region trail belongs to a different account. Security Hub CSPM can only generate findings for the account that owns the trail.  
As a best practice, use organization trails to log events from many accounts in an organization. Organization trails are multi-Region trails by default and can only be managed by the AWS Organizations management account or the CloudTrail delegated administrator account. Using an organization trail results in a control status of `NO_DATA` for controls evaluated in organization member accounts. In member accounts, Security Hub CSPM only generates findings for member-owned resources. Findings that pertain to organization trails are generated in the resource owner's account. You can see these findings in your Security Hub CSPM delegated administrator account by using cross-Region aggregation.
For the alarm, the current account must either own the referenced Amazon SNS topic, or must get access to the Amazon SNS topic by calling `ListSubscriptionsByTopic`. Otherwise Security Hub CSPM generates `WARNING` findings for the control.

### Remediation
<a name="cloudwatch-9-remediation"></a>

To pass this control, follow these steps to create an Amazon SNS topic, an AWS CloudTrail trail, a metric filter, and an alarm for the metric filter.

1. Create an Amazon SNS topic. For instructions, see [Getting started with Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/sns-getting-started.html#CreateTopic) in the *Amazon Simple Notification Service Developer Guide*. Create a topic that receives all CIS alarms, and create at least one subscription to the topic.

1. Create a CloudTrail trail that applies to all AWS Regions. For instructions, see [Creating a trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.html) in the *AWS CloudTrail User Guide*.

   Make note of the name of the CloudWatch Logs log group that you associate with the CloudTrail trail. You create the metric filter for that log group in the next step.

1. Create a metric filter. For instructions, see [Create a metric filter for a log group](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CreateMetricFilterProcedure.html) in the *Amazon CloudWatch User Guide*. Use the following values:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html)

1. Create an alarm based on the filter. For instructions, see [Create a CloudWatch alarm based on a log group-metric filter](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Alarm-On-Logs.html) in the *Amazon CloudWatch User Guide*. Use the following values:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html)

## [CloudWatch.10] Ensure a log metric filter and alarm exist for security group changes
<a name="cloudwatch-10"></a>

**Related requirements:** CIS AWS Foundations Benchmark v1.2.0/3.10, CIS AWS Foundations Benchmark v1.4.0/4.10, NIST.800-171.r2 3.14.6, NIST.800-171.r2 3.14.7

**Category:** Detect > Detection services

**Severity:** Low

**Resource type:** `AWS::Logs::MetricFilter`, `AWS::CloudWatch::Alarm`, `AWS::CloudTrail::Trail`, `AWS::SNS::Topic`

**AWS Config rule:** None (custom Security Hub CSPM rule)

**Schedule type:** Periodic

**Parameters:** None

You can do real-time monitoring of API calls by directing CloudTrail logs to CloudWatch Logs and establishing corresponding metric filters and alarms. Security groups are a stateful packet filter that controls ingress and egress traffic in a VPC.

CIS recommends that you create a metric filter and alarm for changes to security groups. Monitoring these changes helps ensure that resources and services aren't unintentionally exposed. 

To run this check, Security Hub CSPM uses custom logic to perform the exact audit steps prescribed for control 4.10 in the [CIS AWS Foundations Benchmark v1.4.0](https://acrobat.adobe.com/link/track?uri=urn:aaid:scds:US:2e5fec5c-5e99-4fb5-b08d-bb46b14754c1#pageNum=1). This control fails if the exact metric filters prescribed by CIS are not used. Additional fields or terms cannot be added to the metric filters.

**Note**  
When Security Hub CSPM performs the check for this control, it looks for CloudTrail trails that the current account uses. These trails might be organization trails that belong to another account. Multi-Region trails also might be based in a different Region.  
The check results in `FAILED` findings in the following cases:  
No trail is configured.
The available trails that are in the current Region and that are owned by current account do not meet the control requirements.
The check results in a control status of `NO_DATA` in the following cases:  
A multi-Region trail is based in a different Region. Security Hub CSPM can only generate findings in the Region where the trail is based.
A multi-Region trail belongs to a different account. Security Hub CSPM can only generate findings for the account that owns the trail.  
As a best practice, use organization trails to log events from many accounts in an organization. Organization trails are multi-Region trails by default and can only be managed by the AWS Organizations management account or the CloudTrail delegated administrator account. Using an organization trail results in a control status of `NO_DATA` for controls evaluated in organization member accounts. In member accounts, Security Hub CSPM only generates findings for member-owned resources. Findings that pertain to organization trails are generated in the resource owner's account. You can see these findings in your Security Hub CSPM delegated administrator account by using cross-Region aggregation.
For the alarm, the current account must either own the referenced Amazon SNS topic, or must get access to the Amazon SNS topic by calling `ListSubscriptionsByTopic`. Otherwise Security Hub CSPM generates `WARNING` findings for the control.

### Remediation
<a name="cloudwatch-10-remediation"></a>

To pass this control, follow these steps to create an Amazon SNS topic, an AWS CloudTrail trail, a metric filter, and an alarm for the metric filter.

1. Create an Amazon SNS topic. For instructions, see [Getting started with Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/sns-getting-started.html#CreateTopic) in the *Amazon Simple Notification Service Developer Guide*. Create a topic that receives all CIS alarms, and create at least one subscription to the topic.

1. Create a CloudTrail trail that applies to all AWS Regions. For instructions, see [Creating a trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.html) in the *AWS CloudTrail User Guide*.

   Make note of the name of the CloudWatch Logs log group that you associate with the CloudTrail trail. You create the metric filter for that log group in the next step.

1. Create a metric filter. For instructions, see [Create a metric filter for a log group](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CreateMetricFilterProcedure.html) in the *Amazon CloudWatch User Guide*. Use the following values:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html)

1. Create an alarm based on the filter. For instructions, see [Create a CloudWatch alarm based on a log group-metric filter](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Alarm-On-Logs.html) in the *Amazon CloudWatch User Guide*. Use the following values:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html)

## [CloudWatch.11] Ensure a log metric filter and alarm exist for changes to Network Access Control Lists (NACL)
<a name="cloudwatch-11"></a>

**Related requirements:** CIS AWS Foundations Benchmark v1.2.0/3.11, CIS AWS Foundations Benchmark v1.4.0/4.11, NIST.800-171.r2 3.14.6, NIST.800-171.r2 3.14.7

**Category:** Detect > Detection services

**Severity:** Low

**Resource type:** `AWS::Logs::MetricFilter`, `AWS::CloudWatch::Alarm`, `AWS::CloudTrail::Trail`, `AWS::SNS::Topic`

**AWS Config rule:** None (custom Security Hub CSPM rule)

**Schedule type:** Periodic

**Parameters:** None

You can do real-time monitoring of API calls by directing CloudTrail logs to CloudWatch Logs and establishing corresponding metric filters and alarms. NACLs are used as a stateless packet filter to control ingress and egress traffic for subnets in a VPC.

CIS recommends that you create a metric filter and alarm for changes to NACLs. Monitoring these changes helps ensure that AWS resources and services aren't unintentionally exposed. 

To run this check, Security Hub CSPM uses custom logic to perform the exact audit steps prescribed for control 4.11 in the [CIS AWS Foundations Benchmark v1.4.0](https://acrobat.adobe.com/link/track?uri=urn:aaid:scds:US:2e5fec5c-5e99-4fb5-b08d-bb46b14754c1#pageNum=1). This control fails if the exact metric filters prescribed by CIS are not used. Additional fields or terms cannot be added to the metric filters.

**Note**  
When Security Hub CSPM performs the check for this control, it looks for CloudTrail trails that the current account uses. These trails might be organization trails that belong to another account. Multi-Region trails also might be based in a different Region.  
The check results in `FAILED` findings in the following cases:  
No trail is configured.
The available trails that are in the current Region and that are owned by current account do not meet the control requirements.
The check results in a control status of `NO_DATA` in the following cases:  
A multi-Region trail is based in a different Region. Security Hub CSPM can only generate findings in the Region where the trail is based.
A multi-Region trail belongs to a different account. Security Hub CSPM can only generate findings for the account that owns the trail.  
As a best practice, use organization trails to log events from many accounts in an organization. Organization trails are multi-Region trails by default and can only be managed by the AWS Organizations management account or the CloudTrail delegated administrator account. Using an organization trail results in a control status of `NO_DATA` for controls evaluated in organization member accounts. In member accounts, Security Hub CSPM only generates findings for member-owned resources. Findings that pertain to organization trails are generated in the resource owner's account. You can see these findings in your Security Hub CSPM delegated administrator account by using cross-Region aggregation.
For the alarm, the current account must either own the referenced Amazon SNS topic, or must get access to the Amazon SNS topic by calling `ListSubscriptionsByTopic`. Otherwise Security Hub CSPM generates `WARNING` findings for the control.

### Remediation
<a name="cloudwatch-11-remediation"></a>

To pass this control, follow these steps to create an Amazon SNS topic, an AWS CloudTrail trail, a metric filter, and an alarm for the metric filter.

1. Create an Amazon SNS topic. For instructions, see [Getting started with Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/sns-getting-started.html#CreateTopic) in the *Amazon Simple Notification Service Developer Guide*. Create a topic that receives all CIS alarms, and create at least one subscription to the topic.

1. Create a CloudTrail trail that applies to all AWS Regions. For instructions, see [Creating a trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.html) in the *AWS CloudTrail User Guide*.

   Make note of the name of the CloudWatch Logs log group that you associate with the CloudTrail trail. You create the metric filter for that log group in the next step.

1. Create a metric filter. For instructions, see [Create a metric filter for a log group](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CreateMetricFilterProcedure.html) in the *Amazon CloudWatch User Guide*. Use the following values:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html)

1. Create an alarm based on the filter. For instructions, see [Create a CloudWatch alarm based on a log group-metric filter](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Alarm-On-Logs.html) in the *Amazon CloudWatch User Guide*. Use the following values:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html)

## [CloudWatch.12] Ensure a log metric filter and alarm exist for changes to network gateways
<a name="cloudwatch-12"></a>

**Related requirements:** CIS AWS Foundations Benchmark v1.2.0/3.12, CIS AWS Foundations Benchmark v1.4.0/4.12, NIST.800-171.r2 3.3.1, NIST.800-171.r2 3.13.1

**Category:** Detect > Detection services

**Severity:** Low

**Resource type:** `AWS::Logs::MetricFilter`, `AWS::CloudWatch::Alarm`, `AWS::CloudTrail::Trail`, `AWS::SNS::Topic`

**AWS Config rule:** None (custom Security Hub CSPM rule)

**Schedule type:** Periodic

**Parameters:** None

You can do real-time monitoring of API calls by directing CloudTrail logs to CloudWatch Logs and establishing corresponding metric filters and alarms. Network gateways are required to send and receive traffic to a destination outside a VPC.

CIS recommends that you create a metric filter and alarm for changes to network gateways. Monitoring these changes helps ensure that all ingress and egress traffic traverses the VPC border via a controlled path.

To run this check, Security Hub CSPM uses custom logic to perform the exact audit steps prescribed for control 4.12 in the [CIS AWS Foundations Benchmark v1.2](https://acrobat.adobe.com/link/track?uri=urn:aaid:scds:US:2e5fec5c-5e99-4fb5-b08d-bb46b14754c1#pageNum=1). This control fails if the exact metric filters prescribed by CIS are not used. Additional fields or terms cannot be added to the metric filters.

**Note**  
When Security Hub CSPM performs the check for this control, it looks for CloudTrail trails that the current account uses. These trails might be organization trails that belong to another account. Multi-Region trails also might be based in a different Region.  
The check results in `FAILED` findings in the following cases:  
No trail is configured.
The available trails that are in the current Region and that are owned by current account do not meet the control requirements.
The check results in a control status of `NO_DATA` in the following cases:  
A multi-Region trail is based in a different Region. Security Hub CSPM can only generate findings in the Region where the trail is based.
A multi-Region trail belongs to a different account. Security Hub CSPM can only generate findings for the account that owns the trail.  
As a best practice, use organization trails to log events from many accounts in an organization. Organization trails are multi-Region trails by default and can only be managed by the AWS Organizations management account or the CloudTrail delegated administrator account. Using an organization trail results in a control status of `NO_DATA` for controls evaluated in organization member accounts. In member accounts, Security Hub CSPM only generates findings for member-owned resources. Findings that pertain to organization trails are generated in the resource owner's account. You can see these findings in your Security Hub CSPM delegated administrator account by using cross-Region aggregation.
For the alarm, the current account must either own the referenced Amazon SNS topic, or must get access to the Amazon SNS topic by calling `ListSubscriptionsByTopic`. Otherwise Security Hub CSPM generates `WARNING` findings for the control.

### Remediation
<a name="cloudwatch-12-remediation"></a>

To pass this control, follow these steps to create an Amazon SNS topic, an AWS CloudTrail trail, a metric filter, and an alarm for the metric filter.

1. Create an Amazon SNS topic. For instructions, see [Getting started with Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/sns-getting-started.html#CreateTopic) in the *Amazon Simple Notification Service Developer Guide*. Create a topic that receives all CIS alarms, and create at least one subscription to the topic.

1. Create a CloudTrail trail that applies to all AWS Regions. For instructions, see [Creating a trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.html) in the *AWS CloudTrail User Guide*.

   Make note of the name of the CloudWatch Logs log group that you associate with the CloudTrail trail. You create the metric filter for that log group in the next step.

1. Create a metric filter. For instructions, see [Create a metric filter for a log group](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CreateMetricFilterProcedure.html) in the *Amazon CloudWatch User Guide*. Use the following values:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html)

1. Create an alarm based on the filter. For instructions, see [Create a CloudWatch alarm based on a log group-metric filter](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Alarm-On-Logs.html) in the *Amazon CloudWatch User Guide*. Use the following values:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html)

## [CloudWatch.13] Ensure a log metric filter and alarm exist for route table changes
<a name="cloudwatch-13"></a>

**Related requirements:** CIS AWS Foundations Benchmark v1.2.0/3.13, CIS AWS Foundations Benchmark v1.4.0/4.13, NIST.800-171.r2 3.3.1, NIST.800-171.r2 3.13.1, NIST.800-171.r2 3.14.6, NIST.800-171.r2 3.14.7

**Category:** Detect > Detection services

**Severity:** Low

**Resource type:** `AWS::Logs::MetricFilter`, `AWS::CloudWatch::Alarm`, `AWS::CloudTrail::Trail`, `AWS::SNS::Topic`

**AWS Config rule:** None (custom Security Hub CSPM rule)

**Schedule type:** Periodic

**Parameters:** None

This control checks whether you monitor API calls in real time by directing CloudTrail logs to CloudWatch Logs and establishing corresponding metric filters and alarms. Routing tables route network traffic between subnets and to network gateways.

CIS recommends that you create a metric filter and alarm for changes to route tables. Monitoring these changes helps ensure that all VPC traffic flows through an expected path.

**Note**  
When Security Hub CSPM performs the check for this control, it looks for CloudTrail trails that the current account uses. These trails might be organization trails that belong to another account. Multi-Region trails also might be based in a different Region.  
The check results in `FAILED` findings in the following cases:  
No trail is configured.
The available trails that are in the current Region and that are owned by current account do not meet the control requirements.
The check results in a control status of `NO_DATA` in the following cases:  
A multi-Region trail is based in a different Region. Security Hub CSPM can only generate findings in the Region where the trail is based.
A multi-Region trail belongs to a different account. Security Hub CSPM can only generate findings for the account that owns the trail.  
As a best practice, use organization trails to log events from many accounts in an organization. Organization trails are multi-Region trails by default and can only be managed by the AWS Organizations management account or the CloudTrail delegated administrator account. Using an organization trail results in a control status of `NO_DATA` for controls evaluated in organization member accounts. In member accounts, Security Hub CSPM only generates findings for member-owned resources. Findings that pertain to organization trails are generated in the resource owner's account. You can see these findings in your Security Hub CSPM delegated administrator account by using cross-Region aggregation.
For the alarm, the current account must either own the referenced Amazon SNS topic, or must get access to the Amazon SNS topic by calling `ListSubscriptionsByTopic`. Otherwise Security Hub CSPM generates `WARNING` findings for the control.

### Remediation
<a name="cloudwatch-13-remediation"></a>

**Note**  
Our recommended filter pattern in these remediation steps differs from the filter pattern in the CIS guidance. Our recommended filters target only events coming from Amazon Elastic Compute Cloud (EC2) API calls.

To pass this control, follow these steps to create an Amazon SNS topic, an AWS CloudTrail trail, a metric filter, and an alarm for the metric filter.

1. Create an Amazon SNS topic. For instructions, see [Getting started with Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/sns-getting-started.html#CreateTopic) in the *Amazon Simple Notification Service Developer Guide*. Create a topic that receives all CIS alarms, and create at least one subscription to the topic.

1. Create a CloudTrail trail that applies to all AWS Regions. For instructions, see [Creating a trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.html) in the *AWS CloudTrail User Guide*.

   Make note of the name of the CloudWatch Logs log group that you associate with the CloudTrail trail. You create the metric filter for that log group in the next step.

1. Create a metric filter. For instructions, see [Create a metric filter for a log group](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CreateMetricFilterProcedure.html) in the *Amazon CloudWatch User Guide*. Use the following values:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html)

1. Create an alarm based on the filter. For instructions, see [Create a CloudWatch alarm based on a log group-metric filter](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Alarm-On-Logs.html) in the *Amazon CloudWatch User Guide*. Use the following values:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html)

## [CloudWatch.14] Ensure a log metric filter and alarm exist for VPC changes
<a name="cloudwatch-14"></a>

**Related requirements:** CIS AWS Foundations Benchmark v1.2.0/3.14, CIS AWS Foundations Benchmark v1.4.0/4.14, NIST.800-171.r2 3.3.1, NIST.800-171.r2 3.13.1, NIST.800-171.r2 3.14.6, NIST.800-171.r2 3.14.7

**Category:** Detect > Detection services

**Severity:** Low

**Resource type:** `AWS::Logs::MetricFilter`, `AWS::CloudWatch::Alarm`, `AWS::CloudTrail::Trail`, `AWS::SNS::Topic`

**AWS Config rule:** None (custom Security Hub CSPM rule)

**Schedule type:** Periodic

**Parameters:** None

You can do real-time monitoring of API calls by directing CloudTrail logs to CloudWatch Logs and establishing corresponding metric filters and alarms. You can have more than one VPC in an account, and you can create a peer connection between two VPCs, enabling network traffic to route between VPCs.

CIS recommends that you create a metric filter and alarm for changes to VPCs. Monitoring these changes helps ensure that authentication and authorization controls remain intact.

To run this check, Security Hub CSPM uses custom logic to perform the exact audit steps prescribed for control 4.14 in the [CIS AWS Foundations Benchmark v1.4.0](https://acrobat.adobe.com/link/track?uri=urn:aaid:scds:US:2e5fec5c-5e99-4fb5-b08d-bb46b14754c1#pageNum=1). This control fails if the exact metric filters prescribed by CIS are not used. Additional fields or terms cannot be added to the metric filters.

**Note**  
When Security Hub CSPM performs the check for this control, it looks for CloudTrail trails that the current account uses. These trails might be organization trails that belong to another account. Multi-Region trails also might be based in a different Region.  
The check results in `FAILED` findings in the following cases:  
No trail is configured.
The available trails that are in the current Region and that are owned by current account do not meet the control requirements.
The check results in a control status of `NO_DATA` in the following cases:  
A multi-Region trail is based in a different Region. Security Hub CSPM can only generate findings in the Region where the trail is based.
A multi-Region trail belongs to a different account. Security Hub CSPM can only generate findings for the account that owns the trail.  
As a best practice, use organization trails to log events from many accounts in an organization. Organization trails are multi-Region trails by default and can only be managed by the AWS Organizations management account or the CloudTrail delegated administrator account. Using an organization trail results in a control status of `NO_DATA` for controls evaluated in organization member accounts. In member accounts, Security Hub CSPM only generates findings for member-owned resources. Findings that pertain to organization trails are generated in the resource owner's account. You can see these findings in your Security Hub CSPM delegated administrator account by using cross-Region aggregation.
For the alarm, the current account must either own the referenced Amazon SNS topic, or must get access to the Amazon SNS topic by calling `ListSubscriptionsByTopic`. Otherwise Security Hub CSPM generates `WARNING` findings for the control.

### Remediation
<a name="cloudwatch-14-remediation"></a>

To pass this control, follow these steps to create an Amazon SNS topic, an AWS CloudTrail trail, a metric filter, and an alarm for the metric filter.

1. Create an Amazon SNS topic. For instructions, see [Getting started with Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/sns-getting-started.html#CreateTopic) in the *Amazon Simple Notification Service Developer Guide*. Create a topic that receives all CIS alarms, and create at least one subscription to the topic.

1. Create a CloudTrail trail that applies to all AWS Regions. For instructions, see [Creating a trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.html) in the *AWS CloudTrail User Guide*.

   Make note of the name of the CloudWatch Logs log group that you associate with the CloudTrail trail. You create the metric filter for that log group in the next step.

1. Create a metric filter. For instructions, see [Create a metric filter for a log group](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CreateMetricFilterProcedure.html) in the *Amazon CloudWatch User Guide*. Use the following values:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html)

1. Create an alarm based on the filter. For instructions, see [Create a CloudWatch alarm based on a log group-metric filter](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Alarm-On-Logs.html) in the *Amazon CloudWatch User Guide*. Use the following values:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html)

## [CloudWatch.15] CloudWatch alarms should have specified actions configured
<a name="cloudwatch-15"></a>

**Related requirements:** NIST.800-53.r5 AU-6(1), NIST.800-53.r5 AU-6(5), NIST.800-53.r5 CA-7, NIST.800-53.r5 IR-4(1), NIST.800-53.r5 IR-4(5), NIST.800-53.r5 SI-2, NIST.800-53.r5 SI-20, NIST.800-53.r5 SI-4(12), NIST.800-53.r5 SI-4(5), NIST.800-171.r2 3.3.4, NIST.800-171.r2 3.14.6

**Category:** Detect > Detection services

**Severity:** High

**Resource type:** `AWS::CloudWatch::Alarm`

**AWS Config rule:** [`cloudwatch-alarm-action-check`](https://docs.aws.amazon.com/config/latest/developerguide/cloudwatch-alarm-action-check.html) ``

**Schedule type:** Change triggered

**Parameters:**


| Parameter | Description | Type | Allowed custom values | Security Hub CSPM default value | 
| --- | --- | --- | --- | --- | 
| `alarmActionRequired` | The control produces a `PASSED` finding if the parameter is set to `true` and the alarm has an action when the alarm state changes to `ALARM`. | Boolean | Not customizable | `true` | 
| `insufficientDataActionRequired` | The control produces a `PASSED` finding if the parameter is set to `true` and the alarm has an action when the alarm state changes to `INSUFFICIENT_DATA`. | Boolean | `true` or `false` | `false` | 
| `okActionRequired` | The control produces a `PASSED` finding if the parameter is set to `true` and the alarm has an action when the alarm state changes to `OK`. | Boolean | `true` or `false` | `false` | 

This control checks whether an Amazon CloudWatch alarm has at least one action configured for the `ALARM` state. The control fails if the alarm doesn't have an action configured for the `ALARM` state. Optionally, you can include custom parameter values to also require alarm actions for the `INSUFFICIENT_DATA` or `OK` states.

**Note**  
Security Hub CSPM evaluates this control based on CloudWatch metric alarms. Metric alarms may be part of composite alarms that have the specified actions configured. The control generates `FAILED` findings in the following cases:  
The specified actions aren't configured for a metric alarm.
The metric alarm is part of a composite alarm that has the specified actions configured.

This control focuses on whether a CloudWatch alarm has an alarm action configured, whereas [CloudWatch.17](#cloudwatch-17) focuses on the activation status of a CloudWatch alarm action.

We recommend CloudWatch alarm actions to automatically alert you when a monitored metric is outside the defined threshold. Monitoring alarms help you identify unusual activities and quickly respond to security and operational issues when an alarm goes into a specific state. The most common type of alarm action is to notify one or more users by sending a message to an Amazon Simple Notification Service (Amazon SNS) topic.

### Remediation
<a name="cloudwatch-15-remediation"></a>

For information about actions supported by CloudWatch alarms, see [Alarm actions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarms-and-actions) in the *Amazon CloudWatch User Guide*.

## [CloudWatch.16] CloudWatch log groups should be retained for a specified time period
<a name="cloudwatch-16"></a>

**Category:** Identify > Logging

**Related requirements:** NIST.800-53.r5 AU-10, NIST.800-53.r5 AU-11, NIST.800-53.r5 AU-6(3), NIST.800-53.r5 AU-6(4), NIST.800-53.r5 CA-7, NIST.800-53.r5 SI-12

**Severity:** Medium

**Resource type:** `AWS::Logs::LogGroup`

**AWS Config rule:** [`cw-loggroup-retention-period-check`](https://docs.aws.amazon.com/config/latest/developerguide/cw-loggroup-retention-period-check.html) ``

**Schedule type:** Periodic

**Parameters:**


| Parameter | Description | Type | Allowed custom values | Security Hub CSPM default value | 
| --- | --- | --- | --- | --- | 
| `minRetentionTime` | Minimum retention period in days for CloudWatch log groups | Enum | `365, 400, 545, 731, 1827, 3653` | `365` | 

This control checks whether an Amazon CloudWatch log group has a retention period of at least the specified number of days. The control fails if the retention period is less than the specified number. Unless you provide a custom parameter value for the retention period, Security Hub CSPM uses a default value of 365 days.

CloudWatch Logs centralize logs from all of your systems, applications, and AWS services in a single, highly scalable service. You can use CloudWatch Logs to monitor, store, and access your log files from Amazon Elastic Compute Cloud (EC2) instances, AWS CloudTrail, Amazon Route 53, and other sources. Retaining your logs for at least 1 year can help you comply with log retention standards.

### Remediation
<a name="cloudwatch-16-remediation"></a>

To configure log retention settings, see [Change log data retention in CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html#SettingLogRetention) in the *Amazon CloudWatch User Guide*.

## [CloudWatch.17] CloudWatch alarm actions should be activated
<a name="cloudwatch-17"></a>

**Category:** Detect > Detection services

**Related requirements:** NIST.800-53.r5 AU-6(1), NIST.800-53.r5 AU-6(5), NIST.800-53.r5 CA-7, NIST.800-53.r5 SI-2, NIST.800-53.r5 SI-4(12)

**Severity:** High

**Resource type:** `AWS::CloudWatch::Alarm`

**AWS Config rule:** [`cloudwatch-alarm-action-enabled-check`](https://docs.aws.amazon.com/config/latest/developerguide/cloudwatch-alarm-action-enabled-check.html) ``

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether CloudWatch alarm actions are activated (`ActionEnabled` should be set to true). The control fails if the alarm action for a CloudWatch alarm is deactivated.

**Note**  
Security Hub CSPM evaluates this control based on CloudWatch metric alarms. Metric alarms may be part of composite alarms that have the alarm actions activated. The control generates `FAILED` findings in the following cases:  
The specified actions aren't configured for a metric alarm.
The metric alarm is part of a composite alarm that has alarm actions activated.

This control focuses on the activation status of a CloudWatch alarm action, whereas [CloudWatch.15](#cloudwatch-15) focuses on whether any `ALARM` action is configured in a CloudWatch alarm.

Alarm actions automatically alert you when a monitored metric is outside the defined threshold. If the alarm action is deactivated, no actions are run when the alarm changes state, and you won't be alerted to changes in monitored metrics. We recommend activating CloudWatch alarm actions to help you quickly respond to security and operational issues.

### Remediation
<a name="cloudwatch-17-remediation"></a>

**To activate a CloudWatch alarm action (console)**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, under **Alarms**, choose **All alarms**.

1. Select the alarm that you want to activate actions for.

1. For **Actions**, choose **Alarm actions–new**, and then choose **Enable**.

For more information about activating CloudWatch alarm actions, see [Alarm actions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarms-and-actions) in the *Amazon CloudWatch User Guide*.