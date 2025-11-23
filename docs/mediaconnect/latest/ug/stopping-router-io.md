# Stopping a router I/O in MediaConnect

You can stop a router input or output when you need to temporarily pause its operation.
When you stop an I/O, it changes to a `Standby` state and stops incurring
charges.

Important things to know about stopping I/Os:

- You can stop and start a router I/O at any time.
- Stopping a router I/O doesn't affect your other I/Os or their takes.
- When you stop an I/O, MediaConnect cancels any maintenance restarts that were scheduled
  when the I/O was started.
- When you stop an I/O, its routing assignments remain in place. For example:
- - If you stop an output, it maintains its input assignment and will resume the
    same connection when restarted.
  - If you stop an input, connected outputs will stop receiving video, but their
    routing connections and capacity reservations are preserved.

## Prerequisites

Before you start, ensure you have:

- An active router input or router output
- No active processes that require the I/O

## Procedure

Follow these steps to stop a router input or a router output.

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/ "https://console.aws.amazon.com/mediaconnect/").
2. In the navigation pane, choose **Router inputs**.
3. Select the router input that you want to stop.
4. Choose **Stop**.
5. Check the outcome:
   1. If successful: The router input status will change to
      **Stopping**, then **Standby**.
   2. If unsuccessful: You'll see an error message explaining what went
      wrong.

6. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/ "https://console.aws.amazon.com/mediaconnect/").
7. In the navigation pane, choose **Router outputs**.
8. Select the router output that you want to stop.
9. Choose **Stop**.
10. In the confirmation dialog, choose **Stop router
    output**.
11. Check the outcome:
    1. If successful: The router output status will change to
       **Stopping**, then **Standby**.
    2. If unsuccessful: You'll see an error message explaining what went
       wrong.

## Next steps

After stopping an I/O, you can:

- [Restart the I/O](starting-router-io.md "starting-router-io.md") later when
  needed.
- [Delete the I/O](deleting-router-io.md "deleting-router-io.md") if you won't use it
  again.
- [Create a new I/O](creating-router-io.md "creating-router-io.md") with different
  settings.

## Additional resources

To stop router I/Os programmatically, see the following pages in the _MediaConnect API Reference_:

- [StopRouterInput](../api/API_StopRouterInput.md "../api/API_StopRouterInput.md")
- [StopRouterOutput](../api/API_StopRouterOutput.md "../api/API_StopRouterOutput.md")

This includes information about how to use the `StopRouterInput` and
`StopRouterOutput` operations and parameters in one of the language-specific
AWS SDKs.
