# Multiple Attribute Queries

The previous examples show how to create expressions for single predicates. The
Amazon SimpleDB query language also supports constructing expressions across multiple predicates
using the `intersection` operator.

Multiple attribute queries work by producing a set of item names from each predicate and
applying the `intersection` operator. The intersection operator only
returns item names that appear in both result sets.

This section shows multiple attribute queries and their results.

###### Note

To view the source data for the queries, see
[Sample Query Data Set](UsingSelectSampleDataset.md "UsingSelectSampleDataset.md").

The following table shows some multiple attribute queries, how they are interpreted, and the
results they return from the sample dataset.

| Select Expression                                                                  | Description                                                                                                                                                                                                                                           | Result                 |
| ---------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| `select * from mydomain where Rating = '****'`                                     | Retrieves all items that have a "\*\*\*\*" Rating.                                                                                                                                                                                                    | 0802131786, 1579124585 |
| `select * from mydomain where every(Rating) = '****'`                              | Retrieves all items that only have a "\*\*\*\*" Rating. Items are not returned that have a multi-valued Rating attribute that contains any value other than '\*\*\*\*.'                                                                               | 0802131786             |
| `select * from mydomain where Keyword = 'Book' intersection Keyword = 'Hardcover'` | Retrieves all items that have a "Book" Keyword and a "Hardcover" Keyword. The first predicate produces 0385333498, 0802131786, and 1579124585. The second produces 1579124585. The intersection operator returns results that appear in both queries. | 1579124585             |
