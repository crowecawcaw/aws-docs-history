# Testing the data migration

After all prerequisites are complete, you can validate migration setup using the
AWS Management Console, ElastiCache API, or AWS CLI. The following example shows using the CLI.

Test migration by calling the `test-migration` command with the following
parameters:

- `--replication-group-id` – The ID of the replication group
  to which data is to be migrated.
- `--customer-node-endpoint-list` – List of endpoints from
  which data should be migrated. List should have only one element.
  The following is an example using the CLI.

```
aws elasticache test-migration --replication-group-id test-cluster --customer-node-endpoint-list "Address='10.0.0.241',Port=6379"
```

ElastiCache will validate migration setup without any actual data migration.
