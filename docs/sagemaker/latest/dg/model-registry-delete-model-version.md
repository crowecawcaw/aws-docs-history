

# Delete a Model Version
<a name="model-registry-delete-model-version"></a>

This procedure demonstrates how to delete a model version in the Amazon SageMaker Studio console.

## Delete a Model Version (Studio or Studio Classic)
<a name="model-registry-delete-model-version-studio"></a>

To delete a model version in the Amazon SageMaker Studio console, complete the following steps based on whether you use Studio or Studio Classic.

------
#### [ Studio ]

1. Open the SageMaker Studio console by following the instructions in [Launch Amazon SageMaker Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-launch.html).

1. In the left navigation pane, choose **Models** to display a list of your model groups.

1. Choose the **Registered models** tab, if not selected already.

1. Immediately below the **Registered models** tab label, choose **Model Groups**, if not selected already.

1. From the model groups list, choose the angle bracket to the left of the model group that you want to view.

1. A list of the model versions in the model group appears. If you don't see the model version that you want to delete, choose **View all**.

1. Select the check boxes next to the model versions that you want to delete.

1. Choose the vertical ellipsis above the top right corner of the table, and choose **Delete** (or **Delete model version** if you are in the model group details page).

1. In the **Delete model version** dialog box, choose **Yes, delete the model version**.

1. Choose **Delete**.

1. Confirm that your deleted model versions no longer appear in the model group.

------
#### [ Studio Classic ]

1. Sign in to Amazon SageMaker Studio Classic. For more information, see [Launch Amazon SageMaker Studio Classic](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-launch.html).

1. In the left navigation pane, choose the **Home** icon ( ![Home icon.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/studio/icons/house.png)).

1. Choose **Models**, and then **Model registry**. A list of your Model Groups appears.

1. From the model groups list, select the name of the Model Group of the model version that you want to delete.

1. From the list of model versions, select the name of the model version that you want to delete.

1. Choose the **Actions** dropdown menu, and choose **Remove**.

1. In the confirmation dialog box, enter `REMOVE`.

1. Choose **Remove**.

1. Confirm the model version you removed does not appear in the list of the model group’s model versions.

------