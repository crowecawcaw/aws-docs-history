# Deleting Custom Tape Pools

The following procedure explains how to delete a custom tape pool using the Storage Gateway
console. To perform this action programmatically using the API, see [DeleteTapePool](../APIReference/API_DeleteTapePool.md "../APIReference/API_DeleteTapePool.md") in the _Storage Gateway API Reference_.

You can delete a custom tape pool only if there are no archived tapes in the pool, and
there are no automatic tape creation policies attached to the pool. If you need to
delete automatic tape creation policies from a tape pool, see [Managing
Automatic Tape Creation](managing-automatic-tape-creation.md "managing-automatic-tape-creation.md").

###### To delete a custom tape pool using the Storage Gateway console

1. Open the Storage Gateway console at
   [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/ "https://console.aws.amazon.com/storagegateway/").
2. In the navigation pane, choose **Pools** to see the available
   pools.
3. Select one or more tape pools to delete.

If the **Tape Count** for the tape pools that you want to
delete is **0**, and if there are no automatic tape creation
policies that reference the custom tape pool, you can delete the pools. 4. Choose **Delete**. The confirmation dialog box
appears. 5. Verify that you want to delete the specified tape pools, then type the word
_delete_ in the confirmation box and choose
**Delete**.

###### Warning

This procedure permanently deletes the selected tape pools and can't
be undone.

After the tape pools are deleted, they disappear from the tape library.
