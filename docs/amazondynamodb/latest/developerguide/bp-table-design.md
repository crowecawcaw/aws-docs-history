# Best practices for DynamoDB table design

General design principles in Amazon DynamoDB recommend that you keep the number of tables
you use to a minimum. In the majority of cases, we recommend that you consider using a single table.
However if a single or small number of tables are not viable, these guidelines may be of use.

- The per account limit cannot be increased above 10,000 tables per account. If your application requires more tables, plan for distributing
  the tables across multiple accounts. For more information see [service, account, and table quotas in Amazon DynamoDB.](ServiceQuotas.md#limits-tables "ServiceQuotas.md#limits-tables")
- Consider control plane limits for concurrent control plane operations that might impact your table
  management.
- Work with AWS solution architects to validate your design patterns for multi-tenant designs.
