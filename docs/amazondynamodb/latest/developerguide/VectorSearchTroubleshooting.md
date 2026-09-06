

# Troubleshooting vector indexes
<a name="VectorSearchTroubleshooting"></a>

The following table lists common issues when working with vector indexes and how to resolve them.


| Symptom | Cause | Resolution | 
| --- | --- | --- | 
| ValidationException: SearchConditionExpression must be provided when SearchSchema has a HASH key | The index defines a vector index partition key (HASH) in its SearchSchema, but the search did not supply its value. | Add the vector index partition key equality to SearchConditionExpression, for example Category = :cat, with a matching ExpressionAttributeValues entry. | 
| ValidationException: One element in SearchSchema is not defined in attribute definitions | A SearchSchema attribute (vector index partition key or inline filter) is not declared in the table's AttributeDefinitions. | Add every SearchSchema attribute to AttributeDefinitions with its type, the same way key attributes are declared for a global secondary index. | 
| ValidationException: Invalid comparator used in SearchConditionExpression | An operator other than = was used. Only the equality operator is currently supported for vector index partition key and inline filter attributes. | Rewrite the condition to use = only. Comparison, range, and set-membership operators are not yet available. | 
| ValidationException: Provided TopK value is out of valid range | TopK was outside 1 to 100. | Set TopK to a value from 1 to 100 inclusive. | 
| ValidationException: Cannot search backfilling vector index: <indexName> or ValidationException: The table does not have the specified index: <indexName> | The vector index is not yet ready for search. IndexStatus is CREATING, either while the index is provisioned or while it backfills existing data. | Use DescribeTable and wait until IndexStatus is ACTIVE and Backfilling is not true, then retry the search. Treat ValidationException as retryable during index creation. | 
| ValidationException: The table does not have the specified index: <indexName> when the index exists and DescribeTable reports IndexStatus ACTIVE | The dedicated search endpoint has not yet begun serving the index. DescribeTable and SearchVectors are served by different endpoints, and the search endpoint can briefly lag after the index becomes ACTIVE. | Retry the search. Treat ValidationException as retryable immediately after an index becomes ACTIVE. If the error persists, confirm the index name and that your network permits the search endpoint hostname. | 
| Write is rejected when writing an item with a vector | The vector has the wrong number of dimensions for the index. | Make sure the vector length matches the index Dimensions. See [Writing items with vector data](VectorSearchWorkingWith.md#VectorSearchWorkingWith.Write). | 
| Write is rejected with "Invalid type for parameter" | The vector attribute has a wrong data type. DynamoDB expects a list of 32-bit floating point numbers. Common causes include sending a String (S), a Number scalar (N), a Number Set (NS), or a List containing non-numeric elements. The error message pinpoints the offending element index when a single member has the wrong type. | Send the vector attribute as a List (L) of Numbers (N). Verify that every element in the list is a valid number and that the list length matches the index Dimensions. | 
| Item is no longer returned by SearchVectors after removing or omitting the vector index partition key attribute | Removing the vector index partition key attribute from an item (through REMOVE in UpdateItem) or omitting it in a PutItem does not produce an error. However, the item is silently de-indexed and no longer appears in search results, even though the base table item and its vector embedding still exist. | Make sure that every item you want to be searchable retains the vector index partition key attribute. If an item unexpectedly disappears from search results, verify that its partition key attribute is still present on the base table item. | 
| Write is rejected with "cannot contain an empty string value" or type mismatch for the vector index partition key | The vector index partition key attribute was set to an empty string or written with the wrong data type. DynamoDB rejects these writes because an index key attribute cannot be empty and must match the declared type. | Use a valid, non-empty value with the correct data type for the vector index partition key attribute. Check the index definition to confirm the expected type. | 
| An attribute is missing from search results | The vector index does not project this attribute. | You can only retrieve attributes projected into the index. To return additional attributes, recreate the index with a broader projection or set ProjectionType to ALL. | 

## Adding a partition key to an existing vector index
<a name="VectorSearchTroubleshooting.ChangePartitionKey"></a>

A vector index's `SearchSchema` is fixed at creation time. You cannot add, remove, or change the partition key (`HASH`) after you create the index. You also cannot change inline filter attributes. To change the schema, create a new index and migrate to it.

To add a partition key or change other `SearchSchema` attributes, complete the following steps.

1. Create a new vector index with the partition key you need. Use the `UpdateTable` API with a `Create` action in the `VectorIndexUpdates` parameter. Give the new index a different name. For instructions, see [Adding a vector index to an existing table](VectorSearchWorkingWith.md#VectorSearchWorkingWith.Create.ExistingTable).

1. Wait for the new index to finish backfilling. Call `DescribeTable` and confirm that `IndexStatus` is `ACTIVE` and `Backfilling` is `false`.

1. Update your application to send `SearchVectors` requests to the new index. Include the partition key value in `SearchConditionExpression`. For more information, see [Filtering with SearchConditionExpression](VectorSearchWorkingWith.md#VectorSearchWorkingWith.Search.Filtering).

1. After you confirm correct results, delete the old index to stop paying for its storage. Use the `UpdateTable` API with a `Delete` action in the `VectorIndexUpdates` parameter. For instructions, see [Deleting a vector index](VectorSearchWorkingWith.md#VectorSearchWorkingWith.Delete).

**Index operations do not affect base table data**  
Creating or deleting a vector index does not affect the base table or its items. DynamoDB re-derives vector data from the base table items during backfill.