# Range Queries

Amazon SimpleDB enables you to execute more than one comparison against attribute values within
the same predicate. This is most commonly used to specify a range of values.

This section shows range queries and their results.

###### Note

To view the source data for the queries, see
[Sample Query Data Set](UsingSelectSampleDataset.md "UsingSelectSampleDataset.md").

The following table shows some range queries, how they are interpreted, and the results they
return from the sample dataset.

| Select Expression                                                                                     | Description                                                                                                                                                                                                       | Result                                         |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| `select * from mydomain where Year > '1975' and Year < '2008'`                                        | Retrieves all items that have a "Year" value between "1975" and "2008", excluding "1975" and "2008".                                                                                                              | 1579124585, B000T9886K, B00005JPLW, B000SF3NGK |
| `select * from mydomain where Year between '1975' and '2008'`                                         | Retrieves all items that have a "Year" value between "1975" and "2008", including "1975" and "2008".                                                                                                              | 1579124585, B000T9886K, B00005JPLW, B000SF3NGK |
| `select * from mydomain where Rating = '***' or Rating = '*****'`                                     | Retrieves all items that have 3 (\*\*\*) or 5 (\*\*\*\*\*) star rating This is a discontiguous range query that consists of two distinct values selected from the range of all possible values for the attribute. | 0385333498, B00005JPLW, B000SF3NGK             |
| `select * from mydomain where (Year > '1950' and Year < '1960') or Year like '193%' or Year = '2007'` | Retrieves all items where the "Year" attribute is either between "1950" and "1960", excluding "1950" and "1960", or falls in the nineteen-thirties, or equals "2007".                                             | 0385333498, 0802131786, B000T9886K, B00005JPLW |
