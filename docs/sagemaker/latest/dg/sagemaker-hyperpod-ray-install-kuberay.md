

# Installing KubeRay on HyperPod Amazon EKS
<a name="sagemaker-hyperpod-ray-install-kuberay"></a>

The KubeRay operator manages the lifecycle of `RayCluster`, `RayJob`, `RayCronJob`, and `RayService` resources. It is required for every Ray capability on HyperPod. HyperPod uses the open source operator without any changes.

## Prerequisites
<a name="sagemaker-hyperpod-ray-install-kuberay-prerequisites"></a>
+ A HyperPod cluster orchestrated by Amazon EKS. For more information, see [Creating a SageMaker HyperPod cluster with Amazon EKS orchestration](sagemaker-hyperpod-eks-operate-console-ui-create-cluster.md).
+ `kubectl` and `helm` installed, with `kubectl` configured for your cluster:

  ```
  aws eks update-kubeconfig --name {{my-eks-cluster}} --region {{my-region}}
  ```

## Installing on an existing cluster
<a name="sagemaker-hyperpod-ray-install-kuberay-existing"></a>

If your cluster does not already run KubeRay, install the operator with Helm.

**To install the KubeRay operator**

1. Add the KubeRay Helm repository.

   ```
   helm repo add kuberay https://ray-project.github.io/kuberay-helm/
   helm repo update
   ```

1. Install the operator.

   ```
   helm install kuberay-operator kuberay/kuberay-operator
   ```

1. Confirm that the operator pod is running.

   ```
   kubectl get pods -l app.kubernetes.io/name=kuberay-operator
   ```

For more information about operator installation options, see [KubeRay operator installation](https://docs.ray.io/en/latest/cluster/kubernetes/getting-started/kuberay-operator-installation.html) in the Ray documentation.

## Upgrading and uninstalling
<a name="sagemaker-hyperpod-ray-install-kuberay-upgrade"></a>

Upgrade the operator to the latest chart version:

```
helm repo update
helm upgrade kuberay-operator kuberay/kuberay-operator
```

Uninstalling removes the operator but not your Ray custom resources:

```
helm uninstall kuberay-operator
```

**Warning**  
Uninstalling the operator stops reconciliation of every Ray resource in the cluster. Running Ray clusters continue but are no longer managed, and deletions do not complete. Delete your Ray resources before you uninstall.