

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Control deployment of workloads into Capacity Reservations with EKS Auto Mode
<a name="auto-odcr"></a>

You can control the deployment of workloads onto [Capacity Reservations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-reservation-overview.html). EKS Auto Mode supports EC2 On-Demand Capacity Reservations (ODCRs), EC2 Capacity Blocks for ML, and Interruptible Capacity Reservations (IODCRs).

**Tip**  
By default, EKS Auto Mode can launch into open ODCRs through open-matching, but does not prioritize them. Instances launched through open-matching are labeled `karpenter.sh/capacity-type: on-demand`, not `reserved`. To prioritize ODCR usage and have instances labeled `karpenter.sh/capacity-type: reserved`, configure `capacityReservationSelectorTerms` in the NodeClass definition. Capacity Blocks for ML always require `capacityReservationSelectorTerms` and are not used automatically.

## EC2 On-Demand Capacity Reservations (ODCRs)
<a name="_ec2_on_demand_capacity_reservations_odcrs"></a>

EC2 On-Demand Capacity Reservations (ODCRs) allow you to reserve compute capacity for your Amazon EC2 instances in a specific Availability Zone for any duration. When using EKS Auto Mode, you may want to control whether your Kubernetes workloads are deployed onto these reserved instances to maximize utilization of pre-purchased capacity or to ensure critical workloads have access to guaranteed resources.

By default, EKS Auto Mode automatically launches into open ODCRs. However, by configuring `capacityReservationSelectorTerms` on a NodeClass, you can explicitly control which ODCRs your workloads use. Nodes provisioned using configured ODCRs will have `karpenter.sh/capacity-type: reserved` and will be prioritized over on-demand and spot. Once this feature is enabled, EKS Auto Mode will no longer automatically use open ODCRs—they must be explicitly selected by a NodeClass, giving you precise control over capacity reservation usage across your cluster.

**Warning**  
If you configure `capacityReservationSelectorTerms` on a NodeClass in a cluster, EKS Auto Mode will no longer automatically use open ODCRs for *any* NodeClass in the cluster.

### Example NodeClass
<a name="_example_nodeclass"></a>

```
apiVersion: eks.amazonaws.com/v1
kind: NodeClass
spec:
  # Optional: Selects upon on-demand capacity reservations and capacity blocks
  # for EKS Auto Mode to prioritize.
  capacityReservationSelectorTerms:
    - id: cr-56fac701cc1951b03
    # Alternative Approaches
    - tags:
        app: "my-app"
      # Optional owning account ID filter
      owner: "012345678901"
```

This example NodeClass demonstrates two approaches for selecting ODCRs. The first method directly references a specific ODCR by its ID (`cr-56fac701cc1951b03`). The second method uses tag-based selection, targeting ODCRs with the tag `Name: "targeted-odcr"`. You can also optionally filter by the AWS account that owns the reservation, which is particularly useful in cross-account scenarios or when working with shared capacity reservations.

## Scheduling labels for Capacity Reservations
<a name="_scheduling_labels_for_capacity_reservations"></a>

When you configure `capacityReservationSelectorTerms` on a NodeClass, nodes provisioned from capacity reservations are labeled with additional scheduling labels. You can use these labels as NodePool requirements or pod scheduling constraints (such as node affinity) to control workload placement.


| Label | Example | Description | 
| --- | --- | --- | 
|  `eks.amazonaws.com/capacity-reservation-id`  |  `cr-56fac701cc1951b03`  | The capacity reservation’s ID | 
|  `eks.amazonaws.com/capacity-reservation-type`  |  `default` or `capacity-block`  | The type of capacity reservation | 
|  `eks.amazonaws.com/capacity-reservation-interruptible`  |  `true` or `false`  | Whether the capacity reservation is interruptible | 

These labels are only present on nodes with `karpenter.sh/capacity-type: reserved`.

## Interruptible Capacity Reservations (IODCRs)
<a name="_interruptible_capacity_reservations_iodcrs"></a>

 [Interruptible Capacity Reservations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/interruptible-capacity-reservations.html) allow you to share unused On-Demand Capacity Reservation capacity with other workloads within your organization. By repurposing unused capacity as interruptible ODCRs, workloads suitable for flexible, fault-tolerant operations, such as batch processing and data analysis, can benefit from temporarily available capacity. Reservation owners can reclaim their capacity at any time, while consumers of interruptible ODCRs will receive an interruption notice before termination to allow for graceful shutdown or checkpointing before the node is terminated.

You select interruptible capacity reservations using `capacityReservationSelectorTerms` the same way you would a standard ODCR—by ID or by tags. To control whether workloads are scheduled on interruptible versus non-interruptible reserved capacity, use the `eks.amazonaws.com/capacity-reservation-interruptible` scheduling label.

When capacity is reclaimed, running instances receive a 2-minute interruption warning through EventBridge events. After the notice period, running instances in the reclaimed capacity enter a shutting down state and are terminated. EKS Auto Mode will automatically begin draining nodes launched from interruptible capacity reservations when the 2-minute interruption warning is received, enabling your workloads to gracefully terminate before the node is reclaimed.

## EC2 Capacity Blocks for ML
<a name="_ec2_capacity_blocks_for_ml"></a>

Capacity Blocks for ML reserve GPU-based accelerated computing instances on a future date to support your short duration machine learning (ML) workloads. Instances that run inside a Capacity Block are automatically placed close together inside Amazon EC2 UltraClusters, for low-latency, petabit-scale, non-blocking networking.

For more information about the supported platforms and instance types, see [Capacity Blocks for ML](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-blocks.html) in the EC2 User Guide.

You can create an EKS Auto Mode NodeClass that uses a Capacity Block for ML, similar to an ODCR (described earlier).

The following sample definitions create three resources:

1. A NodeClass that references your Capacity Block reservation

1. A NodePool that uses the NodeClass and applies a taint

1. A Pod specification that tolerates the taint and requests GPU resources

### Example NodeClass
<a name="_example_nodeclass_2"></a>

This NodeClass references a specific Capacity Block for ML by its reservation ID. You can obtain this ID from the EC2 console.

```
apiVersion: eks.amazonaws.com/v1
kind: NodeClass
metadata:
  name: gpu
spec:
  # Specify your Capacity Block reservation ID
  capacityReservationSelectorTerms:
    - id: cr-56fac701cc1951b03
```

For more information, see [Create a Node Class for Amazon EKS](create-node-class.md).

### Example NodePool
<a name="_example_nodepool"></a>

This NodePool references the `gpu` NodeClass and specifies important configuration:
+ It **only** uses reserved capacity by setting `karpenter.sh/capacity-type: reserved` 
+ It requests specific GPU instance families appropriate for ML workloads
+ It applies a `nvidia.com/gpu` taint to ensure only GPU workloads are scheduled on these nodes

```
apiVersion: karpenter.sh/v1
kind: NodePool
metadata:
  name: gpu
spec:
  template:
    spec:
      nodeClassRef:
        group: eks.amazonaws.com
        kind: NodeClass
        name: gpu
      requirements:
        - key: eks.amazonaws.com/instance-family
          operator: In
          values:
            - g6
            - p4d
            - p4de
            - p5
            - p5e
            - p5en
            - p6
            - p6-b200
        - key: karpenter.sh/capacity-type
          operator: In
          values:
            - reserved
            # Enable other capacity types
            # - on-demand
            # - spot
      taints:
        - effect: NoSchedule
          key: nvidia.com/gpu
```

For more information, see [Create a Node Pool for EKS Auto Mode](create-node-pool.md).

### Example Pod
<a name="_example_pod"></a>

This example pod demonstrates how to configure a workload to run on your Capacity Block nodes:
+ It uses a **nodeSelector** to target specific GPU types (in this case, H200 GPUs)
+ It includes a **toleration** for the `nvidia.com/gpu` taint applied by the NodePool
+ It explicitly **requests GPU resources** using the `nvidia.com/gpu` resource type

```
apiVersion: v1
kind: Pod
metadata:
  name: nvidia-smi
spec:
  nodeSelector:
    # Select specific GPU type - uncomment as needed
    # eks.amazonaws.com/instance-gpu-name: l4
    # eks.amazonaws.com/instance-gpu-name: a100
    eks.amazonaws.com/instance-gpu-name: h200
    # eks.amazonaws.com/instance-gpu-name: b200
    eks.amazonaws.com/compute-type: auto
  restartPolicy: OnFailure
  containers:
  - name: nvidia-smi
    image: public.ecr.aws/amazonlinux/amazonlinux:2023-minimal
    args:
    - "nvidia-smi"
    resources:
      requests:
        # Uncomment if needed
        # memory: "30Gi"
        # cpu: "3500m"
        nvidia.com/gpu: 1
      limits:
        # Uncomment if needed
        # memory: "30Gi"
        nvidia.com/gpu: 1
  tolerations:
  - key: nvidia.com/gpu
    effect: NoSchedule
    operator: Exists
```

For more information, see [Pods](https://kubernetes.io/docs/concepts/workloads/pods/) in the Kubernetes documentation.

### Related Resources
<a name="_related_resources"></a>
+  [Capacity Blocks for ML](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-blocks.html) in the Amazon EC2 User Guide
+  [Find and purchase Capacity Blocks](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-blocks-purchase.html) in the Amazon EC2 User Guide
+  [Interruptible Capacity Reservations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/interruptible-capacity-reservations.html) in the Amazon EC2 User Guide
+  [Manage compute resources for AI/ML workloads on Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/ml-compute-management.html) 
+  [GPU Resource Optimization and Cost Management](https://docs.aws.amazon.com/eks/latest/best-practices/aiml-compute.html#_gpu_resource_optimization_and_cost_management) in the EKS Best Practices Guide