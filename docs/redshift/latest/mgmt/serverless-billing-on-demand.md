Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Billing for on-demand compute capacity

**Base capacity and its effect on billing**

When queries run, you're billed according to the capacity used in a given duration, in
RPU hours on a per-second basis. When no queries are running, you aren't billed for
compute capacity. You are also charged for Redshift Managed Storage (RMS), based on the
amount of data stored.

When you create your workgroup, you have the option to set the **Base
capacity** for computing. To meet the price/performance requirements of
your workload at a workgroup level, adjust the base capacity higher or lower for an
existing workgroup.
Select the workgroup from **Workgroup
configuration** and choose the **Limits** tab to change
the base capacity using the console.

As the number of queries increases, Amazon Redshift Serverless scales automatically to provide
consistent performance.

**Maximum RPU hours usage limit**

To keep costs predictable for Amazon Redshift Serverless, you can set the **Maximum RPU
hours** used per day, per week, or per month. You can set it using the
console or with the API. When a limit is reached, you can specify that a log entry is
written to a system table, or you receive an alert, or user queries are turned off.
Setting the maximum RPU hours helps keep your cost under
control. Settings for maximum RPU hours apply to
your workgroup for both queries that access data in your data warehouse and queries that
access external data, such as in an external table in
Amazon S3.

The following is an example:

Assume you set a limit for 100 hours for each week. To do this on the console, you do
the following:

1. Choose your workgroup and then choose **Manage usage
   limits** under the **Limits** tab.
2. Add a usage limit, choosing the **Weekly** frequency, a
   duration of **100** hours, and the setting the action to
   **Turn off user queries**.
   In this example, if you reach the 100 RPU hour limit for a week, queries are turned
   off.

Setting the maximum RPU hours for the workgroup doesn't limit the performance or
compute resources for the workgroup. You can adjust the settings at any time with no
affect on query processing. The goal for setting maximum RPU hours is to help you meet
your price and performance requirements. For more information about serverless billing,
see [Amazon Redshift pricing](https://aws.amazon.com/redshift/pricing/ "https://aws.amazon.com/redshift/pricing/").

Another way to keep the cost for Amazon Redshift Serverless predictable is to use AWS [Cost
Anomaly Detection](https://aws.amazon.com/aws-cost-management/aws-cost-anomaly-detection/ "https://aws.amazon.com/aws-cost-management/aws-cost-anomaly-detection/") to reduce the chance for billing surprises and provide
more control.

###### Note

The [Amazon Redshift pricing
calculator](https://calculator.aws/#/addService/Redshift "https://calculator.aws/#/addService/Redshift") is helpful for estimating pricing. You enter the compute
resources you need and it provides a preview of the cost.

## Setting Max capacity to

control costs for compute resources

The Max capacity setting serves as the RPU ceiling that Amazon Redshift Serverless can
scale up to. It helps control your cost for compute resources. In a similar way to
how base capacity sets a minimum amount of compute resources available, Max capacity
sets a ceiling on RPU usage. That way, it helps your spending adhere to your plans.
Max capacity applies
specifically to each workgroup and it limits compute usage at all times.

### How Max capacity

differs from RPU hour usage limits

The purpose of both maximum RPU hour limits and the Max capacity setting is
to control cost. But they achieve this through different means. The following
points explain the difference:

- _Max capacity_ – This setting establishes
  the highest count of RPUs that Amazon Redshift Serverless uses for scaling
  purposes. When automatic compute scaling is required, having a higher
  value for Max capacity can enhance query throughput. When the Max
  capacity limit is reached, the workgroup doesn't scale up resources any
  further.
- _Maximum RPU hours usage limit_ – Unlike Max
  capacity, this setting doesn't set a ceiling on capacity. But it does
  perform other actions to help you limit costs. These include adding an
  entry to a log, notifying you, or stopping queries from running, if you
  choose.

You can use Max capacity exclusively, or you can compliment it with actions
from maximum RPU hour usage limits.

### A Max capacity

use case

Each workgroup can have a different Max capacity setting. It helps you enforce
budgeting requirements. To illustrate how this works, assume the following:

- You have a workgroup with the base capacity set to 256 RPUs. You have
  steady workloads at just over 256 RPUs for most of the month.
- Max capacity is set to 512 RPUs.

Assume you have unexpected high use over a three-day period to generate ad-hoc
statistical reports. In
this case, you have Max capacity set to avoid compute costs beyond those for 512
RPUs. When you do this, you can be sure that compute capacity won't exceed this
upper
bound.

### Usage notes for Max

capacity

These notes can help you set Max capacity appropriately:

- Each Amazon Redshift Serverless workgroup can have a different Max capacity
  setting.
- If you have a period of very high resource usage and Max capacity is
  set to a low RPU level, it can delay workload processing and result in a
  user experience that isn't optimal.
- Configuring the Max capacity setting doesn't interfere with running
  queries, even during times of high RPU usage. It doesn't work like a
  usage limit, which can stop queries from running. It only limits compute
  resources available to the workgroup. You can view capacity used over a
  period of time on the Amazon Redshift Serverless dashboard. For more information
  about viewing summary data, see [Checking
  Amazon Redshift Serverless summary data using the dashboard](serverless-dashboard.md "serverless-dashboard.md").
- The top Max capacity setting is 5632 RPUs.

### How to set Max

capacity

You can set Max capacity in the console. For an existing workgroup, you can
change the setting under **Workgroup configuration**. You
can also use the CLI to set it by using a command like the following
sample:

```
aws redshift-serverless update-workgroup --workgroup-name myworkgroup --max-capacity 512
```

This sets the Max capacity setting for the workgroup with the given name.
After setting it, you can check the value on the console to verify it. You can
also check the value using the CLI by running the `get-workgroup`
command.

You can turn off the Max capacity setting by setting it to `-1`,
like the following:

```
aws redshift-serverless update-workgroup --workgroup-name myworkgroup --max-capacity -1
```

## Monitoring Amazon Redshift Serverless usage

and cost

There are several ways you can estimate usage and billing for Amazon Redshift Serverless.
System views can be helpful because the system metadata, including query and usage
data, is timely and you don't have to do any setup to query it. CloudWatch can also be
useful for monitoring usage for your Amazon Redshift Serverless instance, and has additional
features to provide insights and set actions.

### Visualizing usage by

querying a system view

Query the SYS_SERVERLESS_USAGE system table to track usage and get the charges
for queries:

```
select trunc(start_time) "Day",
(sum(charged_seconds)/3600::double
precision) * <Price for 1 RPU> as cost_incurred
from sys_serverless_usage
group by 1
order by 1
```

This query provides the cost per day incurred for Amazon Redshift Serverless, based on
usage.

#### Usage notes for

determining usage and cost

- You pay for the workloads you run in RPU-hours on a per-second
  basis, with a 60-second minimum charge.
- Records from the sys_serverless_usage system table show cost
  incurred in 1-minute time intervals. Understanding the following
  columns is important:

The charged_seconds column:

    + Provides the compute unit (RPU) seconds that were charged
     during the time interval. The results include any minimum
     charges in Amazon Redshift Serverless.
    + Has information about compute-resource usage after
     transactions complete. Thus, this column value may be 0 if
     transactions haven't finished.

The compute_seconds column:

    + Provides real-time compute usage information. This doesn't
     include any minimum charges in Amazon Redshift Serverless. Thus it
     can differ to some degree from the charged seconds billed
     during the interval.
    + Shows usage information during each transaction (even if a
     transaction hasn’t ended), and hence the data provided is
     real-time.

- There are situations where compute_seconds is 0 but
  charged_seconds is greater than 0, or vice versa. This is normal
  behavior resulting from the way data is recorded in the system view.
  For a more accurate representation of serverless usage details, we
  recommend aggregating the data in SYS_SERVERLESS_USAGE.

For more information about monitoring tables and views, see [Monitoring queries and
workloads with Amazon Redshift Serverless](serverless-monitoring.md "serverless-monitoring.md").

### Visualizing usage with

CloudWatch

You can use the metrics available in CloudWatch to track usage. The metrics
generated for CloudWatch are `ComputeSeconds`, indicating the total RPU
seconds used in the current minute and `ComputeCapacity`, indicating
the total compute capacity for that minute. Usage metrics can also be found on
the Redshift console on the Redshift **Serverless
dashboard**. For more information about CloudWatch, see [What is Amazon CloudWatch?](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md")
