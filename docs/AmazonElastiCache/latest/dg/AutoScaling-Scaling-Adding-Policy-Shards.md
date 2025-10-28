# Adding a scaling

policy

You can add a scaling policy using the AWS Management Console.

###### To add an Auto Scaling policy to an ElastiCache for Valkey and Redis OSS cluster

1.  Sign in to the AWS Management Console and open the Amazon ElastiCache console at [https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/ "https://console.aws.amazon.com/elasticache/").
2.  In the navigation pane, choose **Valkey** or **Redis OSS**.
3.  Choose the cluster that you want to add a policy to (choose the cluster
    name and not the button to its left).
4.  Choose the **Auto Scaling policies** tab.
5.  Choose **add dynamic scaling**.
6.  For **Policy name** enter a policy name.
7.  For **Scalable Dimension** choose
    **shards**.
8.  For the target metric, choose one of the following:
    - **Primary CPU Utilization** to create a policy
      based on the average CPU utilization.
    - **Memory** to create a policy based on the
      average database memory.
    - **Capacity** to create a policy based on average
      database capacity usage. The Capacity metric includes memory and SSD
      utilization for data-tiered instances, and memory utilization for
      all other instance types.

9.  For the target value, choose a value greater than or equal to 35 and less
    than or equal to 70. Auto scaling will maintain this value for the selected
    target metric across your ElastiCache shards:

        * **Primary CPU Utilization**: maintains target
         value for `EngineCPUUtilization` metric on primary nodes.
        * **Memory**: maintains target value for
         `DatabaseMemoryUsageCountedForEvictPercentage` metric
        * **Capacity** maintains target value for
         `DatabaseCapacityUsageCountedForEvictPercentage`
         metric,

    Cluster shards are added or removed to keep the metric close to the
    specified value.

10. (Optional) Scale-in or scale-out cooldown periods are not supported from
    the console. Use the AWS CLI to modify the cooldown values.
11. For **Minimum capacity**, type the minimum number of
    shards that the ElastiCache Auto Scaling policy is required to maintain.
12. For **Maximum capacity**, type the maximum number of
    shards that the ElastiCache Auto Scaling policy is required to maintain. This
    value must be less than or equal to 250.
13. Choose **Create**.
