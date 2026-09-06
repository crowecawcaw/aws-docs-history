

# View the Deployment History of a Model
<a name="model-registry-deploy-history"></a>

To view the deployments for a model version in the Amazon SageMaker Studio console, complete the following steps based on whether you use Studio or Studio Classic.

------
#### [ Studio ]

**View the deployment history for a model version**

1. Open the SageMaker Studio console by following the instructions in [Launch Amazon SageMaker Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-launch.html).

1. In the left navigation pane, choose **Models** to display a list of your model groups.

1. Choose the **Registered models** tab, if not selected already.

1. Immediately below the **Registered models** tab label, choose **Model Groups**, if not selected already.

1. From the model groups list, choose the angle bracket to the left of the model group that you want to view.

1. A list of the model versions in the model group appears. If you don't see the model version that you want to delete, choose **View all**.

1. Select the name of the model version that you want to view.

1. Choose the **Activity** tab. Deployments for the model version appear as events in the activity list with an **Event type** of **ModelDeployment**.

------
#### [ Studio Classic ]

**View the deployment history for a model version**

1. Sign in to Amazon SageMaker Studio Classic. For more information, see [Launch Amazon SageMaker Studio Classic](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-launch.html).

1. In the left navigation pane, choose the **Home** icon ( ![Home icon.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/studio/icons/house.png)).

1. Choose **Models**, and then **Model registry**.

1. From the model groups list, select the name of the Model Group that you want to view.

1. A new tab appears with a list of the model versions in the Model Group.

1. In the list of model versions, select the name of the model version for which you want to view details.

1. On the model version tab that opens, choose **Activity**. Deployments for the model version appear as events in the activity list with an **Event type** of **ModelDeployment**.

------