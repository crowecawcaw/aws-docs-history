

# Understand Networking Flexible Cost Allocation in your Cost and Usage Reports

After you associate a policy with a resource and turn on the data, Cost and Usage Reports that include split cost allocation data break down the shared resource's usage. The report keeps a summary line item for the shared resource and adds an allocated line item for each resource that generated usage, in the same split cost allocation columns that Amazon ECS and Amazon EKS use. Reports that don't include split cost allocation data are unchanged. The breakdown doesn't change your total charges or the account billed for the usage.

The *AWS Data Exports User Guide* documents the split cost allocation columns, the networking cost allocation tags, and how the line items are structured:
+ [Split cost allocation data for networking](https://docs.aws.amazon.com/cur/latest/userguide/split-cost-allocation-data.html#split-cost-allocation-data-networking) – How allocated usage, cost, and tags appear in your report.
+ [Example of split cost allocation data for networking](https://docs.aws.amazon.com/cur/latest/userguide/example-split-cost-allocation-data-networking.html) – A worked example that allocates a NAT gateway's data processing charge to the instances that sent traffic through it.

To turn on the data in your reports, see [Turning on the data in your Cost and Usage Reports](networking-flex-cost-allocation-work-with.md#networking-flex-cost-allocation-turn-on).