

# Configuring PID remapping

You can configure PID remapping when you create or update a router output.

## Prerequisites
<a name="configuring-pid-remapping-prerequisites"></a>
+ A router output.

## Procedure
<a name="configuring-pid-remapping-procedure"></a>

### To configure PID remapping on a router output
<a name="configure-pid-remapping-section"></a><a name="configure-pid-remapping-procedure"></a>

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/).

1. In the navigation pane, choose **Router outputs**.

1. Choose **Create router output**, or select a router output and choose **Edit**.

1. Expand **Processors**, and for **PID remapping**, choose **Enabled**.

1. Choose the transport stream settings. For more information, see [Transport stream settings](pid-remapping-transport-stream-settings.md).

   1. For **Transport stream ID**, **Program number**, **Program map table PID**, and **Program clock reference PID**, choose **Passthrough** to keep the input value, or choose **Custom** and enter a **Custom value**.

1. Define the rules. For more information, see [Rules](pid-remapping-writing-rules.md).

   1. For **Default action**, choose **Pass**, **Null**, **Drop**, or **Map auto**.

   1. (Optional) Under **Auto map settings**, change the **Starting PID** and **PIDs per program**.

   1. Under **Rules**, choose **Add rule** for each rule, in the order that MediaConnect should process them. For each rule, choose a **Match expression** and an **Action**, and enter their values. To reorder rules, drag them.

1. Choose **Create router output** or **Save changes**.

### To turn off PID remapping on a router output
<a name="turn-off-pid-remapping-section"></a><a name="turn-off-pid-remapping-procedure"></a>

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/).

1. In the navigation pane, choose **Router outputs**.

1. Select the router output and choose **Edit**.

1. Expand **Processors**, and for **PID remapping**, choose **Disabled**.

1. Choose **Save changes**.

## Next steps
<a name="configuring-pid-remapping-next-steps"></a>
+ [Transport stream settings](pid-remapping-transport-stream-settings.md)
+ [Rules](pid-remapping-writing-rules.md)
+ [PID remapping examples](pid-remapping-examples.md)

## Additional resources
<a name="configuring-pid-remapping-additional-resources"></a>

To configure PID remapping programmatically, see the following pages in the *MediaConnect API Reference*:
+ [CreateRouterOutput](https://docs.aws.amazon.com/mediaconnect/latest/api/API_CreateRouterOutput.html)
+ [UpdateRouterOutput](https://docs.aws.amazon.com/mediaconnect/latest/api/API_UpdateRouterOutput.html)

This includes information about how to use the `CreateRouterOutput` and `UpdateRouterOutput` operations and parameters in one of the language-specific AWS SDKs.