# Limitations

The following are limitations of the Zendesk connector:

- Offset-based pagination limits the number of pages that can be fetched to 100, but it not recommended as the total number of records that can be fetched is 10,000. However, the cursor-based pagination that is implemented for the Zendesk connector overcomes this limitation. Only the EQUAL_TO filter operator is supported through the Zendesk API.

Because of this limitation, partitioning is not supported for the Zendesk connector.

- For the "Ticket Event" entity the Rate Limit is 10 requests per minute. While running a AWS Glue ETL job you may receive a 429 (too many requests) error.
