

# Setting up Studio for Ray
<a name="sagemaker-hyperpod-ray-studio-setup"></a>

Amazon SageMaker Studio is a web-based IDE that gives data scientists and ML engineers a purpose-built interface for managing Ray workloads.

## Prerequisites
<a name="sagemaker-hyperpod-ray-studio-setup-prerequisites"></a>

You need the following before you set up Studio:
+ A HyperPod cluster orchestrated by Amazon EKS. For more information, see [Creating a SageMaker HyperPod cluster with Amazon EKS orchestration](sagemaker-hyperpod-eks-operate-console-ui-create-cluster.md).
+ The KubeRay operator installed. It reconciles every Ray resource Studio creates. For more information, see [Installing KubeRay on HyperPod Amazon EKS](sagemaker-hyperpod-ray-install-kuberay.md).

The following are optional, and each one adds a capability rather than gating the setup:
+ The SageMaker AI Spaces add-on, for interactive development in a JupyterLab or Code Editor space attached to a Ray cluster. For more information, see [Setting up the Spaces add-on](sagemaker-hyperpod-ray-spaces-addon-setup.md).
+ The HyperPod Ray Endpoint Operator, for authenticated Ray Dashboard links and remote job submission. For more information, see [Installing the HyperPod Ray Endpoint Operator](sagemaker-hyperpod-ray-endpoint-operator.md).

## Step 1: Create a SageMaker AI domain
<a name="sagemaker-hyperpod-ray-studio-setup-domain"></a>

Studio access to a HyperPod cluster runs through a SageMaker AI domain, and the domain execution role is the IAM principal Studio uses to act on your cluster. Create the domain and associate it with your cluster by following [Setting up an Amazon EKS cluster in Studio](sagemaker-hyperpod-studio-setup-eks.md).

## Step 2: Grant the domain access to your cluster
<a name="sagemaker-hyperpod-ray-studio-setup-policy"></a>

Cluster access for Studio users is controlled by cluster-access policies attached to the execution role on the domain or the user profile. Only a role with the right policies attached reaches the cluster.

**To grant cluster access**

1. Open the SageMaker AI console and choose **HyperPod clusters**, then choose your cluster.

1. On the **Configuration** tab, find **Cluster access for SageMaker domains**.

1. Choose **Manage access**.

1. Select the policies your users need:
   + `AmazonSagemakerHyperpodTrainingPolicy` — `RayCluster`, `RayJob`, and `RayCronJob`.
   + `AmazonSagemakerHyperpodInferencePolicy` — `RayCluster` and `RayService`.
   + `AmazonSagemakerHyperpodSpacePolicy` — spaces, for interactive development.
   + `AmazonSagemakerHyperpodSpaceTemplatePolicy` — space templates.
   + `AmazonSagemakerHyperpodUserClusterPolicy` — cluster visibility for a user.

1. Choose whether to scope access to a namespace or to the whole cluster. Scope to a namespace when teams share a cluster.

1. Save.

Granting access this way creates the Amazon EKS access entry for the execution role for you, so there is no separate step in the Amazon EKS console. For the concepts behind the access model, see [Setting up Kubernetes role-based access control](sagemaker-hyperpod-eks-setup-rbac.md).

## Step 3: Verify
<a name="sagemaker-hyperpod-ray-studio-setup-verify"></a>

**To confirm access**

1. Open the [Domains page](https://console.aws.amazon.com/sagemaker/home#/studio) in the SageMaker AI console and choose your domain.

1. Launch Studio for a user profile.

1. Under **Compute**, select your HyperPod cluster.

1. Choose **Tasks**.

1. Confirm that you are able to see your Ray workloads.