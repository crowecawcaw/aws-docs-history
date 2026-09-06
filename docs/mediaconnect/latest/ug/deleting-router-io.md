

# Deleting a router I/O in MediaConnect
<a name="deleting-router-io"></a>

When you no longer need a router input or output, you can delete it from your configuration. This permanently removes the I/O and frees up its resources. You might delete a router I/O when you want to switch to a different routing setup or clean up your unused resources.

**Important**  
Deleting a router I/O is permanent and can't be undone. When you delete a router I/O, any takes using this router I/O will be removed.

## Prerequisites
<a name="deleting-router-io-prerequisites"></a>

Before you start:
+ Make sure that the I/O you want to delete is either in `Standby` or `Stopping` state.
+ Make sure that the router I/O isn’t connected to a flow or a MediaLive channel.
+ For inputs: Ensure the input is not assigned to any outputs.
+ Consider documenting the I/O's configuration in case you need to recreate it later.

## Procedure
<a name="deleting-router-io-procedure"></a>

### To delete a router input
<a name="delete-router-input-section"></a><a name="delete-router-input-procedure"></a>

**To delete a router input**

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/).

1. In the navigation pane, choose **Router inputs**.

1. Select the input that you want to delete and choose **View resources**.

1. Choose **Delete**.

1. In the dialog box that appears, choose **Delete router input** to confirm your decision.

1. Check the outcome:

   1. If successful: The router output status will change to `Deleted`.

   1. If unsuccessful: You'll see an error message explaining what went wrong.

### To delete a router output
<a name="delete-router-output-section"></a><a name="delete-router-output-procedure"></a>

**To delete a router output**

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/).

1. In the navigation pane, choose **Router outputs**.

1. Select the router output that you want to delete and choose **View resource**.

1. Choose **Delete**.

1. In the dialog box that appears, choose **Delete router output **to confirm your decision.

1. Check the outcome:

   1. If successful: The router output status will change to `Deleted`.

   1. If unsuccessful: You'll see an error message explaining what went wrong.

## Next steps
<a name="deleting-router-io-next-steps"></a>

After deleting an I/O, you can:
+ [Create a new router I/O](creating-router-io.md) with different settings if needed.
+ [Review your remaining router I/Os](viewing-router-io.md) to ensure your routing setup is complete.

## Additional resources
<a name="deleting-router-io-additional-resources"></a>

To delete router I/Os programmatically, see the following pages in the *MediaConnect API Reference*:
+ [DeleteRouterInput](https://docs.aws.amazon.com/mediaconnect/latest/api/API_DeleteRouterInput.html)
+ [DeleteRouterOutput](https://docs.aws.amazon.com/mediaconnect/latest/api/API_DeleteRouterOutput.html)

This includes information about how to use the `DeleteRouterInput` and `DeleteRouterOutput` operations and parameters in one of the language-specific AWS SDKs.