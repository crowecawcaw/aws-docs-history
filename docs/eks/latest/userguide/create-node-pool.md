**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Create a Node Pool for EKS Auto Mode

Amazon EKS node pools offer a flexible way to manage compute resources in your Kubernetes cluster. This topic demonstrates how to create and configure node pools by using Karpenter, a node provisioning tool that helps optimize cluster scaling and resource utilization. With Karpenter’s NodePool resource, you can define specific requirements for your compute resources, including instance types, availability zones, architectures, and capacity types.

You cannot modify the built-in `system` and `general-purpose` node pools. You can only enable or disable them. For more information, see [Enable or Disable Built-in NodePools](set-builtin-node-pools.md "set-builtin-node-pools.md").

The NodePool specification allows for fine-grained control over your EKS cluster’s compute resources through various supported labels and requirements. These include options for specifying EC2 instance categories, CPU configurations, availability zones, architectures (ARM64/AMD64), and capacity types (spot or on-demand). You can also set resource limits for CPU and memory usage, ensuring your cluster stays within required operational boundaries.

EKS Auto Mode leverages well-known Kubernetes labels to provide consistent and standardized ways of identifying node characteristics. These labels, such as `topology.kubernetes.io/zone` for availability zones and `kubernetes.io/arch` for CPU architecture, follow established Kubernetes conventions. Additionally, EKS-specific labels (prefixed with `eks.amazonaws.com/`) extend this functionality with AWS-specific attributes such as instance types, CPU manufacturers, GPU capabilities, and networking specifications. This standardized labeling system enables seamless integration with existing Kubernetes tools while providing deep AWS infrastructure integration.

## Create a NodePool

Follow these steps to create a NodePool for your Amazon EKS cluster:

1. Create a YAML file named `nodepool.yaml` with your required NodePool configuration. You can use the sample configuration below.
2. Apply the NodePool to your cluster:

```
kubectl apply -f nodepool.yaml
```

3. Verify that the NodePool was created successfully:

```
kubectl get nodepools
```

4. (Optional) Monitor the NodePool status:

```
kubectl describe nodepool default
```

Ensure that your NodePool references a valid NodeClass that exists in your cluster. The NodeClass defines AWS-specific configurations for your compute resources. For more information, see [Create a Node Class for Amazon EKS](create-node-class.md "create-node-class.md").

## Sample NodePool

```
apiVersion: karpenter.sh/v1
kind: NodePool
metadata:
  name: my-node-pool
spec:
  template:
    metadata:
      labels:
        billing-team: my-team
    spec:
      nodeClassRef:
        group: eks.amazonaws.com
        kind: NodeClass
        name: default

      requirements:
        - key: "eks.amazonaws.com/instance-category"
          operator: In
          values: ["c", "m", "r"]
        - key: "eks.amazonaws.com/instance-cpu"
          operator: In
          values: ["4", "8", "16", "32"]
        - key: "topology.kubernetes.io/zone"
          operator: In
          values: ["us-west-2a", "us-west-2b"]
        - key: "kubernetes.io/arch"
          operator: In
          values: ["arm64", "amd64"]

  limits:
    cpu: "1000"
    memory: 1000Gi
```

## EKS Auto Mode Supported Labels

EKS Auto Mode supports the following well known labels.

###### Note

EKS Auto Mode uses different labels than Karpenter. Labels related to EC2 managed instances start with `eks.amazonaws.com`.

| Label                                                      | Example      | Description                                                                                                                                                                                                                    |
| ---------------------------------------------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| topology.kubernetes.io/zone                                | us-east-2a   | AWS region                                                                                                                                                                                                                     |
| node.kubernetes.io/instance-type                           | g4dn.8xlarge | AWS instance type                                                                                                                                                                                                              |
| kubernetes.io/arch                                         | amd64        | Architectures are defined by [GOARCH values](https://github.com/golang/go/blob/master/src/internal/syslist/syslist.go#L58 "https://github.com/golang/go/blob/master/src/internal/syslist/syslist.go#L58") on the instance      |
| karpenter.sh/capacity-type                                 | spot         | Capacity types include `spot`, `on-demand`                                                                                                                                                                                     |
| eks.amazonaws.com/instance-hypervisor                      | nitro        | Instance types that use a specific hypervisor                                                                                                                                                                                  |
| eks.amazonaws.com/compute-type                             | auto         | Identifies EKS Auto Mode managed nodes                                                                                                                                                                                         |
| eks.amazonaws.com/instance-encryption-in-transit-supported | true         | Instance types that support (or not) in-transit encryption                                                                                                                                                                     |
| eks.amazonaws.com/instance-category                        | g            | Instance types of the same category, usually the string before the generation number                                                                                                                                           |
| eks.amazonaws.com/instance-generation                      | 4            | Instance type generation number within an instance category                                                                                                                                                                    |
| eks.amazonaws.com/instance-family                          | g4dn         | Instance types of similar properties but different resource quantities                                                                                                                                                         |
| eks.amazonaws.com/instance-size                            | 8xlarge      | Instance types of similar resource quantities but different properties                                                                                                                                                         |
| eks.amazonaws.com/instance-cpu                             | 32           | Number of CPUs on the instance                                                                                                                                                                                                 |
| eks.amazonaws.com/instance-cpu-manufacturer                | `aws`        | Name of the CPU manufacturer                                                                                                                                                                                                   |
| eks.amazonaws.com/instance-memory                          | 131072       | Number of mebibytes of memory on the instance                                                                                                                                                                                  |
| eks.amazonaws.com/instance-ebs-bandwidth                   | 9500         | Number of [maximum megabits](../../../AWSEC2/latest/UserGuide/ebs-optimized.md#ebs-optimization-performance "../../../AWSEC2/latest/UserGuide/ebs-optimized.md#ebs-optimization-performance") of EBS available on the instance |
| eks.amazonaws.com/instance-network-bandwidth               | 131072       | Number of [baseline megabits](../../../AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.md "../../../AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.md") available on the instance                               |
| eks.amazonaws.com/instance-gpu-name                        | t4           | Name of the GPU on the instance, if available                                                                                                                                                                                  |
| eks.amazonaws.com/instance-gpu-manufacturer                | nvidia       | Name of the GPU manufacturer                                                                                                                                                                                                   |
| eks.amazonaws.com/instance-gpu-count                       | 1            | Number of GPUs on the instance                                                                                                                                                                                                 |
| eks.amazonaws.com/instance-gpu-memory                      | 16384        | Number of mebibytes of memory on the GPU                                                                                                                                                                                       |
| eks.amazonaws.com/instance-local-nvme                      | 900          | Number of gibibytes of local nvme storage on the instance                                                                                                                                                                      | ###### Note EKS Auto Mode only supports certain instances, and has minimum size requirements. For more information, see [EKS Auto Mode supported instance reference](automode-learn-instances.md#auto-supported-instances "automode-learn-instances.md#auto-supported-instances"). ## EKS Auto Mode Not Supported Labels EKS Auto Mode does not support the following labels. <br>• EKS Auto Mode only supports Linux + `node.kubernetes.io/windows-build` + `kubernetes.io/os` ## Disable built-in node pools If you create custom node pools, you can disable the built-in node pools. For more information, see [Enable or Disable Built-in NodePools](set-builtin-node-pools.md "set-builtin-node-pools.md"). ## Cluster without built-in node pools You can create a cluster without the built-in node pools. This is helpful when your organization has created customized node pools. ###### Note When you create a cluster without built-in node pools, the `default` NodeClass is not automatically provisioned. You’ll need to create a custom NodeClass. For more information, see [Create a Node Class for Amazon EKS](create-node-class.md "create-node-class.md"). **Overview:** 1. Create an EKS cluster with the both `nodePools` and `nodeRoleArn` values empty. <br>• Sample eksctl `autoModeConfig`: `autoModeConfig: enabled: true nodePools: [] # Do not set a nodeRoleARN` For more information, see [Create an EKS Auto Mode Cluster with the eksctl CLI](automode-get-started-eksctl.md "automode-get-started-eksctl.md") 2. Create a custom node class with a node role ARN <br>• For more information, see [Create a Node Class for Amazon EKS](create-node-class.md "create-node-class.md") 3. Create an access entry for the custom node class <br>• For more information, see [Create node class access entry](create-node-class.md#auto-node-access-entry "create-node-class.md#auto-node-access-entry") 4. Create a custom node pool, as described above. ## Disruption You can configure EKS Auto Mode to disrupt Nodes through your NodePool in multiple ways. You can use `spec.disruption.consolidationPolicy`, `spec.disruption.consolidateAfter`, or `spec.template.spec.expireAfter`. You can also rate limit EKS Auto Mode’s disruption through the NodePool’s `spec.disruption.budgets`. You can also control the time windows and number of simultaneous Nodes disrupted. For instructions on configuring this behavior, see [Disruption](https://karpenter.sh/docs/concepts/disruption/ "https://karpenter.sh/docs/concepts/disruption/") in the Karpenter Documentation. You can configure disruption for node pools to: <br>• Identify when instances are underutilized, and consolidate workloads. <br>• Create a node pool disruption budget to rate limit node terminations due to drift, emptiness, and consolidation. By default, EKS Auto Mode: <br>• Consolidates underutilized instances. <br>• Terminates instances after 336 hours. <br>• Sets a single disruption budget of 10% of nodes. <br>• Allows Nodes to be replaced due to drift when a new Auto Mode AMI is released, which occurs roughly once per week. ## Termination Grace Period When a `terminationGracePeriod` is not explicitly defined on an EKS Auto NodePool, the system automatically applies a default 24-hour termination grace period to the associated NodeClaim. While EKS Auto customers will not see a `terminationGracePeriod` defaulted in their custom NodePool configurations, they will observe this default value on the NodeClaim. The functionality remains consistent whether the grace period is explicitly set on the NodePool or defaulted on the NodeClaim, ensuring predictable node termination behavior across the cluster. |
