# Editing and deleting a channel

You can edit an existing (saved) channel to change how it processes the input, and you can
delete a channel. However, you can edit or delete a channel only when it is not running.

## Editing a channel

You can edit any existing channel by editing, adding, or deleting output groups and outputs.
you can also edit, add, or delete the channel's video, audio, and caption encodes.

The channel must be idle (not running).

###### Note

You can't change the class for a channel by editing the channel.
Instead, see [Update the channel class—pipeline redundancy](edit-channel-class.md "edit-channel-class.md").

###### To edit a channel

1. On the **channels** page, choose the option by the channel name.
2. Choose actions, and then choose **edit**. The
   edit channel page appears. The details on this page are identical to those on
   the **create channel** page. For information about working with this page, see
   [Creating a channel from scratch](creating-channel-scratch.md "creating-channel-scratch.md").
3. When done, choose update channel.

Wait for the channel **state** to return to **idle**
before performing another action with this channel.

## Editing the tags associated with a channel

You can edit the tags associated with a channel at any time, when the channel is running or
when it is idle. You can add more tags (up to the [limit](tagging.md#tagging-restrictions "tagging.md#tagging-restrictions")), and you can delete tags.

###### To edit the tags in a channel

1. On the **Channels** page, choose the channel name.
2. Choose the Tags tab. Add or delete tags. To edit the value of an existing
   tag, delete the tag and add it again. For more information, see [Tagging resources](tagging.md "tagging.md").
3. When done, choose Save.

## Deleting a channel

You can delete a channel from the **Channels** list or the details view.

The channel must be idle (not running).

###### To delete a channel

1. On the **Channels** page, choose the option by the channel name.
2. If the channel is running, choose **Stop**.
3. Choose **Delete**.
