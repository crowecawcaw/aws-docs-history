

# Amazon ECS service scaling execution block sample policy
<a name="security_iam_region_switch_ecs"></a>

**(Optional) Permissions to wait for target group health**  
 When the `waitELBTargetGroupHealthy` option is enabled on your Amazon ECS service scaling execution block, add the following permissions. For more information about this option, see [Amazon ECS service scaling execution block](ecs-service-scaling-block.md).   
`ecs:ListTasks` — to list the service's running tasks so Region switch knows which targets to check.
`ecs:DescribeTasks` — to get each task's network details (the task ENI IP address, or the container instance and host port) that identify its target group entry.
`elasticloadbalancing:DescribeTargetHealth` — to read the health of the service's targets in the associated target groups.
`ecs:DescribeContainerInstances` — to resolve a task's container instance to its EC2 instance ID for target matching. Required only when the service runs tasks that use the `bridge` or `host` network mode.
 If `waitELBTargetGroupHealthy` option is disabled, you can omit these permissions. 

 The following is a sample JSON policy to attach if you add execution blocks to a Region switch plan for Amazon ECS service scaling: 

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ecs:DescribeServices",
        "ecs:UpdateService"
      ],
      "Resource": [
        "arn:aws:ecs:us-east-1:111122223333:service/app-cluster-primary/app-service",
        "arn:aws:ecs:us-west-2:111122223333:service/app-cluster-secondary/app-service"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "ecs:DescribeClusters"
      ],
      "Resource": [
        "arn:aws:ecs:us-east-1:111122223333:cluster/app-cluster-primary",
        "arn:aws:ecs:us-west-2:111122223333:cluster/app-cluster-secondary"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "ecs:ListServices"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "application-autoscaling:DescribeScalableTargets",
        "application-autoscaling:RegisterScalableTarget"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "cloudwatch:GetMetricStatistics"
      ],
      "Resource": "*"
    },
    {
      "Sid": "RequiredOnlyWhenWaitELBTargetGroupHealthyEnabled",
      "Effect": "Allow",
      "Action": [
        "ecs:ListTasks",
        "elasticloadbalancing:DescribeTargetHealth"
      ],
      "Resource": "*"
    },
    {
      "Sid": "DescribeTasksWhenWaitELBTargetGroupHealthyEnabled",
      "Effect": "Allow",
      "Action": [
         "ecs:DescribeTasks"
      ],
      "Resource": [
         "arn:aws:ecs:us-east-1:111122223333:task/app-cluster-primary/*",
         "arn:aws:ecs:us-west-2:111122223333:task/app-cluster-secondary/*"
      ]
    },
    {
      "Sid": "RequiredOnlyForBridgeOrHostNetworkModeTasks",
      "Effect": "Allow",
      "Action": [
         "ecs:DescribeContainerInstances"
      ],
      "Resource": [
         "arn:aws:ecs:us-east-1:111122223333:container-instance/app-cluster-primary/*",
         "arn:aws:ecs:us-west-2:111122223333:container-instance/app-cluster-secondary/*"
      ]
    }
  ]
}
```