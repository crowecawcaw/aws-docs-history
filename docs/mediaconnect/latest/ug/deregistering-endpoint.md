

# Deregistering an endpoint in MediaConnect
<a name="deregistering-endpoint"></a>

You can deregister source and destination endpoints that you no longer need.

**Important**  
Deregistering an endpoint is permanent and can't be undone. When you deregister an endpoint, MediaConnect disconnects it, stops sharing it, and removes it from your endpoint registry.

## Prerequisites
<a name="deregistering-endpoint-prerequisites"></a>
+ The following procedures assume that you have at least one endpoint in your AWS account.
+ You own the endpoint. You can't deregister an endpoint that another AWS account shares with you.

## Procedure
<a name="deregistering-endpoint-procedure"></a>

### To deregister a source endpoint
<a name="deregister-source-endpoint-section"></a><a name="deregister-source-endpoint-procedure"></a>

1. Open the [MediaConnect console](https://console.aws.amazon.com/mediaconnect/).

1. In the navigation pane, under **Endpoints**, choose **Source endpoints**.

1. Select the source endpoint that you want to deregister.

1. Choose **Deregister**.

1. In the confirmation dialog box, choose **Deregister source endpoint**.

### To deregister a destination endpoint
<a name="deregister-destination-endpoint-section"></a><a name="deregister-destination-endpoint-procedure"></a>

1. Open the [MediaConnect console](https://console.aws.amazon.com/mediaconnect/).

1. In the navigation pane, under **Endpoints**, choose **Destination endpoints**.

1. Select the destination endpoint that you want to deregister.

1. Choose **Deregister**.

1. In the confirmation dialog box, choose **Deregister destination endpoint**.

## Additional resources
<a name="deregistering-endpoint-additional-resources"></a>

For more information about deregistering endpoints programmatically, see the following pages in the *MediaConnect API Reference*:
+ [DeregisterSourceEndpoint](https://docs.aws.amazon.com/mediaconnect/latest/api/API_DeregisterSourceEndpoint.html)
+ [DeregisterDestinationEndpoint](https://docs.aws.amazon.com/mediaconnect/latest/api/API_DeregisterDestinationEndpoint.html)

This includes information about how to use these operations and parameters in one of the language-specific AWS SDKs.