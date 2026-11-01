

# Using the Connection manager in MediaConnect
<a name="using-connection-manager"></a>

The Connection manager gives you a visual map of your media workflow, from the sources that send content, through your router inputs and outputs, to the destinations that receive it. You can use it to connect endpoints, route content, and create router inputs and outputs, all from one place.

## Prerequisites
<a name="using-connection-manager-prerequisites"></a>

The following procedures assume that you have one or more endpoints in your endpoint registry.

## Procedure
<a name="using-connection-manager-procedure"></a>

### Choosing endpoints to work with
<a name="connection-manager-choosing-endpoints"></a><a name="open-connection-manager-procedure"></a>

**To choose endpoints**

1. Open the [MediaConnect console](https://console.aws.amazon.com/mediaconnect/).

1. In the navigation pane, under **Operational views**, choose **Connection manager**.

1. Choose **Configure**.

1. In the **Choose endpoints** panel, select the endpoints that you want to work with on the **Sources**, **Router inputs**, **Router outputs**, and **Destinations** tabs.

The Connection manager shows the endpoints that you choose and how they connect. Each endpoint appears as a card that shows its name, state, type, and Availability Zone or Region. Router inputs and outputs also show any messages they report, and router inputs show a preview of their signal.

### Connecting and disconnecting endpoints
<a name="connection-manager-connecting"></a><a name="make-connection-procedure"></a>

**To connect endpoints**

1. Drag from the connection point on the edge of an endpoint's card to the endpoint that you want to connect it to.

1. If the **Make connection** dialog box opens, review the changes, and then choose **Make connection**.

The connection is made as soon as you release the drag. The **Make connection** dialog box opens only when MediaConnect must release existing connections first, or when the change creates router inputs and outputs. To move a connection, connect one of its endpoints to a different endpoint.<a name="disconnect-connection-procedure"></a>

**To disconnect endpoints**

1. Choose the line between the two endpoints.

1. In the **Disconnect endpoints** dialog box, choose **Disconnect**.

### Creating router inputs and outputs as you connect
<a name="connection-manager-creating-router-io"></a>

You can create a router input or router output in the Connection manager while you connect endpoints. MediaConnect names the new router input or output after the endpoint and places it in the same Availability Zone.<a name="quick-create-router-io-procedure"></a>

**To create a router input or output as you connect**

1. Drag from the connection point on a source or destination card, and release over an empty spot in the **Router inputs** or **Router outputs** column.

1. In the **Make connection** dialog box, review the steps, and then choose **Make connection**.

If you release a source over the **Router outputs** column, or a destination over the **Router inputs** column, MediaConnect creates both a router input and a router output and routes between them.

#### Connecting two standard endpoints
<a name="connecting-standard-endpoints"></a>

When you connect two standard endpoints in the Connection manager, it creates a router input and a router output to link them. It then connects each standard endpoint to one of them and routes the input to the output.

**Note**  
You pay for the router input and router output that the Connection manager creates at the same rates as any other router input and output. For more information about pricing, see [Pricing for MediaConnect](what-is-pricing.md).

### Routing between router inputs and outputs
<a name="connection-manager-routing"></a>

You can also route content between router inputs and router outputs in the Connection manager. For other ways to manage routes, see [Managing routes in MediaConnect](assigning-route.md).<a name="route-connection-manager-procedure"></a>

**To route a router input to a router output**
+ Drag from the connection point on the router side of a router input's card to a router output. The route takes effect immediately.<a name="unroute-connection-manager-procedure"></a>

**To unroute a router output**

1. Choose the route line between the router input and the router output.

1. In the **Unroute router output** dialog box, choose **Unroute**.

### Highlighting a signal path
<a name="connection-manager-highlighting"></a><a name="highlight-signal-path-procedure"></a>

**To highlight a signal path**

1. Choose an endpoint's card. The Connection manager highlights the endpoints and connections on its signal path.

1. To clear the highlight, choose the card again.

Each card also has an actions menu with **View resource**, and **Start** and **Stop** for router inputs and outputs.

## Additional resources
<a name="using-connection-manager-additional-resources"></a>

The Connection manager uses the same endpoint operations that you can call directly. For more information about connecting and disconnecting endpoints programmatically, see the following pages in the *MediaConnect API Reference*:
+ [ConnectEndpoints](https://docs.aws.amazon.com/mediaconnect/latest/api/API_ConnectEndpoints.html)
+ [DisconnectEndpoints](https://docs.aws.amazon.com/mediaconnect/latest/api/API_DisconnectEndpoints.html)

This includes information about how to use the `ConnectEndpoints` and `DisconnectEndpoints` operations and their parameters in one of the language-specific AWS SDKs.