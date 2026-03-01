# Use scheduled actions to override forecast values for Amazon ECS

Sometimes, you might have additional information about your future application
requirements that the forecast calculation is unable to take into account. For example,
forecast calculations might underestimate the tasks needed for an upcoming marketing event.
You can use scheduled actions to temporarily override the forecast during future time
periods. The scheduled actions can run on a recurring basis, or at a specific date and time
when there are one-time demand fluctuations.

For example, you can create a scheduled action with a higher number of tasks than what is
forecasted. At runtime, Amazon ECS updates the minimum number of tasks in your service. Because
predictive scaling optimizes for the number of tasks, a scheduled action with a minimum
number of tasks that is higher than the forecast values is honored. This prevents the number
of tasks from being less than expected. To stop overriding the forecast, use a second
scheduled action to return the minimum number of tasks to its original setting.

The following procedure outlines the steps for overriding the forecast during future
time periods.

###### Topics

- [Step 1: (Optional) Analyze time series data](#analyzing-time-series-data "#analyzing-time-series-data")
- [Step 2: Create two scheduled actions](#scheduling-capacity "#scheduling-capacity")

###### Important

This topic assumes that you are trying to override the forecast to scale to a higher
capacity than what is forecasted. If you need to temporarily decrease the number of
tasks without interference from a predictive scaling policy, use _forecast only_ mode instead. While in forecast only mode, predictive
scaling will continue to generate forecasts, but it will not automatically increase the
number of tasks. You can then monitor resource utilization and manually decrease the
number of tasks as needed.

## Step 1: (Optional) Analyze time series data

Start by analyzing the forecast time series data. This is an optional step, but it
is helpful if you want to understand the details of the forecast.

1. **Retrieve the forecast**

After the forecast is created, you can query for a specific time period in
the forecast. The goal of the query is to get a complete view of the time
series data for a specific time period.

Your query can include up to two days of future forecast data. If you have
been using predictive scaling for a while, you can also access your past
forecast data. However, the maximum time duration between the start and end
time is 30 days.

To get the forecast using the [get-predictive-scaling-forecast](../../../cli/latest/reference/autoscaling/get-predictive-scaling-forecast.md "../../../cli/latest/reference/autoscaling/get-predictive-scaling-forecast.md") AWS CLI command, provide the
following parameters in the command:

    * Enter the name of the cluster name in the `resource-id`
     parameter.
    * Enter the name of the policy in the `--policy-name`
     parameter.
    * Enter the start time in the `--start-time` parameter to
     return only forecast data for after or at the specified time.
    * Enter the end time in the `--end-time` parameter to
     return only forecast data for before the specified time.

```
aws application-autoscaling get-predictive-scaling-forecast \
    --service-namespace ecs \
    --resource-id service/MyCluster/test \
    --policy-name `cpu40-predictive-scaling-policy` \
    --scalable-dimension ecs:service:DesiredCount \
    --start-time "`2021-05-19T17:00:00Z`" \
    --end-time "`2021-05-19T23:00:00Z`"
```

If successful, the command returns data similar to the following example.

```
{
    "LoadForecast": [
        {
            "Timestamps": [
                "2021-05-19T17:00:00+00:00",
                "2021-05-19T18:00:00+00:00",
                "2021-05-19T19:00:00+00:00",
                "2021-05-19T20:00:00+00:00",
                "2021-05-19T21:00:00+00:00",
                "2021-05-19T22:00:00+00:00",
                "2021-05-19T23:00:00+00:00"
            ],
            "Values": [
                153.0655799339254,
                128.8288551285919,
                107.1179447150675,
                197.3601844551528,
                626.4039934516954,
                596.9441277518481,
                677.9675713779869
            ],
            "MetricSpecification": {
                "TargetValue": 40.0,
                "PredefinedMetricPairSpecification": {
                    "PredefinedMetricType": "ASGCPUUtilization"
                }
            }
        }
    ],
    "CapacityForecast": {
        "Timestamps": [
            "2021-05-19T17:00:00+00:00",
            "2021-05-19T18:00:00+00:00",
            "2021-05-19T19:00:00+00:00",
            "2021-05-19T20:00:00+00:00",
            "2021-05-19T21:00:00+00:00",
            "2021-05-19T22:00:00+00:00",
            "2021-05-19T23:00:00+00:00"
        ],
        "Values": [
            2.0,
            2.0,
            2.0,
            2.0,
            4.0,
            4.0,
            4.0
        ]
    },
    "UpdateTime": "2021-05-19T01:52:50.118000+00:00"
}
```

The response includes two forecasts: `LoadForecast` and
`CapacityForecast`. `LoadForecast` shows the
hourly load forecast. `CapacityForecast` shows forecast values
for the capacity that is needed on an hourly basis to handle the forecasted
load while maintaining a `TargetValue` of 40.0 (40% average CPU
utilization). 2. **Identify the target time period**

Identify the hour or hours when the one-time demand fluctuation should
take place. Remember that dates and times shown in the forecast are in
UTC.

## Step 2: Create two scheduled actions

Next, create two scheduled actions for a specific time period when your
application will have a higher than forecasted load. For example, if you have a
marketing event that will drive traffic to your site for a limited period of time,
you can schedule a one-time action to update the minimum capacity when it starts.
Then, schedule another action to return the minimum capacity to the original setting
when the event ends.

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. On the **Clusters** page, choose the cluster.
3. On the cluster details page, in the **Services** section,
   and then choose the service.

The service details page appears. 4. Choose **Service Auto Scaling**.

The policies page appears. 5. Choose **Scheduled actions**, and then choose **Create**.

The **Create Schedule action** page appears. 6. For **Action name**, enter a unique name. 7. For **Time zone**, choose a time zone.

All of the time zones listed are from the IANA Time Zone database. For
more information, see [List of tz database time zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones "https://en.wikipedia.org/wiki/List_of_tz_database_time_zones"). 8. For **Start time**, enter the **Date**
and **Time** the action starts. 9. For **Recurrence**, choose **Once**. 10. Under **Task adjustments**, For Minimum, enter a value less
than or equal to the maximum number of tasks.. 11. Choose **Create scheduled action**.

The policies page appears. 12. Configure a second scheduled action to return the minimum number of tasks to
the original setting at the end of the event. Predictive scaling can scale the
number of tasks only when the value you set for **Minimum** is
lower than the forecast values.

###### To create two scheduled actions for one-time events (AWS CLI)

To use the AWS CLI to create the scheduled actions, use the [put-scheduled-update-group-action](../../../cli/latest/reference/autoscaling/put-scheduled-update-group-action.md "../../../cli/latest/reference/autoscaling/put-scheduled-update-group-action.md") command.

For example, let's define a schedule that maintains a minimum capacity of three
instances on May 19 at 5:00 PM for eight hours. The following commands show how to
implement this scenario.

The first [put-scheduled-update-group-action](../../../cli/latest/reference/autoscaling/put-scheduled-update-group-action.md "../../../cli/latest/reference/autoscaling/put-scheduled-update-group-action.md") command instructs Amazon EC2 Auto Scaling to update
the minimum capacity of the specified Auto Scaling group at 5:00 PM UTC on May 19, 2021.

```
aws autoscaling put-scheduled-update-group-action --scheduled-action-name `my-event-start` \
  --auto-scaling-group-name `my-asg` --start-time "`2021-05-19T17:00:00Z`" --minimum-capacity `3`
```

The second command instructs Amazon EC2 Auto Scaling to set the group's minimum capacity to one
at 1:00 AM UTC on May 20, 2021.

```
aws autoscaling put-scheduled-update-group-action --scheduled-action-name `my-event-end` \
  --auto-scaling-group-name `my-asg` --start-time "`2021-05-20T01:00:00Z`" --minimum-capacity `1`
```

After you add these scheduled actions to the Auto Scaling group, Amazon EC2 Auto Scaling does the
following:

- At 5:00 PM UTC on May 19, 2021, the first scheduled action runs. If the
  group currently has fewer than three instances, the group scales out to
  three instances. During this time and for the next eight hours, Amazon EC2 Auto Scaling can
  continue to scale out if the predicted capacity is higher than the actual
  capacity or if there is a dynamic scaling policy in effect.
- At 1:00 AM UTC on May 20, 2021, the second scheduled action runs. This
  returns the minimum capacity to its original setting at the end of the
  event.

### Scaling based on recurring schedules

To override the forecast for the same time period every week, create two
scheduled actions and provide the time and date logic using a cron expression.

The cron expression format consists of five fields separated by spaces:
[Minute] [Hour] [Day\_of\_Month] [Month\_of\_Year] [Day\_of\_Week]. Fields can contain
any allowed values, including special characters.

For example, the following cron expression runs the action every Tuesday at
6:30 AM. The asterisk is used as a wildcard to match all values for a
field.

```
30 6 * * 2
```

### See also

For more information about how to manage scheduled
actions, see [Use scheduled actions to scale Amazon ECS services](service-autoscaling-schedulescaling.md "service-autoscaling-schedulescaling.md").
