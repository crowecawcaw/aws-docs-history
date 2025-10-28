**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Deploy an accelerated workload

This tutorial demonstrates how Amazon EKS Auto Mode simplifies launching hardware-accelerated workloads. Amazon EKS Auto Mode streamlines operations beyond the cluster itself by automating key infrastructure components providing compute, networking, load balancing, storage, and Identity Access and Management capabilities out of the box.

Amazon EKS Auto Mode includes the drivers and device plugins required for certain instance types, such as NVIDIA and AWS Neuron drivers. You do not have to install or update these components.

EKS Auto Mode automatically manages drivers for these accelerators:

- [AWS Trainium](https://aws.amazon.com/ai/machine-learning/trainium/ "https://aws.amazon.com/ai/machine-learning/trainium/")
- [AWS Inferentia](https://aws.amazon.com/ai/machine-learning/inferentia/ "https://aws.amazon.com/ai/machine-learning/inferentia/")
- [NVIDIA GPUs on Amazon EC2 accelerated instances](../../../ec2/latest/instancetypes/ac.md "../../../ec2/latest/instancetypes/ac.md")

###### Note

EKS Auto Mode includes the NVIDIA device plugin for Kubernetes. This plugin runs automatically and isn’t visible as a daemon set in your cluster.

Additional networking support:

- [Elastic Fabric Adapter (EFA)](https://aws.amazon.com/hpc/efa/ "https://aws.amazon.com/hpc/efa/")
  Amazon EKS Auto Mode eliminates the toil of accelerator driver and device plugin management.

You can also benefit from cost savings by scaling the cluster to zero. You can configure EKS Auto Mode to terminate instances when no workloads are running. This is useful for batch based inference workloads.

The following provides an example of how to launch accelerated workloads with Amazon EKS Auto Mode.

## Prerequisites

- A Kubernetes cluster with Amazon EKS Auto Mode configured.
- A `default` EKS Node class as created when the `general-purpose` or `system` Managed Node Pools are enabled.

## Step 1: Deploy a GPU workload

In this example, you will create a NodePool for NVIDIA based workloads that requires 45GB GPU memory. With EKS Auto Mode, you use Kubernetes scheduling constraints to define your instance requirements.

To deploy the Amazon EKS Auto Mode `NodePool` and the sample `workload`, review the following NodePool and Pod definition and save as `nodepool-gpu.yaml` and `pod.yaml`:

**nodepool-gpu.yaml**

```
apiVersion: karpenter.sh/v1
kind: NodePool
metadata:
  name: gpu
spec:
  disruption:
    budgets:
    - nodes: 10%
    consolidateAfter: 1h
    consolidationPolicy: WhenEmpty
  template:
    metadata: {}
    spec:
      nodeClassRef:
        group: eks.amazonaws.com
        kind: NodeClass
        name: default
      requirements:
        - key: "karpenter.sh/capacity-type"
          operator: In
          values: ["on-demand"]
        - key: "kubernetes.io/arch"
          operator: In
          values: ["amd64"]
        - key: "eks.amazonaws.com/instance-family"
          operator: In
          values:
          - g6e
          - g6
      taints:
        - key: nvidia.com/gpu
          effect: NoSchedule
      terminationGracePeriod: 24h0m0s
```

**pod.yaml**

```
apiVersion: v1
kind: Pod
metadata:
  name: nvidia-smi
spec:
  nodeSelector:
    eks.amazonaws.com/compute-type: auto
  restartPolicy: OnFailure
  containers:
  - name: nvidia-smi
    image: public.ecr.aws/amazonlinux/amazonlinux:2023-minimal
    args:
    - "nvidia-smi"
    resources:
      requests:
        memory: "30Gi"
        cpu: "3500m"
        nvidia.com/gpu: 1
      limits:
        memory: "30Gi"
        nvidia.com/gpu: 1
  tolerations:
  - key: nvidia.com/gpu
    effect: NoSchedule
    operator: Exists
```

Note the `eks.amazonaws.com/compute-type: auto` selector requires the workload be deployed on an Amazon EKS Auto Mode node. The NodePool also sets a taint that only allows pods with tolerations for Nvidia GPUs to be scheduled.

Apply the NodePool and workload to your cluster.

```
kubectl apply -f nodepool-gpu.yaml
kubectl apply -f pod.yaml
```

You should see the following output:

```
nodepool.karpenter.sh/gpu configured created
pod/nvidia-smi created
```

Wait a few seconds, and check the nodes in your cluster. You should now see a new node provisioned in your Amazon EKS Auto Mode cluster:

```
> kubectl get nodes

NAME        TYPE          CAPACITY    ZONE         NODE                  READY   AGE
gpu-dnknr   g6e.2xlarge   on-demand   us-west-2b   i-02315c7d7643cdee6   True    76s
```

## Step 2: Validate

You can see Amazon EKS Auto Mode launched a `g6e.2xlarge` rather than an `g6.2xlarge` as the workload required an instance with l40s `GPU`, according to the following Kubernetes scheduling constraints:

```
...
  nodeSelector:
    eks.amazonaws.com/instance-gpu-name: l40s
...
    requests:
        memory: "30Gi"
        cpu: "3500m"
        nvidia.com/gpu: 1
      limits:
        memory: "30Gi"
        nvidia.com/gpu: 1
```

Now, look at the containers logs, by running the following command:

```
kubectl logs nvidia-smi
```

Sample output:

````
+---------------------------------------------------------------------------------------+
| NVIDIA-SMI 535.230.02             Driver Version: 535.230.02   CUDA Version: 12.2     |
|-----------------------------------------+----------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |         Memory-Usage | GPU-Util  Compute M. |
|                                         |                      |               MIG M. |
|=========================================+======================+======================|
|   0  NVIDIA L40S                    On  | 00000000:30:00.0 Off |                    0 |
| N/A   27C    P8              23W / 350W |      0MiB / 46068MiB |      0%      Default |
|                                         |                      |                  N/A | +-----------------------------------------+----------------------+----------------------+ +---------------------------------------------------------------------------------------+
| Processes:                                                                            | |  GPU   GI   CI        PID   Type   Process name                            GPU Memory |
|        ID   ID                                                             Usage      | |=======================================================================================|
|  No running processes found                                                           | +---------------------------------------------------------------------------------------+ ``` You can see that the container has detected it’s running on an instance with an `NVIDIA` GPU and that you’ve not had to install any device drivers, as this is managed by Amazon EKS Auto Mode. ## Step 3: Clean-up To remove all objects created, use `kubectl` to delete the sample deployment and NodePool so the node is terminated: ``` kubectl delete -f nodepool-gpu.yaml kubectl delete -f pod.yaml ``` ## Example NodePools Reference ### Create an NVIDIA NodePool The following NodePool defines: <br>• Only launch instances of `g6e` and `g6` family <br>• Consolidate nodes when empty for 1 hour + The 1 hour value for `consolodateAfter` supports spiky workloads and reduce node churn. You can tune `consolidateAfter` based on your workload requirements. **Example NodePool with GPU instance family and consolidation** ``` apiVersion: karpenter.sh/v1 kind: NodePool metadata: name: gpu spec: disruption: budgets: <br>• nodes: 10% consolidateAfter: 1h consolidationPolicy: WhenEmpty template: metadata: {} spec: nodeClassRef: group: eks.amazonaws.com kind: NodeClass name: default requirements: <br>• key: "karpenter.sh/capacity-type" operator: In values: ["on-demand"] <br>• key: "kubernetes.io/arch" operator: In values: ["amd64"] <br>• key: "eks.amazonaws.com/instance-family" operator: In values: <br>• g6e <br>• g6 terminationGracePeriod: 24h0m0s ``` Instead of to setting the `eks.amazonaws.com/instance-gpu-name` you might use `eks.amazonaws.com/instance-family` to specify the instance family. For other well-known labels which influence scheduling review, see [EKS Auto Mode Supported Labels](create-node-pool.md#auto-supported-labels "create-node-pool.md#auto-supported-labels"). If you have specific storage requirements you can tune the nodes ephemeral storage `iops`, `size` and `throughput` by creating your own [NodeClass](create-node-class.md "create-node-class.md") to reference in the NodePool. Learn more about the [configurable NodeClass options](create-node-class.md "create-node-class.md"). **Example storage configuration for NodeClass** ``` apiVersion: eks.amazonaws.com/v1 kind: NodeClass metadata: name: gpu spec: ephemeralStorage: iops: 3000 size: 80Gi throughput: 125 ``` ### Define an AWS Trainium and AWS Inferentia NodePool The following NodePool has an `eks.amazonaws.com/instance-category` set that says, only launch instances of Inferentia and Trainium family: ``` <br>• key: "eks.amazonaws.com/instance-category" operator: In values: <br>• inf <br>• trn ```
````
