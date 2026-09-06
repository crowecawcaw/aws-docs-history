

# Missing NVIDIA GPU plugin error
<a name="sagemaker-hyperpod-model-deployment-ts-gpu"></a>

Model deployment fails with GPU insufficiency error despite having available GPU nodes. This occurs when the NVIDIA device plugin is not installed in the HyperPod cluster.

**Error message:**

```
0/15 nodes are available: 10 node(s) didn't match Pod's node affinity/selector, 
5 Insufficient nvidia.com/gpu. preemption: 0/15 nodes are available: 
10 Preemption is not helpful for scheduling, 5 No preemption victims found for incoming pod.
```

**Root cause:**
+ Kubernetes cannot detect GPU resources without the NVIDIA device plugin
+ Results in scheduling failures for GPU workloads

**Resolution:**

Install the NVIDIA GPU plugin by running:

```
kubectl create -f https://raw.githubusercontent.com/NVIDIA/k8s-device-plugin/refs/tags/v0.17.1/deployments/static/nvidia-device-plugin.yml
```

**Verification steps:**

1. Check the plugin deployment status:

   ```
   kubectl get pods -n kube-system | grep nvidia-device-plugin
   ```

1. Verify GPU resources are now visible:

   ```
   kubectl get nodes -o=custom-columns=NAME:.metadata.name,GPU:.status.allocatable.nvidia\\.com/gpu
   ```

1. Retry model deployment

**Note**  
Ensure NVIDIA drivers are installed on GPU nodes. Plugin installation is a one-time setup per cluster. May require cluster admin privileges to install.