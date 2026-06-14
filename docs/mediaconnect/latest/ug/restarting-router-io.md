# Restarting a router I/O in MediaConnect

You can manually restart your router I/Os in MediaConnect when you need to perform maintenance
or system updates. MediaConnect automatically performs maintenance restarts every 60-66 days from
the initial start date. However, manual restarts give you additional flexibility to manage
your router I/Os on your own schedule.

###### Note

Restarting a router I/O also applies any pending maintenance updates and resets the
maintenance countdown. For more information about how maintenance works for router I/Os,
see [Maintenance in MediaConnect](maintenance.md "maintenance.md").

## Prerequisites

Before you start, ensure that you have an active router input or output.

## Procedure

Follow these steps to restart a router input or output.

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/ "https://console.aws.amazon.com/mediaconnect/").
2. In the navigation pane, choose **Router inputs**.
3. Select the router input that you want to restart.
4. Choose **Restart**.
5. The router input status changes to **Migrating** while
   it restarts, and then returns to **Active**.

6. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/ "https://console.aws.amazon.com/mediaconnect/").
7. In the navigation pane, choose **Router outputs**.
8. Select the router output that you want to restart.
9. Choose **Start**.
10. The router output status changes to **Migrating** while
    it restarts, and then returns to **Active**.

## Next steps

After manually restarting an I/O, you can:

- [Monitor its status](viewing-router-io.md "viewing-router-io.md") in the console
- [View the countdown](viewing-router-io.md "viewing-router-io.md") until the next
  scheduled maintenance restart
- [Update the maintenance schedule if needed](editing-router-io.md "editing-router-io.md")
  (must put I/O in standby mode first)

## Additional resources

To restart router I/Os programmatically, see the following pages in the _MediaConnect API Reference_:

- [RestartRouterInput](../api/API_RestartRouterInput.md "../api/API_RestartRouterInput.md")
- [RestartRouterOutput](../api/API_RestartRouterOutput.md "../api/API_RestartRouterOutput.md")

This includes information about how to use the `RestartRouterInput` and
`RestartRouterOutput` operations and parameters in one of the language-specific
AWS SDKs.
