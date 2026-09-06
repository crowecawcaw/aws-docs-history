

# Setting up Ray metrics collection
<a name="sagemaker-hyperpod-ray-observability-setup"></a>

To collect Ray metrics, install or update the SageMaker HyperPod Observability add-on and turn on Ray metrics. The add-on deploys a collector with scrape configuration for Ray head pods, worker pods, and the KubeRay operator, so you do not hand-author scrape configuration per cluster. Metrics land in Amazon Managed Service for Prometheus and are visualized in Amazon Managed Grafana.

## Prerequisites
<a name="sagemaker-hyperpod-ray-observability-setup-prereq"></a>
+ The KubeRay operator installed on your HyperPod cluster. For more information, see [Installing KubeRay on HyperPod Amazon EKS](sagemaker-hyperpod-ray-install-kuberay.md).
+ The Observability add-on on version 1.0.6 or later. Earlier versions run, but Ray metrics do not appear.

## Turn on Ray metrics
<a name="sagemaker-hyperpod-ray-observability-setup-turn-on"></a>

**Note**  
Any newly created HyperPod cluster, with either **Quick setup** or **Custom setup** in the console, has Ray metrics turned on by default. Use the following steps for a cluster created another way, or one where Ray metrics are off.

**To turn on Ray metrics**

1. Open the HyperPod cluster in the console, then go to the Observability add-on configuration on the **Add-ons** or **Dashboard** tab.

1. Install the add-on, or update it if it is already installed.

1. Confirm the **Ray metrics** checkbox is selected. It is selected by default.

1. Save the configuration.

**Important**  
If the Observability add-on is already installed, upgrade it to version 1.0.6 or later, then upgrade the Grafana dashboards from the SageMaker AI console. New Ray metrics and dashboard panels do not appear until both the add-on and the dashboards are upgraded.

To upgrade the dashboards, open your cluster in the SageMaker AI console, choose the **Dashboard** tab, and in the **HyperPod Observability** section choose **Actions**, then **Upgrade dashboards**. Confirm the upgrade in the dialog. Upgrading overwrites the Ray Core, Ray Data, Ray Train, and Ray Serve dashboards, so copy any customizations first.

![The Upgrade dashboards dialog in the SageMaker AI console, listing the Ray Core, Ray Data, Ray Train, and Ray Serve dashboards to be upgraded.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/ray/observability-upgrade-grafana-dashboards.png)


For the general add-on setup and the console steps, see [Observability](sagemaker-hyperpod-ray-observability.md) and [Observability for Amazon SageMaker HyperPod cluster orchestrated by Amazon EKS](sagemaker-hyperpod-eks-cluster-observability.md).

## Verify
<a name="sagemaker-hyperpod-ray-observability-setup-verify"></a>

Confirm the add-on reports the Ray pods as scrape targets, then open Grafana and confirm a Ray dashboard shows data for a running cluster. If a dashboard is empty, confirm the add-on is on version 1.0.6 or later first.