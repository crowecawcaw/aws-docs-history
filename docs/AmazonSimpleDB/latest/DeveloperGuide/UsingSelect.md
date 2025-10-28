# Using Select to Create Amazon SimpleDB Queries

This section describes `Select`, a function that takes query
expressions similar to the standard SQL `SELECT` statement.

Use the following format for the `Select` function.

```
select `output_list`
from `domain_name`
[where `expression`]
[`sort_instructions`]
[limit `limit`]
```

The `output_list` can be any of the following:

- \* (all attributes)
- itemName() (the item name only)
- count(\*)
- An explicit list of attributes (attribute1,..., attributeN)

| Name                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `domain_name`       | The domain to search.                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `expression`        | The match expression. This rest of this section provides examples of how to form select expressions.                                                                                                                                                                                                                                                                                                                                                     |
| `sort_instructions` | Sorts the results on a single attribute, in ascending or descending order. For information on sorting results, see [Sort](SortingDataSelect.md "SortingDataSelect.md").                                                                                                                                                                                                                                                                                  |
| `limit`             | The `limit` is the maximum number of results per page to return (default: 100, max. 2500). NoteThe total size of the response cannot exceed 1 MB. Amazon SimpleDB automatically adjusts the number of items returned per page to enforce this limit. For example, even if you ask to retrieve 2500 items, but each individual item is 10 KB in size, the system returns 100 items and an appropriate next token so you can get the next page of results. | The `expression` can be any of the following: <br>• <select expression> intersection <select expression> <br>• NOT <select expression> <br>• (<select expression>) <br>• <select expression> or <select expression> <br>• <select expression> and <select expression> <br>• <simple comparison> ###### Note For information on how to use quotes with Amazon SimpleDB, see [Select Quoting Rules](QuotingRulesSelect.md "QuotingRulesSelect.md"). |
