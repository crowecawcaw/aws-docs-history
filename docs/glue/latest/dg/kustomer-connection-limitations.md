# Kustomer limitations

The following are limitations or notes for Kustomer:

- The `Customer Searches` entity is not supported since the Kustomer API documentation has not declared any endpoint for it.
- The support of filtration and incremental transfer on the `Klasses` entity is not supported.
- Order by can be supported on multiple applicable fields in a single request.

However, the order by functionality on multiple fields has been observed to behave inconsistently from the SaaS end for some combinations. It is unpredictable as there could be 'n' combinations that might show incorrect sorting results. For example:

For the `Customers` entity, order by `progressiveStatus desc, name asc` doesn't yield the correct sorted result. It sorts only based on the `progressiveStatus` order. If such a behaviour is observed, you can use a single field to be ordered upon.

- Order by on the field 'id' is only supported by the `Conversations` and `Messages` entities as a query parameter. For example: https://api.kustomerapp.com/v1/conversations?sort=desc (This sorts the results by 'id' in descending order.)

Additionally, any other filter or ordering on any other field is translated into a POST request body having the API endpoint as POST https://api.kustomerapp.com/v1/customers/search
To allow the support of ordering by 'id' in `Conversations` and `Messages`, either only order by id should be present or any other filter and/or order by on any other applicable field.

- Kustomer allows a maximum of 10K records to be fetched irrespective of a filtered or a non-filtered request. Due to this limitation, there will be data loss for any entity holding more than 10K records. There are two possible workarounds that you can perform to partially mitigate this:
  - Apply filters to fetch a specific set of records.
  - If there are more than 10K records with an applied filter, apply a successive filter value in a new subsequent request or apply ranges in filters. For example:

  1st request's filterExpression: `modifiedAt >= 2022-03-15T05:26:23.000Z and modifiedAt < 2023-03-15T05:26:23.000Z`

  Assume this exhausts the 10K record limit.

  Another request can be triggered with filterExpression: `modifiedAt >= 2023-03-15T05:26:23.000Z`

- As a SaaS behavior, the `CONTAINS` operator in Kustomer supports matching only on complete words and not partial matches within a word. For example: "body CONTAINS 'test record'" will match a record having 'test' in the 'body' field. However, "body CONTAINS 'test'" will not match a record having 'testAnotherRecord' in the 'body' field.
