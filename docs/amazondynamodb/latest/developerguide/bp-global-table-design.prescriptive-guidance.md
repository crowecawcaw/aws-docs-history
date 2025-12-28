# Throughput capacity planning for DynamoDB global tables

Migrating traffic from one Region to another requires careful consideration of DynamoDB table settings
regarding capacity.

Here are some considerations for managing write capacity:

- A global table must be in on-demand mode or provisioned with auto scaling enabled.
- If provisioned with auto scaling, the write settings (minimum, maximum, and target
  utilization) are replicated across Regions. Although the auto scaling settings are
  synchronized, the actual provisioned write capacity can float independently between
  Regions.
- One reason you could see different provisioned write capacity is due to the TTL feature. When
  you enable TTL in DynamoDB, you can specify an attribute name whose value indicates the time
  of expiration for the item, in Unix epoch time format in seconds. After that time, DynamoDB
  can delete the item without incurring write costs. With global tables, you can configure
  TTL in any Region, and the setting is automatically replicated to other Regions that are
  associated with the global table. When an item is eligible for deletion through a TTL
  rule, that work can be done in any Region. The delete operation is performed without
  consuming write units on the source table, but the replica tables will get a replicated
  write of that delete operation and will incur replicated write unit costs. TTL isn't
  supported in MRSC tables.
- If you’re using auto scaling, make sure that the maximum provisioned write capacity setting is
  sufficiently high to handle all write operations as well as all potential TTL delete operations.
  Auto scaling adjusts each Region according to its write consumption. On-demand tables have no
  maximum provisioned write capacity setting, but the _table-level maximum write throughput
  limit_ specifies the maximum sustained write capacity the on-demand table will allow. The
  default limit to 40,000, but it is adjustable. We recommend that you set it high enough to handle
  all write operations (including TTL write operations) that the on-demand table might need. This
  value must be the same across all participating Regions when you set up global tables.
  Here are some considerations for managing read capacity:

- Read capacity management settings are allowed to differ between Regions because it’s assumed
  that different Regions might have independent read patterns. When you first add a global
  replica to a table, the capacity of the source Region is propagated. After creation you can adjust
  the read capacity settings, which aren’t transferred to the other side.
- When you use DynamoDB auto scaling, make sure that the maximum provisioned read capacity
  settings are sufficiently high to handle all read operations across all Regions. During standard
  operations the read capacity will perhaps be spread across Regions, but during failover the table
  should be able to automatically adapt to the increased read workload. On-demand tables have
  no maximum provisioned read capacity setting, but the _table-level maximum read throughput
  limit_ specifies the maximum sustained read capacity the on-demand table will allow. The default
  limit is 40,000, but it is adjustable. We recommend that you set it high enough to handle all read
  operations that the table might need if all read operations were to route to this single Region.
- If a table in one Region doesn’t usually receive read traffic but might have to absorb a large
  amount of read traffic after a failover, you can pre-warm the capacity of the to accept a
  higher level of read traffic.
  ARC has [readiness checks](../../../r53recovery/latest/dg/recovery-readiness.md "../../../r53recovery/latest/dg/recovery-readiness.md") that can be useful for confirming that DynamoDB Regions have similar
  table settings and account quotas, whether or not you use Route 53 to route requests. These
  readiness checks can also help in adjusting account-level quotas to make sure they
  match.
