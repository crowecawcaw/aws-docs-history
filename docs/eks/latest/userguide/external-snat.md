**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Enable outbound internet access for Pods

**Applies to**: Linux `IPv4` Fargate nodes, Linux nodes with Amazon EC2 instances

If you deployed your cluster using the `IPv6` family, then the information in this topic isn’t applicable to your cluster, because `IPv6` addresses are not network translated. For more information about using `IPv6` with your cluster, see [Learn about IPv6 addresses to clusters, Pods, and services](cni-ipv6.md "cni-ipv6.md").

By default, each Pod in your cluster is assigned a [private](../../../AWSEC2/latest/UserGuide/using-instance-addressing.md#concepts-private-addresses "../../../AWSEC2/latest/UserGuide/using-instance-addressing.md#concepts-private-addresses")
`IPv4` address from a classless inter-domain routing (CIDR) block that is associated with the VPC that the Pod is deployed in. Pods in the same VPC communicate with each other using these private IP addresses as end points. When a Pod communicates to any `IPv4` address that isn’t within a CIDR block that’s associated to your VPC, the Amazon VPC CNI plugin (for both [Linux](https://github.com/aws/amazon-vpc-cni-k8s#amazon-vpc-cni-k8s "https://github.com/aws/amazon-vpc-cni-k8s#amazon-vpc-cni-k8s") or [Windows](https://github.com/aws/amazon-vpc-cni-plugins/tree/master/plugins/vpc-bridge "https://github.com/aws/amazon-vpc-cni-plugins/tree/master/plugins/vpc-bridge")) translates the Pod’s `IPv4` address to the primary private `IPv4` address of the primary [elastic network interface](../../../AWSEC2/latest/UserGuide/using-eni.md#eni-basics "../../../AWSEC2/latest/UserGuide/using-eni.md#eni-basics") of the node that the Pod is running on, by default [\*](#snat-exception "#snat-exception").

###### Note

For Windows nodes, there are additional details to consider. By default, the [VPC CNI plugin for Windows](https://github.com/aws/amazon-vpc-cni-plugins/tree/master/plugins/vpc-bridge "https://github.com/aws/amazon-vpc-cni-plugins/tree/master/plugins/vpc-bridge") is defined with a networking configuration in which the traffic to a destination within the same VPC is excluded for SNAT. This means that internal VPC communication has SNAT disabled and the IP address allocated to a Pod is routable inside the VPC. But traffic to a destination outside of the VPC has the source Pod IP SNAT’ed to the instance ENI’s primary IP address. This default configuration for Windows ensures that the pod can access networks outside of your VPC in the same way as the host instance.

Due to this behavior:

- Your Pods can communicate with internet resources only if the node that they’re running on has a [public](../../../AWSEC2/latest/UserGuide/using-instance-addressing.md#concepts-public-addresses "../../../AWSEC2/latest/UserGuide/using-instance-addressing.md#concepts-public-addresses") or [elastic](../../../vpc/latest/userguide/vpc-eips.md "../../../vpc/latest/userguide/vpc-eips.md") IP address assigned to it and is in a [public subnet](../../../vpc/latest/userguide/configure-subnets.md#subnet-basics "../../../vpc/latest/userguide/configure-subnets.md#subnet-basics"). A public subnet’s associated [route table](../../../vpc/latest/userguide/VPC_Route_Tables.md "../../../vpc/latest/userguide/VPC_Route_Tables.md") has a route to an internet gateway. We recommend deploying nodes to private subnets, whenever possible.
- For versions of the plugin earlier than `1.8.0`, resources that are in networks or VPCs that are connected to your cluster VPC using [VPC peering](../../../vpc/latest/peering/what-is-vpc-peering.md "../../../vpc/latest/peering/what-is-vpc-peering.md"), a [transit VPC](../../../whitepapers/latest/aws-vpc-connectivity-options/transit-vpc-option.md "../../../whitepapers/latest/aws-vpc-connectivity-options/transit-vpc-option.md"), or [AWS Direct Connect](../../../directconnect/latest/UserGuide/Welcome.md "../../../directconnect/latest/UserGuide/Welcome.md") can’t initiate communication to your Pods behind secondary elastic network interfaces. Your Pods can initiate communication to those resources and receive responses from them, though.
  If either of the following statements are true in your environment, then change the default configuration with the command that follows.

- You have resources in networks or VPCs that are connected to your cluster VPC using [VPC peering](../../../vpc/latest/peering/what-is-vpc-peering.md "../../../vpc/latest/peering/what-is-vpc-peering.md"), a [transit VPC](../../../whitepapers/latest/aws-vpc-connectivity-options/transit-vpc-option.md "../../../whitepapers/latest/aws-vpc-connectivity-options/transit-vpc-option.md"), or [AWS Direct Connect](../../../directconnect/latest/UserGuide/Welcome.md "../../../directconnect/latest/UserGuide/Welcome.md") that need to initiate communication with your Pods using an `IPv4` address and your plugin version is earlier than `1.8.0`.
- Your Pods are in a [private subnet](../../../vpc/latest/userguide/configure-subnets.md#subnet-basics "../../../vpc/latest/userguide/configure-subnets.md#subnet-basics") and need to communicate outbound to the internet. The subnet has a route to a [NAT gateway](../../../vpc/latest/userguide/vpc-nat-gateway.md "../../../vpc/latest/userguide/vpc-nat-gateway.md").

```
kubectl set env daemonset -n kube-system aws-node AWS_VPC_K8S_CNI_EXTERNALSNAT=true
```

###### Note

The `AWS_VPC_K8S_CNI_EXTERNALSNAT` and `AWS_VPC_K8S_CNI_EXCLUDE_SNAT_CIDRS` CNI configuration variables aren’t applicable to Windows nodes. Disabling SNAT isn’t supported for Windows. As for excluding a list of `IPv4` CIDRs from SNAT, you can define this by specifying the `ExcludedSnatCIDRs` parameter in the Windows bootstrap script. For more information on using this parameter, see [Bootstrap script configuration parameters](eks-optimized-windows-ami.md#bootstrap-script-configuration-parameters "eks-optimized-windows-ami.md#bootstrap-script-configuration-parameters").

## Host networking

\* If a Pod’s spec contains `hostNetwork=true` (default is `false`), then its IP address isn’t translated to a different address. This is the case for the `kube-proxy` and Amazon VPC CNI plugin for Kubernetes Pods that run on your cluster, by default. For these Pods, the IP address is the same as the node’s primary IP address, so the Pod’s IP address isn’t translated. For more information about a Pod’s `hostNetwork` setting, see [PodSpec v1 core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.33/#podspec-v1-core "https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.33/#podspec-v1-core") in the Kubernetes API reference.
