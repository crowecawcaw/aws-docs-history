

# Service level objectives (SLOs)
<a name="CloudWatch-ServiceLevelObjectives"></a>

You can use Application Signals to create *service level objectives* for the services for your critical business operations or dependencies. By creating SLOs on these services, you will be able to track them on the SLO dashboard, giving you an at-a-glance view of your most important operations.

In addition to creating a quick view your operators can use to see the current status of critical operations, you can use SLOs to track the longer-term performance of your services, to make sure that they are meeting your expectations. If you have service level agreements with customers, SLOs are a great tool to make sure that they are met. 

Assessing your services' health with SLOs starts with setting clear, measurable objectives based on key performance metrics— *service level indicators (SLIs)*. An SLO tracks the SLI performance against the threshold and goal that you set, and reports how far or how close your application performance is to the threshold.

Application Signals helps you set SLOs on your key performance metrics. Application Signals automatically collects `Latency` and `Availability` metrics for every service and operation that it discovers, and these metrics are often ideal to use as SLIs. With the SLO creation wizard, you can use these metrics for your SLOs. You can then track the status of all of your SLOs with the Application Signals dashboards. 

You can set SLOs on specific operations or dependencies that your service calls or uses. You can use any CloudWatch metric or metric expression as an SLI, in addition to using the `Latency` and `Availability` metrics.

**Creating SLOs is very important for getting the most benefit from CloudWatch Application Signals.** After you create SLOs, you can view their status in the Application Signals console to quickly see which of your these critical services and operations are performing well and which are unhealthy. Having SLOs to track provides the following major benefits:
+ It is easier for your service operators to see the current operational health of critical services as measured against the SLI. Then they can quickly triage and identify unhealthy services and operations.
+ You can track your service performance against measurable business goals over longer periods of time.

By choosing what to set SLOs on, you are prioritizing what is important to you. The Application Signals dashboards automatically present information about what you have prioritized.

When you create an SLO, you can also choose to create CloudWatch alarms at the same time to monitor the SLOs. You can set alarms that monitor for breaches of the threshold, and also for warning levels. These alarms can automatically notify you if the SLO metrics are breaching the threshold that you set, or if they are nearing a warning threshold. For example, an SLO nearing its warning threshold can let you know that your team might need to slow down churn in the application to make sure that long-term performance goals are met.

**Topics**
+ [SLO concepts](#CloudWatch-ServiceLevelObjectives-concepts)
+ [Calculate error budget and attainment for period-based SLOs](#CloudWatch-ServiceLevelObjectives-budget)
+ [Calculate error budget and attainment for request-based SLOs](#CloudWatch-ServiceLevelObjectives-budget-request)
+ [Calculate burn rates and optionally set burn rate alarms](#CloudWatch-ServiceLevelObjectives-burn)
+ [Create an SLO](#CloudWatch-ServiceLevelObjectives-Create)
+ [Use SLO recommendations](#CloudWatch-ServiceLevelObjectives-Recommendations)
+ [View and triage SLO status](#CloudWatch-ServiceLevelObjectives-Triage)
+ [Edit an existing SLO](#CloudWatch-ServiceLevelObjectives-Edit)
+ [Delete an SLO](#CloudWatch-ServiceLevelObjectives-Delete)

## SLO concepts
<a name="CloudWatch-ServiceLevelObjectives-concepts"></a>

An SLO includes the following components:
+ A *service level indicator (SLI)*, which is a key performance metric that you specify. It represents the desired level of performance for your application. Application Signals automatically collects the key metrics `Latency` and `Availability` for the services and operations that it discovers, and these can often be ideal metrics to set SLOs for.

  You choose the threshold to use for your SLI. For example, 200ms for latency.
+ A *goal* or *attainment goal*, which is the percentage of time or requests that the SLI is expected to meet the threshold over each time *interval*. The time intervals can be as short as hours or as long as a year. 

  Intervals can be either calendar intervals or rolling intervals.
  + *Calendar intervals* are aligned with the calendar, such as an SLO that is tracked per month. CloudWatch automatically adjusts health, budget, and attainment numbers based on the number of days in a month. Calendar intervals are better suited for business goals that are measured on a calendar-aligned basis.
  + *Rolling intervals* are calculated on a rolling basis. Rolling intervals are better suited for tracking recent user experience of your application.
+ The *period* is a shorter length of time, and many periods make up an interval. The application's performance is compared to the SLI during each period within the interval. For each period, the application is determined to have either achieved or not achieved the necessary performance.

For example, a goal of 99% with a calendar interval of one day and a period of 1 minute means that the application must meet or achieve the success threshold during 99% of the 1-minute periods during the day. If it does, then the SLO is met for that day. The next day is a new evaluation interval. The application must meet or achieve the success threshold during 99% of the 1-minute periods during the second day to meet the SLO for that second day.

An SLI can be based on one of the new standard application metrics collected by Application Signals. Alternatively, it can be any CloudWatch metric or metric expression. The standard application metrics that you can use for an SLI are `Latency` and `Availability`. `Availability` represents the successful responses divided by the total requests. It is calculated as **(1 - Fault Rate)\*100**, where Fault responses are `5xx` errors. Success responses are responses without a `5XX` error. `4XX` responses are treated as successful. 

In addition to creating SLOs on a single operation or on all operations of a service, you can create *composite SLOs* that monitor a subset of operations for a service. Composite SLOs aggregate the `Availability` metric across multiple operations, giving you a unified view of reliability for a group of related operations. You can select between 2 and 20 operations to include in a composite SLO. For more information, see [Create a composite SLO on multiple operations](#CloudWatch-ServiceLevelObjectives-Create-Composite).

## Calculate error budget and attainment for period-based SLOs
<a name="CloudWatch-ServiceLevelObjectives-budget"></a>

When you view information about an SLO, you see its current health status and its *error budget*. The error budget is the amount of time within the interval that can breach the threshold but still let the SLO be met. The *total error budget* is the total amount of breaching time that can be tolerated through the entire interval. The *remaining error budget* is the remaining amount of breaching time that can be tolerated during the current interval. This is after the amount of breaching time that has already happened has been subtracted from the total error budget.

The following figure illustrates the attainment and error budget concepts for a goal with a 30-day interval, 1-minute periods, and a 99% attainment goal. 30 days includes 43,200 1-minute periods. 99% of 43,200 is 42,768, so 42,768 minutes during the month must be healthy for the SLO to be met. So far in the current interval, 130 of the 1-minute periods were unhealthy.

![Bar chart showing total periods in an SLO interval with attainment and error budget numbers.](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/images/SLO-budget.png)


### Determine success within each period
<a name="CloudWatch-ServiceLevelObjectives-success"></a>

Within each period, the SLI data is aggregated into a single data point based on the statistic used for the SLI. This data point represents the entire length of the period. That single data point is compared to the SLI threshold to determine if the period is healthy. Seeing unhealthy periods during the current time range on the dashboard can alert your service operators that the service needs to be triaged.

If the period is determined to be unhealthy, the entire length of the period is counted as failed against the error budget. Tracking the error budget lets you know whether the service is achieving the performance that you want over a longer period of time.

### Time window exclusions
<a name="CloudWatch-TimeWindowExclusion"></a>

*Time window exclusions* is a block of time with a defined start and end date. This time period is excluded from the SLO's performance metrics and you can schedule one-time or recurring time exclusions windows. For example, scheduled maintenance.

**Note**  
For period-based SLOs, SLI data in the exclusion window is considered as non-breaching.
For request-based SLOs, all good and bad requests in the exclusion window are excluded.
When an interval for a request-based SLO is completely excluded, a default attainment rate metric of 100% is published.
You can only specify time windows with a start date in the future.

## Calculate error budget and attainment for request-based SLOs
<a name="CloudWatch-ServiceLevelObjectives-budget-request"></a>

After you have created an SLO, you can retrieve error budget reports for it. An *error budget* is the amount of requests that your application can be non-compliant with the SLO's goal, and still have your application meet the goal. For a request-based SLO, the remaining error budget is dynamic and can increase or decrease, depending on the ratio of good requests to total requests

The following table illustrates the calculation for a request-based SLO with an interval of 5 days and 85% attainment goal. In this example, assume there is no traffic before Day 1. The SLO did not meet the goal on Day 10.

**Note**  
For request-based SLOs, `TotalRequestCountPerMinute` and `BadRequestCountPerMinute` are emitted as additional metrics compared to period-based SLO metrics. These metrics are provided for observability purposes and are not used as inputs to attainment-rate calculations.  
Because these metrics are generated from periodically evaluated metric data, their values might occasionally differ from expected request counts due to metric publication timing or delays. Such discrepancies do not impact SLO attainment calculations, which are computed independently of these emitted per-minute metrics.


| Time | Total requests | Bad requests | Accumulative total requests in last 5 days | Accumulative total good requests in last 5 days | Request-based attainment | Total budget requests | Remaining budget requests | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
| Day 1 | 10 | 1 | 10 | 9 | 9/10 = 90% | 1.5 | 0.5 | 
| Day 2 | 5 | 1 | 15 | 13 | 13/15=86% | 2.3 | 0.3 | 
| Day 3 | 1 | 1 | 16 | 13 | 13/16=81% | 2.4 | -0.6 | 
| Day 4 | 24 | 0 | 40 | 37 | 37/40=92% | 6.0 | 3.0 | 
| Day 5 | 20 | 5 | 60 | 52 | 52/60=87% | 9.0 | 1.0 | 
| Day 6 | 6 | 2 | 56 | 47 | 47/56=84% | 8.4 | -0.6 | 
| Day 7 | 10 | 3 | 61 | 50 | 50/61=82% | 9.2 | -1.8 | 
| Day 8 | 15 | 6 | 75 | 59 | 59/75=79% | 11.3 | -4.7 | 
| Day 9 | 12 | 1 | 63 | 46 | 46/63=73% | 9.5 | -7.5 | 
| Day 10 |  | 5 | 57 | 40 | 40/57=70% | 8.5 | -8.5 | 
| **Final attainment for last 5 days** |  |  |  | **** | 70% |  |  | 

## Calculate burn rates and optionally set burn rate alarms
<a name="CloudWatch-ServiceLevelObjectives-burn"></a>

You can use Application Signals to calculate the *burn rates* for your service level objectives. A burn rate is a metric that indicates how fast the service is consuming the error budget, relative to the attainment goal of the SLO. It's expressed as a mutliple factor of the baseline error rate. 

The burn rate is calculated according to the *baseline error rate*, which depends on the attainment goal. The attainment goal is the percentage of either healthy time periods or successful requests that must be achieved to meet the SLO goal. The baseline error rate is (100% - attainment goal percentage), and this number would use up the exact complete error budget at the end of the SLO's time interval. So an SLO with an attainment goal of 99% would have a baseline error rate of 1%.

Monitoring the burn rate tells us how far off you are from the baseline error rate. Again taking the example of an attainment goal of 99%, the following is true:
+ **Burn rate = 1**: If the burn rate remains exactly at the baseline error rate all the time, you meet exactly the SLO goal.
+ **Burn rate < 1**: If the burn rate is lower than the baseline error rate, you are on track to exceed the SLO goal.
+ **Burn rate > 1**: If the burn rate is higher than baseline error rate, you have a chance to fail the SLO goal.

When you create burn rates for your SLOs, you can also choose to create CloudWatch alarms at the same time to monitor the burn rates. You can set a threshold for the burn rates and the alarms can automatically notify you if the burn rate metrics are breaching the threshold that you set. For example, a burn rate nearing its threshold can let you know that the SLO is burning through the error budget faster than your team can tolerate and your team might need to slow down churn in the application to make sure that long-term performance goals are met.

Creating alarms incurs charges. For more information about CloudWatch pricing, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/).

### Calculate the burn rate
<a name="ServiceLevelObjectives-calculate-burnrate"></a>

To calculate the burn rate, you must specify a *look-back window*. The look-back window is the time duration over which to measure the error rate.

`burn rate = error rate over the look-back window / (100% - attainment goal)`

**Note**  
When there is no data for the burn rate period, Application Signals calculates the burn rate based on attainment.

The error rate is calculated as the ratio of the number of bad events over the total number of events during the burn rate window:
+ For period-based SLOs, error rate is calculated as bad periods divided by total periods. The total periods represents the entirety of periods during the look-back window.
+ For request-based SLOs, this is a measure of bad requests divided by total requests. The total number of requests is the number of requests during the look-back window.

The look-back window must be a multiple of the SLO period time, and must be less than the SLO interval.

### Determine the appropriate threshold for a burn rate alarm
<a name="ServiceLevelObjectives-calculate-threshold"></a>

When you configure a burn rate alarm, you need to choose a value for the burn rate as the alarm threshold. The value for this threshold depends on the SLO interval length and look-back window, and depends on the which method or mental model that your team wants to adopt. There are two main methods available for determining the threshold.

**Method 1: Determine the percentage of estimated total error budget your team is willing to burn in the look-back window.**

If you want to get alarmed when X% of the estimated error budget is spent within the last burn rate look-back hours, the burn rate threshold is the following:

`burn rate threshold = X% * SLO interval length / look-back window size`

For example, 5% of a 30-day (720-hour) error budget spent over one hour requires a burn rate of `5% * 720 / 1 = 36`. Therefore, if the burn rate look-back window is1 hour, you set the burn rate threshold to be 36.

You can use the CloudWatch console to create burn rate alarms using this method. You can specify the number X, and the threshold is determined using the above formula.

The SLO interval length is determined based on the SLO interval type:
+ For SLOs with a rolling interval, it's the length of the interval in hours.
+ For SLOs with a calendar-based interval:
  + If the unit is days or weeks, it's the length of the interval in hours.
  + If the unit is a month, 30 days is taken as the estimated length and convert it to hours.

**Method 2: Determine the time unitl budget exhaustion for the next interval**

To have the alarm notify you when the current error rate in the most recent look-back window indicates that the time until budget exhaustion is less than X hours away (assuming the budget remaining is currently 100%), you can use the following formula to determine the burn rate threshold.

`burn rate threshold = SLO interval length / X`

Note that the time until budget exhaustion (X) in the above formula assumes that the total budget remaining is currently 100%, and therefore it does not take into account the amount of budget that has already been burnt in this interval. You can also think of it as the time till budget exhaustion for the next interval. 

### Walkthroughs for burn rate alarms
<a name="ServiceLevelObjectives-burnrate-examples"></a>

As an example, let's take an SLO with a 28-day rolling interval. Setting a burn rate alarm for this SLO involves two steps:

1. Set the burn rate and the look-back window.

1. Crete a CloudWatch alarm that monitors the burn rate.

To get started, determine how much of the total error budget the service is willing to burn through within a specific time frame. In other words, statie your objective by using this sentence: "I want to get alerted when X% of my total error budget is consumed within M minutes."

For example, you might want to set the objective to be alerted when 2% of the total error budget is consumed within 60 minutes.

To set the burn rate, you first define the look-back window. The look-back windows is M, which in this example is 60 minutes.

Next, you create the CloudWatch alarm. When you do so, you must specify a threshold for the burn rate. If burn rate exceeds this threshold, the alarm will notify you. To find the threshold,use the following formula:

` burn rate threshold = X% * SLO interval length/ look-back window size`

In this example, X is 2 because you want to be alerted if 2% of the error budget is consumed within 60 minutes. The interval length is 40,320 minutes (28 days), and 60 minutes is the look-back window, so the answer is:

`burn rate threshold = 2% * 40,320 / 60 = 13.44.`

In this example, you would set 13.44 as the alarm threshold.

### Multiple alarms with different windows
<a name="ServiceLevelObjectives-burnrate-multi-alarm"></a>

By setting up alarms on multiple look-back windows, you can quickly detect sharp error rate increases with the short window and at the same time detect smaller error rate increases that eventually deplete the error budget if they remain unnoticed.

Additionally, you could set a *composite alarm* on a burn rate with long window and on a burn rate with a short window (1/12th of the long window), and be informed only when both of the burn rates breach a threshold. This way, you can make sure that you get alerted only for situations that are still happening. For more information about composite alarms in CloudWatch, see [Create a composite alarm](Create_Composite_Alarm.md).

**Note**  
You can set a metric alarm on a burn rate when you create the burn rate. To set a compoaite alarm on multiple burn rate alarms, you must use the instructions in [Create a composite alarm](Create_Composite_Alarm.md).

One composite alarm strategy recommended in the [Google Site Reliability Engineering workbook](https://sre.google/workbook/alerting-on-slos/) includes three composite alarms:
+ One composite alarm that watches a pair of alarms, one with a one-hour window and one with a five-minute window.
+ A second composite alarm that watches a pair of alarms, one with a six-hour window and one with a 30-minute window.
+ A third composite alarm that watches a pair of alarms, one with a three-day window and one with a six-hour window.

The steps to do this set up are the following:

1. Create five burn rates, with windows of five minutes, 30 minutes, one hour, six hours, and three days.

1. Create the following three pairs of CloudWatch alarms. Each pair includes one long window and one short window that is 1/12th of the long window, and the thresholds are determined by using the steps in [Determine the appropriate threshold for a burn rate alarm](#ServiceLevelObjectives-calculate-threshold). When you calculate the threshold for each alarm in the pair, use the longer look-back window of the pair in your calculation.
   + Alarms on the 1-hour and 5-minute burn rates (the threshold is determined by 2% of the total budget) 
   + Alarms on the 6-hour and 30-minute burn rates (the threshold is determined by 5% of the total budget)
   + Alarms on the 3-day and 6-hour burn rates (the threshold is determined by 10% of the total budget)

1. For each of these pairs, create a composite alarm to get alerted when both of the individual alarms go into ALARM state. For more information about creating composite alarms, see [Create a composite alarm](Create_Composite_Alarm.md).

   For example, if your alarms for the first pair (one-hour window and five-minute window) are named `OneHourBurnRate` and `FiveMinuteBurnRate`, the CloudWatch composite alarm rule would be `ALARM(OneHourBurnRate) AND ALARM(FiveMinuteBurnRate)`

The previous strategy is possible only for SLOs with interval length of at least three hours. For SLOs with shorter interval lengths, CloudWatch recommend that you start with one pair of burn rate alarms where one alarm has a look-back window that is 1/12th of the look-back window of the other alarm. Then set a composite alarm on this pair.

## Create an SLO
<a name="CloudWatch-ServiceLevelObjectives-Create"></a>

We recommend that you set both latency and availability SLOs on your critical applications. These metrics collected by Application Signals align with common business goals.

You can also set SLOs on any CloudWatch metric or any metric math expression that results in a single time series.

The first time that you create an SLO in your account, CloudWatch automatically creates the **AWSServiceRoleForCloudWatchApplicationSignals** service-linked role in your account, if it doesn't already exist. This service-linked role allows CloudWatch to collect CloudWatch Logs data, X-Ray trace data, CloudWatch metrics data, and tagging data from applications in your account. For more information about CloudWatch service-linked roles, see [Using service-linked roles for CloudWatch](using-service-linked-roles.md).

When you create an SLO, you specify whether it is a *period-based SLO* or a *request-based SLO*. Each type of SLO has a different way of evaluating your application's performance against its attainment goal.
+ A *period-based SLO* uses defined *periods* of time within a specified total time interval. For each period of time, Application Signals determines whether the application met its goal. The attainment rate is calculated as the `number of good periods/number of total periods`.

  For example, for a period-based SLO, meeting an attainment goal of 99.9% means that within your interval, your application must meet its performance goal during at least 99.9% of the time periods.
+ A *request-based SLO* doesn't use pre-defined periods of time. Instead, the SLO measures `number of good requests/number of total requests` during the interval. At any time, you can find the ratio of good requests to total requests for the interval up to the time stamp that you specify, and measure that ratio against the goal set in your SLO.

**Topics**
+ [Create a period-based SLO](#CloudWatch-ServiceLevelObjectives-Create-Period)
+ [Create a request-based SLO](#CloudWatch-ServiceLevelObjectives-Create-Request)
+ [Create an SLO on an app monitor](#CloudWatch-ServiceLevelObjectives-Create-AppMonitor)
+ [Create an SLO on a canary](#CloudWatch-ServiceLevelObjectives-Create-Canary)
+ [Create a composite SLO on multiple operations](#CloudWatch-ServiceLevelObjectives-Create-Composite)

### Create a period-based SLO
<a name="CloudWatch-ServiceLevelObjectives-Create-Period"></a>

Use the following procedure to create a period-based SLO.

**To create a period-based SLO**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Service Level Objectives (SLO)**.

1. Choose **Create SLO**.

1. For **Set Service Level Indicator (SLI)**, do one of the following:
   + To set the SLO on a service operation, all operations, or the dependency of a service, using either of the standard application metrics `Latency` or `Availability`:

     1. For **Type**, choose **Service**.

     1. Select an account that this SLO will monitor.

     1. Select the service that this SLO will monitor.

     1. For **Type**, choose one of the following:
        + **Service Operations** — to create an SLO on a service operation, all operations, or a subset of operations.
        + **Service Dependency** — to create an SLO on a dependency of the service.

     1. If you chose **Service Operations**, select the operation that this SLO will monitor. To create a service-level SLO that monitors the overall health of your service across all operations, select **All Operations**. Otherwise, select a specific operation to monitor.

        To create an SLO that monitors a subset of operations, see [Create a composite SLO on multiple operations](#CloudWatch-ServiceLevelObjectives-Create-Composite).

     1. If you chose **Service Dependency**, do the following:

        1. Under **Select an operation**, select one specific operation or select **All operations** to use the metrics from all operations of this service that calls a dependency.

        1. Under **Select a dependency**, search and select the required dependency for which you want to measure the reliability.

           After you select the dependency, you can view the updated graph and historical data based on the dependency.

     1. For **Select a calculation method**, choose **Periods**.

        The **Select service** and **Select operation** drop-downs are populated by services and operations that have been active within the past 24 hours.

     1. Choose either **Availability** or **Latency** and then set the threshold.
   + To set the SLO on any CloudWatch metric or a CloudWatch metric math expression:

     1. For **Type**, choose **CloudWatch Metric**.

     1. Choose **Select CloudWatch metric**.

        The **Select metric** screen appears. Use the **Browse** or **Query** tabs to find the metric you want, or create a metric math expression. 

        After you select the metric that you want, choose the **Graphed metrics** tab and select the **Statistic** and **Period** to use for the SLO. Then choose **Select metric**.

        For more information about these screens, see [Graph a metric](graph_a_metric.md) and [Add a math expression to a CloudWatch graph](using-metric-math.md#adding-metrics-expression-console). 

     1. For **Select a calculation method**, choose **Periods**.

     1. For **Set condition**, select a comparison operator and threshold for the SLO to use as the indicator of success.

1. If you selected **Service** in step 4, set the period length for this SLO. 

1. Enter a name for the SLO. Including the name of a service or operation, along with appropriate keywords such as latency or availability, will help you quickly identify what the SLO status indicates during triage.

1. Set the **interval** and **attainment goal** for the SLO. For more information about intervals and attainment goals and how they work together, see [SLO concepts](#CloudWatch-ServiceLevelObjectives-concepts).

1. (Optional) For **Set SLO burn rates** do the following:
   + Set the length (in minutes) of the look-back window for the burn rate. For information about how to choose this length, see [Walkthroughs for burn rate alarms](#ServiceLevelObjectives-burnrate-examples).
   + To create more burn rates for this SLO, choose **Add more burn rates** and set the look-back window for the additional burn rates.

1. (Optional) Create burn rate alarms by doing the following:
   + Under **Set burn rate alarms** select the check box for each burn rate that you want to create an alarm for. For each of these alarms, do the following:
     + Specify the Amazon SNS topic to use for notifications when the alarm goes into ALARM state.
     + Either set a burn rate threshold or specify the percentage of the estimated total budget burnt in the last look-back window you want to stay below. If you set the percentage of estimated total budget burned, the burn rate threshold is calculated for you and used in the alarm. To either decide what threshold to set or to understand how this option is used to compute the burn rate threshold, see [Determine the appropriate threshold for a burn rate alarm](#ServiceLevelObjectives-calculate-threshold). 

1. (Optional) Set one or more CloudWatch alarms or a warning threshold for the SLO. 

   1. CloudWatch alarms can use Amazon SNS to proactively notify you if an application is unhealthy based on its SLI performance. 

      To create an alarm, select one of the alarm check boxes and enter or create the Amazon SNS topic to use for notifications when the alarm goes into `ALARM` state. For more information about CloudWatch alarms, see [Using Amazon CloudWatch alarms](CloudWatch_Alarms.md). Creating alarms incurs charges. For more information about CloudWatch pricing, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/).

   1. If you set a warning threshold, it appears in Application Signals screens to help you identify SLOs that are in danger of being unmet, even if they're currently healthy. 

      To set a warning threshold, enter the threshold value in **Warning threshold**. When the SLO's error budget is lower than the warning threshold, the SLO is marked with **Warning** in several Application Signals screens. Warning thresholds also appear on error budget graphs. You can also create an **SLO warning alarm** that's based on the warning threshold.

1. (Optional) For **Set SLO time window exclusion**, do the following:
   + Under **Exclude time window**, set the time window to be excluded from the SLO performance metrics.

     You can choose **Set time window** and enter the **Start window** for every hour or month or you can choose **Set time window with CRON** and enter the CRON expression.
   + Under **Repeat**, set if this time window exclusion is recurring or not.
   + (Optional) Under **Add reason**, you can choose to enter a reason for the time window exclusion. For example, scheduled maintenance.
   + Select **Add time window** to add upto 10 time exclusion windows.

1. To add tags to this SLO, choose the **Tags** tab and then choose **Add new tag**. Tags can help you manage, identify, organize, search for, and filter resources. For more information about tagging, see [ Tagging your AWS resources](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html). 
**Note**  
If the application this SLO is related to is registered in AWS Service Catalog AppRegistry, you can use the `awsApplication` tag to associate this SLO with that application in AppRegistry. For more information, see [ What is AppRegistry?](https://docs.aws.amazon.com/servicecatalog/latest/arguide/intro-app-registry.html)

1. Choose **Create SLO**. If you also chose to create one or more alarms, the button name changes to reflect this.

### Create a request-based SLO
<a name="CloudWatch-ServiceLevelObjectives-Create-Request"></a>

Use the following procedure to create a request-based SLO.

**To create a request-based SLO**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Service Level Objectives (SLO)**.

1. Choose **Create SLO**.

1. For **Set Service Level Indicator (SLI)**, do one of the following:
   + To set the SLO on a service operation, all operations, or the dependency of a service, using either of the standard application metrics `Latency` or `Availability`:

     1. For **Type**, choose **Service**.

     1. Select the service that this SLO will monitor.

     1. For **Type**, choose one of the following:
        + **Service Operations** — to create an SLO on a service operation, all operations, or a subset of operations.
        + **Service Dependency** — to create an SLO on a dependency of the service.

     1. If you chose **Service Operations**, select the operation that this SLO will monitor. To create a service-level SLO that monitors the overall health of your service across all operations, select **All Operations**. Otherwise, select a specific operation to monitor.

        To create an SLO that monitors a subset of operations, see [Create a composite SLO on multiple operations](#CloudWatch-ServiceLevelObjectives-Create-Composite).

     1. If you chose **Service Dependency**, do the following:

        1. Under **Select an operation**, select one specific operation or select **All operations** to use the metrics from all operations of this service that calls a dependency.

        1. Under **Select a dependency**, search and select the required dependency for which you want to measure the reliability.

           After you select the dependency, you can view the updated graph and historical data based on the dependency.

     1. For **Select a calculation method**, choose **Requests**.

     1. The **Select service** and **Select operation** drop-downs are populated by services and operations that have been active within the past 24 hours.

     1. Choose either **Availability** or **Latency**. If you choose **Latency**, set the threshold.
   + To set the SLO on any CloudWatch metric or a CloudWatch metric math expression:

     1. For **Type**, choose **CloudWatch Metric**.

     1. For **Define target requests**, do the following:

        1. Choose whether you want to measure **Good Requests** or **Bad Requests**.

        1. Choose **Select CloudWatch metric**. This metric will be the numerator of the ratio of target requests to total requests. If you use a latency metric, use the **Trimmed count (TC)** statistics. If the threshold is 9 ms and you're using the less than (<) comparison operator, then use threshold TC (:threshold - 1). For more information about TC, see [Syntax](Statistics-definitions.md#Statistics-syntax).

           The **Select metric** screen appears. Use the **Browse** or **Query** tabs to find the metric you want, or create a metric math expression. 

     1. For **Define total requests**, choose the CloudWatch metric that you want to use for the source. This metric will be the denominator of the ratio of target requests to total requests.

        The **Select metric** screen appears. Use the **Browse** or **Query** tabs to find the metric you want, or create a metric math expression. 

        After you select the metric that you want, choose the **Graphed metrics** tab and select the **Statistic** and **Period** to use for the SLO. Then choose **Select metric**.

        If you use a latency metric which emits one data point per request, use the **Sample count statistics** to count the number of total requests.

        For more information about these screens, see [Graph a metric](graph_a_metric.md) and [Add a math expression to a CloudWatch graph](using-metric-math.md#adding-metrics-expression-console). 

1. Enter a name for the SLO. Including the name of a service or operation, along with appropriate keywords such as latency or availability, will help you quickly identify what the SLO status indicates during triage.

1. Set the **interval** and **attainment goal** for the SLO. For more information about intervals and attainment goals and how they work together, see [SLO concepts](#CloudWatch-ServiceLevelObjectives-concepts).

1. (Optional) For **Set SLO burn rates** do the following:
   + Set the length (in minutes) of the look-back window for the burn rate. For information about how to choose this length, see [Walkthroughs for burn rate alarms](#ServiceLevelObjectives-burnrate-examples).
   + To create more burn rates for this SLO, choose **Add more burn rates** and set the look-back window for the additional burn rates.

1. (Optional) Create burn rate alarms by doing the following:
   + Under **Set burn rate alarms** select the check box for each burn rate that you want to create an alarm for. For each of these alarms, do the following:
     + Specify the Amazon SNS topic to use for notifications when the alarm goes into ALARM state.
     + Either set a burn rate threshold or specify the percentage of the estimated total budget burnt in the last look-back window you want to stay below. If you set the percentage of estimated total budget burned, the burn rate threshold is calculated for you and used in the alarm. To either decide what threshold to set or to understand how this option is used to compute the burn rate threshold, see [Determine the appropriate threshold for a burn rate alarm](#ServiceLevelObjectives-calculate-threshold). 

1. (Optional) Set one or more CloudWatch alarms or a warning threshold for the SLO. 

   1. CloudWatch alarms can use Amazon SNS to proactively notify you if an application is unhealthy based on its SLI performance. 

      To create an alarm, select one of the alarm check boxes and enter or create the Amazon SNS topic to use for notifications when the alarm goes into `ALARM` state. For more information about CloudWatch alarms, see [Using Amazon CloudWatch alarms](CloudWatch_Alarms.md). Creating alarms incurs charges. For more information about CloudWatch pricing, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/).

   1. If you set a warning threshold, it appears in Application Signals screens to help you identify SLOs that are in danger of being unmet, even if they're currently healthy. 

      To set a warning threshold, enter the threshold value in **Warning threshold**. When the SLO's error budget is lower than the warning threshold, the SLO is marked with **Warning** in several Application Signals screens. Warning thresholds also appear on error budget graphs. You can also create an **SLO warning alarm** that's based on the warning threshold.

1. (Optional) For **Set SLO time window exclusion**, do the following:
   + Under **Exclude time window**, set the time window to be excluded from the SLO performance metrics.

     You can choose **Set time window** and enter the **Start window** for every hour or month or you can choose **Set time window with CRON** and enter the CRON expression.
   + Under **Repeat**, set if this time window exclusion is recurring or not.
   + (Optional) Under **Add reason**, you can choose to enter a reason for the time window exclusion. For example, scheduled maintenance.
   + Select **Add time window** to add upto 10 time exclusion windows.

1. To add tags to this SLO, choose the **Tags** tab and then choose **Add new tag**. Tags can help you manage, identify, organize, search for, and filter resources. For more information about tagging, see [ Tagging your AWS resources](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html). 
**Note**  
If the application this SLO is related to is registered in AWS Service Catalog AppRegistry, you can use the `awsApplication` tag to associate this SLO with that application in AppRegistry. For more information, see [ What is AppRegistry?](https://docs.aws.amazon.com/servicecatalog/latest/arguide/intro-app-registry.html)

1. Choose **Create SLO**. If you also chose to create one or more alarms, the button name changes to reflect this.

### Create an SLO on an app monitor
<a name="CloudWatch-ServiceLevelObjectives-Create-AppMonitor"></a>

You can create SLOs to monitor the performance of your CloudWatch RUM app monitors. This allows you to track real user experience metrics and make sure your web and mobile applications meet performance goals. SLOs on app monitors use request-based evaluation, which measures the ratio of good requests to total requests.

**To create an SLO on an app monitor**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Service Level Objectives (SLO)**.

1. Choose **Create SLO**.

1. For **Set Service Level Indicator (SLI)**, choose **RUM AppMonitor**.

1. Select the app monitor that this SLO will monitor from the dropdown list. The list shows the app monitor name along with the supported platform (Web, iOS, or Android).

1. (Optional) Select a specific page or screen to monitor. If you don't select a page, the SLO will monitor all pages for the app monitor.

1. For **Select metric**, choose the metric to use for the SLI. The available metrics depend on the platform:
   + For web applications: `PerformanceNavigationDuration`, `JSErrorCount`, `Http4xxCount`, and `Http5xxCount`
   + For mobile applications (iOS and Android): `ScreenLoadTime`, `CrashCount`, `Http4xxCount`, and `Http5xxCount`

1. For **Set condition**, select a comparison operator and threshold for the SLO to use as the indicator of success.

1. Enter a name for the SLO. Including the app monitor name and appropriate keywords will help you quickly identify what the SLO status indicates during triage.

1. Set the **interval** and **attainment goal** for the SLO. For more information, see [SLO concepts](#CloudWatch-ServiceLevelObjectives-concepts).

1. (Optional) Configure burn rates and alarms as needed. For more information, see [Calculate burn rates and optionally set burn rate alarms](#CloudWatch-ServiceLevelObjectives-burn).

1. (Optional) Set time window exclusions if needed.

1. (Optional) Add tags to help organize and identify this SLO.

1. Choose **Create SLO**.

### Create an SLO on a canary
<a name="CloudWatch-ServiceLevelObjectives-Create-Canary"></a>

You can create SLOs to monitor the performance of your CloudWatch Synthetics canaries. This allows you to track synthetic monitoring results and make sure your endpoints and APIs meet availability and performance goals. SLOs on canaries use period-based evaluation, where each canary run is treated as a discrete evaluation period.

**To create an SLO on a canary**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Service Level Objectives (SLO)**.

1. Choose **Create SLO**.

1. For **Set Service Level Indicator (SLI)**, choose **Synthetics Canary**.

1. Select the canary that this SLO will monitor from the dropdown list.

1. For **Select metric**, choose either `SuccessPercent` or `Duration`:
   + `SuccessPercent` measures the percentage of successful canary runs
   + `Duration` measures how long each canary run takes to complete

1. For **Set condition**, select a comparison operator and threshold for the SLO to use as the indicator of success.

1. Enter a name for the SLO. Including the canary name and appropriate keywords will help you quickly identify what the SLO status indicates during triage.

1. Set the **interval** and **attainment goal** for the SLO. For more information, see [SLO concepts](#CloudWatch-ServiceLevelObjectives-concepts).

1. (Optional) Configure burn rates and alarms as needed. For more information, see [Calculate burn rates and optionally set burn rate alarms](#CloudWatch-ServiceLevelObjectives-burn).

1. (Optional) Set time window exclusions if needed.

1. (Optional) Add tags to help organize and identify this SLO.

1. Choose **Create SLO**.

### Create a composite SLO on multiple operations
<a name="CloudWatch-ServiceLevelObjectives-Create-Composite"></a>

You can create a composite SLO that monitors the `Availability` metric across a subset of operations for a service. This is useful when you want to track the reliability of a group of related operations together, rather than monitoring a single operation or all operations.

Composite SLOs support both period-based and request-based evaluation. You can select between 2 and 20 operations to include. There are two ways to select operations:
+ *Explicit selection* — Manually pick individual operations from the dropdown.
+ *Pattern matching* — Use a prefix or regular expression to automatically match operations by name.

**Note**  
Composite SLOs support only the `Availability` metric. The `Latency` metric is not available for composite SLOs.

**To create a composite SLO**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Service Level Objectives (SLO)**.

1. Choose **Create SLO**.

1. For **Set Service Level Indicator (SLI)**, for **Type**, choose **Service**.

1. Select the service that this SLO will monitor.

1. For **Type**, choose **Service Operations**.

1. Select the operations to include in this composite SLO. Do one of the following:
   + To manually select operations, choose multiple operations from the **Operation** dropdown. You can select between 2 and 20 operations.

     The selected operations appear as tokens below the dropdown. You can remove an operation by choosing the dismiss icon on its token.
   + To select operations by pattern, select the **Use pattern matching** checkbox. Then do the following:

     1. For **Pattern type**, choose either **Prefix** or **Regular expression**.
        + **Prefix** matches all operations whose names start with the text you enter. For example, entering `Invoke` matches operations named `InvokeFunction`, `InvokeAsync`, and so on.
        + **Regular expression** matches all operations whose names match the regex pattern you enter. For example, entering `^Invoke.*` matches the same operations as the prefix example.

     1. Enter the pattern in the **Pattern** field. The console displays the matched operations as tokens below the field so you can verify the results.

   After you select operations, the metric is automatically set to **Availability**.

1. For **Select a calculation method**, choose either **Periods** or **Requests**.

1. If you selected **Periods**, set the period length and the availability threshold for this SLO.

1. Enter a name for the SLO, or use the auto-generated name. The auto-generated name includes the service name and the word "composite" to help you identify it.

1. Set the **interval** and **attainment goal** for the SLO. For more information about intervals and attainment goals and how they work together, see [SLO concepts](#CloudWatch-ServiceLevelObjectives-concepts).

1. (Optional) Configure burn rates and alarms as needed. For more information, see [Calculate burn rates and optionally set burn rate alarms](#CloudWatch-ServiceLevelObjectives-burn).

1. (Optional) Set one or more CloudWatch alarms or a warning threshold for the SLO.

1. (Optional) Set time window exclusions if needed.

1. (Optional) Add tags to help organize and identify this SLO.

1. Choose **Create SLO**.

## Use SLO recommendations
<a name="CloudWatch-ServiceLevelObjectives-Recommendations"></a>

Application Signals can provide recommendations for your SLO configuration based on historical metric data from the last 30 days. When you provide basic information about your service and the type of SLO you want to create, Application Signals analyzes your metric data and suggests optimal values for the metric threshold, SLO goal, and burn rate windows.

To receive SLO recommendations, you must provide the following information:
+ Choose either **Service Operation** or **Service Dependency**:
  + For **Service Operation**, specify the service and operation
  + For **Service Dependency**, specify the service, operation (or all operations), and dependency
+ The SLO evaluation type: either *period-based* or *request-based*
+ The type of standard application metric: either `Latency` or `Availability`

Based on this information and your service's historical performance data, Application Signals recommends the following SLO configuration parameters:
+ **Metric threshold** - The performance threshold for your SLI, calculated based on your service's actual performance over the last 30 days.
+ **SLO goal** - The suggested attainment goal percentage that aligns with your service's historical reliability.
+ **Burn rate windows** - Recommended look-back window durations for monitoring how quickly your service consumes its error budget.

You can accept the recommended values or adjust them based on your specific business requirements. The recommendations provide a data-driven starting point for configuring SLOs that reflect your service's actual performance characteristics.

## View and triage SLO status
<a name="CloudWatch-ServiceLevelObjectives-Triage"></a>

You can quickly see the health of your SLOs using either the **Service Level Objectives** or the **Services** options in the CloudWatch console. The **Services** view provides an at-a-glance view of the ratio of unhealthy services, calculated based on SLOs that you have set. For more information about using the **Services** option, see [Monitor the operational health of your applications with Application Signals](Services.md).

The **Service Level Objectives** view provides a macro view of your organization. You can see the met and unmet SLOs as a whole. This gives you a view of how many of your services and operations are performing to your expectations over longer periods of time, according to the SLIs that you chose.

**To view all of your SLOs using the Service Level Objectives view**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Service Level Objectives (SLO)**.

   The **Service Level Objectives (SLO)** list appears.

   You can quickly see the current status of your SLOs in the **SLI status** column. To sort the SLOs so that all the unhealthy ones are at the top of the list, choose the **SLI status** column until the unhealthy SLOs are all at the top.

   The SLO table has the following default columns. You can adjust which columns are displayed by choosing the gear icon above the list. For more information about goals, SLIs, attainment, and intervals, see [SLO concepts](#CloudWatch-ServiceLevelObjectives-concepts).
   + The name of the SLO.
   + The **Goal** column displays the percentage of periods during each interval that must successfully meet the SLI threshold for the SLO goal to be met. It also displays the interval length for the SLO.
   + The **SLI status** displays whether the current operational state of the application is healthy or not. If any period during the currently selected time range was unhealthy for the SLO, then the **SLI status** displays **Unhealthy**.
   + If this SLO is configured to monitor a dependency, the **Dependency** and **Remote Operation** columns will show the details about that dependency relationship.
   + The **Ending attainment** is the attainment level achieved as of the end of the selected time range. Sort by this column to see the SLOs that are most in danger of not being met.
   + The **Attainment delta** is the difference in attainment level between the start and end of the selected time range. A negative delta means that the metric is trending in a downward direction. Sort by this column to see the latest trends of the SLOs.
   + The **Ending error budget (%)** is the percentage of total time in the period that can have unhealthy periods and still have the SLO be achieved successfully. If you set this to 5%, and the SLI is unhealthy in 5% or fewer of the remaining periods in the interval, the SLO is still achieved successfully.
   + The **Error budget delta** is the difference in error budget between the start and end of the selected time range. A negative delta means that the metric is trending in a failing direction.
   + The **Ending error budget (time)** is the amount of actual time in the interval that can be unhealthy and still have the SLO be achieved successfully. For example, if this is 14 minutes, then if the SLI is unhealthy for fewer than 14 minutes during the remaining interval, the SLO will still be achieved successfully.
   + The ** Ending error budget (requests)** is the amount of requests in the interval that can be unhealthy and still have the SLO be achieved successfully. For request-based SLOs, this value is dynamic and can fluctuate as the cumulative total number of requests changes over time.
   + The **Service**, **Operation**, and **Type** columns display information about what service and operation this SLO is set for.

1. To see the attainment and error budget graphs for an SLO, choose the radio button next to the SLO name.

   The graphs at the top of the page display the **SLO attainment** and **Error budget** status. A graph about the SLI metric associated with this SLO is also displayed.

1. To further triage an SLO that is not meeting its goal, choose the service name, operation name, or dependency name associated with that SLO. You are taken to the details page where you can triage further. For more information, see [View detailed service activity and operational health with the service detail page](ServiceDetail.md).

1. To change the time range of the charts and tables on the page, choose a new time range near the top of the screen.

## Edit an existing SLO
<a name="CloudWatch-ServiceLevelObjectives-Edit"></a>

Follow these steps to edit an existing SLO. When you edit an SLO, you can change only the threshold, interval, attainment goal, and tags. To change other aspects such as service, operation, or metric, create a new SLO instead of editing an existing one.

Changing part of an SLO core configuration, such as period or threshold, invalidates all the previous data points and assessments about attainment and health. It effectively deletes and re-creates the SLO.

**Note**  
If you edit an SLO, alarms associated with that SLO are not automatically updated. You might need to update the alarms to keep them in sync with the SLO.

**To edit an existing SLO**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Service Level Objectives (SLO)**.

1. Choose the radio button next to the SLO that you want to edit, and choose **Actions**, **Edit SLO**.

1. Make your changes, then choose **Save changes**.

## Delete an SLO
<a name="CloudWatch-ServiceLevelObjectives-Delete"></a>

Follow these steps to delete an existing SLO. 

**Note**  
When you delete an SLO, alarms associated with that SLO are not automatically deleted. You'll need to delete them yourself. For more information, see [Managing alarms](Manage-CloudWatch-Alarm.md).

**To delete an SLO**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Service Level Objectives (SLO)**.

1. Choose the radio button next to the SLO that you want to edit, and choose **Actions**, **Delete SLO**.

1. Choose **Confirm**.