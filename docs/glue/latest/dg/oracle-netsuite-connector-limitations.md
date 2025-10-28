# Limitations and notes for Oracle NetSuite connector

The following are limitations or notes for the Oracle NetSuite connector:

- The values of the access_token and refresh_token parameters are in JSON Web Token (JWT) format. The access token is valid for 60 minutes whereas the refresh_token is valid for seven days.
- During client ID and client secret generation, if you select "PUBLIC CLIENT" along with "AUTHORIZATION CODE GRANT", then the refresh token is only valid for three hours and is for one-time use only.
- You can fetch at most 1,00,000 records using the connector. For more information, refer to [Executing SuiteQL Queries Through REST Web Services](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_157909186990.html "https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_157909186990.html").
- Partitions are created such that each partition will fetch records in multiples of 1000, except possibly the last one which will fetch the remaining records.
- For Item, Transaction Line and Transaction Accounting Line objects, the connector will not support a few operators due to following reasons:
  - Applying the `EQUAL_TO`, `NOT_EQUAL_TO` filter operators to fields of type Date gives unreliable results.
  - Applying the `LESS_THAN_OR_EQUAL_TO` filter operator to fields of type Date gives unreliable results and behaves similar to the `LESS_THAN` operator.
  - Applying the `GREATER_THAN` filter operator to fields of type Date= gives unreliable results and behaves similar to `GREATER_THAN_OR_EQUAL_TO` operator.

- For Item, Transaction Line, Transaction Accounting Line, and Custom Record Type objects, boolean values come in the format T/F instead of the standard true/false. The connector maps the t/f values to true/false to ensure consistency in data.
