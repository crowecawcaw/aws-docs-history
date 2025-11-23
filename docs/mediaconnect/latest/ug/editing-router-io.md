# Updating a router I/O in MediaConnect

When your requirements change, you can edit existing router I/Os to meet your needs. You
can update the I/O name, description, maximum bitrate, protocol settings, and other
configuration parameters at any time.

## Prerequisites

- The following procedure assumes you've already created at least one router
  I/O.
- If you want to update a router I/O's maintenance configuration, you must ensure
  that the router I/O is in **Standby** state.
- If you want to connect your router I/O to a MediaConnect flow, your flow must be
  set up for router integration. For more information, see [Integrating router
  I/Os with MediaConnect
  flows](integrate-flow-with-router.md "integrate-flow-with-router.md").
- If you want to connect your router output to a MediaLive input, your MediaLive
  input must be set up for router integration. For more information, see [Integrating router
  outputs
  with MediaLive inputs](integrate-eml-with-router.md "integrate-eml-with-router.md").

## Procedure

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/ "https://console.aws.amazon.com/mediaconnect/").
2. In the navigation pane, choose **Router inputs**.
3. Select the router input that you want to update and choose
   **Edit**.
4. Update the router input details as needed.
5. Choose **Save changes**.
6. Check the outcome:
   1. If successful: The router input will be updated with your changes.
   2. If unsuccessful: You'll see an error message explaining what went
      wrong.

7. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/ "https://console.aws.amazon.com/mediaconnect/").
8. In the navigation pane, choose **Router outputs**.
9. Select the router output that you want to update and choose
   **Edit**.
10. Update router output details as needed.
11. Choose **Save changes**.
12. Check the outcome:
    1. If successful: The router output will be updated with your changes.
    2. If unsuccessful: You'll see an error message explaining what went
       wrong.

## Next steps

After you update a router I/O, you can [review the
updated I/O](viewing-router-io.md "viewing-router-io.md") to verify that your updates were successful.

## Additional resources

To update router I/Os programmatically, see the following pages in the _MediaConnect API Reference_:

- [UpdateRouterInput](../api/API_UpdateRouterInput.md "../api/API_UpdateRouterInput.md")
- [UpdateRouterOutput](../api/API_UpdateRouterOutput.md "../api/API_UpdateRouterOutput.md")

This includes information about how to use these operations and their parameters in
one of the language-specific AWS SDKs.
