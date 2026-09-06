

# Delete a feature group
<a name="feature-store-delete-feature-group"></a>

You can use the console or the Amazon SageMaker Feature Store API to delete your feature group. The instructions on using Feature Store through the console depends on if you have enabled Studio or Studio Classic as your default experience. For more information about the differences between the two, or how to change your default, see [Amazon SageMaker Studio](studio-updated.md).

The following sections provide an overview on how to delete a feature group.

**Topics**
+ [Delete a feature group using the console](#feature-store-delete-feature-group-studio)
+ [Delete feature group example Python code](#feature-store-delete-feature-group-example)

## Delete a feature group using the console
<a name="feature-store-delete-feature-group-studio"></a>

This section shows two ways to delete a feature group in the console, depending on your default experience: Studio or Studio Classic.

### Delete feature group if Studio is your default experience (console)
<a name="feature-store-delete-feature-group-studio-updated"></a>

1. Open the Studio console by following instructions in [Launch Amazon SageMaker Studio Classic](studio-launch.md).

1. Choose **Data** in the left navigation pane to expand the dropdown list.

1. From the dropdown list, choose **Feature Store**.

1. (Optional) To view your feature groups, choose **My account**. To view shared feature groups, choose **Cross account**.

1. In the **Feature Group Catalog** tab, choose the feature group to delete under **Feature group name**.

1. Choose **Delete feature group**.

1. In the pop-up window, confirm deletion by entering **delete** in the field, then choose **Delete**.

### Delete feature group if Studio Classic is your default experience (console)
<a name="feature-store-delete-feature-group-studio-classic"></a>

1. Open the Studio Classic console by following the instructions in [Launch Amazon SageMaker Studio Classic](studio-launch.md).

1. In the left navigation pane, choose the **Home** icon (![Home icon.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/studio/icons/house.png)).

1. Choose **Data**.

1. From the dropdown list, choose **Feature Store**.

1. (Optional) To view your feature groups, choose **My account**. To view shared feature groups, choose **Cross account**.

1. In the **Feature Group Catalog** tab, choose the feature group to delete under **Feature group name**.

1. Choose **Delete feature group**.

1. In the pop-up window, confirm deletion by typing **delete** in the field, then choose **Delete**.

## Delete feature group example Python code
<a name="feature-store-delete-feature-group-example"></a>

The following code uses the [`DeleteFeatureGroup`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteFeatureGroup.html) API operation to delete your feature group using the AWS SDK for Python (Boto3). It assumes that you've set up Feature Store and created a feature group. For more information about getting started, see [Introduction to Feature Store example notebook](feature-store-introduction-notebook.md).

```
from sagemaker.core.helper.session_helper import Session
from sagemaker.mlops.feature_store import FeatureGroup

sagemaker_session = Session()
fg_name = '{{your-feature-group-name}}'

my_fg = FeatureGroup(feature_group_name=fg_name)
my_fg.delete()
```