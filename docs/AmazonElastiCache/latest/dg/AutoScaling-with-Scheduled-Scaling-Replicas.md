# Scheduled scaling

Scaling based on a schedule enables you to scale your application in response to
predictable changes in demand. To use scheduled scaling, you create scheduled
actions, which tell ElastiCache for Valkey and Redis OSS to perform scaling activities at specific times. When you
create a scheduled action, you specify an existing ElastiCache cluster, when the scaling
activity should occur, minimum capacity, and maximum capacity. You can create
scheduled actions that scale one time only or that scale on a recurring schedule.

You can only create a scheduled action for ElastiCache clusters that already exist.
You can't create a scheduled action at the same time that you create a
cluster.

For more information on terminology for scheduled action creation, management, and
deletion, see [Commonly used commands for scheduled action creation, management, and deletion](../../../autoscaling/application/userguide/application-auto-scaling-scheduled-scaling.md#scheduled-scaling-commonly-used-commands "../../../autoscaling/application/userguide/application-auto-scaling-scheduled-scaling.md#scheduled-scaling-commonly-used-commands")

**To create a one-time scheduled action:**

Similar to Shard dimension. See [Scheduled scaling](AutoScaling-with-Scheduled-Scaling-Shards.md "AutoScaling-with-Scheduled-Scaling-Shards.md") .

**To delete a scheduled action**

Similar to Shard dimension. See [Scheduled scaling](AutoScaling-with-Scheduled-Scaling-Shards.md "AutoScaling-with-Scheduled-Scaling-Shards.md") .

**To manage scheduled scaling using the AWS CLI**

Use the following application-autoscaling APIs:

- [put-scheduled-action](../../../cli/latest/reference/application-autoscaling/put-scheduled-action.md "../../../cli/latest/reference/application-autoscaling/put-scheduled-action.md")
- [describe-scheduled-actions](../../../cli/latest/reference/application-autoscaling/describe-scheduled-actions.md "../../../cli/latest/reference/application-autoscaling/describe-scheduled-actions.md")
- [delete-scheduled-action](../../../cli/latest/reference/application-autoscaling/delete-scheduled-action.md "../../../cli/latest/reference/application-autoscaling/delete-scheduled-action.md")

## Use CloudFormation to

create Auto Scaling policies

This snippet shows how to create a scheduled action and apply it to an [AWS::ElastiCache::ReplicationGroup](../../../AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.md") resource using the [AWS::ApplicationAutoScaling::ScalableTarget](../../../AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.md") resource. It uses the
[Fn::Join](../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-join.md "../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-join.md") and [Ref](../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.md "../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.md") intrinsic functions to construct the `ResourceId`
property with the logical name of the
`AWS::ElastiCache::ReplicationGroup` resource that is specified
in the same template.

```


ScalingTarget:
   Type: 'AWS::ApplicationAutoScaling::ScalableTarget'
   Properties:
     MaxCapacity: 0
     MinCapacity: 0
     ResourceId: !Sub replication-group/${logicalName}
     ScalableDimension: 'elasticache:replication-group:Replicas'
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
