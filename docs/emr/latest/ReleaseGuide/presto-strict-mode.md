# Activating Presto strict mode

In certain situations, long-running queries can lead to high costs and cause Amazon EMR to
use more cluster resources. This takes resources away from other workloads on the
cluster. With Amazon EMR versions 6.8 and later, you can use a strict mode feature that
rejects or warns you about the following types of long-running queries:

- Queries without predicates on the partitioned columns that result in table
  scans of large amounts of data
- Queries with cross joins between two large tables
- Queries that sort large number of rows without limit
  After Presto completely optimizes the query plan, strict mode runs. To use and
  customize strict mode to your query needs, you can configure Presto in the following
  ways.

| Presto configurations for strict mode | Setting                                                                                                                                                                                            | Description                                                        | Default |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ------- |
| `strict-mode-enabled`                 | Turns strict mode on and off. A value of `true` indicates<br>that strict mode is on.                                                                                                               | `false`                                                            |
| `strict-mode-fail-query`              | Rejects queries if strict mode detects probable long-running queries.<br>If `false`, Amazon EMR only raises a warning.                                                                             | `false`                                                            |
| `strict-mode-restrictions`            | Specifies the restrictions to apply when strict mode is turned on.<br>Strict mode supports the following restrictions:<br>MANDATORY_PARTITION_PREDICATE, DISALLOW_CROSS_JOIN, and<br>LIMITED_SORT. | MANDATORY_PARTITION_PREDICATE,DISALLOW_CROSS_JOIN,<br>LIMITED_SORT |

To experiment with strict mode, you can override these configurations, or set them as
session properties when you use the Presto client.

###### To set the configuration at cluster creation with the AWS Management Console

1. Choose **Create cluster** and select Amazon EMR version 6.8.0, and
   Presto or Trino. For more information, see [Installing PrestoDB and Trino](emr-presto-considerations.md#emr-prestodb-prestosql "emr-presto-considerations.md#emr-prestodb-prestosql").
2. Specify the configuration properties for strict mode directly, or upload a
   JSON file to Amazon S3. Optionally, select the AWS Glue data catalog for your
   metastore. Specify your VPC, subnets, bootstrap actions, key pair, and security
   group. Choose **Create cluster** to create your cluster.
3. Log in to the primary node of the cluster and run `presto-cli` or
   `trino-cli`.
4. Submit your queries. Strict mode validates each query and determines if it is
   long-running. Depending on your `strict-mode-fail-query` setting,
   Amazon EMR rejects the query or raises a warning.
5. When you're finished with your queries, terminate the cluster and delete your
   resources.

###### To set the configuration on a running cluster with the AWS CLI

1. Log in to the primary node of your cluster with the AWS CLI and run
   `presto-cli` or `trino-cli`.
2. Run the following commands with your desired values.

```
set session strict_mode_enabled = true;
set session strict_mode_fail_query = false;
set session strict_mode_restrictions = 'DISALLOW_CROSS_JOIN,LIMITED_SORT';
```

## Considerations

When you use strict mode, consider the following:

- In some cases, strict mode can reject short-running queries that don’t
  consume a lot of resources. For example, queries on small tables don’t apply
  dynamic filtering or replace inner joins with cross joins. This can lead the
  query to use the mandatory partition predicate or disallow cross join. When
  this happens, strict mode rejects the query.
- The strict mode check is only applied on SELECT, INSERT, CREATE TABLE AS
  SELECT, and EXPLAIN ANALYZE query types.
- You can only use the restriction on the mandatory partition predicate with
  the Hive connector.
