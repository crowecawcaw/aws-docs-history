# Deleting an endpoint in AWS Elemental MediaPackage

Endpoints in MediaPackage can serve content until they're deleted. These steps shows how to
delete the endpoint if it should no longer respond to playback requests. You must delete
all endpoints from a channel before you can delete the channel.

###### Warning

If you delete an endpoint, the playback URL stops working.

You can use the MediaPackage console, the AWS CLI, or the MediaPackage API to
delete an endpoint.

###### To delete an endpoint

1. Access the channel that the endpoint is associated with, as described in [Viewing channel details in AWS Elemental MediaPackage](channels-view.md "channels-view.md").

The console shows all existing origin endpoints that are configured in MediaPackage. 2. Under **Origin endpoints**, choose the endpoint that you want to delete. 3. Choose **Delete**. 4. In the **Delete endpoints** confirmation dialog box, choose **Delete**.
