# Additional permissions for AWS CloudFormation

If you use AWS CloudFormationto manage your game hosting resources, add the AWS CloudFormation permissions to the policy syntax.

```
    {
      "Action": [
        "autoscaling:DescribeLifecycleHooks",
        "autoscaling:DescribeNotificationConfigurations",
        "ec2:DescribeLaunchTemplateVersions"
      ]
      "Effect": "Allow",
      "Resource": "*"
    }
```
