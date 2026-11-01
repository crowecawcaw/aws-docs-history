

# Stopping endpoint sharing in MediaConnect
<a name="stopping-endpoint-sharing"></a>

You can stop sharing an endpoint when you no longer want consuming accounts to use it. When you unshare an endpoint, MediaConnect removes it from every resource share that holds it.

## Prerequisites
<a name="stopping-endpoint-sharing-prerequisites"></a>

Your account owns one or more endpoints that it shares with other accounts. Only the sharing account can unshare an endpoint.

## Procedure
<a name="stopping-endpoint-sharing-procedure"></a><a name="stop-endpoint-sharing-procedure"></a>

**To stop sharing an endpoint**

1. Open the [MediaConnect console](https://console.aws.amazon.com/mediaconnect/).

1. In the navigation pane, under **Endpoints**, choose **Source endpoints** or **Destination endpoints**.

1. Select the endpoint that you want to stop sharing.

1. Choose **Unshare**.

1. Review **Accounts losing access**. It lists every account that can reach the endpoint through a resource share. All of these accounts lose access when you unshare the endpoint.

1. If unsharing would leave a resource share empty, choose one of the following options:

   1. **Keep the resource shares** - Keep the empty resource shares so that you can reuse them later.

   1. **Delete the resource shares** - Delete the resource shares that would be left empty.

1. To confirm, choose **Unshare**. If you chose to delete the resource shares, the button reads **Unshare and delete** followed by the number of resource shares.

When you unshare an endpoint, MediaConnect disconnects any active connection that a consuming account has to the endpoint. The endpoint stays registered in your account.

To stop sharing every endpoint in a resource share, delete the resource share in the AWS RAM console.

**Important**  
Deleting a resource share is permanent and can't be undone. When you delete a resource share, every consuming account loses access to all the endpoints in it.

## Additional resources
<a name="stopping-endpoint-sharing-additional-resources"></a>

For more information about managing and deleting resource shares, see the [AWS RAM User Guide](https://docs.aws.amazon.com/ram/latest/userguide/).