

# Additional permissions for CloudFormation
<a name="gsg-iam-permissions-users-policycfn"></a>

If you use CloudFormation to manage your game hosting resources, add the CloudFormation permissions to the policy syntax. 

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