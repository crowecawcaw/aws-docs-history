# Using Views in Amazon DocumentDB 8.0

- Amazon DocumentDB 8.0 now supports views. Views function as virtual collections that present data based on specified aggregation operations. When you create a view, you define a query that transforms data from one or more source collections.
  Amazon DocumentDB 8.0 executes this query each time the view is accessed, without consuming additional storage resources. Unlike standard collections, views in Amazon DocumentDB 8.0 do not store documents on disk, making them an efficient solution for presenting transformed or filtered data to applications.
  To create a view in Amazon DocumentDB, you can use the createView command or the db.createView() helper method:

```

db.createView("viewName","sourceCollection",
[
    { $match: { status: "active" } },
    { $project: { _id: 1, name: 1, email: 1 } }
]
)

```

This creates a view named "viewName" based on "sourceCollection" that only includes active documents and projects only the \_id, name, and email fields.
Views in Amazon DocumentDB are read-only. Write operations on views will return an error.
For optimal performance with large datasets, you can structure your view pipelines to maximize efficiency.
For complex aggregation pipelines, it's recommended to use the $match stage as the first stage or early in the pipeline to reduce the number of documents subsequent stages need to process, thus improving query performance.

## Best Practices

Some best practices to follow with Views are listed below.

- Filter Early: Use $match stages early in view pipelines to reduce the amount of data processed.
- Avoid Complex Aggregations: For frequently accessed views with complex aggregations, consider creating a separate collection with precomputed results that are updated periodically.
- Index Planning: Ensure that fields used in view pipelines, especially in $match and $sort operations, are properly indexed on the source collection.
- Query Optimization: Use the explain command to understand how your view queries are executed and optimize accordingly.
- Alternatives for Views: Given the functional differences between Amazon DocumentDB and MongoDB views, consider using regular collections with scheduled updates as an alternative to views when encountering limitations.

## Aggregator Operator Compatibility

Amazon DocumentDB supports many aggregation operators in view definitions while continuing to expand compatibility. When using views, focus on these supported operators:

- $match for filtering documents
- $project for field selection and transformation
- $addFields for adding computed fields
- $sort for ordering results
- $limit and $skip for pagination

Some specialized operators like $currentOp, $replaceRoot, and $geoNear currently work in direct aggregation queries rather than view definitions.

## Leveraging Indexes and Views

Views in Amazon DocumentDB 8.0 use the indexes of the underlying collection. As a result, you cannot create, drop, or rebuild indexes on a view directly. However, well-designed indexes on the source collection can significantly improve view query performance
Below are some steps to optimize query performance on views:

- Ensure appropriate indexes exist on the source collection fields used in the view's pipeline, especially in $match and $sort operations
- Use the explain() method to analyze query execution plans and verify index usage. E.g., `db.viewName.find({...}).explain()`
