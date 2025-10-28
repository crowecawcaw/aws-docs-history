# Estimating GuardDuty usage cost

During the 30-day free trial, you can use the GuardDuty console or API operations to estimate
the daily average usage costs for GuardDuty. The cost estimation projects what your estimated
costs will be after the trial period. However, to review an accurate cost estimate during
free trial, GuardDuty recommends using AWS Billing at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").

When you operate in a multiple-account environment, the GuardDuty administrator account can monitor cost
metrics for all of the member accounts.

###### Note about Malware Protection for S3 usage cost

The usage cost for Malware Protection for S3 is not included under **Usage** in the
GuardDuty console. For more information, see [Reviewing usage cost for Malware Protection for S3](usage-cost-malware-protection-s3-gdu.md "usage-cost-malware-protection-s3-gdu.md").

**You can view cost estimation based on the following
metrics:**

- **Account ID** – Lists the estimated cost for
  your account, or for your member accounts if you are operating as a GuardDuty administrator account.
- **Data sources** – Lists the estimated cost
  for all the [Foundational data sources](guardduty_data-sources.md "guardduty_data-sources.md") – AWS CloudTrail management
  events, VPC flow logs, and Route53 Resolver DNS query logs.
- **Features** – Lists the estimated cost for
  the [GuardDuty features](guardduty-feature-object-api-changes-march2023.md#guardduty-feature-enablement-datasource-relation "guardduty-feature-object-api-changes-march2023.md#guardduty-feature-enablement-datasource-relation") – CloudTrail data events for S3, EKS Audit Log Monitoring, EBS
  volume data, RDS login activity, EKS Runtime Monitoring, Fargate Runtime Monitoring, EC2 Runtime Monitoring, or
  Lambda Network Activity Monitoring.
- **S3 buckets** – Lists the estimated cost for
  S3 data events on a specified bucket or the most expensive buckets for accounts in
  your environment. This statistic is available only when you enable [S3 Protection](s3-protection.md "s3-protection.md") for an
  AWS account.

## Understanding how GuardDuty calculates usage

costs

The estimates displayed in the GuardDuty console may differ slightly than those in your
AWS Billing and Cost Management console. The following list explains how GuardDuty estimates usage costs:

- The GuardDuty usage estimate is for the current Region only.
- The GuardDuty usage cost is based on the last 30 days of usage.
- The trial usage cost estimate includes the estimate for foundational data
  sources and features that are currently in the trial period. Each feature and
  data source within GuardDuty has its own trial period but it may overlap with the
  trial period of GuardDuty or another feature that was enabled at the same
  time.
- The GuardDuty usage estimate includes GuardDuty volume pricing discounts per Region,
  as detailed on the [Amazon GuardDuty
  Pricing](https://aws.amazon.com/guardduty/pricing/ "https://aws.amazon.com/guardduty/pricing/") page, but only for individual accounts meeting the volume
  pricing tiers. Volume pricing discounts are not included in estimates for
  combined total usage between accounts within an organization. For information
  about combined usage volume discount pricing, see [AWS Billing: Volume Discounts](../../../awsaccountbilling/latest/aboutv2/useconsolidatedbilling-discounts.md "../../../awsaccountbilling/latest/aboutv2/useconsolidatedbilling-discounts.md").
- The sum of the usage cost for each AWS account in your organization may not
  always be the same as the last 30-day estimated cost for the selected data
  source. The pricing tier may change as GuardDuty processes more events or data. For
  more information, see [Pricing Tiers](../../../awsaccountbilling/latest/aboutv2/con-bill-blended-rates.md#Blended_Rate_Overview "../../../awsaccountbilling/latest/aboutv2/con-bill-blended-rates.md#Blended_Rate_Overview") in the _AWS Billing User
  Guide_.

###

This scenario explains that to stop incurring usage cost for Runtime Monitoring, you must
have both the Runtime Monitoring and EKS Runtime Monitoring features disabled.

GuardDuty has consolidated the console experience for EKS Runtime Monitoring into Runtime Monitoring.
GuardDuty recommends [Checking EKS Runtime Monitoring configuration
status](checking-eks-runtime-monitoring-enable-status.md "checking-eks-runtime-monitoring-enable-status.md") and
[Migrating from EKS Runtime Monitoring to
Runtime Monitoring](migrating-from-eksrunmon-to-runtime-monitoring.md "migrating-from-eksrunmon-to-runtime-monitoring.md").

As a part of migrating to Runtime Monitoring, ensure to [Disable
EKS Runtime Monitoring](disabling-eks-runtime-monitoring.md "disabling-eks-runtime-monitoring.md"). This is important
because if you later choose to disable Runtime Monitoring and you do not disable EKS Runtime Monitoring,
you will continue incurring usage cost for EKS Runtime Monitoring.

### Runtime Monitoring – How VPC

flow logs from EC2 instances impact usage cost

When you manage the security agent (either manually or through GuardDuty) in EKS Runtime Monitoring
or Runtime Monitoring for EC2 instances, and
GuardDuty is presently deployed on an Amazon EC2 instance and receives
the [Collected runtime event
types](runtime-monitoring-collected-events.md "runtime-monitoring-collected-events.md") from this instance, GuardDuty will not charge
your AWS account for the analysis of VPC flow logs from this Amazon EC2 instance. This helps GuardDuty avoid double usage cost in the account.

### How GuardDuty estimates usage

cost for CloudTrail events

When you enable GuardDuty, it automatically starts consuming AWS CloudTrail event logs
recorded for your account in the selected AWS Region. GuardDuty replicates [Global service events](../../../awscloudtrail/latest/userguide/cloudtrail-concepts.md#cloudtrail-concepts-global-service-events "../../../awscloudtrail/latest/userguide/cloudtrail-concepts.md#cloudtrail-concepts-global-service-events") logs and then processes these events
independently in each Region where you have GuardDuty enabled. This helps GuardDuty maintain
user and role profiles in each Region to identify anomalies.

Your CloudTrail configuration does not impact GuardDuty usage cost or the way GuardDuty
processes your event logs. Your GuardDuty usage cost is affected by your usage of AWS
APIs which log to CloudTrail. For more information, see [AWS CloudTrail management events](guardduty_data-sources.md#guardduty_controlplane "guardduty_data-sources.md#guardduty_controlplane").
