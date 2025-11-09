**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Prerequisite setup for hybrid nodes

To use Amazon EKS Hybrid Nodes, you must have private connectivity from your on-premises environment to/from AWS, bare metal servers or virtual machines with a supported operating system, and AWS IAM Roles Anywhere or AWS Systems Manager (SSM) hybrid activations configured. You are responsible for managing these prerequisites throughout the hybrid nodes lifecycle.

- Hybrid network connectivity from your on-premises environment to/from AWS
- Infrastructure in the form of physical or virtual machines
- Operating system that is compatible with hybrid nodes
- On-premises IAM credentials provider configured

![Hybrid node network connectivity.](images/hybrid-prereq-diagram.png)

## Hybrid network connectivity

The communication between the Amazon EKS control plane and hybrid nodes is routed through the VPC and subnets you pass during cluster creation, which builds on the [existing mechanism](https://aws.github.io/aws-eks-best-practices/networking/subnets/ "https://aws.github.io/aws-eks-best-practices/networking/subnets/") in Amazon EKS for control plane to node networking. There are several [documented options](../../../whitepapers/latest/aws-vpc-connectivity-options/network-to-amazon-vpc-connectivity-options.md "../../../whitepapers/latest/aws-vpc-connectivity-options/network-to-amazon-vpc-connectivity-options.md") available for you to connect your on-premises environment with your VPC including AWS Site-to-Site VPN, AWS Direct Connect, or your own VPN connection. Reference the [AWS Site-to-Site VPN](../../../vpn/latest/s2svpn/VPC_VPN.md "../../../vpn/latest/s2svpn/VPC_VPN.md") and [AWS Direct Connect](../../../directconnect/latest/UserGuide/Welcome.md "../../../directconnect/latest/UserGuide/Welcome.md") user guides for more information on how to use those solutions for your hybrid network connection.

For an optimal experience, we recommend that you have reliable network connectivity of at least 100 Mbps and a maximum of 200ms round trip latency for the hybrid nodes connection to the AWS Region. This is general guidance that accommodates most use cases but is not a strict requirement. The bandwidth and latency requirements can vary depending on the number of hybrid nodes and your workload characteristics, such as application image size, application elasticity, monitoring and logging configurations, and application dependencies on accessing data stored in other AWS services. We recommend that you test with your own applications and environments before deploying to production to validate that your networking setup meets the requirements for your workloads.

## On-premises network configuration

You must enable inbound network access from the Amazon EKS control plane to your on-premises environment to allow the Amazon EKS control plane to communicate with the `kubelet` running on hybrid nodes and optionally with webhooks running on your hybrid nodes. Additionally, you must enable outbound network access for your hybrid nodes and components running on them to communicate with the Amazon EKS control plane. You can configure this communication to stay fully private to your AWS Direct Connect, AWS Site-to-Site VPN, or your own VPN connection.

The Classless Inter-Domain Routing (CIDR) ranges you use for your on-premises node and pod networks must use IPv4 RFC-1918 address ranges. Your on-premises router must be configured with routes to your on-premises nodes and optionally pods. See [On-premises networking configuration](hybrid-nodes-networking.md#hybrid-nodes-networking-on-prem "hybrid-nodes-networking.md#hybrid-nodes-networking-on-prem") for more information on the on-premises network requirements, including the full list of required ports and protocols that must be enabled in your firewall and on-premises environment.

## EKS cluster configuration

To minimize latency, we recommend that you create your Amazon EKS cluster in the AWS Region closest to your on-premises or edge environment. You pass your on-premises node and pod CIDRs during Amazon EKS cluster creation via two API fields: `RemoteNodeNetwork` and `RemotePodNetwork`. You may need to discuss with your on-premises network team to identify your on-premises node and pod CIDRs. The node CIDR is allocated from your on-premises network and the pod CIDR is allocated from the Container Network Interface (CNI) you use if you are using an overlay network for your CNI. Cilium and Calico use overlay networks by default.

The on-premises node and pod CIDRs you configure via the `RemoteNodeNetwork` and `RemotePodNetwork` fields are used to configure the Amazon EKS control plane to route traffic through your VPC to the `kubelet` and the pods running on your hybrid nodes. Your on-premises node and pod CIDRs cannot overlap with each other, the VPC CIDR you pass during cluster creation, or the service IPv4 configuration for your Amazon EKS cluster. Also, Pod CIDRs must be unique to each EKS cluster so that your on-premises router can route traffic.

We recommend that you use either public or private endpoint access for the Amazon EKS Kubernetes API server endpoint. If you choose “Public and Private”, the Amazon EKS Kubernetes API server endpoint will always resolve to the public IPs for hybrid nodes running outside of your VPC, which can prevent your hybrid nodes from joining the cluster. When you use public endpoint access, the Kubernetes API server endpoint is resolved to public IPs and the communication from hybrid nodes to the Amazon EKS control plane will be routed over the internet. When you choose private endpoint access, the Kubernetes API server endpoint is resolved to private IPs and the communication from hybrid nodes to the Amazon EKS control plane will be routed over your private connectivity link, in most cases AWS Direct Connect or AWS Site-to-Site VPN.

## VPC configuration

You must configure the VPC you pass during Amazon EKS cluster creation with routes in its routing table for your on-premises node and optionally pod networks with your virtual private gateway (VGW) or transit gateway (TGW) as the target. An example is shown below. Replace `REMOTE_NODE_CIDR` and `REMOTE_POD_CIDR` with the values for your on-premises network.

| Destination      | Target           | Description                                    |
| ---------------- | ---------------- | ---------------------------------------------- |
| 10.226.0.0/16    | local            | Traffic local to the VPC routes within the VPC |
| REMOTE_NODE_CIDR | tgw-abcdef123456 | On-prem node CIDR, route traffic to the TGW    |
| REMODE_POD_CIDR  | tgw-abcdef123456 | On-prem pod CIDR, route traffic to the TGW     |

## Security group configuration

When you create a cluster, Amazon EKS creates a security group that’s named `eks-cluster-sg-<cluster-name>-<uniqueID>`. You cannot alter the inbound rules of this Cluster Security Group but you can restrict the outbound rules. You must add an additional security group to your cluster to enable the kubelet and optionally webhooks running on your hybrid nodes to contact the Amazon EKS control plane. The required inbound rules for this additional security group are shown below. Replace `REMOTE_NODE_CIDR` and `REMOTE_POD_CIDR` with the values for your on-premises network.

| Name                 | Security group rule ID | IP version | Type  | Protocol | Port range | Source           |
| -------------------- | ---------------------- | ---------- | ----- | -------- | ---------- | ---------------- |
| On-prem node inbound | sgr-abcdef123456       | IPv4       | HTTPS | TCP      | 443        | REMOTE_NODE_CIDR |
| On-prem pod inbound  | sgr-abcdef654321       | IPv4       | HTTPS | TCP      | 443        | REMOTE_POD_CIDR  |

## Infrastructure

You must have bare metal servers or virtual machines available to use as hybrid nodes. Hybrid nodes are agnostic to the underlying infrastructure and support x86 and ARM architectures. Amazon EKS Hybrid Nodes follows a “bring your own infrastructure” approach, where you are responsible for provisioning and managing the bare metal servers or virtual machines that you use for hybrid nodes. While there is not a strict minimum resource requirement, we recommend that you use hosts with at least 1 vCPU and 1GiB RAM for hybrid nodes.

## Operating system

Bottlerocket, Amazon Linux 2023 (AL2023), Ubuntu, and RHEL are validated on an ongoing basis for use as the node operating system for hybrid nodes. Bottlerocket is supported by AWSin VMware vSphere environments only. AL2023 is not covered by AWS Support Plans when run outside of Amazon EC2. AL2023 can only be used in on-premises virtualized environments, see the [Amazon Linux 2023 User Guide](../../../linux/al2023/ug/outside-ec2.md "../../../linux/al2023/ug/outside-ec2.md") for more information. AWS supports the hybrid nodes integration with Ubuntu and RHEL operating systems but does not provide support for the operating system itself.

You are responsible for operating system provisioning and management. When you are testing hybrid nodes for the first time, it is easiest to run the Amazon EKS Hybrid Nodes CLI (`nodeadm`) on an already provisioned host. For production deployments, we recommend that you include `nodeadm` in your golden operating system images with it configured to run as a systemd service to automatically join hosts to Amazon EKS clusters at host startup.

## On-premises IAM credentials provider

Amazon EKS Hybrid Nodes use temporary IAM credentials provisioned by AWS SSM hybrid activations or AWS IAM Roles Anywhere to authenticate with the Amazon EKS cluster. You must use either AWS SSM hybrid activations or AWS IAM Roles Anywhere with the Amazon EKS Hybrid Nodes CLI (`nodeadm`). We recommend that you use AWS SSM hybrid activations if you do not have existing Public Key Infrastructure (PKI) with a Certificate Authority (CA) and certificates for your on-premises environments. If you do have existing PKI and certificates on-premises, use AWS IAM Roles Anywhere.

Similar to the [Amazon EKS node IAM role](create-node-role.md "create-node-role.md") for nodes running on Amazon EC2, you will create a Hybrid Nodes IAM Role with the required permissions to join hybrid nodes to Amazon EKS clusters. If you are using AWS IAM Roles Anywhere, configure a trust policy that allows AWS IAM Roles Anywhere to assume the Hybrid Nodes IAM Role and configure your AWS IAM Roles Anywhere profile with the Hybrid Nodes IAM Role as an assumable role. If you are using AWS SSM, configure a trust policy that allows AWS SSM to assume the Hybrid Nodes IAM Role and create the hybrid activation with the Hybrid Nodes IAM Role. See [Prepare credentials for hybrid nodes](hybrid-nodes-creds.md "hybrid-nodes-creds.md") for how to create the Hybrid Nodes IAM Role with the required permissions.
