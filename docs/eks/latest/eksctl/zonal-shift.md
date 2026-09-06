

# Support for Zonal Shift in EKS clusters
<a name="zonal-shift"></a>

EKS now supports Amazon Application Recovery Controller (ARC) zonal shift and zonal autoshift that enhances the resiliency of multi-AZ cluster environments. With AWS Zonal Shift, customers can shift in-cluster traffic away from an impaired availability zone, ensuring new Kubernetes pods and nodes are launched in healthy availability zones only.

## Creating a cluster with zonal shift enabled
<a name="_creating_a_cluster_with_zonal_shift_enabled"></a>

```
# zonal-shift-cluster.yaml
---
apiVersion: eksctl.io/v1alpha5
kind: ClusterConfig

metadata:
  name: highly-available-cluster
  region: us-west-2


zonalShiftConfig:
  enabled: true
```

```
eksctl create cluster -f zonal-shift-cluster.yaml
```

## Enabling zonal shift on an existing cluster
<a name="_enabling_zonal_shift_on_an_existing_cluster"></a>

To enable or disable zonal shift on an existing cluster, run

```
eksctl utils update-zonal-shift-config -f zonal-shift-cluster.yaml
```

or without a config file:

```
eksctl utils update-zonal-shift-config --cluster=zonal-shift-cluster --enabled
```

## Further information
<a name="_further_information"></a>
+  [EKS Zonal Shift](https://docs.aws.amazon.com/eks/latest/userguide/zone-shift.html) 