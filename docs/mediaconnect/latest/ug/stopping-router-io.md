

# Stopping a router I/O in MediaConnect
<a name="stopping-router-io"></a>

You can stop a router input or output when you need to temporarily pause its operation. When you stop an I/O, it changes to a `Standby` state and stops incurring charges.

Important things to know about stopping I/Os:
+ You can stop and start a router I/O at any time.
+ Stopping a router I/O doesn't affect your other I/Os or their takes.
+ When you stop an I/O, MediaConnect cancels any maintenance restarts that were scheduled when the I/O was started.
+ When you stop an I/O, its routing assignments remain in place. For example:
+ 
  + If you stop an output, it maintains its input assignment and will resume the same connection when restarted.
  + If you stop an input, connected outputs will stop receiving video, but their routing connections and capacity reservations are preserved.

## Prerequisites
<a name="stopping-router-io-prerequisites"></a>

Before you start, ensure you have:
+ An active router input or router output
+ No active processes that require the I/O

## Procedure
<a name="stopping-router-io-procedure"></a>

Follow these steps to stop a router input or a router output.

### To stop a router input
<a name="stop-router-input-section"></a><a name="deactivate-router-io-procedure"></a>

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/).

1. In the navigation pane, choose **Router inputs**.

1. Select the router input that you want to stop.

1. Choose **Stop**.

1. Check the outcome:

   1. If successful: The router input status will change to **Stopping**, then **Standby**.

   1. If unsuccessful: You'll see an error message explaining what went wrong.

### To stop a router output
<a name="stop-router-output-section"></a><a name="deactivate-router-io-procedure"></a>

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/).

1. In the navigation pane, choose **Router outputs**.

1. Select the router output that you want to stop.

1. Choose **Stop**.

1. In the confirmation dialog, choose **Stop router output**.

1. Check the outcome:

   1. If successful: The router output status will change to **Stopping**, then **Standby**.

   1. If unsuccessful: You'll see an error message explaining what went wrong.

## Next steps
<a name="stopping-router-io-next-steps"></a>

After stopping an I/O, you can:
+ [Restart the I/O](starting-router-io.md) later when needed.
+ [Delete the I/O](deleting-router-io.md) if you won't use it again.
+ [Create a new I/O](creating-router-io.md) with different settings.

## Additional resources
<a name="stopping-router-io-additional-resources"></a>

To stop router I/Os programmatically, see the following pages in the *MediaConnect API Reference*:
+ [StopRouterInput](https://docs.aws.amazon.com/mediaconnect/latest/api/API_StopRouterInput.html)
+ [StopRouterOutput](https://docs.aws.amazon.com/mediaconnect/latest/api/API_StopRouterOutput.html)

This includes information about how to use the `StopRouterInput` and `StopRouterOutput` operations and parameters in one of the language-specific AWS SDKs.