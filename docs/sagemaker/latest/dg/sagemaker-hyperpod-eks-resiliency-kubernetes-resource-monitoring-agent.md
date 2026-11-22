

# Kubernetes Resource Monitoring Agent

The Amazon SageMaker HyperPod Kubernetes Resource Monitoring Agent helps you keep large training clusters healthy. One agent in the cluster continuously watches all nodes, pods, DaemonSets, and distributed training jobs. It reports problems as Kubernetes events, structured Amazon CloudWatch logs, and HyperPod cluster events that you can receive in Amazon EventBridge. With this agent, you and HyperPod get real-time visibility into cluster-level issues that can disrupt large-scale training, such as degraded nodes, crash-looping infrastructure pods, missing device plugins, failed training jobs, and stalled GPU collective communication.

This agent works alongside the HyperPod health monitoring and recovery functions. It complements the on-host Health Monitoring Agent and the HyperPod training operator. For more information about these components, see [Health Monitoring System](sagemaker-hyperpod-eks-resiliency-health-monitoring-agent.md) and [Using the HyperPod training operator](sagemaker-eks-operator.md).

The three components cover different layers:
+ The **Health Monitoring Agent** runs on each node and detects hardware and host-level faults, such as NVIDIA GPU errors, AWS Trainium errors, and Amazon EC2 platform errors. When it detects a fault, the HyperPod node recovery system can label, taint, and replace or reboot the node automatically.
+ The **Kubernetes Resource Monitoring Agent** runs once per cluster and detects Kubernetes cluster-level health issues across all nodes, pods, DaemonSets, and training jobs.
+ The **HyperPod training operator** runs distributed training jobs and recovers them from process-level faults.

**Note**  
The Kubernetes Resource Monitoring Agent is an observability component. It detects and reports issues. It does not remediate nodes or workloads, because the application workload might cause an issue.  
It runs only on HyperPod-managed nodes. If the agent starts on a node that HyperPod does not manage, it logs a message and exits.

## Supported versions
<a name="sagemaker-hyperpod-eks-resiliency-kubernetes-resource-monitoring-agent-supported-versions"></a>

This agent works with the Kubernetes versions that HyperPod supports. For more information about the supported versions, see [Getting started with Amazon EKS support in SageMaker HyperPod](sagemaker-hyperpod-eks-prerequisites.md).

The agent monitors the following distributed training job types. Each job monitor turns itself off if the corresponding custom resource definition (CRD) is not installed in the cluster.


| Job type | API resource | Default state | 
| --- | --- | --- | 
| HyperPod PyTorchJob | sagemaker.amazonaws.com/v1 hyperpodpytorchjobs | Turned on | 
| Kubeflow TrainJob (Trainer v2) | trainer.kubeflow.org/v1alpha1 trainjobs | Turned on | 
| Kubeflow PyTorchJob (v1, legacy) | kubeflow.org/v1 pytorchjobs | Turned on by the Helm chart | 

## How the Kubernetes Resource Monitoring Agent works
<a name="sagemaker-hyperpod-eks-resiliency-kubernetes-resource-monitoring-agent-how-it-works"></a>

This agent runs as a single-replica Kubernetes `Deployment` in the `aws-hyperpod` namespace. It uses cluster-wide Kubernetes informers to watch resources across the cluster from one place. By default, it avoids common NVIDIA GPU instance types, such as ml.p5 and ml.g6 types, so that it does not use GPU capacity reserved for training.

At startup, the agent does the following:

1. Initializes structured logging to the node's log volume.

1. Starts an HTTP health server on port `8081`. Kubernetes probes can reach the agent from this point.

1. Creates in-cluster Kubernetes API clients.

1. Runs the HyperPod validation check. The agent checks that the node's Amazon EC2 provider ID matches the HyperPod pattern. If HyperPod does not manage the node, the agent logs a message and exits with code `0`.

1. Starts all turned-on monitors and waits until the core Kubernetes caches (Node, Pod, DaemonSet) have synced. Training-job CRD caches sync in the background, so the agent starts even if optional job CRDs are not installed.

1. Becomes ready after its first healthy monitoring cycle. The readiness probe (`/readyz`) then returns `200`.

When the agent detects a problem, it records a Kubernetes event on the affected object and writes a structured log entry. It also keeps a current health report for HyperPod components and instances, which HyperPod uses to send you cluster events. For more information, see [How the agent reports issues](#sagemaker-hyperpod-eks-resiliency-kubernetes-resource-monitoring-agent-reporting).

## Health checks performed by the Kubernetes Resource Monitoring Agent
<a name="sagemaker-hyperpod-eks-resiliency-kubernetes-resource-monitoring-agent-checks"></a>

The agent runs the following continuous checks. You can turn each monitor on or off independently. For more information, see [Configuration reference](#sagemaker-hyperpod-eks-resiliency-kubernetes-resource-monitoring-agent-configuration).

### Nodes
<a name="sagemaker-hyperpod-eks-resiliency-kubernetes-resource-monitoring-agent-checks-nodes"></a>
+ **Node conditions** – Reports a problem when the `Ready` condition becomes `False` or `Unknown`, or when `MemoryPressure`, `DiskPressure`, `PIDPressure`, or `NetworkUnavailable` becomes `True` or `Unknown`.
+ **GPU capacity** – Detects when a node has fewer allocatable NVIDIA GPUs (`nvidia.com/gpu`) than its instance type provides. For an instance type that the agent does not know, or a node that uses Multi-Instance GPU (MIG), it detects when the allocatable count drops below the last count it saw, becomes zero, or disappears. A node that has just become Ready gets a 10-minute grace period.
+ **EFA capacity** – Detects the same conditions for Elastic Fabric Adapter (EFA) devices (`vpc.amazonaws.com/efa`), compared with the number of EFA devices that the instance type provides.
+ **GPU capability labels** – Reports when a GPU node loses its NVIDIA capability labels, which can indicate a device plugin or driver problem.
+ **Taints** – Detects when a taint is added to a node or when its effect changes. For `NoExecute` taints, it logs the pods and training jobs that might be evicted.
+ **Required HyperPod labels** – Verifies that HyperPod management labels are present. Newly seen nodes get a 5-minute grace period. The agent immediately reports labels that are removed from a previously labeled node.

### Pods
<a name="sagemaker-hyperpod-eks-resiliency-kubernetes-resource-monitoring-agent-checks-pods"></a>
+ **Critical infrastructure pods** – Reports failures, `CrashLoopBackOff`, container errors, and pods that have not been running for 5 minutes. Critical pods are DaemonSet-owned pods in the `kube-system`, `aws-hyperpod`, `kubeflow`, and `nvidia-gpu-addon` namespaces, Kubeflow training operator pods (label `control-plane: kubeflow-training-operator`), and the agent's own pod.
+ **Container restarts** – Detects increasing restart counts of critical infrastructure pods.
+ **Sustained unready pods** – When a critical pod stays not ready for 1 minute, the agent emits an event.
+ **Job association** – Maps each pod to its owning training job and node, so that problems can be correlated across resources.

The pod monitor watches only the namespaces in `monitoring.monitoredNamespaces`. The default is `aws-hyperpod`, `kube-system`, `default`, and `kubeflow`. To watch critical pods in another namespace, such as `nvidia-gpu-addon`, add it to the list.

### DaemonSets
<a name="sagemaker-hyperpod-eks-resiliency-kubernetes-resource-monitoring-agent-checks-daemonsets"></a>

The DaemonSet monitor watches DaemonSets in the `aws-hyperpod` and `kube-system` namespaces.
+ **Required DaemonSet presence** – Every 5 minutes, the agent verifies that the DaemonSets listed in `monitoring.necessaryDaemonsets` exist. By default, this is only the Health Monitoring Agent.
+ **Partial availability** – Reports when a DaemonSet has not had all of its desired pods available for 5 minutes.
+ **Rollout tracking** – Tracks DaemonSet rollout start and completion, and reports a rollout that has made no progress for 15 minutes.
+ **Misscheduled pods** – Reports when a DaemonSet has misscheduled pods.

### Distributed training jobs
<a name="sagemaker-hyperpod-eks-resiliency-kubernetes-resource-monitoring-agent-checks-jobs"></a>

The agent tracks the lifecycle of distributed training jobs and reports failures with the related node and pod context. On failure, it logs the failure reason and the affected pods and nodes. If NVIDIA Collective Communications Library (NCCL) Reliability, Availability, and Serviceability (RAS) monitoring is active, it also includes the job's NCCL RAS communication report.

### NCCL collective-communication health
<a name="sagemaker-hyperpod-eks-resiliency-kubernetes-resource-monitoring-agent-checks-nccl"></a>

When NCCL RAS monitoring is turned on, the agent checks the health of NCCL inter-GPU communication for each running training job. It periodically connects to the NCCL RAS daemon on each participating pod (TCP port `28028` by default), requests status, and combines the results for each endpoint into a job-level health state:
+ `healthy` – All endpoints respond with valid NCCL RAS data.
+ `degraded` – Some endpoints are unreachable or return invalid data, which indicates a partial loss of GPU communication.
+ `unhealthy` – All endpoints fail, which indicates that NCCL collective communication for the job might have stalled or stopped.

The agent queries only the training pods of a job. The training operator's pod-manager pods are not NCCL RAS endpoints.

NCCL RAS monitoring requires NCCL 2.24 or later. By default, NCCL listens for RAS clients on `localhost` only, so the agent cannot reach it from its own pod. To make the RAS socket reachable, set `NCCL_RAS_ADDR` to the pod IP address in each training container. The following example sets it from the pod IP address:

```yaml
env:
  - name: POD_IP
    valueFrom:
      fieldRef:
        fieldPath: status.podIP
  - name: NCCL_RAS_ADDR
    value: "$(POD_IP):28028"
```

If you change `monitoring.ncclRas.port`, use the same port in `NCCL_RAS_ADDR`.

The training job must run in a namespace that is listed in `monitoring.monitoredNamespaces`. The agent finds the training pods of a job through the pod monitor. For a job in another namespace, the agent has no NCCL RAS endpoints and the job-level state stays `no_data`.

**Important**  
With `NCCL_RAS_ADDR` set to the pod IP address, any pod in the cluster that can reach the training pods can query their NCCL RAS status. NVIDIA notes that binding RAS to an externally reachable interface has security implications. To limit access, use a Kubernetes NetworkPolicy that allows port `28028` only from the agent's pod.

A NetworkPolicy that selects the training pods denies all other incoming traffic to them, including the TCP traffic that NCCL uses between the job's pods. The policy must therefore also allow traffic between the pods of the job. EFA traffic does not use IP and is not affected. The following example allows both. Replace {{job-name}} with the name of your training job and {{job-namespace}} with its namespace:

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: {{job-name}}-nccl-ras
  namespace: {{job-namespace}}
spec:
  podSelector:
    matchLabels:
      HPJob: {{job-name}}
  policyTypes:
    - Ingress
  ingress:
    - from:
        - podSelector:
            matchLabels:
              HPJob: {{job-name}}
    - from:
        - namespaceSelector:
            matchLabels:
              kubernetes.io/metadata.name: aws-hyperpod
          podSelector:
            matchLabels:
              app: cluster-monitoring-agent
      ports:
        - protocol: TCP
          port: 28028
```

The example uses the `HPJob` label that the HyperPod training operator sets on training pods. For other job types, select the training pods with their own labels. On Amazon EKS, NetworkPolicies take effect only when network policy support is turned on in the Amazon VPC CNI plugin. For more information, see [Kubernetes network policies](https://docs.aws.amazon.com/eks/latest/userguide/cni-network-policy.html) in the *Amazon EKS User Guide*.

NCCL RAS monitoring of a job starts automatically when you create the training job, and stops when the job completes or you delete it. To use it, turn on `monitoring.enableNcclRasMonitor` and the monitor for the job's type.

## How the agent reports issues
<a name="sagemaker-hyperpod-eks-resiliency-kubernetes-resource-monitoring-agent-reporting"></a>

The agent reports issues in three ways: Kubernetes events, structured Amazon CloudWatch logs, and HyperPod cluster events.

### Kubernetes events
<a name="sagemaker-hyperpod-eks-resiliency-kubernetes-resource-monitoring-agent-reporting-k8s-events"></a>

The agent creates Warning events on the affected node, pod, DaemonSet, or training job. You can view these problems with standard tools such as `kubectl get events` and `kubectl describe`. When an issue clears, it creates a Normal recovery event.

The agent creates the following Warning events.


| Event reason | Meaning | 
| --- | --- | 
| NodeConditionDegraded | A node condition (Ready, MemoryPressure, DiskPressure, PIDPressure, NetworkUnavailable) became degraded. | 
| NodeResourceDegraded | A node has fewer allocatable GPUs or EFA devices than its instance type provides, or than it reported earlier. | 
| NodeGPUCapabilityLost | A GPU node lost its NVIDIA capability labels. | 
| NodeRequiredLabelsMissing | A node is missing required HyperPod labels. | 
| NodeTaintAdded | A taint was added to a node. | 
| NodeTaintEffectChanged | The effect of an existing taint changed. | 
| NoExecuteTaintApplied | A NoExecute taint was applied. Pods and jobs on the node might be evicted. | 
| CriticalPodRestarted | A critical infrastructure pod restarted. | 
| CriticalPodCrashLoop | A critical infrastructure pod entered CrashLoopBackOff. | 
| CriticalPodContainerError | A container of a critical infrastructure pod is in an error state. | 
| CriticalPodFailed | A critical infrastructure pod failed. | 
| CriticalPodNotRunning | A critical infrastructure pod is not running. | 
| ControlPlanePodUnready | A Kubeflow training operator pod is not ready. | 
| DaemonSetPodSustainedUnready | A DaemonSet pod stayed not ready beyond the debounce period. | 
| NecessaryDaemonSetMissing | A required DaemonSet is missing. | 
| DaemonSetPartiallyUnavailable | A DaemonSet does not have all of its desired pods available. | 
| DaemonSetRolloutStalled | A DaemonSet rollout stopped progressing. | 
| DaemonSetMisscheduled | A DaemonSet has misscheduled pods. | 
| TrainingJobFailed | A distributed training job failed. | 
| NCCLProtocolErrorsPersistent | NCCL RAS reports persistent protocol errors for a job. | 
| MonitoringDegraded | The agent itself cannot watch some resources (for example, because of Kubernetes API errors). | 

The agent creates the following Normal events.


| Event reason | Meaning | 
| --- | --- | 
| NodeRecovered | A node issue reported earlier cleared. | 
| PodRecovered | A pod issue reported earlier cleared. | 
| DaemonSetRecovered | A DaemonSet issue reported earlier cleared. | 
| DaemonSetRolloutStarted | A DaemonSet rollout started. | 
| DaemonSetRolloutCompleted | A DaemonSet rollout completed. | 
| TrainingJobStarted | A distributed training job started. | 
| TrainingJobCompleted | A distributed training job completed. | 
| MonitoringRecovered | The agent can watch all resources again. | 

The following kubectl command lists the events that the agent emits:

```bash
kubectl get events -A --field-selector source=hyperpod-kubernetes-resource-monitoring-agent
```

### Structured Amazon CloudWatch logs
<a name="sagemaker-hyperpod-eks-resiliency-kubernetes-resource-monitoring-agent-reporting-logs"></a>

The agent writes JSON log entries that include the affected node, pods, and jobs, along with the change that triggered the report. For more information, see [Logs](#sagemaker-hyperpod-eks-resiliency-kubernetes-resource-monitoring-agent-logs).

### HyperPod cluster events (Amazon EventBridge)
<a name="sagemaker-hyperpod-eks-resiliency-kubernetes-resource-monitoring-agent-reporting-cluster-events"></a>

The agent keeps a current health report for HyperPod components and instances in the status of the cluster-scoped `HyperPodKRMAConfig` object named `default`. HyperPod reads this report and turns changes into cluster events. You can list them with the `ListClusterEvents` and `DescribeClusterEvent` APIs. They are also delivered to the default event bus in Amazon EventBridge in your account, with source `aws.sagemaker` and detail type `SageMaker HyperPod Cluster Event`. For more information, see [SageMaker HyperPod cluster events reference](sagemaker-hyperpod-cluster-events-reference.md).

Cluster events are available for clusters with `NodeProvisioningMode` set to `Continuous`.

HyperPod sends an event for the following:
+ **HyperPod Health Monitoring Agent** (cluster event): The agent is not deployed, an update of the agent is not progressing, or the agent is not running, failing to start, or restarting on some instances. While the agent cannot run, HyperPod cannot detect instance faults or start automatic recovery on the affected instances.
+ **Instance signals that the Health Monitoring Agent does not cover** (instance events): An instance reports fewer GPUs than expected, fewer EFA network devices than expected, or no longer reports its GPU capabilities.

The following table shows when HyperPod sends an event.


| Change | Event | Level | 
| --- | --- | --- | 
| Healthy to unhealthy | Fault event | Warn | 
| Still unhealthy after 6 hours | Repeated fault event, every 6 hours | Warn | 
| Unhealthy to healthy | Recovery event | Info | 
| Healthy when monitoring starts | No event | — | 

The following AWS CLI command lists cluster events. Replace {{cluster-name}} with the name of your cluster and {{region}} with your AWS Region:

```bash
aws sagemaker list-cluster-events --cluster-name {{cluster-name}} --region {{region}}
```

To receive the events in EventBridge, create a rule on the default event bus with the following event pattern, and choose a target such as an Amazon SNS topic:

```json
{
  "source": ["aws.sagemaker"],
  "detail-type": ["SageMaker HyperPod Cluster Event"]
}
```

The following kubectl command shows the health report in the cluster:

```bash
kubectl get hyperpodkrmaconfigs default -o yaml
```

## Install the Kubernetes Resource Monitoring Agent
<a name="sagemaker-hyperpod-eks-resiliency-kubernetes-resource-monitoring-agent-install"></a>

This agent is part of the HyperPod Helm chart, as the `hyperpod-kubernetes-resource-monitor` subchart. It installs into the `aws-hyperpod` namespace, which the `deep-health-check` subchart creates. For the chart source, see [HyperPodHelmChart](https://github.com/aws/sagemaker-hyperpod-cli/tree/main/helm_chart/HyperPodHelmChart) on the GitHub website.

### Install with Helm
<a name="sagemaker-hyperpod-eks-resiliency-kubernetes-resource-monitoring-agent-install-helm"></a>

The subchart is turned off by default in the HyperPod Helm chart. The following commands install the chart with the agent. Replace {{region}} with the AWS Region of your cluster:

```bash
git clone https://github.com/aws/sagemaker-hyperpod-cli.git
cd sagemaker-hyperpod-cli/helm_chart
helm dependencies update HyperPodHelmChart
helm install dependencies HyperPodHelmChart \
  --namespace kube-system \
  --set hyperpod-kubernetes-resource-monitor.enabled=true \
  --set hyperpod-kubernetes-resource-monitor.region={{region}}
```

To add the agent to a cluster where the HyperPod Helm chart is already installed, first apply the agent's CRD, because Helm does not install custom resource definitions (CRDs) on an upgrade. Then upgrade the release. Replace {{region}} with the AWS Region of your cluster:

```bash
kubectl apply -f HyperPodHelmChart/charts/hyperpod-kubernetes-resource-monitor/crds/
helm upgrade dependencies HyperPodHelmChart \
  --namespace kube-system \
  --reuse-values \
  --set hyperpod-kubernetes-resource-monitor.enabled=true \
  --set hyperpod-kubernetes-resource-monitor.region={{region}}
```

The following kubectl commands verify the deployment:

```bash
kubectl get deployment -n aws-hyperpod hyperpod-kubernetes-resource-monitoring-agent
kubectl get pods -n aws-hyperpod -l app=cluster-monitoring-agent
kubectl logs -f deployment/hyperpod-kubernetes-resource-monitoring-agent -n aws-hyperpod
kubectl get hyperpodkrmaconfigs default
```

To remove the agent, upgrade the release with `--set hyperpod-kubernetes-resource-monitor.enabled=false`. Helm does not delete the `HyperPodKRMAConfig` CRD.

### Default deployment configuration
<a name="sagemaker-hyperpod-eks-resiliency-kubernetes-resource-monitoring-agent-install-defaults"></a>


| Attribute | Value | 
| --- | --- | 
| Workload kind | Deployment (one replica; rolling update with maxSurge: 0, so two agents never run at the same time) | 
| Namespace | aws-hyperpod | 
| Image | {{account-id}}.dkr.ecr.{{region}}.amazonaws.com/hyperpod-cluster-monitoring-agent:{{image-tag}}, from the HyperPod Amazon ECR repository of the cluster's AWS Region | 
| Health port | 8081/TCP | 
| Scheduling | Avoids a list of NVIDIA GPU instance types (ml.p4d, ml.p4de, ml.p5, ml.p5e, ml.p6, ml.g5, ml.g6, ml.g6e, and ml.gr6 types) through preferred node affinity. Other instance types, such as AWS Trainium types, are not avoided. To change this, set affinity or nodeSelector. | 
| CPU request / limit | 100m / 200m | 
| Memory request / limit | 512Mi / 1Gi | 
| Security context | Runs as non-root (UID 1000), read-only root file system, all Linux capabilities dropped | 
| Log volume | Host path /var/log/aws mounted into the container | 

### Required role-based access control (RBAC) permissions
<a name="sagemaker-hyperpod-eks-resiliency-kubernetes-resource-monitoring-agent-install-rbac"></a>

The agent needs cluster-wide read access and permission to create events and update its health report. The Helm chart creates a ClusterRole and ClusterRoleBinding with the following permissions.


| API group | Resources | Verbs | 
| --- | --- | --- | 
| core ("") | nodes, nodes/status, pods, pods/status | get, list, watch | 
| core (""), events.k8s.io | events | create, patch | 
| apps | daemonsets | get, list, watch | 
| batch | jobs | get, list, watch | 
| sagemaker.amazonaws.com | hyperpodpytorchjobs | get, list, watch | 
| kubeflow.org | pytorchjobs, pytorchjobs/status | get, list, watch | 
| trainer.kubeflow.org | trainjobs, trainjobs/status | get, list, watch | 
| apiextensions.k8s.io | customresourcedefinitions | get, list | 
| sagemaker.amazonaws.com | hyperpodkrmaconfigs | get | 
| sagemaker.amazonaws.com | hyperpodkrmaconfigs/status | get, update, patch | 
| coordination.k8s.io | leases | get, list, watch, create, update, patch (used only when leader election is turned on) | 

When the health report is turned on, the chart also lets the Kubernetes user of the HyperPod service-linked role (`hyperpod-service-linked-role`) `get` the `HyperPodKRMAConfig` object named `default`, so that HyperPod can read the report.

## Configuration reference
<a name="sagemaker-hyperpod-eks-resiliency-kubernetes-resource-monitoring-agent-configuration"></a>

You configure the agent with Helm chart values, which map to environment variables on the container. In the HyperPod Helm chart, prefix each value with `hyperpod-kubernetes-resource-monitor.`, such as `hyperpod-kubernetes-resource-monitor.monitoring.enablePodMonitor`.

### General settings
<a name="sagemaker-hyperpod-eks-resiliency-kubernetes-resource-monitoring-agent-configuration-general"></a>


| Helm value | Environment variable | Default | Description | 
| --- | --- | --- | --- | 
| enabled (HyperPod Helm chart only) | — | false | Installs the agent. | 
| region | — | "" | AWS Region of the HyperPod Amazon ECR repository to pull the image from. When empty, the AWS Region is read from the nodes' topology.kubernetes.io/region label, then defaults to us-east-1. | 
| image.repository | — | "" | Full image repository, without the tag. Overrides the HyperPod Amazon ECR repository. | 
| image.tag | — | Agent release | Image tag. | 
| healthStatusReport.enabled | ENABLE\_HEALTH\_STATUS\_REPORT | true | Writes the health report that HyperPod cluster events are based on. | 
| leaderElection.enabled | ENABLE\_LEADER\_ELECTION | false | Uses a Kubernetes Lease so that only one replica reports at a time. Required before you run more than one replica. | 
| monitoring.monitoredNamespaces | MONITORED\_NAMESPACES | aws-hyperpod, kube-system, default, kubeflow | Namespaces that the pod monitor watches. | 

### Monitor toggles
<a name="sagemaker-hyperpod-eks-resiliency-kubernetes-resource-monitoring-agent-configuration-monitors"></a>


| Helm value | Environment variable | Default | Description | 
| --- | --- | --- | --- | 
| monitoring.enableNodeMonitor | ENABLE\_NODE\_MONITOR | true | Monitors node conditions, GPU and EFA capacity, labels, and taints. | 
| monitoring.enablePodMonitor | ENABLE\_POD\_MONITOR | true | Monitors critical infrastructure pods and container restarts. | 
| monitoring.enableDaemonsetMonitor | ENABLE\_DAEMONSET\_MONITOR | true | Monitors DaemonSet health and required DaemonSet presence. | 
| monitoring.enableHyperpodPytorchJobMonitor | ENABLE\_HYPERPOD\_PYTORCH\_JOB\_MONITOR | true | Monitors HyperPodPyTorchJob resources. Also required for NCCL RAS monitoring of these jobs. | 
| monitoring.enableKubeflowV1PytorchJobMonitor | ENABLE\_KUBEFLOW\_V1\_PYTORCH\_JOB\_MONITOR | true | Monitors legacy Kubeflow PyTorchJob v1 resources. | 
| monitoring.enableKubeflowV2PytorchJobMonitor | ENABLE\_KUBEFLOW\_TRAINJOB\_MONITOR | true | Monitors Kubeflow TrainJob (Trainer v2) resources. | 
| monitoring.enableNcclRasMonitor | ENABLE\_NCCL\_RAS\_MONITOR | true | Monitors NCCL RAS collective-communication health for each job. | 

A monitor for a custom resource turns itself off if the cluster doesn't have the corresponding CRD, whatever the toggle value.

### Required DaemonSets
<a name="sagemaker-hyperpod-eks-resiliency-kubernetes-resource-monitoring-agent-configuration-daemonsets"></a>

Use `monitoring.necessaryDaemonsets` to declare the DaemonSets that must exist in the cluster. Every 5 minutes, the agent checks each one. If a DaemonSet is missing or has no available pods, the agent emits a `NecessaryDaemonSetMissing` Kubernetes event. Only the Health Monitoring Agent also produces HyperPod cluster events.

The following example shows the default list, which contains only the HyperPod Health Monitoring Agent:

```yaml
monitoring:
  necessaryDaemonsets:
    - name: "health-monitoring-agent"
      namespace: "aws-hyperpod"
```

You can add other DaemonSets that your cluster depends on. List only DaemonSets that are installed (check with `kubectl get daemonsets -A`), and keep the Health Monitoring Agent entry, because setting the list replaces the default. The DaemonSets to add depend on how the cluster exposes GPUs.


| GPU setup | DaemonSets to add | 
| --- | --- | 
| Device plugins from the HyperPod Helm chart | kube-system/dependencies-nvidia-device-plugin and kube-system/dependencies-aws-efa-k8s-device-plugin | 
| NVIDIA GPU operator | nvidia-device-plugin-daemonset in the namespace where you installed the GPU operator, and the EFA device plugin if you use it | 
| Dynamic Resource Allocation (DRA) | None. DRA clusters do not use device plugins. | 

### NCCL RAS settings
<a name="sagemaker-hyperpod-eks-resiliency-kubernetes-resource-monitoring-agent-configuration-nccl"></a>

The following table lists the settings under `monitoring.ncclRas`. They apply when `monitoring.enableNcclRasMonitor` is `true`.


| Helm value | Environment variable | Default | Description | 
| --- | --- | --- | --- | 
| monitoring.ncclRas.port | NCCL\_RAS\_PORT | 28028 | TCP port of the NCCL RAS daemon. | 
| monitoring.ncclRas.monitorInterval | NCCL\_RAS\_MONITOR\_INTERVAL | 30 | Polling interval, in seconds. | 
| monitoring.ncclRas.timeout | NCCL\_RAS\_TIMEOUT | 10 | Connection timeout for each endpoint, in seconds. | 
| monitoring.ncclRas.maxRetries | NCCL\_RAS\_MAX\_RETRIES | 3 | Number of connection attempts for each endpoint in each polling cycle. Attempts are spaced by a short exponential backoff that starts at about 0.5 seconds. | 

## Health check endpoints
<a name="sagemaker-hyperpod-eks-resiliency-kubernetes-resource-monitoring-agent-endpoints"></a>

The agent serves the following endpoints on port `8081`. The Kubernetes startup, liveness, and readiness probes use them.


| Endpoint | Method | Purpose | Responses | 
| --- | --- | --- | --- | 
| /healthz | GET | Liveness probe. Succeeds while the process is alive. | 200 ok | 
| /readyz | GET | Readiness probe. Succeeds after the Kubernetes clients are initialized, monitoring has started, and the first healthy monitoring cycle has finished. | 200 ready; 503 while starting | 
| /health | GET | Detailed status in JSON. | 200 or 503 with a JSON body | 

The following example shows a `/health` response:

```json
{
  "status": "healthy",
  "kubernetes_client_initialized": true,
  "monitoring_running": true,
  "first_healthy_cycle": true,
  "is_leader": true,
  "timestamp": "2026-01-01T00:00:00Z",
  "uptime_seconds": 3600
}
```

## Logs
<a name="sagemaker-hyperpod-eks-resiliency-kubernetes-resource-monitoring-agent-logs"></a>

The agent writes structured JSON logs to the host log volume. They are collected into CloudWatch Logs in the HyperPod cluster log group `/aws/sagemaker/Clusters/{{cluster-name}}/{{cluster-id}}`, in the log streams `SageMakerClusterMonitoringAgent/{{instance-group}}/{{instance-id}}`.

The agent writes logs with the following characteristics:

Log file  
`/var/log/aws/clusters/sagemaker-cluster-monitoring-agent.log`

Format  
JSON, with ISO 8601 timestamps and a `component` field that identifies the monitor, such as `NODE`, `POD`, `DAEMONSET`, `HyperpodPyTorchJob`, `KubeflowTrainJob`, or `nccl-ras-informer-{{job-name}}`.

The following CloudWatch Logs Insights query finds degraded node conditions:

```sql
fields @timestamp, @message
| filter @message like /NodeConditionDegraded/
| sort @timestamp desc
```

## Troubleshooting the Kubernetes Resource Monitoring Agent
<a name="sagemaker-hyperpod-eks-resiliency-kubernetes-resource-monitoring-agent-troubleshooting"></a>

This section helps you resolve common problems with the agent: startup failures, image pull errors, permission errors, and missing events.

### Agent pod exits with code 0 after it starts
<a name="sagemaker-hyperpod-eks-resiliency-kubernetes-resource-monitoring-agent-troubleshooting-exits"></a>

The agent checks the node's Amazon EC2 provider ID at startup. On a node that HyperPod does not manage, it logs a message and exits with code `0`.

Make sure that the pod is scheduled on a HyperPod node.

### Agent pod does not start
<a name="sagemaker-hyperpod-eks-resiliency-kubernetes-resource-monitoring-agent-troubleshooting-not-start"></a>

The pod mounts the `/var/log/aws` host directory as its log volume. If that directory doesn't exist on the node, the pod can't start.

1. Inspect the pod events with the following kubectl command:

   ```bash
   kubectl describe pod -l app=cluster-monitoring-agent -n aws-hyperpod
   ```

1. Make sure that the `/var/log/aws` directory exists on the node.

### Image pull errors
<a name="sagemaker-hyperpod-eks-resiliency-kubernetes-resource-monitoring-agent-troubleshooting-image-pull"></a>

The image comes from the HyperPod Amazon ECR repository of the AWS Region that is set in `region`. A wrong Region, or no network path to Amazon ECR, causes image pull errors.

1. Make sure that `region` is the AWS Region of your cluster.

1. Make sure that the nodes can reach Amazon ECR in that AWS Region.

### RBAC permission errors in the agent logs
<a name="sagemaker-hyperpod-eks-resiliency-kubernetes-resource-monitoring-agent-troubleshooting-rbac"></a>

The agent needs the service account, ClusterRole, and ClusterRoleBinding that the Helm chart creates. If one of them is missing, the agent logs permission errors.

Run the following kubectl commands, and make sure that the service account, ClusterRole, and ClusterRoleBinding exist:

```bash
kubectl get serviceaccount -n aws-hyperpod
kubectl get clusterrole,clusterrolebinding | grep -i hyperpod
```

### No HyperPod cluster events
<a name="sagemaker-hyperpod-eks-resiliency-kubernetes-resource-monitoring-agent-troubleshooting-no-events"></a>

HyperPod creates cluster events from the health report that the agent writes. Without the report, or on a cluster that does not use continuous provisioning, you get no events.

1. Make sure that the cluster has `NodeProvisioningMode` set to `Continuous`.

1. Make sure that `healthStatusReport.enabled` is `true`.

1. Make sure that the health report exists and is updated. Run the following command:

   ```bash
   kubectl get hyperpodkrmaconfigs default -o yaml
   ```

1. If the `HyperPodKRMAConfig` CRD is missing, apply it from the subchart's `crds/` directory, and then restart the agent.

### Training job monitor reports nothing
<a name="sagemaker-hyperpod-eks-resiliency-kubernetes-resource-monitoring-agent-troubleshooting-job-monitor"></a>

The agent turns a job monitor off when the CRD for that job type is not installed.

1. Install the CRD, or the operator that provides it.

1. Restart the agent.