# Use AWS CloudFormation to create a scaling

policy

The following example shows how to configure model auto scaling on an endpoint using
AWS CloudFormation.

```
  Endpoint:
    Type: "AWS::SageMaker::Endpoint"
    Properties:
      EndpointName: `yourEndpointName`
      EndpointConfigName: `yourEndpointConfigName`

  ScalingTarget:
    Type: "AWS::ApplicationAutoScaling::ScalableTarget"
    Properties:
      MaxCapacity: `10`
      MinCapacity: `2`
      ResourceId: endpoint/`my-endpoint`/variant/`my-variant`
      RoleARN: `arn`
      ScalableDimension: sagemaker:variant:DesiredInstanceCount
      ServiceNamespace: sagemaker

  ScalingPolicy:
    Type: "AWS::ApplicationAutoScaling::ScalingPolicy"
    Properties:
      PolicyName: `my-scaling-policy`
      PolicyType: TargetTrackingScaling
      ScalingTargetId:
        Ref: ScalingTarget
      TargetTrackingScalingPolicyConfiguration:
        TargetValue: `70.0`
        ScaleInCooldown: `600`
        ScaleOutCooldown: `30`
        PredefinedMetricSpecification:
          PredefinedMetricType: SageMakerVariantInvocationsPerInstance
```

For more information, see [Create Application Auto Scaling resources with AWS CloudFormation](../../../autoscaling/application/userguide/creating-resources-with-cloudformation.md "../../../autoscaling/application/userguide/creating-resources-with-cloudformation.md") in the
_Application Auto Scaling User Guide_.
