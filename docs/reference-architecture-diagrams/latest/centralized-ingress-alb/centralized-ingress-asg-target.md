

# Centralized Ingress - Auto Scaling Group Target
<a name="centralized-ingress-asg-target"></a>

Publication date: **March 24, 2022 ([Diagram history](#asg-diagram-history))**

This architecture adds a [Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html) with a static IP to eliminate the need for manual instance registration. The [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html) in the Central Ingress VPC targets the Network Load Balancer IP address through [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html), and instances register automatically using an Auto Scaling group.

## Centralized ingress with Auto Scaling group target architecture
<a name="asg-diagram1"></a>

![Architecture diagram showing centralized ingress with Application Load Balancer targeting Network Load Balancer static IP for Auto Scaling group registration.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/centralized-ingress-alb/images/centralized-ingress-alb-2.png)


The following steps describe the data flow in this architecture:

1. Traffic from the internet reaches the **Central Ingress VPC**. The Application Load Balancer sends the request to the target group using the Network Load Balancer static IP address through AWS Transit Gateway.

1. The traffic forwards to the **Application VPC** according to the Transit Gateway route table associated with the **Central Ingress VPC**.

1. The traffic enters the Application VPC and forwards to the Network Load Balancer IP address.

1. The Network Load Balancer forwards the traffic to registered instances in the Auto Scaling group using an instance ID target type.

For more information about Application Load Balancer target group types, see [Target groups for your Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-target-groups.html).

For more information about Network Load Balancer target group types, see [Target groups for your Network Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html).

## Further reading
<a name="asg-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="asg-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](centralized-ingress-ec2-target.md#ec2t-diagram-history) | Reference architecture diagram first published. | March 24, 2022 | 
| [Initial publication](#asg-diagram-history) | Reference architecture diagram first published. | March 24, 2022 | 
| [Initial publication](centralized-ingress-asg-alb-target.md#asgalb-diagram-history) | Reference architecture diagram first published. | March 24, 2022 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.