

# Billing
<a name="aurora-faq-billing"></a>

**Topics**
+ [How much does Amazon Aurora cost?](#aurora-faq-how-much-does-amazon-aurora-cost)
+ [Is there a free tier for Amazon Aurora?](#aurora-faq-is-there-a-free-tier-for-amazon-aurora)
+ [Can I save money with a Database Savings Plan?](#aurora-faq-can-i-save-money-with-a-database-savings-plan)
+ [Is there a charge for Aurora replication?](#aurora-faq-is-there-a-charge-for-aurora-replication)
+ [What are I/O operations in Aurora and how are they calculated?](#aurora-faq-what-are-io-operations-in-aurora-and-how-are-they-calculated)
+ [What is the difference between Aurora Standard and Aurora I/O-Optimized?](#aurora-faq-what-is-the-difference-between-aurora-standard-and-aurora-io)
+ [When should I choose Aurora I/O-Optimized?](#aurora-faq-when-should-i-choose-aurora-io-optimized)
+ [How do I switch to Aurora I/O-Optimized?](#aurora-faq-how-do-i-switch-to-aurora-io-optimized)
+ [Does Aurora I/O-Optimized work with Reserved Instances?](#aurora-faq-does-aurora-io-optimized-work-with-reserved-instances)
+ [Are there changes to backup or snapshot pricing with I/O-Optimized?](#aurora-faq-are-there-changes-to-backup-or-snapshot-pricing-with-io-opti)
+ [Do cross-Region replication I/O charges still apply with I/O-Optimized?](#aurora-faq-do-cross-region-replication-io-charges-still-apply-with-io-o)
+ [Are there additional charges for optimized reads for Aurora PostgreSQL?](#aurora-faq-are-there-additional-charges-for-optimized-reads-for-aurora-)

## How much does Amazon Aurora cost?
<a name="aurora-faq-how-much-does-amazon-aurora-cost"></a>

See the [Aurora pricing page](https://aws.amazon.com/rds/aurora/pricing/) for current pricing information. Aurora offers two cluster configurations — Aurora Standard and Aurora I/O-Optimized — so you can optimize costs based on your workload.

## Is there a free tier for Amazon Aurora?
<a name="aurora-faq-is-there-a-free-tier-for-amazon-aurora"></a>

Yes. Amazon Aurora is available with the [AWS Free Tier](https://aws.amazon.com/free/) for Aurora PostgreSQL serverless and Aurora DSQL. New customers will receive up to $100 in credits at sign-up and can earn up to an additional $100 in credits, totaling $200, to explore eligible AWS services, including Aurora, on both Free and Paid plans. In addition, the [Aurora free tier](https://aws.amazon.com/rds/free/) offers the following benefits:

Aurora PostgreSQL provides 4 ACUs and 1 GiB of storage per cluster on the Free plan.

Aurora DSQL provides the first 100k DPUs and 1 GiB of storage every month on the Free and Paid plans.

Check the [Aurora pricing page](https://aws.amazon.com/rds/aurora/pricing/) for current Free Tier details and eligibility.

## Can I save money with a Database Savings Plan?
<a name="aurora-faq-can-i-save-money-with-a-database-savings-plan"></a>

Yes, you can purchase a [Database Savings Plan](https://aws.amazon.com/savingsplans/database-pricing/) for your Aurora usage and reduce costs by up to 35% when you commit to a consistent amount of usage over a 1-year term.

## Is there a charge for Aurora replication?
<a name="aurora-faq-is-there-a-charge-for-aurora-replication"></a>

No, Aurora replication is bundled into the price. You are charged based on the storage your database consumes at the database layer, not the storage consumed in the virtualized storage layer.

## What are I/O operations in Aurora and how are they calculated?
<a name="aurora-faq-what-are-io-operations-in-aurora-and-how-are-they-calculated"></a>

I/O operations are performed by the Aurora database engine against its SSD-based virtualized storage layer. Every database page read operation counts as one I/O.

Key details about I/O billing:
+ Read I/Os: If your query traffic can be served entirely from memory or cache, you will not be charged for data page retrieval. Pages not in memory incur read I/O charges (16 KB per page in Aurora MySQL, 8 KB in Aurora PostgreSQL).
+ Write I/Os: Counted in 4 KB units. Only redo log records (Aurora MySQL) or write-ahead log records (Aurora PostgreSQL) are written — Aurora never flushes dirty data pages to storage.
+ Monitoring: Check "VolumeReadIOPs" and "VolumeWriteIOPs" metrics in the Amazon RDS console.

With Aurora Standard, you pay per-request for I/O. With Aurora I/O-Optimized, read and write I/O operations are included at no additional charge.

## What is the difference between Aurora Standard and Aurora I/O-Optimized?
<a name="aurora-faq-what-is-the-difference-between-aurora-standard-and-aurora-io"></a>

Aurora offers two configurations to optimize your database spend: Aurora Standard and Aurora I/O-Optimized.

You can switch between configurations using the Amazon RDS console, AWS CLI, or AWS SDK. You can switch to I/O-Optimized once every 30 days, and switch back to Standard at any time. Aurora I/O-Optimized works with existing Aurora Reserved Instances.

## When should I choose Aurora I/O-Optimized?
<a name="aurora-faq-when-should-i-choose-aurora-io-optimized"></a>

Aurora I/O-Optimized is the ideal choice when you need predictable costs for any application. It delivers improved price performance for I/O-intensive applications that require high write throughput or run analytical queries processing large amounts of data. For customers with an I/O spend exceeding 25% of their Aurora bill, you can save up to 40% on costs.

## How do I switch to Aurora I/O-Optimized?
<a name="aurora-faq-how-do-i-switch-to-aurora-io-optimized"></a>

You can use the one-click experience in the [Amazon RDS console](https://console.aws.amazon.com/rds/) to change the storage type of your existing database clusters. You can also use the AWS CLI or AWS SDK. You can switch to I/O-Optimized once every 30 days and switch back to Standard at any time.

## Does Aurora I/O-Optimized work with Reserved Instances?
<a name="aurora-faq-does-aurora-io-optimized-work-with-reserved-instances"></a>

Yes, Aurora I/O-Optimized works with existing Aurora Reserved Instances. Aurora automatically accounts for the price difference between Aurora Standard and Aurora I/O-Optimized with Reserved Instances, providing even more savings on your I/O spend.

## Are there changes to backup or snapshot pricing with I/O-Optimized?
<a name="aurora-faq-are-there-changes-to-backup-or-snapshot-pricing-with-io-opti"></a>

No. There are no changes to the price of backtrack, snapshot, export, or continuous backup with Aurora I/O-Optimized.

## Do cross-Region replication I/O charges still apply with I/O-Optimized?
<a name="aurora-faq-do-cross-region-replication-io-charges-still-apply-with-io-o"></a>

Yes. The charges for I/O operations required to replicate data across Regions continue to apply. Aurora I/O-Optimized does not charge for read and write I/O operations, which is different from data replication.

## Are there additional charges for optimized reads for Aurora PostgreSQL?
<a name="aurora-faq-are-there-additional-charges-for-optimized-reads-for-aurora-"></a>

No. There are no additional charges for optimized reads beyond the price of Intel-based R6id and Graviton-based R6gd and R8gd instances. For more information, visit the [Aurora pricing page](https://aws.amazon.com/rds/aurora/pricing/).