**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Assign security groups to individual Pods

**Applies to**: Linux nodes with Amazon EC2 instances

**Applies to**: Private subnets

Security groups for Pods integrate Amazon EC2 security groups with Kubernetes Pods. You can use Amazon EC2 security groups to define rules that allow inbound and outbound network traffic to and from Pods that you deploy to nodes running on many Amazon EC2 instance types and Fargate. For a detailed explanation of this capability, see the [Introducing security groups for Pods](https://aws.amazon.com/blogs/containers/introducing-security-groups-for-pods "https://aws.amazon.com/blogs/containers/introducing-security-groups-for-pods") blog post.

## Compatibility with Amazon VPC CNI plugin for Kubernetes features

You can use security groups for Pods with the following features:

- IPv4 Source Network Address Translation - For more information, see [Enable outbound internet access for Pods](external-snat.md "external-snat.md").
- IPv6 addresses to clusters, Pods, and services - For more information, see [Learn about IPv6 addresses to clusters, Pods, and services](cni-ipv6.md "cni-ipv6.md").
- Restricting traffic using Kubernetes network policies - For more information, see [Limit Pod traffic with Kubernetes network policies](cni-network-policy.md "cni-network-policy.md").

## Considerations

Before deploying security groups for Pods, consider the following limitations and conditions:

- Security groups for Pods can’t be used with Windows nodes.
- Security groups for Pods can be used with clusters configured for the `IPv6` family that contain Amazon EC2 nodes by using version 1.16.0 or later of the Amazon VPC CNI plugin. You can use security groups for Pods with clusters configure `IPv6` family that contain only Fargate nodes by using version 1.7.7 or later of the Amazon VPC CNI plugin. For more information, see [Learn about IPv6 addresses to clusters, Pods, and services](cni-ipv6.md "cni-ipv6.md")
- Security groups for Pods are supported by most [Nitro-based](../../../AWSEC2/latest/UserGuide/instance-types.md#ec2-nitro-instances "../../../AWSEC2/latest/UserGuide/instance-types.md#ec2-nitro-instances") Amazon EC2 instance families, though not by all generations of a family. For example, the `m5`, `c5`, `r5`, `m6g`, `c6g`, and `r6g` instance family and generations are supported. No instance types in the `t` family are supported. For a complete list of supported instance types, see the [limits.go](https://github.com/aws/amazon-vpc-resource-controller-k8s/blob/v1.5.0/pkg/aws/vpc/limits.go "https://github.com/aws/amazon-vpc-resource-controller-k8s/blob/v1.5.0/pkg/aws/vpc/limits.go") file on GitHub. Your nodes must be one of the listed instance types that have `IsTrunkingCompatible: true` in that file.
- If you’re using custom networking and security groups for Pods together, the security group specified by security groups for Pods is used instead of the security group specified in the `ENIConfig`.
- If you’re using version `1.10.2` or earlier of the Amazon VPC CNI plugin and you include the `terminationGracePeriodSeconds` setting in your Pod spec, the value for the setting can’t be zero.
- If you’re using version `1.10` or earlier of the Amazon VPC CNI plugin, or version `1.11` with `POD_SECURITY_GROUP_ENFORCING_MODE`=`strict`, which is the default setting, then Kubernetes services of type `NodePort` and `LoadBalancer` using instance targets with an `externalTrafficPolicy` set to `Local` aren’t supported with Pods that you assign security groups to. For more information about using a load balancer with instance targets, see [Route TCP and UDP traffic with Network Load Balancers](network-load-balancing.md "network-load-balancing.md").
- If you’re using version `1.10` or earlier of the Amazon VPC CNI plugin or version `1.11` with `POD_SECURITY_GROUP_ENFORCING_MODE`=`strict`, which is the default setting, source NAT is disabled for outbound traffic from Pods with assigned security groups so that outbound security group rules are applied. To access the internet, Pods with assigned security groups must be launched on nodes that are deployed in a private subnet configured with a NAT gateway or instance. Pods with assigned security groups deployed to public subnets are not able to access the internet.

If you’re using version `1.11` or later of the plugin with `POD_SECURITY_GROUP_ENFORCING_MODE`=`standard`, then Pod traffic destined for outside of the VPC is translated to the IP address of the instance’s primary network interface. For this traffic, the rules in the security groups for the primary network interface are used, rather than the rules in the Pod’s security groups.

- To use Calico network policy with Pods that have associated security groups, you must use version `1.11.0` or later of the Amazon VPC CNI plugin and set `POD_SECURITY_GROUP_ENFORCING_MODE`=`standard`. Otherwise, traffic flow to and from Pods with associated security groups are not subjected to Calico network policy enforcement and are limited to Amazon EC2 security group enforcement only. To update your Amazon VPC CNI version, see [Assign IPs to Pods with the Amazon VPC CNI](managing-vpc-cni.md "managing-vpc-cni.md")
- Pods running on Amazon EC2 nodes that use security groups in clusters that use [NodeLocal DNSCache](https://kubernetes.io/docs/tasks/administer-cluster/nodelocaldns/ "https://kubernetes.io/docs/tasks/administer-cluster/nodelocaldns/") are only supported with version `1.11.0` or later of the Amazon VPC CNI plugin and with `POD_SECURITY_GROUP_ENFORCING_MODE`=`standard`. To update your Amazon VPC CNI plugin version, see [Assign IPs to Pods with the Amazon VPC CNI](managing-vpc-cni.md "managing-vpc-cni.md")
- Security groups for Pods might lead to higher Pod startup latency for Pods with high churn. This is due to rate limiting in the resource controller.
- The EC2 security group scope is at the Pod-level - For more information, see [Security group](../../../vpc/latest/userguide/VPC_SecurityGroups.md "../../../vpc/latest/userguide/VPC_SecurityGroups.md").

If you set `POD_SECURITY_GROUP_ENFORCING_MODE=standard` and `AWS_VPC_K8S_CNI_EXTERNALSNAT=false`, traffic destined for endpoints outside the VPC use the node’s security groups, not the Pod’s security groups.
