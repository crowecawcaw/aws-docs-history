# Modifying Amazon ECS account

settings

Modify your account settings to access Amazon ECS features.

The `guardDutyActivate` parameter is read-only in Amazon ECS and indicates whether
Runtime Monitoring is turned on or off by your security administrator in your
Amazon ECS account. GuardDuty controls this account setting on your behalf. For more information, see [Protecting Amazon ECS workloads with Runtime Monitoring](ecs-guard-duty-integration.md "ecs-guard-duty-integration.md").

###### Important

The `dualStackIPv6`, `fargateFIPSMode` and the
`fargateTaskRetirementWaitPeriod` account settings can only be viewed
or changed using the AWS CLI.

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. In the navigation bar at the top, select the Region for which to view your
   account settings.
3. In the navigation page, choose **Account Settings**.
4. Choose **Update**.
5. (Optional) To increase or decrease the number of tasks that you can run in
   the awsvpc network mode for each EC2 instance, under **AWSVPC
   Trunking**, select **AWSVPC Trunking**.
6. (Optional) To use, or stop using CloudWatch Container Insights by default for clusters, under
   **CloudWatch Container Insights observability**, choose one of the following
   options:
   - To use Container Insights with enhanced observability, choose
     **Container Insights with enhanced
     observability**.
   - To use Container Insights, choose **Container
     Insights**.
   - To stop using Container Insights, choose **Turned
     off**.

7. (Optional) To enable or disable tagging authorization, under
   **Resource Tagging Authorization**, select or clear
   **Resource Tagging Authorization**.
8. (Optional) To configure a default log driver mode for when a log delivery
   mode isn't defined in a container's `logConfiguration`, under **Default log driver mode**, choose one of
   the following options:
   - To set the default log driver mode as `blocking`, choose
     **Blocking**.
   - To set the default log driver mode as `non-blocking`,
     choose **Non-blocking**.

9. Choose **Save changes**.
10. On the confirmation screen, choose **Confirm** to save the
    selection.

## Next steps

If you turned on Container Insights with enhanced observability or Container
Insights, you can optionally update your existing clusters to use the feature. For
more information, see [Updating an Amazon ECS
cluster](update-cluster-v2.md "update-cluster-v2.md").
