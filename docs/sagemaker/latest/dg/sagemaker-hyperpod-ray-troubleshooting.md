# Troubleshooting Ray on HyperPod

Use this page to diagnose common problems with Ray clusters, dashboards, jobs, and
observability on HyperPod. Each entry gives the symptom, the cause, and the
resolution.

## Ray cluster stuck in Pending

###### Symptom

The head or worker pods stay `Pending` and the cluster never reaches
`Running`.

###### Cause

The requested vCPU or memory is higher than the Kubernetes allocatable capacity on
the chosen instance type. Allocatable is lower than the instance nameplate because
kube-system reserves and DaemonSets consume part of each node.

###### Resolution

Lower the vCPU and memory requests so they fit allocatable capacity, or choose a
larger instance type. Check allocatable with `kubectl describe node
 `my-node`` and set requests below the reported
values.

## ray.init() fails with a version error

###### Symptom

`ray.init()` fails, or the cluster starts but clients cannot
connect.

###### Cause

The Ray version in the space or client image does not match
`spec.rayVersion` in the cluster manifest.

###### Resolution

Set `spec.rayVersion` to the Ray version in the container image, and
use the same Ray version in the space or client. For more information, see [Installing KubeRay on HyperPod Amazon EKS](sagemaker-hyperpod-ray-install-kuberay.md "sagemaker-hyperpod-ray-install-kuberay.md").

## Dashboard link returns an authorization error

###### Symptom

The Ray Dashboard link opens but returns an authorization error.

###### Cause

Under the private access strategy, the dashboard is scoped to the identity that
created the connection. A different identity is denied.

###### Resolution

Open the dashboard as the identity that created the cluster, or use the public
access strategy to grant access to anyone with connect permission in the namespace.
For more information, see [Access strategies and security best practices](sagemaker-hyperpod-ray-dashboard-access-strategies.md "sagemaker-hyperpod-ray-dashboard-access-strategies.md").

## Ray workload never admitted

###### Symptom

A `RayCluster` or `RayJob` stays unadmitted and no pods are
created.

###### Cause

The namespace has no compute allocation in HyperPod Task Governance, so
Task Governance holds the workload with no quota to admit it against.

###### Resolution

Assign a compute allocation to the namespace, or submit to a namespace that has
one. For more information, see [Setting up task governance for Ray](sagemaker-hyperpod-ray-task-governance-setup.md "sagemaker-hyperpod-ray-task-governance-setup.md").

## Grafana dashboards are empty

###### Symptom

The Ray Grafana dashboards load but show no data for a running cluster.

###### Cause

Ray metrics are not turned on in the HyperPod Observability add-on, so no
Ray metrics are scraped.

###### Resolution

Turn on Ray metrics in the Observability add-on and confirm the add-on version
supports Ray metric scraping. For more information, see [Setting up Ray metrics collection](sagemaker-hyperpod-ray-observability-setup.md "sagemaker-hyperpod-ray-observability-setup.md").

## Job submission fails to reach the endpoint

###### Symptom

`ray job submit` fails to connect, or returns an authorization
error.

###### Cause

The job submission endpoint is unreachable, or the session token expired. A
dashboard or endpoint session is valid for up to six hours.

###### Resolution

Confirm the endpoint address, then generate a new connection URL to refresh the
token and retry. For more information, see [Generating a dashboard connection URL](sagemaker-hyperpod-ray-dashboard-connection-url.md "sagemaker-hyperpod-ray-dashboard-connection-url.md").
