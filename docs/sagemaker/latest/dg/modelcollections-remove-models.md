# Remove Model Groups or Collections

from a Collection

When you remove Model Groups or Collections from a Collection, you are removing
them from a particular grouping and not from the Model Registry. You can remove Model Groups
from a Collection in the Amazon SageMaker Studio console.

To remove one or more Model Groups or Collections from a Collection, complete the
following steps based on whether you use Studio or Studio Classic.

Studio

1. Open the SageMaker Studio console by following the
   instructions in [Launch
   Amazon SageMaker Studio](studio-updated-launch.md "studio-updated-launch.md").
2. In the left navigation pane, choose
   **Models**.
3. Choose the **Registered models** tab, if not
   selected already.
4. Immediately below the **Registered models**
   tab label, choose **Collections**.
5. Navigate to the Collection which contains the Model Groups or
   Collections you want to remove.
6. Select the Model Groups or Collections that you want to
   remove. You can select up to 10. If you select more than 10
   Model Groups or Collections, the UI option to remove them is
   inactive.

###### Important

You cannot simultaneously select Model Groups and
Collections for removal. To remove both Model Groups and
Collections, first remove Model Groups, and then remove
Collections.

###### Important

You cannot remove non-empty Collections. To remove a
non-empty Collection, first remove its contents. 7. In the **Actions** dropdown menu in the top
right, choose **Remove X items from
collection** (where X is the number of Model Groups
that you selected). 8. Confirm that you want to remove the selected Model
Groups.

Studio Classic

1. Sign in to Amazon SageMaker Studio Classic. For more information, see [Launch
   Amazon SageMaker Studio Classic](studio-launch.md "studio-launch.md").
2. In the left navigation pane, choose the
   **Home** icon (
   ![Black square icon representing a placeholder or empty image.](images/studio/icons/house.png)
   ).
3. Choose **Models**, and then **Model
   registry**.
4. Choose the **Collections** tab.
5. Navigate to the Collection which contains the Model Groups or
   Collections you want to remove.
6. Select the Model Groups or Collections that you want to
   remove. You can select up to 10. If you select more than 10
   Model Groups or Collections, the UI option to remove them is
   inactive.

###### Important

You cannot simultaneously select Model Groups and
Collections for removal. To remove both Model Groups and
Collections, first remove Model Groups, and then remove
Collections.

###### Important

You cannot remove non-empty Collections. To remove a
non-empty Collection, first remove its contents. 7. In the **Actions** dropdown menu in the top
right, choose **Remove X items from
collection** (where X is the number of Model Groups
you selected). 8. Confirm that you want to remove the selected Model
Groups.
