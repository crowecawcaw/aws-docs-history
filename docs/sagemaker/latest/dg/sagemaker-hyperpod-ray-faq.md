# Ray on HyperPod FAQs

## Does HyperPod modify Ray or KubeRay?

HyperPod runs the upstream, open source Ray and KubeRay without changes. Your
Ray code, the Ray APIs, and the `RayCluster`, `RayJob`,
`RayCronJob`, and `RayService` custom resources behave as they do
in open source. HyperPod adds capabilities around Ray, such as a managed Studio
experience, secure dashboard access, observability, and resiliency.

## Can I keep my existing KubeRay installation?

You can keep the KubeRay operator you already run. HyperPod capabilities
install alongside it, and manifests you already apply continue to work. If your cluster
has no KubeRay operator yet, install it as described in [Installing KubeRay on HyperPod Amazon EKS](sagemaker-hyperpod-ray-install-kuberay.md "sagemaker-hyperpod-ray-install-kuberay.md").

## Do I need SageMaker Studio?

Amazon SageMaker Studio is required only for the managed experience, where data scientists
create and manage Ray clusters without Kubernetes knowledge. On an existing Ray
platform, you use `kubectl`, Helm, and the toolkit library, and nothing
requires Studio. For more information, see [Getting started](sagemaker-hyperpod-ray-getting-started.md "sagemaker-hyperpod-ray-getting-started.md").

## Can I use my own Prometheus and Grafana?

You can keep your own Prometheus and Grafana. The HyperPod Observability
add-on is one option that arrives configured, but you can scrape Ray metrics with your
own stack instead. For more information, see [Setting up Ray metrics collection](sagemaker-hyperpod-ray-observability-setup.md "sagemaker-hyperpod-ray-observability-setup.md").

## How does quota work with a long-lived Ray cluster?

HyperPod Task Governance accounts for quota at the `RayCluster`
level, so a long-lived cluster holds its full declared capacity for as long as it runs.
Size a persistent cluster to the capacity you intend to reserve, and use
`RayJob` for work that acquires and releases capacity per job. For more
information, see [Queueing with task governance](sagemaker-hyperpod-ray-task-governance.md "sagemaker-hyperpod-ray-task-governance.md").

## What happens to my Ray job when a GPU node fails?

HyperPod detects the fault through health checks and reboots or replaces the
node, and KubeRay reschedules the affected Ray pods. Your job resumes from its last
checkpoint, so write checkpoints to recover in-progress work. For more information, see
[Automatic node recovery with Ray](sagemaker-hyperpod-ray-node-recovery.md "sagemaker-hyperpod-ray-node-recovery.md").

## Which Ray libraries are supported?

HyperPod supports the open source Ray libraries, including Ray Core, Ray
Train, Ray Data, and Ray Serve, because it runs Ray unmodified. Match
`spec.rayVersion` to the Ray version in your container image. For the library APIs, see the [Ray documentation](https://docs.ray.io/en/latest/index.html "https://docs.ray.io/en/latest/index.html") on the Ray
website.

## Can I adopt one capability without the others?

Each HyperPod capability installs independently as an add-on or a Python
package, so you can adopt one and stop. A team with its own Ray platform can add
observability or authenticated dashboard access without changing the rest. For the full
list and dependencies, see [Getting started](sagemaker-hyperpod-ray-getting-started.md "sagemaker-hyperpod-ray-getting-started.md").
