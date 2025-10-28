# Viewing the AWS Config Dashboard

Use the **Dashboard** to see an overview of your resources, rules,
conformance packs, and their compliance states and to visualize your AWS Config usage and success
metrics with Amazon CloudWatch. This page helps you quickly identify the top resources in your AWS
account, the conformance packs with the lowest level of compliance in your AWS account,
what rules or resources are noncompliant in your AWS account, what traffic is driving your
AWS Config usage, and key metrics for success and failure that have occured in your
workflows.

###### To use the AWS Config Dashboard

1. Sign in to the AWS Management Console and open the AWS Config console at
   [https://console.aws.amazon.com/config/home](https://console.aws.amazon.com/config/home "https://console.aws.amazon.com/config/home").
2. In the left navigation pane, choose **Dashboard**.

###### Contents

- [Compliance and Resource
  Inventory](viewing-the-aws-config-dashboard.md#aws-config-dashboard-compliance "viewing-the-aws-config-dashboard.md#aws-config-dashboard-compliance")
- [AWS Config Usage and Success Metrics](viewing-the-aws-config-dashboard.md#aws-config-dashboard-metrics "viewing-the-aws-config-dashboard.md#aws-config-dashboard-metrics")

## Compliance and Resource

Inventory

After setup, AWS Config starts recording your specified resources and evaluating them
against your rules. It may take a few minutes for AWS Config to display your resources,
rules, conformance packs, and their compliance states.

**Conformance packs by compliance score**

_Conformance packs by compliance score_ displays up to
10 of your conformance packs with the lowest compliance score. A compliance
score is the percentage of the number of compliant rule-resource
combinations in a conformance pack compared to the number of total possible
rule-resource combinations in the conformance pack.

This metric provides you with a high-level view of the compliance state of
your conformance packs, and can be used to identify, investigate, and
understand the level of compliance in your conformance packs. You can use
the compliance score to track remediation progress, perform comparisons
across different sets of requirements, and see the impact a specific change
or deployment has on a conformance pack.

To view the deployment status, compliance score, compliance score
timeline, and rules for a conformance pack in a detailed view, choose the
name of the conformance pack under **Conformance
pack**.

**Compliance status**

_Compliance status_ displays the number of your
compliant and noncompliant rules and compliant and noncompliant resources.
Resources are compliant or noncompliant based on an evaluation of the rule
associated with it. If a resource does not follow the rule's specifications,
the resource and the rule are flagged as noncompliant.

To view the list of noncompliant rules and resources, choose
**Noncompliant rule(s)** or **Noncompliant
resource(s)**.

**Rules by noncompliant resources**

_Rules by noncompliant resources_ displays your top
noncompliant rules in descending order by the number of resources. Choose a
rule to view its details, parameters, and the resources in scope for that
specific rule.

For a comprehensive list of noncompliant rules, choose **View all
noncompliant rules**.

**Resource inventory**

_Resource inventory_ displays the total number of
resources that AWS Config is recording in descending order by the number of
resources, and the count of each resource type in your AWS account. To
open all resources for a resource type, choose that resource type to go to
its **Resources inventory** page.

You can use the dropdown list to indicate which resource totals you want
to view. By default, it is set to view **All resources**,
but you can change it to AWS resources, Third-party resources, or Custom
resources.

###### Note

The **Evaluate your AWS resource configuration using Config
rules** message may appear on the **Dashboard** for
the following reasons:

- You haven't set up AWS Config Rules for your AWS account. You can choose
  **Add rule** to go to the **Rules**
  page.
- AWS Config is still evaluating your resources against your rules. You can
  refresh the page to see the latest evaluation results.
- AWS Config evaluated your resources against your rules and did not find any
  resources in scope. You can specify the resources for AWS Config to record in the
  **Settings** page. For more information, see [Recording AWS Resources with AWS Config](select-resources.md "select-resources.md").

## AWS Config Usage and Success Metrics

You can use Amazon CloudWatch dashboards in the AWS Config console to visualize your AWS Config usage and
success metrics.

For each dashboard, you can do the following:

- Adjust the dashboard time range to display data from the past **3 Hours**, **1 Day**, or
  **1 Week**.
- Choose the **Calender icon**, to enter a custom time range: either a
  **Relative** time for a past specified amount of time or an
  **Absolute** time range between two dates.
- You can
  change the time format to display dashboard data in **UTC**
  (Coordinated Universal Time) or **Local time zone** (the time
  zone specified as your local time zone in the operating system of your device).
- Use the **Drop arrow** next the **Refresh
  icon** to specify how often the data in a dashboard should refresh,
  or to turn off the automatic refresh. Choose **Off**,
  **10 Seconds**, **1 Minute**, **2
  Minutes**, **5 Minutes**, or **15
  Minutes** to change the refresh internal.
- Choose **More options** (the vertical ellipsis menu) to add the AWS Config usage metrics or
  the AWS Config success metrics you are currently viewing in the AWS Config Dashboard to the
  CloudWatch console. This opens a new tab in the CloudWatch console that allows you to create
  a new custom dashboard in CloudWatch with information copied from your current AWS Config
  usage metrics or AWS Config success metrics.

If you want to perform additional analyses of these metrics with CloudWatch, choose
**Metrics** in the left navigation pane of the CloudWatch console and
then choose **AWS/Config**. For more information on what you can do
from the CloudWatch console, see [Using
Amazon CloudWatch dashboards](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md") and [Using Amazon CloudWatch metrics](../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md "../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md") in the _CloudWatch User Guide_.

**AWS Config Usage Metrics**

| Metric                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Unit  |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Configuration Items Recorded`                            | The number of configuration items recorded for each resource type or all resource types. A configuration item represents a point-in-time view of the various attributes of a supported AWS resource. For more information about configuration items or supported resource types, see [Configuration Items](config-concepts.md#config-items.html "config-concepts.md#config-items.html") and [Supported Resource Types](resource-config-reference.md "resource-config-reference.md").                                                                                                        | Count | You can select the resource type that you want to view by using the dropdown list. By default, it is set to view all resource types. **AWS Config Success Metrics** |
| Metric                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Unit  |
| ---                                                       | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | ---   |
| `Change Notifications Delivery Failed`                    | The number of failed change notification deliveries to the Amazon SNS topic for your delivery channel. A change notification informs you about a change to the configuration state of your AWS resources. You can use the [ConfigStreamDeliveryInfo](../APIReference/API_ConfigStreamDeliveryInfo.md "../APIReference/API_ConfigStreamDeliveryInfo.md") API to get the `lastErrorCode` or `lastErrorMessage` for the last attempted delivery for a change notification. For more information, see [Managing the Delivery Channel](manage-delivery-channel.md "manage-delivery-channel.md"). | Count |
| `Config History Export Failed`                            | The number of failed configuration history exports to your Amazon S3 bucket. A configuration history is a collection of the configuration items for a given resource over a specified time period. For more information about configuration history, see [Configuration History](config-concepts.md#config-history "config-concepts.md#config-history").                                                                                                                                                                                                                                    | Count |
| `Configuration Recorder Insufficient Permissions Failure` | The number of failed permission access attempts due to the IAM role policy for all the configuration recorders in your account and AWS Region having insufficient permissions. The configuration recorder detects changes in to the resource types in scope. For the configuration recorder to record your AWS resource configurations, it requires the necessary IAM permissions. For more information, see [IAM Role Policy for Getting Configuration Details](iamrole-permissions.md#iam-role-policies-describe-apis "iamrole-permissions.md#iam-role-policies-describe-apis").          | Count |
| `Config Snapshot Export Failed`                           | The number of failed configuration snapshot exports to your Amazon S3 bucket. A configuration snapshot is a collection of the configuration items for the supported resources in your account. For more information about configuration snapshots, see [Configuration Snapshot](config-concepts.md#config-snapshot "config-concepts.md#config-snapshot").                                                                                                                                                                                                                                   | Count |
