# Evaluate your predictive scaling policies for Amazon ECS

Before you use a predictive scaling policy to scale your services, review the
recommendations and other data for your policy in the Amazon ECS console. This is
important because you don't want a predictive scaling policy to scale your actual
capacity until you know that its predictions are accurate.

If the service is new, allow 24 hours to create the first forecast.

When AWS creates a forecast, it uses historical data. If your service doesn't
have much recent historical data yet, predictive scaling might temporarily backfill the forecast
with aggregates created from the currently available historical aggregates. Forecasts
are backfilled for up to two weeks before a policy's creation date.

## View your predictive

scaling recommendations

For effective analysis, service auto scaling should have at least two predictive scaling
policies to compare. (However, you can still review the findings for a single
policy.) When you create multiple policies, you can evaluate a policy that uses one
metric against a policy that uses a different metric. You can also evaluate the
impact of different target value and metric combinations. After the predictive
scaling policies are created, Amazon ECS immediately starts evaluating which policy
would do a better job of scaling your group.

###### To view your recommendations in the Amazon ECS console

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. On the **Clusters** page, choose the cluster.
3. On the cluster details page, in the **Services** section,
   choose the service.

The service details page appears. 4. Choose **Service auto scaling**. 5. Choose the predictive scaling policy, and then choose
**Actions**, **Predictive Scaling**,
**View recommendation**.

You can view details about a policy along with our recommendation. The
recommendation tells you whether the predictive scaling policy does a better job
than not using it.

If you're unsure whether a predictive scaling policy is appropriate for
your group, review the **Availability impact** and
**Cost impact** columns to choose the right policy. The
information for each column tells you what the impact of the policy is.

    * **Availability impact**: Describes whether the policy
     would avoid negative impact to availability by provisioning enough tasks
     to handle the workload, compared to not using the policy.
    * **Cost impact**: Describes whether the policy would
     avoid negative impact on your costs by not over-provisioning tasks,
     compared to not using the policy. By over-provisioning too much, your
     services are underutilized or idle, which only adds to the cost
     impact.

If you have multiple policies, then a **Best prediction**
tag displays next to the name of the policy that gives the most availability
benefits at lower cost. More weight is given to availability impact. 6. (Optional) To select the desired time period for recommendation results,
choose your preferred value from the **Evaluation period**
dropdown: **2 days**, **1 week**, or
**2 weeks**. By default, the
evaluation period is the last two weeks. A longer evaluation period provides
more data points to the recommendation results. However, adding more data
points might not improve the results if your load patterns have changed,
such as after a period of exceptional demand. In this case, you can get a
more focused recommendation by looking at more recent data.

###### Note

Recommendations are generated only for policies that are in **Forecast
only** mode. The recommendations feature works better when a policy
is in the **Forecast only** mode throughout the evaluation
period. If you start a policy in **Forecast and scale** mode
and switch it to **Forecast only** mode later, the findings for
that policy are likely to be biased. This is because the policy has already
contributed toward the actual capacity.

## Review predictive

scaling monitoring graphs

In the console, you can review the forecast of the previous days, weeks, or months to
visualize how well the policy performs over time. You can also use this information to
evaluate the accuracy of predictions when deciding whether to let a policy scale your
actual number of tasks.

###### To review predictive scaling monitoring graphs in the Amazon ECS

console

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. On the **Clusters** page, choose the cluster.
3. On the cluster details page, in the **Services** section,
   choose the service.

The service details page appears. 4. Choose **Service auto scaling**. 5. Choose the predictive scaling policy, and then choose
**Actions**, **Predictive Scaling**,
**View Graph**. 6. In the **Monitoring** section, you can view your policy's
past and future forecasts for load and capacity against actual values. The
**Load** graph shows load forecast and actual values
for the load metric that you chose. The **Capacity** graph
shows the number of tasks predicted by the policy. It also includes the
actual number of tasks launched. The vertical line separates historical
values from future forecasts. These graphs become available shortly after
the policy is created. 7. (Optional) To change the amount of historical data shown in the chart,
choose your preferred value from the **Evaluation period**
dropdown at the top of the page. The evaluation period does not transform
the data on this page in any way. It only changes the amount of historical
data shown.

###### Compare data in the **Load** graph

Each horizontal line represents a different set of data points reported in
one-hour intervals:

1. **Actual observed load** uses the SUM statistic for your
   chosen load metric to show the total hourly load in the past.
2. **Load predicted by the policy** shows the hourly load
   prediction. This prediction is based on the previous two weeks of actual
   load observations.

###### Compare data in the **Capacity** graph

Each horizontal line represents a different set of data points reported in
one-hour intervals:

1. **Actual observed number of tasks** shows your Amazon ECS service
   actual capacity in the past, which depends on your other scaling policies and
   minimum group size in effect for the selected time period.
2. **Capacity predicted by the policy** shows the baseline
   capacity that you can expect to have at the beginning of each hour when the
   policy is in **Forecast and scale** mode.
3. **Inferred required number of tasks** shows the ideal number
   of tasks in your service to maintain the scaling metric at the target value you
   chose.
4. **Minimum number of tasks** shows the minimum number of tasks
   in your service.
5. **Maximum capacity** shows the maximum number of tasks in
   your service.

For the purpose of calculating the inferred required capacity, we begin by assuming
that each task is equally utilized at a specified target value. In practice, the number
of tasks are not equally utilized. By assuming that utilization is uniformly spread
between tasks, however, we can make a likelihood estimate of the amount of capacity that
is needed. The requirement for thenumber of tasks is then calculated to be inversely
proportional to the scaling metric that you used for your predictive scaling policy. In
other words, as the number of tasks increase, the scaling metric decreases at the same
rate. For example, if the number of tasks doubles, the scaling metric must decrease by
half.

The formula for the inferred required capacity:

`sum of (actualServiceUnits*scalingMetricValue)/(targetUtilization)`

For example, we take the `actualServiceUnits` (`10`) and the
`scalingMetricValue` (`30`) for a given hour. We then take the
`targetUtilization` that you specified in your predictive scaling policy
(`60`) and calculate the inferred required capacity for the same hour.
This returns a value of `5`. This means that five is the inferred amount of
capacity required to maintain capacity in direct inverse proportion to the target value
of the scaling metric.

###### Note

Various levers are available for you to adjust and improve the cost savings
and availability of your application.

- You use predictive scaling for the baseline capacity and dynamic
  scaling to handle additional capacity. Dynamic scaling works
  independently from predictive scaling, scaling in and out based on
  current utilization. First, Amazon ECS calculates the recommended number
  of tasks for each non-scheduled scaling policy. Then, it scales based on
  the policy that provides the largest number of tasks.
- To allow scale in to occur when the load decreases, your service should
  always have at least one dynamic scaling policy with the scale-in portion
  enabled.
- You can improve scaling performance by making sure that your minimum and
  maximum capacity are not too restrictive. A policy with a recommended number
  of tasks that does not fall within the minimum and maximum capacity range
  will be prevented from scaling in and out.
