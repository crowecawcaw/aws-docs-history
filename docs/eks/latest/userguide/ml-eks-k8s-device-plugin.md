**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Install Kubernetes device plugin for GPUs

Kubernetes [device plugins](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/ "https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/") have been the primary mechanism for advertising specialized infrastructure such as GPUs, network interfaces, and network adaptors as consumable resources for Kubernetes workloads. While [Dynamic Resource Allocation](https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/ "https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/") (DRA) is positioned as the future for device management in Kubernetes, most specialized infrastructure providers are early in their support for DRA drivers. Kubernetes device plugins remain a widely available approach for using GPUs in Kubernetes clusters today.

## Considerations

- When using the EKS-optimized AL2023 AMIs with NVIDIA GPUs, you must install the [NVIDIA Kubernetes device plugin](https://github.com/NVIDIA/k8s-device-plugin "https://github.com/NVIDIA/k8s-device-plugin"). You can install and manage the NVIDIA Kubernetes device plugin with Helm, your choice of Kubernetes tooling, or the NVIDIA GPU operator.
- When using the EKS-optimized Bottlerocket AMIs with NVIDIA GPUs, you do not need to install the NVIDIA Kubernetes device plugin, as it is already included in the EKS-optimized Bottlerocket AMIs. This includes when you use GPU instances with EKS Auto Mode.
- When using the EKS-optimized AL2023 or Bottlerocket AMIs with AWS Inferentia or Trainium GPUs, then you must install the Neuron Kubernetes device plugin, and optionally install the [Neuron Kubernetes scheduler extension](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/containers/tutorials/k8s-neuron-scheduler.html "https://awsdocs-neuron.readthedocs-hosted.com/en/latest/containers/tutorials/k8s-neuron-scheduler.html"). For more information, see the [Neuron documentation for running on EKS](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/containers/kubernetes-getting-started.html "https://awsdocs-neuron.readthedocs-hosted.com/en/latest/containers/kubernetes-getting-started.html").

## Install NVIDIA Kubernetes device plugin

The following procedure describes how to install the NVIDIA Kubernetes device plugin and run a sample test on NVIDIA GPU instances.

### Prerequisites

- EKS cluster created
- NVIDIA GPU nodes running in the cluster using EKS-optimized AL2023 NVIDIA AMI
- Helm installed in your command-line environment, see [Setup Helm instructions](helm.md "helm.md").

### Procedure

1. Add the `nvdp` Helm chart repository.

```
helm repo add nvdp https://nvidia.github.io/k8s-device-plugin
```

2. Update your local Helm repository to make sure that you have the most recent charts.

```
helm repo update
```

3. Get the latest version of the NVIDIA Kubernetes device plugin

```
helm search repo nvdp --devel
```

```
NAME                      	CHART VERSION	APP VERSION	DESCRIPTION
nvdp/gpu-feature-discovery	0.17.4       	0.17.4     	...
nvdp/nvidia-device-plugin 	0.17.4       	0.17.4     	...
```

4. Install the NVIDIA Kubernetes device plugin on your cluster, replacing `0.17.4` with the latest version from the command above.

```
helm install nvdp nvdp/nvidia-device-plugin \
  --namespace nvidia \
  --create-namespace \
  --version `0.17.4` \
  --set gfd.enabled=true
```

5. Verify the NVIDIA Kubernetes device plugin is running in your cluster. The output below shows the output with two nodes in the cluster.

```
kubectl get ds -n nvidia nvdp-nvidia-device-plugin
```

```
NAME                        DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR   AGE
nvdp-nvidia-device-plugin   2         2         2       2            2           <none>          11m
```

6. Verify that your nodes have allocatable GPUs with the following command.

```
kubectl get nodes "-o=custom-columns=NAME:.metadata.name,GPU:.status.allocatable.nvidia\.com/gpu"
```

```
NAME                                           GPU
ip-192-168-11-225.us-west-2.compute.internal   1
ip-192-168-24-96.us-west-2.compute.internal    1
```

7. Create a file named `nvidia-smi.yaml` with the following contents. This manifest launches a [minimal AL2023 container image](../../../linux/al2023/ug/minimal-container.md "../../../linux/al2023/ug/minimal-container.md") that runs `nvidia-smi` on a node.

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
      command: ['/bin/sh', '-c']
      args: ['nvidia-smi && tail -f /dev/null']
      resources:
        limits:
          nvidia.com/gpu: 1
  tolerations:
    - key: 'nvidia.com/gpu'
      operator: 'Equal'
      value: 'true'
      effect: 'NoSchedule'
```

8. Apply the manifest with the following command.

```
kubectl apply -f nvidia-smi.yaml
```

9. After the Pod has finished running, view its logs with the following command.

```
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

## Install Neuron Kubernetes device plugin

The following procedure describes how to install the Neuron Kubernetes device plugin and run a sample test on an Inferentia instance.

### Prerequisites

- EKS cluster created
- Neuron GPU nodes running in the cluster using EKS-optimized AL2023 Neuron AMI or Bottlerocket AMI
- Helm installed in your command-line environment, see [Setup Helm instructions](helm.md "helm.md").

### Procedure

1. Install the Neuron Kubernetes device plugin on your cluster.

```
helm upgrade --install neuron-helm-chart oci://public.ecr.aws/neuron/neuron-helm-chart \
    --set "npd.enabled=false"
```

2. Verify the Neuron Kubernetes device plugin is running in your cluster. The output below shows the output with a single Neuron node in the cluster.

```
kubectl get ds -n kube-system neuron-device-plugin
```

```
NAME                   DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR   AGE
neuron-device-plugin   1         1         1       1            1           <none>          72s
```

3. Verify that your nodes have allocatable NueronCores with the following command.

```
kubectl get nodes "-o=custom-columns=NAME:.metadata.name,NeuronCore:.status.allocatable.aws\.amazon\.com/neuroncore"
```

```
NAME                                           NeuronCore
ip-192-168-47-173.us-west-2.compute.internal   2
```

4. Verify that your nodes have allocatable NueronDevices with the following command.

```
kubectl get nodes "-o=custom-columns=NAME:.metadata.name,NeuronDevice:.status.allocatable.aws\.amazon\.com/neuron"
```

```
NAME                                           NeuronDevice
ip-192-168-47-173.us-west-2.compute.internal   1
```

5. Create a file named `neuron-ls.yaml` with the following contents. This manifest launches an [Neuron Monitor](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/tools/neuron-sys-tools/neuron-monitor-user-guide.html "https://awsdocs-neuron.readthedocs-hosted.com/en/latest/tools/neuron-sys-tools/neuron-monitor-user-guide.html") container that has the `neuron-ls` tool installed.

```
apiVersion: v1
kind: Pod
metadata:
  name: neuron-ls
spec:
  restartPolicy: Never
  containers:
  - name: neuron-container
    image: public.ecr.aws/g4h4h0b5/neuron-monitor:1.0.0
    command: ["/bin/sh"]
    args: ["-c", "neuron-ls"]
    resources:
      limits:
        aws.amazon.com/neuron: 1
  tolerations:
  - key: "aws.amazon.com/neuron"
    operator: "Exists"
    effect: "NoSchedule"
```

6. Apply the manifest with the following command.

```
kubectl apply -f neuron-ls.yaml
```

7. After the Pod has finished running, view its logs with the following command.

```
kubectl logs neuron-ls
```

An example output is below.

```
instance-type: inf2.xlarge
instance-id: ...
+--------+--------+--------+---------+
| NEURON | NEURON | NEURON |   PCI   |
| DEVICE | CORES  | MEMORY |   BDF   |
+--------+--------+--------+---------+
| 0      | 2      | 32 GB  | 00:1f.0 |
+--------+--------+--------+---------+
```
