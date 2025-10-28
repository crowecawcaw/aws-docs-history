# Deploy a workload

The following examples demonstrate how HyperPod autoscaling with Karpenter
automatically provisions nodes in response to workload demands. These examples show
basic scaling behavior and multi-availability zone distribution patterns.

###### Deploy a simple workload

1. The following Kubernetes deployment includes pods that request for 1 CPU and
   256M memory per replica or pod. In this scenario, the pods aren’t spun up
   yet.

```
kubectl apply -f https://raw.githubusercontent.com/aws/karpenter-provider-aws/refs/heads/main/examples/workloads/inflate.yaml
```

2. To test the scale up process, run the following command. Karpenter will add
   new nodes to the cluster.

```
kubectl scale deployment inflate --replicas 10
```

3. To test the scale down process, run the following command. Karpenter will
   remove nodes from the cluster.

```
kubectl scale deployment inflate --replicas 0
```

###### Deploy a workload across multiple AZs

1. Run the following command to deploy a workload that runs a Kubernetes
   deployment where the pods in deployment need to spread evenly across different
   availability zones with a max Skew of 1.

```
kubectl apply -f https://raw.githubusercontent.com/aws/karpenter-provider-aws/refs/heads/main/examples/workloads/spread-zone.yaml
```

2. Run the following command to adjust number of pods:

```
kubectl scale deployment zone-spread --replicas 15
```

Karpenter will add new nodes to the cluster with at least one node it a
different availability zone.
For more examples, see [Karpenter example workloads](https://github.com/aws/karpenter-provider-aws/tree/main/examples/workloads "https://github.com/aws/karpenter-provider-aws/tree/main/examples/workloads") on GitHub.
