# Editing a channel in AWS Elemental MediaPackage

These steps show how to edit
the description on a channel in MediaPackage and
your channel's policy settings. You can't edit the name of the channel.

You can use the MediaPackage console, MediaPackage API, or AWS CLI to edit a channel. When
you're editing a channel, don't put sensitive identifying information like customer
account numbers into free-form fields such as the name or description field. MediaPackage
doesn’t require that you supply any customer data. This includes when you work
with MediaPackage using the MediaPackage console, MediaPackage API, AWS CLI, or AWS SDKs. Any data that
you enter into MediaPackage might get picked up for inclusion in diagnostic logs or Amazon CloudWatch Events.

###### To edit a channel

1. Access the channel group that the channel is associated with, as described in [Viewing channel group details in AWS Elemental MediaPackage](channel-group-view.md "channel-group-view.md").
2. To edit a specific channel, select that channel from the **Channels** list.
3. On the channel's details page, choose **Edit**.
4. Make the changes that you want.
5. Choose **Update**.
