# Configure Application Auto Scaling resources with

CloudFormation

This section provides CloudFormation template examples for Application Auto Scaling scaling policies and scheduled
actions for different AWS resources.

###### Important

When an Application Auto Scaling snippet is included in the template, you might need to declare a
dependency on the specific scalable resource that's created through the template using the
`DependsOn` attribute. This overrides the default parallelism and directs CloudFormation
to operate on resources in a specified order. Otherwise, the scaling configuration might be
applied before the resource has been set up completely.

For more information, see [DependsOn
attribute](../TemplateReference/aws-attribute-dependson.md "../TemplateReference/aws-attribute-dependson.md").

###### Snippet categories

- [Create a scaling policy for an AppStream fleet](#w2aac11c41c15c19b9 "#w2aac11c41c15c19b9")
- [Create a scaling policy for an Aurora DB cluster](#w2aac11c41c15c19c11 "#w2aac11c41c15c19c11")
- [Create a scaling policy for a DynamoDB table](#w2aac11c41c15c19c13 "#w2aac11c41c15c19c13")
- [Create a scaling policy for an Amazon ECS service (metrics: average CPU and
  memory)](#w2aac11c41c15c19c15 "#w2aac11c41c15c19c15")
- [Create a scaling policy for an Amazon ECS service (metric: average request count per
  target)](#w2aac11c41c15c19c17 "#w2aac11c41c15c19c17")
- [Create a scheduled action with a cron expression for a Lambda function](#w2aac11c41c15c19c19 "#w2aac11c41c15c19c19")
- [Create a scheduled action with an at expression for a Spot Fleet](#w2aac11c41c15c19c21 "#w2aac11c41c15c19c21")

## Create a scaling policy for an AppStream fleet

This snippet shows how to create a policy and apply it to an [`AWS::AppStream::Fleet`](../TemplateReference/aws-resource-appstream-fleet.md "../TemplateReference/aws-resource-appstream-fleet.md") resource using the [`AWS::ApplicationAutoScaling::ScalingPolicy`](../TemplateReference/aws-resource-applicationautoscaling-scalingpolicy.md "../TemplateReference/aws-resource-applicationautoscaling-scalingpolicy.md") resource. The [`AWS::ApplicationAutoScaling::ScalableTarget`](../TemplateReference/aws-resource-applicationautoscaling-scalabletarget.md "../TemplateReference/aws-resource-applicationautoscaling-scalabletarget.md") resource declares a
scalable target to which this policy is applied. Application Auto Scaling can scale the number of fleet
instances at a minimum of 1 instance and a maximum of 20. The policy keeps the average
capacity utilization of the fleet at 75 percent, with scale-out and scale-in cooldown
periods of 300 seconds (5 minutes).

It uses the `Fn::Join` and `Rev` intrinsic functions to construct
the `ResourceId` property with the logical name of the
`AWS::AppStream::Fleet` resource that's specified in the same template. For
more information, see [Intrinsic function reference](../TemplateReference/intrinsic-function-reference.md "../TemplateReference/intrinsic-function-reference.md").

### JSON

```
{
  "Resources" : {
    "ScalableTarget" : {
      "Type" : "AWS::ApplicationAutoScaling::ScalableTarget",
      "Properties" : {
        "MaxCapacity" : 20,
        "MinCapacity" : 1,
        "RoleARN" : { "Fn::Sub" : "arn:aws:iam::${AWS::AccountId}:role/aws-service-role/appstream.application-autoscaling.amazonaws.com/AWSServiceRoleForApplicationAutoScaling_AppStreamFleet" },
        "ServiceNamespace" : "appstream",
        "ScalableDimension" : "appstream:fleet:DesiredCapacity",
        "ResourceId" : {
          "Fn::Join" : [
            "/",
            [
              "fleet",
              {
                "Ref" : "`logicalName`"
              }
            ]
          ]
        }
      }
    },
    "ScalingPolicyAppStreamFleet" : {
      "Type" : "AWS::ApplicationAutoScaling::ScalingPolicy",
      "Properties" : {
        "PolicyName" : { "Fn::Sub" : "${AWS::StackName}-target-tracking-cpu75" },
        "PolicyType" : "TargetTrackingScaling",
        "ServiceNamespace" : "appstream",
        "ScalableDimension" : "appstream:fleet:DesiredCapacity",
        "ResourceId" : {
          "Fn::Join" : [
            "/",
            [
              "fleet",
              {
                "Ref" : "`logicalName`"
              }
            ]
          ]
        },
        "TargetTrackingScalingPolicyConfiguration" : {
          "TargetValue" : 75,
          "PredefinedMetricSpecification" : {
            "PredefinedMetricType" : "AppStreamAverageCapacityUtilization"
          },
          "ScaleInCooldown" : 300,
          "ScaleOutCooldown" : 300
        }
      }
    }
  }
}
```

### YAML

```
---
Resources:
  ScalableTarget:
    Type: AWS::ApplicationAutoScaling::ScalableTarget
    Properties:
      MaxCapacity: 20
      MinCapacity: 1
      RoleARN:
        Fn::Sub: 'arn:aws:iam::${AWS::AccountId}:role/aws-service-role/appstream.application-autoscaling.amazonaws.com/AWSServiceRoleForApplicationAutoScaling_AppStreamFleet'
      ServiceNamespace: appstream
      ScalableDimension: appstream:fleet:DesiredCapacity
      ResourceId: !Join
        - /
        - - fleet
          - !Ref `logicalName`
  ScalingPolicyAppStreamFleet:
    Type: AWS::ApplicationAutoScaling::ScalingPolicy
    Properties:
      PolicyName: !Sub ${AWS::StackName}-target-tracking-cpu75
      PolicyType: TargetTrackingScaling
      ServiceNamespace: appstream
      ScalableDimension: appstream:fleet:DesiredCapacity
      ResourceId: !Join
        - /
        - - fleet
          - !Ref `logicalName`
      TargetTrackingScalingPolicyConfiguration:
        TargetValue: 75
        PredefinedMetricSpecification:
          PredefinedMetricType: AppStreamAverageCapacityUtilization
        ScaleInCooldown: 300
        ScaleOutCooldown: 300
```

## Create a scaling policy for an Aurora DB cluster

In this snippet, you register an [`AWS::RDS::DBCluster`](../TemplateReference/aws-resource-rds-dbcluster.md "../TemplateReference/aws-resource-rds-dbcluster.md")
resource. The [`AWS::ApplicationAutoScaling::ScalableTarget`](../TemplateReference/aws-resource-applicationautoscaling-scalabletarget.md "../TemplateReference/aws-resource-applicationautoscaling-scalabletarget.md") resource indicates
that the DB cluster should be dynamically scaled to have from one to eight Aurora Replicas.
You also apply a target tracking scaling policy to the cluster using the [`AWS::ApplicationAutoScaling::ScalingPolicy`](../TemplateReference/aws-resource-applicationautoscaling-scalingpolicy.md "../TemplateReference/aws-resource-applicationautoscaling-scalingpolicy.md") resource.

In this configuration, the `RDSReaderAverageCPUUtilization` predefined metric
is used to adjust an Aurora DB cluster based on an average CPU utilization of 40 percent
across all Aurora Replicas in that Aurora DB cluster. The configuration provides a scale-in
cooldown period of 10 minutes and a scale-out cooldown period of 5 minutes.

This example uses the `Fn::Sub` intrinsic function to construct the
`ResourceId` property with the logical name of the
`AWS::RDS::DBCluster` resource that is specified in the same template. For more
information, see [Intrinsic function reference](../TemplateReference/intrinsic-function-reference.md "../TemplateReference/intrinsic-function-reference.md").

### JSON

```
{
  "Resources" : {
    "ScalableTarget" : {
      "Type" : "AWS::ApplicationAutoScaling::ScalableTarget",
      "Properties" : {
        "MaxCapacity" : 8,
        "MinCapacity" : 1,
        "RoleARN" : { "Fn::Sub" : "arn:aws:iam::${AWS::AccountId}:role/aws-service-role/rds.application-autoscaling.amazonaws.com/AWSServiceRoleForApplicationAutoScaling_RDSCluster" },
        "ServiceNamespace" : "rds",
        "ScalableDimension" : "rds:cluster:ReadReplicaCount",
        "ResourceId" : { "Fn::Sub" : "cluster:${`logicalName`}" }
      }
    },
    "ScalingPolicyDBCluster" : {
      "Type" : "AWS::ApplicationAutoScaling::ScalingPolicy",
      "Properties" : {
        "PolicyName" : { "Fn::Sub" : "${AWS::StackName}-target-tracking-cpu40" },
        "PolicyType" : "TargetTrackingScaling",
        "ServiceNamespace" : "rds",
        "ScalableDimension" : "rds:cluster:ReadReplicaCount",
        "ResourceId" : { "Fn::Sub" : "cluster:${`logicalName`}" },
        "TargetTrackingScalingPolicyConfiguration" : {
          "TargetValue" : 40,
          "PredefinedMetricSpecification" : {
            "PredefinedMetricType" : "RDSReaderAverageCPUUtilization"
          },
          "ScaleInCooldown" : 600,
          "ScaleOutCooldown" : 300
        }
      }
    }
  }
}
```

### YAML

```
---
Resources:
  ScalableTarget:
    Type: AWS::ApplicationAutoScaling::ScalableTarget
    Properties:
      MaxCapacity: 8
      MinCapacity: 1
      RoleARN:
        Fn::Sub: 'arn:aws:iam::${AWS::AccountId}:role/aws-service-role/rds.application-autoscaling.amazonaws.com/AWSServiceRoleForApplicationAutoScaling_RDSCluster'
      ServiceNamespace: rds
      ScalableDimension: rds:cluster:ReadReplicaCount
      ResourceId: !Sub cluster:${`logicalName`}
  ScalingPolicyDBCluster:
    Type: AWS::ApplicationAutoScaling::ScalingPolicy
    Properties:
      PolicyName: !Sub ${AWS::StackName}-target-tracking-cpu40
      PolicyType: TargetTrackingScaling
      ServiceNamespace: rds
      ScalableDimension: rds:cluster:ReadReplicaCount
      ResourceId: !Sub cluster:${`logicalName`}
      TargetTrackingScalingPolicyConfiguration:
        TargetValue: 40
        PredefinedMetricSpecification:
          PredefinedMetricType: RDSReaderAverageCPUUtilization
        ScaleInCooldown: 600
        ScaleOutCooldown: 300
```

## Create a scaling policy for a DynamoDB table

This snippet shows how to create a policy with the `TargetTrackingScaling`
policy type and apply it to an [`AWS::DynamoDB::Table`](../TemplateReference/aws-resource-dynamodb-table.md "../TemplateReference/aws-resource-dynamodb-table.md") resource using the [`AWS::ApplicationAutoScaling::ScalingPolicy`](../TemplateReference/aws-resource-applicationautoscaling-scalingpolicy.md "../TemplateReference/aws-resource-applicationautoscaling-scalingpolicy.md") resource. The [`AWS::ApplicationAutoScaling::ScalableTarget`](../TemplateReference/aws-resource-applicationautoscaling-scalabletarget.md "../TemplateReference/aws-resource-applicationautoscaling-scalabletarget.md") resource declares a
scalable target to which this policy is applied, with a minimum of five write capacity units
and a maximum of 15. The scaling policy scales the table's write capacity throughput to
maintain the target utilization at 50 percent based on the
`DynamoDBWriteCapacityUtilization` predefined metric.

It uses the `Fn::Join` and `Ref` intrinsic functions to construct
the `ResourceId` property with the logical name of the
`AWS::DynamoDB::Table` resource that's specified in the same template. For more
information, see [Intrinsic function reference](../TemplateReference/intrinsic-function-reference.md "../TemplateReference/intrinsic-function-reference.md").

###### Note

For more information about how to create an CloudFormation template for DynamoDB resources, see
the blog post [How to use CloudFormation to configure auto scaling for Amazon DynamoDB tables and
indexes](https://aws.amazon.com/blogs/database/how-to-use-aws-cloudformation-to-configure-auto-scaling-for-amazon-dynamodb-tables-and-indexes/ "https://aws.amazon.com/blogs/database/how-to-use-aws-cloudformation-to-configure-auto-scaling-for-amazon-dynamodb-tables-and-indexes/") on the AWS Database Blog.

### JSON

```
{
  "Resources" : {
    "WriteCapacityScalableTarget" : {
      "Type" : "AWS::ApplicationAutoScaling::ScalableTarget",
      "Properties" : {
        "MaxCapacity" : 15,
        "MinCapacity" : 5,
        "RoleARN" : { "Fn::Sub" : "arn:aws:iam::${AWS::AccountId}:role/aws-service-role/dynamodb.application-autoscaling.amazonaws.com/AWSServiceRoleForApplicationAutoScaling_DynamoDBTable" },
        "ServiceNamespace" : "dynamodb",
        "ScalableDimension" : "dynamodb:table:WriteCapacityUnits",
        "ResourceId" : {
          "Fn::Join" : [
            "/",
            [
              "table",
              {
                "Ref" : "`logicalName`"
              }
            ]
          ]
        }
      }
    },
    "WriteScalingPolicy" : {
      "Type" : "AWS::ApplicationAutoScaling::ScalingPolicy",
      "Properties" : {
        "PolicyName" : "WriteScalingPolicy",
        "PolicyType" : "TargetTrackingScaling",
        "ScalingTargetId" : { "Ref" : "WriteCapacityScalableTarget" },
        "TargetTrackingScalingPolicyConfiguration" : {
          "TargetValue" : 50.0,
          "ScaleInCooldown" : 60,
          "ScaleOutCooldown" : 60,
          "PredefinedMetricSpecification" : {
            "PredefinedMetricType" : "DynamoDBWriteCapacityUtilization"
          }
        }
      }
    }
  }
}
```

### YAML

```
---
Resources:
  WriteCapacityScalableTarget:
    Type: AWS::ApplicationAutoScaling::ScalableTarget
    Properties:
      MaxCapacity: 15
      MinCapacity: 5
      RoleARN:
        Fn::Sub: 'arn:aws:iam::${AWS::AccountId}:role/aws-service-role/dynamodb.application-autoscaling.amazonaws.com/AWSServiceRoleForApplicationAutoScaling_DynamoDBTable'
      ServiceNamespace: dynamodb
      ScalableDimension: dynamodb:table:WriteCapacityUnits
      ResourceId: !Join
        - /
        - - table
          - !Ref `logicalName`
  WriteScalingPolicy:
    Type: AWS::ApplicationAutoScaling::ScalingPolicy
    Properties:
      PolicyName: WriteScalingPolicy
      PolicyType: TargetTrackingScaling
      ScalingTargetId: !Ref WriteCapacityScalableTarget
      TargetTrackingScalingPolicyConfiguration:
        TargetValue: 50.0
        ScaleInCooldown: 60
        ScaleOutCooldown: 60
        PredefinedMetricSpecification:
          PredefinedMetricType: DynamoDBWriteCapacityUtilization
```

## Create a scaling policy for an Amazon ECS service (metrics: average CPU and

memory)

This snippet shows how to create a policy and apply it to an [`AWS::ECS::Service`](../TemplateReference/aws-resource-ecs-service.md "../TemplateReference/aws-resource-ecs-service.md")
resource using the [`AWS::ApplicationAutoScaling::ScalingPolicy`](../TemplateReference/aws-resource-applicationautoscaling-scalingpolicy.md "../TemplateReference/aws-resource-applicationautoscaling-scalingpolicy.md") resource. The [`AWS::ApplicationAutoScaling::ScalableTarget`](../TemplateReference/aws-resource-applicationautoscaling-scalabletarget.md "../TemplateReference/aws-resource-applicationautoscaling-scalabletarget.md") resource declares a
scalable target to which this policy is applied. Application Auto Scaling can scale the number of tasks at a
minimum of 1 task and a maximum of 6.

It creates two scaling policies with the `TargetTrackingScaling` policy type.
The policies are used to scale the ECS service based on the service's average CPU and memory
usage. It uses the `Fn::Join` and `Ref` intrinsic functions to
construct the `ResourceId` property with the logical names of the [`AWS::ECS::Cluster`](../TemplateReference/aws-resource-ecs-cluster.md "../TemplateReference/aws-resource-ecs-cluster.md") (`myContainerCluster`) and
`AWS::ECS::Service` (`myService`) resources that are specified in
the same template. For more information, see [Intrinsic function reference](../TemplateReference/intrinsic-function-reference.md "../TemplateReference/intrinsic-function-reference.md").

### JSON

```
{
  "Resources" : {
    "ECSScalableTarget" : {
      "Type" : "AWS::ApplicationAutoScaling::ScalableTarget",
      "Properties" : {
        "MaxCapacity" : "6",
        "MinCapacity" : "1",
        "RoleARN" : { "Fn::Sub" : "arn:aws:iam::${AWS::AccountId}:role/aws-service-role/ecs.application-autoscaling.amazonaws.com/AWSServiceRoleForApplicationAutoScaling_ECSService" },
        "ServiceNamespace" : "ecs",
        "ScalableDimension" : "ecs:service:DesiredCount",
        "ResourceId" : {
          "Fn::Join" : [
            "/",
            [
              "service",
              {
                "Ref" : "`myContainerCluster`"
              },
              {
                "Fn::GetAtt" : [
                  "`myService`",
                  "Name"
                ]
              }
            ]
          ]
        }
      }
    },
    "ServiceScalingPolicyCPU" : {
      "Type" : "AWS::ApplicationAutoScaling::ScalingPolicy",
      "Properties" : {
        "PolicyName" : { "Fn::Sub" : "${AWS::StackName}-target-tracking-cpu70" },
        "PolicyType" : "TargetTrackingScaling",
        "ScalingTargetId" : { "Ref" : "ECSScalableTarget" },
        "TargetTrackingScalingPolicyConfiguration" : {
          "TargetValue" : 70.0,
          "ScaleInCooldown" : 180,
          "ScaleOutCooldown" : 60,
          "PredefinedMetricSpecification" : {
            "PredefinedMetricType" : "ECSServiceAverageCPUUtilization"
          }
        }
      }
    },
    "ServiceScalingPolicyMem" : {
      "Type" : "AWS::ApplicationAutoScaling::ScalingPolicy",
      "Properties" : {
        "PolicyName" : { "Fn::Sub" : "${AWS::StackName}-target-tracking-mem90" },
        "PolicyType" : "TargetTrackingScaling",
        "ScalingTargetId" : { "Ref" : "ECSScalableTarget" },
        "TargetTrackingScalingPolicyConfiguration" : {
          "TargetValue" : 90.0,
          "ScaleInCooldown" : 180,
          "ScaleOutCooldown" : 60,
          "PredefinedMetricSpecification" : {
            "PredefinedMetricType" : "ECSServiceAverageMemoryUtilization"
          }
        }
      }
    }
  }
}
```

### YAML

```
---
Resources:
  ECSScalableTarget:
    Type: AWS::ApplicationAutoScaling::ScalableTarget
    Properties:
      MaxCapacity: 6
      MinCapacity: 1
      RoleARN:
        Fn::Sub: 'arn:aws:iam::${AWS::AccountId}:role/aws-service-role/ecs.application-autoscaling.amazonaws.com/AWSServiceRoleForApplicationAutoScaling_ECSService'
      ServiceNamespace: ecs
      ScalableDimension: 'ecs:service:DesiredCount'
      ResourceId: !Join
        - /
        - - service
          - !Ref `myContainerCluster`
          - !GetAtt `myService`.Name
  ServiceScalingPolicyCPU:
    Type: AWS::ApplicationAutoScaling::ScalingPolicy
    Properties:
      PolicyName: !Sub ${AWS::StackName}-target-tracking-cpu70
      PolicyType: TargetTrackingScaling
      ScalingTargetId: !Ref ECSScalableTarget
      TargetTrackingScalingPolicyConfiguration:
        TargetValue: 70.0
        ScaleInCooldown: 180
        ScaleOutCooldown: 60
        PredefinedMetricSpecification:
          PredefinedMetricType: ECSServiceAverageCPUUtilization
  ServiceScalingPolicyMem:
    Type: AWS::ApplicationAutoScaling::ScalingPolicy
    Properties:
      PolicyName: !Sub ${AWS::StackName}-target-tracking-mem90
      PolicyType: TargetTrackingScaling
      ScalingTargetId: !Ref ECSScalableTarget
      TargetTrackingScalingPolicyConfiguration:
        TargetValue: 90.0
        ScaleInCooldown: 180
        ScaleOutCooldown: 60
        PredefinedMetricSpecification:
          PredefinedMetricType: ECSServiceAverageMemoryUtilization
```

## Create a scaling policy for an Amazon ECS service (metric: average request count per

target)

The following example applies a target tracking scaling policy with the
`ALBRequestCountPerTarget` predefined metric to an ECS service. The policy is
used to add capacity to the ECS service when the request count per target (per minute)
exceeds the target value. Because the value of `DisableScaleIn` is set to
`true`, the target tracking policy won't remove capacity from the scalable
target.

It uses the `Fn::Join` and `Fn::GetAtt` intrinsic functions to
construct the `ResourceLabel` property with the logical names of the [`AWS::ElasticLoadBalancingV2::LoadBalancer`](../TemplateReference/aws-resource-elasticloadbalancingv2-loadbalancer.md "../TemplateReference/aws-resource-elasticloadbalancingv2-loadbalancer.md")
(`myLoadBalancer`) and [`AWS::ElasticLoadBalancingV2::TargetGroup`](../TemplateReference/aws-resource-elasticloadbalancingv2-targetgroup.md "../TemplateReference/aws-resource-elasticloadbalancingv2-targetgroup.md")
(`myTargetGroup`) resources that are specified in the same template. For more
information, see [Intrinsic function reference](../TemplateReference/intrinsic-function-reference.md "../TemplateReference/intrinsic-function-reference.md").

The `MaxCapacity` and `MinCapacity` properties of the scalable
target and the `TargetValue` property of the scaling policy reference parameter
values that you pass to the template when creating or updating a stack.

### JSON

```
{
  "Resources" : {
    "ECSScalableTarget" : {
      "Type" : "AWS::ApplicationAutoScaling::ScalableTarget",
      "Properties" : {
        "MaxCapacity" : { "Ref" : "MaxCount" },
        "MinCapacity" : { "Ref" : "MinCount" },
        "RoleARN" : { "Fn::Sub" : "arn:aws:iam::${AWS::AccountId}:role/aws-service-role/ecs.application-autoscaling.amazonaws.com/AWSServiceRoleForApplicationAutoScaling_ECSService" },
        "ServiceNamespace" : "ecs",
        "ScalableDimension" : "ecs:service:DesiredCount",
        "ResourceId" : {
          "Fn::Join" : [
            "/",
            [
              "service",
              {
                "Ref" : "`myContainerCluster`"
              },
              {
                "Fn::GetAtt" : [
                  "`myService`",
                  "Name"
                ]
              }
            ]
          ]
        }
      }
    },
    "ServiceScalingPolicyALB" : {
      "Type" : "AWS::ApplicationAutoScaling::ScalingPolicy",
      "Properties" : {
        "PolicyName" : "alb-requests-per-target-per-minute",
        "PolicyType" : "TargetTrackingScaling",
        "ScalingTargetId" : { "Ref" : "ECSScalableTarget" },
        "TargetTrackingScalingPolicyConfiguration" : {
          "TargetValue" : { "Ref" : "ALBPolicyTargetValue" },
          "ScaleInCooldown" : 180,
          "ScaleOutCooldown" : 30,
          "DisableScaleIn" : true,
          "PredefinedMetricSpecification" : {
            "PredefinedMetricType" : "ALBRequestCountPerTarget",
            "ResourceLabel" : {
              "Fn::Join" : [
                "/",
                [
                  {
                    "Fn::GetAtt" : [
                      "`myLoadBalancer`",
                      "LoadBalancerFullName"
                    ]
                  },
                  {
                    "Fn::GetAtt" : [
                      "`myTargetGroup`",
                      "TargetGroupFullName"
                    ]
                  }
                ]
              ]
            }
          }
        }
      }
    }
  }
}
```

### YAML

```
---
Resources:
  ECSScalableTarget:
    Type: AWS::ApplicationAutoScaling::ScalableTarget
    Properties:
      MaxCapacity: !Ref MaxCount
      MinCapacity: !Ref MinCount
      RoleARN:
        Fn::Sub: 'arn:aws:iam::${AWS::AccountId}:role/aws-service-role/ecs.application-autoscaling.amazonaws.com/AWSServiceRoleForApplicationAutoScaling_ECSService'
      ServiceNamespace: ecs
      ScalableDimension: 'ecs:service:DesiredCount'
      ResourceId: !Join
        - /
        - - service
          - !Ref `myContainerCluster`
          - !GetAtt `myService`.Name
  ServiceScalingPolicyALB:
    Type: AWS::ApplicationAutoScaling::ScalingPolicy
    Properties:
      PolicyName: alb-requests-per-target-per-minute
      PolicyType: TargetTrackingScaling
      ScalingTargetId: !Ref ECSScalableTarget
      TargetTrackingScalingPolicyConfiguration:
        TargetValue: !Ref ALBPolicyTargetValue
        ScaleInCooldown: 180
        ScaleOutCooldown: 30
        DisableScaleIn: true
        PredefinedMetricSpecification:
          PredefinedMetricType: ALBRequestCountPerTarget
          ResourceLabel: !Join
            - '/'
            - - !GetAtt `myLoadBalancer`.LoadBalancerFullName
              - !GetAtt `myTargetGroup`.TargetGroupFullName
```

## Create a scheduled action with a cron expression for a Lambda function

This snippet registers the provisioned concurrency for a function alias ([`AWS::Lambda::Alias`](../TemplateReference/aws-resource-lambda-alias.md "../TemplateReference/aws-resource-lambda-alias.md")) named `BLUE` using the [`AWS::ApplicationAutoScaling::ScalableTarget`](../TemplateReference/aws-resource-applicationautoscaling-scalabletarget.md "../TemplateReference/aws-resource-applicationautoscaling-scalabletarget.md") resource. It also
creates a scheduled action with a recurring schedule using a cron expression. The time zone
for the recurring schedule is UTC.

It uses the `Fn::Join` and `Ref` intrinsic functions in the
`RoleARN` property to specify the ARN of the service-linked role. It uses the
`Fn::Sub` intrinsic function to construct the `ResourceId` property
with the logical name of the [`AWS::Lambda::Function`](../TemplateReference/aws-resource-lambda-function.md "../TemplateReference/aws-resource-lambda-function.md") or [`AWS::Serverless::Function`](../../../serverless-application-model/latest/developerguide/sam-resource-function.md "../../../serverless-application-model/latest/developerguide/sam-resource-function.md") resource that is specified in the same
template. For more information, see [Intrinsic function reference](../TemplateReference/intrinsic-function-reference.md "../TemplateReference/intrinsic-function-reference.md").

###### Note

You can't allocate provisioned concurrency on an alias that points to the unpublished
version
(`$LATEST`).

For more information about how to create an CloudFormation template for Lambda resources, see
the blog post [Scheduling AWS Lambda Provisioned Concurrency for recurring peak usage](https://aws.amazon.com/blogs/compute/scheduling-aws-lambda-provisioned-concurrency-for-recurring-peak-usage/ "https://aws.amazon.com/blogs/compute/scheduling-aws-lambda-provisioned-concurrency-for-recurring-peak-usage/") on the
AWS Compute Blog.

### JSON

```
{
  "ScalableTarget" : {
    "Type" : "AWS::ApplicationAutoScaling::ScalableTarget",
    "Properties" : {
      "MaxCapacity" : 250,
      "MinCapacity" : 0,
      "RoleARN" : {
        "Fn::Join" : [
          ":",
          [
            "arn:aws:iam:",
            {
              "Ref" : "AWS::AccountId"
            },
            "role/aws-service-role/lambda.application-autoscaling.amazonaws.com/AWSServiceRoleForApplicationAutoScaling_LambdaConcurrency"
          ]
        ]
      },
      "ServiceNamespace" : "lambda",
      "ScalableDimension" : "lambda:function:ProvisionedConcurrency",
      "ResourceId" : { "Fn::Sub" : "function:${`logicalName`}:BLUE" },
      "ScheduledActions" : [
        {
          "ScalableTargetAction" : {
            "MinCapacity" : "250"
          },
          "ScheduledActionName" : "my-scale-out-scheduled-action",
          "Schedule" : "cron(0 18 * * ? *)",
          "EndTime" : "2022-12-31T12:00:00.000Z"
        }
      ]
    }
  }
}
```

### YAML

```
ScalableTarget:
  Type: AWS::ApplicationAutoScaling::ScalableTarget
  Properties:
    MaxCapacity: 250
    MinCapacity: 0
    RoleARN: !Join
      - ':'
      - - 'arn:aws:iam:'
        - !Ref 'AWS::AccountId'
        - role/aws-service-role/lambda.application-autoscaling.amazonaws.com/AWSServiceRoleForApplicationAutoScaling_LambdaConcurrency
    ServiceNamespace: lambda
    ScalableDimension: lambda:function:ProvisionedConcurrency
    ResourceId: !Sub function:${`logicalName`}:BLUE
    ScheduledActions:
      - ScalableTargetAction:
          MinCapacity: 250
        ScheduledActionName: my-scale-out-scheduled-action
        Schedule: 'cron(0 18 * * ? *)'
        EndTime: '2022-12-31T12:00:00.000Z'
```

## Create a scheduled action with an `at` expression for a Spot Fleet

This snippet shows how to create two scheduled actions that occur only once for an
[`AWS::EC2::SpotFleet`](../TemplateReference/aws-resource-ec2-spotfleet.md "../TemplateReference/aws-resource-ec2-spotfleet.md") resource using the [`AWS::ApplicationAutoScaling::ScalableTarget`](../TemplateReference/aws-resource-applicationautoscaling-scalabletarget.md "../TemplateReference/aws-resource-applicationautoscaling-scalabletarget.md") resource. The time
zone for each one-time scheduled action is UTC.

It uses the `Fn::Join` and `Ref` intrinsic functions to construct
the `ResourceId` property with the logical name of the
`AWS::EC2::SpotFleet` resource that is specified in the same template. For more
information, see [Intrinsic function reference](../TemplateReference/intrinsic-function-reference.md "../TemplateReference/intrinsic-function-reference.md").

###### Note

The Spot Fleet request must have a request type of `maintain`. Automatic
scaling isn't supported for one-time requests or Spot blocks.

### JSON

```
{
  "Resources" : {
    "SpotFleetScalableTarget" : {
      "Type" : "AWS::ApplicationAutoScaling::ScalableTarget",
      "Properties" : {
        "MaxCapacity" : 0,
        "MinCapacity" : 0,
        "RoleARN" : { "Fn::Sub" : "arn:aws:iam::${AWS::AccountId}:role/aws-service-role/ec2.application-autoscaling.amazonaws.com/AWSServiceRoleForApplicationAutoScaling_EC2SpotFleetRequest" },
        "ServiceNamespace" : "ec2",
        "ScalableDimension" : "ec2:spot-fleet-request:TargetCapacity",
        "ResourceId" : {
          "Fn::Join" : [
            "/",
            [
              "spot-fleet-request",
              {
                "Ref" : "`logicalName`"
              }
            ]
          ]
        },
        "ScheduledActions" : [
          {
            "ScalableTargetAction" : {
              "MaxCapacity" : "10",
              "MinCapacity" : "10"
            },
            "ScheduledActionName" : "my-scale-out-scheduled-action",
            "Schedule" : "at(2022-05-20T13:00:00)"
          },
          {
            "ScalableTargetAction" : {
              "MaxCapacity" : "0",
              "MinCapacity" : "0"
            },
            "ScheduledActionName" : "my-scale-in-scheduled-action",
            "Schedule" : "at(2022-05-20T21:00:00)"
          }
        ]
      }
    }
  }
}
```

### YAML

```
---
Resources:
  SpotFleetScalableTarget:
    Type: AWS::ApplicationAutoScaling::ScalableTarget
    Properties:
      MaxCapacity: 0
      MinCapacity: 0
      RoleARN:
        Fn::Sub: 'arn:aws:iam::${AWS::AccountId}:role/aws-service-role/ec2.application-autoscaling.amazonaws.com/AWSServiceRoleForApplicationAutoScaling_EC2SpotFleetRequest'
      ServiceNamespace: ec2
      ScalableDimension: 'ec2:spot-fleet-request:TargetCapacity'
      ResourceId: !Join
        - /
        - - spot-fleet-request
          - !Ref `logicalName`
      ScheduledActions:
        - ScalableTargetAction:
            MaxCapacity: 10
            MinCapacity: 10
          ScheduledActionName: my-scale-out-scheduled-action
          Schedule: 'at(2022-05-20T13:00:00)'
        - ScalableTargetAction:
            MaxCapacity: 0
            MinCapacity: 0
          ScheduledActionName: my-scale-in-scheduled-action
          Schedule: 'at(2022-05-20T21:00:00)'
```
