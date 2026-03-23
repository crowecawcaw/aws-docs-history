**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Manage NVIDIA GPU devices on Amazon EKS

NVIDIA GPUs are widely used for machine learning training, inference, and high-performance computing workloads. Amazon EKS supports two mechanisms for managing NVIDIA GPU devices in your EKS clusters: the _NVIDIA DRA driver for GPUs_ and the _NVIDIA Kubernetes device plugin_.

It’s recommended to use the NVIDIA DRA driver for new deployments on clusters running Kubernetes version 1.34 or later. The NVIDIA DRA driver enables flexible GPU allocation and GPU sharing between containers. The NVIDIA device plugin remains supported.

## NVIDIA DRA driver vs. NVIDIA device plugin

| Capability                  | NVIDIA DRA driver                                                                                           | NVIDIA device plugin                                               |
| --------------------------- | ----------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| Minimum Kubernetes version  | 1.34                                                                                                        | All EKS-supported Kubernetes versions                              |
| Karpenter and EKS Auto Mode | Not supported                                                                                               | Supported                                                          |
| EKS-optimized AMIs          | AL2023                                                                                                      | AL2023, Bottlerocket                                               |
| Device advertisement        | Rich attributes via `ResourceSlice` objects including GPU model, memory, driver version, and topology       | Integer count of `nvidia.com/gpu` extended resources               |
| GPU sharing                 | Multiple containers in the same Pod can share a GPU through shared `ResourceClaim` references               | Not supported. Each GPU is exclusively allocated to one container. |
| ComputeDomains              | Manages Multi-Node NVLink (MNNVL) through `ComputeDomain` resources for secure multi-node GPU communication | Not supported                                                      |
| Attribute-based selection   | Filter GPUs by model, memory, or other attributes using CEL expressions                                     | Not supported                                                      |

## Install the NVIDIA DRA driver

The NVIDIA DRA driver for GPUs manages two types of resources: GPUs and ComputeDomains. It runs two DRA kubelet plugins: `gpu-kubelet-plugin` and `compute-domain-kubelet-plugin`. Each can be enabled or disabled separately during installation. This guide focuses on GPU allocation. For using ComputeDomains, see [Use P6e-GB200 UltraServers with Amazon EKS](ml-eks-nvidia-ultraserver.md "ml-eks-nvidia-ultraserver.md").

Using the NVIDIA DRA driver with Bottlerocket is not currently supported.

### Prerequisites

- An Amazon EKS cluster running Kubernetes version 1.34 or later.
- Nodes with NVIDIA GPU instance types (such as `P` or `G` instances).
- Nodes with host-level components installed for NVIDIA GPUs. When using the EKS-optimized AL2023 or Bottlerocket NVIDIA AMIs, the host-level NVIDIA driver, CUDA user mode driver, and container toolkit are pre-installed.
- Helm installed in your command-line environment, see the [Setup Helm instructions](helm.md "helm.md") for more information.
- `kubectl` configured to communicate with your cluster, see [Install or update kubectl](install-kubectl.md#kubectl-install-update "install-kubectl.md#kubectl-install-update") for more information.

### Procedure

###### Important

When using the NVIDIA DRA driver for GPU device management, it cannot be deployed alongside the NVIDIA device plugin on the same node. See upstream Kubernetes [KEP-5004](https://github.com/kubernetes/enhancements/issues/5004 "https://github.com/kubernetes/enhancements/issues/5004") for updates.

1. Add the NVIDIA DRA driver Helm chart repository.

```
helm repo add nvidia https://helm.ngc.nvidia.com/nvidia
```

2. Update your local Helm repository.

```
helm repo update
```

3. Get the latest version of the NVIDIA DRA driver.

```
helm search repo nvidia/nvidia-dra
```

4. Install the NVIDIA DRA driver.

```
helm install nvidia-dra-driver-gpu nvidia/nvidia-dra-driver-gpu \
    --create-namespace \
    --namespace nvidia-dra-driver-gpu \
    --set resources.computeDomains.enabled=false \
    --set 'gpuResourcesEnabledOverride=true'
```

For advanced configuration options, see the [NVIDIA DRA driver Helm chart](https://github.com/NVIDIA/k8s-dra-driver-gpu/blob/main/deployments/helm/nvidia-dra-driver-gpu/values.yaml "https://github.com/NVIDIA/k8s-dra-driver-gpu/blob/main/deployments/helm/nvidia-dra-driver-gpu/values.yaml"). 5. Verify that the DRA driver pods are running.

```
kubectl get pods -n nvidia-dra-driver-gpu
```

6. Verify that the `DeviceClass` objects were created.

```
kubectl get deviceclass
```

```
NAME            AGE
gpu.nvidia.com  60s
```

7. Verify that `ResourceSlice` objects are published for your GPU nodes.

```
kubectl get resourceslice
```

### Request NVIDIA GPUs in a Pod

To request NVIDIA GPUs using the DRA driver, create a `ResourceClaimTemplate` that references the `gpu.nvidia.com`
`DeviceClass` and reference it in your Pod specification.

The following example requests a single GPU:

```
apiVersion: resource.k8s.io/v1
kind: ResourceClaimTemplate
metadata:
  name: single-gpu
spec:
  spec:
    devices:
      requests:
      - name: gpu
        exactly:
          deviceClassName: gpu.nvidia.com
          count: 1
---
apiVersion: v1
kind: Pod
metadata:
  name: gpu-workload
spec:
  containers:
  - name: app
    ...
    resources:
      claims:
      - name: gpu
  resourceClaims:
  - name: gpu
    resourceClaimTemplateName: single-gpu
  tolerations:
  - key: "nvidia.com/gpu"
    operator: "Exists"
    effect: "NoSchedule"
```

## Install the NVIDIA Kubernetes device plugin

The NVIDIA Kubernetes device plugin advertises NVIDIA GPUs as `nvidia.com/gpu` extended resources. You request GPUs in container resource requests and limits.

### Prerequisites

- An Amazon EKS cluster.
- Nodes with NVIDIA GPU instance types using the EKS-optimized AL2023 NVIDIA AMI. The EKS-optimized Bottlerocket AMIs include the NVIDIA device plugin and no separate installation is required.
- Helm installed in your command-line environment, see the [Setup Helm instructions](helm.md "helm.md") for more information.
- `kubectl` configured to communicate with your cluster, see [Install or update kubectl](install-kubectl.md#kubectl-install-update "install-kubectl.md#kubectl-install-update") for more information.

### Procedure

1. Add the NVIDIA device plugin Helm chart repository.

```
helm repo add nvdp https://nvidia.github.io/k8s-device-plugin
```

2. Update your local Helm repository.

```
helm repo update
```

3. Install the NVIDIA Kubernetes device plugin.

```
helm install nvdp nvdp/nvidia-device-plugin \
    --namespace nvidia \
    --create-namespace \
    --set gfd.enabled=true
```

###### Note

You can also install and manage the NVIDIA Kubernetes device plugin using the [NVIDIA GPU Operator](https://github.com/NVIDIA/gpu-operator "https://github.com/NVIDIA/gpu-operator"), which automates the management of all NVIDIA software components needed to provision GPUs. 4. Verify the NVIDIA device plugin DaemonSet is running.

```
kubectl get ds -n nvidia nvdp-nvidia-device-plugin
```

```
NAME                        DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR   AGE
nvdp-nvidia-device-plugin   2         2         2       2            2           <none>          60s
```

5. Verify that your nodes have allocatable GPUs.

```
kubectl get nodes "-o=custom-columns=NAME:.metadata.name,GPU:.status.allocatable.nvidia\.com/gpu"
```

An example output is as follows.

```
NAME                                           GPU
ip-192-168-11-225.us-west-2.compute.internal   1
ip-192-168-24-96.us-west-2.compute.internal    1
```

### Request NVIDIA GPUs in a Pod

To request NVIDIA GPUs using the device plugin, specify the `nvidia.com/gpu` resource in your container resource limits.

```
apiVersion: v1
kind: Pod
metadata:
  name: nvidia-smi
spec:
  restartPolicy: OnFailure
  containers:
  - name: gpu-demo
    image: public.ecr.aws/amazonlinux/amazonlinux:2023-minimal
    command: ["/bin/sh", "-c"]
    args: ["nvidia-smi && tail -f /dev/null"]
    resources:
      limits:
        nvidia.com/gpu: 1
  tolerations:
  - key: "nvidia.com/gpu"
    operator: "Equal"
    value: "true"
    effect: "NoSchedule"
```

To run this test, apply the manifest and view the logs:

```
kubectl apply -f nvidia-smi.yaml
kubectl logs nvidia-smi
```

An example output is as follows.

```
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI XXX.XXX.XX            Driver Version: XXX.XXX.XX     CUDA Version: XX.X      |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA L4                      On  |   00000000:31:00.0 Off |                    0 |
| N/A   27C    P8             11W /   72W |       0MiB /  23034MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|  No running processes found                                                             |
+-----------------------------------------------------------------------------------------+
```
