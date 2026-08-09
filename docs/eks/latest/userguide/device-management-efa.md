**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Manage EFA devices on Amazon EKS

[Elastic Fabric Adapter](../../../AWSEC2/latest/UserGuide/efa.md "../../../AWSEC2/latest/UserGuide/efa.md") (EFA) is a network device for Amazon EC2 instances that enables high-performance inter-node communication and RDMA (Remote Direct Memory Access) for artificial intelligence, machine learning, and High Performance Computing (HPC) workloads. Amazon EKS supports two mechanisms for managing EFA devices in EKS clusters: the _EFA Dynamic Resource Allocation (DRA) driver (DRANET)_ and the _EFA device plugin_.

We recommend using DRA drivers for new deployments with Kubernetes versions 1.34 and later when using [static capacity provisioning](https://karpenter.sh/docs/concepts/nodepools/#static-nodepool "https://karpenter.sh/docs/concepts/nodepools/#static-nodepool") in Karpenter, EKS managed node groups, or self-managed nodes. DRA is not currently supported with EKS Auto Mode. With the EFA DRA driver, you can configure topology-aware allocation that pairs EFA interfaces with their topologically-local GPUs or Neuron devices, and share devices between Pods.

## EFA DRA driver vs. EFA device plugin

| Feature                    | EFA DRA driver                                                                                 | EFA device plugin                                                   |
| -------------------------- | ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| Minimum Kubernetes version | 1.34                                                                                           | All EKS-supported Kubernetes versions                               |
| EKS Compute                | Karpenter (static capacity only), managed node groups, self-managed nodes                      | EKS Auto Mode, Karpenter, managed node groups, self-managed nodes   |
| EKS-optimized AMIs         | AL2023, Bottlerocket                                                                           | AL2023, Bottlerocket                                                |
| Device advertisement       | Rich attributes via `ResourceSlice` objects including device type, topology, and PCIe locality | Integer count of `vpc.amazonaws.com/efa` extended resources         |
| GPU-EFA affinity           | DRA-native topology-awareness                                                                  | Automatic topology-awareness (EKS-optimized AL2023 AMIs only)       |
| Neuron-EFA affinity        | DRA-native topology-awareness                                                                  | Automatic topology-awareness (EKS-optimized AL2023 AMIs only)       |
| Device sharing             | Multiple Pods can share the same EFA device through shared `ResourceClaim` references          | Not supported. Each EFA device is exclusively allocated to one Pod. |

## Creating EKS nodes with EFA interfaces

When you create EKS nodes with EFA interfaces, the EFA interfaces are attached to the instance during instance provisioning. You can customize the per-device EFA configuration and use [placement groups](../../../AWSEC2/latest/UserGuide/placement-groups.md "../../../AWSEC2/latest/UserGuide/placement-groups.md") with EKS Auto Mode, Karpenter, EKS managed node groups, or EKS self-managed node groups. With EKS Auto Mode, you pass configuration for each network interface through the `NodeClass` under `advancedNetworking.networkInterfaces`. With Karpenter, you pass configuration for each network interface via the `EC2NodeClass`. With EKS managed node groups or self-managed nodes, you pass configuration for each network interface with [launch templates](../../../AWSEC2/latest/UserGuide/ec2-launch-templates.md "../../../AWSEC2/latest/UserGuide/ec2-launch-templates.md").

When using [eksctl](install-kubectl.md#eksctl-install-update "install-kubectl.md#eksctl-install-update") for provisioning EKS nodes with the `efaEnabled` setting, all interfaces are configured with interface type `EFA`, an EFA-specific security group is created, and the EFA device plugin is installed on the cluster. If you need to customize the per-device EFA configuration when using `eksctl`, it is recommended to use `eksctl’s support for [launch templates](../eksctl/launch-template-support.md "../eksctl/launch-template-support.md").

The following examples show how to configure `NodeClass` and launch templates with EFA interfaces. This is useful to customize the interfaces used for EFA vs standard IP-based traffic. For information on the number of EFA interfaces supported by each instance type and how to configure them for maximum network bandwidth, see [Maximize network bandwidth for EFA-enabled instance types](../../../AWSEC2/latest/UserGuide/efa-acc-inst-types.md "../../../AWSEC2/latest/UserGuide/efa-acc-inst-types.md") in the _Amazon EC2 User Guide_.

## EKS Auto Mode

In EKS Auto Mode, you configure EFA network interfaces using the `advancedNetworking.networkInterfaces` field in the `NodeClass` (`eks.amazonaws.com/v1`). Each entry specifies a `networkCardIndex`, `deviceIndex`, and `interfaceType`. The `interfaceType` can be `interface` for standard network interfaces or `efa-only` for EFA interfaces dedicated to RDMA traffic without IP addresses assigned.

When `networkInterfaces` is configured, instances launched by the `NodePool` referencing the `NodeClass` use this configuration regardless of whether Pods request `vpc.amazonaws.com/efa` resources. EKS Auto Mode does not attach additional IPs, prefixes, or ENIs after instance launch for nodes with static network interface configuration — only the interfaces and IPs configured at launch are available to Pods.

This feature can be used with [static capacity node pools](auto-static-capacity.md "auto-static-capacity.md") to maintain pre-warmed, EFA-ready nodes for distributed training and inference workloads.

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

For the full list of constraints on static network interface configuration, see [Static Network Interface Configuration](create-node-class.md#static-network-interfaces "create-node-class.md#static-network-interfaces") in the NodeClass documentation.

## Karpenter

Each entry in `networkInterfaces` specifies a `networkCardIndex`, `deviceIndex`, and `interfaceType`. The `interfaceType` can be `interface` for standard network interfaces or `efa-only` for EFA interfaces that are dedicated to RDMA traffic and do not have IP addresses assigned. When `networkInterfaces` is configured, instances launched by the `NodePool` referencing the `NodeClass` use this configuration regardless of whether Pods request `vpc.amazonaws.com/efa` resources.

When using Karpenter without specifying `networkInterfaces` in your `NodeClass`, instances created for Pods requesting `vpc.amazonaws.com/efa` have all interfaces configured with interface type `EFA`.

The `networkInterfaces` configuration for `EC2NodeClass` was added in Karpenter v1.11. The following example shows an `EC2NodeClass` configured for a P6-B200 instance with 1 ENA interface and 8 EFA-only interfaces.

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

With EKS managed node groups or self-managed nodes, you pass configuration for each network interface with [launch templates](../../../AWSEC2/latest/UserGuide/ec2-launch-templates.md "../../../AWSEC2/latest/UserGuide/ec2-launch-templates.md").

The following example shows a launch template configured for a P6-B200 instance with 1 ENA interface and 8 EFA-only interfaces. The primary network interface (network card 0, device index 0) uses a standard `interface` type for IP traffic, while additional interfaces use `efa-only` for dedicated RDMA traffic. Adjust the number of `efa-only` interfaces based on your instance type. For the number of EFA interfaces supported by each instance type, see [Maximize network bandwidth for EFA-enabled instance types](../../../AWSEC2/latest/UserGuide/efa-acc-inst-types.md "../../../AWSEC2/latest/UserGuide/efa-acc-inst-types.md") in the _Amazon EC2 User Guide_.

Replace `*security-group-id*` with your values. The security group must allow all inbound and outbound traffic to and from itself to enable EFA OS-bypass functionality. For more information, see [Step 1: Prepare an EFA-enabled security group](../../../AWSEC2/latest/UserGuide/efa-start.md#efa-start-security "../../../AWSEC2/latest/UserGuide/efa-start.md#efa-start-security") in the _Amazon EC2 User Guide_.

###### Important

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

The EKS-optimized AL2023 AMIs and all Bottlerocket AMIs include the host-level components required to use EFA, specifically the components installed by the [aws-efa-installer](../../../AWSEC2/latest/UserGuide/efa-start.md#efa-start-enable "../../../AWSEC2/latest/UserGuide/efa-start.md#efa-start-enable"). The EKS AL2023 and Bottlerocket AMIs **do not include** the EFA DRA driver or EFA device plugin, and these must be installed separately on your cluster before deploying workloads.

## Conserving IP address allocation

EFA-enabled instances such as `p5.48xlarge` and `p6-b200.48xlarge` support many network interfaces. By default, the Amazon VPC CNI allocates IP addresses across all IP-enabled attached ENIs, which can consume a large number of IP addresses from your subnet even when those addresses are not actively used by Pods. On instances with dozens of network interfaces, this can quickly exhaust your subnet’s available IP space.

To reduce IP address consumption on EFA-enabled nodes, configure your network interfaces to use `efa-only` for all interfaces except the primary. EFA-only interfaces are dedicated to RDMA traffic and do not have IP addresses assigned, so they do not consume addresses from your subnet. For example configurations, see [Karpenter](#eks-efa-auto-karpenter "#eks-efa-auto-karpenter") and [EKS managed node groups and self-managed nodes](#eks-efa-mng-self-managed "#eks-efa-mng-self-managed"). For the recommended interface layout for each instance type, see [Maximize network bandwidth for EFA-enabled instance types](../../../AWSEC2/latest/UserGuide/efa-acc-inst-types.md "../../../AWSEC2/latest/UserGuide/efa-acc-inst-types.md") in the _Amazon EC2 User Guide_.

In addition to using `efa-only` interfaces, you can configure the Amazon VPC CNI to limit the number of warm (pre-allocated) IP addresses and ENIs. By default, the VPC CNI pre-allocates a warm pool of ENIs and IP addresses for faster Pod startup, but on large instances this can reserve hundreds of unused IP addresses. Set the `WARM_IP_TARGET` and `WARM_ENI_TARGET` environment variables on the `aws-node` DaemonSet to control how many spare IP addresses and ENIs the CNI maintains. For more information on these settings, see [Amazon VPC CNI best practices](../best-practices/vpc-cni.md#_overview "../best-practices/vpc-cni.md#_overview").

###### Note

The `WARM_ENI_TARGET` and `WARM_IP_TARGET` settings are cluster-wide and apply to all nodes managed by the VPC CNI. There is currently no way to set different values for each node group or instance type. If you need more granular control of these settings, provide feedback on [containers-roadmap issue #1834](https://github.com/aws/containers-roadmap/issues/1834 "https://github.com/aws/containers-roadmap/issues/1834") on GitHub.

## Install the EFA DRA driver (DRANET)

The EFA DRA driver is built in the upstream [DRANET](https://github.com/kubernetes-sigs/dranet "https://github.com/kubernetes-sigs/dranet") project on GitHub, which provides cloud-aware network device management for Kubernetes DRA. _EFA DRA driver_ and _DRANET_ are used interchangeably throughout this documentation and refer to the same tool.

The EFA DRA driver advertises EFA devices as `ResourceSlice` objects with the driver name `dra.net` and the `DeviceClass` name `efa.networking.k8s.aws`. The EFA DRA driver runs as a DaemonSet on each node and automatically discovers EFA devices.

### Prerequisites

- An Amazon EKS cluster running Kubernetes version 1.34 or later with static capacity provisioned by Karpenter, EKS managed node groups, or self-managed node groups.
- Nodes with EFA-enabled Amazon EC2 instance types. For a list of supported instance types, see [Supported instance types](../../../AWSEC2/latest/UserGuide/efa.md#efa-instance-types "../../../AWSEC2/latest/UserGuide/efa.md#efa-instance-types") in the _Amazon EC2 User Guide_.
- Nodes with host-level components installed for EFA, see [Install the EFA software](../../../AWSEC2/latest/UserGuide/efa-start.md#efa-start-enable "../../../AWSEC2/latest/UserGuide/efa-start.md#efa-start-enable") for more information. The EKS-optimized AL2023 NVIDIA and Neuron AMIs, and the Bottlerocket AMIs include the EFA host-level components.
- Helm installed in your command-line environment, see the [Setup Helm instructions](helm.md "helm.md") for more information.
- `kubectl` configured to communicate with your cluster, see [Install or update kubectl](install-kubectl.md#kubectl-install-update "install-kubectl.md#kubectl-install-update") for more information.

### Procedure

###### Important

Do not install the EFA DRA driver on nodes where the EFA device plugin is running. The two mechanisms cannot coexist on the same node. Doing so can cause silent oversubscription of the underlying devices to multiple pods on the same node.

1. Add the EKS Helm chart repository.

```
helm repo add eks https://aws.github.io/eks-charts
```

2. Update your local Helm repository.

```
helm repo update
```

3. Install the EFA DRA driver on your cluster using Helm. The EFA DRA driver automatically detects that it is running on EC2 instances via the Instance Metadata Service (IMDS) and enables EFA device discovery. The EFA DRA driver is deployed as a DaemonSet in the `kube-system` namespace by default. See the Helm values.yaml in the [EKS Helm chart repository](https://github.com/aws/eks-charts/tree/master/stable/aws-dranet "https://github.com/aws/eks-charts/tree/master/stable/aws-dranet") on GitHub for the configurable parameters.

```
helm install aws-dranet eks/aws-dranet --namespace kube-system
```

4. Verify that the DRANET DaemonSet is running.

```
kubectl get daemonset -n kube-system aws-dranet
```

```
NAME          DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR   AGE
aws-dranet    2         2         2       2            2           <none>          60s
```

5. Verify that the `DeviceClass` was created.

```
kubectl get deviceclass
```

```
NAME                    AGE
efa.networking.k8s.aws  60s
```

6. Verify that `ResourceSlice` objects are advertised for your nodes.

```
kubectl get resourceslices --field-selector spec.driver=dra.net
```

If you experience errors with the steps above, you can check the logs for DRANET with the following command.

```
kubectl logs -n kube-system -l app=aws-dranet
```

7. To request EFA devices using the DRA driver, create a `ResourceClaim` or `ResourceClaimTemplate` that references the EFA `DeviceClass` and reference it in your Pod specification. The following example requests a single EFA device.

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

The EFA DRA driver supports topology-aware allocation that pairs EFA interfaces with GPUs or Neuron devices on the same PCIe root. Use the `matchAttribute` constraint to align EFA and GPU or Neuron device allocations. To use this capability, you must also use the NVIDIA or Neuron DRA drivers. For more information, see [Manage NVIDIA GPUs on Amazon EKS](device-management-nvidia.md "device-management-nvidia.md") and [Manage Neuron devices on Amazon EKS](device-management-neuron.md "device-management-neuron.md").

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

The number in the `devicegroup` attribute name corresponds to the number of Neuron devices in the connected topology group. For example, `resource.aws.com/devicegroup1_id` identifies a single Neuron device, `resource.aws.com/devicegroup4_id` identifies a group of 4 connected devices, and `resource.aws.com/devicegroup8_id` and `resource.aws.com/devicegroup16_id` identify groups of 8 and 16 connected devices respectively. Choose the `matchAttribute` that matches the device `count` in your request so that the allocated Neuron devices and EFA interfaces belong to the same connected topology group. For more information on these attributes, see the [Neuron DRA driver documentation](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/containers/neuron-dra.html "https://awsdocs-neuron.readthedocs-hosted.com/en/latest/containers/neuron-dra.html").

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

2. Reference the `ResourceClaim` by name in each Pod that needs access to the EFA devices. Each Pod uses `resourceClaimName` to reference the existing claim instead of `resourceClaimTemplateName`.

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

Both Pods reference the same `shared-efa`
`ResourceClaim` and are scheduled to the node where those EFA devices are allocated. The `ResourceClaim` lifecycle is independent of the Pods — it persists until you delete it, even if all Pods referencing it are removed.

## Install the EFA Kubernetes device plugin

The EFA Kubernetes device plugin advertises EFA devices as `vpc.amazonaws.com/efa` extended resources. You request EFA devices in container resource requests and limits. For a complete walkthrough of setting up EFA with training workloads, see [Run machine learning training on Amazon EKS with Elastic Fabric Adapter](node-efa.md "node-efa.md").

###### Important

Topology-aligned allocation of NVIDIA GPUs or Neuron devices with EFA interfaces happens automatically when using the EKS-optimized AL2023 accelerated AMIs. This automatic alignment does not occur when using Bottlerocket EKS-optimized AMIs or custom AMIs. If you need topology-aligned accelerator and EFA device allocation with Bottlerocket or custom AMIs, use the EFA DRA driver and the corresponding Neuron DRA driver. To use the NVIDIA DRA driver on Bottlerocket, you must first disable the NVIDIA device plugin that is bundled with the Bottlerocket NVIDIA variants, which requires Bottlerocket version 1.63.0 or later. For more information, see [Topology-aware EFA and GPU/Neuron device allocation](#efa-dra-topology-aware "#efa-dra-topology-aware") and [Install the NVIDIA DRA driver](device-management-nvidia-dra-device-plugin.md#eks-nvidia-dra-driver "device-management-nvidia-dra-device-plugin.md#eks-nvidia-dra-driver").

###### Important

Starting with NVIDIA `k8s-device-plugin` v0.19.0, the `--mofed-enabled` flag defaults to `true`, which causes the NVIDIA device plugin to mount all `/dev/infiniband/uverbs*` devices into containers requesting GPUs. This conflicts with the EFA device plugin, which should be the component managing EFA device allocation at `/dev/infiniband`. If you are using EKS managed node groups or self-managed nodes with the NVIDIA device plugin, you must explicitly disable MOFED. For instructions, see [Install the NVIDIA Kubernetes device plugin](device-management-nvidia-dra-device-plugin.md#eks-nvidia-device-plugin "device-management-nvidia-dra-device-plugin.md#eks-nvidia-device-plugin").

EKS Auto Mode does not enable MOFED by default and is not affected by this issue.

### Prerequisites

- An Amazon EKS cluster.
- Nodes with EFA-enabled Amazon EC2 instance types. For a list of supported instance types, see [Supported instance types](../../../AWSEC2/latest/UserGuide/efa.md#efa-instance-types "../../../AWSEC2/latest/UserGuide/efa.md#efa-instance-types") in the _Amazon EC2 User Guide_.
- Nodes with host-level components installed for EFA, see [Install the EFA software](../../../AWSEC2/latest/UserGuide/efa-start.md#efa-start-enable "../../../AWSEC2/latest/UserGuide/efa-start.md#efa-start-enable") for more information. The EKS-optimized AL2023 AMIs and the Bottlerocket AMIs include the EFA host-level components.
- Helm installed in your command-line environment, see the [Setup Helm instructions](helm.md "helm.md") for more information.
- `kubectl` configured to communicate with your cluster, see [Install or update kubectl](install-kubectl.md#kubectl-install-update "install-kubectl.md#kubectl-install-update") for more information.

### Procedure

1. Add the EKS Helm chart repository.

```
helm repo add eks https://aws.github.io/eks-charts
```

2. Update your local Helm repository.

```
helm repo update
```

3. Install the EFA device plugin.

```
helm install efa eks/aws-efa-k8s-device-plugin -n kube-system
```

4. Verify the EFA device plugin DaemonSet is running.

```
kubectl get daemonset -n kube-system efa-aws-efa-k8s-device-plugin
```

```
NAME                                  DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR   AGE
efa-aws-efa-k8s-device-plugin         2         2         2       2            2           <none>          60s
```

5. Verify that your nodes have allocatable EFA resources.

```
kubectl get nodes "-o=custom-columns=NAME:.metadata.name,EFA:.status.allocatable.vpc\.amazonaws\.com/efa"
```

```
NAME                                           EFA
ip-192-168-11-225.us-west-2.compute.internal   4
ip-192-168-24-96.us-west-2.compute.internal    4
```

6. To request EFA devices using the device plugin, specify the `vpc.amazonaws.com/efa` resource in your container resource requests and limits.

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
