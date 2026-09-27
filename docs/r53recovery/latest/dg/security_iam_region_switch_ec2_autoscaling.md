

# EC2 Auto Scaling execution block sample policy
<a name="security_iam_region_switch_ec2_autoscaling"></a>

**(Optional) Permission to wait for target group health**  
 When the `waitELBTargetGroupHealthy` option is enabled on your EC2 Auto Scaling execution block, add the `elasticloadbalancing:DescribeTargetHealth` permission. If this option is disabled, you can omit this permission. For more information about this option, see [Amazon EC2 Auto Scaling group execution block](ec2-auto-scaling-block.md). 

 The following is a sample JSON policy to attach if you add execution blocks to a Region switch plan for EC2 Auto Scaling groups: 

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "autoscaling:DescribeAutoScalingGroups"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "autoscaling:UpdateAutoScalingGroup"
      ],
      "Resource": [
        "arn:aws:autoscaling:us-east-1:111122223333:autoScalingGroup:123d456e-123e-1111-abcd-EXAMPLE22222:autoScalingGroupName/app-asg-primary",
        "arn:aws:autoscaling:us-west-2:111122223333:autoScalingGroup:1234a321-123e-1234-aabb-EXAMPLE33333:autoScalingGroupName/app-asg-secondary"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "cloudwatch:GetMetricStatistics"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "cloudwatch:namespace": "AWS/AutoScaling"
        }
      }
    },
    {
      "Sid": "RequiredOnlyWhenWaitELBTargetGroupHealthyEnabled",
      "Effect": "Allow",
      "Action": [
        "elasticloadbalancing:DescribeTargetHealth"
      ],
      "Resource": "*"
    }
  ]
}
```