

# Connecting and disconnecting endpoints in MediaConnect
<a name="connecting-endpoints"></a>

You can connect a source endpoint to a destination endpoint so that content flows between the devices or resources that the endpoints represent, and disconnect them when you no longer need the connection. You can connect and disconnect endpoints in the MediaConnect console in two ways:
+ From the **Source endpoints** and **Destination endpoints** lists, by following the procedures on this page.
+ In the Connection manager, which shows your sources, router inputs and outputs, and destinations side by side so that you can connect and disconnect them visually. For more information, see [Using the Connection manager in MediaConnect](using-connection-manager.md).

You can also connect and disconnect endpoints programmatically with the MediaConnect API.

## Prerequisites
<a name="connecting-endpoints-prerequisites"></a>

The following procedures assume that you have a source endpoint and a destination endpoint in your endpoint registry.

## Procedure
<a name="connecting-endpoints-procedure"></a>

### To connect a source endpoint to a destination endpoint
<a name="connect-source-endpoint-section"></a><a name="connect-source-endpoint-procedure"></a>

1. Open the [MediaConnect console](https://console.aws.amazon.com/mediaconnect/).

1. In the navigation pane, choose **Source endpoints**.

1. Select the source endpoint that you want to connect.

1. Choose **Connect**.

1. In the **Connect endpoint** dialog box, select the destination endpoint that you want to connect to.

1. Choose **Connect**.

### To connect a destination endpoint to a source endpoint
<a name="connect-destination-endpoint-section"></a><a name="connect-destination-endpoint-procedure"></a>

1. Open the [MediaConnect console](https://console.aws.amazon.com/mediaconnect/).

1. In the navigation pane, choose **Destination endpoints**.

1. Select the destination endpoint that you want to connect.

1. Choose **Connect**.

1. In the **Connect endpoint** dialog box, select the source endpoint that you want to connect to.

1. Choose **Connect**.

### To disconnect a source endpoint
<a name="disconnect-source-endpoint-section"></a><a name="disconnect-source-endpoint-procedure"></a>

1. Open the [MediaConnect console](https://console.aws.amazon.com/mediaconnect/).

1. In the navigation pane, choose **Source endpoints**.

1. Select the source endpoint that you want to disconnect.

1. Choose **Disconnect**.

1. In the **Disconnect endpoints** dialog box, choose **Disconnect**.

### To disconnect a destination endpoint
<a name="disconnect-destination-endpoint-section"></a><a name="disconnect-destination-endpoint-procedure"></a>

1. Open the [MediaConnect console](https://console.aws.amazon.com/mediaconnect/).

1. In the navigation pane, choose **Destination endpoints**.

1. Select the destination endpoint that you want to disconnect.

1. Choose **Disconnect**.

1. In the **Disconnect endpoints** dialog box, choose **Disconnect**.

## Additional resources
<a name="connecting-endpoints-additional-resources"></a>

For more information about connecting and disconnecting endpoints programmatically, see the following pages in the *MediaConnect API Reference*:
+ [ConnectEndpoints](https://docs.aws.amazon.com/mediaconnect/latest/api/API_ConnectEndpoints.html)
+ [DisconnectEndpoints](https://docs.aws.amazon.com/mediaconnect/latest/api/API_DisconnectEndpoints.html)

This includes information about how to use the `ConnectEndpoints` and `DisconnectEndpoints` operations and their parameters in one of the language-specific AWS SDKs.