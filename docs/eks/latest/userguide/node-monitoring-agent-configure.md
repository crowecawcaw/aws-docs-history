

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Configure the Amazon EKS node monitoring agent
<a name="node-monitoring-agent-configure"></a>

The EKS node monitoring agent is deployed as a DaemonSet. For the node health issues that the agent detects, see [Detect node health issues with the EKS node monitoring agent](node-health-nma.md).

The configuration values in this topic are Helm chart values, and you can set them whether you install the agent as an EKS add-on or manage it with Kubernetes tooling such as Helm. With an EKS add-on, you pass them as the add-on’s configuration values. The EKS add-on accepts the subset of chart values in its configuration schema and rejects any others. For the full set of values and their defaults, see the EKS node monitoring agent [Helm chart](https://github.com/aws/eks-node-monitoring-agent/blob/main/charts/eks-node-monitoring-agent/values.yaml).

## Agent configuration values
<a name="nma-configure-agent"></a>

You can customize the agent installation with the following configuration values.


| Configuration Option | Description | 
| --- | --- | 
|  `nodeAgent.resources.requests.cpu`  | CPU resource request for the agent. | 
|  `nodeAgent.resources.requests.memory`  | Memory resource request for the agent. | 
|  `nodeAgent.resources.limits.cpu`  | CPU resource limit for the agent. | 
|  `nodeAgent.resources.limits.memory`  | Memory resource limit for the agent. | 
|  `nodeAgent.resizePolicy`  | Resource resize policy for the agent container. | 
|  `nodeAgent.tolerations`  | Tolerations for scheduling the agent on tainted nodes. | 
|  `nodeAgent.nodeSelector`  | Node labels that a node must have for the agent Pod to be scheduled on it. | 
|  `nodeAgent.affinity`  | Pod affinities for the agent. | 
|  `nodeAgent.priorityClassName`  | Name of an existing PriorityClass assigned to the agent Pod. Defaults to `system-node-critical`. | 
|  `nodeAgent.podLabels`  | Labels applied to the agent Pod. Merged with `global.podLabels`, and these take precedence on a conflict. | 
|  `nodeAgent.podAnnotations`  | Annotations applied to the agent Pod. Merged with `global.podAnnotations`, and these take precedence on a conflict. | 
|  `nodeAgent.probePort`  | Health probe port for the agent. Defaults to `8002`. Used for both the `--probe-address` argument and the liveness probe. | 
|  `nodeAgent.dcgmAddress`  | Address of an existing DCGM host engine as `host:port`. When empty, the agent uses `localhost:5555`, which is where the bundled `dcgm-server` DaemonSet listens. See [Use an existing NVIDIA DCGM host engine](#nma-configure-byo-dcgm). | 
|  `nodeAgent.ipamdIntrospectionAddress`  | IPAMD introspection API address as `host:port`. When empty, the agent uses `localhost:61679`. Set this when the Amazon VPC CNI is configured with `INTROSPECTION_BIND_ADDRESS`. | 
|  `nodeAgent.dnsPolicy`  | DNS policy for the agent Pod. Valid values: `ClusterFirst`, `ClusterFirstWithHostNet`, `Default`. Set `ClusterFirstWithHostNet` when `dcgmAddress` uses a Kubernetes Service hostname. | 
|  `nodeAgent.nvidiaDriverRoot`  | Override for the NVIDIA driver root path. Only needed when the NVIDIA GPU Operator uses a non-default driver install directory. | 
|  `nodeAgent.monitors`  | Per-monitor configuration, keyed by plugin name. For example, set `nodeAgent.monitors.nvidia.enabled` to `false` to unregister the NVIDIA monitor. | 
|  `nodeAgent.additionalArgs`  | Additional command-line arguments to pass to the agent. | 

**Note**  
These configuration values apply to agent version `v1.6.0` (add-on version `v1.6.0-eksbuild.1`) and later. Earlier chart versions used a `monitoringAgent` key instead of `nodeAgent`. To confirm the values that your add-on version accepts, see [Get add-on versions and the configuration schema](#nma-configure-versions).

You can pass any of the agent’s command-line arguments that don’t have a dedicated configuration value, such as `hostname-override` and `verbosity`, through `nodeAgent.additionalArgs` with EKS add-ons or a Helm installation.

```
aws eks update-addon \
  --cluster-name my-cluster \
  --addon-name eks-node-monitoring-agent \
  --configuration-values '{"nodeAgent":{"additionalArgs":["--verbosity=4"]}}'
```

To change the health probe port, set `nodeAgent.probePort` rather than passing `--probe-address` through `nodeAgent.additionalArgs`. The chart always passes `--probe-address` and uses the same port for the agent’s liveness probe, so setting the port through `nodeAgent.probePort` keeps the two consistent.

## NVIDIA DCGM configuration values
<a name="nma-configure-dcgm"></a>

On NVIDIA GPU nodes, the EKS node monitoring agent collects GPU health from NVIDIA DCGM (Data Center GPU Manager). The agent connects as a DCGM client in standalone mode, so an `nv-hostengine` process must be reachable on the node. By default the chart provides one through the `dcgm-server` DaemonSet, which the agent reaches on `localhost:5555`. This component runs only on NVIDIA GPU instance types, as shown by the `nodeAffinity` in the agent’s [Helm chart](https://github.com/aws/eks-node-monitoring-agent/blob/main/charts/eks-node-monitoring-agent/values.yaml).

If your cluster already runs `nv-hostengine` on each GPU node, you can point the agent at it instead of running a second instance. For more information, see [Use an existing NVIDIA DCGM host engine](#nma-configure-byo-dcgm).

EKS Auto Mode includes the EKS node monitoring agent in the node AMI. There is no `eks-node-monitoring-agent` add-on to install and no separate `dcgm-server` Pod. On all other compute types, the add-on runs the DCGM host engine in a `dcgm-server` DaemonSet on NVIDIA GPU nodes.

The `dcgm-server` DaemonSet must be able to schedule on your GPU nodes. If it can’t, the EKS node monitoring agent can’t reach `nv-hostengine` and reports `AcceleratedHardwareReady=False` with the reason `DCGMError`. On EKS Auto Mode and self-managed Karpenter, automatic node repair acts on that condition and can replace otherwise healthy GPU nodes after each wait period. EKS managed node groups don’t repair `DCGMError` by default. For more information, see [How the repair action is chosen](node-repair.md#node-repair-reason-vs-status).

In agent version `v1.7.3` (add-on version `v1.7.3-eksbuild.1`) and later, `dcgmAgent.tolerations` defaults to a toleration for the `nvidia.com/gpu` taint key with any effect, so `dcgm-server` schedules on GPU nodes that carry the standard NVIDIA device plugin taint without additional configuration.

**Important**  
In agent versions earlier than `v1.7.3`, `dcgmAgent.tolerations` is empty by default. If your GPU nodes carry a taint, such as `nvidia.com/gpu:NoSchedule`, either upgrade the add-on or set `dcgmAgent.tolerations` to match the taints on your nodes before you enable automatic node repair. If your GPU nodes carry a custom taint with a different key, set `dcgmAgent.tolerations` on any agent version.

**Note**  
The EKS node monitoring agent’s DCGM component is separate from the NVIDIA DCGM Exporter that you install for GPU metrics in [Step 3: Create the monitoring stack](ml-cluster-setup-cli.md#cluster-setup-cli-monitoring). The DCGM Exporter exports Prometheus metrics and is not involved in node health detection or node repair.

You can customize the NVIDIA DCGM installation with the following configuration values.


| Configuration Option | Description | 
| --- | --- | 
|  `dcgmAgent.resources.requests.cpu`  | CPU resource request for the DCGM agent. | 
|  `dcgmAgent.resources.requests.memory`  | Memory resource request for the DCGM agent. | 
|  `dcgmAgent.resources.limits.cpu`  | CPU resource limit for the DCGM agent. | 
|  `dcgmAgent.resources.limits.memory`  | Memory resource limit for the DCGM agent. | 
|  `dcgmAgent.resizePolicy`  | Resource resize policy for the DCGM agent container. | 
|  `dcgmAgent.tolerations`  | Tolerations for scheduling the DCGM agent on tainted nodes. In agent version `v1.7.3` and later, this defaults to a toleration for the `nvidia.com/gpu` taint key. Setting this value replaces the default, so include the `nvidia.com/gpu` toleration if your nodes also carry that taint. | 
|  `dcgmAgent.nodeSelector`  | Node labels that a node must have for the DCGM agent Pod to be scheduled on it. | 
|  `dcgmAgent.affinity`  | Pod affinities for the DCGM agent. | 
|  `dcgmAgent.priorityClassName`  | Name of an existing PriorityClass assigned to the DCGM agent Pod. Defaults to `system-node-critical`. | 
|  `dcgmAgent.podLabels`  | Labels applied to the DCGM agent Pod. Merged with `global.podLabels`, and these take precedence on a conflict. | 
|  `dcgmAgent.podAnnotations`  | Annotations applied to the DCGM agent Pod. Merged with `global.podAnnotations`, and these take precedence on a conflict. | 
|  `dcgmAgent.enabled`  | Whether to deploy the bundled `dcgm-server` DaemonSet. Defaults to `true`. | 

You can also set `global.podLabels` and `global.podAnnotations` to apply labels and annotations to every Pod that the chart deploys.

If you run an agent version earlier than `v1.7.3`, the following AWS CLI example updates the add-on so that `dcgm-server` tolerates the `nvidia.com/gpu` taint. If your GPU nodes carry a custom taint, replace the `key` value with the key of that taint.

```
aws eks update-addon \
  --cluster-name my-cluster \
  --addon-name eks-node-monitoring-agent \
  --configuration-values '{"dcgmAgent":{"tolerations":[{"key":"nvidia.com/gpu","operator":"Exists"}]}}'
```

After the add-on update completes, verify that a `dcgm-server` Pod is running on each GPU node.

```
kubectl get pods -n kube-system -l k8s-app=dcgm-server -o wide
```

## Use an existing NVIDIA DCGM host engine
<a name="nma-configure-byo-dcgm"></a>

If your cluster already runs an `nv-hostengine` process on each GPU node, you can configure the EKS node monitoring agent to use it instead of the bundled `dcgm-server` DaemonSet. One example is the NVIDIA GPU Operator with standalone DCGM enabled, which exposes a per-node host engine through a node-local `nvidia-dcgm` Service. NVIDIA recommends standalone mode when multiple clients interact with DCGM, so a single host engine per node is recommended over running two instances. For more information, see [Standalone mode](https://docs.nvidia.com/datacenter/dcgm/latest/user-guide/getting-started.html#standalone-mode) in the *NVIDIA DCGM documentation*.

This configuration requires agent version `v1.7.1` (add-on version `v1.7.1-eksbuild.1`) or later. EKS Auto Mode doesn’t support it, because the agent is built into the node AMI and isn’t configurable.

To use an existing host engine, set the following configuration values.

1. Set `dcgmAgent.enabled` to `false` so that the chart doesn’t deploy its own `dcgm-server` DaemonSet.

1. Set `nodeAgent.dcgmAddress` to the `host:port` address of your existing host engine.

1. If that address is a Kubernetes Service hostname, set `nodeAgent.dnsPolicy` to `ClusterFirstWithHostNet`. The agent Pod uses host networking, so without this value it resolves names with the host’s DNS configuration and can’t resolve Service hostnames.

The following example points the agent at the GPU Operator’s `nvidia-dcgm` Service.

```
{
  "dcgmAgent": {
    "enabled": false
  },
  "nodeAgent": {
    "dcgmAddress": "nvidia-dcgm.gpu-operator.svc:5555",
    "dnsPolicy": "ClusterFirstWithHostNet"
  }
}
```

Apply it to the EKS add-on with the following command.

```
aws eks update-addon \
  --cluster-name my-cluster \
  --addon-name eks-node-monitoring-agent \
  --configuration-values '{"dcgmAgent":{"enabled":false},"nodeAgent":{"dcgmAddress":"nvidia-dcgm.gpu-operator.svc:5555","dnsPolicy":"ClusterFirstWithHostNet"}}'
```

After the update completes, confirm that the agent reports GPU health through the external host engine. Your GPU nodes should report `AcceleratedHardwareReady=True`, and no `dcgm-server` Pods should be running.

```
kubectl get pods -n kube-system -l k8s-app=dcgm-server
kubectl get nodes -o custom-columns='NAME:.metadata.name,ACCEL:.status.conditions[?(@.type=="AcceleratedHardwareReady")].status,REASON:.status.conditions[?(@.type=="AcceleratedHardwareReady")].reason'
```

**Important**  
If you set `dcgmAgent.enabled` to `false` without providing a reachable `nodeAgent.dcgmAddress`, the agent can’t connect to a host engine and reports `AcceleratedHardwareReady=False` with the reason `DCGMError` shortly after startup. On EKS Auto Mode and self-managed Karpenter, automatic node repair can replace otherwise healthy GPU nodes as a result. For more information, see [How the repair action is chosen](node-repair.md#node-repair-reason-vs-status).

To disable GPU health monitoring entirely rather than redirect it, disable the bundled server and the NVIDIA monitor together. Disabling the server alone leaves the monitor registered, which produces the `DCGMError` condition described previously.

```
{
  "dcgmAgent": {
    "enabled": false
  },
  "nodeAgent": {
    "monitors": {
      "nvidia": {
        "enabled": false
      }
    }
  }
}
```

## Get add-on versions and the configuration schema
<a name="nma-configure-versions"></a>

You can use the following AWS CLI commands to get useful information about the versions and schema for the EKS node monitoring agent EKS add-on.

Get the latest agent add-on version for your Kubernetes version. Replace `1.35` with your Kubernetes version.

```
aws eks describe-addon-versions \
  --addon-name eks-node-monitoring-agent \
  --kubernetes-version 1.35 \
  --query='addons[].addonVersions[].addonVersion'
```

Get the agent add-on schema supported in EKS add-ons. This returns the configuration values that the version you specify accepts. Replace `v1.7.3-eksbuild.1` with your agent version.

```
aws eks describe-addon-configuration \
  --addon-name eks-node-monitoring-agent \
  --addon-version v1.7.3-eksbuild.1 \
  --query 'configurationSchema' --output text
```