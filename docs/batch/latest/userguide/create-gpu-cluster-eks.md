# Create a GPU-based Kubernetes cluster on Amazon EKS

Before you create a GPU-based Kubernetes cluster on Amazon EKS, you must have completed the steps in [Getting started with AWS Batch on Amazon EKS](getting-started-eks.md "getting-started-eks.md"). In addition, also consider the
following:

- AWS Batch supports instance types with NVIDIA GPUs.
- By default, AWS Batch selects the Amazon EKS accelerated AMI with the Kubernetes version that matches your Amazon EKS cluster
  control plane version.

```
`$` `cat <<EOF > ./batch-eks-gpu-ce.json
{
 "computeEnvironmentName": "My-Eks-GPU-CE1",
 "type": "MANAGED",
 "state": "ENABLED",
 "eksConfiguration": {
 "eksClusterArn": "arn:aws:eks:`<region>`:`<account>`:cluster/`<cluster-name>`",
 "kubernetesNamespace": "my-aws-batch-namespace"
 },
 "computeResources": {
 "type": "EC2",
 "allocationStrategy": "BEST_FIT_PROGRESSIVE",
 "minvCpus": 0,
 "maxvCpus": 1024,
 "instanceTypes": [
 "p3dn.24xlarge",
 "p4d.24xlarge"
 ],
 "subnets": [
 "`<eks-cluster-subnets-with-access-to-internet-for-image-pull>`"
 ],
 "securityGroupIds": [
 "`<eks-cluster-sg>`"
 ],
 "instanceRole": "`<eks-instance-profile>`"
 }
}
EOF`

`$` `aws batch create-compute-environment --cli-input-json file://./batch-eks-gpu-ce.json`
```

AWS Batch doesn't manage the NVIDIA GPU device plugin on your behalf. You must install this plugin
into your Amazon EKS cluster and allow it to target the AWS Batch nodes. For more information, see [Enabling GPU Support in
Kubernetes](https://github.com/NVIDIA/k8s-device-plugin#enabling-gpu-support-in-kubernetes "https://github.com/NVIDIA/k8s-device-plugin#enabling-gpu-support-in-kubernetes") on GitHub.

To configure the NVIDIA device plugin (`DaemonSet`) to target the AWS Batch nodes, run
the following commands.

```
`# pull nvidia daemonset spec`
`$` `curl -O https://raw.githubusercontent.com/NVIDIA/k8s-device-plugin/v0.12.2/nvidia-device-plugin.yml`
`# using your favorite editor, add Batch node toleration
# this will allow the DaemonSet to run on Batch nodes
- key: "batch.amazonaws.com/batch-node"
 operator: "Exists"`
`$` `kubectl apply -f nvidia-device-plugin.yml`
```

We do not recommend that you mix compute-based (CPU and memory) workloads with GPU-based workloads in the same
pairings of compute environment and job queue. This is because compute jobs can use up GPU capacity.

To attach job queues, run the following commands.

```
`$` `cat <<EOF > ./batch-eks-gpu-jq.json
 {
 "jobQueueName": "My-Eks-GPU-JQ1",
 "priority": 10,
 "computeEnvironmentOrder": [
 {
 "order": 1,
 "computeEnvironment": "My-Eks-GPU-CE1"
 }
 ]
 }
EOF`

`$` `aws batch create-job-queue --cli-input-json file://./batch-eks-gpu-jq.json`
```
