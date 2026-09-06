

# Centralized Ingress - Auto Scaling Group Target with ALB
<a name="centralized-ingress-asg-alb-target"></a>

Publication date: **March 24, 2022 ([Diagram history](#asgalb-diagram-history))**

This architecture chains a [Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html) and [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html) in the application VPC. The Network Load Balancer static IP eliminates manual registration, and the chained ALB provides layer 7 load balancing capabilities at the application level.

## Centralized ingress with Auto Scaling group and ALB target architecture
<a name="asgalb-diagram1"></a>

![Architecture diagram showing centralized ingress with chained Network Load Balancer and Application Load Balancer for layer 7 load balancing with Auto Scaling groups.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/centralized-ingress-alb/images/centralized-ingress-alb-3.png)


The following steps describe the data flow in this architecture:

1. Traffic from the internet reaches the **Central Ingress VPC**. The Application Load Balancer sends the request to the target group with the Network Load Balancer IP address through AWS Transit Gateway.

1. The traffic forwards to the **Application VPC** according to the Transit Gateway route table associated with the **Central Ingress VPC**.

1. The traffic enters the Application VPC and forwards to the Network Load Balancer IP address.

1. The Network Load Balancer forwards the traffic to the Application Load Balancer using an ALB-type target group.

1. The Application Load Balancer forwards the traffic to registered instances in the Auto Scaling group using an instance ID target type.

For more information about Application Load Balancer target group types, see [Target groups for your Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-target-groups.html).

For more information about Network Load Balancer target group types, see [Target groups for your Network Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html).

## Further reading
<a name="asgalb-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="asgalb-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](centralized-ingress-ec2-target.md#ec2t-diagram-history) | Reference architecture diagram first published. | March 24, 2022 | 
| [Initial publication](centralized-ingress-asg-target.md#asg-diagram-history) | Reference architecture diagram first published. | March 24, 2022 | 
| [Initial publication](#asgalb-diagram-history) | Reference architecture diagram first published. | March 24, 2022 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.