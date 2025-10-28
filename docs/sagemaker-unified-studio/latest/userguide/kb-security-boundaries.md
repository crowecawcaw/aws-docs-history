# Understanding security boundaries with structured data sources in an Amazon Bedrock knowledge

base

Use the following information to understand how security boundaries affect structured data sources
in an Amazon Bedrock knowledge base.

###### Topics

- [Accessing structured data in an Amazon Bedrock knowledge base](#kb-data-access "#kb-data-access")
- [Database and table selection as query
  guidelines](#kb-query-guidelines "#kb-query-guidelines")
- [Reliable security boundaries](#kb-reliable-boundaries "#kb-reliable-boundaries")
- [Best practices for sensitive data](#kb-best-practices "#kb-best-practices")

## Accessing structured data in an Amazon Bedrock knowledge base

When you create an Amazon Bedrock knowledge base with a structured data source such as Amazon Redshift,
the knowledge base operates with the same permissions as your project user role. This
means the knowledge base can potentially access any data that your project role has
permission to access. This includes all databases accessible to your project and tables
within those databases (both owned by your project and subscribed from other projects
through the Business Data Catalog).

## Database and table selection as query

guidelines

Configure your knowledge base by selecting a database and specifying which tables and
columns to use. Customize your selection by including or excluding tables and columns
according to your requirements. These selections help
the knowledge base generate more accurate SQL queries by:

- Focusing the model on relevant data sources
- Reducing unnecessary references to irrelevant tables or columns
- Helping prioritize which data should be considered when answering
  queries

However, due to the nature of large language model based SQL generation:

- These selections are treated as recommendations rather than strict security
  boundaries.
- The knowledge base may occasionally generate queries that reference databases,
  tables, or columns outside your specified selections.
- Actual query execution is still governed by your project's permissions.

## Reliable security boundaries

The guaranteed security boundary is at the project level. A knowledge base can never
access data from another project unless that data has been explicitly shared with your
project. All data access is subject to authentication and authorization through AWS Identity and Access Management
and Amazon DataZone project permissions.

## Best practices for sensitive data

If your project contains both sensitive and non-sensitive data, and you want to ensure
the knowledge base only accesses specific non-sensitive data, consider these
approaches:

### Create a Dedicated \*knowledge

base-safe\* project

- Create a separate project specifically for knowledge base usage
- Use the Business Data Catalog to publish only non-sensitive tables from
  source projects
- Have your knowledge base-safe project subscribe only to the tables
  intended for knowledge base access
- Build knowledge bases exclusively in this controlled environment

### Implement guardrails in your chat agent app

- Deploy guardrails to detect and block prompts that attempt to manipulate
  the knowledge base.
- Configure content filtering to prevent SQL injection patterns in
  prompts.
- Set up rejection criteria for prompts that try to bypass configured
  constraints.

For information about guardrails, see [Safeguard your Amazon Bedrock app with a guardrail](guardrails.md "guardrails.md").
