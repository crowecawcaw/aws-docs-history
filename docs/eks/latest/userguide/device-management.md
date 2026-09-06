

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Manage hardware devices on Amazon EKS
<a name="device-management"></a>

Amazon EKS supports two Kubernetes mechanisms for managing specialized hardware devices in EKS clusters: *Dynamic Resource Allocation (DRA)* and *device plugins*. Both mechanisms enable workloads to access hardware accelerators such as NVIDIA GPUs and AWS Trainium chips, and high-performance network devices such as Elastic Fabric Adapter (EFA).

We recommend using DRA drivers for new deployments with Kubernetes versions 1.34 and later when using [static capacity provisioning](https://karpenter.sh/docs/concepts/nodepools/#static-nodepool) in Karpenter, EKS managed node groups, or self-managed nodes. DRA is not currently supported with EKS Auto Mode. DRA provides richer device selection, topology-aware scheduling, and device sharing capabilities that are not possible with device plugins.

Reference the Kubernetes documentation for [Dynamic Resource Allocation](https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/) and [device plugins](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/) for general information about these two Kubernetes features.

## Dynamic Resource Allocation vs device plugins
<a name="_dynamic_resource_allocation_vs_device_plugins"></a>

Kubernetes device plugins have been the primary mechanism for exposing specialized hardware to Kubernetes workloads. Device plugins advertise devices as extended resources (for example, `nvidia.com/gpu` or `aws.amazon.com/neuroncore`) that you request in container resource requests and limits. While device plugins are widely supported and used, they have limitations:
+ Devices are requested as opaque integer counts with no attribute-based filtering.
+ No support for device sharing between containers or Pods.
+ No expressive topology-aware allocation across device types.
+ Custom scheduler extensions are often required for intelligent placement.

Dynamic Resource Allocation (DRA) is a Kubernetes feature made generally available in Kubernetes version 1.34 that addresses these limitations. With DRA, device drivers publish rich device attributes to the Kubernetes scheduler through `ResourceSlice` objects. You request devices using `ResourceClaim` and `ResourceClaimTemplate` objects that reference `DeviceClass` categories.

DRA enables:
+ Attribute-based device selection using [Common Expression Language (CEL)](https://kubernetes.io/docs/reference/using-api/cel/) expressions.
+ Topology-aware allocation that ensures devices are co-located on the same PCIe switch or NUMA domain.
+ Device sharing between multiple containers or Pods through shared `ResourceClaim` references.
+ Dynamic partitioning and sharing of NVIDIA GPUs when using MIG or time-slicing

## DRA drivers for Amazon EKS
<a name="_dra_drivers_for_amazon_eks"></a>

The following DRA drivers are commonly used for managing specialized hardware devices in Amazon EKS clusters.

NVIDIA DRA driver  
The [NVIDIA DRA driver for GPUs](https://github.com/kubernetes-sigs/dra-driver-nvidia-gpu) on GitHub enables flexible allocation and dynamic configuration of NVIDIA GPUs. See [Use the NVIDIA DRA driver or device plugin on Amazon EKS](device-management-nvidia-dra-device-plugin.md) for information on managing GPUs with the NVIDIA DRA driver and [Use P6e-GB200 UltraServers with Amazon EKS](ml-eks-nvidia-ultraserver.md) for information on using `ComputeDomains` for Multi-Node NVLink (MNNVL) workloads with EC2 Grace-Blackwell instances.

EFA DRA driver  
The EFA DRA driver ([DRANET](https://github.com/kubernetes-sigs/dranet) on GitHub) manages Elastic Fabric Adapter (EFA) device allocation with topology-aware scheduling that pairs EFA interfaces with their topologically-local GPUs or Neuron devices, and supports device sharing between Pods. For more information, see [Manage EFA devices on Amazon EKS](device-management-efa.md).

Neuron DRA driver  
The Neuron DRA driver manages AWS Trainium and AWS Inferentia2 device allocation with topology-aware scheduling, connected device subset allocation, and Logical NeuronCore (LNC) configuration, without requiring custom scheduler extensions. For more information, see [Manage Neuron devices on Amazon EKS](device-management-neuron.md).

## Device plugins for Amazon EKS
<a name="_device_plugins_for_amazon_eks"></a>

The following device plugins are commonly used for managing specialized hardware devices in Amazon EKS clusters.

NVIDIA device plugin  
The [NVIDIA device plugin](https://github.com/NVIDIA/k8s-device-plugin) on GitHub advertises NVIDIA GPUs as `nvidia.com/gpu` extended resources and tracks the health of GPUs.

EFA device plugin  
The EFA device plugin discovers all available EFA devices on each node and advertises EFA devices as `vpc.amazonaws.com/efa` extended resources.

Neuron device plugin  
The [Neuron device plugin](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/containers/tutorials/k8s-setup.html) exposes Neuron hardware as `aws.amazon.com/neuroncore` and `aws.amazon.com/neuron` extended resources. It discovers available Neuron devices on each node, advertises them as allocatable resources, and manages their lifecycle.

## Considerations
<a name="_considerations"></a>

Before using DRA drivers on Amazon EKS, review the following considerations:
+ DRA is available on Amazon EKS with Kubernetes version 1.33 and above, but it is recommended for Kubernetes versions 1.34 and later because of an upstream [Kubernetes issue](https://github.com/kubernetes/kubernetes/issues/133920) on GitHub. Your cluster control plane and nodes must be running a Kubernetes version that supports DRA.
+ DRA is not currently compatible with EKS Auto Mode.
+ DRA is not currently compatible with Karpenter when using dynamically provisioned capacity. You must use static capacity provisioning in Karpenter, or EKS managed node groups or self-managed nodes with DRA drivers.
+ DRA drivers and device plugins for the same device type **must** not run simultaneously on the same node. Uninstall the device plugin before installing the corresponding DRA driver, or deploy them on separate nodes. Running both DRA driver and device plugin for the same device on the same node can cause silent oversubscription of the underlying hardware devices.
+ DRA uses different Kubernetes API resources (`ResourceClaim`, `ResourceClaimTemplate`, `DeviceClass`) than device plugins (`resource.limits`, `resource.requests`). You can use DRA to manage the device plugin extended resources without changing your workload specifications. For more information about extended resources in DRA, see the [Kubernetes documentation](https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/#extended-resource) on the Kubernetes website.
+ The DRA drivers for NVIDIA, EFA, and Neuron are compatible with both the EKS-optimized AL2023 AMIs and the Bottlerocket AMIs. If you are using the NVIDIA DRA driver with Bottlerocket, disable the NVIDIA device plugin that is included in the Bottlerocket NVIDIA variants.
+ Device plugins remain fully supported for all Kubernetes versions.

## DRA ResourceClaim vs ResourceClaimTemplate
<a name="_dra_resourceclaim_vs_resourceclaimtemplate"></a>

When using DRA, you request devices through `ResourceClaim` or `ResourceClaimTemplate` objects. These two resource types serve different purposes and have different lifecycle behaviors.

ResourceClaim  
A `ResourceClaim` is a named Kubernetes object that you create independently of any Pod. You reference it in a Pod specification by name using the `resourceClaimName` field. A `ResourceClaim` has the following characteristics:  
+ It must exist in the cluster before any Pod that references it is created. If the claim does not exist, the Pod remains in a pending state.
+ It persists until you explicitly delete it, regardless of whether any Pods reference it.
+ Multiple Pods can reference the same `ResourceClaim`, which enables device sharing. All Pods that reference the same claim share access to the same allocated devices and are scheduled to the same node.

  Use a `ResourceClaim` when you need multiple Pods to share access to the same devices, or when you need a claim to exist beyond the lifetime of a single Pod.

ResourceClaimTemplate  
A `ResourceClaimTemplate` defines a template that Kubernetes uses to automatically generate a unique `ResourceClaim` for each Pod. You reference it in a Pod specification using the `resourceClaimTemplateName` field. The `ResourceClaimTemplate` itself is not bound to any Pod — it is a reusable template that persists independently. A `ResourceClaimTemplate` has the following characteristics:  
+ Kubernetes creates a new `ResourceClaim` for each Pod that references the template. Each Pod gets its own separate set of devices.
+ Each generated `ResourceClaim` is bound to the lifecycle of the Pod that triggered its creation. When the Pod is deleted, the associated generated `ResourceClaim` is also deleted. The `ResourceClaimTemplate` itself is not affected and continues to generate new claims for future Pods.

  Use a `ResourceClaimTemplate` when each Pod in a workload needs its own dedicated devices with similar configurations. For example, use a `ResourceClaimTemplate` for Pods in a Job that uses parallel execution where each Pod needs its own GPU or EFA devices.

The following table summarizes the differences between `ResourceClaim` and `ResourceClaimTemplate`.


| Behavior | ResourceClaim | ResourceClaimTemplate | 
| --- | --- | --- | 
| Creation | You create it manually before Pods reference it | Kubernetes generates a claim automatically per Pod | 
| Lifecycle | Persists until you delete it | The template persists until you delete it. Each generated `ResourceClaim` is bound to the Pod that triggered its creation. | 
| Device sharing across Pods | Supported. Multiple Pods can reference the same claim. | Not supported. Each Pod gets a separate claim. | 
| Pod specification field |  `resourceClaimName`  |  `resourceClaimTemplateName`  | 

For examples of using `ResourceClaim` objects to share EFA devices between Pods, see [Share EFA devices between multiple Pods](device-management-efa.md#efa-dra-share). For examples of using `ResourceClaimTemplate` objects with topology-aware allocation, see [Topology-aware EFA and GPU/Neuron device allocation](device-management-efa.md#efa-dra-topology-aware).

## Topics
<a name="_topics"></a>
+  [Manage EFA devices on Amazon EKS](device-management-efa.md) 
+  [Manage Neuron devices on Amazon EKS](device-management-neuron.md) 
+  [Manage NVIDIA GPUs on Amazon EKS](device-management-nvidia.md) 
+  [Use the NVIDIA DRA driver or device plugin on Amazon EKS](device-management-nvidia-dra-device-plugin.md) 
+  [Use multi-instance GPUs (MIG) with NVIDIA GPUs on Amazon EKS](device-management-nvidia-mig.md) 
+  [Use time-slicing with NVIDIA GPUs on Amazon EKS](device-management-nvidia-time-slicing.md) 