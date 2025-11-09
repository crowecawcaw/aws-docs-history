# Security Hub controls for Amazon CloudWatch

These AWS Security Hub controls evaluate the Amazon CloudWatch service and resources. The controls might not
be available in all AWS Regions. For more information, see [Availability of controls by
Region](securityhub-regions.md#securityhub-regions-control-support "securityhub-regions.md#securityhub-regions-control-support").

## [CloudWatch.1] A log metric filter and alarm should exist for usage of the "root" user

**Related requirements:** CIS AWS Foundations Benchmark
v1.2.0/1.1,CIS AWS Foundations Benchmark v1.2.0/3.3, CIS AWS Foundations Benchmark
v1.4.0/1.7,CIS AWS Foundations Benchmark v1.4.0/4.3, NIST.800-171.r2 3.14.6,
NIST.800-171.r2 3.14.7, PCI DSS v3.2.1/7.2.1

**Category:** Detect > Detection services

**Severity:** Low

**Resource type:** `AWS::Logs::MetricFilter`, `AWS::CloudWatch::Alarm`, `AWS::CloudTrail::Trail`, `AWS::SNS::Topic`

**AWS Config rule:** None (custom Security Hub rule)

**Schedule type:** Periodic

**Parameters:** None

The root user has unrestricted access to all services and resources in an AWS account.
We highly recommend that you avoid using the root user for daily tasks. Minimizing the use
of the root user and adopting the principle of least privilege for access management
reduces the risk of accidental changes and unintended disclosure of highly privileged
credentials.

As a best practice, use your root user credentials only when required to [perform account and service management tasks](../../../general/latest/gr/aws_tasks-that-require-root.md "../../../general/latest/gr/aws_tasks-that-require-root.md"). Apply AWS Identity and Access Management (IAM) policies
directly to groups and roles but not users. For a tutorial on how to set up an
administrator for daily use, see [Creating your first IAM admin user and group](../../../IAM/latest/UserGuide/getting-started_create-admin-group.md "../../../IAM/latest/UserGuide/getting-started_create-admin-group.md") in
the _IAM User Guide_

To run this check, Security Hub uses custom logic to perform the exact audit steps
prescribed for control 1.7 in the [CIS AWS Foundations Benchmark v1.4.0](https://acrobat.adobe.com/link/track?uri=urn:aaid:scds:US:2e5fec5c-5e99-4fb5-b08d-bb46b14754c1#pageNum=1 "https://acrobat.adobe.com/link/track?uri=urn:aaid:scds:US:2e5fec5c-5e99-4fb5-b08d-bb46b14754c1#pageNum=1"). This control fails if the exact
metric filters prescribed by CIS are not used. Additional fields or terms cannot be
added to the metric filters.

###### Note

When Security Hub performs the check for this control, it looks for CloudTrail trails that the current account uses. These trails might be organization trails that belong to another account. Multi-Region trails also might be based in a different Region.

The check results in `FAILED` findings in the following cases:

- No trail is configured.
- The available trails that are in the current Region and that are owned by current account do not meet the control requirements.
  The check results in a control status of `NO_DATA` in the following cases:

- A multi-Region trail is based in a different Region. Security Hub can only generate findings in the Region where the trail is based.
- A multi-Region trail belongs to a different account. Security Hub can only generate findings for the account that owns the trail.

We recommend organization trails to log events from many accounts in an organization. Organization trails are multi-Region
trails by default and can only be managed by the AWS Organizations management account or the CloudTrail delegated administrator account. Using an
organization trail results in a control status of `NO_DATA` for controls evaluated in organization member
accounts. In member accounts, Security Hub only generates findings for member-owned resources. Findings that pertain to organization trails
are generated in the resource owner's account. You can see these findings in your Security Hub delegated administrator account by using cross-Region
aggregation.
For the alarm, the current account must either own the referenced Amazon SNS topic, or must get access to the Amazon SNS topic by calling `ListSubscriptionsByTopic`. Otherwise Security Hub generates `WARNING` findings for the control.

### Remediation

To pass this control, follow these steps to create an Amazon SNS topic, an AWS CloudTrail
trail, a metric filter, and an alarm for the metric filter.

1. Create an Amazon SNS topic. For instructions, see [Getting started with Amazon SNS](../../../sns/latest/dg/sns-getting-started.md#CreateTopic "../../../sns/latest/dg/sns-getting-started.md#CreateTopic") in the
   _Amazon Simple Notification Service Developer Guide_. Create a topic that receives all CIS alarms, and create
   at least one subscription to the topic.
2. Create a CloudTrail trail that applies to all AWS Regions. For instructions, see [Creating a trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.md") in the
   _AWS CloudTrail User Guide_.

Make note of the name of the CloudWatch Logs log group that you associate with the CloudTrail trail. You create the
metric filter for that log group in the next step. 3. Create a metric filter. For instructions, see [Create a metric filter for a log group](../../../AmazonCloudWatch/latest/logs/CreateMetricFilterProcedure.md "../../../AmazonCloudWatch/latest/logs/CreateMetricFilterProcedure.md") in the
_Amazon CloudWatch User Guide_. Use the following values:

| Field                          | Value                                                                                                    |
| ------------------------------ | -------------------------------------------------------------------------------------------------------- |
| Define pattern, Filter pattern | `{$.userIdentity.type="Root" && $.userIdentity.invokedBy NOT EXISTS && $.eventType !="AwsServiceEvent"}` |
| Metric namespace               | `LogMetrics`                                                                                             |
| Metric value                   | `1`                                                                                                      |
| Default value                  | `0`                                                                                                      |

4. Create an alarm based on the filter. For instructions, see [Create a CloudWatch alarm based on a log group-metric filter](../../../AmazonCloudWatch/latest/monitoring/Alarm-On-Logs.md "../../../AmazonCloudWatch/latest/monitoring/Alarm-On-Logs.md") in the _Amazon CloudWatch User Guide_. Use the following values:

| Field                             | Value         |
| --------------------------------- | ------------- |
| Conditions, Threshold type        | Static        |
| Whenever `your-metric-name` is... | Greater/Equal |
| than...                           | `1`           |

## [CloudWatch.2] Ensure a log metric filter and alarm exist for unauthorized API calls

**Related requirements:** CIS AWS Foundations Benchmark
v1.2.0/3.1, NIST.800-171.r2 3.13.1, NIST.800-171.r2 3.14.6, NIST.800-171.r2
3.14.7

**Category:** Detect > Detection services

**Severity:** Low

**Resource type:** `AWS::Logs::MetricFilter`, `AWS::CloudWatch::Alarm`, `AWS::CloudTrail::Trail`, `AWS::SNS::Topic`

**AWS Config rule:** None (custom Security Hub rule)

**Schedule type:** Periodic

**Parameters:** None

You can do real-time monitoring of API calls by directing CloudTrail logs to CloudWatch Logs and
establishing corresponding metric filters and alarms.

CIS recommends that you create a metric filter and alarm for unauthorized API
calls. Monitoring unauthorized API calls helps reveal application errors and might
reduce time to detect malicious activity.

To run this check, Security Hub uses custom logic to perform the exact audit steps
prescribed for control 3.1 in the [CIS AWS Foundations Benchmark v1.2](https://d1.awsstatic.com/whitepapers/compliance/AWS_CIS_Foundations_Benchmark.pdf "https://d1.awsstatic.com/whitepapers/compliance/AWS_CIS_Foundations_Benchmark.pdf"). This control fails if the exact
metric filters prescribed by CIS are not used. Additional fields or terms cannot be
added to the metric filters.

###### Note

When Security Hub performs the check for this control, it looks for CloudTrail trails that the current account uses. These trails might be organization trails that belong to another account. Multi-Region trails also might be based in a different Region.

The check results in `FAILED` findings in the following cases:

- No trail is configured.
- The available trails that are in the current Region and that are owned by current account do not meet the control requirements.
  The check results in a control status of `NO_DATA` in the following cases:

- A multi-Region trail is based in a different Region. Security Hub can only generate findings in the Region where the trail is based.
- A multi-Region trail belongs to a different account. Security Hub can only generate findings for the account that owns the trail.

We recommend organization trails to log events from many accounts in an organization. Organization trails are multi-Region
trails by default and can only be managed by the AWS Organizations management account or the CloudTrail delegated administrator account. Using an
organization trail results in a control status of `NO_DATA` for controls evaluated in organization member
accounts. In member accounts, Security Hub only generates findings for member-owned resources. Findings that pertain to organization trails
are generated in the resource owner's account. You can see these findings in your Security Hub delegated administrator account by using cross-Region
aggregation.
For the alarm, the current account must either own the referenced Amazon SNS topic, or must get access to the Amazon SNS topic by calling `ListSubscriptionsByTopic`. Otherwise Security Hub generates `WARNING` findings for the control.

### Remediation

To pass this control, follow these steps to create an Amazon SNS topic, an AWS CloudTrail
trail, a metric filter, and an alarm for the metric filter.

1. Create an Amazon SNS topic. For instructions, see [Getting started with Amazon SNS](../../../sns/latest/dg/sns-getting-started.md#CreateTopic "../../../sns/latest/dg/sns-getting-started.md#CreateTopic") in the
   _Amazon Simple Notification Service Developer Guide_. Create a topic that receives all CIS alarms, and create
   at least one subscription to the topic.
2. Create a CloudTrail trail that applies to all AWS Regions. For instructions, see [Creating a trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.md") in the
   _AWS CloudTrail User Guide_.

Make note of the name of the CloudWatch Logs log group that you associate with the CloudTrail trail. You create the
metric filter for that log group in the next step. 3. Create a metric filter. For instructions, see [Create a metric filter for a log group](../../../AmazonCloudWatch/latest/logs/CreateMetricFilterProcedure.md "../../../AmazonCloudWatch/latest/logs/CreateMetricFilterProcedure.md") in the
_Amazon CloudWatch User Guide_. Use the following values:

| Field                          | Value                                     |
| ------------------------------ | ----------------------------------------- | --- | -------------------------------- |
| Define pattern, Filter pattern | `{($.errorCode="\*UnauthorizedOperation") |     | ($.errorCode="AccessDenied\*")}` |
| Metric namespace               | `LogMetrics`                              |
| Metric value                   | `1`                                       |
| Default value                  | `0`                                       |

4. Create an alarm based on the filter. For instructions, see [Create a CloudWatch alarm based on a log group-metric filter](../../../AmazonCloudWatch/latest/monitoring/Alarm-On-Logs.md "../../../AmazonCloudWatch/latest/monitoring/Alarm-On-Logs.md") in the _Amazon CloudWatch User Guide_. Use the following values:

| Field                             | Value         |
| --------------------------------- | ------------- |
| Conditions, Threshold type        | Static        |
| Whenever `your-metric-name` is... | Greater/Equal |
| than...                           | `1`           |

## [CloudWatch.3] Ensure a log metric filter and alarm exist for Management Console sign-in without MFA

**Related requirements:** CIS AWS Foundations Benchmark v1.2.0/3.2

**Category:** Detect > Detection services

**Severity:** Low

**Resource type:** `AWS::Logs::MetricFilter`, `AWS::CloudWatch::Alarm`, `AWS::CloudTrail::Trail`, `AWS::SNS::Topic`

**AWS Config rule:** None (custom Security Hub rule)

**Schedule type:** Periodic

**Parameters:** None

You can do real-time monitoring of API calls by directing CloudTrail logs to CloudWatch Logs and
establishing corresponding metric filters and alarms.

CIS recommends that you create a metric filter and alarm console logins that
aren't protected by MFA. Monitoring for single-factor console logins increases
visibility into accounts that aren't protected by MFA.

To run this check, Security Hub uses custom logic to perform the exact audit steps
prescribed for control 3.2 in the [CIS AWS Foundations Benchmark v1.2](https://d1.awsstatic.com/whitepapers/compliance/AWS_CIS_Foundations_Benchmark.pdf "https://d1.awsstatic.com/whitepapers/compliance/AWS_CIS_Foundations_Benchmark.pdf"). This control fails if the exact
metric filters prescribed by CIS are not used. Additional fields or terms cannot be
added to the metric filters.

###### Note

When Security Hub performs the check for this control, it looks for CloudTrail trails that the current account uses. These trails might be organization trails that belong to another account. Multi-Region trails also might be based in a different Region.

The check results in `FAILED` findings in the following cases:

- No trail is configured.
- The available trails that are in the current Region and that are owned by current account do not meet the control requirements.
  The check results in a control status of `NO_DATA` in the following cases:

- A multi-Region trail is based in a different Region. Security Hub can only generate findings in the Region where the trail is based.
- A multi-Region trail belongs to a different account. Security Hub can only generate findings for the account that owns the trail.

We recommend organization trails to log events from many accounts in an organization. Organization trails are multi-Region
trails by default and can only be managed by the AWS Organizations management account or the CloudTrail delegated administrator account. Using an
organization trail results in a control status of `NO_DATA` for controls evaluated in organization member
accounts. In member accounts, Security Hub only generates findings for member-owned resources. Findings that pertain to organization trails
are generated in the resource owner's account. You can see these findings in your Security Hub delegated administrator account by using cross-Region
aggregation.
For the alarm, the current account must either own the referenced Amazon SNS topic, or must get access to the Amazon SNS topic by calling `ListSubscriptionsByTopic`. Otherwise Security Hub generates `WARNING` findings for the control.

### Remediation

To pass this control, follow these steps to create an Amazon SNS topic, an AWS CloudTrail
trail, a metric filter, and an alarm for the metric filter.

1. Create an Amazon SNS topic. For instructions, see [Getting started with Amazon SNS](../../../sns/latest/dg/sns-getting-started.md#CreateTopic "../../../sns/latest/dg/sns-getting-started.md#CreateTopic") in the
   _Amazon Simple Notification Service Developer Guide_. Create a topic that receives all CIS alarms, and create
   at least one subscription to the topic.
2. Create a CloudTrail trail that applies to all AWS Regions. For instructions, see [Creating a trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.md") in the
   _AWS CloudTrail User Guide_.

Make note of the name of the CloudWatch Logs log group that you associate with the CloudTrail trail. You create the
metric filter for that log group in the next step. 3. Create a metric filter. For instructions, see [Create a metric filter for a log group](../../../AmazonCloudWatch/latest/logs/CreateMetricFilterProcedure.md "../../../AmazonCloudWatch/latest/logs/CreateMetricFilterProcedure.md") in the
_Amazon CloudWatch User Guide_. Use the following values:

| Field                          | Value                                                                                                                                                                  |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Define pattern, Filter pattern | `{ ($.eventName = "ConsoleLogin") && ($.additionalEventData.MFAUsed != "Yes") && ($.userIdentity.type = "IAMUser") && ($.responseElements.ConsoleLogin = "Success") }` |
| Metric namespace               | `LogMetrics`                                                                                                                                                           |
| Metric value                   | `1`                                                                                                                                                                    |
| Default value                  | `0`                                                                                                                                                                    |

4. Create an alarm based on the filter. For instructions, see [Create a CloudWatch alarm based on a log group-metric filter](../../../AmazonCloudWatch/latest/monitoring/Alarm-On-Logs.md "../../../AmazonCloudWatch/latest/monitoring/Alarm-On-Logs.md") in the _Amazon CloudWatch User Guide_. Use the following values:

| Field                             | Value         |
| --------------------------------- | ------------- |
| Conditions, Threshold type        | Static        |
| Whenever `your-metric-name` is... | Greater/Equal |
| than...                           | `1`           |

## [CloudWatch.4] Ensure a log metric filter and alarm exist for IAM policy changes

**Related requirements:** CIS AWS Foundations Benchmark
v1.2.0/3.4, CIS AWS Foundations Benchmark v1.4.0/4.4, NIST.800-171.r2 3.14.6,
NIST.800-171.r2 3.14.7

**Category:** Detect > Detection services

**Severity:** Low

**Resource type:** `AWS::Logs::MetricFilter`, `AWS::CloudWatch::Alarm`, `AWS::CloudTrail::Trail`, `AWS::SNS::Topic`

**AWS Config rule:** None (custom Security Hub rule)

**Schedule type:** Periodic

**Parameters:** None

This control checks whether you monitor API calls in real time by directing CloudTrail logs to CloudWatch Logs and
establishing corresponding metric filters and alarms.

CIS recommends that you create a metric filter and alarm for changes made to IAM
policies. Monitoring these changes helps ensure that authentication and
authorization controls remain intact.

###### Note

When Security Hub performs the check for this control, it looks for CloudTrail trails that the current account uses. These trails might be organization trails that belong to another account. Multi-Region trails also might be based in a different Region.

The check results in `FAILED` findings in the following cases:

- No trail is configured.
- The available trails that are in the current Region and that are owned by current account do not meet the control requirements.
  The check results in a control status of `NO_DATA` in the following cases:

- A multi-Region trail is based in a different Region. Security Hub can only generate findings in the Region where the trail is based.
- A multi-Region trail belongs to a different account. Security Hub can only generate findings for the account that owns the trail.

We recommend organization trails to log events from many accounts in an organization. Organization trails are multi-Region
trails by default and can only be managed by the AWS Organizations management account or the CloudTrail delegated administrator account. Using an
organization trail results in a control status of `NO_DATA` for controls evaluated in organization member
accounts. In member accounts, Security Hub only generates findings for member-owned resources. Findings that pertain to organization trails
are generated in the resource owner's account. You can see these findings in your Security Hub delegated administrator account by using cross-Region
aggregation.
For the alarm, the current account must either own the referenced Amazon SNS topic, or must get access to the Amazon SNS topic by calling `ListSubscriptionsByTopic`. Otherwise Security Hub generates `WARNING` findings for the control.

### Remediation

###### Note

Our recommended filter pattern in these remediation steps differs from the filter pattern in the CIS guidance. Our recommended filters
target only events coming from IAM API calls.

To pass this control, follow these steps to create an Amazon SNS topic, an AWS CloudTrail
trail, a metric filter, and an alarm for the metric filter.

1. Create an Amazon SNS topic. For instructions, see [Getting started with Amazon SNS](../../../sns/latest/dg/sns-getting-started.md#CreateTopic "../../../sns/latest/dg/sns-getting-started.md#CreateTopic") in the
   _Amazon Simple Notification Service Developer Guide_. Create a topic that receives all CIS alarms, and create
   at least one subscription to the topic.
2. Create a CloudTrail trail that applies to all AWS Regions. For instructions, see [Creating a trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.md") in the
   _AWS CloudTrail User Guide_.

Make note of the name of the CloudWatch Logs log group that you associate with the CloudTrail trail. You create the
metric filter for that log group in the next step. 3. Create a metric filter. For instructions, see [Create a metric filter for a log group](../../../AmazonCloudWatch/latest/logs/CreateMetricFilterProcedure.md "../../../AmazonCloudWatch/latest/logs/CreateMetricFilterProcedure.md") in the
_Amazon CloudWatch User Guide_. Use the following values:

| Field                          | Value                                                                   |
| ------------------------------ | ----------------------------------------------------------------------- | --- | ------------------------------ | --- | ------------------------------ | --- | ---------------------------- | --- | --------------------------- | --- | --------------------------- | --- | -------------------------- | --- | -------------------------- | --- | --------------------------------- | --- | --------------------------------- | --- | ------------------------------ | --- | ------------------------------ | --- | ------------------------------ | --- | ------------------------------ | --- | ------------------------------- | --- | ---------------------------------- |
| Define pattern, Filter pattern | `{($.eventSource=iam.amazonaws.com) && (($.eventName=DeleteGroupPolicy) |     | ($.eventName=DeleteRolePolicy) |     | ($.eventName=DeleteUserPolicy) |     | ($.eventName=PutGroupPolicy) |     | ($.eventName=PutRolePolicy) |     | ($.eventName=PutUserPolicy) |     | ($.eventName=CreatePolicy) |     | ($.eventName=DeletePolicy) |     | ($.eventName=CreatePolicyVersion) |     | ($.eventName=DeletePolicyVersion) |     | ($.eventName=AttachRolePolicy) |     | ($.eventName=DetachRolePolicy) |     | ($.eventName=AttachUserPolicy) |     | ($.eventName=DetachUserPolicy) |     | ($.eventName=AttachGroupPolicy) |     | ($.eventName=DetachGroupPolicy))}` |
| Metric namespace               | `LogMetrics`                                                            |
| Metric value                   | `1`                                                                     |
| Default value                  | `0`                                                                     |

4. Create an alarm based on the filter. For instructions, see [Create a CloudWatch alarm based on a log group-metric filter](../../../AmazonCloudWatch/latest/monitoring/Alarm-On-Logs.md "../../../AmazonCloudWatch/latest/monitoring/Alarm-On-Logs.md") in the _Amazon CloudWatch User Guide_. Use the following values:

| Field                             | Value         |
| --------------------------------- | ------------- |
| Conditions, Threshold type        | Static        |
| Whenever `your-metric-name` is... | Greater/Equal |
| than...                           | `1`           |

## [CloudWatch.5] Ensure a log metric filter and alarm exist for CloudTrail

configuration changes

**Related requirements:** CIS AWS Foundations Benchmark
v1.2.0/3.5, CIS AWS Foundations Benchmark v1.4.0/4.5, NIST.800-171.r2 3.3.8,
NIST.800-171.r2 3.14.6, NIST.800-171.r2 3.14.7

**Category:** Detect > Detection services

**Severity:** Low

**Resource type:** `AWS::Logs::MetricFilter`, `AWS::CloudWatch::Alarm`, `AWS::CloudTrail::Trail`, `AWS::SNS::Topic`

**AWS Config rule:** None (custom Security Hub rule)

**Schedule type:** Periodic

**Parameters:** None

You can do real-time monitoring of API calls by directing CloudTrail logs to CloudWatch Logs and
establishing corresponding metric filters and alarms.

CIS recommends that you create a metric filter and alarm for changes to CloudTrail
configuration settings. Monitoring these changes helps ensure sustained visibility
to activities in the account.

To run this check, Security Hub uses custom logic to perform the exact audit steps
prescribed for control 4.5 in the [CIS AWS Foundations Benchmark v1.4.0](https://acrobat.adobe.com/link/track?uri=urn:aaid:scds:US:2e5fec5c-5e99-4fb5-b08d-bb46b14754c1#pageNum=1 "https://acrobat.adobe.com/link/track?uri=urn:aaid:scds:US:2e5fec5c-5e99-4fb5-b08d-bb46b14754c1#pageNum=1"). This control fails if the exact
metric filters prescribed by CIS are not used. Additional fields or terms cannot be
added to the metric filters.

###### Note

When Security Hub performs the check for this control, it looks for CloudTrail trails that the current account uses. These trails might be organization trails that belong to another account. Multi-Region trails also might be based in a different Region.

The check results in `FAILED` findings in the following cases:

- No trail is configured.
- The available trails that are in the current Region and that are owned by current account do not meet the control requirements.
  The check results in a control status of `NO_DATA` in the following cases:

- A multi-Region trail is based in a different Region. Security Hub can only generate findings in the Region where the trail is based.
- A multi-Region trail belongs to a different account. Security Hub can only generate findings for the account that owns the trail.

We recommend organization trails to log events from many accounts in an organization. Organization trails are multi-Region
trails by default and can only be managed by the AWS Organizations management account or the CloudTrail delegated administrator account. Using an
organization trail results in a control status of `NO_DATA` for controls evaluated in organization member
accounts. In member accounts, Security Hub only generates findings for member-owned resources. Findings that pertain to organization trails
are generated in the resource owner's account. You can see these findings in your Security Hub delegated administrator account by using cross-Region
aggregation.
For the alarm, the current account must either own the referenced Amazon SNS topic, or must get access to the Amazon SNS topic by calling `ListSubscriptionsByTopic`. Otherwise Security Hub generates `WARNING` findings for the control.

### Remediation

To pass this control, follow these steps to create an Amazon SNS topic, an AWS CloudTrail
trail, a metric filter, and an alarm for the metric filter.

1. Create an Amazon SNS topic. For instructions, see [Getting started with Amazon SNS](../../../sns/latest/dg/sns-getting-started.md#CreateTopic "../../../sns/latest/dg/sns-getting-started.md#CreateTopic") in the
   _Amazon Simple Notification Service Developer Guide_. Create a topic that receives all CIS alarms, and create
   at least one subscription to the topic.
2. Create a CloudTrail trail that applies to all AWS Regions. For instructions, see [Creating a trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.md") in the
   _AWS CloudTrail User Guide_.

Make note of the name of the CloudWatch Logs log group that you associate with the CloudTrail trail. You create the
metric filter for that log group in the next step. 3. Create a metric filter. For instructions, see [Create a metric filter for a log group](../../../AmazonCloudWatch/latest/logs/CreateMetricFilterProcedure.md "../../../AmazonCloudWatch/latest/logs/CreateMetricFilterProcedure.md") in the
_Amazon CloudWatch User Guide_. Use the following values:

| Field                          | Value                       |
| ------------------------------ | --------------------------- | --- | ------------------------- | --- | ------------------------- | --- | -------------------------- | --- | --------------------------- |
| Define pattern, Filter pattern | `{($.eventName=CreateTrail) |     | ($.eventName=UpdateTrail) |     | ($.eventName=DeleteTrail) |     | ($.eventName=StartLogging) |     | ($.eventName=StopLogging)}` |
| Metric namespace               | `LogMetrics`                |
| Metric value                   | `1`                         |
| Default value                  | `0`                         |

4. Create an alarm based on the filter. For instructions, see [Create a CloudWatch alarm based on a log group-metric filter](../../../AmazonCloudWatch/latest/monitoring/Alarm-On-Logs.md "../../../AmazonCloudWatch/latest/monitoring/Alarm-On-Logs.md") in the _Amazon CloudWatch User Guide_. Use the following values:

| Field                             | Value         |
| --------------------------------- | ------------- |
| Conditions, Threshold type        | Static        |
| Whenever `your-metric-name` is... | Greater/Equal |
| than...                           | `1`           |

## [CloudWatch.6] Ensure a log metric filter and alarm exist for AWS Management Console authentication failures

**Related requirements:** CIS AWS Foundations Benchmark
v1.2.0/3.6, CIS AWS Foundations Benchmark v1.4.0/4.6, NIST.800-171.r2 3.14.6,
NIST.800-171.r2 3.14.7

**Category:** Detect > Detection services

**Severity:** Low

**Resource type:** `AWS::Logs::MetricFilter`, `AWS::CloudWatch::Alarm`, `AWS::CloudTrail::Trail`, `AWS::SNS::Topic`

**AWS Config rule:** None (custom Security Hub rule)

**Schedule type:** Periodic

**Parameters:** None

You can do real-time monitoring of API calls by directing CloudTrail logs to CloudWatch Logs and
establishing corresponding metric filters and alarms.

CIS recommends that you create a metric filter and alarm for failed console
authentication attempts. Monitoring failed console logins might decrease lead time
to detect an attempt to brute-force a credential, which might provide an indicator,
such as source IP, that you can use in other event correlations.

To run this check, Security Hub uses custom logic to perform the exact audit steps
prescribed for control 4.6 in the [CIS AWS Foundations Benchmark v1.4.0](https://acrobat.adobe.com/link/track?uri=urn:aaid:scds:US:2e5fec5c-5e99-4fb5-b08d-bb46b14754c1#pageNum=1 "https://acrobat.adobe.com/link/track?uri=urn:aaid:scds:US:2e5fec5c-5e99-4fb5-b08d-bb46b14754c1#pageNum=1"). This control fails if the exact
metric filters prescribed by CIS are not used. Additional fields or terms cannot be
added to the metric filters.

###### Note

When Security Hub performs the check for this control, it looks for CloudTrail trails that the current account uses. These trails might be organization trails that belong to another account. Multi-Region trails also might be based in a different Region.

The check results in `FAILED` findings in the following cases:

- No trail is configured.
- The available trails that are in the current Region and that are owned by current account do not meet the control requirements.
  The check results in a control status of `NO_DATA` in the following cases:

- A multi-Region trail is based in a different Region. Security Hub can only generate findings in the Region where the trail is based.
- A multi-Region trail belongs to a different account. Security Hub can only generate findings for the account that owns the trail.

We recommend organization trails to log events from many accounts in an organization. Organization trails are multi-Region
trails by default and can only be managed by the AWS Organizations management account or the CloudTrail delegated administrator account. Using an
organization trail results in a control status of `NO_DATA` for controls evaluated in organization member
accounts. In member accounts, Security Hub only generates findings for member-owned resources. Findings that pertain to organization trails
are generated in the resource owner's account. You can see these findings in your Security Hub delegated administrator account by using cross-Region
aggregation.
For the alarm, the current account must either own the referenced Amazon SNS topic, or must get access to the Amazon SNS topic by calling `ListSubscriptionsByTopic`. Otherwise Security Hub generates `WARNING` findings for the control.

### Remediation

To pass this control, follow these steps to create an Amazon SNS topic, an AWS CloudTrail
trail, a metric filter, and an alarm for the metric filter.

1. Create an Amazon SNS topic. For instructions, see [Getting started with Amazon SNS](../../../sns/latest/dg/sns-getting-started.md#CreateTopic "../../../sns/latest/dg/sns-getting-started.md#CreateTopic") in the
   _Amazon Simple Notification Service Developer Guide_. Create a topic that receives all CIS alarms, and create
   at least one subscription to the topic.
2. Create a CloudTrail trail that applies to all AWS Regions. For instructions, see [Creating a trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.md") in the
   _AWS CloudTrail User Guide_.

Make note of the name of the CloudWatch Logs log group that you associate with the CloudTrail trail. You create the
metric filter for that log group in the next step. 3. Create a metric filter. For instructions, see [Create a metric filter for a log group](../../../AmazonCloudWatch/latest/logs/CreateMetricFilterProcedure.md "../../../AmazonCloudWatch/latest/logs/CreateMetricFilterProcedure.md") in the
_Amazon CloudWatch User Guide_. Use the following values:

| Field                          | Value                                                                      |
| ------------------------------ | -------------------------------------------------------------------------- |
| Define pattern, Filter pattern | `{($.eventName=ConsoleLogin) && ($.errorMessage="Failed authentication")}` |
| Metric namespace               | `LogMetrics`                                                               |
| Metric value                   | `1`                                                                        |
| Default value                  | `0`                                                                        |

4. Create an alarm based on the filter. For instructions, see [Create a CloudWatch alarm based on a log group-metric filter](../../../AmazonCloudWatch/latest/monitoring/Alarm-On-Logs.md "../../../AmazonCloudWatch/latest/monitoring/Alarm-On-Logs.md") in the _Amazon CloudWatch User Guide_. Use the following values:

| Field                             | Value         |
| --------------------------------- | ------------- |
| Conditions, Threshold type        | Static        |
| Whenever `your-metric-name` is... | Greater/Equal |
| than...                           | `1`           |

## [CloudWatch.7] Ensure a log metric filter and alarm exist for disabling or scheduled deletion of customer managed keys

**Related requirements:** CIS AWS Foundations Benchmark
v1.2.0/3.7, CIS AWS Foundations Benchmark v1.4.0/4.7, NIST.800-171.r2 3.13.10,
NIST.800-171.r2 3.13.16, NIST.800-171.r2 3.14.6, NIST.800-171.r2 3.14.7

**Category:** Detect > Detection services

**Severity:** Low

**Resource type:** `AWS::Logs::MetricFilter`, `AWS::CloudWatch::Alarm`, `AWS::CloudTrail::Trail`, `AWS::SNS::Topic`

**AWS Config rule:** None (custom Security Hub rule)

**Schedule type:** Periodic

**Parameters:** None

You can do real-time monitoring of API calls by directing CloudTrail logs to CloudWatch Logs and
establishing corresponding metric filters and alarms.

CIS recommends that you create a metric filter and alarm for customer managed keys that have
changed state to disabled or scheduled deletion. Data encrypted with disabled or
deleted keys is no longer accessible.

To run this check, Security Hub uses custom logic to perform the exact audit steps
prescribed for control 4.7 in the [CIS AWS Foundations Benchmark v1.4.0](https://acrobat.adobe.com/link/track?uri=urn:aaid:scds:US:2e5fec5c-5e99-4fb5-b08d-bb46b14754c1#pageNum=1 "https://acrobat.adobe.com/link/track?uri=urn:aaid:scds:US:2e5fec5c-5e99-4fb5-b08d-bb46b14754c1#pageNum=1"). This control fails if the exact
metric filters prescribed by CIS are not used. Additional fields or terms cannot be
added to the metric filters. The control also fails if
`ExcludeManagementEventSources` contains
`kms.amazonaws.com`.

###### Note

When Security Hub performs the check for this control, it looks for CloudTrail trails that the current account uses. These trails might be organization trails that belong to another account. Multi-Region trails also might be based in a different Region.

The check results in `FAILED` findings in the following cases:

- No trail is configured.
- The available trails that are in the current Region and that are owned by current account do not meet the control requirements.
  The check results in a control status of `NO_DATA` in the following cases:

- A multi-Region trail is based in a different Region. Security Hub can only generate findings in the Region where the trail is based.
- A multi-Region trail belongs to a different account. Security Hub can only generate findings for the account that owns the trail.

We recommend organization trails to log events from many accounts in an organization. Organization trails are multi-Region
trails by default and can only be managed by the AWS Organizations management account or the CloudTrail delegated administrator account. Using an
organization trail results in a control status of `NO_DATA` for controls evaluated in organization member
accounts. In member accounts, Security Hub only generates findings for member-owned resources. Findings that pertain to organization trails
are generated in the resource owner's account. You can see these findings in your Security Hub delegated administrator account by using cross-Region
aggregation.
For the alarm, the current account must either own the referenced Amazon SNS topic, or must get access to the Amazon SNS topic by calling `ListSubscriptionsByTopic`. Otherwise Security Hub generates `WARNING` findings for the control.

### Remediation

To pass this control, follow these steps to create an Amazon SNS topic, an AWS CloudTrail
trail, a metric filter, and an alarm for the metric filter.

1. Create an Amazon SNS topic. For instructions, see [Getting started with Amazon SNS](../../../sns/latest/dg/sns-getting-started.md#CreateTopic "../../../sns/latest/dg/sns-getting-started.md#CreateTopic") in the
   _Amazon Simple Notification Service Developer Guide_. Create a topic that receives all CIS alarms, and create
   at least one subscription to the topic.
2. Create a CloudTrail trail that applies to all AWS Regions. For instructions, see [Creating a trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.md") in the
   _AWS CloudTrail User Guide_.

Make note of the name of the CloudWatch Logs log group that you associate with the CloudTrail trail. You create the
metric filter for that log group in the next step. 3. Create a metric filter. For instructions, see [Create a metric filter for a log group](../../../AmazonCloudWatch/latest/logs/CreateMetricFilterProcedure.md "../../../AmazonCloudWatch/latest/logs/CreateMetricFilterProcedure.md") in the
_Amazon CloudWatch User Guide_. Use the following values:

| Field                          | Value                                                            |
| ------------------------------ | ---------------------------------------------------------------- | --- | ------------------------------------ |
| Define pattern, Filter pattern | `{($.eventSource=kms.amazonaws.com) && (($.eventName=DisableKey) |     | ($.eventName=ScheduleKeyDeletion))}` |
| Metric namespace               | `LogMetrics`                                                     |
| Metric value                   | `1`                                                              |
| Default value                  | `0`                                                              |

4. Create an alarm based on the filter. For instructions, see [Create a CloudWatch alarm based on a log group-metric filter](../../../AmazonCloudWatch/latest/monitoring/Alarm-On-Logs.md "../../../AmazonCloudWatch/latest/monitoring/Alarm-On-Logs.md") in the _Amazon CloudWatch User Guide_. Use the following values:

| Field                             | Value         |
| --------------------------------- | ------------- |
| Conditions, Threshold type        | Static        |
| Whenever `your-metric-name` is... | Greater/Equal |
| than...                           | `1`           |

## [CloudWatch.8] Ensure a log metric filter and alarm exist for S3 bucket policy changes

**Related requirements:** CIS AWS Foundations Benchmark
v1.2.0/3.8, CIS AWS Foundations Benchmark v1.4.0/4.8, NIST.800-171.r2 3.14.6,
NIST.800-171.r2 3.14.7

**Category:** Detect > Detection services

**Severity:** Low

**Resource type:** `AWS::Logs::MetricFilter`, `AWS::CloudWatch::Alarm`, `AWS::CloudTrail::Trail`, `AWS::SNS::Topic`

**AWS Config rule:** None (custom Security Hub rule)

**Schedule type:** Periodic

**Parameters:** None

You can do real-time monitoring of API calls by directing CloudTrail logs to CloudWatch Logs and
establishing corresponding metric filters and alarms.

CIS recommends that you create a metric filter and alarm for changes to S3 bucket
policies. Monitoring these changes might reduce time to detect and correct
permissive policies on sensitive S3 buckets.

To run this check, Security Hub uses custom logic to perform the exact audit steps
prescribed for control 4.8 in the [CIS AWS Foundations Benchmark v1.4.0](https://acrobat.adobe.com/link/track?uri=urn:aaid:scds:US:2e5fec5c-5e99-4fb5-b08d-bb46b14754c1#pageNum=1 "https://acrobat.adobe.com/link/track?uri=urn:aaid:scds:US:2e5fec5c-5e99-4fb5-b08d-bb46b14754c1#pageNum=1"). This control fails if the exact
metric filters prescribed by CIS are not used. Additional fields or terms cannot be
added to the metric filters.

###### Note

When Security Hub performs the check for this control, it looks for CloudTrail trails that the current account uses. These trails might be organization trails that belong to another account. Multi-Region trails also might be based in a different Region.

The check results in `FAILED` findings in the following cases:

- No trail is configured.
- The available trails that are in the current Region and that are owned by current account do not meet the control requirements.
  The check results in a control status of `NO_DATA` in the following cases:

- A multi-Region trail is based in a different Region. Security Hub can only generate findings in the Region where the trail is based.
- A multi-Region trail belongs to a different account. Security Hub can only generate findings for the account that owns the trail.

We recommend organization trails to log events from many accounts in an organization. Organization trails are multi-Region
trails by default and can only be managed by the AWS Organizations management account or the CloudTrail delegated administrator account. Using an
organization trail results in a control status of `NO_DATA` for controls evaluated in organization member
accounts. In member accounts, Security Hub only generates findings for member-owned resources. Findings that pertain to organization trails
are generated in the resource owner's account. You can see these findings in your Security Hub delegated administrator account by using cross-Region
aggregation.
For the alarm, the current account must either own the referenced Amazon SNS topic, or must get access to the Amazon SNS topic by calling `ListSubscriptionsByTopic`. Otherwise Security Hub generates `WARNING` findings for the control.

### Remediation

To pass this control, follow these steps to create an Amazon SNS topic, an AWS CloudTrail
trail, a metric filter, and an alarm for the metric filter.

1. Create an Amazon SNS topic. For instructions, see [Getting started with Amazon SNS](../../../sns/latest/dg/sns-getting-started.md#CreateTopic "../../../sns/latest/dg/sns-getting-started.md#CreateTopic") in the
   _Amazon Simple Notification Service Developer Guide_. Create a topic that receives all CIS alarms, and create
   at least one subscription to the topic.
2. Create a CloudTrail trail that applies to all AWS Regions. For instructions, see [Creating a trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.md") in the
   _AWS CloudTrail User Guide_.

Make note of the name of the CloudWatch Logs log group that you associate with the CloudTrail trail. You create the
metric filter for that log group in the next step. 3. Create a metric filter. For instructions, see [Create a metric filter for a log group](../../../AmazonCloudWatch/latest/logs/CreateMetricFilterProcedure.md "../../../AmazonCloudWatch/latest/logs/CreateMetricFilterProcedure.md") in the
_Amazon CloudWatch User Guide_. Use the following values:

| Field                          | Value                                                             |
| ------------------------------ | ----------------------------------------------------------------- | --- | ----------------------------- | --- | --------------------------- | --- | -------------------------------- | --- | ---------------------------------- | --- | -------------------------------- | --- | ------------------------------ | --- | ----------------------------------- | --- | ---------------------------------------- |
| Define pattern, Filter pattern | `{($.eventSource=s3.amazonaws.com) && (($.eventName=PutBucketAcl) |     | ($.eventName=PutBucketPolicy) |     | ($.eventName=PutBucketCors) |     | ($.eventName=PutBucketLifecycle) |     | ($.eventName=PutBucketReplication) |     | ($.eventName=DeleteBucketPolicy) |     | ($.eventName=DeleteBucketCors) |     | ($.eventName=DeleteBucketLifecycle) |     | ($.eventName=DeleteBucketReplication))}` |
| Metric namespace               | `LogMetrics`                                                      |
| Metric value                   | `1`                                                               |
| Default value                  | `0`                                                               |

4. Create an alarm based on the filter. For instructions, see [Create a CloudWatch alarm based on a log group-metric filter](../../../AmazonCloudWatch/latest/monitoring/Alarm-On-Logs.md "../../../AmazonCloudWatch/latest/monitoring/Alarm-On-Logs.md") in the _Amazon CloudWatch User Guide_. Use the following values:

| Field                             | Value         |
| --------------------------------- | ------------- |
| Conditions, Threshold type        | Static        |
| Whenever `your-metric-name` is... | Greater/Equal |
| than...                           | `1`           |

## [CloudWatch.9] Ensure a log metric filter and alarm exist for AWS Config configuration changes

**Related requirements:** CIS AWS Foundations Benchmark
v1.2.0/3.9, CIS AWS Foundations Benchmark v1.4.0/4.9, NIST.800-171.r2 3.3.8,
NIST.800-171.r2 3.14.6, NIST.800-171.r2 3.14.7

**Category:** Detect > Detection services

**Severity:** Low

**Resource type:** `AWS::Logs::MetricFilter`, `AWS::CloudWatch::Alarm`, `AWS::CloudTrail::Trail`, `AWS::SNS::Topic`

**AWS Config rule:** None (custom Security Hub rule)

**Schedule type:** Periodic

**Parameters:** None

You can do real-time monitoring of API calls by directing CloudTrail logs to CloudWatch Logs and
establishing corresponding metric filters and alarms.

CIS recommends that you create a metric filter and alarm for changes to AWS Config
configuration settings. Monitoring these changes helps ensure sustained visibility
of configuration items in the account.

To run this check, Security Hub uses custom logic to perform the exact audit steps
prescribed for control 4.9 in the [CIS AWS Foundations Benchmark v1.4.0](https://acrobat.adobe.com/link/track?uri=urn:aaid:scds:US:2e5fec5c-5e99-4fb5-b08d-bb46b14754c1#pageNum=1 "https://acrobat.adobe.com/link/track?uri=urn:aaid:scds:US:2e5fec5c-5e99-4fb5-b08d-bb46b14754c1#pageNum=1"). This control fails if the exact
metric filters prescribed by CIS are not used. Additional fields or terms cannot be
added to the metric filters.

###### Note

When Security Hub performs the check for this control, it looks for CloudTrail trails that the current account uses. These trails might be organization trails that belong to another account. Multi-Region trails also might be based in a different Region.

The check results in `FAILED` findings in the following cases:

- No trail is configured.
- The available trails that are in the current Region and that are owned by current account do not meet the control requirements.
  The check results in a control status of `NO_DATA` in the following cases:

- A multi-Region trail is based in a different Region. Security Hub can only generate findings in the Region where the trail is based.
- A multi-Region trail belongs to a different account. Security Hub can only generate findings for the account that owns the trail.

We recommend organization trails to log events from many accounts in an organization. Organization trails are multi-Region
trails by default and can only be managed by the AWS Organizations management account or the CloudTrail delegated administrator account. Using an
organization trail results in a control status of `NO_DATA` for controls evaluated in organization member
accounts. In member accounts, Security Hub only generates findings for member-owned resources. Findings that pertain to organization trails
are generated in the resource owner's account. You can see these findings in your Security Hub delegated administrator account by using cross-Region
aggregation.
For the alarm, the current account must either own the referenced Amazon SNS topic, or must get access to the Amazon SNS topic by calling `ListSubscriptionsByTopic`. Otherwise Security Hub generates `WARNING` findings for the control.

### Remediation

To pass this control, follow these steps to create an Amazon SNS topic, an AWS CloudTrail
trail, a metric filter, and an alarm for the metric filter.

1. Create an Amazon SNS topic. For instructions, see [Getting started with Amazon SNS](../../../sns/latest/dg/sns-getting-started.md#CreateTopic "../../../sns/latest/dg/sns-getting-started.md#CreateTopic") in the
   _Amazon Simple Notification Service Developer Guide_. Create a topic that receives all CIS alarms, and create
   at least one subscription to the topic.
2. Create a CloudTrail trail that applies to all AWS Regions. For instructions, see [Creating a trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.md") in the
   _AWS CloudTrail User Guide_.

Make note of the name of the CloudWatch Logs log group that you associate with the CloudTrail trail. You create the
metric filter for that log group in the next step. 3. Create a metric filter. For instructions, see [Create a metric filter for a log group](../../../AmazonCloudWatch/latest/logs/CreateMetricFilterProcedure.md "../../../AmazonCloudWatch/latest/logs/CreateMetricFilterProcedure.md") in the
_Amazon CloudWatch User Guide_. Use the following values:

| Field                          | Value                                                                              |
| ------------------------------ | ---------------------------------------------------------------------------------- | --- | ----------------------------------- | --- | -------------------------------- | --- | ----------------------------------------- |
| Define pattern, Filter pattern | `{($.eventSource=config.amazonaws.com) && (($.eventName=StopConfigurationRecorder) |     | ($.eventName=DeleteDeliveryChannel) |     | ($.eventName=PutDeliveryChannel) |     | ($.eventName=PutConfigurationRecorder))}` |
| Metric namespace               | `LogMetrics`                                                                       |
| Metric value                   | `1`                                                                                |
| Default value                  | `0`                                                                                |

4. Create an alarm based on the filter. For instructions, see [Create a CloudWatch alarm based on a log group-metric filter](../../../AmazonCloudWatch/latest/monitoring/Alarm-On-Logs.md "../../../AmazonCloudWatch/latest/monitoring/Alarm-On-Logs.md") in the _Amazon CloudWatch User Guide_. Use the following values:

| Field                             | Value         |
| --------------------------------- | ------------- |
| Conditions, Threshold type        | Static        |
| Whenever `your-metric-name` is... | Greater/Equal |
| than...                           | `1`           |

## [CloudWatch.10] Ensure a log metric filter and alarm exist for security group changes

**Related requirements:** CIS AWS Foundations Benchmark
v1.2.0/3.10, CIS AWS Foundations Benchmark v1.4.0/4.10, NIST.800-171.r2 3.14.6,
NIST.800-171.r2 3.14.7

**Category:** Detect > Detection services

**Severity:** Low

**Resource type:** `AWS::Logs::MetricFilter`, `AWS::CloudWatch::Alarm`, `AWS::CloudTrail::Trail`, `AWS::SNS::Topic`

**AWS Config rule:** None (custom Security Hub rule)

**Schedule type:** Periodic

**Parameters:** None

You can do real-time monitoring of API calls by directing CloudTrail logs to CloudWatch Logs and
establishing corresponding metric filters and alarms. Security groups are a stateful
packet filter that controls ingress and egress traffic in a VPC.

CIS recommends that you create a metric filter and alarm for changes to security
groups. Monitoring these changes helps ensure that resources and services aren't
unintentionally exposed.

To run this check, Security Hub uses custom logic to perform the exact audit steps
prescribed for control 4.10 in the [CIS AWS Foundations Benchmark v1.4.0](https://acrobat.adobe.com/link/track?uri=urn:aaid:scds:US:2e5fec5c-5e99-4fb5-b08d-bb46b14754c1#pageNum=1 "https://acrobat.adobe.com/link/track?uri=urn:aaid:scds:US:2e5fec5c-5e99-4fb5-b08d-bb46b14754c1#pageNum=1"). This control fails if the exact
metric filters prescribed by CIS are not used. Additional fields or terms cannot be
added to the metric filters.

###### Note

When Security Hub performs the check for this control, it looks for CloudTrail trails that the current account uses. These trails might be organization trails that belong to another account. Multi-Region trails also might be based in a different Region.

The check results in `FAILED` findings in the following cases:

- No trail is configured.
- The available trails that are in the current Region and that are owned by current account do not meet the control requirements.
  The check results in a control status of `NO_DATA` in the following cases:

- A multi-Region trail is based in a different Region. Security Hub can only generate findings in the Region where the trail is based.
- A multi-Region trail belongs to a different account. Security Hub can only generate findings for the account that owns the trail.

We recommend organization trails to log events from many accounts in an organization. Organization trails are multi-Region
trails by default and can only be managed by the AWS Organizations management account or the CloudTrail delegated administrator account. Using an
organization trail results in a control status of `NO_DATA` for controls evaluated in organization member
accounts. In member accounts, Security Hub only generates findings for member-owned resources. Findings that pertain to organization trails
are generated in the resource owner's account. You can see these findings in your Security Hub delegated administrator account by using cross-Region
aggregation.
For the alarm, the current account must either own the referenced Amazon SNS topic, or must get access to the Amazon SNS topic by calling `ListSubscriptionsByTopic`. Otherwise Security Hub generates `WARNING` findings for the control.

### Remediation

To pass this control, follow these steps to create an Amazon SNS topic, an AWS CloudTrail
trail, a metric filter, and an alarm for the metric filter.

1. Create an Amazon SNS topic. For instructions, see [Getting started with Amazon SNS](../../../sns/latest/dg/sns-getting-started.md#CreateTopic "../../../sns/latest/dg/sns-getting-started.md#CreateTopic") in the
   _Amazon Simple Notification Service Developer Guide_. Create a topic that receives all CIS alarms, and create
   at least one subscription to the topic.
2. Create a CloudTrail trail that applies to all AWS Regions. For instructions, see [Creating a trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.md") in the
   _AWS CloudTrail User Guide_.

Make note of the name of the CloudWatch Logs log group that you associate with the CloudTrail trail. You create the
metric filter for that log group in the next step. 3. Create a metric filter. For instructions, see [Create a metric filter for a log group](../../../AmazonCloudWatch/latest/logs/CreateMetricFilterProcedure.md "../../../AmazonCloudWatch/latest/logs/CreateMetricFilterProcedure.md") in the
_Amazon CloudWatch User Guide_. Use the following values:

| Field                          | Value                                         |
| ------------------------------ | --------------------------------------------- | --- | ------------------------------------------ | --- | ---------------------------------------- | --- | --------------------------------------- | --- | --------------------------------- | --- | ----------------------------------- |
| Define pattern, Filter pattern | `{($.eventName=AuthorizeSecurityGroupIngress) |     | ($.eventName=AuthorizeSecurityGroupEgress) |     | ($.eventName=RevokeSecurityGroupIngress) |     | ($.eventName=RevokeSecurityGroupEgress) |     | ($.eventName=CreateSecurityGroup) |     | ($.eventName=DeleteSecurityGroup)}` |
| Metric namespace               | `LogMetrics`                                  |
| Metric value                   | `1`                                           |
| Default value                  | `0`                                           |

4. Create an alarm based on the filter. For instructions, see [Create a CloudWatch alarm based on a log group-metric filter](../../../AmazonCloudWatch/latest/monitoring/Alarm-On-Logs.md "../../../AmazonCloudWatch/latest/monitoring/Alarm-On-Logs.md") in the _Amazon CloudWatch User Guide_. Use the following values:

| Field                             | Value         |
| --------------------------------- | ------------- |
| Conditions, Threshold type        | Static        |
| Whenever `your-metric-name` is... | Greater/Equal |
| than...                           | `1`           |

## [CloudWatch.11] Ensure a log metric filter and alarm exist for changes to Network Access Control Lists (NACL)

**Related requirements:** CIS AWS Foundations Benchmark
v1.2.0/3.11, CIS AWS Foundations Benchmark v1.4.0/4.11, NIST.800-171.r2 3.14.6,
NIST.800-171.r2 3.14.7

**Category:** Detect > Detection services

**Severity:** Low

**Resource type:** `AWS::Logs::MetricFilter`, `AWS::CloudWatch::Alarm`, `AWS::CloudTrail::Trail`, `AWS::SNS::Topic`

**AWS Config rule:** None (custom Security Hub rule)

**Schedule type:** Periodic

**Parameters:** None

You can do real-time monitoring of API calls by directing CloudTrail logs to CloudWatch Logs and
establishing corresponding metric filters and alarms. NACLs are used as a stateless
packet filter to control ingress and egress traffic for subnets in a VPC.

CIS recommends that you create a metric filter and alarm for changes to NACLs.
Monitoring these changes helps ensure that AWS resources and services aren't
unintentionally exposed.

To run this check, Security Hub uses custom logic to perform the exact audit steps
prescribed for control 4.11 in the [CIS AWS Foundations Benchmark v1.4.0](https://acrobat.adobe.com/link/track?uri=urn:aaid:scds:US:2e5fec5c-5e99-4fb5-b08d-bb46b14754c1#pageNum=1 "https://acrobat.adobe.com/link/track?uri=urn:aaid:scds:US:2e5fec5c-5e99-4fb5-b08d-bb46b14754c1#pageNum=1"). This control fails if the exact
metric filters prescribed by CIS are not used. Additional fields or terms cannot be
added to the metric filters.

###### Note

When Security Hub performs the check for this control, it looks for CloudTrail trails that the current account uses. These trails might be organization trails that belong to another account. Multi-Region trails also might be based in a different Region.

The check results in `FAILED` findings in the following cases:

- No trail is configured.
- The available trails that are in the current Region and that are owned by current account do not meet the control requirements.
  The check results in a control status of `NO_DATA` in the following cases:

- A multi-Region trail is based in a different Region. Security Hub can only generate findings in the Region where the trail is based.
- A multi-Region trail belongs to a different account. Security Hub can only generate findings for the account that owns the trail.

We recommend organization trails to log events from many accounts in an organization. Organization trails are multi-Region
trails by default and can only be managed by the AWS Organizations management account or the CloudTrail delegated administrator account. Using an
organization trail results in a control status of `NO_DATA` for controls evaluated in organization member
accounts. In member accounts, Security Hub only generates findings for member-owned resources. Findings that pertain to organization trails
are generated in the resource owner's account. You can see these findings in your Security Hub delegated administrator account by using cross-Region
aggregation.
For the alarm, the current account must either own the referenced Amazon SNS topic, or must get access to the Amazon SNS topic by calling `ListSubscriptionsByTopic`. Otherwise Security Hub generates `WARNING` findings for the control.

### Remediation

To pass this control, follow these steps to create an Amazon SNS topic, an AWS CloudTrail
trail, a metric filter, and an alarm for the metric filter.

1. Create an Amazon SNS topic. For instructions, see [Getting started with Amazon SNS](../../../sns/latest/dg/sns-getting-started.md#CreateTopic "../../../sns/latest/dg/sns-getting-started.md#CreateTopic") in the
   _Amazon Simple Notification Service Developer Guide_. Create a topic that receives all CIS alarms, and create
   at least one subscription to the topic.
2. Create a CloudTrail trail that applies to all AWS Regions. For instructions, see [Creating a trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.md") in the
   _AWS CloudTrail User Guide_.

Make note of the name of the CloudWatch Logs log group that you associate with the CloudTrail trail. You create the
metric filter for that log group in the next step. 3. Create a metric filter. For instructions, see [Create a metric filter for a log group](../../../AmazonCloudWatch/latest/logs/CreateMetricFilterProcedure.md "../../../AmazonCloudWatch/latest/logs/CreateMetricFilterProcedure.md") in the
_Amazon CloudWatch User Guide_. Use the following values:

| Field                          | Value                            |
| ------------------------------ | -------------------------------- | --- | ----------------------------------- | --- | ------------------------------ | --- | ----------------------------------- | --- | ------------------------------------ | --- | -------------------------------------------- |
| Define pattern, Filter pattern | `{($.eventName=CreateNetworkAcl) |     | ($.eventName=CreateNetworkAclEntry) |     | ($.eventName=DeleteNetworkAcl) |     | ($.eventName=DeleteNetworkAclEntry) |     | ($.eventName=ReplaceNetworkAclEntry) |     | ($.eventName=ReplaceNetworkAclAssociation)}` |
| Metric namespace               | `LogMetrics`                     |
| Metric value                   | `1`                              |
| Default value                  | `0`                              |

4. Create an alarm based on the filter. For instructions, see [Create a CloudWatch alarm based on a log group-metric filter](../../../AmazonCloudWatch/latest/monitoring/Alarm-On-Logs.md "../../../AmazonCloudWatch/latest/monitoring/Alarm-On-Logs.md") in the _Amazon CloudWatch User Guide_. Use the following values:

| Field                             | Value         |
| --------------------------------- | ------------- |
| Conditions, Threshold type        | Static        |
| Whenever `your-metric-name` is... | Greater/Equal |
| than...                           | `1`           |

## [CloudWatch.12] Ensure a log metric filter and alarm exist for changes to network gateways

**Related requirements:** CIS AWS Foundations Benchmark
v1.2.0/3.12, CIS AWS Foundations Benchmark v1.4.0/4.12, NIST.800-171.r2 3.3.1,
NIST.800-171.r2 3.13.1

**Category:** Detect > Detection services

**Severity:** Low

**Resource type:** `AWS::Logs::MetricFilter`, `AWS::CloudWatch::Alarm`, `AWS::CloudTrail::Trail`, `AWS::SNS::Topic`

**AWS Config rule:** None (custom Security Hub rule)

**Schedule type:** Periodic

**Parameters:** None

You can do real-time monitoring of API calls by directing CloudTrail logs to CloudWatch Logs and
establishing corresponding metric filters and alarms. Network gateways are required
to send and receive traffic to a destination outside a VPC.

CIS recommends that you create a metric filter and alarm for changes to network
gateways. Monitoring these changes helps ensure that all ingress and egress traffic
traverses the VPC border via a controlled path.

To run this check, Security Hub uses custom logic to perform the exact audit steps
prescribed for control 4.12 in the [CIS AWS Foundations Benchmark v1.2](https://acrobat.adobe.com/link/track?uri=urn:aaid:scds:US:2e5fec5c-5e99-4fb5-b08d-bb46b14754c1#pageNum=1 "https://acrobat.adobe.com/link/track?uri=urn:aaid:scds:US:2e5fec5c-5e99-4fb5-b08d-bb46b14754c1#pageNum=1"). This control fails if the exact
metric filters prescribed by CIS are not used. Additional fields or terms cannot be
added to the metric filters.

###### Note

When Security Hub performs the check for this control, it looks for CloudTrail trails that the current account uses. These trails might be organization trails that belong to another account. Multi-Region trails also might be based in a different Region.

The check results in `FAILED` findings in the following cases:

- No trail is configured.
- The available trails that are in the current Region and that are owned by current account do not meet the control requirements.
  The check results in a control status of `NO_DATA` in the following cases:

- A multi-Region trail is based in a different Region. Security Hub can only generate findings in the Region where the trail is based.
- A multi-Region trail belongs to a different account. Security Hub can only generate findings for the account that owns the trail.

We recommend organization trails to log events from many accounts in an organization. Organization trails are multi-Region
trails by default and can only be managed by the AWS Organizations management account or the CloudTrail delegated administrator account. Using an
organization trail results in a control status of `NO_DATA` for controls evaluated in organization member
accounts. In member accounts, Security Hub only generates findings for member-owned resources. Findings that pertain to organization trails
are generated in the resource owner's account. You can see these findings in your Security Hub delegated administrator account by using cross-Region
aggregation.
For the alarm, the current account must either own the referenced Amazon SNS topic, or must get access to the Amazon SNS topic by calling `ListSubscriptionsByTopic`. Otherwise Security Hub generates `WARNING` findings for the control.

### Remediation

To pass this control, follow these steps to create an Amazon SNS topic, an AWS CloudTrail
trail, a metric filter, and an alarm for the metric filter.

1. Create an Amazon SNS topic. For instructions, see [Getting started with Amazon SNS](../../../sns/latest/dg/sns-getting-started.md#CreateTopic "../../../sns/latest/dg/sns-getting-started.md#CreateTopic") in the
   _Amazon Simple Notification Service Developer Guide_. Create a topic that receives all CIS alarms, and create
   at least one subscription to the topic.
2. Create a CloudTrail trail that applies to all AWS Regions. For instructions, see [Creating a trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.md") in the
   _AWS CloudTrail User Guide_.

Make note of the name of the CloudWatch Logs log group that you associate with the CloudTrail trail. You create the
metric filter for that log group in the next step. 3. Create a metric filter. For instructions, see [Create a metric filter for a log group](../../../AmazonCloudWatch/latest/logs/CreateMetricFilterProcedure.md "../../../AmazonCloudWatch/latest/logs/CreateMetricFilterProcedure.md") in the
_Amazon CloudWatch User Guide_. Use the following values:

| Field                          | Value                                 |
| ------------------------------ | ------------------------------------- | --- | ----------------------------------- | --- | ----------------------------------- | --- | ----------------------------------- | --- | ----------------------------------- | --- | ------------------------------------- |
| Define pattern, Filter pattern | `{($.eventName=CreateCustomerGateway) |     | ($.eventName=DeleteCustomerGateway) |     | ($.eventName=AttachInternetGateway) |     | ($.eventName=CreateInternetGateway) |     | ($.eventName=DeleteInternetGateway) |     | ($.eventName=DetachInternetGateway)}` |
| Metric namespace               | `LogMetrics`                          |
| Metric value                   | `1`                                   |
| Default value                  | `0`                                   |

4. Create an alarm based on the filter. For instructions, see [Create a CloudWatch alarm based on a log group-metric filter](../../../AmazonCloudWatch/latest/monitoring/Alarm-On-Logs.md "../../../AmazonCloudWatch/latest/monitoring/Alarm-On-Logs.md") in the _Amazon CloudWatch User Guide_. Use the following values:

| Field                             | Value         |
| --------------------------------- | ------------- |
| Conditions, Threshold type        | Static        |
| Whenever `your-metric-name` is... | Greater/Equal |
| than...                           | `1`           |

## [CloudWatch.13] Ensure a log metric filter and alarm exist for route table changes

**Related requirements:** CIS AWS Foundations Benchmark
v1.2.0/3.13, CIS AWS Foundations Benchmark v1.4.0/4.13, NIST.800-171.r2 3.3.1,
NIST.800-171.r2 3.13.1, NIST.800-171.r2 3.14.6, NIST.800-171.r2 3.14.7

**Category:** Detect > Detection services

**Severity:** Low

**Resource type:** `AWS::Logs::MetricFilter`, `AWS::CloudWatch::Alarm`, `AWS::CloudTrail::Trail`, `AWS::SNS::Topic`

**AWS Config rule:** None (custom Security Hub rule)

**Schedule type:** Periodic

**Parameters:** None

This control checks whether you monitor API calls in real time by directing CloudTrail logs to CloudWatch Logs and
establishing corresponding metric filters and alarms. Routing tables route network
traffic between subnets and to network gateways.

CIS recommends that you create a metric filter and alarm for changes to route
tables. Monitoring these changes helps ensure that all VPC traffic flows through an
expected path.

###### Note

When Security Hub performs the check for this control, it looks for CloudTrail trails that the current account uses. These trails might be organization trails that belong to another account. Multi-Region trails also might be based in a different Region.

The check results in `FAILED` findings in the following cases:

- No trail is configured.
- The available trails that are in the current Region and that are owned by current account do not meet the control requirements.
  The check results in a control status of `NO_DATA` in the following cases:

- A multi-Region trail is based in a different Region. Security Hub can only generate findings in the Region where the trail is based.
- A multi-Region trail belongs to a different account. Security Hub can only generate findings for the account that owns the trail.

We recommend organization trails to log events from many accounts in an organization. Organization trails are multi-Region
trails by default and can only be managed by the AWS Organizations management account or the CloudTrail delegated administrator account. Using an
organization trail results in a control status of `NO_DATA` for controls evaluated in organization member
accounts. In member accounts, Security Hub only generates findings for member-owned resources. Findings that pertain to organization trails
are generated in the resource owner's account. You can see these findings in your Security Hub delegated administrator account by using cross-Region
aggregation.
For the alarm, the current account must either own the referenced Amazon SNS topic, or must get access to the Amazon SNS topic by calling `ListSubscriptionsByTopic`. Otherwise Security Hub generates `WARNING` findings for the control.

### Remediation

###### Note

Our recommended filter pattern in these remediation steps differs from the filter pattern in the CIS guidance. Our recommended filters
target only events coming from Amazon Elastic Compute Cloud (EC2) API calls.

To pass this control, follow these steps to create an Amazon SNS topic, an AWS CloudTrail
trail, a metric filter, and an alarm for the metric filter.

1. Create an Amazon SNS topic. For instructions, see [Getting started with Amazon SNS](../../../sns/latest/dg/sns-getting-started.md#CreateTopic "../../../sns/latest/dg/sns-getting-started.md#CreateTopic") in the
   _Amazon Simple Notification Service Developer Guide_. Create a topic that receives all CIS alarms, and create
   at least one subscription to the topic.
2. Create a CloudTrail trail that applies to all AWS Regions. For instructions, see [Creating a trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.md") in the
   _AWS CloudTrail User Guide_.

Make note of the name of the CloudWatch Logs log group that you associate with the CloudTrail trail. You create the
metric filter for that log group in the next step. 3. Create a metric filter. For instructions, see [Create a metric filter for a log group](../../../AmazonCloudWatch/latest/logs/CreateMetricFilterProcedure.md "../../../AmazonCloudWatch/latest/logs/CreateMetricFilterProcedure.md") in the
_Amazon CloudWatch User Guide_. Use the following values:

| Field                          | Value                                                             |
| ------------------------------ | ----------------------------------------------------------------- | --- | ------------------------------ | --- | -------------------------- | --- | ------------------------------------------ | --- | ------------------------------ | --- | ------------------------- | --- | --------------------------------------- |
| Define pattern, Filter pattern | `{($.eventSource=ec2.amazonaws.com) && (($.eventName=CreateRoute) |     | ($.eventName=CreateRouteTable) |     | ($.eventName=ReplaceRoute) |     | ($.eventName=ReplaceRouteTableAssociation) |     | ($.eventName=DeleteRouteTable) |     | ($.eventName=DeleteRoute) |     | ($.eventName=DisassociateRouteTable))}` |
| Metric namespace               | `LogMetrics`                                                      |
| Metric value                   | `1`                                                               |
| Default value                  | `0`                                                               |

4. Create an alarm based on the filter. For instructions, see [Create a CloudWatch alarm based on a log group-metric filter](../../../AmazonCloudWatch/latest/monitoring/Alarm-On-Logs.md "../../../AmazonCloudWatch/latest/monitoring/Alarm-On-Logs.md") in the _Amazon CloudWatch User Guide_. Use the following values:

| Field                             | Value         |
| --------------------------------- | ------------- |
| Conditions, Threshold type        | Static        |
| Whenever `your-metric-name` is... | Greater/Equal |
| than...                           | `1`           |

## [CloudWatch.14] Ensure a log metric filter and alarm exist for VPC changes

**Related requirements:** CIS AWS Foundations Benchmark
v1.2.0/3.14, CIS AWS Foundations Benchmark v1.4.0/4.14, NIST.800-171.r2 3.3.1,
NIST.800-171.r2 3.13.1, NIST.800-171.r2 3.14.6, NIST.800-171.r2 3.14.7

**Category:** Detect > Detection services

**Severity:** Low

**Resource type:** `AWS::Logs::MetricFilter`, `AWS::CloudWatch::Alarm`, `AWS::CloudTrail::Trail`, `AWS::SNS::Topic`

**AWS Config rule:** None (custom Security Hub rule)

**Schedule type:** Periodic

**Parameters:** None

You can do real-time monitoring of API calls by directing CloudTrail logs to CloudWatch Logs and
establishing corresponding metric filters and alarms. You can have more than one VPC
in an account, and you can create a peer connection between two VPCs, enabling
network traffic to route between VPCs.

CIS recommends that you create a metric filter and alarm for changes to VPCs.
Monitoring these changes helps ensure that authentication and authorization controls
remain intact.

To run this check, Security Hub uses custom logic to perform the exact audit steps
prescribed for control 4.14 in the [CIS AWS Foundations Benchmark v1.4.0](https://acrobat.adobe.com/link/track?uri=urn:aaid:scds:US:2e5fec5c-5e99-4fb5-b08d-bb46b14754c1#pageNum=1 "https://acrobat.adobe.com/link/track?uri=urn:aaid:scds:US:2e5fec5c-5e99-4fb5-b08d-bb46b14754c1#pageNum=1"). This control fails if the exact
metric filters prescribed by CIS are not used. Additional fields or terms cannot be
added to the metric filters.

###### Note

When Security Hub performs the check for this control, it looks for CloudTrail trails that the current account uses. These trails might be organization trails that belong to another account. Multi-Region trails also might be based in a different Region.

The check results in `FAILED` findings in the following cases:

- No trail is configured.
- The available trails that are in the current Region and that are owned by current account do not meet the control requirements.
  The check results in a control status of `NO_DATA` in the following cases:

- A multi-Region trail is based in a different Region. Security Hub can only generate findings in the Region where the trail is based.
- A multi-Region trail belongs to a different account. Security Hub can only generate findings for the account that owns the trail.

We recommend organization trails to log events from many accounts in an organization. Organization trails are multi-Region
trails by default and can only be managed by the AWS Organizations management account or the CloudTrail delegated administrator account. Using an
organization trail results in a control status of `NO_DATA` for controls evaluated in organization member
accounts. In member accounts, Security Hub only generates findings for member-owned resources. Findings that pertain to organization trails
are generated in the resource owner's account. You can see these findings in your Security Hub delegated administrator account by using cross-Region
aggregation.
For the alarm, the current account must either own the referenced Amazon SNS topic, or must get access to the Amazon SNS topic by calling `ListSubscriptionsByTopic`. Otherwise Security Hub generates `WARNING` findings for the control.

### Remediation

To pass this control, follow these steps to create an Amazon SNS topic, an AWS CloudTrail
trail, a metric filter, and an alarm for the metric filter.

1. Create an Amazon SNS topic. For instructions, see [Getting started with Amazon SNS](../../../sns/latest/dg/sns-getting-started.md#CreateTopic "../../../sns/latest/dg/sns-getting-started.md#CreateTopic") in the
   _Amazon Simple Notification Service Developer Guide_. Create a topic that receives all CIS alarms, and create
   at least one subscription to the topic.
2. Create a CloudTrail trail that applies to all AWS Regions. For instructions, see [Creating a trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.md") in the
   _AWS CloudTrail User Guide_.

Make note of the name of the CloudWatch Logs log group that you associate with the CloudTrail trail. You create the
metric filter for that log group in the next step. 3. Create a metric filter. For instructions, see [Create a metric filter for a log group](../../../AmazonCloudWatch/latest/logs/CreateMetricFilterProcedure.md "../../../AmazonCloudWatch/latest/logs/CreateMetricFilterProcedure.md") in the
_Amazon CloudWatch User Guide_. Use the following values:

| Field                          | Value                     |
| ------------------------------ | ------------------------- | --- | ----------------------- | --- | -------------------------------- | --- | ---------------------------------------- | --- | ---------------------------------------- | --- | ---------------------------------------- | --- | ---------------------------------------- | --- | ---------------------------------- | --- | ---------------------------------- | --- | ----------------------------------- | --- | ------------------------------------ |
| Define pattern, Filter pattern | `{($.eventName=CreateVpc) |     | ($.eventName=DeleteVpc) |     | ($.eventName=ModifyVpcAttribute) |     | ($.eventName=AcceptVpcPeeringConnection) |     | ($.eventName=CreateVpcPeeringConnection) |     | ($.eventName=DeleteVpcPeeringConnection) |     | ($.eventName=RejectVpcPeeringConnection) |     | ($.eventName=AttachClassicLinkVpc) |     | ($.eventName=DetachClassicLinkVpc) |     | ($.eventName=DisableVpcClassicLink) |     | ($.eventName=EnableVpcClassicLink)}` |
| Metric namespace               | `LogMetrics`              |
| Metric value                   | `1`                       |
| Default value                  | `0`                       |

4. Create an alarm based on the filter. For instructions, see [Create a CloudWatch alarm based on a log group-metric filter](../../../AmazonCloudWatch/latest/monitoring/Alarm-On-Logs.md "../../../AmazonCloudWatch/latest/monitoring/Alarm-On-Logs.md") in the _Amazon CloudWatch User Guide_. Use the following values:

| Field                             | Value         |
| --------------------------------- | ------------- |
| Conditions, Threshold type        | Static        |
| Whenever `your-metric-name` is... | Greater/Equal |
| than...                           | `1`           |

## [CloudWatch.15] CloudWatch alarms should have specified actions configured

**Related requirements:** NIST.800-53.r5 AU-6(1),
NIST.800-53.r5 AU-6(5), NIST.800-53.r5 CA-7, NIST.800-53.r5 IR-4(1), NIST.800-53.r5
IR-4(5), NIST.800-53.r5 SI-2, NIST.800-53.r5 SI-20, NIST.800-53.r5 SI-4(12),
NIST.800-53.r5 SI-4(5), NIST.800-171.r2 3.3.4, NIST.800-171.r2 3.14.6

**Category:** Detect > Detection services

**Severity:** High

**Resource type:**
`AWS::CloudWatch::Alarm`

**AWS Config rule:**
[`cloudwatch-alarm-action-check`](../../../config/latest/developerguide/cloudwatch-alarm-action-check.md "../../../config/latest/developerguide/cloudwatch-alarm-action-check.md")

**Schedule type:** Change triggered

**Parameters:**

| Parameter                        | Description                                                                                                                                                   | Type    | Allowed custom values | Security Hub default value |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | --------------------- | -------------------------- |
| `alarmActionRequired`            | The control produces a `PASSED` finding if the parameter is set to `true`<br>and the alarm has an action when the alarm state changes to `ALARM`.             | Boolean | Not customizable      | `true`                     |
| `insufficientDataActionRequired` | The control produces a `PASSED` finding if the parameter is set to `true`<br>and the alarm has an action when the alarm state changes to `INSUFFICIENT_DATA`. | Boolean | `true` or `false`     | `false`                    |
| `okActionRequired`               | The control produces a `PASSED` finding if the parameter is set to `true`<br>and the alarm has an action when the alarm state changes to `OK`.                | Boolean | `true` or `false`     | `false`                    |

This control checks whether an Amazon CloudWatch alarm has at least one action configured for the `ALARM` state. The control
fails if the alarm doesn't have an action configured for the `ALARM` state. Optionally, you can include custom
parameter values to also require alarm actions for the `INSUFFICIENT_DATA` or `OK` states.

###### Note

Security Hub evaluates this control based on CloudWatch metric alarms. Metric alarms may be part of composite alarms
that have the specified actions configured. The control generates `FAILED` findings in the following cases:

- The specified actions aren't configured for a metric alarm.
- The metric alarm is part of a composite alarm that has the specified actions configured.

This control focuses on whether a CloudWatch alarm has an alarm action configured, whereas
[CloudWatch.17](#cloudwatch-17 "#cloudwatch-17") focuses on the activation status of a CloudWatch alarm action.

We recommend CloudWatch alarm actions to automatically alert you when a monitored
metric is outside the defined threshold. Monitoring alarms help you identify unusual
activities and quickly respond to security and operational issues when an alarm goes into a specific state.
The most common type of alarm action is to notify one or more users by sending a message
to an Amazon Simple Notification Service (Amazon SNS) topic.

### Remediation

For information about actions supported by CloudWatch alarms, see [Alarm actions](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md#alarms-and-actions "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md#alarms-and-actions") in the _Amazon CloudWatch User Guide_.

## [CloudWatch.16] CloudWatch log groups should be retained for a specified time period

**Category:** Identify > Logging

**Related requirements:** NIST.800-53.r5 AU-10,
NIST.800-53.r5 AU-11,
NIST.800-53.r5 AU-6(3),
NIST.800-53.r5 AU-6(4),
NIST.800-53.r5 CA-7,
NIST.800-53.r5 SI-12

**Severity:** Medium

**Resource type:**
`AWS::Logs::LogGroup`

**AWS Config rule:**
[`cw-loggroup-retention-period-check`](../../../config/latest/developerguide/cw-loggroup-retention-period-check.md "../../../config/latest/developerguide/cw-loggroup-retention-period-check.md")

**Schedule type:** Periodic

**Parameters:**

| Parameter          | Description                                                | Type | Allowed custom values            | Security Hub default value |
| ------------------ | ---------------------------------------------------------- | ---- | -------------------------------- | -------------------------- |
| `minRetentionTime` | Minimum retention period in days for CloudWatch log groups | Enum | `365, 400, 545, 731, 1827, 3653` | `365`                      |

This control checks whether an Amazon CloudWatch log group has a retention period of at least the specified number of days.
The control fails if the retention period is less than the specified number. Unless you provide a custom parameter value for the
retention period, Security Hub uses a default value of 365 days.

CloudWatch Logs centralize logs from all of your systems, applications, and AWS services in a single, highly scalable service.
You can use CloudWatch Logs to monitor, store, and access your log files from Amazon Elastic Compute Cloud (EC2) instances, AWS CloudTrail, Amazon Route 53, and other sources.
Retaining your logs for at least 1 year can help you comply with log retention standards.

### Remediation

To configure log retention settings, see [Change log data retention in CloudWatch Logs](../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md#SettingLogRetention "../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md#SettingLogRetention") in the _Amazon CloudWatch User Guide_.

## [CloudWatch.17] CloudWatch alarm actions should be activated

**Category:** Detect > Detection services

**Related requirements:** NIST.800-53.r5 AU-6(1),
NIST.800-53.r5 AU-6(5),
NIST.800-53.r5 CA-7,
NIST.800-53.r5 SI-2,
NIST.800-53.r5 SI-4(12)

**Severity:** High

**Resource type:**
`AWS::CloudWatch::Alarm`

**AWS Config rule:**
[`cloudwatch-alarm-action-enabled-check`](../../../config/latest/developerguide/cloudwatch-alarm-action-enabled-check.md "../../../config/latest/developerguide/cloudwatch-alarm-action-enabled-check.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether CloudWatch alarm actions are activated (`ActionEnabled` should be set to true). The control fails if the alarm action for a CloudWatch alarm is deactivated.

###### Note

Security Hub evaluates this control based on CloudWatch metric alarms. Metric alarms may be part of composite alarms
that have the alarm actions activated. The control generates `FAILED` findings in the following cases:

- The specified actions aren't configured for a metric alarm.
- The metric alarm is part of a composite alarm that has alarm actions activated.

This control focuses on the activation status of a CloudWatch alarm action, whereas [CloudWatch.15](#cloudwatch-15 "#cloudwatch-15")
focuses on whether any `ALARM` action is configured in a CloudWatch alarm.

Alarm actions automatically alert you when a monitored metric is outside the defined
threshold. If the alarm action is deactivated, no actions are run when the alarm changes
state, and you won't be alerted to changes in monitored metrics. We recommend activating
CloudWatch alarm actions to help you quickly respond to security and operational
issues.

### Remediation

###### To activate a CloudWatch alarm action (console)

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, under **Alarms**, choose **All alarms**.
3. Select the alarm that you want to activate actions for.
4. For **Actions**, choose **Alarm actions–new**, and then choose **Enable**.

For more information about activating CloudWatch alarm actions, see [Alarm actions](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md#alarms-and-actions "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md#alarms-and-actions") in the _Amazon CloudWatch User Guide_.
