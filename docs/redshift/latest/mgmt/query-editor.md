Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Querying a database using the Amazon Redshift query

editor v1

Using the query editor is an easy way to run queries on databases hosted by your Amazon Redshift
cluster. After creating your cluster, you can immediately run queries by using the query
editor on the Amazon Redshift console.

###### Note

You can't query data in Amazon Redshift Serverless using this original query editor. Use
Amazon Redshift query editor v2 instead.

In February 2021, an updated query editor was deployed and authorization permissions
to use the query editor changed. The new query editor uses the Amazon Redshift Data API to run
queries. The `AmazonRedshiftQueryEditor` policy, which is an AWS managed
AWS Identity and Access Management (IAM) policy, was updated to include the necessary permissions. If you have a
custom IAM policy, make sure that you update it. Use
`AmazonRedshiftQueryEditor` as a guide. The changes to
`AmazonRedshiftQueryEditor` include the following:

- Permission to manage query editor statement results requires the statement
  owner user.
- Permission to use Secrets Manager to connect to a database has been added.
  For more information, see [Permissions
  required to use the Amazon Redshift console query editor](redshift-iam-access-control-identity-based.md#redshift-policy-resources.required-permissions.query-editor "redshift-iam-access-control-identity-based.md#redshift-policy-resources.required-permissions.query-editor").

When you connect to your cluster from the new query editor, you can use one of two
authentication methods.

Using the query editor, you can do the following:

- Run single SQL statement queries.
- Download result sets as large as 100 MB to a comma-separated value (CSV)
  file.
- Save queries for reuse. You can't save queries in the Europe (Paris) Region, the
  Asia Pacific (Osaka) Region, the Asia Pacific (Hong Kong) Region, or the Middle East (Bahrain) Region.
- View query runtime details for user-defined tables.
- Schedule queries to run at a future time.
- View a history of queries that you created in the query editor.
- Run queries against clusters using enhanced VPC routing.

## Query editor considerations

Consider the following about working with queries when you use the query
editor:

- The maximum duration of a query is 24 hours.
- The maximum query result size is 100 MB. If a call returns more than 100
  MB of response data, the call is terminated.
- The maximum retention time for query results is 24 hours.
- The maximum query statement size is 100 KB.
- The cluster must be in a virtual private cloud (VPC) based on the Amazon VPC
  service.
- You can't use transactions in the query editor. For more information about
  transactions, see [BEGIN](../dg/r_BEGIN.md "../dg/r_BEGIN.md") in the
  _Amazon Redshift Database Developer Guide._
- You can save a query up to 3,000 characters long.
