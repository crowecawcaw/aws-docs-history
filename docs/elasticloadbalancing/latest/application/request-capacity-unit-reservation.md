

# Request Load balancer Capacity Unit reservation for your Application Load Balancer
<a name="request-capacity-unit-reservation"></a>

Before you use LCU reservation, review the following:
+ Capacity is reserved at the regional level and is evenly distributed across availability zones. Confirm you have enough evenly distributed targets in each availability zone before turning on LCU reservation.
+ LCU reservation requests are fulfilled on a first come first serve basis, and depends on available capacity for a zone at that time. Most requests are typically fulfilled within a few minutes, but can take up to a few hours.
+ To update an existing reservation, the previous request must be provisioned or failed. You can increase reserved capacity as many times as you need, however you can only decrease the reserved capacity two times per day.
+ You will continue to incur charges for any reserved or provisioned capacity until they are terminated or cancelled.

------
#### [ Console ]

**To request an LCU reservation**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. On the navigation pane, choose **Load Balancers**.

1. Select the load balancer name.

1. On the **Capacity** tab, choose **Edit LCU Reservation**.

1. Select **Historic reference based estimate**.

1. Select the reference period to view the recommended reserved LCU level.

1. If you do not have historic reference workload, you can choose **Manual estimate** and enter the number of LCUs to be reserved.

1. Choose **Save**.

------
#### [ AWS CLI ]

**To request an LCU reservation**  
Use the [modify-capacity-reservation](https://docs.aws.amazon.com/cli/latest/reference/elbv2/modify-capacity-reservation.html) command.

```
aws elbv2 modify-capacity-reservation \
    --load-balancer-arn {{load-balancer-arn}} \
    --minimum-load-balancer-capacity CapacityUnits={{100}}
```

------
#### [ CloudFormation ]

**To request an LCU reservation**  
Update the [AWS::ElasticLoadBalancingV2::LoadBalancer](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-loadbalancer.html) resource.

```
Resources:
  myLoadBalancer:
    Type: 'AWS::ElasticLoadBalancingV2::LoadBalancer'
    Properties:
      Name: my-alb
      Type: application
      Scheme: internal
      Subnets: 
        - !Ref subnet-AZ1
        - !Ref subnet-AZ2
      SecurityGroups: 
        - !Ref mySecurityGroup
      MinimumLoadBalancerCapacity:
        CapacityUnits: {{100}}
```

------