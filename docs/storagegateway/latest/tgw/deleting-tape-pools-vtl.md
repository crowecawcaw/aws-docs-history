

# Deleting Custom Tape Pools
<a name="deleting-tape-pools-vtl"></a>

The following procedure explains how to delete a custom tape pool using the Storage Gateway console. To perform this action programmatically using the API, see [DeleteTapePool](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_DeleteTapePool.html) in the *Storage Gateway API Reference*.

You can delete a custom tape pool only if there are no archived tapes in the pool, and there are no automatic tape creation policies attached to the pool. If you need to delete automatic tape creation policies from a tape pool, see [Managing Automatic Tape Creation](https://docs.aws.amazon.com/storagegateway/latest/tgw/managing-automatic-tape-creation.html).

**To delete a custom tape pool using the Storage Gateway console**

1. Open the Storage Gateway console at [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/).

1. In the navigation pane, choose **Pools** to see the available pools.

1. Select one or more tape pools to delete.

   If the **Tape Count** for the tape pools that you want to delete is **0**, and if there are no automatic tape creation policies that reference the custom tape pool, you can delete the pools.

1. Choose **Delete**. The confirmation dialog box appears.

1. Verify that you want to delete the specified tape pools, then type the word *delete* in the confirmation box and choose **Delete**.
**Warning**  
This procedure permanently deletes the selected tape pools and can't be undone.

   After the tape pools are deleted, they disappear from the tape library.