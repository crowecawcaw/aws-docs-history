

# Updating a router I/O in MediaConnect
<a name="editing-router-io"></a>

When your requirements change, you can edit existing router I/Os to meet your needs. You can update the I/O name, description, maximum bitrate, protocol settings, and other configuration parameters at any time.

## Prerequisites
<a name="editing-router-io-prerequisites"></a>
+ The following procedure assumes you've already created at least one router I/O.
+ If you want to update a router I/O's maintenance configuration, you must ensure that the router I/O is in **Standby** state.
+ If you want to connect your router I/O to a MediaConnect flow, your flow must be set up for router integration. For more information, see [Integrating router I/Os with MediaConnect flows](integrate-flow-with-router.md).
+ If you want to connect your router output to a MediaLive input, your MediaLive input must be set up for router integration. For more information, see [Integrating router I/Os with MediaLive](integrate-eml-with-router.md).
+ If you want to connect your router input to, or disconnect it from, a MediaLive channel output, your MediaLive channel must have a MediaConnect Router output group configured. For more information, see [Integrating router I/Os with MediaLive](integrate-eml-with-router.md).

## Procedure
<a name="editing-router-io-procedure"></a>

### To update a router input
<a name="edit-router-input-section"></a><a name="edit-router-input-procedure"></a>

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/).

1. In the navigation pane, choose **Router inputs**.

1. Select the router input that you want to update and choose **Edit**.

1. Update the router input details as needed.

1. Choose **Save changes**.

1. Check the outcome:

   1. If successful: The router input will be updated with your changes.

   1. If unsuccessful: You'll see an error message explaining what went wrong.

### To update a router output
<a name="edit-router-output-section"></a><a name="edit-router-output-procedure"></a>

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/).

1. In the navigation pane, choose **Router outputs**.

1. Select the router output that you want to update and choose **Edit**.

1. Update router output details as needed.
**Note**  
You cannot change the **Recovery latency mode** while the output is taking an input. Clear the input assignment for the output, and then change the mode.

1. Choose **Save changes**.

1. Check the outcome:

   1. If successful: The router output will be updated with your changes.

   1. If unsuccessful: You'll see an error message explaining what went wrong.

## Next steps
<a name="editing-router-io-next-steps"></a>

After you update a router I/O, you can [review the updated I/O](viewing-router-io.md) to verify that your updates were successful.

## Additional resources
<a name="editing-router-io-additional-resources"></a>

To update router I/Os programmatically, see the following pages in the *MediaConnect API Reference*:
+ [UpdateRouterInput](https://docs.aws.amazon.com/mediaconnect/latest/api/API_UpdateRouterInput.html)
+ [UpdateRouterOutput](https://docs.aws.amazon.com/mediaconnect/latest/api/API_UpdateRouterOutput.html)

This includes information about how to use these operations and their parameters in one of the language-specific AWS SDKs.