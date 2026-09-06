

# Starting a router I/O in MediaConnect
<a name="starting-router-io"></a>

Before you can deliver content through the router, you must first start the router I/O that you want to use. This action changes the router input or output status to `Active`.

## Prerequisites
<a name="starting-router-io-prerequisites"></a>

The following procedure assumes that you've already created a router input or a router output.

## Procedure
<a name="starting-router-io-procedure"></a>

Follow these steps to start a router input or output.

### To start a router input
<a name="start-router-input-section"></a><a name="start-router-input-procedure"></a>

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/).

1. In the navigation pane, choose **Router inputs**.

1. Select the router input that you want to start.

1. Choose **Start**.

1. Check the outcome:

   1. If successful: You'll see the status change from **Standby** to **Starting**, and then to **Active**.

   1. If unsuccessful: You'll see an error message explaining what went wrong.

### To start a router output
<a name="start-router-output-section"></a><a name="start-router-output-procedure"></a>

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/).

1. In the navigation pane, choose **Router outputs**.

1. Select the router output that you want to start.

1. Choose **Start**.

1. Check the outcome:

   1. If successful: You'll see the status change from **Standby** to **Starting**, and then to **Active**.

   1. If unsuccessful: You'll see an error message explaining what went wrong.

## Next steps
<a name="starting-router-io-next-steps"></a>

You can now use these I/Os in your routing assignments. To assign routes between your inputs and outputs, see [Managing routes in MediaConnect](assigning-route.md).

## Additional resources
<a name="starting-router-io-additional-resources"></a>

To start router I/Os programmatically, see the following pages in the *MediaConnect API Reference*:
+ [StartRouterInput](https://docs.aws.amazon.com/mediaconnect/latest/api/API_StartRouterInput.html)
+ [StartRouterOutput](https://docs.aws.amazon.com/mediaconnect/latest/api/API_StartRouterOutput.html)

This includes information about how to use the `StartRouterInput` and `StartRouterOutput` operations and parameters in one of the language-specific AWS SDKs.