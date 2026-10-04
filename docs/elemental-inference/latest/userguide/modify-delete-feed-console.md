

# Editing, archiving, and deleting feeds using the console
<a name="modify-delete-feed-console"></a>

To manage an existing feed, open the Elemental Inference console at [https://console.aws.amazon.com/elemental-inference/](https://console.aws.amazon.com/elemental-inference/). In the navigation pane, choose **Feeds**, and then select the feed to open its details page.

On the feed details page, take one of the following actions.
+ To edit a feed – Choose **Actions**, **Edit**. The **Edit feed** page opens with the same sections as the create-feed page, except tags. To change tags, use the **Tags** tab on the feed details page. On the **Edit feed** page, each output can also be enabled or disabled, or removed with **Remove**. Make your changes, and then choose **Save**. The **Feed outputs** tab is read-only. To change a feed's outputs, edit the feed.

  If you add a feature (an output), make sure that you have room in the [enabled outputs quota](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/elemental-inference/quotas) for Elemental Inference. The list of quotas is sorted alphabetically. Look for quotas that don't start with "Request rate for".

  An output that was created by an association, for example by an MediaLive channel, is managed by the associated resource. Editing it might affect the associated service.
+ To archive a feed – Choose **Actions**, **Archive**, and then confirm. Archiving removes the feed's association. Archived feeds can no longer be updated or handle traffic, but you can still delete them. You can archive only active feeds that have an association.
+ To delete a feed – Choose **Actions**, **Delete**, and then confirm. This permanently deletes the feed. You can't undo this action.

You can also archive or delete feeds directly from the **Feeds** list. Select one or more feeds, and then choose **Actions**.

**Note**  
Archived and deleted feeds can't be edited.