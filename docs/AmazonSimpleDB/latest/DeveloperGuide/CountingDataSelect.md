# Count

If you want to count the number of items in a result set instead of returning the
items, use `count(*)`. Instead of returning a list of items, Amazon SimpleDB returns
a single item called `Domain` with a `Count` attribute.

###### Note

If the count request takes more than five seconds, Amazon SimpleDB returns the number of items
that it could count and a next token to return additional results. The client is responsible
for accumulating the partial counts.

If Amazon SimpleDB returns a 408 Request Timeout, please resubmit the request.

The default result limit of 100 and maximum result limit of 2500 do not apply to
count(\*). However, you can restrict the maximum number of counted results using the
limit clause.

The next token returned by `count(*)` and `select` are interchangeable
as long as the `where` and `order by` clauses match. For example, if you want to return
the 200 items after the first 10,000 (similar to an offset), you can perform a count with a limit clause of 10,000
and use the next token to return the next 200 items with `select`.

The following table shows `count(*)` queries and the results they
return from the sample dataset.

###### Note

To view the source data for the queries, see
[Sample Query Data Set](UsingSelectSampleDataset.md "UsingSelectSampleDataset.md").

| Select Expression                                               | Description                                                            | Result |
| --------------------------------------------------------------- | ---------------------------------------------------------------------- | ------ |
| `select count(*) from mydomain where Title = 'The Right Stuff'` | Counts all items where the attribute "Title" equals "The Right Stuff." | 1      |
| `select count(*) from mydomain where Year > '1985'`             | Counts all items where "Year" is greater than "1985."                  | 3      |
| `select count(*) from mydomain limit 500`                       | Counts all items in the domain, with a limit of 500.                   | 6      |
| `select count(*) from mydomain limit 4`                         | Counts all items in the domain, with a limit of 4.                     | 4      |
