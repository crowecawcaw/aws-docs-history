

# Compare Model Versions
<a name="model-registry-version-compare"></a>

As you generate model versions, you might want to compare models versions by viewing relevant model quality metrics side-by-side. For example, you might want to track accuracy by comparing mean squared error (MSE) values, or you might decide to remove models that perform poorly on selected measures. The following procedure shows you how to set up model version comparison in Model Registry using the Amazon SageMaker Studio Classic console.

## Compare Model Versions (Amazon SageMaker Studio Classic)
<a name="model-registry-version-compare-studio"></a>

**Note**  
You can only compare model versions the Amazon SageMaker Studio Classic console.

To compare model versions within a model group, complete the following steps:

1. Sign in to Studio Classic. For more information, see [Amazon SageMaker AI domain overview](gs-studio-onboard.md).

1. In the left navigation pane, choose the **Home** icon ( ![Home icon.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/studio/icons/house.png)).

1. Choose **Models**, and then **Model registry**.

1. From the model groups list, select the name of the Model Group you want to view. A new tab opens with a list of the model versions in the Model Group.

1. In the list of model versions, check the boxes next to the model versions you want to compare.

1. Choose the **Actions** dropdown menu, then choose **Compare**. A listing of model quality metrics appears for your selected models.