# Delete a feature group

You can use the console or the Amazon SageMaker Feature Store API to delete your feature group. The instructions
on using Feature Store through the console depends on if you have enabled Studio or Studio Classic as
your default experience. For more information about the differences between the two, or how to
change your default, see [Amazon SageMaker Studio](studio-updated.md "studio-updated.md").

The following sections provide an overview on how to delete a feature group.

###### Topics

- [Delete a feature group using the
  console](#feature-store-delete-feature-group-studio "#feature-store-delete-feature-group-studio")
- [Delete feature group example Python
  code](#feature-store-delete-feature-group-example "#feature-store-delete-feature-group-example")

## Delete a feature group using the

console

This section shows two ways to delete a feature group in the console, depending on your
default experience: Studio or Studio Classic.

1. Open the Studio console by following instructions in [Launch Amazon SageMaker Studio Classic](studio-launch.md "studio-launch.md").
2. Choose **Data** in the left navigation pane to expand the
   dropdown list.
3. From the dropdown list, choose **Feature Store**.
4. (Optional) To view your feature groups, choose **My account**. To
   view shared feature groups, choose **Cross account**.
5. In the **Feature Group Catalog** tab, choose the feature group to
   delete under **Feature group name**.
6. Choose **Delete feature group**.
7. In the pop-up window, confirm deletion by entering `delete`
   in the field, then choose **Delete**.
8. Open the Studio Classic console by following the instructions in [Launch Amazon SageMaker Studio Classic](studio-launch.md "studio-launch.md").
9. In the left navigation pane, choose the **Home** icon (
   ![Black square icon representing a placeholder or empty image.](images/studio/icons/house.png)
   ).
10. Choose **Data**.
11. From the dropdown list, choose **Feature Store**.
12. (Optional) To view your feature groups, choose **My account**. To
    view shared feature groups, choose **Cross account**.
13. In the **Feature Group Catalog** tab, choose the feature group to
    delete under **Feature group name**.
14. Choose **Delete feature group**.
15. In the pop-up window, confirm deletion by typing `delete` in
    the field, then choose **Delete**.

## Delete feature group example Python

code

The following code uses the [`DeleteFeatureGroup`](../APIReference/API_DeleteFeatureGroup.md "../APIReference/API_DeleteFeatureGroup.md") API operation to delete your feature group using
the AWS SDK for Python (Boto3). It assumes that you've set up Feature Store and created a feature group. For more
information about getting started, see [Introduction to Feature Store example
notebook](feature-store-introduction-notebook.md "feature-store-introduction-notebook.md").

```
import sagemaker
from sagemaker.feature_store.feature_group import FeatureGroup

sagemaker_session = sagemaker.Session()
fg_name = '`your-feature-group-name`'

my_fg = FeatureGroup(name=fg_name, sagemaker_session=sagemaker_session)
my_fg.delete()
```
