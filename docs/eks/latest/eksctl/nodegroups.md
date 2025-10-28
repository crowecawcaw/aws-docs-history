# Nodegroups

This chapter includes information about how you create and configure Nodegroups with Eksctl. Nodegroups are groups of EC2 instances attached to an EKS cluster.

## Topics:

- [Spot instances](spot-instances.md "spot-instances.md")
  - Create and manage EKS clusters with Spot instances using managed node groups
  - Configure Spot instances for unmanaged node groups using the MixedInstancesPolicy
  - Distinguish Spot and On-Demand instances using the `node-lifecycle` Kubernetes label

- [Auto Scaling](autoscaling.md "autoscaling.md")
  - Enable automatic scaling of Kubernetes cluster nodes by creating a cluster or nodegroup with IAM role that allows the use of the cluster autoscaler
  - Configure nodegroup definitions to include necessary tags and annotations for the cluster autoscaler to scale the nodegroup
  - Create separate nodegroups for each availability zone if workloads have zone-specific requirements, such as zone-specific storage or affinity rules

- [EKS managed nodegroups](nodegroup-managed.md "nodegroup-managed.md")
  - Provision and manage EC2 instances (nodes) for Amazon EKS Kubernetes clusters
  - Easily apply bug fixes, security patches, and update nodes to the latest Kubernetes versions

- [EKS Hybrid Nodes](hybrid-nodes.md "hybrid-nodes.md")
  - Enable running on-premises and edge applications on customer-managed infrastructure with the same AWS EKS clusters, features, and tools used in the AWS Cloud
  - Configure networking to connect on-premises networks to an AWS VPC, using options like AWS Site-to-Site VPN or AWS Direct Connect
  - Set up credentials for remote nodes to authenticate with the EKS cluster, using either AWS Systems Manager (SSM) or AWS IAM Roles Anywhere

- [Support for Node Repair Config in EKS Managed Nodegroups](nodegroup-node-repair-config.md "nodegroup-node-repair-config.md")
  - Enabling Node Repair for EKS Managed Nodegroups to automatically monitor and replace or reboot unhealthy worker nodes

- [ARM Support](arm-support.md "arm-support.md")
  - Create an EKS cluster with ARM-based Graviton instances for improved performance and cost-efficiency

- [Taints](nodegroup-taints.md "nodegroup-taints.md")
  - Apply taints to specific node groups in a Kubernetes cluster
  - Control scheduling and eviction of pods based on taint keys, values, and effects

- [Launch Template support for Managed Nodegroups](launch-template-support.md "launch-template-support.md")
  - Launching managed node groups using a provided EC2 Launch Template
  - Upgrading a managed node group to use a different version of a Launch Template
  - Understanding limitations and considerations when using custom AMIs and Launch Templates with managed node groups

- [Work with node groups](general-nodegroups.md "general-nodegroups.md")
  - Enable SSH access to EC2 instances in the node group
  - Scale the number of nodes in a node group up or down

- [Custom subnets](nodegroup-with-custom-subnet.md "nodegroup-with-custom-subnet.md")
  - Extend an existing VPC with a new subnet and add a Nodegroup to that subnet

- [Node bootstrapping](node-bootstrapping.md "node-bootstrapping.md")
  - Understand the new node initialization process (nodeadm) introduced in AmazonLinux2023
  - Learn about the default NodeConfig settings applied by eksctl for self-managed and EKS-managed nodes
  - Customize the node bootstrapping process by providing an overrideBootstrapCommand with a custom NodeConfig

- [Unmanaged nodegroups](nodegroup-unmanaged.md "nodegroup-unmanaged.md")
  - Create or update unmanaged node groups in an EKS cluster
  - Update default Kubernetes add-ons like kube-proxy, aws-node, and CoreDNS

- [GPU Support](gpu-support.md "gpu-support.md")
  - Eksctl supports selecting GPU instance types for nodegroups, enabling the use of GPU-accelerated workloads on EKS clusters.
  - Eksctl automatically installs the NVIDIA Kubernetes device plugin when a GPU-enabled instance type is selected, facilitating the use of GPU resources in the cluster.
  - Users can disable automatic plugin installation and manually install a specific version of the NVIDIA Kubernetes device plugin using the provided commands.

- [Instance Selector](instance-selector.md "instance-selector.md")
  - Automatically generate a list of suitable EC2 instance types based on resource criteria like vCPUs, memory, GPUs, and CPU architecture
  - Create clusters and node groups with the instance types matched by the specified instance selector criteria
  - Perform a dry run to inspect and modify the instance types matched by the instance selector before creating a node group

- [Additional Volume Mappings](nodegroup-additional-volume-mappings.md "nodegroup-additional-volume-mappings.md")
  - Configure additional volume mappings for a managed node group in an EKS cluster
  - Customize volume properties like size, type, encryption, IOPS, and throughput for the additional volumes
  - Attach existing EBS snapshots as additional volumes to the node group

- [Windows Worker Nodes](windows-worker-nodes.md "windows-worker-nodes.md")
  - Add Windows node groups to an existing Linux Kubernetes cluster to enable running Windows workloads
  - Schedule workloads on the appropriate operating system (Windows or Linux) using node selectors based on the `kubernetes.io/os` and `kubernetes.io/arch` labels

- [Custom AMI support](custom-ami-support.md "custom-ami-support.md")
  - Use the `--node-ami` flag to specify a custom AMI for node groups, query AWS for the latest EKS-optimized AMI, or use AWS Systems Manager Parameter Store to find the AMI.
  - Set the `--node-ami-family` flag to specify the operating system family for the node group AMI, such as AmazonLinux2, Ubuntu2204, or WindowsServer2022CoreContainer.
  - For Windows node groups, specify a custom AMI and provide a PowerShell bootstrap script via the `overrideBootstrapCommand`.

- [Custom DNS](nodegroup-customize-dns.md "nodegroup-customize-dns.md")
  - Overwrite the DNS server IP address used for internal and external DNS lookups
