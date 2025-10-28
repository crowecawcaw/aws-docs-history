**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Run GPU-accelerated containers (Linux on EC2)

The Amazon EKS optimized accelerated Amazon Linux AMIs are built on top of the standard Amazon EKS optimized Amazon Linux AMIs. For details on these AMIs, see [Amazon EKS optimized accelerated Amazon Linux AMIs](eks-optimized-ami.md#gpu-ami "eks-optimized-ami.md#gpu-ami").
The following text describes how to enable AWS Neuron-based workloads.

###### To enable AWS Neuron (ML accelerator) based workloads

For details on training and inference workloads using Neuron in Amazon EKS, see the following references:

- [Containers - Kubernetes - Getting Started](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/containers/kubernetes-getting-started.html "https://awsdocs-neuron.readthedocs-hosted.com/en/latest/containers/kubernetes-getting-started.html") in the _AWS Neuron Documentation_
- [Training](https://github.com/aws-neuron/aws-neuron-eks-samples/blob/master/README.md#training "https://github.com/aws-neuron/aws-neuron-eks-samples/blob/master/README.md#training") in AWS Neuron EKS Samples on GitHub
- [Deploy ML inference workloads with AWSInferentia on Amazon EKS](inferentia-support.md "inferentia-support.md")
  The following procedure describes how to run a workload on a GPU based instance with the Amazon EKS optimized accelerated AMIs.

1. After your GPU nodes join your cluster, you must apply the [NVIDIA device plugin for Kubernetes](https://github.com/NVIDIA/k8s-device-plugin "https://github.com/NVIDIA/k8s-device-plugin") as a DaemonSet on your cluster. Replace `vX.X.X` with your desired [NVIDIA/k8s-device-plugin](https://github.com/NVIDIA/k8s-device-plugin/releases "https://github.com/NVIDIA/k8s-device-plugin/releases") version before running the following command.

```
kubectl apply -f https://raw.githubusercontent.com/NVIDIA/k8s-device-plugin/vX.X.X/deployments/static/nvidia-device-plugin.yml
```

2. You can verify that your nodes have allocatable GPUs with the following command.

```
kubectl get nodes "-o=custom-columns=NAME:.metadata.name,GPU:.status.allocatable.nvidia\.com/gpu"
```

3. Create a file named `nvidia-smi.yaml` with the following contents. Replace `tag` with your desired tag for [nvidia/cuda](https://hub.docker.com/r/nvidia/cuda/tags "https://hub.docker.com/r/nvidia/cuda/tags"). This manifest launches an [NVIDIA CUDA](https://developer.nvidia.com/cuda-zone "https://developer.nvidia.com/cuda-zone") container that runs `nvidia-smi` on a node.

```
apiVersion: v1
kind: Pod
metadata:
  name: nvidia-smi
spec:
  restartPolicy: OnFailure
  containers:
  - name: nvidia-smi
    image: nvidia/cuda:tag
    args:
    - "nvidia-smi"
    resources:
      limits:
        nvidia.com/gpu: 1
```

4. Apply the manifest with the following command.

```
kubectl apply -f nvidia-smi.yaml
```

5. After the Pod has finished running, view its logs with the following command.

```
kubectl logs nvidia-smi
```

An example output is as follows.

````
Mon Aug  6 20:23:31 20XX
+-----------------------------------------------------------------------------+
| NVIDIA-SMI XXX.XX                 Driver Version: XXX.XX                    |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  Tesla V100-SXM2...  On   | 00000000:00:1C.0 Off |                    0 |
| N/A   46C    P0    47W / 300W |      0MiB / 16160MiB |      0%      Default | +-------------------------------+----------------------+----------------------+ +-----------------------------------------------------------------------------+
| Processes:                                                       GPU Memory | |  GPU       PID   Type   Process name                             Usage      |
|=============================================================================| |  No running processes found                                                 | +-----------------------------------------------------------------------------+ ```
````
