**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Manage Neuron devices on Amazon EKS

AWS Trainium and AWS Inferentia are purpose-built machine learning chips designed by AWS. Amazon EKS supports two mechanisms for managing Neuron devices in EKS clusters: the _Neuron DRA driver_ and the _Neuron Kubernetes device plugin_.

We recommend using DRA drivers for new deployments with Kubernetes versions 1.34 and later when using [static capacity provisioning](https://karpenter.sh/docs/concepts/nodepools/#static-nodepool "https://karpenter.sh/docs/concepts/nodepools/#static-nodepool") in Karpenter, EKS managed node groups, or self-managed nodes. DRA is not currently supported with EKS Auto Mode. The Neuron DRA driver provides topology-aware allocation, connected device subset scheduling, Logical NeuronCore (LNC) configuration, and UltraServer multi-node allocation without requiring custom scheduler extensions.

## Neuron DRA driver vs. Neuron device plugin

| Feature                       | Neuron DRA driver                                                                                                          | Neuron device plugin                                                                                                                                                                                                                                                                        |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Minimum Kubernetes version    | 1.34                                                                                                                       | All EKS-supported Kubernetes versions                                                                                                                                                                                                                                                       |
| EKS Compute                   | Karpenter (static capacity only), managed node groups, self-managed nodes                                                  | EKS Auto Mode, Karpenter, managed node groups, self-managed nodes                                                                                                                                                                                                                           |
| EKS-optimized AMI support     | AL2023 (Neuron), Bottlerocket                                                                                              | AL2023 (Neuron), Bottlerocket                                                                                                                                                                                                                                                               |
| Device advertisement          | Rich attributes via `ResourceSlice` objects including device ID, instance type, topology, driver version, and EFA locality | Integer count of `aws.amazon.com/neuron` and `aws.amazon.com/neuroncore` extended resources                                                                                                                                                                                                 |
| Connected device subsets      | Allocate subsets of 1, 4, 8, or 16 connected Neuron devices using topology constraints                                     | Requires the [Neuron scheduler extension](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/containers/tutorials/k8s-neuron-scheduler.html "https://awsdocs-neuron.readthedocs-hosted.com/en/latest/containers/tutorials/k8s-neuron-scheduler.html") for contiguous device allocation |
| LNC configuration             | Per-workload Logical NeuronCore configuration (LNC=1 or LNC=2) through `ResourceClaimTemplate` parameters                  | Requires pre-configuration in EC2 launch templates                                                                                                                                                                                                                                          |
| Attribute-based selection     | Filter devices by instance type, driver version, and other attributes using CEL expressions                                | Not supported                                                                                                                                                                                                                                                                               |
| Topology-aware EFA allocation | DRA-native topology-awareness                                                                                              | Automatic topology-awareness (EKS-optimized AL2023 AMIs only)                                                                                                                                                                                                                               |

## Install the Neuron DRA driver

The Neuron DRA driver advertises Neuron devices as `ResourceSlice` objects with the `DeviceClass` name `neuron.aws.com`. The driver runs as a DaemonSet and automatically discovers Neuron devices and their topology attributes.

Detailed information about the Neuron DRA driver is available in the [Neuron DRA documentation](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/containers/neuron-dra.html#neuron-dra-driver-attributes-reference "https://awsdocs-neuron.readthedocs-hosted.com/en/latest/containers/neuron-dra.html#neuron-dra-driver-attributes-reference").

### Prerequisites

- An Amazon EKS cluster running Kubernetes version 1.34 or later with static capacity provisioned by Karpenter, EKS managed node groups, or self-managed node groups.
- Nodes with AWS Trainium or Inferentia2 instance types.
- Helm installed in your command-line environment, see the [Setup Helm instructions](helm.md "helm.md") for more information.
- `kubectl` configured to communicate with your cluster, see [Install or update kubectl](install-kubectl.md#kubectl-install-update "install-kubectl.md#kubectl-install-update") for more information.

### Procedure

###### Important

Do not install the Neuron DRA driver on nodes where the Neuron device plugin is running. The two mechanisms cannot coexist on the same node. Doing so can cause silent oversubscription of the underlying devices to multiple pods on the same node.

1. Install the Neuron DRA driver using Helm.

```
helm upgrade --install neuron-helm-chart oci://public.ecr.aws/neuron/neuron-helm-chart \
    --namespace neuron-dra-driver \
    --create-namespace \
    --set "devicePlugin.enabled=false" \
    --set "npd.enabled=false" \
    --set "draDriver.enabled=true"
```

The driver is deployed as a DaemonSet in the `neuron-dra-driver` namespace by default with the `DeviceClass`
`neuron.aws.com`. 2. Verify that the DRA driver DaemonSet is running.

```
kubectl get ds -n neuron-dra-driver neuron-dra-driver-kubelet-plugin
```

```
NAME                              DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR   AGE
neuron-dra-driver-kubelet-plugin  1         1         1       1            1           <none>          60s
```

3. Verify that the `DeviceClass` was created.

```
kubectl get deviceclass neuron.aws.com
```

```
NAME            AGE
neuron.aws.com  60s
```

4. Verify that `ResourceSlice` objects are advertised for your nodes.

```
kubectl get resourceslice
```

See the [Neuron DRA documentation](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/containers/neuron-dra.html#neuron-dra-driver-attributes-reference "https://awsdocs-neuron.readthedocs-hosted.com/en/latest/containers/neuron-dra.html#neuron-dra-driver-attributes-reference") for information on the available `ResourceSlice` object attributes.

### Request Neuron devices in a Pod

To request Neuron devices using the DRA driver, create a `ResourceClaimTemplate` that references the `neuron.aws.com`
`DeviceClass` and reference it in your Pod specification.

The following example requests all Neuron devices on a `trn2.48xlarge` instance:

```
apiVersion: resource.k8s.io/v1
kind: ResourceClaimTemplate
metadata:
  name: all-neurons
spec:
  spec:
    devices:
      requests:
      - name: neurons
        exactly:
          deviceClassName: neuron.aws.com
          selectors:
          - cel:
              expression: "device.attributes['neuron.aws.com'].instanceType == 'trn2.48xlarge'"
          allocationMode: All
---
apiVersion: v1
kind: Pod
metadata:
  name: neuron-workload
spec:
  containers:
  - name: app
    ...
    resources:
      claims:
      - name: neurons
  resourceClaims:
  - name: neurons
    resourceClaimTemplateName: all-neurons
```

### Allocate connected device subsets

The Neuron DRA driver can allocate subsets of connected Neuron devices without requiring the [Neuron scheduler extension](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/containers/tutorials/k8s-neuron-scheduler.html "https://awsdocs-neuron.readthedocs-hosted.com/en/latest/containers/tutorials/k8s-neuron-scheduler.html"). Supported subset sizes are 1, 4, 8, or 16 devices. Use the `matchAttribute` constraint with a topology group ID to ensure devices are connected.

The following example requests 4 connected Neuron devices:

```
apiVersion: resource.k8s.io/v1
kind: ResourceClaimTemplate
metadata:
  name: 1x4-connected-neurons
spec:
  spec:
    devices:
      requests:
      - name: neurons
        exactly:
          deviceClassName: neuron.aws.com
          allocationMode: ExactCount
          count: 4
          selectors:
          - cel:
              expression: "device.attributes['neuron.aws.com'].instanceType == 'trn2.48xlarge'"
      constraints:
      - requests: ["neurons"]
        matchAttribute: "resource.aws.com/devicegroup4_id"
```

The supported `matchAttribute` values for connected subsets are `resource.aws.com/devicegroup1_id`, `resource.aws.com/devicegroup4_id`, `resource.aws.com/devicegroup8_id`, and `resource.aws.com/devicegroup16_id`. The number in the `devicegroup` attribute name corresponds to the number of Neuron devices in the connected topology group. For example, `resource.aws.com/devicegroup1_id` identifies a single Neuron device, `resource.aws.com/devicegroup4_id` identifies a group of 4 connected devices, and `resource.aws.com/devicegroup8_id` and `resource.aws.com/devicegroup16_id` identify groups of 8 and 16 connected devices respectively. Choose the `matchAttribute` that matches the device `count` in your request so that the allocated devices belong to the same connected topology group. For more information on these attributes, see the [Neuron DRA driver documentation](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/containers/neuron-dra.html "https://awsdocs-neuron.readthedocs-hosted.com/en/latest/containers/neuron-dra.html").

### Configure Logical NeuronCores (LNC)

The Neuron DRA driver allows per-workload Logical NeuronCore configuration through `ResourceClaimTemplate` parameters. This eliminates the need to pre-configure LNC in EC2 Launch Templates.

The following example requests all Neuron devices with LNC set to 1:

```
apiVersion: resource.k8s.io/v1
kind: ResourceClaimTemplate
metadata:
  name: all-neurons-lnc-1
spec:
  spec:
    devices:
      requests:
      - name: neurons
        exactly:
          deviceClassName: neuron.aws.com
          selectors:
          - cel:
              expression: "device.attributes['neuron.aws.com'].instanceType == 'trn2.48xlarge'"
          allocationMode: All
      config:
      - requests: ["neurons"]
        opaque:
          driver: neuron.aws.com
          parameters:
            apiVersion: neuron.aws.com/v1
            kind: NeuronConfig
            logicalNeuronCore: 1
```

### Allocate Neuron devices with aligned EFA interfaces

See [Topology-aware EFA and GPU/Neuron device allocation](device-management-efa.md#efa-dra-topology-aware "device-management-efa.md#efa-dra-topology-aware")

## Install the Neuron Kubernetes device plugin

The Neuron Kubernetes device plugin advertises Neuron devices as `aws.amazon.com/neuron` and NeuronCores as `aws.amazon.com/neuroncore` extended resources. You request Neuron devices in container resource requests and limits.

### Prerequisites

- An Amazon EKS cluster.
- Nodes with host-level components installed for AWS Trainium or AWS Inferentia instances. These are included if using the EKS AL2023 accelerated AMIs or the EKS Bottlerocket AMIs.
- Helm installed in your command-line environment, see the [Setup Helm instructions](helm.md "helm.md") for more information.
- `kubectl` configured to communicate with your cluster, see [Install or update kubectl](install-kubectl.md#kubectl-install-update "install-kubectl.md#kubectl-install-update") for more information.

### Procedure

1. Install the Neuron Kubernetes device plugin using Helm.

```
helm upgrade --install neuron-helm-chart oci://public.ecr.aws/neuron/neuron-helm-chart \
    --set "npd.enabled=false"
```

2. Verify the Neuron device plugin DaemonSet is running.

```
kubectl get ds -n kube-system neuron-device-plugin
```

```
NAME                   DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR   AGE
neuron-device-plugin   1         1         1       1            1           <none>          60s
```

3. Verify that your nodes have allocatable Neuron devices.

```
kubectl get nodes "-o=custom-columns=NAME:.metadata.name,NeuronDevice:.status.allocatable.aws\.amazon\.com/neuron,NeuronCore:.status.allocatable.aws\.amazon\.com/neuroncore"
```

```
NAME                                           NeuronDevice   NeuronCore
ip-192-168-47-173.us-west-2.compute.internal   1              2
```

### Verify Neuron devices with a test Pod

You can verify that Neuron devices are accessible by running the `neuron-ls` tool in a test Pod.

1. Create a file named `neuron-ls.yaml` with the following contents. This manifest launches an [Neuron Monitor](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/tools/neuron-sys-tools/neuron-monitor-user-guide.html "https://awsdocs-neuron.readthedocs-hosted.com/en/latest/tools/neuron-sys-tools/neuron-monitor-user-guide.html") container that has the `neuron-ls` tool installed.

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
      requests:
        aws.amazon.com/neuron: 1
  tolerations:
  - key: "aws.amazon.com/neuron"
    operator: "Exists"
    effect: "NoSchedule"
```

2. Apply the manifest.

```
kubectl apply -f neuron-ls.yaml
```

3. After the Pod has finished running, view its logs.

```
kubectl logs neuron-ls
```

An example output is as follows.

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

###### Note

When using the Neuron device plugin, contiguous device allocation on instances with multiple Neuron devices (such as `trn2.48xlarge`) requires the [Neuron Kubernetes scheduler extension](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/containers/tutorials/k8s-neuron-scheduler.html "https://awsdocs-neuron.readthedocs-hosted.com/en/latest/containers/tutorials/k8s-neuron-scheduler.html"). The Neuron DRA driver handles this automatically through topology constraints.

For more information about using Neuron devices with Amazon EKS, see the [Neuron documentation for running on EKS](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/containers/kubernetes-getting-started.html "https://awsdocs-neuron.readthedocs-hosted.com/en/latest/containers/kubernetes-getting-started.html").
