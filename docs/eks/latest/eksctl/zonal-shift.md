# Support for Zonal Shift in EKS clusters

EKS now supports Amazon Application Recovery Controller (ARC) zonal shift and zonal autoshift that enhances the
resiliency of multi-AZ cluster environments. With AWS Zonal Shift, customers can shift in-cluster traffic away
from an impaired availability zone, ensuring new Kubernetes pods and nodes are launched in healthy availability zones only.

## Creating a cluster with zonal shift enabled

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

To enable or disable zonal shift on an existing cluster, run

```
eksctl utils update-zonal-shift-config -f zonal-shift-cluster.yaml
```

or without a config file:

```
eksctl utils update-zonal-shift-config --cluster=zonal-shift-cluster --enabled
```

## Further information

- [EKS Zonal Shift](../userguide/zone-shift.md "../userguide/zone-shift.md")
