**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Review EKS Auto Mode release notes

This page documents updates to Amazon EKS Auto Mode. You can periodically check this page for announcements about features, bug fixes, known issues, and deprecated functionality.

To receive notifications of all source file changes to this specific documentation page, you can subscribe to the following URL with an RSS reader:

```
https://github.com/awsdocs/amazon-eks-user-guide/commits/mainline/latest/ug/automode/auto-change.adoc.atom
```

## August 12, 2026

**Feature**: The Amazon EKS Auto Mode load balancer controller now supports features from AWS Load Balancer Controller through v3.4. Note that Gateway API is not supported yet.

- JWT validation for Ingress – Validate JSON Web Tokens (JWTs) at the Application Load Balancer (ALB) listener rule level before requests reach your backend, through a new Ingress-level action. For more information, see [Application Load Balancer now supports client credential flow with JWT verification](https://aws.amazon.com/about-aws/whats-new/2025/11/application-load-balancer-jwt-verification/ "https://aws.amazon.com/about-aws/whats-new/2025/11/application-load-balancer-jwt-verification/").
- Network Load Balancer (NLB) weighted target groups – Distribute traffic across multiple target groups by weight on an NLB Service. This supports blue-green and canary deployment patterns, including a weight of 0 when at least one other target group has a non-zero weight. For more information, see [Network Load Balancers now support Weighted Target Groups](https://aws.amazon.com/blogs/networking-and-content-delivery/network-load-balancers-now-support-weighted-target-groups/ "https://aws.amazon.com/blogs/networking-and-content-delivery/network-load-balancers-now-support-weighted-target-groups/").
- TargetGroupBinding reconciliation events – Amazon EKS now emits Kubernetes events on TargetGroupBinding reconciliation failures, making target registration problems visible through `kubectl describe` instead of controller logs only.
- Subnet ordering preserved – The `aws-load-balancer-subnets` annotation now honors the order you specify, rather than reordering subnets internally.
- Cross-zone load balancing for ALB – You can now explicitly disable cross-zone load balancing on Application Load Balancers.

## August 5, 2026

**Feature**: The Amazon EKS Auto Mode load balancer controller now supports multi-cluster target groups, matching the behavior of the AWS Load Balancer Controller. With this feature, you can share the same target group ARN across multiple `TargetGroupBinding` resources, so a single target group can serve multiple Kubernetes clusters (in the same VPC) or accept targets from other sources. For more information, see [Configure multi-cluster target groups](auto-multi-cluster-target-groups.md "auto-multi-cluster-target-groups.md").

## July 27, 2026

**Feature**: The Amazon Elastic Kubernetes Service (Amazon EKS) Auto Mode load balancer controller now supports features from AWS Load Balancer Controller v2.13 and v2.14.

- Application Load Balancer (ALB) URL Rewrite – You can now transform request URLs and Host headers before requests reach your backend services, without changing your application. For more information, see [Introducing URL and host header rewrite with AWS Application Load Balancers](https://aws.amazon.com/blogs/networking-and-content-delivery/introducing-url-and-host-header-rewrite-with-aws-application-load-balancers/ "https://aws.amazon.com/blogs/networking-and-content-delivery/introducing-url-and-host-header-rewrite-with-aws-application-load-balancers/").
- PrefixListsIDs and LoadBalancerName in IngressClassParams – You can now set security group prefix lists and a custom load balancer name for your Application Load Balancer. Both are supported as Ingress annotations and as fields in IngressClassParams (prefixListsIDs and loadBalancerName). When set in IngressClassParams, the configuration applies to all Ingresses in the IngressClass. You no longer need to annotate every Ingress resource individually.
- Frontend NLB for Ingress – You can now place a Network Load Balancer (NLB) in front of an Application Load Balancer. This combines NLB static IP addresses and AWS PrivateLink with the layer-7 routing capabilities of ALB. Enable this feature with the alb.ingress.kubernetes.io/enable-frontend-nlb annotation. For more information, see [Application Load Balancer-type Target Group for Network Load Balancer](https://aws.amazon.com/blogs/networking-and-content-delivery/application-load-balancer-type-target-group-for-network-load-balancer/ "https://aws.amazon.com/blogs/networking-and-content-delivery/application-load-balancer-type-target-group-for-network-load-balancer/").
- TCP\_UDP listener support – NLB Services can now use TCP\_UDP listeners, which allow both TCP and UDP traffic on the same port. Enable this feature with the service.beta.kubernetes.io/aws-load-balancer-enable-tcp-udp-listener annotation.
- Per-target-group proxy protocol – You can now configure Proxy Protocol v2 headers at the individual target group level by using the service.beta.kubernetes.io/aws-load-balancer-proxy-protocol-per-target-group annotation, rather than applying the configuration to all target groups uniformly.
- targetType field in IngressClassParams – You can now set the default target type (instance or IP) directly in IngressClassParams, removing the need to annotate every Ingress resource individually.
- Subnet discovery by reachability – Subnet selection no longer strictly requires kubernetes.io/role tags. The controller now falls back to route-table-based reachability analysis when tags are absent. The controller doesn’t currently support this fallback for load balancers with an ip-address-type of dualstack.
- IPv4 IP Address Manager (IPAM) support for ALB – An internet-facing ALB can now draw its public IPv4 addresses from an Amazon Virtual Private Cloud (Amazon VPC) IPAM pool instead of from AWS-managed address ranges. This gives you predictable IP address blocks for allow lists. Specify the pool with the alb.ingress.kubernetes.io/ipam-ipv4-pool-id annotation. For more information, see [Simplify ALB’s public IP address assignment with VPC IPAM](https://aws.amazon.com/blogs/networking-and-content-delivery/simplify-albs-public-ip-address-assignment-with-vpc-ipam/ "https://aws.amazon.com/blogs/networking-and-content-delivery/simplify-albs-public-ip-address-assignment-with-vpc-ipam/").

**Feature**: Added the `Balanced` consolidation policy for EKS Auto Mode NodePools. Setting `spec.disruption.consolidationPolicy: Balanced` scores each consolidation action by weighing compute cost savings against disruption cost. It skips actions where the disruption outweighs the savings. If you use `WhenEmpty` today, you can switch to `Balanced` to gain the cost savings of consolidation. If you use `WhenEmptyOrUnderutilized` today, you can switch to `Balanced` to eliminate pod disruption for marginal benefits. `WhenEmpty` and `WhenEmptyOrUnderutilized` are unchanged, and existing NodePools keep their current behavior. For more information, see [Create a Node Pool for EKS Auto Mode](create-node-pool.md "create-node-pool.md") and [Disruption](https://karpenter.sh/docs/concepts/disruption/ "https://karpenter.sh/docs/concepts/disruption/") in the Karpenter documentation.

## July 21, 2026

**Feature**: Added support for static network interface configuration on NodeClass. You can now configure Elastic Fabric Adapter (EFA) network interfaces using `advancedNetworking.networkInterfaces` for both dynamic and static capacity provisioning, enabling EFA-ready nodes for distributed training and inference workloads. For more information, see [Static Network Interface Configuration](create-node-class.md#static-network-interfaces "create-node-class.md#static-network-interfaces").

## June 30, 2026

**Feature**: The EKS Auto Mode load balancer controller now supports features from AWS Load Balancer Controller v2.10, v2.11, and v2.12.

From upstream v2.12.0:

- Listener rule priority management — The controller can now explicitly set and reorder listener rule priorities, resolving ordering conflicts when multiple Ingress rules target the same listener

From upstream v2.11.0:

- Load Balancer Capacity Unit (LCU) Reservation — You can now reserve capacity units on both Application Load Balancers (ALBs) and Network Load Balancers (NLBs), ensuring predictable performance for workloads with known traffic patterns

From upstream v2.10.0:

- ALB Shield Advanced protection — ALB resources can now be protected with AWS Shield Advanced via the alb.ingress.kubernetes.io/shield-advanced-protection annotation
- Bring your own custom TargetGroupBinding — You can now reference pre-existing target groups not created by the controller, enabling integration with externally managed infrastructure
- UDP support for dual-stack NLB on IPv6 clusters — NLB Services on IPv6 clusters now support UDP protocol listeners
- ALB HTTP and HTTPS listener attributes — Fine-grained control over listener-level attributes (for example, routing behavior, header modifications) via annotations

### Update on managed policies

AWS has updated AmazonEKSServiceRolePolicy and AmazonEKSLoadBalancingPolicy to support these new features.

### Action required for customers using custom IAM policies

If you are supplying your own custom IAM policy for the EKS Auto Mode cluster role instead of using the AWS-managed AmazonEKSLoadBalancingPolicy, you must ensure your policy includes the permissions listed above. Failure to update your custom policy will result in access denied errors when using the new features.

To verify parity, compare your custom policy against the [latest version of AmazonEKSLoadBalancingPolicy](../../../aws-managed-policy/latest/reference/AmazonEKSLoadBalancingPolicy.md "../../../aws-managed-policy/latest/reference/AmazonEKSLoadBalancingPolicy.md").

Specifically, ensure your policy includes:

- elasticloadbalancing:ModifyCapacityReservation, elasticloadbalancing:ModifyIpPools, elasticloadbalancing:ModifyListenerAttributes, and elasticloadbalancing:SetRulePriorities
- ec2:DescribeIpamPools and ec2:DescribeRouteTables
- shield:CreateProtection, shield:DeleteProtection, and shield:TagResource

## June 9, 2026

**Feature**: Added instance status check monitoring to EKS Auto Mode. The compute controller now polls EC2 `DescribeInstanceStatus` to detect scheduled maintenance events and instance or system status check failures, automatically replacing unhealthy nodes.

## June 4, 2026

**Documentation**: Added guidance on controlling compute costs in EKS Auto Mode, including how consolidation works, what blocks it, and recommended patterns for bursty workloads. For more information, see [Cost optimization in EKS Auto Mode](auto-cost-control.md "auto-cost-control.md").

## June 3, 2026

**Feature**: Added support for Interruptible Capacity Reservations in EKS Auto Mode. For more information, see [Control deployment of workloads into Capacity Reservations with EKS Auto Mode](auto-odcr.md "auto-odcr.md").

## May 5, 2026

**Feature**: Added support for EC2 Placement Groups in EKS Auto Mode. For more information, see [Node Class Specification](create-node-class.md#auto-node-class-spec "create-node-class.md#auto-node-class-spec").

## April 10, 2026

**New supported instance types**: p6-b200, p6-b300, p5e, p5en, trn2, hpc8a, x8aedz, x8i. For the full list of supported instances, see [Learn about Amazon EKS Auto Mode Managed instances](automode-learn-instances.md "automode-learn-instances.md").

## April 2, 2026

**Chore**: NodeClass dry run validation will now use dynamically selected instance types based on linked NodePools.

## February 2, 2026

**Feature**: Added support to disable v4Egress traffic from IPv6 pods in EKS Auto Mode IPv6 clusters. For more information, see [Disable IPv4 egress from IPv6 pods in IPv6 clusters.](create-node-class.md#enableV4Egress "create-node-class.md#enableV4Egress").

## December 19, 2025

**Feature**: Added support for secondary IP mode that provisions secondary IP addresses instead of prefixes to Auto nodes. The mode maintains one secondary IP as MinimalIPTarget and saves IP resources for customers who don’t need to warm up more secondary IPs or prefixes. For more information, see [Node Class Specification](create-node-class.md#auto-node-class-spec "create-node-class.md#auto-node-class-spec") and [Secondary IP Mode for Pods](create-node-class.md#secondary-IP-mode "create-node-class.md#secondary-IP-mode").

## November 19, 2025

**Feature**: Enabled Seekable OCI (SOCI) parallel pull and unpack for G, P, and Trn family instances with local NVMe storage. SOCI parallel pull and unpack is always used for these instance families with EKS Auto Mode and there are no configuration changes required to enable it. For more information on SOCI, see the [launch blog](https://aws.amazon.com/blogs/containers/introducing-seekable-oci-parallel-pull-mode-for-amazon-eks/ "https://aws.amazon.com/blogs/containers/introducing-seekable-oci-parallel-pull-mode-for-amazon-eks/").

## November 19, 2025

**Feature**: Added support for static-capacity node pools that maintain a fixed number of nodes. For more information, see [Static Capacity Node Pools in EKS Auto Mode](auto-static-capacity.md "auto-static-capacity.md").

## October 23, 2025

**Feature:** Users with clusters in US regions can now request to use FIPS compatible AMIs by specifying `spec.advancedSecurity.fips` in their NodeClass definition.

## October 1, 2025

**Feature:** EKS Auto Mode now supports deploying nodes to AWS Local Zones. For more information, see [Deploy EKS Auto Mode nodes onto Local Zones](auto-local-zone.md "auto-local-zone.md").

## September 30, 2025

**Feature:** Added support for instanceProfile to the NodeClass `spec.instanceProfile` which is mutually exclusive from the `spec.role` field.

## September 29, 2025

DRA is not currently supported by EKS Auto Mode.

## September 10, 2025

**Chore:** Events fired from the Auto Mode Compute controller will now use the name `eks-auto-mode/compute` instead of `karpenter`.

## August 24, 2025

**Bug Fix:** VPCs that used a DHCP option set with a custom domain name that contained capital letters would cause Nodes to fail to join the cluster due to generating an invalid hostname. This has been resolved and domain names with capital letters now work correctly.

## August 15, 2025

**Bug Fix:** The Pod Identity Agent will now only listen on the IPv4 Link Local address in an IPv4 EKS cluster to avoid issues where the Pod can’t reach the IPv6 address.

## August 6, 2025

**Feature:** Added new configuration on the NodeClass `spec.advancedNetworking.associatePublicIPAddress` which can be used to prevent public IP addresses from being assigned to EKS Auto Mode Nodes

## June 30, 2025

**Feature:** The Auto Mode NodeClass now uses the configured custom KMS key to encrypt the read-only root volume of the instance, in addition to the read/write data volume. Previously, the custom KMS key was only used to encrypt the data volume.

## June 20, 2025

**Feature:** Support for controlling deployment of workloads into EC2 On-Demand Capacity Reservations (ODCRs). This adds the optional key `capacityReservationSelectorTerms` to the NodeClass, allowing you to explicitly control which ODCRs your workloads use. For more information, see [Control deployment of workloads into Capacity Reservations with EKS Auto Mode](auto-odcr.md "auto-odcr.md").

## June 13, 2025

**Feature:** Support for separate pod subnets in the `NodeClass`. This adds the optional keys `podSubnetSelectorTerms` and `podSecurityGroupSelectorTerms` to set the subnets and security groups for the pods. For more information, see [Separate subnets and security groups for Pods](create-node-class.md#pod-subnet-selector "create-node-class.md#pod-subnet-selector").

## April 30, 2025

**Feature:** Support for forward network proxies in the `NodeClass`. This adds the optional key `advancedNetworking` to set your HTTPS proxy. For more information, see [Node Class Specification](create-node-class.md#auto-node-class-spec "create-node-class.md#auto-node-class-spec").

## April 18, 2025

**Feature:** Support for resolving .local domains (typically reserved for Multicast DNS) via unicast DNS.

## April 11, 2025

**Feature:** Added `certificateBundles` and `ephemeralStorage.kmsKeyID` to `NodeClass`. For more information, see [Node Class Specification](create-node-class.md#auto-node-class-spec "create-node-class.md#auto-node-class-spec").

**Feature:** Improved image pull speed, particularly for instance types with local instance storage that can take advantage of the faster image decompression.

**Bug Fix:** Resolved a race condition which caused FailedCreatePodSandBox , Error while dialing: dial tcp 127.0.0.1:50051: connect: connection refused to sometimes occur for Pods scheduling to a Node immediately at startup.

## April 4, 2025

**Feature:** Increase `registryPullQPS` from 5 to 25 and `registryBurst` from 10 to 50 to reduce client enforced image pull throttling (`Failed to pull image xyz: pull QPS exceeded`)

## March 31, 2025

**Bug Fix:** Fixes an issue where if a Core DNS Pod is running on an Auto Mode node, DNS queries from Pods on the node would hit that Core DNS Pod instead of the node local DNS server. DNS queries from Pods on an Auto Mode node will always go to the node local DNS.

## March 21, 2025

**Bug Fix:** Auto Mode nodes now resolve `kube-dns.kube-system.svc.cluster.local` correctly when there isn’t a `kube-dns` service installed in the cluster. Addresses GitHub issue [#2546](https://github.com/aws/containers-roadmap/issues/2546 "https://github.com/aws/containers-roadmap/issues/2546").

## March 14, 2025

**Feature**: `IPv4` egress enabled in `IPv6` clusters. `IPv4` traffic egressing from `IPv6` Auto Mode clusters will now be automatically translated to the `v4` address of the node primary ENI.
