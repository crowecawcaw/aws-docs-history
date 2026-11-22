

# Online migration to ElastiCache Serverless

Amazon ElastiCache Serverless for Valkey supports migration from self-managed Valkey and Redis OSS on Amazon EC2 with zero downtime. *Zero downtime* means no errors returned to the client during migration, measured the same way the [ElastiCache SLA](https://aws.amazon.com/elasticache/sla/) measures availability. Your application continues reading and writing through cutover.

This section covers migration to an ElastiCache Serverless cache. To migrate to a node-based cluster instead, see [Online migration to ElastiCache node-based clusters](OnlineMigration.md).

Online migration moves your self-managed Valkey or Redis OSS data into ElastiCache Serverless for Valkey while your application keeps serving traffic. You do not need a third-party replication tool or a maintenance window to switch over.

Migration usage is free for the first 180 days per AWS account, starting when the account first prepares a migration. Your target ElastiCache Serverless cache bills at the standard rates during the migration. For more information, see [Amazon ElastiCache pricing](https://aws.amazon.com/elasticache/pricing/) on the AWS website.

During a migration, you point your application at the migration endpoint. The migration endpoint is your serverless cache's standard endpoint, so your application keeps using it after cutover. ElastiCache routes your application's requests to your source cache while it replicates your data to the target cache. When you complete the cutover, ElastiCache switches over at the next fully synced window, and your application is then served by ElastiCache Serverless.

The following topics describe the requirements, source authentication, the console and AWS CLI instructions, and cutover modes for online migration.

**Topics**
+ [Migration steps](#migration-to-serverless-how-it-works)
+ [What ElastiCache manages and what you manage](#migration-to-serverless-responsibilities)
+ [Prerequisites and limitations](migration-to-serverless-prerequisites.md)
+ [Source authentication](migration-to-serverless-auth.md)
+ [Migrate your data](migration-to-serverless-procedure.md)
+ [Monitor the migration](migration-to-serverless-monitoring.md)
+ [Canceling and troubleshooting](migration-to-serverless-troubleshooting.md)

## Migration steps
<a name="migration-to-serverless-how-it-works"></a>

A migration has three steps, each with its own API operation: prepare the migration, start the data sync, and complete the cutover. ElastiCache publishes an event at every transition.

1. **Prepare the migration** – ElastiCache validates your source cache and your target cache against the migration requirements. It provisions the infrastructure that reads from your source and returns the migration endpoint. You then point your application at the migration endpoint and confirm that it is serving traffic through the endpoint. The console reminds you to do this before you start the data sync, because ElastiCache cannot detect whether your application has moved. For more information, see [Prerequisites and limitations for online migration to ElastiCache Serverless](migration-to-serverless-prerequisites.md) and [Redirecting your application](migration-to-serverless-procedure.md#migration-to-serverless-redirect).

1. **Start the data sync** – ElastiCache begins replicating data from your source cache to the target cache. It keeps replicating as your application writes. You can stop the data sync while it is in progress. Your application continues to be served by your source cache. For more information, see [Starting the data sync](migration-to-serverless-procedure.md#migration-to-serverless-start).

1. **Complete the cutover** – ElastiCache switches your migration endpoint over to serve from the target cache at the next fully synced window. You choose whether to trigger this yourself or have ElastiCache do it for you. For more information, see [Cutting over](migration-to-serverless-procedure.md#migration-to-serverless-complete).

For the console and AWS CLI steps, see [Migrating your data to ElastiCache Serverless](migration-to-serverless-procedure.md).

## What ElastiCache manages and what you manage
<a name="migration-to-serverless-responsibilities"></a>

A migration spans your infrastructure and ours.


| ElastiCache manages | You manage | 
| --- | --- | 
| The migration endpoint that your application connects to. | Your source cache, including its capacity, its engine version, and its availability. ElastiCache reads from your source but does not operate it. | 
| The infrastructure that reads from your source cache and replicates to your target during the migration. | The source requirements on this page, including replication support, the memory limit per node, the engine version range, and network reachability. | 
| The target ElastiCache Serverless cache. | Your client configuration, including retry behavior, connection pooling, and not caching node IP addresses. | 

A failed request can originate on either side. If you see errors during a migration, check your source cache health and capacity first. A source that is unavailable or out of memory surfaces as errors through the migration endpoint.

The ElastiCache Service Level Agreement applies to your ElastiCache Serverless cache during a migration on the same terms as at any other time.