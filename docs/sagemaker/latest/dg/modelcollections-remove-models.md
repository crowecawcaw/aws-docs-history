

# Remove Model Groups or Collections from a Collection
<a name="modelcollections-remove-models"></a>

When you remove Model Groups or Collections from a Collection, you are removing them from a particular grouping and not from the Model Registry. You can remove Model Groups from a Collection in the Amazon SageMaker Studio console.

To remove one or more Model Groups or Collections from a Collection, complete the following steps based on whether you use Studio or Studio Classic.

------
#### [ Studio ]

1. Open the SageMaker Studio console by following the instructions in [Launch Amazon SageMaker Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-launch.html).

1. In the left navigation pane, choose **Models**.

1. Choose the **Registered models** tab, if not selected already.

1. Immediately below the **Registered models** tab label, choose **Collections**.

1. Navigate to the Collection which contains the Model Groups or Collections you want to remove.

1. Select the Model Groups or Collections that you want to remove. You can select up to 10. If you select more than 10 Model Groups or Collections, the UI option to remove them is inactive.
**Important**  
You cannot simultaneously select Model Groups and Collections for removal. To remove both Model Groups and Collections, first remove Model Groups, and then remove Collections.
**Important**  
You cannot remove non-empty Collections. To remove a non-empty Collection, first remove its contents.

1. In the **Actions** dropdown menu in the top right, choose **Remove X items from collection** (where X is the number of Model Groups that you selected).

1. Confirm that you want to remove the selected Model Groups.

------
#### [ Studio Classic ]

1. Sign in to Amazon SageMaker Studio Classic. For more information, see [Launch Amazon SageMaker Studio Classic](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-launch.html).

1. In the left navigation pane, choose the **Home** icon ( ![Home icon.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/studio/icons/house.png)).

1. Choose **Models**, and then **Model registry**.

1. Choose the **Collections** tab.

1. Navigate to the Collection which contains the Model Groups or Collections you want to remove.

1. Select the Model Groups or Collections that you want to remove. You can select up to 10. If you select more than 10 Model Groups or Collections, the UI option to remove them is inactive.
**Important**  
You cannot simultaneously select Model Groups and Collections for removal. To remove both Model Groups and Collections, first remove Model Groups, and then remove Collections.
**Important**  
You cannot remove non-empty Collections. To remove a non-empty Collection, first remove its contents.

1. In the **Actions** dropdown menu in the top right, choose **Remove X items from collection** (where X is the number of Model Groups you selected).

1. Confirm that you want to remove the selected Model Groups.

------