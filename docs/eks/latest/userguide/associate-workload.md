

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Control if a workload is deployed on EKS Auto Mode nodes
<a name="associate-workload"></a>

When running workloads in an EKS cluster with EKS Auto Mode, you might need to control whether specific workloads run on EKS Auto Mode nodes or other compute types. This topic describes how to use node selectors and affinity rules to ensure your workloads are scheduled on the intended compute infrastructure.

The examples in this topic demonstrate how to use the `eks.amazonaws.com/compute-type` label to either require or prevent workload deployment on EKS Auto Mode nodes. This is particularly useful in mixed-mode clusters where you’re running both EKS Auto Mode and other compute types, such as self-managed Karpenter provisioners or EKS Managed Node Groups.

EKS Auto Mode nodes have set the value of the label `eks.amazonaws.com/compute-type` to `auto`. You can use this label to control if a workload is deployed to nodes managed by EKS Auto Mode.

## Require that a workload is deployed to EKS Auto Mode nodes
<a name="_require_that_a_workload_is_deployed_to_eks_auto_mode_nodes"></a>

**Note**  
This `nodeSelector` value is not required for EKS Auto Mode. This `nodeSelector` value is only relevant if you are running a cluster in a mixed mode, node types not managed by EKS Auto Mode. For example, you may have static compute capacity deployed to your cluster with EKS Managed Node Groups, and have dynamic compute capacity managed by EKS Auto Mode.

You can add this `nodeSelector` to Deployments or other workloads to require Kubernetes schedule them onto EKS Auto Mode nodes.

```
apiVersion: apps/v1
kind: Deployment
spec:
  template:
    spec:
      nodeSelector:
        eks.amazonaws.com/compute-type: auto
```

## Require that a workload is not deployed to EKS Auto Mode nodes
<a name="_require_that_a_workload_is_not_deployed_to_eks_auto_mode_nodes"></a>

You can add this `nodeAffinity` to Deployments or other workloads to require Kubernetes **not** schedule them onto EKS Auto Mode nodes.

```
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: eks.amazonaws.com/compute-type
            operator: NotIn
            values:
            - auto
```

## Target a specific NodePool
<a name="_target_a_specific_nodepool"></a>

An Amazon EKS Auto Mode cluster can have more than one NodePool. You might want a workload to run only on nodes from a particular NodePool. To accomplish this, workloads can match on either of the following labels:
+  **A custom label that you define on the NodePool.** When you add labels under `spec.template.metadata.labels` in a NodePool, Amazon EKS Auto Mode applies those labels to every node that the NodePool provisions. Custom labels are the recommended approach. A custom label ties the workload to a capability, such as `workload-class: gpu-inference`, instead of to a specific NodePool name.
+  **The well-known `karpenter.sh/nodepool` label.** Amazon EKS Auto Mode applies this label to every node it provisions, using the name of the NodePool as the value. Use this label when you have not defined a custom label and want to target a NodePool by name.

### Target a custom NodePool label
<a name="_target_a_custom_nodepool_label"></a>

First, define a label on the NodePool.

```
apiVersion: karpenter.sh/v1
kind: NodePool
metadata:
  name: gpu
spec:
  template:
    metadata:
      labels:
        workload-class: gpu-inference
```

For more information about NodePool configuration, see [Create a Node Pool for EKS Auto Mode](create-node-pool.md).

Next, match that label from the workload.

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: inference
spec:
  template:
    spec:
      nodeSelector:
        workload-class: gpu-inference
```

Pods from this Deployment schedule only onto nodes that the `gpu` NodePool provisions. Workloads without this `nodeSelector` continue to run on the default NodePool.

### Target a NodePool by name
<a name="_target_a_nodepool_by_name"></a>

**NodePool name changes affect scheduling**  
Pinning a workload by name can leave pods in the `Pending` state if you rename or delete the target NodePool. Use a custom capability label for any workload that you expect to outlive a single NodePool definition.

```
apiVersion: apps/v1
kind: Deployment
spec:
  template:
    spec:
      nodeSelector:
        karpenter.sh/nodepool: <your-nodepool-name>
```

For more information about how Karpenter matches pods to NodePools, see [Scheduling](https://karpenter.sh/docs/concepts/scheduling/) in the Karpenter documentation.