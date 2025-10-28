**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Run critical add-ons on dedicated instances

In this topic, you will learn how to deploy a workload with a `CriticalAddonsOnly` toleration so EKS Auto Mode will schedule it onto the `system` node pool.

EKS Auto Mode’s built-in `system` node pool is designed for running critical add-ons on dedicated instances. This segregation ensures essential components have dedicated resources and are isolated from general workloads, enhancing overall cluster stability and performance.

This guide demonstrates how to deploy add-ons to the `system` node pool by utilizing the `CriticalAddonsOnly` toleration and appropriate node selectors. By following these steps, you can ensure that your critical applications are scheduled onto the dedicated `system` nodes, leveraging the isolation and resource allocation benefits provided by EKS Auto Mode’s specialized node pool structure.

EKS Auto Mode has two built-in node pools: `general-purpose` and `system`. For more information, see [Enable or Disable Built-in NodePools](set-builtin-node-pools.md "set-builtin-node-pools.md").

The purpose of the `system` node pool is to segregate critical add-ons onto different nodes. Nodes provisioned by the `system` node pool have a `CriticalAddonsOnly` Kubernetes taint. Kubernetes will only schedule pods onto these nodes if they have a corresponding toleration. For more information, see [Taints and Tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/ "https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/") in the Kubernetes documentation.

## Prerequisites

- EKS Auto Mode Cluster with the built-in `system` node pool enabled. For more information, see [Enable or Disable Built-in NodePools](set-builtin-node-pools.md "set-builtin-node-pools.md")
- `kubectl` installed and configured. For more information, see [Set up to use Amazon EKS](setting-up.md "setting-up.md").

## Procedure

Review the example yaml below. Note the following configurations:

- `nodeSelector` — This associates the workload with the built-in `system` node pool. This node pool must be enabled with the AWS API. For more information, see [Enable or Disable Built-in NodePools](set-builtin-node-pools.md "set-builtin-node-pools.md").
- `tolerations` — This toleration overcomes the `CriticalAddonsOnly` taint on nodes in the `system` node pool.

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: sample-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: sample-app
  template:
    metadata:
      labels:
        app: sample-app
    spec:
      nodeSelector:
        karpenter.sh/nodepool: system
      tolerations:
      - key: "CriticalAddonsOnly"
        operator: "Exists"
      containers:
      - name: app
        image: nginx:latest
        resources:
          requests:
            cpu: "500m"
            memory: "512Mi"
```

To update a workload to run on the `system` node pool, you need to:

1. Update the existing workload to add the following configurations described above:
   - `nodeSelector`
   - `tolerations`

2. Deploy the updated workload to your cluster with `kubectl apply`

After updating the workload, it will run on dedicated nodes.
