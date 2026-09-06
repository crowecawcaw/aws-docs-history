

# Restarting a router I/O in MediaConnect
<a name="restarting-router-io"></a>

You can manually restart your router I/Os in MediaConnect when you need to perform maintenance or system updates. MediaConnect automatically performs maintenance restarts every 60-66 days from the initial start date. However, manual restarts give you additional flexibility to manage your router I/Os on your own schedule.

**Note**  
Restarting a router I/O also applies any pending maintenance updates and resets the maintenance countdown. For more information about how maintenance works for router I/Os, see [Maintenance in MediaConnect](maintenance.md).

## Prerequisites
<a name="restarting-router-io-prerequisites"></a>

Before you start, ensure that you have an active router input or output.

## Procedure
<a name="restarting-router-io-procedure"></a>

Follow these steps to restart a router input or output.

### To restart a router input
<a name="restart-router-input-section"></a><a name="restart-router-input-procedure"></a>

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/).

1. In the navigation pane, choose **Router inputs**.

1. Select the router input that you want to restart.

1. Choose **Restart**.

1. The router input status changes to **Migrating** while it restarts, and then returns to **Active**.

### To restart a router output
<a name="restart-router-output-section"></a><a name="start-router-output-procedure"></a>

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/).

1. In the navigation pane, choose **Router outputs**.

1. Select the router output that you want to restart.

1. Choose **Start**.

1. The router output status changes to **Migrating** while it restarts, and then returns to **Active**.

## Next steps
<a name="restarting-router-io-next-steps"></a>

After manually restarting an I/O, you can: 
+ [Monitor its status](viewing-router-io.md) in the console
+ [View the countdown](viewing-router-io.md) until the next scheduled maintenance restart
+ [Update the maintenance schedule if needed](editing-router-io.md) (must put I/O in standby mode first)

## Additional resources
<a name="restarting-router-io-additional-resources"></a>

To restart router I/Os programmatically, see the following pages in the *MediaConnect API Reference*:
+  [ RestartRouterInput](https://docs.aws.amazon.com/mediaconnect/latest/api/API_RestartRouterInput.html) 
+ [RestartRouterOutput](https://docs.aws.amazon.com/mediaconnect/latest/api/API_RestartRouterOutput.html)

This includes information about how to use the `RestartRouterInput` and `RestartRouterOutput` operations and parameters in one of the language-specific AWS SDKs.