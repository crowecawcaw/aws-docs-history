# Update the health check settings of a Network Load Balancer

target group

You can update the health check settings for your target group at any time.
For the list of health check settings, see [Health check settings](target-group-health-checks.md#health-check-settings "target-group-health-checks.md#health-check-settings").

Console

###### To update the health check settings

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, under **Load Balancing**,
   choose **Target Groups**.
3. Choose the name of the target group to open its details
   page.
4. On the **Health checks** tab, choose
   **Edit**.
5. On the **Edit health check settings** page,
   modify the settings as needed.
6. Choose **Save changes**.

AWS CLI

###### To update the health check settings

Use the [modify-target-group](../../../cli/latest/reference/elbv2/modify-target-group.md "../../../cli/latest/reference/elbv2/modify-target-group.md") command. The following example
updates the **HealthyThresholdCount** and
**HealthCheckTimeoutSeconds** settings.

```
aws elbv2 modify-target-group \
    --target-group-arn `target-group-arn` \
    --healthy-threshold-count `3` \
    --health-check-timeout-seconds `20`
```

CloudFormation

###### To update the health check settings

Update the [AWS::ElasticLoadBalancingV2::TargetGroup](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-targetgroup.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-targetgroup.md") resource
to include the updated health check settings. The following example
updates the **HealthyThresholdCount** and
**HealthCheckTimeoutSeconds** settings.

```
Resources:
  myTargetGroup:
    Type: 'AWS::ElasticLoadBalancingV2::TargetGroup'
    Properties:
      Name: my-target-group
      Protocol: TCP
      Port: 80
      TargetType: instance
      VpcId: !Ref myVPC
      HealthyThresholdCount: `3`
      HealthCheckTimeoutSeconds: `20`
```
