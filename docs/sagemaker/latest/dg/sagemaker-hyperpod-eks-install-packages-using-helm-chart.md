# Installing

packages on the Amazon EKS cluster using Helm

Before creating a SageMaker HyperPod cluster and attaching it to an Amazon EKS cluster, you
should install packages using [Helm](https://helm.sh/ "https://helm.sh/"), a package
manager for Kubernetes. Helm is an open-source tool for setting up a installation
process for Kubernetes clusters. It enables the automation and streamlining of
dependency installations and simplifies various setups needed for preparing the Amazon EKS
cluster as the orchestrator (control plane) for a SageMaker HyperPod cluster.

The SageMaker HyperPod service team provides a Helm chart package, which bundles key
dependencies such as device/EFA plug-ins, plug-ins, [Kubeflow Training
Operator](https://www.kubeflow.org/docs/components/training/ "https://www.kubeflow.org/docs/components/training/"), and associated permission configurations.

###### Important

This Helm installation step is required. If you set up your Amazon EKS cluster using
the [AWS Management Console](sagemaker-hyperpod-eks-operate-console-ui-create-cluster.md "sagemaker-hyperpod-eks-operate-console-ui-create-cluster.md") or [AWS CloudFormation](smcluster-getting-started-eks-console-create-cluster-cfn.md "smcluster-getting-started-eks-console-create-cluster-cfn.md"),
you can skip this step because the installation is handled automatically during the
setup process. If you set up the cluster directly using the APIs, use the provided
Helm chart to configure your Amazon EKS cluster. Failure to configure your Amazon EKS cluster
using the provided Helm chart might result in the SageMaker HyperPod cluster not
functioning correctly or the creation process failing entirely. The
`aws-hyperpod` namespace name cannot be modified.

1. [Install Helm](https://helm.sh/docs/intro/install/ "https://helm.sh/docs/intro/install/") on your
   local machine.
2. Download the Helm charts provided by SageMaker HyperPod located at
   `helm_chart/HyperPodHelmChart` in the [SageMaker HyperPod CLI repository](https://github.com/aws/sagemaker-hyperpod-cli/tree/main/helm_chart "https://github.com/aws/sagemaker-hyperpod-cli/tree/main/helm_chart").

```
git clone https://github.com/aws/sagemaker-hyperpod-cli.git
cd sagemaker-hyperpod-cli/helm_chart

```

3. Update the dependencies of the Helm chart, preview the changes that will be
   made to your Kubernetes cluster, and install the Helm chart.

```
helm dependencies update HyperPodHelmChart
```

```
helm install hyperpod-dependencies HyperPodHelmChart --namespace kube-system --dry-run
```

```
helm install hyperpod-dependencies HyperPodHelmChart --namespace kube-system
```

In summary, the Helm installation sets up various components for your Amazon EKS cluster,
including job scheduling and queueing (Kueue), storage management, MLflow integration,
and Kubeflow. Additionally, the charts install the following components for integrating
with the SageMaker HyperPod cluster resiliency features, which are required components.

- **Health monitoring agent** – This installs the
  health-monitoring agent provided by SageMaker HyperPod. This is required if you want
  to get your HyperPod cluster be monitored. Health-monitoring agents are
  provided as Docker images as follows. In the provided `values.yaml`
  in the Helm charts, the image is preset. The agent support GPU-based instances
  and Trainium-accelerator-based instances (`trn1`, `trn1n`,
  `inf2`). It is installed to the `aws-hyperpod`
  namespace. To find your supported URI, see
  [Supported Regions and their ECR URIs in the
  sagemaker-hyperpod-cli repository on GitHub](https://github.com/aws/sagemaker-hyperpod-cli/blob/main/helm_chart/readme.md#6-notes "https://github.com/aws/sagemaker-hyperpod-cli/blob/main/helm_chart/readme.md#6-notes").
- **Deep health check** – This sets up a
  `ClusterRole`, a ServiceAccount
  (`deep-health-check-service-account`) in the
  `aws-hyperpod` namespace, and a `ClusterRoleBinding`
  to enable the SageMaker HyperPod deep health check feature. For more information about
  the Kubernetes RBAC file for deep health check, see the configuration file
  [`deep-health-check-rbac.yaml`](https://github.com/aws/sagemaker-hyperpod-cli/blob/main/helm_chart/HyperPodHelmChart/charts/deep-health-check/templates/deep-health-check-rbac.yaml "https://github.com/aws/sagemaker-hyperpod-cli/blob/main/helm_chart/HyperPodHelmChart/charts/deep-health-check/templates/deep-health-check-rbac.yaml") in the SageMaker HyperPod
  CLI GitHub repository.
- **`job-auto-restart`** - This sets up
  a `ClusterRole`, a ServiceAccount (`job-auto-restart`) in
  the `aws-hyperpod` namespace, and a `ClusterRoleBinding`,
  to enable the auto-restart feature for PyTorch training jobs in SageMaker HyperPod.
  For more information about the Kubernetes RBAC file for
  `job-auto-restart`, see the configuration file [`job-auto-restart-rbac.yaml`](https://github.com/aws/sagemaker-hyperpod-cli/blob/main/helm_chart/HyperPodHelmChart/charts/job-auto-restart/templates/job-auto-restart-rbac.yaml "https://github.com/aws/sagemaker-hyperpod-cli/blob/main/helm_chart/HyperPodHelmChart/charts/job-auto-restart/templates/job-auto-restart-rbac.yaml") in the SageMaker HyperPod CLI
  GitHub repository.
- **Kubeflow MPI operator** – The [MPI Operator](https://github.com/kubeflow/mpi-operator "https://github.com/kubeflow/mpi-operator") is a
  Kubernetes operator that simplifies running distributed Machine Learning (ML)
  and High-Performance Computing (HPC) workloads using the Message Passing
  Interface (MPI) on Kubernetes clusters. It installs MPI Operator v0.5. It is
  installed to the `mpi-operator` namespace.
- **`nvidia-device-plugin`** – This is a
  Kubernetes device plug-in that allows you to automatically expose NVIDIA GPUs
  for consumption by containers in your Amazon EKS cluster. It allows Kubernetes to
  allocate and provide access to the requested GPUs for that container. Required
  when using an instance type with GPU.
- **`neuron-device-plugin`** – This is a
  Kubernetes device plug-in that allows you to automatically expose AWS
  Inferentia chips for consumption by containers in your Amazon EKS cluster. It allows
  Kubernetes to access and utilize the AWS Inferentia chips on the cluster
  nodes. Required when using a Neuron instance type.
- **`aws-efa-k8s-device-plugin`** – This
  is a Kubernetes device plug-in that enables the use of AWS Elastic Fabric
  Adapter (EFA) on Amazon EKS clusters. EFA is a network device that provides
  low-latency and high-throughput communication between instances in a cluster.
  Required when using an EFA supported instance type.
  For more information about the installation procedure using the provided Helm charts,
  see the [README file in the SageMaker HyperPod CLI repository](https://github.com/aws/sagemaker-hyperpod-cli/tree/main/helm_chart "https://github.com/aws/sagemaker-hyperpod-cli/tree/main/helm_chart").
