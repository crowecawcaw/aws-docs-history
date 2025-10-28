# Online migration to Amazon Keyspaces: strategies and best practices

If you need to maintain application availability during a migration from Apache Cassandra to Amazon Keyspaces, you can prepare a
custom online migration strategy by implementing the key components discussed in this topic. By following these best
practices for online migrations, you can ensure that application availability and read-after-write consistency are maintained
during the entire migration process, minimizing the impact on your users.

When designing an online migration strategy from Apache Cassandra to Amazon Keyspaces, you need to consider the following key steps.

1. **Writing new data**
   - **ZDM Dual Write Proxy for Amazon Keyspaces Migration** – Use the ZDM Dual Write Proxy available on
     [Github](https://github.com/aws-samples/amazon-keyspaces-examples/blob/main/migration/online/zdm-proxy/README.md "https://github.com/aws-samples/amazon-keyspaces-examples/blob/main/migration/online/zdm-proxy/README.md")
     to perform zero-downtime migration from Apache Cassandra to Amazon Keyspaces. The ZDM Proxy performs dual writes without the need to
     refactor existing applications and performs dual reads for query validation.
   - Application dual-writes: You can implement dual writes in your application using existing Cassandra client libraries
     and drivers. Designate one database as the leader and the other as the follower. Write failures to the follower database are
     recorded in a
     [dead letter queue (DLQ)](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.md "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.md") for analysis.
   - Messaging tier dual-writes: Alternatively, you can configure your existing messaging platform to send writes to both
     Cassandra and Amazon Keyspaces using an additional consumer. This creates eventually consistent views across both databases.

2. **Migrating historical data**
   - Copy historical data: You can migrate historical data from Cassandra to Amazon Keyspaces using
     AWS Glue or custom extract, transform, and load (ETL) scripts. Handle conflict resolution between dual writes and bulk loads using techniques
     like lightweight transactions or timestamps.
   - Use Time-To-Live (TTL): For shorter data retention periods, you can use TTL in both Cassandra and Amazon Keyspaces
     to avoid uploading unnecessary historical data. As old data expires in Cassandra and new data is written via dual-writes,
     Amazon Keyspaces eventually catches up.

3. **Validating data**
   - Dual reads: Implement dual reads from both Cassandra (primary) and Amazon Keyspaces (secondary) databases,
     comparing results asynchronously. Differences are logged or sent to a DLQ.
   - Sample reads: Use Λ functions to periodically sample and compare data across both systems,
     logging any discrepancies to a DLQ.

4. **Migrating the application**
   - Blue-green strategy: Switch your application to treat Amazon Keyspaces as the primary and Cassandra as the secondary
     data store in a single step. Monitor performance and roll back if issues arise.
   - Canary deployment: Gradually roll out the migration to a subset of users first,
     incrementally increasing traffic to Amazon Keyspaces as the primary until fully migrated.

5. **Decommissioning Cassandra**

Once your application is fully migrated to Amazon Keyspaces and data consistency is validated, you can plan to decommission
your Cassandra cluster based on data retention policies.
By planning an online migration strategy with these components, you can transition smoothly to the fully managed Amazon Keyspaces service with
minimal downtime or disruption. The following sections go into each component in more detail.

###### Topics

- [Writing new data during an online migration](migration-online-dw.md "migration-online-dw.md")
- [Uploading historical data during an online migration](migration-online-historical.md "migration-online-historical.md")
- [Validating data consistency during an online migration](migration-online-validation.md "migration-online-validation.md")
- [Migrating the application during an online migration](migration-online-app-migration.md "migration-online-app-migration.md")
- [Decommissioning Cassandra after an online migration](migration-online-decommission.md "migration-online-decommission.md")
