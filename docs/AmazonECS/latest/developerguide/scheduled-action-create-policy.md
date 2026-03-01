# Create a scheduled action for Amazon ECS service auto scaling

Create a scheduled action to have Amazon ECS increase or decrease the number of tasks that your
service runs based on the date and time.

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. On the **Clusters** page, choose the cluster.
3. On the cluster details page, in the **Services** section,
   choose the service.

The service details page appears. 4. Choose **Service auto scaling**.

The service auto scaling page appears. 5. If you haven't configured service auto scaling, choose **Set the
number of tasks**.

The **Amazon ECS service task count** section appears.

Under **Amazon ECS service task count**, choose **Use
service auto scaling to adjust your service's desired task
count**.

The **Task count section** appears.

    1. For **Minimum number of tasks**, enter the lower limit of the
     number of tasks for service auto scaling to use. The desired count will not go
     below this count.
    2. For **Maximum**, enter the upper limit of the
     number of tasks for service auto scaling to use. The desired count will not go
     above this count.
    3. Choose **Choose Save**.


    The policies page appears.

6. Choose **Scheduled actions**, and then choose **Create**.

The **Create Scheduled action** page appears. 7. For **Action name**, enter a unique name. 8. For **Time zone**, choose a time zone.

All of the time zones listed are from the IANA Time Zone database. For
more information, see [List of tz database time zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones "https://en.wikipedia.org/wiki/List_of_tz_database_time_zones"). 9. For **Start time**, enter the **Date**
and **Time** the action starts.

If you chose a recurring schedule, the start time defines when the first
scheduled action in the recurring series runs. 10. For **Recurrence**, choose one of the available
options.

    * To scale on a recurring schedule, choose how often Amazon ECS runs the
     scheduled action.




    	+ If you choose an option that begins with
    	 **Rate**, the cron expression is
    	 created for you.
    	+ If you choose **Cron**, enter a cron
    	 expression that specifies when to perform the action.
    * To scale only once, choose **Once**.

11. Under **Task adjustments**, do the following:
    - For **Minimum**, enter the minumum number of
      tasks the service should run.
    - For **Maximum**, enter the maximum number of
      tasks the service should run.

12. Choose **Create scheduled action**.
    Use the AWS CLI as follows to configure scheduled scaling policies for your service.
    Replace each `user input placeholder` with your own
    information.

###### Example: To scale one time only

Use the following [put-scheduled-action](../../../cli/latest/reference/application-autoscaling/put-scheduled-action.md "../../../cli/latest/reference/application-autoscaling/put-scheduled-action.md") command with the `--start-time
 "YYYY-MM-DDThh:mm:ssZ"` and and either or both of the
`--MinCapacity` and `--MaxCapacity` options.

```
aws application-autoscaling put-scheduled-action --service-namespace ecs \
  --resource-id service/`my-cluster`/`my-service` \
  --scheduled-action-name `my-one-time-schedule` \
  --start-time `2021-01-30T12:00:00` \
  --scalable-target-action MinCapacity=`3`,MaxCapacity=`10`
```

###### Example: To schedule scaling on a recurring schedule

Use the following [put-scheduled-action](../../../cli/latest/reference/application-autoscaling/put-scheduled-action.md "../../../cli/latest/reference/application-autoscaling/put-scheduled-action.md") command. Replace the
`user input` with your values.

```
aws application-autoscaling put-scheduled-action --service-namespace ecs \
  --resource-id service/`my-cluster`/`my-service` \
  --scheduled-action-name `my-recurring-action` \
  --schedule "rate(`5 hours`)" \
  --start-time `2021-01-30T12:00:00` \
  --end-time `2021-01-31T22:00:00` \
  --scalable-target-action MinCapacity=`3`,MaxCapacity=`10`
```

The specified recurrence schedule runs based on the UTC time zone. To specify a
different time zone, include the `--time-zone` option and the name of the
IANA time zone, as in the following example.

```
--time-zone "`America/New_York`"
```

For more information, see [List of tz database time zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones "https://en.wikipedia.org/wiki/List_of_tz_database_time_zones").
