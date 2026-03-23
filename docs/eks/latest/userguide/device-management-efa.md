**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Manage EFA devices on Amazon EKS

[Elastic Fabric Adapter](../../../AWSEC2/latest/UserGuide/efa.md "../../../AWSEC2/latest/UserGuide/efa.md") (EFA) is a network device for Amazon EC2 instances that enables high-performance inter-node communication for machine learning training and High Performance Computing (HPC) workloads. Amazon EKS supports the _EFA device plugin_ for managing EFA devices in EKS clusters.

## Creating EKS nodes with EFA interfaces

When you create EKS nodes with EFA interfaces, the EFA interfaces are attached during instance bootstrap. If you need to customize the per-device EFA configuration or use [placement groups](../../../AWSEC2/latest/UserGuide/placement-groups.md "../../../AWSEC2/latest/UserGuide/placement-groups.md") for the EFA-enabled EC2 instances, it’s recommended to use EKS managed node groups or EKS self-managed node groups. You can pass configuration for each network interface with [launch templates](../../../AWSEC2/latest/UserGuide/ec2-launch-templates.md "../../../AWSEC2/latest/UserGuide/ec2-launch-templates.md").

When using EKS Auto Mode or Karpenter with dynamic provisioning, instances created for Pods requesting `vpc.amazonaws.com/efa` have all interfaces configured with interface type `EFA`. Static capacity provisioning in EKS Auto Mode and Karpenter does not currently support per-device EFA configuration. EKS Auto Mode and Karpenter do not currently support placement groups.

When using [eksctl](install-kubectl.md#eksctl-install-update "install-kubectl.md#eksctl-install-update") for provisioning EKS nodes with the `efaEnabled` setting, all interfaces are configured with interface type `EFA`, an EFA-specific security group is created, and the EFA device plugin is installed on the cluster. If you need to customize the per-device EFA configuration when using `eksctl`, it is recommended to use `eksctl’s support for [launch templates](../eksctl/launch-template-support.md "../eksctl/launch-template-support.md").

## Using EKS-optimized AMIs with EFA

The EKS-optimized AL2023 accelerated AMIs (NVIDIA and Neuron) and all Bottlerocket AMIs include the host-level components required to use EFA. The EKS AL2023 and Bottlerocket AMIs do not include the EFA device plugin, and the device plugin must be installed separately on your cluster before deploying workloads that use EFA.

## Install the EFA Kubernetes device plugin

The EFA device plugin advertises EFA devices as `vpc.amazonaws.com/efa` extended resources. You request EFA devices in container resource requests and limits. For a complete walkthrough of setting up EFA with training workloads, see [Run machine learning training on Amazon EKS with Elastic Fabric Adapter](node-efa.md "node-efa.md").

The EFA device plugin automatically allocates EFA devices that are topologically close to Neuron accelerators and NVIDIA GPUs on the physical EC2 instance.

### Prerequisites

- An Amazon EKS cluster.
- Nodes with EFA-enabled Amazon EC2 instance types. For a list of supported instance types, see [Supported instance types](../../../AWSEC2/latest/UserGuide/efa.md#efa-instance-types "../../../AWSEC2/latest/UserGuide/efa.md#efa-instance-types") in the _Amazon EC2 User Guide_.
- Nodes with host-level components installed for EFA. These are included if using the EKS AL2023 accelerated AMIs or the EKS Bottlerocket AMIs.
- Helm installed in your command-line environment, see the [Setup Helm instructions](helm.md "helm.md") for more information.
- `kubectl` configured to communicate with your cluster, see [Install or update kubectl](install-kubectl.md#kubectl-install-update "install-kubectl.md#kubectl-install-update") for more information.

### Procedure

1. Add the EKS Helm chart repository.

```
helm repo add eks https://aws.github.io/eks-charts
```

2. Update your local Helm repository.

```
helm repo update
```

3. Install the EFA device plugin.

```
helm install efa eks/aws-efa-k8s-device-plugin -n kube-system
```

4. Verify the EFA device plugin DaemonSet is running.

```
kubectl get daemonset -n kube-system aws-efa-k8s-device-plugin-daemonset
```

```
NAME                                  DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR   AGE
aws-efa-k8s-device-plugin-daemonset   2         2         2       2            2           <none>          60s
```

5. Verify that your nodes have allocatable EFA resources.

```
kubectl get nodes "-o=custom-columns=NAME:.metadata.name,EFA:.status.allocatable.vpc\.amazonaws\.com/efa"
```

```
NAME                                           EFA
ip-192-168-11-225.us-west-2.compute.internal   4
ip-192-168-24-96.us-west-2.compute.internal    4
```

### Request EFA devices in a Pod

To request EFA devices using the device plugin, specify the `vpc.amazonaws.com/efa` resource in your container resource requests or limits.

```
apiVersion: v1
kind: Pod
metadata:
  name: efa-workload
spec:
  containers:
  - name: app
    ...
    resources:
      limits:
        vpc.amazonaws.com/efa: 4
        hugepages-2Mi: ...
      requests:
        vpc.amazonaws.com/efa: 4
        hugepages-2Mi: ...
```
