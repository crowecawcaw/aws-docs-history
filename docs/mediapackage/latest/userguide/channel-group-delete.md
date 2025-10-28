# Deleting a channel group from AWS Elemental MediaPackage

This guides shows how to delete a channel group to stop AWS Elemental MediaPackage from receiving
content. Before you can delete the channel group, you must delete the channel group's
channels and endpoints. For instructions, see [Deleting a channel in AWS Elemental MediaPackage](channels-delete.md "channels-delete.md") and [Deleting an endpoint in AWS Elemental MediaPackage](endpoints-delete.md "endpoints-delete.md"). You can use the MediaPackage console, MediaPackage
API, or AWS CLI to delete a channel group.

###### Warning

If you delete a channel group, you'll lose access to the egress domain URL. If
that happens, you must create a new channel group to replace it.

###### To delete a channel group

1. Open the MediaPackage console at [https://console.aws.amazon.com/mediapackage/](https://console.aws.amazon.com/mediapackage/ "https://console.aws.amazon.com/mediapackage/").

The console shows all existing channel groups that are configured in MediaPackage. 2. Select the name of the channel group that you want to delete. 3. Choose **Delete**. 4. Choose **Delete** in the confirmation dialog box.
