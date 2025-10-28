# Enable zonal shift for your Application Load Balancer

Zonal shift is disabled by default and must be enabled on each Application Load Balancer. This ensures that you can start a zonal shift
using only the specific Application Load Balancers that you want. For more information, see [Zonal shift for your Application Load Balancer](zonal-shift.md "zonal-shift.md").

Console

###### To enable zonal shift

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, under **Load Balancing**, choose **Load Balancers**.
3. Select the Application Load Balancer.
4. On the **Attributes** tab, choose **Edit**.
5. Under **Availability Zone routing configuration**, for
   **ARC zonal shift integration**, choose **Enable**.
6. Choose **Save changes**.

AWS CLI

###### To enable zonal shift

Use the [modify-load-balancer-attributes](../../../cli/latest/reference/elbv2/modify-load-balancer-attributes.md "../../../cli/latest/reference/elbv2/modify-load-balancer-attributes.md") command with the
`zonal_shift.config.enabled` attribute.

```
aws elbv2 modify-load-balancer-attributes \
    --load-balancer-arn `load-balancer-arn` \
    --attributes "Key=zonal_shift.config.enabled,Value=`true`"
```

CloudFormation

###### To enable zonal shift

Update the [AWS::ElasticLoadBalancingV2::LoadBalancer](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-loadbalancer.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-loadbalancer.md") resource
to include the `zonal_shift.config.enabled` attribute.

```
Resources:
  myLoadBalancer:
    Type: 'AWS::ElasticLoadBalancingV2::LoadBalancer'
    Properties:
      Name: my-alb
      Type: application
      Scheme: internal
      IpAddressType: dualstack
      Subnets:
        - !Ref subnet-AZ1
        - !Ref subnet-AZ2
      SecurityGroups:
        - !Ref mySecurityGroup
      LoadBalancerAttributes:
        -Key: "zonal_shift.config.enabled"
         Value: "`true`"
```
