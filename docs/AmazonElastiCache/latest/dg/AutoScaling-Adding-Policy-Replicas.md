# Adding a scaling policy

You can add a scaling policy using the AWS Management Console.

###### Adding a scaling policy using the AWS Management Console

To add an auto scaling policy to ElastiCache for Valkey and Redis OSS

1. Sign in to the AWS Management Console and open the Amazon ElastiCache console at [https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/ "https://console.aws.amazon.com/elasticache/").
2. In the navigation pane, choose **Valkey** or **Redis OSS**.
3. Choose the cluster that you want to add a policy to (choose the cluster
   name and not the button to its left).
4. Choose the **Auto Scaling policies** tab.
5. Choose **add dynamic scaling**.
6. Under **Scaling policies**, choose **Add dynamic
   scaling**.
7. For **Policy Name**, enter the policy name.
8. For **Scalable Dimension**, select
   **Replicas** from dialog box.
9. For the target value, type the Avg percentage of CPU utilization that you
   want to maintain on ElastiCache Replicas. This value must be >=35 and
   <=70. Cluster replicas are added or removed to keep the metric close to
   the specified value.
10. (Optional) scale-in or scale-out cooldown periods are not supported from
    the Console. Use the AWS CLI to modify the cool down values.
11. For **Minimum capacity**, type the minimum number of
    replicas that the ElastiCache Auto Scaling policy is required to maintain.
12. For **Maximum capacity**, type the maximum number of
    replicas the ElastiCache Auto Scaling policy is required to maintain. This value
    must be >=5.
13. Choose **Create**.
