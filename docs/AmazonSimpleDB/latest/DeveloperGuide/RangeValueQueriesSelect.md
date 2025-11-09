# Queries on Attributes with Multiple Values

One of the unique features of Amazon SimpleDB is that it allows you to associate multiple values
with a single attribute. Internet-related attributes such as _tag_ or _keyword_ often contain
multiple values, which are easy to support through the Amazon SimpleDB data model and query
language.

###### Important

Each attribute is considered individually against the comparison conditions defined
in the predicate. Item names are selected if _any_ of the values match
the predicate condition. To change this behavior, use the `every()` operator to
return results where _every_ attribute matches the query expression.

This section shows queries on attributes with multiple values and their results.

###### Note

To view the source data for the queries, see
[Sample Query Data Set](UsingSelectSampleDataset.md "UsingSelectSampleDataset.md").

The following table shows some queries on attributes with multiple values, how they are
interpreted, and the results they return from the sample dataset.

| Select Expression                                                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Result                             |
| ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------- |
| `select<br>• from mydomain where Rating = '4 stars' or Rating = '****'`      | Retrieves all items with a 4 star (\*\*\*\*) rating.<br>The data set has this rating stored as both "4 stars" and "\*\*\*\*."<br>Amazon SimpleDB returns items that have either or both.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | 1579124585, 0802131786, B000T9886K |
| `select<br>• from mydomain where Keyword = 'Book' and Keyword = 'Hardcover'` | Retrieve all items that have the Keyword attribute as both "Book" and<br>"Hardcover."<br>Based on the data set, you might be surprised that the result did not return the<br>"1579124585" item. As described earlier, each value is evaluated<br>individually against the predicate expression. Since neither of the values<br>satisfies \*both<br>• comparisons defined in the predicate, the item name is not<br>selected.<br>To get the desired results, you can use the `select<br>• from mydomain<br>where Keyword = 'Book' intersection Keyword = 'Hardcover'` expression.<br>For more information, see [Multiple Attribute Queries](MultipleAttributeQueriesSelect.md "MultipleAttributeQueriesSelect.md"). | <none>                             |
| `select<br>• from mydomain where every(keyword) in ('Book', 'Paperback')`    | Retrieves all items where the only keyword is Book or Paperback. If<br>the item contains any other keyword entries, it is not returned.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | 0385333498, 0802131786             |
