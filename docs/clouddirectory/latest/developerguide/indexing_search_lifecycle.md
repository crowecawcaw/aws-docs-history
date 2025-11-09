Amazon Cloud Directory is no longer be open to new customers. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") and [Amazon Neptune](https://aws.amazon.com/neptune/ "https://aws.amazon.com/neptune/"). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/ "https://aws.amazon.com/support/").

# Index Lifecycle

You can use the following API calls to help with the development lifecycle of indexes.

1. You create indexes with the `CreateIndex` API call. You supply an index definition structure that
   describes the attributes on attached objects that the index will track. The definition also
   indicates whether or not the index should enforce uniqueness. The result is an object ID for
   the new index, which should immediately be attached to your hierarchy like any other object.
   For example, this can be a branch dedicated to holding indexes.
2. You attach objects to the index manually with the `AttachToIndex` API call. The index then automatically tracks the values
   of its defined attributes on each attached object.
3. To use the indexes to search for objects with more efficient enumeration, call
   `ListIndex` and specify a range of values that you are interested
   in.
4. Use the `ListAttachedIndices` API call to enumerate the indexes that are attached
   to a given object.
5. Use the `DetachFromIndex` API call to remove objects from the index
   manually.
6. Once you detach all objects from the index, you can delete the index with the
   `DeleteObject` API call.
   There is no limit on the number of indexes within a directory, other than the limit on the
   space used by all objects. Indexes and their attachments do consume space, but it is similar to
   that consumed by nodes and parent–child links. There is a limit on the number of indexes
   that can be attached to a given object. For more information, see [Amazon Cloud Directory Limits](limits.md "limits.md").
