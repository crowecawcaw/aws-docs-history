# Using UltraServers in Amazon SageMaker HyperPod

SageMaker HyperPod support for Ultraservers provides high-performance GPU computing capabilities
for AI and machine learning workloads. Built on NVIDIA GB200 and NVL72 architecture, these
Ultraservers provide NVLink connectivity across 18 GB200 instances in a dual-rack configuration,
totaling 72 B200 GPUs. This NVLink fabric allows workloads to use GPU communications that increase
usable GPU capacity and addressable memory beyond what's possible with discrete instances, supporting
more complex and resource-intensive AI models. The NVLink connectivity is enabled by NVIDIA IMEX
technology, which handles the low-level configuration for secure GPU fabric connections across
instances within the same rack.

HyperPod simplifies the deployment and management of these GPU clusters through intelligent
topology awareness and automated configuration. The platform automatically discovers and labels nodes
with their physical location and capacity block information, which supports topology-aware
scheduling for distributed workloads. HyperPod abstracts the complex IMEX configuration
requirements, allowing you to focus on workload deployment rather than low-level GPU fabric setup.
You can choose flexible deployment options including both self-managed nodes and EKS managed node
groups. Amazon EKS provides optimized AMIs that include pre-configured NVIDIA drivers, Fabric
Manager, IMEX drivers, and all necessary system software for seamless operation.

The integration includes pod placement capabilities that ensure distributed workloads are scheduled
optimally across NVL72 domains using standard Kubernetes topology labels. Built-in monitoring and
automated recovery features provide operational support, where the AMI health agent detects GPU
errors from kernel logs and can automatically remediate issues or replace faulty nodes in managed
node groups. This combination of GPU scale, intelligent workload placement, and automated operations
helps you focus on your AI/ML innovations rather than infrastructure complexity, while achieving
maximum performance from your GPU investments.

To get set up using UltraServers with your HyperPod cluster, see the following steps:

1. Create an [EKS-based HyperPod cluster](sagemaker-hyperpod-eks-operate-console-ui-create-cluster.md "sagemaker-hyperpod-eks-operate-console-ui-create-cluster.md"). When you choose an instance group, make sure you choose an UltraServer.
2. After your cluster is created, use the following commands install operational plugins:

NVIDIA device plugin v0.17.2

```
kubectl apply -f https://raw.githubusercontent.com/NVIDIA/k8s-device-plugin/v0.17.2/deployments/static/nvidia-device-plugin.yml
```

FD DaemonSet v0.17.3

```
kubectl apply -k "https://github.com/kubernetes-sigs/node-feature-discovery/deployment/overlays/default?ref=v0.17.3"
```

GPU feature discovery

```
kubectl apply -f https://raw.githubusercontent.com/NVIDIA/k8s-device-plugin/v0.17.2/deployments/static/gpu-feature-discovery-daemonset.yaml
```

You can now run jobs. The following example demonstrates how to create a domain, configure an IMEX domain, and enable channel allocation.
These steps also let you create a pod to provision a channel for NCCL communication.

1. Create a resource specification file to use with Kubectl.

```
cat <<EOF > imex-channel-injection.yaml
---
apiVersion: resource.nvidia.com/v1beta1
kind: ComputeDomain
metadata:
  name: imex-channel-injection
spec:
  numNodes: 1
  channel:
    resourceClaimTemplate:
      name: imex-channel-0
---
apiVersion: v1
kind: Pod
metadata:
  name: imex-channel-injection
spec:
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: nvidia.com/gpu.clique
            operator: Exists
          - key: topology.k8s.aws/ultraserver-id
            operator: In
            values:
            - <`UltraServer-ID`>
  containers:
  - name: ctr
    image: ubuntu:22.04
    command: ["bash", "-c"]
    args: ["ls -la /dev/nvidia-caps-imex-channels; trap 'exit 0' TERM; sleep 9999 & wait"]
    resources:
      claims:
      - name: imex-channel-0
  resourceClaims:
  - name: imex-channel-0
    resourceClaimTemplateName: imex-channel-0
EOF
```

2. Apply the configuration that you created.

```
kubectl apply -f imex-channel-injection.yaml
```

3. To verify that your pod is created, run the `get pods` commands.

```
kubectl get pods
kubectl get pods -n nvidia-dra-driver-gpu -l resource.nvidia.com/computeDomain
```

4. You can also check the logs from the pod to see if it allocated a communication channel.

```
kubectl logs imex-channel-injection
```

```
total 0
drwxr-xr-x 2 root root     60 Feb 19 10:43 .
drwxr-xr-x 6 root root    380 Feb 19 10:43 ..
crw-rw-rw- 1 root root 507, 0 Feb 19 10:43 channel0
```

5. You can also check the logs to verify that the automated IMEX configuration is running with an allocated channel.

```
kubectl logs -n nvidia-dra-driver-gpu -l resource.nvidia.com/computeDomain --tail=-1
/etc/nvidia-imex/nodes_config.cfg:
```

```
IMEX Log initializing at: 8/8/2025 14:23:12.081
[Aug 8 2025 14:23:12] [INFO] [tid 39] IMEX version 570.124.06 is running with the following configuration options

[Aug 8 2025 14:23:12] [INFO] [tid 39] Logging level = 4

[Aug 8 2025 14:23:12] [INFO] [tid 39] Logging file name/path = /var/log/nvidia-imex.log

[Aug 8 2025 14:23:12] [INFO] [tid 39] Append to log file = 0

[Aug 8 2025 14:23:12] [INFO] [tid 39] Max Log file size = 1024 (MBs)

[Aug 8 2025 14:23:12] [INFO] [tid 39] Use Syslog file = 0

[Aug 8 2025 14:23:12] [INFO] [tid 39] IMEX Library communication bind interface =

[JAug 8 2025 14:23:12] [INFO] [tid 39] IMEX library communication bind port = 50000

[Aug 8 2025 14:23:12] [INFO] [tid 39] Identified this node as ID 0, using bind IP of '10.115.131.8', and network interface of enP5p9s0
[Aug 8 2025 14:23:120] [INFO] [tid 39] nvidia-imex persistence file /var/run/nvidia-imex/persist.dat does not exist.  Assuming no previous importers.
[Aug 8 2025 14:23:12] [INFO] [tid 39] NvGpu Library version matched with GPU Driver version
[Aug 8 2025 14:23:12] [INFO] [tid 63] Started processing of incoming messages.
[Aug 8 2025 14:23:12] [INFO] [tid 64] Started processing of incoming messages.
[Aug 8 2025 14:23:12] [INFO] [tid 65] Started processing of incoming messages.
[Aug 8 2025 14:23:12] [INFO] [tid 39] Creating gRPC channels to all peers (nPeers = 1).
[Aug 8 2025 14:23:12] [INFO] [tid 66] Started processing of incoming messages.
[Aug 8 2025 14:23:12] [INFO] [tid 39] IMEX_WAIT_FOR_QUORUM != FULL, continuing initialization without waiting for connections to all nodes.
[Aug 8 2025 14:23:12] [INFO] [tid 67] Connection established to node 0 with ip address 10.115.131.8. Number of times connected: 1
[Aug 8 2025 14:23:12] [INFO] [tid 39] GPU event successfully subscribed
```

6. After you've verified everything, delete the workload and remove the configuration.

```
kubectl delete -f imex-channel-injection.yaml
```
