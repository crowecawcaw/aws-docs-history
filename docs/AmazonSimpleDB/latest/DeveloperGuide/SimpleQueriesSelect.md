# Simple Queries

This section shows simple queries and their results.

###### Note

To view the source data for the queries, see
[Sample Query Data Set](UsingSelectSampleDataset.md "UsingSelectSampleDataset.md").

The following table shows some simple queries, how they are interpreted, and the results
they return from the sample dataset.

| Select Expression                                           | Description                                                                                                                                                                                                                                                   | Result                                         |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| `select<br>• from mydomain where Title = 'The Right Stuff'` | Retrieves all items where the attribute "Title" equals "The Right Stuff".                                                                                                                                                                                     | 1579124585                                     |
| `select<br>• from mydomain where Year > '1985'`             | Retrieves all items where "Year" is greater than "1985".<br>Although this looks like a numerical comparison, it is<br>lexicographical. Because the calendar won't change to five digits for<br>nearly 8,000 years, "Year" is not zero padded.                 | B000T9886K, B00005JPLW, B000SF3NGK             |
| `select<br>• from mydomain where Rating like '****%'`       | Retrieves all items that have at least a 4 star (\*\*\*\*) rating.<br>The prefix comparison is case-sensitive and exact and does not match<br>attributes that only have the "4 star" value, such as item B000T9886K.                                          | 0385333498, 1579124585, 0802131786, B000SF3NGK |
| `select<br>• from mydomain where Pages < '00320'`           | Retrieves all items that have less than 320 pages.<br>This attribute is zero padded in the data set and the select<br>expression, which allows for proper lexicographical comparison between the<br>strings. Items without this attribute are not considered. | 1579124585, 0802131786,                        |
