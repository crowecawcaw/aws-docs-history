# Request Load balancer Capacity Unit reservation for your Network Load Balancer

Before you use LCU reservation, review the following:

- LCU reservation is not supported on Network Load Balancers using TLS listeners.
- LCU reservation only supports reserving throughput capacity for
  Network Load Balancers. When requesting a LCU reservation, convert your capacity
  needs from Mbps to LCUs using the conversion rate of 1 LCU to 2.2
  Mbps.
- Capacity is reserved at the regional level and is evenly
  distributed across availability zones. Confirm you have
  enough evenly distributed targets in each availability zone
  before turning on LCU reservation.
- LCU reservation requests are fulfilled on a first
  come first serve basis, and depends on available capacity
  for a zone at that time. Most requests are typically fulfilled
  within an hour, but can take up to a few hours.
- To update an existing reservation, the previous request
  must be provisioned or failed. You can increase reserved
  capacity as many times as you need, however you can only decrease the
  reserved capacity two times per day.
- You will continue to incur charges for any reserved or provisioned
  capacity until they are terminated or cancelled.

Console

###### To request an LCU reservation

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, choose **Load Balancers**.
3. Select the load balancer name.
4. On the **Capacity** tab, choose **Edit LCU
   Reservation**.
5. Select **Historic reference based estimate**.
6. Select the reference period to view the recommended reserved LCU level.
7. If you do not have historic reference workload, you can choose
   **Manual estimate** and enter the number of LCUs
   to be reserved.
8. Choose **Save**.

AWS CLI

###### To request an LCU reservation

Use the [modify-capacity-reservation](../../../cli/latest/reference/elbv2/modify-capacity-reservation.md "../../../cli/latest/reference/elbv2/modify-capacity-reservation.md")
command.

```
aws elbv2 modify-capacity-reservation \
    --load-balancer-arn `load-balancer-arn` \
    --minimum-load-balancer-capacity CapacityUnits=`3000`
```

CloudFormation

###### To request an LCU reservation

Update the [AWS::ElasticLoadBalancingV2::LoadBalancer](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-loadbalancer.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-loadbalancer.md")
resource.

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
        CapacityUnits: `3000`
```
