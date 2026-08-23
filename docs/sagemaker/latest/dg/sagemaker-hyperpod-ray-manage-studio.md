# Managing Ray workloads with Studio

Amazon SageMaker Studio manages Ray workloads from a web interface. Open your cluster in the
HyperPod console, then choose the **Tasks** tab. The
tab lists the Ray resources in the namespaces you have access to, and the **Task type** filter switches between `RayCluster`,
`RayJob`, `RayCronJob`, and `RayService`.

Studio reads and writes the same KubeRay custom resources that the operator
reconciles. A resource you create in Studio is identical to one you apply with
`kubectl`. You can move between the two surfaces on the same workload.

Before anyone uses the **Tasks** tab, configure a SageMaker AI domain
and grant it access to your cluster. For more information, see [Setting up Studio for Ray](sagemaker-hyperpod-ray-studio-setup.md "sagemaker-hyperpod-ray-studio-setup.md").

## Creating a cluster

Choose **Create Ray cluster** and either complete the form
or paste a `RayCluster` manifest into the YAML view. The form covers the
common fields. The YAML view accepts any field the KubeRay operator supports. Use it when
you need a field the form does not expose.

The namespace selector in the form shows the compute allocation and current utilization
for each namespace you have access to. Use it to size the cluster against the capacity
that is actually free before you submit, instead of finding out afterward that the
cluster is waiting on quota. This matters most in a namespace that HyperPod Task
Governance manages, where the cluster is not admitted until quota exists for its full
declared size. For more information, see [Quota and scheduling behavior for Ray workloads](sagemaker-hyperpod-ray-task-governance-quota.md "sagemaker-hyperpod-ray-task-governance-quota.md").

Attach a space to the cluster when you want to develop against it interactively. A
space is a JupyterLab or Code Editor environment in Amazon SageMaker Studio. Code you run there,
in a notebook or a terminal, reaches the cluster through `ray.init()`.

A space carries its own Ray version, from the SageMaker AI Distribution image it runs. Match
that version to the Ray version of the cluster. A mismatch produces runtime errors that
are hard to diagnose. For more information, see [Attaching Ray cluster to Space](sagemaker-hyperpod-ray-attach-space.md "sagemaker-hyperpod-ray-attach-space.md").

## Actions on a cluster

Choose **Actions** on a row to act on that resource
without leaving Studio.

| Action                      | What it does                                                                                                                                                                                                                                                                                               |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Interactive development** | Opens a JupyterLab or Code Editor space attached to the cluster, so<br>`ray.init()` in that space connects to it. Requires the<br>SageMaker AI Spaces add-on. For more information, see [Attaching Ray cluster to Space](sagemaker-hyperpod-ray-attach-space.md "sagemaker-hyperpod-ray-attach-space.md"). |
| **Submit job**              | Submits a job to the running cluster.                                                                                                                                                                                                                                                                      |
| **Open Ray Dashboard**      | Opens the Ray Dashboard for the cluster. Requires the Ray Endpoint<br>Operator. For more information, see [Installing the HyperPod Ray Endpoint Operator](sagemaker-hyperpod-ray-endpoint-operator.md "sagemaker-hyperpod-ray-endpoint-operator.md").                                                      |
| **Open Grafana**            | Opens the Grafana dashboards for the cluster. Requires the<br>observability add-on. For more information, see [Setting up Ray metrics collection](sagemaker-hyperpod-ray-observability-setup.md "sagemaker-hyperpod-ray-observability-setup.md").                                                          |
| **Edit Ray cluster**        | Changes the cluster, including worker replica counts.                                                                                                                                                                                                                                                      |
| **Suspend Ray cluster**     | Stops the cluster's pods and keeps the resource. Releases the<br>compute.                                                                                                                                                                                                                                  |
| **Resume Ray cluster**      | Restarts the pods of a suspended cluster with its existing<br>configuration. Available when the cluster is suspended.                                                                                                                                                                                      |
| **Delete Ray cluster**      | Deletes the cluster and its pods.                                                                                                                                                                                                                                                                          |

## Viewing details and events

Choose a resource name to open it. The **Events** tab
lists the pods of the Ray cluster together with their Kubernetes events. Start there when
a cluster does not reach a running state. It also helps when a pod restarts unexpectedly,
or a job fails for a reason its logs do not explain. The events name the failing pod and
the reason, such as an image pull failure or insufficient allocatable capacity. For more
information, see [Troubleshooting Ray on HyperPod](sagemaker-hyperpod-ray-troubleshooting.md "sagemaker-hyperpod-ray-troubleshooting.md").

To see utilization for the cluster, choose **Actions**,
then **Open Grafana**. For quota, priority, and preemption
behavior in a namespace that HyperPod Task Governance manages, see [Quota and scheduling behavior for Ray workloads](sagemaker-hyperpod-ray-task-governance-quota.md "sagemaker-hyperpod-ray-task-governance-quota.md").
