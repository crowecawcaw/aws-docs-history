

# Deploy models from JumpStart using Amazon SageMaker Studio
<a name="sagemaker-hyperpod-model-deployment-deploy-js-ui"></a>

The following steps show you through how to deploy models from JumpStart using Amazon SageMaker Studio.

## Prerequisites
<a name="sagemaker-hyperpod-model-deployment-deploy-js-ui-prereqs"></a>

Verify that you've set up inference capabilities on your Amazon SageMaker HyperPod clusters. For more information, see [Setting up your HyperPod clusters for model deployment](sagemaker-hyperpod-model-deployment-setup.md). 

## Create a HyperPod deployment
<a name="sagemaker-hyperpod-model-deployment-deploy-js-ui-create"></a>

1. In Amazon SageMaker Studio, open the **JumpStart** landing page from the left navigation pane. 

1. Under **All public models**, choose a model you want to deploy.
**Note**  
If you’ve selected a gated model, you’ll have to accept the End User License Agreement (EULA).

1. Choose **SageMaker HyperPod**.

1. Under **Deployment settings**, JumpStart will recommend an instance for deployment. You can modify these settings if necessary.

   1. If you modify **Instance type**, ensure it’s compatible with the chosen **HyperPod cluster**. If there aren’t any compatible instances, you’ll need to select a new **HyperPod cluster **or contact your admin to add compatible instances to the cluster.

   1. To prioritize the model deployment, install the task governance addon, create compute allocations, and set up task rankings for the cluster policy. Once this is done, you should see an option to select a priority for the model deployment which can be used for preemption of other deployments and tasks on the cluster. 

   1. Enter the namespace to which your admin has provided you access. You may have to directly reach out to your admin to get the exact namespace. Once a valid namespace is provided, the **Deploy** button should be enabled to deploy the model.

   1. If your instance type is partitioned (MIG enabled), select a **GPU partition type**.

   1. If you want to enable L2 KVCache or Intelligent routing for speeding up LLM inference, enable them. By default, only L1 KV Cache is enabled. For more details on KVCache and Intelligent routing, see [SageMaker HyperPod model deployment](sagemaker-hyperpod-model-deployment.md).

1. Choose **Deploy** and wait for the **Endpoint** to be created.

1. After the **Endpoint** has been created, select **Test inference**.

## Edit a HyperPod deployment
<a name="sagemaker-hyperpod-model-deployment-deploy-js-ui-edit"></a>

1. In Amazon SageMaker Studio, select **Compute** and then **HyperPod clusters** from the left navigation pane. 

1. Under **Deployments**, choose the HyperPod cluster deployment you want to modify.

1. From the vertical ellipsis icon (⋮), choose **Edit**.

1. Under **Deployment settings**, you can enable or disable **Auto-scaling**, and change the number of **Max replicas**.

1. Select **Save**.

1. The **Status** will change to **Updating**. Once it changes back to **In service**, your changes are complete and you’ll see a message confirming it.

## Delete a HyperPod deployment
<a name="sagemaker-hyperpod-model-deployment-deploy-js-ui-delete"></a>

1. In Amazon SageMaker Studio, select **Compute** and then **HyperPod clusters** from the left navigation pane. 

1. Under **Deployments**, choose the HyperPod cluster deployment you want to modify.

1. From the vertical ellipsis icon (⋮), choose **Delete**.

1. In the **Delete HyperPod deployment window**, select the checkbox.

1. Choose **Delete**.

1. The **Status** will change to **Deleting**. Once the HyperPod deployment has been deleted, you’ll see a message confirming it.