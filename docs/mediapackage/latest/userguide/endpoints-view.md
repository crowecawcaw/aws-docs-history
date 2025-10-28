# Viewing an origin endpoint in AWS Elemental MediaPackage

These steps shows how to view all origin endpoints that are configured in AWS Elemental MediaPackage.
You can view the details about a specific endpoint to obtain its playback URL, the
packaging settings, and the manifests within the endpoint. You can use the MediaPackage
console, the AWS CLI, or the MediaPackage API to view the details of an endpoint.

###### To view an origin endpoint

1. Access the channel that the endpoint is associated with, as described in [Viewing channel details in AWS Elemental MediaPackage](channels-view.md "channels-view.md").

The console shows all existing origin endpoints that are configured in MediaPackage. 2. (Optional) To adjust your viewing preferences, choose **Preferences**. For
example, you can adjust the page size and properties that you want to view. 3. To view more information about a specific origin endpoint, select that
origin endpoint from the **Origin Endpoints** list. For downstream device requests, you must
provide the endpoint URL from the **Endpoint URL** field or the
CloudFront CDN URL.
