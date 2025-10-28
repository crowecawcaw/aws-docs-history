# Resetting an endpoint in AWS Elemental MediaPackage

These steps show how to reset an origin endpoint in MediaPackage. Resetting the endpoint
clears previous content from endpoint egress. For information about when you might want
to reset, see [Reset for AWS Elemental MediaPackage channels and endpoints](resetting.md "resetting.md").

You can use the MediaPackage console, the AWS CLI, or the MediaPackage API to reset an
endpoint.

###### To reset an endpoint (console)

1. Access the channel that the endpoint is associated with, as described in [Viewing channel details in AWS Elemental MediaPackage](channels-view.md "channels-view.md").

The console shows all existing origin endpoints that are configured in
MediaPackage. 2. Under **Origin endpoints**, choose the endpoint that you want
to reset and then choose **Reset history**.

MediaPackage might return old content from this endpoint in the first 30 seconds
after the endpoint reset. For best results, when possible, wait 30 seconds from
endpoint reset to send playback requests to this endpoint.
