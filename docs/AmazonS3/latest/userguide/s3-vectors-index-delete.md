# Deleting a vector index

###### Note

Amazon S3 Vectors is in preview release for Amazon Simple Storage Service and is subject to change.

You can delete a vector index when you no longer need it. This operation permanently removes the index and all vectors that are stored within it.

###### Important

When you delete a vector index, you need to know the following:

- You can delete vector indexes even when the indexes contain vectors.
- All vectors stored in the index are permanently deleted
- All metadata associated with those vectors is permanently lost
- The operation can't be undone or reversed
- Any ongoing operations on the index will fail immediately
- Applications querying the index will receive errors
- The index name becomes available for reuse within the bucket
  Before you delete a vector index, verify the vector index. For more information about how to check the index details, see [GetIndex](../API/API_GetIndex.md "../API/API_GetIndex.md") in the _Amazon S3 API Reference_. For more information about how to list vectors inside the index to see what will be deleted, see [Listing vector indexes](s3-vectors-index-list.md "s3-vectors-index-list.md").

To delete a vector index, use the following example commands. Replace the `user input placeholders` with your own information.

```
aws s3vectors delete-index --vector-bucket-name "`amzn-s3-demo-vector-bucket`" \
          --index-name "`idx2`"
```

For more information about how to verify whether the index is deleted, see [Listing vector indexes](s3-vectors-index-list.md "s3-vectors-index-list.md").
