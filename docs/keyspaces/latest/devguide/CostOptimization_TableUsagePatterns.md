# Evaluate your table usage patterns to optimize performance and cost

This section provides an overview of how to evaluate if you are efficiently using your Amazon Keyspaces
tables. There are certain usage patterns which are not optimal for Amazon Keyspaces, and they allow
room for optimization from both a performance and a cost perspective.

###### Topics

- [Perform fewer
  strongly-consistent read operations](#CostOptimization_TableUsagePatterns_StronglyConsistentReads "#CostOptimization_TableUsagePatterns_StronglyConsistentReads")
- [Enable Time to Live (TTL)](#CostOptimization_TableUsagePatterns_TTL "#CostOptimization_TableUsagePatterns_TTL")

## Perform fewer

strongly-consistent read operations

Amazon Keyspaces allows you to configure [read consistency](consistency.md#ReadConsistency "consistency.md#ReadConsistency") on a
per-request basis. Read requests are eventually consistent by default. Eventually
consistent reads are charged at 0.5 RCU for up to 4 KB of data.

Most parts of distributed workloads are flexible and can tolerate eventual consistency.
However, there can be access patterns requiring strongly consistent reads. Strongly consistent
reads are charged at 1 RCU for up to 4 KB of data, essentially doubling your read costs. Amazon Keyspaces
provides you with the flexibility to use both consistency models on the same table.

You can evaluate your workload and application code to confirm if strongly consistent
reads are used only where required.

## Enable Time to Live (TTL)

[Time to Live (TTL)](TTL.md "TTL.md") helps you simplify your application logic
and optimize the price of storage by expiring data from tables automatically. Data that you
no longer need is automatically deleted from your table based on the Time to Live value
that you set.
