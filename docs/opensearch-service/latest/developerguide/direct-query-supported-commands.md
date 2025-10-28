# Supported SQL and PPL commands

OpenSearch SQL and OpenSearch Pipeline Processing Language (PPL) are languages for querying,
analyzing, and processing data in OpenSearch, CloudWatch Logs Insights, and Security Lake. You can use OpenSearch
SQL and OpenSearch PPL in OpenSearch Discover to query data within CloudWatch Logs, Amazon S3, or Security Lake. CloudWatch Logs
Insights also supports both OpenSearch PPL and OpenSearch SQL query languages, in addition to
Logs Insights QL, a purpose-built query language for analyzing CloudWatch Logs.

- **OpenSearch SQL**: OpenSearch SQL provides a familiar
  option if you're used to working with relational databases. OpenSearch SQL offers a
  subset of SQL functionality, making it a good choice for performing ad-hoc queries
  and data analysis tasks. With OpenSearch SQL, you can use commands such as SELECT,
  FROM, WHERE, GROUP BY, HAVING, and various other SQL commands and functions
  available in SQL. You can execute JOINs across tables (or log groups), correlate
  data across tables (or log groups) using subqueries, and use the rich set of JSON,
  mathematical, string, conditional, and other SQL functions to perform powerful
  analysis on log and security data.
- **OpenSearch PPL (Piped Processing Language):** With
  OpenSearch PPL, you can retrieve, query, and analyze data using piped-together
  commands, making it easier to understand and compose complex queries. Its syntax is
  based on Unix pipes, and enables chaining of commands to transform and process data.
  With PPL, you can filter and aggregate data, and use commands such as JOINs,
  subqueries, LOOKUP, and a rich set of math, string, date, conditional, and other
  functions for analysis.
  Although most of the commands in OpenSearch PPL and OpenSearch SQL query languages are
  common across CloudWatch Logs and OpenSearch, there are some differences in which set of commands and
  functions are supported in each of these services. For more details, see the tables on the
  following pages.

######

- [Supported OpenSearch SQL commands and
  functions](supported-directquery-sql.md "supported-directquery-sql.md")
  - [Additional information for
    CloudWatch Logs Insights users using OpenSearch SQL](supported-directquery-sql.md#supported-sql-for-multi-log-queries "supported-directquery-sql.md#supported-sql-for-multi-log-queries")
  - [General SQL restrictions](supported-directquery-sql.md#general-sql-restrictions "supported-directquery-sql.md#general-sql-restrictions")

- [Supported PPL commands](supported-ppl.md "supported-ppl.md")
  - [Additional information for
    CloudWatch Logs Insights users using OpenSearch PPL](supported-ppl.md#supported-ppl-for-cloudwatch-users "supported-ppl.md#supported-ppl-for-cloudwatch-users")
