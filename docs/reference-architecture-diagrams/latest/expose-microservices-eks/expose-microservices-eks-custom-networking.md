# Deal with Pod IP Exhaustion

This architecture shows how to deal with pod IP exhaustion by adding secondary CIDR blocks from the [RFC 6598](https://datatracker.ietf.org/doc/html/rfc6598 "https://datatracker.ietf.org/doc/html/rfc6598") address space to your [Amazon VPC](../../../vpc/latest/userguide/what-is-amazon-vpc.md "../../../vpc/latest/userguide/what-is-amazon-vpc.md"). Using the [CNI Custom Networking](../../../eks/latest/userguide/cni-custom-network.md "../../../eks/latest/userguide/cni-custom-network.md") feature, pods no longer consume [RFC 1918](https://datatracker.ietf.org/doc/html/rfc1918 "https://datatracker.ietf.org/doc/html/rfc1918") IP addresses in the VPC.

## Deal with Pod IP Exhaustion

![Architecture diagram showing Amazon EKS custom networking with secondary CIDR blocks to address pod IP exhaustion.](images/expose-microservices-eks-2.png)

The following steps describe the inbound external flow:

1. Amazon Route 53 resolves incoming requests to the public ELB deployed by the AWS Load Balancer Controller.
2. The ELBs forward traffic to applications. You choose between instance mode (traffic sent to a worker node, then the service redirects to the pod) or IP mode (traffic directed to the pod IP directly).

The following steps describe the inbound internal flow:

1. Amazon Route 53 resolves incoming requests to the private ELB deployed by the [AWS Load Balancer Controller](https://kubernetes-sigs.github.io/aws-load-balancer-controller/v2.3/how-it-works/ "https://kubernetes-sigs.github.io/aws-load-balancer-controller/v2.3/how-it-works/") using a private hosted zone.
2. The ELBs forward traffic to applications in instance mode or IP mode.

The following steps describe the outbound external flow:

1. A pod in a private subnet initiates an outbound request to the internet. The private route table forwards traffic to the NAT gateway (NGW).
2. The public route table forwards traffic from the NGW to the internet gateway (IGW).

The following steps describe the outbound internal flow:

1. A pod in a private subnet initiates an outbound request to the on-premises network. The private route table forwards traffic to the virtual private gateway (VGW).
2. Traffic reaches the on-premises network over the VPN or AWS Direct Connect connection.

###### Note

The default behavior of Amazon EKS is to source NAT pod traffic to the primary IP address of the hosting worker node. [AWS Fargate](https://aws.amazon.com/fargate/ "https://aws.amazon.com/fargate/") for Amazon EKS supports additional CIDRs. The [ENIConfig custom resource](https://www.eksworkshop.com/beginner/160_advanced-networking/secondary_cidr/eniconfig_crd/ "https://www.eksworkshop.com/beginner/160_advanced-networking/secondary_cidr/eniconfig_crd/") defines the subnet in which pods are scheduled. See this [blog post](https://aws.amazon.com/blogs/containers/eks-vpc-routable-ip-address-conservation/ "https://aws.amazon.com/blogs/containers/eks-vpc-routable-ip-address-conservation/") for multi-account settings.

## Further reading

For additional information, refer to the following resources:

- [AWS Architecture Icons](https://aws.amazon.com/architecture/icons "https://aws.amazon.com/architecture/icons")
- [AWS Architecture Center](https://aws.amazon.com/architecture "https://aws.amazon.com/architecture")
- [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected "https://aws.amazon.com/architecture/well-architected")

## Diagram history

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change                                                                                                                         | Description                                     | Date              |
| ------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------- | ----------------- |
| [Initial publication](expose-microservices-eks-ipv4.md#diagram-history "expose-microservices-eks-ipv4.md#diagram-history")     | Reference architecture diagram first published. | February 22, 2022 |
| Initial publication                                                                                                            | Reference architecture diagram first published. | February 22, 2022 |
| [Initial publication](expose-microservices-eks-ipv6.md#diagram-history-3 "expose-microservices-eks-ipv6.md#diagram-history-3") | Reference architecture diagram first published. | February 22, 2022 |

###### Note

To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.
