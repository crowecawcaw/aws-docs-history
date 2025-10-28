# SQL analytics

You can use the query editor to perform analysis using SQL. The query editor tool provides a
place to write and run queries, view results, and share your work with your team.

For information about getting started with the query editor, see [Get started with the query editor in
Amazon SageMaker Unified Studio](getting-started-querying.md "getting-started-querying.md").

###### Topics

- [Navigate the query editor](query-editor-navigate.md "query-editor-navigate.md")
- [Connect data resources](query-connect-resources.md "query-connect-resources.md")
- [Supported query engines](#w124aac60c15 "#w124aac60c15")
- [Create a query](query-create.md "query-create.md")
- [Generative SQL](generative-sql.md "generative-sql.md")
- [Review query history](query-history.md "query-history.md")
- [Schedule a query](query-schedule.md "query-schedule.md")

## Supported query engines

The Amazon SageMaker Unified Studio query editor supports the following query engines:

- Amazon Redshift. For more information, see [Query
  processing](../../../redshift/latest/dg/c-query-processing.md "../../../redshift/latest/dg/c-query-processing.md") in the Amazon Amazon Redshift Database Developer Guide.
- Amazon Athena. For more information, see [Running SQL
  queries using Amazon Athena](../../../athena/latest/ug/querying-athena-tables.md "../../../athena/latest/ug/querying-athena-tables.md") in the Amazon Amazon Athena User Guide.

Both engines use Querybooks to develop queries and work with data from one place. You can
change the query engine from the upper-right corner of the Querybook editor and selecting the
data source you want to use from the dropdown menu.
