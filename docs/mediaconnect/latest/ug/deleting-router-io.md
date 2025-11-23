# Deleting a router I/O in MediaConnect

When you no longer need a router input or output, you can delete it from your
configuration. This permanently removes the I/O and frees up its resources. You might delete
a router I/O when you want to switch to a different routing setup or clean up your unused
resources.

###### Important

Deleting a router I/O is permanent and can't be undone. When you delete a router I/O,
any takes using this router I/O will be removed.

## Prerequisites

Before you start:

- Make sure that the I/O you want to delete is either in `Standby` or
  `Stopping` state.
- Make sure that the router I/O isn’t connected to a flow or a MediaLive
  channel.
- For inputs: Ensure the input is not assigned to any outputs.
- Consider documenting the I/O's configuration in case you need to recreate it
  later.

## Procedure

###### To delete a router input

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/ "https://console.aws.amazon.com/mediaconnect/").
2. In the navigation pane, choose **Router inputs**.
3. Select the input that you want to delete and choose **View
   resources**.
4. Choose **Delete**.
5. In the dialog box that appears, choose **Delete router
   input** to confirm your decision.
6. Check the outcome:
   1. If successful: The router output status will change to
      `Deleted`.
   2. If unsuccessful: You'll see an error message explaining what went
      wrong.

###### To delete a router output

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/ "https://console.aws.amazon.com/mediaconnect/").
2. In the navigation pane, choose **Router outputs**.
3. Select the router output that you want to delete and choose **View
   resource**.
4. Choose **Delete**.
5. In the dialog box that appears, choose **Delete router
   output** to confirm your decision.
6. Check the outcome:
   1. If successful: The router output status will change to
      `Deleted`.
   2. If unsuccessful: You'll see an error message explaining what went
      wrong.

## Next steps

After deleting an I/O, you can:

- [Create a new router I/O](creating-router-io.md "creating-router-io.md") with
  different settings if needed.
- [Review your remaining router I/Os](viewing-router-io.md "viewing-router-io.md") to
  ensure your routing setup is complete.

## Additional resources

To delete router I/Os programmatically, see the following pages in the _MediaConnect API Reference_:

- [DeleteRouterInput](../api/API_DeleteRouterInput.md "../api/API_DeleteRouterInput.md")
- [DeleteRouterOutput](../api/API_DeleteRouterOutput.md "../api/API_DeleteRouterOutput.md")

This includes information about how to use the `DeleteRouterInput` and
`DeleteRouterOutput` operations and parameters in one of the
language-specific AWS SDKs.
