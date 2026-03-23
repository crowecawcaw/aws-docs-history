**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Manage hardware devices on Amazon EKS

Amazon EKS supports two Kubernetes mechanisms for managing specialized hardware devices in EKS clusters: _Dynamic Resource Allocation (DRA)_ and _device plugins_. Both mechanisms enable workloads to access hardware accelerators such as NVIDIA GPUs and AWS Trainium chips, and high-performance network devices such as Elastic Fabric Adapter (EFA). It’s recommended to use DRA drivers for new deployments with Kubernetes versions 1.34 and later, as DRA provides richer device selection, topology-aware scheduling, and device sharing capabilities that are not possible with device plugins.

Reference the Kubernetes documentation for [Dynamic Resource Allocation](https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/ "https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/") and [device plugins](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/ "https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/") for general information about these two Kubernetes features.

## Dynamic Resource Allocation vs device plugins

Kubernetes device plugins have been the primary mechanism for exposing specialized hardware to Kubernetes workloads. Device plugins advertise devices as extended resources (for example, `nvidia.com/gpu` or `aws.amazon.com/neuroncore`) that you request in container resource requests and limits. While device plugins are widely supported and used, they have limitations:

- Devices are requested as opaque integer counts with no attribute-based filtering.
- No support for device sharing between containers or Pods.
- No expressive topology-aware allocation across device types.
- Custom scheduler extensions are often required for intelligent placement.

Dynamic Resource Allocation (DRA) is a Kubernetes feature made generally available in Kubernetes version 1.34 that addresses these limitations. With DRA, device drivers publish rich device attributes to the Kubernetes scheduler through `ResourceSlice` objects. You request devices using `ResourceClaim` and `ResourceClaimTemplate` objects that reference `DeviceClass` categories.

DRA enables:

- Attribute-based device selection using [Common Expression Language (CEL)](https://kubernetes.io/docs/reference/using-api/cel/ "https://kubernetes.io/docs/reference/using-api/cel/") expressions.
- Topology-aware allocation that ensures devices are co-located on the same PCIe switch or NUMA domain.
- Device sharing between multiple containers or Pods through shared `ResourceClaim` references.
- Constraint-based scheduling that aligns different device types

## DRA drivers for Amazon EKS

The following DRA drivers are commonly used for managing specialized hardware devices in Amazon EKS clusters.

Neuron DRA driver

The Neuron DRA driver manages AWS Trainium and AWS Inferentia2 device allocation with topology-aware scheduling, connected device subset allocation, and Logical NeuronCore (LNC) configuration, without requiring custom scheduler extensions.

NVIDIA DRA driver

The [NVIDIA DRA driver for GPUs](https://github.com/NVIDIA/k8s-dra-driver-gpu "https://github.com/NVIDIA/k8s-dra-driver-gpu") enables flexible allocation and dynamic reconfiguration of NVIDIA GPUs, including support for `ComputeDomain` resources for Multi-Node NVLink (MNNVL) workloads on EC2 Grace-Blackwell instances. For more information on using `ComputeDomains` with EC2 Grace-Blackwell instances, see [Use P6e-GB200 UltraServers with Amazon EKS](ml-eks-nvidia-ultraserver.md "ml-eks-nvidia-ultraserver.md").

## Device plugins for Amazon EKS

The following device plugins are commonly used for managing specialized hardware devices in Amazon EKS clusters.

EFA device plugin

The EFA device plugin discovers all available EFA devices on each node and advertises EFA devices as `vpc.amazonaws.com/efa` extended resources.

Neuron device plugin

The [Neuron device plugin](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/containers/tutorials/k8s-setup.html "https://awsdocs-neuron.readthedocs-hosted.com/en/latest/containers/tutorials/k8s-setup.html") exposes Neuron hardware as `aws.amazon.com/neuroncore` and `aws.amazon.com/neuron` extended resources. It discovers available Neuron devices on each node, advertises them as allocatable resources, and manages their lifecycle.

NVIDIA device plugin

The [NVIDIA device plugin](https://github.com/NVIDIA/k8s-device-plugin "https://github.com/NVIDIA/k8s-device-plugin") advertises NVIDIA GPUs as `nvidia.com/gpu` extended resources and tracks the health of GPUs.

## Considerations

Before using DRA drivers on Amazon EKS, review the following considerations:

- DRA is available on Amazon EKS with Kubernetes version 1.33 and above, but it is recommended for Kubernetes versions 1.34 and later due to an upstream [Kubernetes issue](https://github.com/kubernetes/kubernetes/issues/133920 "https://github.com/kubernetes/kubernetes/issues/133920"). Your cluster control plane and nodes must be running a Kubernetes version that supports DRA.
- DRA is not currently compatible with Karpenter or EKS Auto Mode provisioned compute. You must use EKS managed node groups or self-managed nodes with DRA drivers.
- DRA drivers and device plugins for the same device type **must** not run simultaneously on the same node. Uninstall the device plugin before installing the corresponding DRA driver, or deploy them on separate nodes. See upstream Kubernetes [KEP-5004](https://github.com/kubernetes/enhancements/issues/5004 "https://github.com/kubernetes/enhancements/issues/5004") for updates on DRA driver and device plugin compatibility.
- DRA uses different Kubernetes API resources (`ResourceClaim`, `ResourceClaimTemplate`, `DeviceClass`) than device plugins (`resource.limits`, `resource.requests`). Migrating from device plugins to DRA requires updating your workload specifications.
- Device plugins remain fully supported for all Kubernetes versions. If your cluster runs a Kubernetes version earlier than 1.34, if you use Karpenter or EKS Auto Mode, or if you use Bottlerocket, continue using device plugins.

## Topics

- [Manage EFA devices on Amazon EKS](device-management-efa.md "device-management-efa.md")
- [Manage Neuron devices on Amazon EKS](device-management-neuron.md "device-management-neuron.md")
- [Manage NVIDIA GPU devices on Amazon EKS](device-management-nvidia.md "device-management-nvidia.md")
