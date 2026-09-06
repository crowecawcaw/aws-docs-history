

# Centralized Ingress - Amazon EC2 Target
<a name="centralized-ingress-ec2-target"></a>

Publication date: **March 24, 2022 ([Diagram history](#ec2t-diagram-history))**

This architecture uses a centralized ingress Amazon VPC with a public [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html) and IP targets. You directly target the IP addresses of Amazon EC2 instances in the application VPC through [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html). This approach requires manual management of IP registrations on the ALB.

## Centralized ingress with Amazon EC2 target architecture
<a name="ec2t-diagram1"></a>

![Architecture diagram showing centralized ingress with Application Load Balancer using IP targets to reach EC2 instances through AWS Transit Gateway.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/centralized-ingress-alb/images/centralized-ingress-alb-1.png)


The following steps describe the data flow in this architecture:

1. Traffic from the internet reaches the **Central Ingress VPC**. The Application Load Balancer sends the request to the target group with the configured IP address through AWS Transit Gateway.

1. The traffic forwards to the **Application VPC** according to the Transit Gateway route table associated with the **Central Ingress VPC**.

1. The traffic enters the Application VPC and forwards to the Amazon EC2 instance.

For more information about Application Load Balancer target group types, see [Target groups for your Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-target-groups.html).

## Further reading
<a name="ec2t-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="ec2t-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#ec2t-diagram-history) | Reference architecture diagram first published. | March 24, 2022 | 
| [Initial publication](centralized-ingress-asg-target.md#asg-diagram-history) | Reference architecture diagram first published. | March 24, 2022 | 
| [Initial publication](centralized-ingress-asg-alb-target.md#asgalb-diagram-history) | Reference architecture diagram first published. | March 24, 2022 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.