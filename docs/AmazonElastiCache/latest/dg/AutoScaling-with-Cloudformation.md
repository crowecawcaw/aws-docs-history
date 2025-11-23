# Use CloudFormation for Auto Scaling

policies

This snippet shows how to create a scheduled action and apply it to an [AWS::ElastiCache::ReplicationGroup](../../../AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.md") resource using the [AWS::ApplicationAutoScaling::ScalableTarget](../../../AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.md") resource. It uses the
[Fn::Join](../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-join.md "../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-join.md") and [Ref](../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.md "../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.md") intrinsic functions to construct the `ResourceId`
property with the logical name of the
`AWS::ElastiCache::ReplicationGroup` resource that is specified in
the same template.

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

  ScalingPolicy:
    Type: "AWS::ApplicationAutoScaling::ScalingPolicy"
    Properties:
      ScalingTargetId: !Ref ScalingTarget
      ServiceNamespace: elasticache
      PolicyName: testpolicy
      PolicyType: TargetTrackingScaling
      ScalableDimension: 'elasticache:replication-group:Replicas'
      TargetTrackingScalingPolicyConfiguration:
        PredefinedMetricSpecification:
          PredefinedMetricType: ElastiCacheReplicaEngineCPUUtilization
        TargetValue: 40
```
