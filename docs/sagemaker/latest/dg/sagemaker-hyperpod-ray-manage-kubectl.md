# Managing Ray workloads with kubectl

Ray on HyperPod uses the upstream KubeRay custom resources without modification. If
you already run Ray on Kubernetes, your existing manifests apply unchanged, and the Ray
documentation is the reference for every field. This page covers what is specific to
HyperPod.

Access to Ray resources is granted by the HyperPod cluster-access policies. Use
`AmazonSagemakerHyperpodTrainingPolicy` for `RayCluster`,
`RayJob`, and `RayCronJob`, or
`AmazonSagemakerHyperpodInferencePolicy` for `RayCluster` and
`RayService`. Associate the policy with the Amazon EKS access entry for your IAM
principal, scoped to a namespace when teams share a cluster.

If your principal is a SageMaker AI domain execution role, the HyperPod console grants the
policy and creates the access entry for you. For more information, see [Setting up Studio for Ray](sagemaker-hyperpod-ray-studio-setup.md "sagemaker-hyperpod-ray-studio-setup.md").

## Supported custom resources

| Resource     | Use it for                                                                                                                                                                                                                                                                                                                                                                                         | Reference                                                                                                                                                                                                                                     |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `RayCluster` | A long-running cluster you submit work to.                                                                                                                                                                                                                                                                                                                                                         | [RayCluster Quickstart](https://docs.ray.io/en/latest/cluster/kubernetes/getting-started/raycluster-quick-start.html "https://docs.ray.io/en/latest/cluster/kubernetes/getting-started/raycluster-quick-start.html") in the Ray documentation |
| `RayJob`     | A single job. KubeRay creates a cluster, runs the job, and tears the<br>cluster down when `shutdownAfterJobFinishes` is<br>`true`.                                                                                                                                                                                                                                                                 | [RayJob Quickstart](https://docs.ray.io/en/latest/cluster/kubernetes/getting-started/rayjob-quick-start.html "https://docs.ray.io/en/latest/cluster/kubernetes/getting-started/rayjob-quick-start.html") in the Ray documentation             |
| `RayCronJob` | A recurring job on a cron schedule, such as nightly batch inference.<br>Set `spec.timeZone` to an IANA name, or the schedule follows<br>the controller's local time zone.                                                                                                                                                                                                                          | [RayCronJob Quickstart](https://docs.ray.io/en/latest/cluster/kubernetes/getting-started/raycronjob-quick-start.html "https://docs.ray.io/en/latest/cluster/kubernetes/getting-started/raycronjob-quick-start.html") in the Ray documentation |
| `RayService` | A Ray Serve application, declared in `serveConfigV2`, with<br>zero-downtime upgrades. For worked HyperPod examples, see [Deploying a model with Ray Serve](sagemaker-hyperpod-ray-deploy-model.md "sagemaker-hyperpod-ray-deploy-model.md") and [Deploying a JumpStart model with Ray Serve](sagemaker-hyperpod-ray-deploy-jumpstart-model.md "sagemaker-hyperpod-ray-deploy-jumpstart-model.md"). | [RayService Quickstart](https://docs.ray.io/en/latest/cluster/kubernetes/getting-started/rayservice-quick-start.html "https://docs.ray.io/en/latest/cluster/kubernetes/getting-started/rayservice-quick-start.html") in the Ray documentation |

###### Note

`RayCronJob` requires KubeRay 1.6.0 or later. On an earlier operator the
resource kind does not exist. For more information, see [Installing KubeRay on HyperPod Amazon EKS](sagemaker-hyperpod-ray-install-kuberay.md "sagemaker-hyperpod-ray-install-kuberay.md").

## Creating a cluster

The following manifest creates a head pod and a GPU worker group on
HyperPod nodes.

```
apiVersion: ray.io/v1
kind: RayCluster
metadata:
  name: `my-cluster`
  namespace: `my-namespace`
spec:
  rayVersion: "2.55.1"
  headGroupSpec:
    rayStartParams:
      dashboard-host: "0.0.0.0"
    template:
      spec:
        containers:
          - name: ray-head
            image: rayproject/ray:2.55.1
            ports:
              - { containerPort: 6379, name: gcs-server }
              - { containerPort: 8265, name: dashboard }
              - { containerPort: 10001, name: client }
            resources:
              requests: { cpu: "2", memory: "4Gi" }
  workerGroupSpecs:
    - groupName: gpu-workers
      replicas: 2
      rayStartParams: {}
      template:
        spec:
          nodeSelector:
            node.kubernetes.io/instance-type: ml.g5.xlarge
          containers:
            - name: ray-worker
              image: rayproject/ray:2.55.1-gpu
              resources:
                limits: { nvidia.com/gpu: "1" }
                requests: { cpu: "4", memory: "16Gi", nvidia.com/gpu: "1" }
```

```
kubectl apply -f my-cluster.yaml -n `my-namespace`
kubectl get raycluster `my-cluster` -n `my-namespace`
```

###### Important

Set `dashboard-host` to `0.0.0.0` on the head group. The Ray
Endpoint Operator needs it to serve the dashboard outside the head pod, and
authenticated dashboard access fails without it.

The cluster is ready when the head pod and at least one worker pod are running.
`RayJob`, `RayCronJob`, and `RayService` follow the
same apply-and-check pattern, and each embeds a `rayClusterSpec` with the same
shape as the `spec` above.

For every field these resources accept, see [RayCluster Configuration](https://docs.ray.io/en/latest/cluster/kubernetes/user-guides/config.html "https://docs.ray.io/en/latest/cluster/kubernetes/user-guides/config.html") in the Ray documentation.

## Submitting jobs to a running cluster

Applying a `RayJob` creates a cluster for that job. To submit to a cluster
that is already running, use the `toolkit-for-ray-on-sagemaker-ai` package. For
more information, see [Submitting jobs remotely with the toolkit library](sagemaker-hyperpod-ray-remote-job-submission.md "sagemaker-hyperpod-ray-remote-job-submission.md").
