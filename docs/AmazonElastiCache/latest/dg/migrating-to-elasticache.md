

# Migrating to ElastiCache
<a name="migrating-to-elasticache"></a>

With online migration, you point ElastiCache at your running self-managed source, and ElastiCache replicates your data into a target cache while your source keeps serving.

Online migration does not move data between two ElastiCache caches.

Choose your path by target. If your target is an ElastiCache Serverless cache, use the serverless path. If your target is a node-based ElastiCache cluster that you size and manage yourself, use the node-based path.

Both paths require a self-managed source that runs on Amazon EC2.

**Topics**
+ [Online migration to ElastiCache Serverless](migration-to-serverless.md)
+ [Online migration to ElastiCache node-based clusters](OnlineMigration.md)