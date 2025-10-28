# Best practices for using bulk data operations in DynamoDB

DynamoDB supports batch operations such as `BatchWriteItem` using which you can
perform up to 25 `PutItem` and `DeleteItem` requests together. However, `BatchWriteItem` doesn't
support `UpdateItem` operations. When it comes to bulk updates, the distinction lies in the
requirements and the nature of the update. You can use other DynamoDB APIs such as
`TransactWriteItems` for batch size up to 100. When more items are involved, you can use
services such as AWS Glue, Amazon EMR, AWS Step Functions or use custom scripts and tools
like DynamoDB-shell for bulk updates.

###### Topics

- [Conditional batch update](BestPractices_ConditionalBatchUpdate.md "BestPractices_ConditionalBatchUpdate.md")
- [Efficient bulk operations](BestPractices_EfficientBulkOperations.md "BestPractices_EfficientBulkOperations.md")
