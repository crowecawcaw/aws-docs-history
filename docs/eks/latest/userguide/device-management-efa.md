

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Manage EFA devices on Amazon EKS
<a name="device-management-efa"></a>

 [Elastic Fabric Adapter](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html) (EFA) is a network device for Amazon EC2 instances that enables high-performance inter-node communication and RDMA (Remote Direct Memory Access) for artificial intelligence, machine learning, and High Performance Computing (HPC) workloads. Amazon EKS supports two mechanisms for managing EFA devices in EKS clusters: the *EFA Dynamic Resource Allocation (DRA) driver (DRANET)* and the *EFA device plugin*.

## EFA DRA driver vs. EFA device plugin
<a name="eks-efa-dra-vs-device-plugin"></a>


| Feature | EFA DRA driver | EFA device plugin | 
| --- | --- | --- | 
| Minimum Kubernetes version | 1.34 | All EKS-supported Kubernetes versions | 
| EKS Compute | Karpenter, managed node groups, self-managed nodes | EKS Auto Mode, Karpenter, managed node groups, self-managed nodes | 
| EKS-optimized AMIs | AL2023, Bottlerocket | AL2023, Bottlerocket | 
| Device advertisement | Rich attributes via `ResourceSlice` objects including device type, topology, and PCIe locality | Integer count of `vpc.amazonaws.com/efa` extended resources | 
| GPU-EFA affinity | DRA-native topology-awareness | Automatic topology-awareness (EKS-optimized AL2023 AMIs only) | 
| Neuron-EFA affinity | DRA-native topology-awareness | Automatic topology-awareness (EKS-optimized AL2023 AMIs only) | 
| Device sharing | Multiple Pods can share the same EFA device through shared `ResourceClaim` references | Not supported. Each EFA device is exclusively allocated to one Pod. | 

We recommend using DRA drivers for new deployments with Kubernetes versions 1.34 and later on Karpenter, EKS managed node groups, or self-managed nodes. Karpenter supports DRA with both dynamic and static capacity provisioning as of Karpenter version 1.15, though dynamic provisioning requires enabling Karpenter feature gates. For more information, see [Using DRA with Karpenter](device-management.md#dra-karpenter). DRA is not currently supported with EKS Auto Mode. With the EFA DRA driver, you can configure topology-aware allocation that pairs EFA interfaces with their topologically-local GPUs or Neuron devices, and share devices between Pods.

With EFA, High Performance Computing (HPC) applications using the Message Passing Interface (MPI) and machine learning applications using the NVIDIA Collective Communications Library (NCCL) can scale to thousands of CPUs or GPUs, which gives you the application performance of an on-premises HPC cluster with the elasticity of the AWS Cloud. Using EFA with Pods running on Amazon EKS can reduce the time to complete large-scale distributed training workloads without adding instances to your cluster. For more information about EFA, see [Elastic Fabric Adapter](https://aws.amazon.com/hpc/efa/).

## EFA and EFA-only interfaces
<a name="eks-efa-interfaces"></a>

An *Elastic Fabric Adapter (EFA)* is a network interface that combines the capabilities of an Elastic Network Adapter (ENA) and an OS-bypass interface, powered by the AWS Scalable Reliable Datagram (SRD) protocol. The OS-bypass interface lets applications communicate directly with the hardware for low-latency transport, while the ENA capabilities carry normal IP traffic.

Amazon EC2 offers two interface types for EFA:
+  ** `efa` ** — Provides both the ENA and OS-bypass capabilities on one interface. The interface receives an IP address from your subnet.
+  ** `efa-only` ** — Provides only the OS-bypass capability. The interface does not receive an IP address and communication is limited to interfaces within the same Availability Zone.

 **We recommend `efa-only` interfaces for all interfaces except the primary network interface.** Distributed training and HPC traffic uses the OS-bypass path, not the IP path, so the IP addresses that `efa` interfaces consume go unused. On an instance such as `p5.48xlarge` or `p6-b200.48xlarge` with dozens of network interfaces, those unused addresses can exhaust a subnet’s available IP space. For more information, see [Conserving IP address allocation](#eks-efa-conserve-ip).

Note the following requirements for `efa-only` interfaces:
+ You cannot set network card `0` to `efa-only`, because it is the primary network card and network interface of the instance. Configure network card `0`, device index `0` as `interface` and use `efa-only` for the remaining interfaces.
+ Amazon VPC CNI version `1.18.5` or later is required. For more information about updating the VPC CNI, see [Assign IPs to Pods with the Amazon VPC CNI](managing-vpc-cni.md).
+ You cannot use `eksctl’s `efaEnabled` setting to create nodes with `efa-only` interfaces, because `efaEnabled` configures every interface as type `efa`. Use a `NodeClass`, an `EC2NodeClass`, or a launch template instead, as shown in the examples that follow.

## Choosing an EFA-enabled instance type
<a name="eks-efa-instance-types"></a>

EFA is supported on a specific set of Amazon EC2 instance types. For the full list, see [Supported instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html#efa-instance-types) in the *Amazon EC2 User Guide*. To run machine learning workloads, we recommend an instance type that also has hardware acceleration chips such as NVIDIA GPUs or [AWS Trainium](https://aws.amazon.com/machine-learning/trainium/) chips. For the list of instance types that have both accelerators and EFA, see [Accelerated computing](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html#efa-instance-types) in the *Amazon EC2 User Guide*.

As you compare instance types, consider the number of EFA network cards available alongside the number of accelerator cards, vCPUs, and memory. You can assign up to one EFA per network card, and an EFA counts as a network interface. To see how many EFAs each instance type supports, see the [Network cards](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html#network-cards) list in the *Amazon EC2 User Guide*. For the recommended interface layout to reach maximum network bandwidth on each instance type, see [Maximize network bandwidth for EFA-enabled instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa-acc-inst-types.html) in the *Amazon EC2 User Guide*.

To find which EFA-enabled instance types are available in an AWS Region, and which Availability Zones offer them, run the following commands. Replace {{region-code}} with your AWS Region.

```
aws ec2 describe-instance-types --region [.replaceable]`region-code` \
    --filters Name=network-info.efa-supported,Values=true \
    --query "InstanceTypes[*].[InstanceType]" --output text
```

```
aws ec2 describe-instance-type-offerings --region [.replaceable]`region-code` \
    --location-type availability-zone \
    --filters Name=instance-type,Values=[.replaceable]`p5.48xlarge` \
    --query 'InstanceTypeOfferings[*].Location' --output text
```

An example output is as follows.

```
us-west-2a    us-west-2c    us-west-2b
```

Your VPC must have subnets with available IP addresses in one of the Availability Zones returned. Because `efa-only` interfaces communicate only within an Availability Zone, place the nodes of a single distributed job in one Availability Zone.

**Important**  
EFA requires hugepages. Amazon EC2 instances with the EFA driver installed pre-allocate 5128 pages of 2 MiB, which you request as `hugepages-2Mi` resources in your workload specifications. The examples in this topic request hugepages alongside EFA devices. For more information about configuring hugepages on EKS nodes, see [Configure hugepages in Amazon EKS clusters](ml-hugepages.md), and for the Kubernetes resource model, see [Manage HugePages](https://kubernetes.io/docs/tasks/manage-hugepages/scheduling-hugepages/) in the Kubernetes documentation.

## Creating EKS nodes with EFA interfaces
<a name="eks-efa-nodes"></a>

When you create EKS nodes with EFA interfaces, the EFA interfaces are attached to the instance during instance provisioning. You can customize the per-device EFA configuration and use [placement groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html) with EKS Auto Mode, Karpenter, EKS managed node groups, or EKS self-managed node groups. With EKS Auto Mode, you pass configuration for each network interface through the `NodeClass` under `advancedNetworking.networkInterfaces`. With Karpenter, you pass configuration for each network interface via the `EC2NodeClass`. With EKS managed node groups or self-managed nodes, you pass configuration for each network interface with [launch templates](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html).

When using [`eksctl`](install-kubectl.md#eksctl-install-update) for provisioning EKS nodes with the `efaEnabled` setting, all interfaces are configured with interface type `EFA`, an EFA-specific security group is created, and the EFA device plugin is installed on the cluster. If you need to customize the per-device EFA configuration when using `eksctl`, it is recommended to use `eksctl’s support for [launch templates](https://docs.aws.amazon.com/eks/latest/eksctl/launch-template-support.html).

The following examples show how to configure `NodeClass` and launch templates with EFA interfaces. This is useful to customize the interfaces used for EFA vs standard IP-based traffic. For information on the number of EFA interfaces supported by each instance type and how to configure them for maximum network bandwidth, see [Maximize network bandwidth for EFA-enabled instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa-acc-inst-types.html) in the *Amazon EC2 User Guide*.

## EKS Auto Mode
<a name="eks-efa-auto-mode"></a>

In EKS Auto Mode, you configure EFA network interfaces using the `advancedNetworking.networkInterfaces` field in the `NodeClass` (`eks.amazonaws.com/v1`). Each entry specifies a `networkCardIndex`, `deviceIndex`, and `interfaceType`. The `interfaceType` can be `interface` for standard network interfaces or `efa-only` for EFA interfaces dedicated to RDMA traffic without IP addresses assigned.

When `networkInterfaces` is configured, instances launched by the `NodePool` referencing the `NodeClass` use this configuration regardless of whether Pods request `vpc.amazonaws.com/efa` resources. EKS Auto Mode does not attach additional IPs, prefixes, or ENIs after instance launch for nodes with static network interface configuration — only the interfaces and IPs configured at launch are available to Pods.

This feature can be used with [static capacity node pools](auto-static-capacity.md) to maintain pre-warmed, EFA-ready nodes for distributed training and inference workloads.

### Example EKS Auto Mode NodeClass with EFA-only interfaces for P5
<a name="eks-efa-auto-mode-example"></a>

```
apiVersion: eks.amazonaws.com/v1
kind: NodeClass
metadata:
  name: efa-node-class
spec:
  role: MyNodeRole
  subnetSelectorTerms:
    - tags:
        Name: "private-subnet"
  securityGroupSelectorTerms:
    - tags:
        Name: "efa-security-group"
  placementGroupSelector:
    name: "ml-training-pg"
  advancedNetworking:
    networkInterfaces:
    - deviceIndex: 0
      interfaceType: interface
      networkCardIndex: 0
      secondaryIPv4PrefixCount: 1
    - networkCardIndex: 0
      deviceIndex: 1
      interfaceType: efa-only
    - networkCardIndex: 1
      deviceIndex: 0
      interfaceType: efa-only
    - networkCardIndex: 2
      deviceIndex: 0
      interfaceType: efa-only
    - networkCardIndex: 3
      deviceIndex: 0
      interfaceType: efa-only
```

For the full list of constraints on static network interface configuration, see [Static Network Interface Configuration](create-node-class.md#static-network-interfaces) in the NodeClass documentation.

## Karpenter
<a name="eks-efa-auto-karpenter"></a>

Each entry in `networkInterfaces` specifies a `networkCardIndex`, `deviceIndex`, and `interfaceType`. The `interfaceType` can be `interface` for standard network interfaces or `efa-only` for EFA interfaces that are dedicated to RDMA traffic and do not have IP addresses assigned. When `networkInterfaces` is configured, instances launched by the `NodePool` referencing the `NodeClass` use this configuration regardless of whether Pods request `vpc.amazonaws.com/efa` resources.

When using Karpenter without specifying `networkInterfaces` in your `NodeClass`, instances created for Pods requesting `vpc.amazonaws.com/efa` have all interfaces configured with interface type `EFA`.

The `networkInterfaces` configuration for `EC2NodeClass` was added in Karpenter v1.11. The following example shows an `EC2NodeClass` configured for a P6-B200 instance with 1 ENA interface and 8 EFA-only interfaces.

**Important**  
Do not combine `spec.networkInterfaces` with Karpenter dynamic capacity provisioning for EFA DRA workloads. Karpenter does not support that combination and the result is undefined behavior. If you use the EFA DRA driver and need a custom interface layout such as the `efa-only` configuration below, use Karpenter static capacity provisioning, EKS managed node groups, or self-managed nodes. For more information, see [Using DRA with Karpenter](device-management.md#dra-karpenter).

### Example Karpenter EC2NodeClass with EFA-only interfaces for P6-B200
<a name="eks-efa-karpenter-example"></a>

```
apiVersion: karpenter.k8s.aws/v1
kind: EC2NodeClass
metadata:
  name: efa-node-class
spec:
  networkInterfaces:
  - networkCardIndex: 0
    deviceIndex: 0
    interfaceType: interface
  - networkCardIndex: 0
    deviceIndex: 1
    interfaceType: efa-only
  - networkCardIndex: 1
    deviceIndex: 0
    interfaceType: efa-only
  - networkCardIndex: 2
    deviceIndex: 0
    interfaceType: efa-only
  - networkCardIndex: 3
    deviceIndex: 0
    interfaceType: efa-only
  - networkCardIndex: 4
    deviceIndex: 0
    interfaceType: efa-only
  - networkCardIndex: 5
    deviceIndex: 0
    interfaceType: efa-only
  - networkCardIndex: 6
    deviceIndex: 0
    interfaceType: efa-only
  - networkCardIndex: 7
    deviceIndex: 0
    interfaceType: efa-only
```

## EKS managed node groups and self-managed nodes
<a name="eks-efa-mng-self-managed"></a>

With EKS managed node groups or self-managed nodes, you pass configuration for each network interface with [launch templates](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html).

The following example shows a launch template configured for a P6-B200 instance with 1 ENA interface and 8 EFA-only interfaces. The primary network interface (network card 0, device index 0) uses a standard `interface` type for IP traffic, while additional interfaces use `efa-only` for dedicated RDMA traffic. Adjust the number of `efa-only` interfaces based on your instance type. For the number of EFA interfaces supported by each instance type, see [Maximize network bandwidth for EFA-enabled instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa-acc-inst-types.html) in the *Amazon EC2 User Guide*.

### Example launch template with EFA-only interfaces for P6-B200
<a name="eks-efa-launch-template-example"></a>

Replace ` security-group-id ` with your values. The security group must allow all inbound and outbound traffic to and from itself to enable EFA OS-bypass functionality. For more information, see [Step 1: Prepare an EFA-enabled security group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa-start.html#efa-start-security) in the *Amazon EC2 User Guide*.

**Important**  
Do not specify `SubnetId` in the launch template when using EKS managed node groups. EKS requires that all subnets are specified through the `CreateNodegroup` API and rejects launch templates that include subnet configuration.

```
{
  "LaunchTemplateName": "efa-launch-template",
  "LaunchTemplateData": {
    "InstanceType": "p6-b200.48xlarge",
    "NetworkInterfaces": [
      {
        "NetworkCardIndex": 0,
        "DeviceIndex": 0,
        "InterfaceType": "interface",
        "Groups": ["security-group-id"]
      },
      {
        "NetworkCardIndex": 0,
        "DeviceIndex": 1,
        "InterfaceType": "efa-only",
        "Groups": ["security-group-id"]
      },
      {
        "NetworkCardIndex": 1,
        "DeviceIndex": 0,
        "InterfaceType": "efa-only",
        "Groups": ["security-group-id"]
      },
      {
        "NetworkCardIndex": 2,
        "DeviceIndex": 0,
        "InterfaceType": "efa-only",
        "Groups": ["security-group-id"]
      },
      {
        "NetworkCardIndex": 3,
        "DeviceIndex": 0,
        "InterfaceType": "efa-only",
        "Groups": ["security-group-id"]
      },
      {
        "NetworkCardIndex": 4,
        "DeviceIndex": 0,
        "InterfaceType": "efa-only",
        "Groups": ["security-group-id"]
      },
      {
        "NetworkCardIndex": 5,
        "DeviceIndex": 0,
        "InterfaceType": "efa-only",
        "Groups": ["security-group-id"]
      },
      {
        "NetworkCardIndex": 6,
        "DeviceIndex": 0,
        "InterfaceType": "efa-only",
        "Groups": ["security-group-id"]
      },
      {
        "NetworkCardIndex": 7,
        "DeviceIndex": 0,
        "InterfaceType": "efa-only",
        "Groups": ["security-group-id"]
      }
    ]
  }
}
```

## Using EKS-optimized AMIs with EFA
<a name="eks-amis-efa"></a>

The EKS-optimized AL2023 AMIs and all Bottlerocket AMIs include the host-level components required to use EFA, specifically the components installed by the [aws-efa-installer](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa-start.html#efa-start-enable). The EKS AL2023 and Bottlerocket AMIs **do not include** the EFA DRA driver or EFA device plugin, and these must be installed separately on your cluster before deploying workloads.

## Conserving IP address allocation
<a name="eks-efa-conserve-ip"></a>

EFA-enabled instances such as `p5.48xlarge` and `p6-b200.48xlarge` support many network interfaces. By default, the Amazon VPC CNI allocates IP addresses across all IP-enabled attached ENIs, which can consume a large number of IP addresses from your subnet even when those addresses are not actively used by Pods. On instances with dozens of network interfaces, this can quickly exhaust your subnet’s available IP space.

To reduce IP address consumption on EFA-enabled nodes, configure your network interfaces to use `efa-only` for all interfaces except the primary. EFA-only interfaces are dedicated to RDMA traffic and do not have IP addresses assigned, so they do not consume addresses from your subnet. For example configurations, see [Karpenter](#eks-efa-auto-karpenter) and [EKS managed node groups and self-managed nodes](#eks-efa-mng-self-managed). For the recommended interface layout for each instance type, see [Maximize network bandwidth for EFA-enabled instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa-acc-inst-types.html) in the *Amazon EC2 User Guide*.

In addition to using `efa-only` interfaces, you can configure the Amazon VPC CNI to limit the number of warm (pre-allocated) IP addresses and ENIs. By default, the VPC CNI pre-allocates a warm pool of ENIs and IP addresses for faster Pod startup, but on large instances this can reserve hundreds of unused IP addresses. Set the `WARM_IP_TARGET` and `WARM_ENI_TARGET` environment variables on the `aws-node` DaemonSet to control how many spare IP addresses and ENIs the CNI maintains. For more information on these settings, see [Amazon VPC CNI best practices](https://docs.aws.amazon.com/eks/latest/best-practices/vpc-cni.html#_overview).

**Note**  
The `WARM_ENI_TARGET` and `WARM_IP_TARGET` settings are cluster-wide and apply to all nodes managed by the VPC CNI. There is currently no way to set different values for each node group or instance type. If you need more granular control of these settings, provide feedback on [containers-roadmap issue \#1834](https://github.com/aws/containers-roadmap/issues/1834) on GitHub.

## Install the EFA DRA driver (DRANET)
<a name="efa-dra-driver"></a>

The EFA DRA driver is built in the upstream [DRANET](https://github.com/kubernetes-sigs/dranet) project on GitHub, which provides cloud-aware network device management for Kubernetes DRA. *EFA DRA driver* and *DRANET* are used interchangeably throughout this documentation and refer to the same tool.

The EFA DRA driver advertises EFA devices as `ResourceSlice` objects with the driver name `dra.net` and the `DeviceClass` name `efa.networking.k8s.aws`. The EFA DRA driver runs as a DaemonSet on each node and automatically discovers EFA devices.

### Prerequisites
<a name="_prerequisites"></a>
+ An Amazon EKS cluster running Kubernetes version 1.34 or later with static capacity provisioned by Karpenter, EKS managed node groups, or self-managed node groups.
+ Nodes with EFA-enabled Amazon EC2 instance types. For a list of supported instance types, see [Supported instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html#efa-instance-types) in the *Amazon EC2 User Guide*.
+ Nodes with host-level components installed for EFA, see [Install the EFA software](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa-start.html#efa-start-enable) for more information. The EKS-optimized AL2023 NVIDIA and Neuron AMIs, and the Bottlerocket AMIs include the EFA host-level components.
+ Helm installed in your command-line environment, see the [Setup Helm instructions](helm.md) for more information.
+  `kubectl` configured to communicate with your cluster, see [Install or update `kubectl`](install-kubectl.md#kubectl-install-update) for more information.

### Procedure
<a name="_procedure"></a>

**Important**  
Do not install the EFA DRA driver on nodes where the EFA device plugin is running. The two mechanisms cannot coexist on the same node. Doing so can cause silent oversubscription of the underlying devices to multiple pods on the same node.

1. Add the EKS Helm chart repository.

   ```
   helm repo add eks https://aws.github.io/eks-charts
   ```

1. Update your local Helm repository.

   ```
   helm repo update
   ```

1. Install the EFA DRA driver on your cluster using Helm. The EFA DRA driver automatically detects that it is running on EC2 instances via the Instance Metadata Service (IMDS) and enables EFA device discovery. The EFA DRA driver is deployed as a DaemonSet in the `kube-system` namespace by default. See the Helm values.yaml in the [EKS Helm chart repository](https://github.com/aws/eks-charts/tree/master/stable/aws-dranet) on GitHub for the configurable parameters.

   ```
   helm install aws-dranet eks/aws-dranet --namespace kube-system
   ```

1. Verify that the DRANET DaemonSet is running.

   ```
   kubectl get daemonset -n kube-system aws-dranet
   ```

   ```
   NAME          DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR   AGE
   aws-dranet    2         2         2       2            2           <none>          60s
   ```

1. Verify that the `DeviceClass` was created.

   ```
   kubectl get deviceclass
   ```

   ```
   NAME                    AGE
   efa.networking.k8s.aws  60s
   ```

1. Verify that `ResourceSlice` objects are advertised for your nodes.

   ```
   kubectl get resourceslices --field-selector spec.driver=dra.net
   ```

   If you experience errors with the steps above, you can check the logs for DRANET with the following command.

   ```
   kubectl logs -n kube-system -l app=aws-dranet
   ```

1. To request EFA devices using the DRA driver, create a `ResourceClaim` or `ResourceClaimTemplate` that references the EFA `DeviceClass` and reference it in your Pod specification. The following example requests a single EFA device.

   ```
   apiVersion: resource.k8s.io/v1
   kind: ResourceClaimTemplate
   metadata:
     name: single-efa-claim
   spec:
     spec:
       devices:
         requests:
         - name: efa
           exactly:
             deviceClassName: efa.networking.k8s.aws
             count: 1
   ---
   apiVersion: v1
   kind: Pod
   metadata:
     name: efa-workload
   spec:
     containers:
     - name: app
       ...
       resources:
         claims:
         - name: efa-device
     resourceClaims:
     - name: efa-device
       resourceClaimTemplateName: single-efa-claim
   ```

## Topology-aware EFA and GPU/Neuron device allocation
<a name="efa-dra-topology-aware"></a>

The EFA DRA driver supports topology-aware allocation that pairs EFA interfaces with GPUs or Neuron devices on the same PCIe root. Use the `matchAttribute` constraint to align EFA and GPU or Neuron device allocations. To use this capability, you must also use the NVIDIA or Neuron DRA drivers. For more information, see [Manage NVIDIA GPUs on Amazon EKS](device-management-nvidia.md) and [Manage Neuron devices on Amazon EKS](device-management-neuron.md).

The following example requests 1 EFA interface aligned with 1 NVIDIA GPU:

```
apiVersion: resource.k8s.io/v1
kind: ResourceClaimTemplate
metadata:
  name: aligned-efa-nvidia
spec:
  spec:
    devices:
      requests:
      - name: 1-efa
        exactly:
          deviceClassName: efa.networking.k8s.aws
          count: 1
      - name: 1-gpu
        exactly:
          deviceClassName: gpu.nvidia.com
          count: 1
      constraints:
      - requests: ["1-gpu", "1-efa"]
        matchAttribute: "resource.kubernetes.io/pcieRoot"
```

The following example requests 4 EFA interfaces aligned with 4 Neuron devices:

```
apiVersion: resource.k8s.io/v1
kind: ResourceClaimTemplate
metadata:
  name: aligned-efa-neuron
spec:
  spec:
    devices:
      requests:
      - name: 4-neurons
        exactly:
          deviceClassName: neuron.aws.com
          count: 4
      - name: 4-efas
        exactly:
          deviceClassName: efa.networking.k8s.aws
          count: 4
      constraints:
      - requests: ["4-neurons", "4-efas"]
        matchAttribute: "resource.aws.com/devicegroup4_id"
```

The number in the `devicegroup` attribute name corresponds to the number of Neuron devices in the connected topology group. For example, `resource.aws.com/devicegroup1_id` identifies a single Neuron device, `resource.aws.com/devicegroup4_id` identifies a group of 4 connected devices, and `resource.aws.com/devicegroup8_id` and `resource.aws.com/devicegroup16_id` identify groups of 8 and 16 connected devices respectively. Choose the `matchAttribute` that matches the device `count` in your request so that the allocated Neuron devices and EFA interfaces belong to the same connected topology group. For more information on these attributes, see the [Neuron DRA driver documentation](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/containers/neuron-dra.html).

You can use `allocationMode` to simplify how EFA devices are allocated to aligned GPU or Neuron accelerators. The `allocationMode` field supports two values: `ExactCount` (the default) requests a specific number of devices specified by `count`, and `All` requests all matching devices in a pool. For example, on `p5.48xlarge` instances there are four EFA devices that share the same PCIe root with one GPU. To allocate these groups of EFA devices with aligned GPUs, even if you do not know the exact EFA-GPU device mapping and count of aligned EFA devices, you can configure your `ResourceClaimTemplate` with `allocationMode: All` for the EFA devices.

```
apiVersion: resource.k8s.io/v1
kind: ResourceClaimTemplate
metadata:
  name: aligned-all-efa-one-nvidia
spec:
  spec:
    devices:
      requests:
      - name: all-efas
        exactly:
          deviceClassName: efa.networking.k8s.aws
          allocationMode: All
      - name: one-gpu
        exactly:
          deviceClassName: gpu.nvidia.com
          allocationMode: ExactCount
          count: 1
      constraints:
      - requests: ["all-efas", "one-gpu"]
        matchAttribute: "resource.kubernetes.io/pcieRoot"
```

## Share EFA devices between multiple Pods
<a name="efa-dra-share"></a>

The EFA DRA driver supports sharing EFA devices between multiple Pods by using a `ResourceClaim`. Unlike a `ResourceClaimTemplate`, which generates a separate claim for each Pod, a `ResourceClaim` is a named object that you create independently and reference from multiple Pods. All Pods that reference the same `ResourceClaim` share access to the same allocated EFA devices and are scheduled to the same node where those devices are available.

To share EFA devices between Pods, create a `ResourceClaim` that requests the EFA devices, then reference that claim by name in each Pod’s `resourceClaims` field using `resourceClaimName`. The `ResourceClaim` must exist in the cluster before the Pods that reference it are created. If a referenced `ResourceClaim` does not exist, the Pods remain in a pending state until the claim is created.

The following example creates a `ResourceClaim` that requests 4 EFA devices, and two Pods that share access to those devices.

1. Create the `ResourceClaim`.

   ```
   apiVersion: resource.k8s.io/v1
   kind: ResourceClaim
   metadata:
     name: shared-efa
   spec:
     devices:
       requests:
       - name: efa
         exactly:
           deviceClassName: efa.networking.k8s.aws
           count: 4
   ```

1. Reference the `ResourceClaim` by name in each Pod that needs access to the EFA devices. Each Pod uses `resourceClaimName` to reference the existing claim instead of `resourceClaimTemplateName`.

   ```
   apiVersion: v1
   kind: Pod
   metadata:
     name: training-worker
   spec:
     containers:
     - name: worker
       image: my-training-image
       resources:
         claims:
         - name: efa-devices
     resourceClaims:
     - name: efa-devices
       resourceClaimName: shared-efa
   ---
   apiVersion: v1
   kind: Pod
   metadata:
     name: training-monitor
   spec:
     containers:
     - name: monitor
       image: my-monitor-image
       resources:
         claims:
         - name: efa-devices
     resourceClaims:
     - name: efa-devices
       resourceClaimName: shared-efa
   ```

Both Pods reference the same `shared-efa` `ResourceClaim` and are scheduled to the node where those EFA devices are allocated. The `ResourceClaim` lifecycle is independent of the Pods — it persists until you delete it, even if all Pods referencing it are removed.

## Install the EFA Kubernetes device plugin
<a name="eks-efa-device-plugin"></a>

The EFA Kubernetes device plugin advertises EFA devices as `vpc.amazonaws.com/efa` extended resources. You request EFA devices in container resource requests and limits.

**Important**  
Topology-aligned allocation of NVIDIA GPUs or Neuron devices with EFA interfaces happens automatically when using the EKS-optimized AL2023 accelerated AMIs. This automatic alignment does not occur when using Bottlerocket EKS-optimized AMIs or custom AMIs. If you need topology-aligned accelerator and EFA device allocation with Bottlerocket or custom AMIs, use the EFA DRA driver and the corresponding Neuron DRA driver. To use the NVIDIA DRA driver on Bottlerocket, you must first disable the NVIDIA device plugin that is bundled with the Bottlerocket NVIDIA variants, which requires Bottlerocket version 1.63.0 or later. For more information, see [Topology-aware EFA and GPU/Neuron device allocation](#efa-dra-topology-aware) and [Install the NVIDIA DRA driver](device-management-nvidia-dra-device-plugin.md#eks-nvidia-dra-driver).

**Important**  
Starting with NVIDIA `k8s-device-plugin` v0.19.0, the `--mofed-enabled` flag defaults to `true`, which causes the NVIDIA device plugin to mount all `/dev/infiniband/uverbs*` devices into containers requesting GPUs. This conflicts with the EFA device plugin, which should be the component managing EFA device allocation at `/dev/infiniband`. If you are using EKS managed node groups or self-managed nodes with the NVIDIA device plugin, you must explicitly disable MOFED. For instructions, see [Install the NVIDIA Kubernetes device plugin](device-management-nvidia-dra-device-plugin.md#eks-nvidia-device-plugin).  
EKS Auto Mode does not enable MOFED by default and is not affected by this issue.

### Prerequisites
<a name="_prerequisites_2"></a>
+ An Amazon EKS cluster.
+ Nodes with EFA-enabled Amazon EC2 instance types. For a list of supported instance types, see [Supported instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html#efa-instance-types) in the *Amazon EC2 User Guide*.
+ Nodes with host-level components installed for EFA, see [Install the EFA software](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa-start.html#efa-start-enable) for more information. The EKS-optimized AL2023 AMIs and the Bottlerocket AMIs include the EFA host-level components.
+ Helm installed in your command-line environment, see the [Setup Helm instructions](helm.md) for more information.
+  `kubectl` configured to communicate with your cluster, see [Install or update `kubectl`](install-kubectl.md#kubectl-install-update) for more information.

### Procedure
<a name="_procedure_2"></a>

1. Add the EKS Helm chart repository.

   ```
   helm repo add eks https://aws.github.io/eks-charts
   ```

1. Update your local Helm repository.

   ```
   helm repo update
   ```

1. Install the EFA device plugin.

   ```
   helm install efa eks/aws-efa-k8s-device-plugin -n kube-system
   ```

1. Verify the EFA device plugin DaemonSet is running.

   ```
   kubectl get daemonset -n kube-system efa-aws-efa-k8s-device-plugin
   ```

   ```
   NAME                                  DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR   AGE
   efa-aws-efa-k8s-device-plugin         2         2         2       2            2           <none>          60s
   ```

1. Verify that your nodes have allocatable EFA resources.

   ```
   kubectl get nodes "-o=custom-columns=NAME:.metadata.name,EFA:.status.allocatable.vpc\.amazonaws\.com/efa"
   ```

   ```
   NAME                                           EFA
   ip-192-168-11-225.us-west-2.compute.internal   4
   ip-192-168-24-96.us-west-2.compute.internal    4
   ```

1. To request EFA devices using the device plugin, specify the `vpc.amazonaws.com/efa` resource in your container resource requests and limits.

   ```
   apiVersion: v1
   kind: Pod
   metadata:
     name: efa-workload
   spec:
     containers:
     - name: app
       ...
       resources:
         limits:
           vpc.amazonaws.com/efa: 4
           hugepages-2Mi: ...
         requests:
           vpc.amazonaws.com/efa: 4
           hugepages-2Mi: ...
   ```

## Test EFA performance with NCCL tests
<a name="eks-efa-nccl-test"></a>

After you install either the EFA DRA driver or the EFA device plugin, we recommend validating the setup before you run production workloads. The [NCCL tests](https://github.com/NVIDIA/nccl-tests) measure collective-communication performance across nodes and confirm that GPUDirect RDMA over EFA is working. You can also find packaged versions of these tests in the [awsome-distributed-training](https://github.com/aws-samples/awsome-distributed-training/tree/main/micro-benchmarks/nccl-tests) repository on GitHub.

The following procedure runs a two-node `all_reduce_perf` benchmark on `p5.48xlarge` instances. Each worker requests all eight GPUs, all EFA devices, and `hugepages-2Mi` on its node, so each worker consumes an entire instance. Adjust the instance type, GPU count, EFA count, and hugepages request to match your nodes.

### Prerequisites
<a name="_prerequisites_3"></a>
+ Two or more nodes with an EFA-enabled, GPU-accelerated instance type, in the same Availability Zone. For more information, see [Choosing an EFA-enabled instance type](#eks-efa-instance-types).
+ Either the EFA DRA driver or the EFA device plugin installed. For more information, see [Install the EFA DRA driver (DRANET)](#efa-dra-driver) or [Install the EFA Kubernetes device plugin](#eks-efa-device-plugin).
+ NVIDIA GPUs exposed to Pods, through either the NVIDIA DRA driver or the NVIDIA device plugin. For more information, see [Manage NVIDIA GPUs on Amazon EKS](device-management-nvidia.md). Use the same mechanism for GPUs that you use for EFA: DRA claims for both, or device plugin resources for both.

### Step 1: Deploy the Kubeflow MPI Operator
<a name="_step_1_deploy_the_kubeflow_mpi_operator"></a>

The NCCL tests use MPI to launch ranks across nodes. The Kubeflow MPI Operator runs Allreduce-style distributed jobs on Kubernetes through the `MPIJob` custom resource. For installation instructions, see [MPI Operator](https://github.com/kubeflow/mpi-operator) on GitHub.

### Step 2: Create the MPIJob manifest
<a name="_step_2_create_the_mpijob_manifest"></a>

Use the manifest that matches how you expose EFA and GPU devices. Copy it to a file named `nccl-tests.yaml`.

#### Using the EFA device plugin
<a name="_using_the_efa_device_plugin"></a>

With the device plugin, the worker requests `vpc.amazonaws.com/efa` and `nvidia.com/gpu` as extended resources.

##### MPIJob using the EFA device plugin
<a name="eks-efa-nccl-device-plugin-yaml"></a>

```
apiVersion: kubeflow.org/v2beta1
kind: MPIJob
metadata:
  name: nccl-tests
spec:
  runPolicy:
    cleanPodPolicy: Running
    backoffLimit: 20
  slotsPerWorker: 8
  mpiReplicaSpecs:
    Launcher:
      replicas: 1
      template:
         spec:
          restartPolicy: OnFailure
          containers:
          - image: public.ecr.aws/hpc-cloud/nccl-tests:latest
            imagePullPolicy: IfNotPresent
            name: test-nccl-launcher
            env:
             - name: PATH
               value: $PATH:/opt/amazon/efa/bin:/usr/bin
            command:
            - /opt/amazon/openmpi/bin/mpirun
            - --allow-run-as-root
            - --tag-output
            - -np
            - "16"
            - -N
            - "8"
            - --bind-to
            - none
            - -x
            - PATH
            - -x
            - LD_LIBRARY_PATH
            - -x
            - NCCL_DEBUG=INFO
            - -x
            - NCCL_BUFFSIZE=8388608
            - -x
            - NCCL_P2P_NET_CHUNKSIZE=524288
            - -x
            - NCCL_TUNER_PLUGIN=/opt/amazon/ofi-nccl/lib/x86_64-linux-gnu/libnccl-ofi-tuner.so
            - --mca
            - pml
            - ^cm,ucx
            - --mca
            - btl
            - tcp,self
            - --mca
            - btl_tcp_if_exclude
            - lo,docker0,veth_def_agent
            - /opt/nccl-tests/build/all_reduce_perf
            - -b
            - "8"
            - -e
            - "16G"
            - -f
            - "2"
            - -g
            - "1"
            - -c
            - "1"
            - -n
            - "100"
    Worker:
      replicas: 2
      template:
        spec:
          nodeSelector:
            node.kubernetes.io/instance-type: "p5.48xlarge"
          containers:
          - image: public.ecr.aws/hpc-cloud/nccl-tests:latest
            imagePullPolicy: IfNotPresent
            name: nccl-tests-worker
            volumeMounts:
            - name: shmem
              mountPath: /dev/shm
            resources:
              limits:
                nvidia.com/gpu: 8
                hugepages-2Mi: 5120Mi
                vpc.amazonaws.com/efa: 32
                memory: 32000Mi
              requests:
                nvidia.com/gpu: 8
                hugepages-2Mi: 5120Mi
                vpc.amazonaws.com/efa: 32
                memory: 32000Mi
          volumes:
          - name: shmem
            hostPath:
              path: /dev/shm
```

The `vpc.amazonaws.com/efa: 32` request claims all EFA devices on a `p5.48xlarge`. On the EKS-optimized AL2023 accelerated AMIs, the device plugin aligns the allocated EFA devices with their topologically-local GPUs automatically.

#### Using the EFA DRA driver
<a name="_using_the_efa_dra_driver"></a>

With DRA, the worker references a `ResourceClaimTemplate` instead of requesting extended resources. Because each worker in this test consumes a whole node, the template requests every EFA device and every GPU with `allocationMode: All` and omits a topology constraint — there is nothing to align when a single Pod receives all devices on the node. For a job whose Pods take only part of a node, add a `matchAttribute` constraint so that each Pod’s EFA devices and GPUs share a PCIe root. For more information, see [Topology-aware EFA and GPU/Neuron device allocation](#efa-dra-topology-aware).

##### MPIJob using the EFA DRA driver
<a name="eks-efa-nccl-dra-yaml"></a>

```
apiVersion: resource.k8s.io/v1
kind: ResourceClaimTemplate
metadata:
  name: nccl-efa-gpus
spec:
  spec:
    devices:
      requests:
      - name: all-efas
        exactly:
          deviceClassName: efa.networking.k8s.aws
          allocationMode: All
      - name: all-gpus
        exactly:
          deviceClassName: gpu.nvidia.com
          allocationMode: All
---
apiVersion: kubeflow.org/v2beta1
kind: MPIJob
metadata:
  name: nccl-tests
spec:
  runPolicy:
    cleanPodPolicy: Running
    backoffLimit: 20
  slotsPerWorker: 8
  mpiReplicaSpecs:
    Launcher:
      replicas: 1
      template:
         spec:
          restartPolicy: OnFailure
          containers:
          - image: public.ecr.aws/hpc-cloud/nccl-tests:latest
            imagePullPolicy: IfNotPresent
            name: test-nccl-launcher
            env:
             - name: PATH
               value: $PATH:/opt/amazon/efa/bin:/usr/bin
            command:
            - /opt/amazon/openmpi/bin/mpirun
            - --allow-run-as-root
            - --tag-output
            - -np
            - "16"
            - -N
            - "8"
            - --bind-to
            - none
            - -x
            - PATH
            - -x
            - LD_LIBRARY_PATH
            - -x
            - NCCL_DEBUG=INFO
            - -x
            - NCCL_BUFFSIZE=8388608
            - -x
            - NCCL_P2P_NET_CHUNKSIZE=524288
            - -x
            - NCCL_TUNER_PLUGIN=/opt/amazon/ofi-nccl/lib/x86_64-linux-gnu/libnccl-ofi-tuner.so
            - --mca
            - pml
            - ^cm,ucx
            - --mca
            - btl
            - tcp,self
            - --mca
            - btl_tcp_if_exclude
            - lo,docker0,veth_def_agent
            - /opt/nccl-tests/build/all_reduce_perf
            - -b
            - "8"
            - -e
            - "16G"
            - -f
            - "2"
            - -g
            - "1"
            - -c
            - "1"
            - -n
            - "100"
    Worker:
      replicas: 2
      template:
        spec:
          nodeSelector:
            node.kubernetes.io/instance-type: "p5.48xlarge"
          containers:
          - image: public.ecr.aws/hpc-cloud/nccl-tests:latest
            imagePullPolicy: IfNotPresent
            name: nccl-tests-worker
            volumeMounts:
            - name: shmem
              mountPath: /dev/shm
            resources:
              claims:
              - name: efa-gpus
              limits:
                hugepages-2Mi: 5120Mi
                memory: 32000Mi
              requests:
                hugepages-2Mi: 5120Mi
                memory: 32000Mi
          resourceClaims:
          - name: efa-gpus
            resourceClaimTemplateName: nccl-efa-gpus
          volumes:
          - name: shmem
            hostPath:
              path: /dev/shm
```

Hugepages remain an extended resource under DRA, so the worker still requests `hugepages-2Mi` directly. Only the EFA and GPU devices move to the `ResourceClaimTemplate`.

### Step 3: Run the test and read the results
<a name="_step_3_run_the_test_and_read_the_results"></a>

1. Apply the manifest. This schedules the job onto two EFA-enabled nodes.

   ```
   kubectl apply -f nccl-tests.yaml
   ```

   An example output is as follows.

   ```
   mpijob.kubeflow.org/nccl-tests created
   ```

1. Verify that the job started its Pods.

   ```
   kubectl get pods
   ```

   An example output is as follows.

   ```
   NAME                          READY   STATUS     RESTARTS   AGE
   nccl-tests-launcher-nbql9     0/1     Init:0/1   0          2m49s
   nccl-tests-worker-0           1/1     Running    0          2m49s
   nccl-tests-worker-1           1/1     Running    0          2m49s
   ```

   The MPI Operator creates one launcher Pod and one worker Pod per node.

1. Follow the launcher log to watch the benchmark. Replace {{nbql9}} with the suffix from your output.

   ```
   kubectl logs -f nccl-tests-launcher-[.replaceable]`nbql9`
   ```

   The `all_reduce_perf` output reports bus bandwidth for each message size. Confirm that bandwidth scales as the message size grows and that the `NCCL_DEBUG=INFO` output shows the `ofi` (libfabric) transport rather than a TCP fallback, which indicates NCCL is using EFA. If the test completes successfully, your cluster is ready for distributed training workloads that use NCCL.