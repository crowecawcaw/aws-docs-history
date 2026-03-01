# Scheduled scaling

Scaling based on a schedule enables you to scale your application in response to
predictable changes in demand. To use scheduled scaling, you create scheduled
actions, which tell ElastiCache for Valkey and Redis OSS to perform scaling activities at specific times. When you
create a scheduled action, you specify an existing cluster, when the scaling
activity should occur, minimum capacity, and maximum capacity. You can create
scheduled actions that scale one time only or that scale on a recurring schedule.

You can only create a scheduled action for clusters that already exist.
You can't create a scheduled action at the same time that you create a
cluster.

For more information on terminology for scheduled action creation, management, and
deletion, see [Commonly used commands for scheduled action creation, management, and deletion](../../../autoscaling/application/userguide/application-auto-scaling-scheduled-scaling.md#scheduled-scaling-commonly-used-commands "../../../autoscaling/application/userguide/application-auto-scaling-scheduled-scaling.md#scheduled-scaling-commonly-used-commands")

###### To create on a recurring schedule:

1. Sign in to the AWS Management Console and open the Amazon ElastiCache console at [https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/ "https://console.aws.amazon.com/elasticache/").
2. In the navigation pane, choose **Valkey** or **Redis OSS**.
3. Choose the cluster that you want to add a policy for.
4. Choose the **Manage Auto Scaling policie** from the
   **Actions** dropdown.
5. Choose the **Auto Scaling policies** tab.
6. In the **Auto scaling policies** section, the
   **Add Scaling policy** dialog box appears. Choose
   **Scheduled scaling**.
7. For **Policy Name**, enter the policy name.
8. For **Scalable Dimension**, choose
   **Shards**.
9. For **Target Shards**, choose the value.
10. For **Recurrence**, choose
    **Recurring**.
11. For **Frequency**, choose the respective value.
12. For **Start Date** and **Start time**,
    choose the time from when the policy will go into effect.
13. Choose **Add Policy**.

###### To create a one-time scheduled action:

1. Sign in to the AWS Management Console and open the Amazon ElastiCache console at [https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/ "https://console.aws.amazon.com/elasticache/").
2. In the navigation pane, choose **Valkey** or **Redis OSS**.
3. Choose the cluster that you want to add a policy for.
4. Choose the **Manage Auto Scaling policie** from the
   **Actions** dropdown.
5. Choose the **Auto Scaling policies** tab.
6. In the **Auto scaling policies** section, the
   **Add Scaling policy** dialog box appears. Choose
   **Scheduled scaling**.
7. For **Policy Name**, enter the policy name.
8. For **Scalable Dimension**, choose
   **Shards**.
9. For **Target Shards**, choose the value.
10. For **Recurrence**, choose **One Time**.
11. For **Start Date** and **Start time**,
    choose the time from when the policy will go into effect.
12. For **End Date** choose the date until when the policy
    would be in effect.
13. Choose **Add Policy**.

###### To delete a scheduled action

1. Sign in to the AWS Management Console and open the Amazon ElastiCache console at [https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/ "https://console.aws.amazon.com/elasticache/").
2. In the navigation pane, choose **Valkey** or **Redis OSS**.
3. Choose the cluster that you want to add a policy for.
4. Choose the **Manage Auto Scaling policie** from the
   **Actions** dropdown.
5. Choose the **Auto Scaling policies** tab.
6. In the **Auto scaling policies** section, choose the auto
   scaling policy, and then choose **Delete** from the
   **Actions** dialog.
   **To manage scheduled scaling using the AWS CLI**

Use the following application-autoscaling APIs:

- [put-scheduled-action](../../../cli/latest/reference/autoscaling/put-scheduled-action.md "../../../cli/latest/reference/autoscaling/put-scheduled-action.md")
- [describe-scheduled-actions](../../../cli/latest/reference/autoscaling/describe-scheduled-actions.md "../../../cli/latest/reference/autoscaling/describe-scheduled-actions.md")
- [delete-scheduled-action](../../../cli/latest/reference/autoscaling/delete-scheduled-action.md "../../../cli/latest/reference/autoscaling/delete-scheduled-action.md")

## Use CloudFormation to create a scheduled action

This snippet shows how to create a target tracking policy and apply it to an
[AWS::ElastiCache::ReplicationGroup](../../../AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.md") resource using the [AWS::ApplicationAutoScaling::ScalableTarget](../../../AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.md") resource. It uses the
[Fn::Join](../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-join.md "../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-join.md") and [Ref](../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.md "../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.md") intrinsic functions to construct the `ResourceId`
property with the logical name of the
`AWS::ElastiCache::ReplicationGroup` resource that is specified
in the same template.

```

ScalingTarget:
   Type: 'AWS::ApplicationAutoScaling::ScalableTarget'
   Properties:
     MaxCapacity: 3
     MinCapacity: 1
     ResourceId: !Sub replication-group/${logicalName}
     ScalableDimension: 'elasticache:replication-group:NodeGroups'
     ServiceNamespace: elasticache
     RoleARN: !Sub "arn:aws:iam::${AWS::AccountId}:role/aws-service-role/elasticache.application-autoscaling.amazonaws.com/AWSServiceRoleForApplicationAutoScaling_ElastiCacheRG"
     ScheduledActions:
       - EndTime: '2020-12-31T12:00:00.000Z'
         ScalableTargetAction:
           MaxCapacity: '5'
           MinCapacity: '2'
         ScheduledActionName: First
         Schedule: 'cron(0 18 * * ? *)'

```
