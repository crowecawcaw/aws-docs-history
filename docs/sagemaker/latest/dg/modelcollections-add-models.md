# Add Model Groups to a

Collection

You can add model groups to a Collection in the Amazon SageMaker Studio console. To add
Model Groups to a Collection, complete the following steps based on whether you use
Studio or Studio Classic.

Studio

1. Open the SageMaker Studio console by following the
   instructions in [Launch
   Amazon SageMaker Studio](studio-updated-launch.md "studio-updated-launch.md").
2. In the left navigation pane, choose
   **Models**.
3. Choose the **Registered models** tab, if not
   selected already.
4. Immediately below the **Registered models**
   tab label, choose **Models**, if not selected
   already.
5. Select the check box next to the model groups that you want to
   add. You can select up to 10 Model Groups. If you select more
   than 10, the UI option to add your Model Groups to a Collection
   is inactive.
6. Choose the vertical ellipsis next to
   **Create**, and choose **Add to
   collection**.
7. Select the radio button for the collection to which you want
   to add your selected Model Groups.
8. Choose **Add to collection**.
9. Check to make sure your Model Groups were added in to the
   collection. In the **Collections** column of
   the Model Groups you selected, you should see the name of
   collection to which you added the Model Groups.

Studio Classic
You can add Model Groups to a Collection from either the
**Model Groups** or
**Collections** tab.

To add one or more Model Groups to a Collection from the **Collections** tab, complete the following steps:

1. Sign in to Amazon SageMaker Studio Classic. For more information, see [Launch
   Amazon SageMaker Studio Classic](studio-launch.md "studio-launch.md").
2. In the left navigation pane, choose the
   **Home** icon (
   ![Black square icon representing a placeholder or empty image.](images/studio/icons/house.png)
   ).
3. Choose **Models**, and then **Model
   registry**.
4. Choose the **Collections** tab.
5. Select the Collection to which you want to add Model Groups.
   If the desired Collection is not at root level, navigate to the
   hierarchy where you want to add your Model Groups.
6. In the **Actions** dropdown menu in the top
   right, choose **Add model groups**.
7. Select the Model Groups that you want to add. You can select
   up to 10 Model Groups. If you select more than 10, the UI option
   to add your Model Groups to a Collection is inactive.
8. Choose **Add to collection**.
9. Check to make sure your Model Groups were added in the current
   hierarchy. If you do not immediately see your new Model Groups,
   choose **Refresh**.

To add one or more Model Groups to a Collection from the
**Model Groups** tab, complete the following
steps:

1. Sign in to Studio Classic. For more information, see [Amazon SageMaker AI domain overview](gs-studio-onboard.md "gs-studio-onboard.md").
2. In the left navigation pane, choose the
   **Home** icon (
   ![Black square icon representing a placeholder or empty image.](images/studio/icons/house.png)
   ).
3. Choose **Models**, and then **Model
   registry**.
4. Choose the **Model Groups** tab.
5. Select the Model Groups that you want to add. You can select
   up to 10. If you select more than 10, the UI option to add your
   Model Groups to a Collection is inactive.
6. In the **Actions** dropdown menu in the top
   right, choose **Add to collection**.
7. In the pop-up dialog, choose the root path location
   `Collections`. This link to the root location
   appears above the table.
8. Navigate to the hierarchy which contains your destination
   Collection, or where you want to create a new Collection to
   which you add your models.
9. (Optional) To add your Model Groups to an existing Collection,
   complete the following steps:
   1. Select the destination Collection.
   2. Choose **Add to collection**.

10. (Optional) To add your Model Groups to a new Collection,
    complete the following steps:
    1. Choose **New collection**.
    2. Enter a name for your new Collection.
    3. Choose **Create**.
