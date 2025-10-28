# Best practices for the lease table with

provisioned capacity mode

If the lease table of your KCL application was switched to provisioned
capacity mode, KCL 3.x creates a global secondary index on the lease table with
the provisioned billing mode and the same read capacity units (RCU) and write capacity
units (WCU) as the base lease table. When the global secondary index is created, we
recommend that you monitor the actual usage on the global secondary index in the
DynamoDB console and adjust the capacity units if needed. For a more detailed guide
about switching the capacity mode of DynamoDB metadata tables created by KCL,
see [DynamoDB capacity mode for metadata tables created
by KCL](kcl-dynamoDB.md#kcl-capacity-mode "kcl-dynamoDB.md#kcl-capacity-mode").

###### Note

By default, KCL creates metadata tables such as the lease table, worker
metrics table, and coordinator state table, and the global secondary index on the
lease table using the on-demand capacity mode. We recommend that you use the
on-demand capacity mode to automatically adjust the capacity based on your usage
changes.
