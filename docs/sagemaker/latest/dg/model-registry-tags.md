

# View and Manage Model Group and Model Version Tags
<a name="model-registry-tags"></a>

Model Registry helps you view and manage tags related to your model groups. You can use tags to categorize model groups by purpose, owner, environment, or other criteria. The following instructions show you how to view, add, delete, and edit your tags in the Amazon SageMaker Studio console.

**Note**  
Model packages in the SageMaker Model Registry do not support tags—these are versioned model packages. Instead, you can add key value pairs using `CustomerMetadataProperties`. Model package groups in the model registry support tagging. 

## View and manage model group tags
<a name="model-registry-tags-model-group"></a>

------
#### [ Studio ]

**To view a model group tag, complete the following steps:**

1. Open the SageMaker Studio console by following the instructions in [Launch Amazon SageMaker Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-launch.html).

1. In the left navigation pane, choose **Models** to display a list of your model groups.

1. Choose the **Registered models** tab, if not selected already.

1. Immediately below the **Registered models** tab label, choose **Model Groups**, if not selected already.

1. From the Model Groups list, select the name of the Model Group you want to view.

1. In the model group page, choose the **Tags** tab. View the tags associated with your model group.

**To add a model group tag, complete the following steps:**

1. Open the SageMaker Studio console by following the instructions in [Launch Amazon SageMaker Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-launch.html).

1. In the left navigation pane, choose **Models** to display a list of your model groups.

1. Choose the **Registered models** tab, if not selected already.

1. Immediately below the **Registered models** tab label, choose **Model Groups**, if not selected already.

1. From the Model Groups list, select the name of the Model Group you want to edit.

1. In the model group page, choose the **Tags** tab.

1. Choose **Add/Edit tags**.

1. Above **\+ Add new tag**, enter your new key in the blank **Key** field.

1. (Optional) Enter your new value in the blank **Value** field.

1. Choose **Confirm changes**.

1. Confirm your new tag appears in the **Tags** section of the **Information** page.

**To delete a model group tag, complete the following steps:**

1. Open the SageMaker Studio console by following the instructions in [Launch Amazon SageMaker Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-launch.html).

1. In the left navigation pane, choose **Models** to display a list of your model groups.

1. Choose the **Registered models** tab, if not selected already.

1. Immediately below the **Registered models** tab label, choose **Model Groups**, if not selected already.

1. From the Model Groups list, select the name of the Model Group you want to edit.

1. In the model group page, choose the **Tags** tab.

1. Choose **Add/Edit tags**.

1. Choose the **Trash** icon next to the key-value pair you want to remove.

1. Choose **Confirm changes**.

**To edit a model group tag, complete the following steps:**

1. Open the SageMaker Studio console by following the instructions in [Launch Amazon SageMaker Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-launch.html).

1. In the left navigation pane, choose **Models** to display a list of your model groups.

1. Choose the **Registered models** tab, if not selected already.

1. Immediately below the **Registered models** tab label, choose **Model Groups**, if not selected already.

1. From the Model Groups list, select the name of the Model Group you want to edit.

1. In the model group page, choose the **Tags** tab.

1. Choose **Add/Edit tags**.

1. Enter a new value in the **Value** field of the key-pair you want to edit.

1. Choose **Confirm changes**.

------
#### [ Studio Classic ]

**To view a model group tag, complete the following steps:**

1. Sign in to Amazon SageMaker Studio Classic. For more information, see [Launch Amazon SageMaker Studio Classic](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-launch.html).

1. In the left navigation pane, choose the **Home** icon ( ![Home icon.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/studio/icons/house.png)).

1. Choose **Models**, and then **Model registry**.

1. From the Model Groups list, select the name of the Model Group you want to edit.

1. Choose **Information**.

1. View your tags in the **Tags** section of the **Information** page.

**To add a model group tag, complete the following steps:**

1. Sign in to Amazon SageMaker Studio Classic. For more information, see [Amazon SageMaker AI domain overview](gs-studio-onboard.md).

1. In the left navigation pane, choose the **Home** icon ( ![Home icon.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/studio/icons/house.png)).

1. Choose **Models**, and then **Model registry**.

1. From the Model Groups list, select the name of the Model Group you want to edit.

1. Choose **Information**.

1. If you don't have any tags, choose **Add tags**.

1. If you have pre-existing tags, choose **Manage tags** in the **Tags** section. A list of the model group's tags appears as key-value pairs.

1. Above **Add new tag**, enter your new key in the blank **Key** field.

1. (Optional) Enter your new value in the blank **Value** field.

1. Choose **Confirm changes**.

1. Confirm your new tag appears in the **Tags** section of the **Information** page.

**To delete a model group tag, complete the following steps:**

1. Sign in to Amazon SageMaker Studio Classic. For more information, see [Amazon SageMaker AI domain overview](gs-studio-onboard.md).

1. In the left navigation pane, choose the **Home** icon ( ![Home icon.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/studio/icons/house.png)).

1. Choose **Models**, and then **Model registry**.

1. From the Model Groups list, select the name of the Model Group you want to edit.

1. Choose **Information**.

1. In the **Tags** section, choose **Manage tags**. A list of the model group's tags appears as key-value pairs.

1. Choose the **Trash** icon to the right of the tag you want to remove.

1. Choose **Confirm changes**.

1. Confirm your removed tag does not appear in the **Tags** section of the **Information** page.

**To edit a model group tag, complete the following steps:**

1. Sign in to Amazon SageMaker Studio Classic. For more information, see [Amazon SageMaker AI domain overview](gs-studio-onboard.md).

1. In the left navigation pane, choose the **Home** icon ( ![Home icon.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/studio/icons/house.png)).

1. Choose **Models**, and then **Model registry**.

1. From the Model Groups list, select the name of the Model Group you want to edit.

1. Choose **Information**.

1. In the **Tags** section, choose **Manage tags**. A list of the model group's tags appears as key-value pairs.

1. Edit any key or value.

1. Choose **Confirm changes**.

1. Confirm your tag contains your edits in the **Tags** section of the **Information** page.

**To assign or tag model groups to a project, complete the following steps:**

1. Get tags with key `sagemaker:project-name` and `sagemaker:project-id` for the SageMaker AI project using the [ListTags](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListTags.html) API.

1. To apply the tags to your model package group, choose one of the following methods:
   + If you create a new model package group and want to add tags, pass your tags from Step 1 to the [CreateModelPackageGroup](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateModelPackageGroup.html) API.
   + If you want to add tags to an existing model package group, use the [AddTags](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AddTags.html) APIs.
   + If you create your model package group through Pipelines, use the `pipeline.create()` or `pipeline.upsert()` methods, or pass your tags to the [RegisterModel](https://docs.aws.amazon.com/sagemaker/latest/dg/build-and-manage-steps.html#step-type-register-model) step.

------