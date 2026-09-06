

# Scaling a development cluster
<a name="sagemaker-hyperpod-ray-scaling-dev-cluster"></a>

You scale a Ray cluster by changing the worker count directly, or by turning on autoscaling so Ray adds and removes workers with load.

## Set a fixed worker count
<a name="sagemaker-hyperpod-ray-scaling-dev-cluster-fixed"></a>

In Studio, edit the cluster and change the replica count for a worker group. In a manifest, set `replicas` on the worker group.

```
workerGroupSpecs:
  - groupName: {{my-workers}}
    replicas: 4
```

## Turn on autoscaling
<a name="sagemaker-hyperpod-ray-scaling-dev-cluster-autoscaling"></a>

Turn on the autoscaling toggle when you edit the cluster in Studio, then set a minimum and maximum for each worker group. In a manifest, set `enableInTreeAutoscaling: true` and the per-group bounds.

```
spec:
  enableInTreeAutoscaling: true
  workerGroupSpecs:
    - groupName: {{my-workers}}
      minReplicas: 1
      maxReplicas: 8
```

Ray scales each worker group between its minimum and maximum based on pending tasks. The minimum sets the idle footprint, and the maximum caps cost.