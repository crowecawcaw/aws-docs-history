# Starting a router I/O in MediaConnect

Before you can deliver content through the router, you must first start the router I/O
that you want to use. This action changes the router input or output status to
`Active`.

## Prerequisites

The following procedure assumes that you've already created a router input or a router
output.

## Procedure

Follow these steps to start a router input or output.

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/ "https://console.aws.amazon.com/mediaconnect/").
2. In the navigation pane, choose **Router inputs**.
3. Select the router input that you want to start.
4. Choose **Start**.
5. Check the outcome:
   1. If successful: You'll see the status change from
      **Standby** to **Starting**, and then to
      **Active**.
   2. If unsuccessful: You'll see an error message explaining what went
      wrong.

6. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/ "https://console.aws.amazon.com/mediaconnect/").
7. In the navigation pane, choose **Router outputs**.
8. Select the router output that you want to start.
9. Choose **Start**.
10. Check the outcome:
    1. If successful: You'll see the status change from
       **Standby** to **Starting**, and then to
       **Active**.
    2. If unsuccessful: You'll see an error message explaining what went
       wrong.

## Next steps

You can now use these I/Os in your routing assignments. To assign routes between your
inputs and outputs, see [Managing routes in MediaConnect](assigning-route.md "assigning-route.md").

## Additional resources

To start router I/Os programmatically, see the following pages in the _MediaConnect API Reference_:

- [StartRouterInput](../api/API_StartRouterInput.md "../api/API_StartRouterInput.md")
- [StartRouterOutput](../api/API_StartRouterOutput.md "../api/API_StartRouterOutput.md")

This includes information about how to use the `StartRouterInput` and
`StartRouterOutput` operations and parameters in one of the language-specific
AWS SDKs.
