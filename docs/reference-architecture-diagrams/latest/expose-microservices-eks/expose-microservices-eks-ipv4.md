

# Expose Microservices in a Hybrid Scenario Using Amazon EKS
<a name="expose-microservices-eks-ipv4"></a>

Publication date: **February 22, 2022 ([Diagram history](#diagram-history))**

This architecture shows how to expose [Amazon Elastic Kubernetes Service](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html) microservices hosted in private subnets to the internet and on-premises networks. The [AWS Load Balancer Controller](https://kubernetes-sigs.github.io/aws-load-balancer-controller/v2.3/guide/service/annotations/) manages Elastic Load Balancers (ELBs) for Kubernetes services and ingresses.

## Expose Microservices in a Hybrid Scenario Using Amazon EKS
<a name="diagram1"></a>

![Architecture diagram showing Amazon EKS microservices exposed through public and private load balancers in a VPC with public and private subnets.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/expose-microservices-eks/images/expose-microservices-eks-1.png)


The following steps describe the inbound external flow:

1. [Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html) resolves incoming requests to the public ELB deployed by the [AWS Load Balancer Controller](https://kubernetes-sigs.github.io/aws-load-balancer-controller/v2.3/how-it-works/).

1. The ELBs forward traffic to applications. You can choose between two modes: instance mode (traffic sent to a worker node, then the [service](https://kubernetes.io/docs/concepts/services-networking/service/) redirects traffic to the pod) or IP mode (traffic directed to the IP of the pod directly). See [cluster networking details](https://aws.amazon.com/blogs/containers/de-mystifying-cluster-networking-for-amazon-eks-worker-nodes/) for more information.

The following steps describe the inbound internal flow:

1. Amazon Route 53 resolves incoming requests to the private ELB deployed by the AWS Load Balancer Controller using a private hosted zone.

1. The ELBs forward traffic to applications in instance mode or IP mode.

The following steps describe the outbound external flow:

1. When a pod in a private subnet initiates an outbound request to the internet, the private route table forwards traffic to the NAT gateway (NGW).

1. The public route table forwards traffic from the NGW to the internet gateway (IGW).

The following steps describe the outbound internal flow:

1. A pod in a private subnet initiates an outbound request to the on-premises network. The private route table forwards traffic to the virtual private gateway (VGW).

1. Traffic reaches the on-premises network over the VPN or AWS Direct Connect connection.

**Note**  
You can use [ingress controllers](https://www.eksworkshop.com/beginner/130_exposing-service/ingress/) such as the [NGINX ingress controller](https://kubernetes.github.io/ingress-nginx/deploy/) as an alternative to the AWS Load Balancer Controller. If you use [AWS Fargate](https://docs.aws.amazon.com/eks/latest/userguide/fargate.html) for Amazon EKS, you only have pod ENIs in the private subnets and must use ELBs with IP mode.

## Further reading
<a name="further-reading"></a>

For additional information, refer to the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | February 22, 2022 | 
| [Initial publication](expose-microservices-eks-custom-networking.md#diagram-history-2) | Reference architecture diagram first published. | February 22, 2022 | 
| [Initial publication](expose-microservices-eks-ipv6.md#diagram-history-3) | Reference architecture diagram first published. | February 22, 2022 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.