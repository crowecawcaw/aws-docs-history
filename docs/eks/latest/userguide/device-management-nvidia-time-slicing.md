

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Use time-slicing with NVIDIA GPUs on Amazon EKS
<a name="device-management-nvidia-time-slicing"></a>

Time-slicing lets multiple Pods share a single physical NVIDIA GPU. The Kubernetes scheduler places multiple Pods on the same GPU, and the GPU’s CUDA scheduler time-multiplexes the work. Time-slicing is the simplest GPU-sharing strategy. It uses software only, requires no special hardware, and works on every NVIDIA GPU instance type on AWS. Time-slicing does not offer memory or compute isolation between Pods that share a GPU. It best suits workloads with low GPU utilization, such as inference services that idle between requests or development environments where several users share a GPU. For workloads that require hardware-level memory and compute isolation, use Multi-Instance GPU (MIG) instead.

On Amazon EKS, you can manage time-slicing with either the [NVIDIA DRA driver](device-management-nvidia-dra-device-plugin.md#eks-nvidia-dra-driver) or the [NVIDIA device plugin](device-management-nvidia-dra-device-plugin.md#eks-nvidia-device-plugin).

Time-slicing can only be used with Karpenter if you are using [static capacity provisioning](https://karpenter.sh/docs/concepts/nodepools/#static-nodepool). Time-slicing is not currently available in EKS Auto Mode.

Time-slicing is a good fit when:
+ GPU utilization is consistently low, for example latency-sensitive inference services that idle between requests.
+ Several developers share a single GPU node for notebook or development work.
+ Your nodes use a GPU instance type that does not support MIG, such as the `g5`, `g6`, or `g6e` families.
+ You can accept that a Pod is occasionally slower because another Pod on the same GPU is busy.

Consider a different approach when:
+ You need memory isolation. Pods on a time-sliced GPU share the same GPU memory, and one Pod can exhaust the memory that other Pods rely on. Use MIG for memory isolation.
+ You need predictable per-Pod latency or quality of service. The GPU scheduler shares compute across slots on a best-effort basis without guarantees.
+ You run training workloads. Time-slicing adds context-switching that reduces training efficiency. A checkpointed job that another Pod slows down must retry from its last checkpoint.

## Considerations
<a name="eks-time-slicing-considerations"></a>

Review the following considerations before you use time-slicing in production.

### General considerations
<a name="_general_considerations"></a>
+  **No memory isolation:** Pods that share a time-sliced GPU share its memory. One Pod can allocate memory that other Pods need, which can cause out-of-memory errors. Match the number of Pods that share each GPU to the memory footprint of your workloads. If your Pods regularly load large models, share fewer Pods per GPU or use MIG.
+  **Best-effort compute sharing:** The GPU scheduler shares compute across Pods on a best-effort basis and does not guarantee proportional compute to each Pod.
+  **Time-slicing and MPS cannot share the same GPU:** Time-slicing sets the GPU compute mode to `DEFAULT`, while NVIDIA Multi-Process Service (MPS) requires `EXCLUSIVE_PROCESS`. You can use both strategies in the same cluster, but not on the same physical GPU at the same time. Time-slicing also has no effect on a MIG instance. To share a single MIG instance across containers, use MPS instead.
+  **Per-container metrics:** NVIDIA Data Center GPU Manager (DCGM) cannot attribute metrics to individual containers when time-slicing is active. GPU-level metrics remain available, but you cannot identify which Pod consumed a given amount of GPU resources.

### NVIDIA DRA driver considerations
<a name="_nvidia_dra_driver_considerations"></a>
+  **Alpha feature:** Time-slicing through the DRA driver requires the `TimeSlicingSettings` feature gate, which is an alpha feature disabled by default. For more information, see [Use GPU time-slicing with the NVIDIA DRA driver](#eks-time-slicing-dra).
+  **User-mediated sharing only:** Pods share a GPU only by referencing the same `ResourceClaim` or `ResourceClaimTemplate`, which is namespace-scoped, so sharing cannot cross namespaces. System-mediated sharing is a proposed future capability.
+  **Disable the built-in device plugin on Bottlerocket:** The DRA driver cannot run alongside the NVIDIA device plugin on the same node. On Bottlerocket, disable the built-in device plugin, which requires Bottlerocket version 1.63.0 or later. For more information, see [Install the NVIDIA DRA driver](device-management-nvidia-dra-device-plugin.md#eks-nvidia-dra-driver).
+  **Compute support:** The NVIDIA DRA driver is supported with static capacity provisioning in Karpenter, EKS managed node groups, or self-managed nodes, and is not supported with EKS Auto Mode. For more information, see the [Karpenter static NodePool documentation](https://karpenter.sh/docs/concepts/nodepools/#static-nodepool) on the Karpenter website.

### NVIDIA device plugin considerations
<a name="_nvidia_device_plugin_considerations"></a>
+  **Best-effort compute sharing with slots:** The device plugin advertises a fixed number of slots per GPU. If a single Pod requests more than one slot, it does not receive additional compute. Enable the `fail-requests-greater-than-one` option to reject Pods that request more than one slot.
+  **Provisioning with Karpenter:** Karpenter counts each `nvidia.com/gpu` request as a physical GPU even when time-slicing is enabled on the GPU. For more information, see [Karpenter issue \#2140](https://github.com/kubernetes-sigs/karpenter/issues/2140) on GitHub.
+  **No support on EKS Auto Mode:** EKS Auto Mode manages the NVIDIA device plugin and does not expose its configuration. Because time-slicing requires device plugin configuration, you cannot apply a time-slicing configuration on EKS Auto Mode nodes.
+  **Time-slicing configuration changes:** The NVIDIA device plugin does not monitor the time-slicing `ConfigMap` for changes. Restart the device plugin after you update the configuration.

## Configuration options
<a name="eks-time-slicing-configuration-options"></a>

You can use time-slicing for NVIDIA GPUs with the EKS-optimized AL2023 and Bottlerocket NVIDIA AMIs. The time-slicing settings vary based on whether you are using the NVIDIA DRA driver or NVIDIA device plugin.

------
#### [ NVIDIA DRA driver ]

The EKS-optimized accelerated AMIs do not include the NVIDIA DRA driver. If you are using Bottlerocket, you must disable the built-in NVIDIA device plugin before you use the NVIDIA DRA driver by setting `settings.kubelet-device-plugins.nvidia.enabled = false` in the node user data, which requires Bottlerocket version 1.63.0 or later. For more information, see [Install the NVIDIA DRA driver](device-management-nvidia-dra-device-plugin.md#eks-nvidia-dra-driver).

With the NVIDIA DRA driver, time-slicing is configured through ResourceClaimTemplates. The `interval` field controls the CUDA time-slice duration.


| Interval | Description | 
| --- | --- | 
| Default | Uses the NVIDIA GPU driver’s built-in default interval | 
| Short | Shorter interval; contexts switch more frequently | 
| Medium | Intermediate interval | 
| Long | each context runs longer per turn before being preempted | 

------
#### [ NVIDIA device plugin ]
+  **Bottlerocket** – The AMI includes a pre-installed NVIDIA device plugin. You configure time-slicing through Bottlerocket settings, with no separate device plugin installation, Helm chart, or `ConfigMap`.
+  **AL2023** – You install the NVIDIA device plugin as described in [Install the NVIDIA Kubernetes device plugin](device-management-nvidia-dra-device-plugin.md#eks-nvidia-device-plugin), and supply the time-slicing configuration through a `ConfigMap`.

  The following options control how the NVIDIA device plugin advertises and manages time-sliced GPUs. The field names differ between the Bottlerocket settings and the AL2023 `ConfigMap`, as shown in the procedures that follow.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/eks/latest/userguide/device-management-nvidia-time-slicing.html)

  For the complete list of GPU sharing options and their default values, see the [NVIDIA Kubernetes device plugin documentation](https://github.com/NVIDIA/k8s-device-plugin/blob/main/README.md#shared-access-to-gpus) on GitHub.

------

## Use GPU time-slicing with the NVIDIA DRA driver
<a name="eks-time-slicing-dra"></a>

With the NVIDIA DRA driver, Pods share a GPU by referencing a common `ResourceClaim` that requests the `gpu.nvidia.com` `DeviceClass` with a time-slicing `GpuConfig`.

The NVIDIA DRA driver currently implements *user-mediated* time-slicing: a GPU is shared only among the Pods and containers that you explicitly point at the same claim. Because a `ResourceClaim` and a `ResourceClaimTemplate` are namespace-scoped, the Pods that share a GPU this way must be in the same namespace. To share a GPU across containers in a single Pod, have each container reference the same request name in the claim. Containers that reference different request names each receive a separate GPU. Create a separate `ResourceClaimTemplate` for each time-slice interval you need, and one in each namespace where you want to share GPUs.

 *System-mediated* time-slicing is when the driver shares a GPU across independent claims (including across namespaces) based on criteria the system defines rather than a claim you configure. For more information about system-mediated time-slicing, see [System-mediated time-slicing of GPUs (issue \#659)](https://github.com/kubernetes-sigs/dra-driver-nvidia-gpu/issues/659) and [pull request \#1257](https://github.com/kubernetes-sigs/dra-driver-nvidia-gpu/pull/1257) on GitHub.

**Important**  
Time-slicing through the DRA driver requires the `TimeSlicingSettings` feature gate, which is an alpha feature disabled by default. If you request the `TimeSlicing` sharing strategy without enabling this feature gate, the driver fails to prepare the device and the Pod stays in `ContainerCreating` with a `FailedPrepareDynamicResources` event that reports `error validating GPU config: unknown GPU sharing strategy: TimeSlicing`. Turn on the feature gate only if you accept the risks of using an alpha capability.

### Prerequisites
<a name="_prerequisites"></a>
+ An Amazon EKS cluster running Kubernetes version 1.34 or later. The NVIDIA DRA driver is supported with static capacity provisioning in Karpenter, EKS managed node groups, or self-managed nodes.
+ Nodes with NVIDIA GPU instance types using the EKS-optimized AL2023 NVIDIA AMI.
+ The NVIDIA DRA driver installed as described in [Install the NVIDIA DRA driver](device-management-nvidia-dra-device-plugin.md#eks-nvidia-dra-driver), with the `TimeSlicingSettings` feature gate enabled.

### Procedure
<a name="_procedure"></a>

1. Create a `ResourceClaim` that requests a GPU with the `TimeSlicing` sharing strategy. Multiple Pods that reference this claim share the same physical GPU.

   ```
   cat <<EOF | kubectl apply -f -
   apiVersion: resource.k8s.io/v1
   kind: ResourceClaim
   metadata:
     name: shared-timeslice-gpu
   spec:
     devices:
       requests:
       - name: gpu
         exactly:
           deviceClassName: gpu.nvidia.com
           count: 1
       config:
       - requests: ["gpu"]
         opaque:
           driver: gpu.nvidia.com
           parameters:
             apiVersion: resource.nvidia.com/v1beta1
             kind: GpuConfig
             sharing:
               strategy: TimeSlicing
               timeSlicingConfig:
                 interval: Long
   EOF
   ```

1. Deploy two or more Pods that reference the shared `ResourceClaim` by name. Each Pod references the claim through `resourceClaims` and `resources.claims`.

   ```
   cat <<EOF | kubectl apply -f -
   apiVersion: v1
   kind: Pod
   metadata:
     name: share-a
   spec:
     tolerations:
       - key: nvidia.com/gpu
         operator: Exists
         effect: NoSchedule
     containers:
       - name: cuda
         image: nvidia/cuda:12.6.0-base-ubuntu22.04
         command: ["nvidia-smi", "-L"]
         resources:
           claims:
           - name: gpu
     resourceClaims:
       - name: gpu
         resourceClaimName: shared-timeslice-gpu
     restartPolicy: OnFailure
   EOF
   ```

1. Verify that the Pods share the same physical GPU. Run `nvidia-smi -L` in each Pod and confirm they report the same GPU UUID.

   ```
   kubectl logs share-a
   ```

   An example output is as follows. A second Pod that references the same claim reports an identical `GPU` UUID, which confirms that both Pods share one physical GPU.

   ```
   GPU 0: NVIDIA L4 (UUID: GPU-b41973ee-5d0a-cde8-6287-12b53f861f02)
   ```

## Use GPU time-slicing on Bottlerocket nodes with the NVIDIA device plugin
<a name="eks-time-slicing-device-plugin-bottlerocket"></a>

On Bottlerocket, the EKS-optimized accelerated AMI includes the NVIDIA device plugin. You enable time-slicing through the `settings.kubelet-device-plugins.nvidia` settings, which Bottlerocket renders into the device plugin configuration when the node boots.

### Prerequisites
<a name="_prerequisites_2"></a>
+ An Amazon EKS cluster. The following procedure provisions NVIDIA GPU nodes with the EKS-optimized Bottlerocket NVIDIA AMI.
+ Karpenter installed and configured in your cluster, because the following procedure uses a Karpenter `EC2NodeClass` to supply the time-slicing settings in the Bottlerocket node user data. For more information, see the [Getting Started with Karpenter](https://karpenter.sh/docs/getting-started/getting-started-with-karpenter/) on the Karpenter website.
+  `kubectl` configured to communicate with your cluster, see [Install or update `kubectl`](install-kubectl.md#kubectl-install-update) for more information.

### Procedure
<a name="_procedure_2"></a>

Add the time-slicing settings to the Bottlerocket user data for your GPU nodes. The following example configures four slots per GPU. The way you supply user data depends on how you provision nodes. The following example shows a Karpenter `EC2NodeClass`.

```
cat <<EOF | kubectl apply -f -
apiVersion: karpenter.k8s.aws/v1
kind: EC2NodeClass
metadata:
  name: gpu-bottlerocket-timeslicing
spec:
  amiFamily: Bottlerocket
  amiSelectorTerms:
    - alias: bottlerocket@latest
  role: eksctl-KarpenterNodeRole-<cluster-name>
  subnetSelectorTerms:
    - tags:
        karpenter.sh/discovery: <cluster-name>
  securityGroupSelectorTerms:
    - tags:
        karpenter.sh/discovery: <cluster-name>
  userData: |
    [settings.kubelet-device-plugins.nvidia]
    device-sharing-strategy = "time-slicing"

    [settings.kubelet-device-plugins.nvidia.time-slicing]
    replicas = 4
    rename-by-default = false
    fail-requests-greater-than-one = true
EOF
```

When nodes provisioned with these settings join the cluster, the device plugin advertises four `nvidia.com/gpu` slots for each physical GPU. You request them in your workload specification with container resources requests or limits for the `nvidia.com/gpu` extended resource.

## Use GPU time-slicing on AL2023 nodes with the NVIDIA device plugin
<a name="eks-time-slicing-device-plugin-al2023"></a>

On AL2023, you install the NVIDIA device plugin as described in [Install the NVIDIA Kubernetes device plugin](device-management-nvidia-dra-device-plugin.md#eks-nvidia-device-plugin), and supply the time-slicing configuration in a `ConfigMap`.

### Prerequisites
<a name="_prerequisites_3"></a>
+ An Amazon EKS cluster with nodes that use NVIDIA GPU instance types and the EKS-optimized AL2023 NVIDIA AMI.
+ Helm installed in your command-line environment, see the [Setup Helm instructions](helm.md) for more information.
+  `kubectl` configured to communicate with your cluster, see [Install or update `kubectl`](install-kubectl.md#kubectl-install-update) for more information.

### Procedure
<a name="_procedure_3"></a>

1. Create the time-slicing `ConfigMap` in the `nvidia` namespace, where you installed the device plugin in [Install the NVIDIA Kubernetes device plugin](device-management-nvidia-dra-device-plugin.md#eks-nvidia-device-plugin). This example configures four slots per GPU.

   ```
   cat <<EOF | kubectl apply -f -
   apiVersion: v1
   kind: ConfigMap
   metadata:
     name: nvidia-device-plugin-config
     namespace: nvidia
   data:
     config.yaml: |
       version: v1
       sharing:
         timeSlicing:
           renameByDefault: false
           failRequestsGreaterThanOne: true
           resources:
             - name: nvidia.com/gpu
               replicas: 4
   EOF
   ```

1. Update the existing NVIDIA device plugin release to reference the `ConfigMap` with the `config.name` value. The `--reuse-values` flag preserves the values you set when you installed the device plugin in [Install the NVIDIA Kubernetes device plugin](device-management-nvidia-dra-device-plugin.md#eks-nvidia-device-plugin).

   ```
   helm upgrade nvdp nvdp/nvidia-device-plugin \
       --namespace nvidia \
       --reuse-values \
       --set config.name=nvidia-device-plugin-config
   ```

**Note**  
The device plugin does not reload automatically when you change the `ConfigMap`. After you update the time-slicing configuration, restart the device plugin Pods to apply the change.

## Verify that GPU time-slicing is active
<a name="verify-eks-time-slicing"></a>

After your time-sliced nodes are `Ready`, confirm that the device plugin advertises the expected number of slots and that Pods share a physical GPU.

**Note**  
The shared-UUID check in this procedure demonstrates time-slicing most clearly when the Pods land on the same physical GPU. On a node with a single GPU, the device plugin advertises four slots and all four Pods share that GPU, so they report the same UUID. On a node with multiple physical GPUs, the scheduler can place Pods on different GPUs. Those Pods report different UUIDs even though time-slicing is active. To demonstrate sharing on one GPU, schedule the workload onto a single-GPU instance type. For example, add a node selector such as `node.kubernetes.io/instance-type: g6.2xlarge` to the Pod specification.

1. Confirm that the node advertises the configured number of GPU slots. With four slots per GPU, a node with one physical GPU reports `4`.

   ```
   kubectl get nodes "-o=custom-columns=NAME:.metadata.name,GPU:.status.allocatable.nvidia\.com/gpu"
   ```

   An example output is as follows.

   ```
   NAME                                           GPU
   ip-192-168-11-225.us-west-2.compute.internal   4
   ```

1. Create a deployment that runs four replicas, each requesting one GPU slot.

   ```
   cat <<EOF | kubectl apply -f -
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: timeslicing-demo
   spec:
     replicas: 4
     selector:
       matchLabels:
         app: timeslicing-demo
     template:
       metadata:
         labels:
           app: timeslicing-demo
       spec:
         tolerations:
           - key: nvidia.com/gpu
             operator: Exists
             effect: NoSchedule
         containers:
           - name: cuda
             image: nvidia/cuda:12.6.0-base-ubuntu22.04
             command: ["bash", "-c", "nvidia-smi --query-gpu=uuid --format=csv,noheader; sleep infinity"]
             resources:
               limits:
                 nvidia.com/gpu: 1
   EOF
   ```

1. Confirm that all four Pods are scheduled on the same node.

   ```
   kubectl get pods -l app=timeslicing-demo -o wide
   ```

1. Confirm that all four Pods report the same GPU UUID. A single shared UUID across all four Pods confirms that one physical GPU is being time-multiplexed.

   ```
   kubectl logs -l app=timeslicing-demo --prefix
   ```

   An example output is as follows.

   ```
   [pod/timeslicing-demo-xxxxxxxxxx-aaaaa/cuda] GPU-c0583cce-87c5-c736-db7f-6d3128c84d03
   [pod/timeslicing-demo-xxxxxxxxxx-bbbbb/cuda] GPU-c0583cce-87c5-c736-db7f-6d3128c84d03
   [pod/timeslicing-demo-xxxxxxxxxx-ccccc/cuda] GPU-c0583cce-87c5-c736-db7f-6d3128c84d03
   [pod/timeslicing-demo-xxxxxxxxxx-ddddd/cuda] GPU-c0583cce-87c5-c736-db7f-6d3128c84d03
   ```