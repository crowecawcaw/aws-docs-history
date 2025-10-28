**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Learn about VPC CNI modes and configuration

The Amazon VPC CNI plugin for Kubernetes provides networking for Pods. Use the following table to learn more about the available networking features.

| Networking feature                                                              | Learn more                                                                                                                         |
| ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Configure your cluster to assign IPv6 addresses to clusters, Pods, and services | [Learn about IPv6 addresses to clusters, Pods, and services](cni-ipv6.md "cni-ipv6.md")                                            |
| Use IPv4 Source Network Address Translation for Pods                            | [Enable outbound internet access for Pods](external-snat.md "external-snat.md")                                                    |
| Restrict network traffic to and from your Pods                                  | [Restrict Pod network traffic with Kubernetes network policies](cni-network-policy-configure.md "cni-network-policy-configure.md") |
| Customize the secondary network interface in nodes                              | [Deploy Pods in alternate subnets with custom networking](cni-custom-network.md "cni-custom-network.md")                           |
| Increase IP addresses for your node                                             | [Assign more IP addresses to Amazon EKS nodes with prefixes](cni-increase-ip-addresses.md "cni-increase-ip-addresses.md")          |
| Use security groups for Pod network traffic                                     | [Assign security groups to individual Pods](security-groups-for-pods.md "security-groups-for-pods.md")                             |
| Use multiple network interfaces for Pods                                        | [Attach multiple network interfaces to Pods](pod-multiple-network-interfaces.md "pod-multiple-network-interfaces.md")              |
