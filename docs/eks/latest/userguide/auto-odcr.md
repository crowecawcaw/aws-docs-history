**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Control deployment of workloads into Capacity Reservations with EKS Auto Mode

You can control the deployment of workloads onto [Capacity Reservations](../../../AWSEC2/latest/UserGuide/capacity-reservation-overview.md "../../../AWSEC2/latest/UserGuide/capacity-reservation-overview.md"). EKS Auto Mode supports EC2 On-Demand Capacity Reservations (ODCRs), and EC2 Capacity Blocks for ML.

###### Tip

By default, EKS Auto Mode automatically launches into open ODCRs and ML Capacity Blocks. When using `capacityReservationSelectorTerms` in the NodeClass definition, EKS Auto Mode will no longer automatically use any open Capacity Reservations.

## EC2 On-Demand Capacity Reservations (ODCRs)

EC2 On-Demand Capacity Reservations (ODCRs) allow you to reserve compute capacity for your Amazon EC2 instances in a specific Availability Zone for any duration. When using EKS Auto Mode, you may want to control whether your Kubernetes workloads are deployed onto these reserved instances to maximize utilization of pre-purchased capacity or to ensure critical workloads have access to guaranteed resources.

By default, EKS Auto Mode automatically launches into open ODCRs. However, by configuring `capacityReservationSelectorTerms` on a NodeClass, you can explicitly control which ODCRs your workloads use. Nodes provisioned using configured ODCRs will have `karpenter.sh/capacity-type: reserved` and will be prioritized over on-demand and spot. Once this feature is enabled, EKS Auto Mode will no longer automatically use open ODCRs—they must be explicitly selected by a NodeClass, giving you precise control over capacity reservation usage across your cluster.

###### Warning

If you configure `capacityReservationSelectorTerms` on a NodeClass in a cluster, EKS Auto Mode will no longer automatically use open ODCRs for _any_ NodeClass in the cluster.

### Example NodeClass

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

## EC2 Capacity Blocks for ML

Capacity Blocks for ML reserve GPU-based accelerated computing instances on a future date to support your short duration machine learning (ML) workloads. Instances that run inside a Capacity Block are automatically placed close together inside Amazon EC2 UltraClusters, for low-latency, petabit-scale, non-blocking networking.

For more information about the supported platforms and instance types, see [Capacity Blocks for ML](../../../AWSEC2/latest/UserGuide/ec2-capacity-blocks.md "../../../AWSEC2/latest/UserGuide/ec2-capacity-blocks.md") in the EC2 User Guide.

You can create an EKS Auto Mode NodeClass that uses a Capacity Block for ML, similar to an ODCR (described earlier).

The following sample definitions create three resources:

1. A NodeClass that references your Capacity Block reservation
2. A NodePool that uses the NodeClass and applies a taint
3. A Pod specification that tolerates the taint and requests GPU resources

### Example NodeClass

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

For more information, see [Create a Node Class for Amazon EKS](create-node-class.md "create-node-class.md").

### Example NodePool

This NodePool references the `gpu` NodeClass and specifies important configuration:

- It **only** uses reserved capacity by setting `karpenter.sh/capacity-type: reserved`
- It requests specific GPU instance families appropriate for ML workloads
- It applies a `nvidia.com/gpu` taint to ensure only GPU workloads are scheduled on these nodes

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

For more information, see [Create a Node Pool for EKS Auto Mode](create-node-pool.md "create-node-pool.md").

### Example Pod

This example pod demonstrates how to configure a workload to run on your Capacity Block nodes:

- It uses a **nodeSelector** to target specific GPU types (in this case, H200 GPUs)
- It includes a **toleration** for the `nvidia.com/gpu` taint applied by the NodePool
- It explicitly **requests GPU resources** using the `nvidia.com/gpu` resource type

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

For more information, see [Pods](https://kubernetes.io/docs/concepts/workloads/pods/ "https://kubernetes.io/docs/concepts/workloads/pods/") in the Kubernetes documentation.

### Related Resources

- [Capacity Blocks for ML](../../../AWSEC2/latest/UserGuide/ec2-capacity-blocks.md "../../../AWSEC2/latest/UserGuide/ec2-capacity-blocks.md") in the Amazon EC2 User Guide
- [Find and purchase Capacity Blocks](../../../AWSEC2/latest/UserGuide/capacity-blocks-purchase.md "../../../AWSEC2/latest/UserGuide/capacity-blocks-purchase.md") in the Amazon EC2 User Guide
- [Manage compute resources for AI/ML workloads on Amazon EKS](ml-compute-management.md "ml-compute-management.md")
- [GPU Resource Optimization and Cost Management](../best-practices/aiml-compute.md#_gpu_resource_optimization_and_cost_management "../best-practices/aiml-compute.md#_gpu_resource_optimization_and_cost_management") in the EKS Best Practices Guide
