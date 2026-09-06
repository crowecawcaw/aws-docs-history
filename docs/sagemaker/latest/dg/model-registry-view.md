

# View Model Groups and Versions
<a name="model-registry-view"></a>

Model Groups and versions help you organize your models. You can view a list of the model versions in a Model Group by using either the AWS SDK for Python (Boto3) (Boto3) or the Amazon SageMaker Studio console.

## View a List of Model Versions in a Group
<a name="model-registry-view-list"></a>

You can view all of the model versions that are associated with a Model Group. If a Model Group represents all models that you train to address a specific ML problem, you can view all of those related models.

### View a List of Model Versions in a Group (Boto3)
<a name="model-registry-view-list-api"></a>

To view model versions associated with a Model Group by using Boto3, call the `list_model_packages` API operation, and pass the name of the Model Group as the value of the `ModelPackageGroupName` parameter. The following code lists the model versions associated with the Model Group you created in [Create a Model Group (Boto3)](model-registry-model-group.md#model-registry-package-group-api).

```
sm_client.list_model_packages(ModelPackageGroupName=model_package_group_name)
```

### View a List of Model Versions in a Group (Studio or Studio Classic)
<a name="model-registry-view-list-studio"></a>

To view a list of the model versions in a Model Group in the Amazon SageMaker Studio console, complete the following steps based on whether you use Studio or Studio Classic.

------
#### [ Studio ]

1. Open the SageMaker Studio console by following the instructions in [Launch Amazon SageMaker Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-launch.html).

1. In the left navigation pane, choose **Models** from the menu.

1. Choose the **Registered models** tab, if not selected already.

1. Immediately below the **Registered models** tab label, choose **Model Groups**, if not selected already.

1. From the model groups list, choose the angle bracket to the left of the model group you want to view.

1. A list of the model versions in the model group appears.

1. (Optional) Choose **View all**, if shown, to view additional model versions.

------
#### [ Studio Classic ]

1. Sign in to Amazon SageMaker Studio Classic. For more information, see [Launch Amazon SageMaker Studio Classic](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-launch.html).

1. In the left navigation pane, choose the **Home** icon ( ![Home icon.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/studio/icons/house.png)).

1. Choose **Models**, and then **Model registry**.

1. From the model groups list, select the name of the Model Group you want to view.

1. A new tab appears with a list of the model versions in the Model Group.

------