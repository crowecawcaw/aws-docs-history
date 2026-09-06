

# Delete a Model Group
<a name="model-registry-delete-model-group"></a>

This procedure demonstrates how to delete a Model Group in the Amazon SageMaker Studio console. When you delete a Model Group, you lose access to the model versions in the Model Group.

## Delete a Model Group (Studio or Studio Classic)
<a name="model-registry-delete-model-group-studio"></a>

**Important**  
You can only delete an empty model group. Before you delete your model group, remove its model versions, if any.

To delete a Model Group in the Amazon SageMaker Studio console, complete the following steps based on whether you use Studio or Studio Classic.

------
#### [ Studio ]

1. Open the SageMaker Studio console by following the instructions in [Launch Amazon SageMaker Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-launch.html).

1. In the left navigation pane, choose **Models**.

1. Choose the **Registered models** tab, if not selected already.

1. Immediately below the **Registered models** tab label, choose **Model Groups**, if not selected already.

1. From the model groups list, select the check box next to the name of the Model Group you want to delete.

1. Choose the vertical ellipsis above the top right corner of the model groups list, and choose **Delete**.

1. In the **Delete model group** dialog box, choose **Yes, delete the model group**.

1. Choose **Delete**.

1. Confirm that your deleted model groups no longer appear in your list of model groups.

------
#### [ Studio Classic ]

1. Sign in to Amazon SageMaker Studio Classic. For more information, see [Launch Amazon SageMaker Studio Classic](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-launch.html).

1. In the left navigation pane, choose the **Home** icon ( ![Home icon.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/studio/icons/house.png)).

1. Choose **Models**, and then **Model registry**. A list of your Model Groups appears.

1. From the model groups list, select the name of the Model Group you want to delete.

1. In the top right corner, choose **Remove**.

1. In the confirmation dialog box, enter `REMOVE`.

1. Choose **Remove**.

------