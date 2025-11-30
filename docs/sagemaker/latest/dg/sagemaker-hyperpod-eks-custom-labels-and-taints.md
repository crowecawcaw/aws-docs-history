# Configuring custom Kubernetes labels and taints in Amazon SageMaker HyperPod

Amazon SageMaker HyperPod clusters with Amazon Elastic Kubernetes Service (Amazon EKS) orchestrator support custom Kubernetes labels and taints for nodes within instance groups. Labels and taints are fundamental scheduling and organization mechanisms in Kubernetes that give you fine-grained control over pod placement and resource utilization.

Labels are key-value pairs that can be attached to Kubernetes objects, allowing you to organize and select resources based on attributes. Taints, working in conjunction with tolerations, are node-specific properties that influence pod scheduling by repelling pods that don't have matching tolerations. Together, these mechanisms enable you to isolate workloads, assign them according to hardware specifications, and ensure optimal resource utilization.

## Common use cases

The following are common scenarios where custom labels and taints are beneficial:

- **Preventing system pods on expensive instances** - Apply taints to GPU instances to prevent system pods and other non-critical workloads from consuming expensive compute resources
- **Integration with existing tooling** - Apply labels that match your organization's established infrastructure patterns and node affinity configurations

## Configuring labels and taints

You can configure custom Kubernetes labels and taints at the instance group level using the `KubernetesConfig` parameter in your cluster configuration. Labels and taints are applied to all nodes in the instance group and persist throughout the cluster's lifecycle.

The `KubernetesConfig` parameter is declarative, meaning you specify the complete desired state of labels and taints for an instance group. SageMaker HyperPod then reconciles the actual state of the nodes to match this desired state.

- **Adding labels or taints** - Include the new labels or taints in the `KubernetesConfig` along with any existing ones you want to keep
- **Updating labels or taints** - Modify the values in the `KubernetesConfig` for the labels or taints you want to change, and include all others you want to keep
- **Removing labels or taints** - Omit the labels or taints you want to remove from the `KubernetesConfig`, keeping only those you want to retain

### Creating a cluster with labels and taints

When creating a new SageMaker HyperPod cluster, include the `KubernetesConfig` parameter in your instance group configuration. The following example shows how to create a cluster with custom labels and taints:

```
{
    "ClusterName": "my-cluster",
    "InstanceGroups": [{
        "InstanceGroupName": "worker-group-1",
        "InstanceType": "ml.p4d.24xlarge",
        "InstanceCount": 4,
        "LifeCycleConfig": {
            "SourceS3Uri": "s3://my-bucket/lifecycle-config.sh",
            "OnCreate": "on-create.sh"
        },
        "ExecutionRole": `"arn:aws:iam::123456789012:role/HyperPodExecutionRole"`,
        "ThreadsPerCore": 1,
        "KubernetesConfig": {
            "Labels": {
                "env": "prod",
                "team": "ml-training",
                "gpu-type": "a100"
            },
            "Taints": [{
                "key": "gpu",
                "value": "true",
                "effect": "NoSchedule"
            },
            {
                "key": "dedicated",
                "value": "ml-workloads",
                "effect": "NoExecute"
            }]
        }
    }],
    "VpcConfig": {
        "SecurityGroupIds": [`"sg-0123456789abcdef0"`],
        "Subnets": [`"subnet-0123456789abcdef0"`, `"subnet-0123456789abcdef1"`]
    },
    "Orchestrator": {
        "Eks": {
            "ClusterArn": `"arn:aws:eks:us-west-2:123456789012:cluster/my-eks-cluster"`
        }
    }
}
```

In this example:

- **Labels** - Three custom labels are applied: `env=prod`, `team=ml-training`, and `gpu-type=a100`
- **Taints** - Two taints are configured to prevent unwanted pod scheduling

### Updating labels and taints on an existing cluster

You can modify labels and taints on an existing cluster using the `UpdateCluster` API. The following example shows how to update the `KubernetesConfig` for an instance group:

```
{
    "ClusterName": "my-cluster",
    "InstanceGroups": [{
        "InstanceGroupName": "worker-group-1",
        "KubernetesConfig": {
            "Labels": {
                "env": "prod",
                "team": "ml-training",
                "gpu-type": "a100",
                "cost-center": "ml-ops"
            },
            "Taints": [{
                "key": "gpu",
                "value": "true",
                "effect": "NoSchedule"
            }]
        }
    }]
}
```

When you update labels and taints, SageMaker HyperPod applies the changes to all nodes in the instance group. The service manages the transition from current to desired state, which you can monitor using the `DescribeCluster` API.

## Monitoring label and taint application

SageMaker HyperPod provides APIs to monitor the status of labels and taints as they are applied to your cluster nodes.

### Checking cluster-level status

Use the `DescribeCluster` API to view the current and desired states of labels and taints at the instance group level. The following example shows the response structure:

```
{
    "ClusterName": "my-cluster",
    "ClusterStatus": "InService",
    "InstanceGroups": [{
        "InstanceGroupName": "worker-group-1",
        "InstanceType": "ml.p4d.24xlarge",
        "CurrentInstanceCount": 4,
        "TargetInstanceCount": 4,
        "KubernetesConfig": {
            "CurrentLabels": {
                "env": "prod",
                "team": "ml-training",
                "gpu-type": "a100"
            },
            "DesiredLabels": {
                "env": "prod",
                "team": "ml-training",
                "gpu-type": "a100"
            },
            "CurrentTaints": [{
                "key": "gpu",
                "value": "true",
                "effect": "NoSchedule"
            }],
            "DesiredTaints": [{
                "key": "gpu",
                "value": "true",
                "effect": "NoSchedule"
            }]
        }
    }]
}
```

When the `CurrentLabels` match `DesiredLabels` and `CurrentTaints` match `DesiredTaints`, all nodes in the instance group have the specified configuration applied. If they differ, the cluster is still in the process of applying the changes.

### Checking individual node status

For node-level details, use the `DescribeClusterNode` API to check the label and taint configuration of individual nodes. The following example shows the response structure:

```
{
    "NodeDetails": {
        "InstanceId": `"i-0123456789abcdef0"`,
        "InstanceGroupName": "worker-group-1",
        "InstanceType": "ml.p4d.24xlarge",
        "InstanceStatus": {
            "Status": "Running",
            "Message": "Node is healthy"
        },
        "LifeCycleConfig": {
            "SourceS3Uri": "s3://my-bucket/lifecycle-config.sh",
            "OnCreate": "on-create.sh"
        },
        "LaunchTime": 1699564800.0,
        "KubernetesConfig": {
            "CurrentLabels": {
                "env": "prod",
                "team": "ml-training",
                "gpu-type": "a100"
            },
            "DesiredLabels": {
                "env": "prod",
                "team": "ml-training",
                "gpu-type": "a100"
            },
            "CurrentTaints": [{
                "key": "gpu",
                "value": "true",
                "effect": "NoSchedule"
            }],
            "DesiredTaints": [{
                "key": "gpu",
                "value": "true",
                "effect": "NoSchedule"
            }]
        }
    }
}
```

Node-level monitoring is useful for troubleshooting when labels or taints are not applying correctly to specific nodes, or when you need to verify the configuration of a particular instance.

## Reserved prefixes

Certain prefixes are reserved for system use and should not be used for custom labels or taints. The following prefixes are reserved:

- `kubernetes.io/` - Reserved for Kubernetes core components
- `k8s.io/` - Reserved for Kubernetes core components
- `sagemaker.amazonaws.com/` - Reserved for SageMaker HyperPod
- `eks.amazonaws.com/` - Reserved for Amazon EKS
- `k8s.aws/` - Reserved for Amazon EKS
- `karpenter.sh/` - Reserved for Karpenter autoscaling

Labels and taints with these prefixes are managed by system components and should not be overwritten with custom values.
