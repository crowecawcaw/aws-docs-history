# Networking

###### Tip

[Register](https://events.eksworkshop.com/workshops/genai/ "https://events.eksworkshop.com/workshops/genai/") for upcoming Amazon EKS AI/ML workshops.

## Consider Higher Network Bandwidth or Elastic Fabric Adapter For Applications with High Inter-Node Communication

For distributed training workloads on Amazon EKS with high inter-node communication demands, consider selecting instances with higher network bandwidth or [Elastic Fabric Adapter](../userguide/node-efa.md "../userguide/node-efa.md") (EFA). Insufficient network performance can bottleneck data transfer, slowing down machine learning tasks like distributed multi-GPU training. Note that inference workloads don’t typically have high inter-node communication.

**Example**

For example, using Karpenter:

```
apiVersion: v1
kind: Pod
metadata:
  name: ml-workload
spec:
  nodeSelector:
    karpenter.k8s.aws/instance-network-bandwidth: "100000"  # 100 Gbps in Mbps
    node.kubernetes.io/instance-type: p5.48xlarge  # EFA-enabled instance
  containers:
  - name: training-job
    image: `763104351884.dkr.ecr.us-west-2.amazonaws.com/pytorch-inference:2.6.0-gpu-py312-cu124-ubuntu22.04-ec2-v1.6`
    resources:
      limits:
        vpc.amazonaws.com/efa: 1  # Requires EFA device plugin
```

Ensure tools like MPI and NCCL are installed in your container image to leverage EFA for training jobs.

## Planning for IP Address Consumption on Large GPU Instances

By default, the Amazon VPC CNI plugin pre-allocates IP addresses to ensure pods can be scheduled quickly, keeping one full spare ENI attached and populated with IPs. On large instances, this can result in dozens of IPs being reserved per node even when only a few pods are running.

This mismatch is common in training and inference workloads where pod density per node is low. At cluster scale, especially during autoscaling events that spin up many GPU nodes with few pods each, this can lead to subnet IP exhaustion even though actual IP utilization is low.

To mitigate this, tune the `WARM_IP_TARGET`, `MINIMUM_IP_TARGET`, and `WARM_ENI_TARGET` variables to match your actual pod density. More info at [VPC CNI’s ENI and IP target settings](https://github.com/aws/amazon-vpc-cni-k8s/blob/master/docs/eni-and-ip-target.md "https://github.com/aws/amazon-vpc-cni-k8s/blob/master/docs/eni-and-ip-target.md").

For a full guide on optimizing IP consumption, see [Optimizing IP Address Utilization](ip-opt.md "ip-opt.md").
