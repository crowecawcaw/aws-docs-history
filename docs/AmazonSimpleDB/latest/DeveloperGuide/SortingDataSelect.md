# Sort

Amazon SimpleDB supports sorting data on a single attribute or the item names, in ascending (default) or
descending order. This section describes how to sort the result set returned from
`Select`.

###### Note

All sort operations are performed in lexicographical order.

The sort attribute must be present in at least one of the predicates of the
expression.

Because returned results must contain the attribute on which you are sorting, do not
use `is null` on the sort attribute. For example, `select * from mydomain
 where author is null and title is not null order by title` will succeed. However,
`select * from mydomain where author is null order by title` will fail because
`title` is not constrained by the `not null` predicate.

To view the source data for the queries, see [Sample Query Data Set](UsingSelectSampleDataset.md "UsingSelectSampleDataset.md").

The following table shows sort queries, how they are interpreted, and the results they
return from the sample dataset.

| Select Expression                                                                                 | Description                                                                             | Result                                                                         |
| ------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| `select * from mydomain where Year < '1980' order by Year asc`                                    | Retrieves all items released before 1980 and lists them in ascending order.             | 0802131786, 0385333498, 1579124585                                             |
| `select * from mydomain where Year < '1980' order by Year`                                        | Same as the previous entry, with "asc" (ascending) omitted.                             | 0802131786, 0385333498, 1579124585                                             |
| `select * from mydomain where Year = '2007' intersection Author is not null order by Author desc` | Retrieves all items released in 2007 and sorts them by author name in descending order. | B00005JPLW, B000T9886K                                                         |
| `select * from mydomain order by Year asc`                                                        | Invalid because Year is not constrained by a predicate in the where clause.             | InvalidSortExpression error. See [API Error Codes](APIError.md "APIError.md"). |
| `select * from mydomain where Year < '1980' order by Year limit 2`                                | Retrieves two items that were released before 1980 and lists them in ascending order.   | 0802131786, 0385333498                                                         |
| `select itemName() from mydomain where itemName() like 'B000%' order by itemName()`               | Retrieves all itemNames() that start with B000 and lists them in ascending order.       | B00005JPLW, B000SF3NGK, B000T9886K                                             |
