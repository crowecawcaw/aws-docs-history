

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Detect node health issues and enable automatic node repair
<a name="node-health"></a>

Node health refers to the operational status and capability of a Kubernetes node to effectively run workloads. A healthy node maintains expected network connectivity, has sufficient compute and storage resources, and can successfully run workloads without disruption.

To help with maintaining healthy nodes in EKS clusters, EKS offers the *node monitoring agent* and *automatic node repair*. These features are automatically enabled with EKS Auto Mode compute. You can also use automatic node repair with EKS managed node groups and Karpenter, and can use the EKS node monitoring agent with any EKS compute types except for AWS Fargate. The EKS node monitoring agent and automatic node repair are most effective when used together, but they can also be used individually in EKS clusters.

**Important**  
The *node monitoring agent* and *node auto repair* are only available on Linux. These features aren’t available on Windows.

## Node monitoring agent
<a name="node-monitoring-agent"></a>

The EKS node monitoring agent reads node logs to detect health issues. It parses logs to detect failures and surfaces status information about the health status of the nodes. For each category of issues detected, the agent applies a dedicated `NodeCondition` to the worker nodes. For detailed information on the node health issues detected by the EKS node monitoring agent, see [Detect node health issues with the EKS node monitoring agent](node-health-nma.md).

EKS Auto Mode compute includes the node monitoring agent. For other EKS compute types, you can add the node monitoring agent as an EKS add-on or you can manage it with Kubernetes tooling such as Helm. For more information, see [Configure the node monitoring agent](node-health-nma.md#node-monitoring-agent-configure).

With the EKS node monitoring agent, the following categories of node health issues are surfaced as node conditions. Note, `Ready`, `DiskPressure`, and `MemoryPressure` are standard Kubernetes node conditions that are surfaced even without the EKS node monitoring agent.


| Node Condition | Description | 
| --- | --- | 
| AcceleratedHardwareReady | AcceleratedHardwareReady indicates whether accelerated hardware (GPU, Neuron) on the node is functioning correctly. | 
| ContainerRuntimeReady | ContainerRuntimeReady indicates whether the container runtime (containerd, etc.) is functioning correctly and able to run containers. | 
| DiskPressure | DiskPressure is a standard Kubernetes condition indicating the node is experiencing disk pressure (low disk space or high I/O). | 
| KernelReady | KernelReady indicates whether the kernel is functioning correctly without critical errors, panics, or resource exhaustion. | 
| MemoryPressure | MemoryPressure is a standard Kubernetes condition indicating the node is experiencing memory pressure (low available memory). | 
| NetworkingReady | NetworkingReady indicates whether the node’s networking stack is functioning correctly (interfaces, routing, connectivity). | 
| StorageReady | StorageReady indicates whether the node’s storage subsystem is functioning correctly (disks, filesystems, I/O). | 
| Ready | Ready is the standard Kubernetes condition indicating the node is healthy and ready to accept pods. | 

## Automatic node repair
<a name="node-auto-repair"></a>

EKS automatic node repair continuously monitors node health, reacts to detected problems, and replaces or reboots nodes when possible. This improves cluster reliability with minimal manual intervention and helps reduce application downtime.

By itself, EKS automatic node repair reacts to the `Ready` conditions of the kubelet, any manually deleted node objects, and EKS managed node group instances that fail to join the cluster. When EKS automatic node repair is enabled with the node monitoring agent installed, EKS automatic node repair reacts to additional node conditions: `AcceleratedHardwareReady`, `ContainerRuntimeReady`, `KernelReady`, `NetworkingReady`, and `StorageReady`.

EKS automatic node repair does not react to standard Kubernetes `DiskPressure`, `MemoryPressure`, or `PIDPressure` node conditions. These conditions often indicate issues with application behavior, workload configuration, or resource limits rather than node-level failures, making it difficult to determine an appropriate default repair action. In these scenarios, workloads are subject to the Kubernetes [node pressure eviction behavior](https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction).

For more information on EKS automatic node repair, see [Automatically repair nodes in EKS clusters](node-repair.md).

**Topics**