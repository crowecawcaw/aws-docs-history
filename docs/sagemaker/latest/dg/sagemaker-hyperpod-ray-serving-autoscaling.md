

# Autoscaling serving capacity
<a name="sagemaker-hyperpod-ray-serving-autoscaling"></a>

Serving capacity scales at two levels on HyperPod. Ray Serve scales replicas inside the cluster to match request load, and managed Karpenter scales cluster nodes to hold those replicas. The two work together: replica autoscaling reacts first, and node autoscaling adds capacity when the existing nodes run out.

## Ray Serve replica autoscaling
<a name="sagemaker-hyperpod-ray-serving-autoscaling-replica"></a>

Ray Serve adjusts the number of replicas for a deployment based on request load. Set an autoscaling configuration on the deployment instead of a fixed replica count:

```
deployments:
  - name: Model
    autoscaling_config:
      min_replicas: 1
      max_replicas: 8
      target_ongoing_requests: 5
```

For replica autoscaling to add and remove worker pods, the Ray autoscaler must be turned on for the cluster. Set `enableInTreeAutoscaling: true` in the `RayCluster` spec, or in the `rayClusterConfig` of a `RayService`:

```
spec:
  enableInTreeAutoscaling: true
```

Without it, the deployment's `autoscaling_config` changes the target replica count, but KubeRay does not create the worker pods to meet it.

Replica autoscaling stays within the cluster's current node capacity. When Ray Serve needs more replicas than the nodes can hold, the pods stay pending until a node is available.

## Node autoscaling with managed Karpenter
<a name="sagemaker-hyperpod-ray-serving-autoscaling-node"></a>

Managed Karpenter on HyperPod adds nodes when Ray pods are pending and removes them when they are idle, so serving capacity follows demand without a fixed node pool. Spot Instances are supported for node capacity, which lowers cost for interruption-tolerant serving. For the setup and configuration, see [Autoscaling on SageMaker HyperPod EKS](sagemaker-hyperpod-eks-autoscaling.md).

## Using both together
<a name="sagemaker-hyperpod-ray-serving-autoscaling-both"></a>

Set replica autoscaling on the deployment and node autoscaling on the cluster. The two levels work together in a chain that responds to increasing request load:

1. **Ray Serve detects load increase.** The autoscaler observes that ongoing requests exceed `target_ongoing_requests` and decides to add another replica.

1. **KubeRay creates a new worker pod.** Ray Serve signals KubeRay to scale the worker group, and KubeRay creates a pod for the new replica.

1. **Pod stays pending if no capacity.** If the existing nodes cannot fit the new pod (insufficient GPU or memory), the pod enters `Pending` state.

1. **Managed Karpenter provisions a node.** HyperPod managed Karpenter detects the pending pod, selects an appropriate instance type, and launches a new node.

1. **Node comes up and pod starts running.** Once the node is ready and joins the cluster, Kubernetes schedules the pending pod onto it. The new replica loads the model and begins serving requests.

On scale-down, the process reverses: Ray Serve removes idle replicas, KubeRay deletes the worker pods, and managed Karpenter terminates nodes that have no running pods after the consolidation window.