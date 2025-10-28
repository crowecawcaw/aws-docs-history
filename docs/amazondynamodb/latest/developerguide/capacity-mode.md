# DynamoDB throughput capacity

This section provides an overview of the two throughput modes available for your DynamoDB
table and considerations in selecting the appropriate capacity mode for your application. A
table’s throughput mode determines how the capacity of a table is managed. Throughput mode
also determines how you're charged for the read and write operations on your tables. In
Amazon DynamoDB, you can choose between **on-demand mode** and
**provisioned mode** for your tables to accommodate
different workload requirements.

###### Topics

- [On-demand mode](#capacity-mode-on-demand "#capacity-mode-on-demand")
- [Provisioned mode](#capacity-mode-provisioned "#capacity-mode-provisioned")
- [DynamoDB on-demand capacity mode](on-demand-capacity-mode.md "on-demand-capacity-mode.md")
- [DynamoDB provisioned capacity mode](provisioned-capacity-mode.md "provisioned-capacity-mode.md")
- [Understanding DynamoDB warm throughput](warm-throughput.md "warm-throughput.md")
- [DynamoDB burst and adaptive capacity](burst-adaptive-capacity.md "burst-adaptive-capacity.md")
- [Considerations when switching capacity modes in DynamoDB](bp-switching-capacity-modes.md "bp-switching-capacity-modes.md")

## On-demand mode

Amazon DynamoDB on-demand mode is a serverless throughput option that simplifies database
management and automatically scales to support customers' most demanding applications.
DynamoDB on-demand enables you to create a table without worrying about capacity planning,
monitoring usage, and configuring scaling policies. DynamoDB on-demand offers
pay-per-request pricing for read and write requests so that you only pay for what you
use. For on-demand mode tables, you don't need to specify how much read and write
throughput you expect your application to perform.

On-demand mode is the default and recommended throughput option for most DynamoDB
workloads. DynamoDB handles all aspects of throughput management and scaling to support
workloads that can start small and scale to millions of requests per second. You can
read and write to your DynamoDB tables as needed without managing throughput capacity on
the table. For more information, see [DynamoDB on-demand capacity mode](on-demand-capacity-mode.md "on-demand-capacity-mode.md").

## Provisioned mode

In provisioned mode, you must specify the number of reads and writes per second that
you require for your application. You'll be charged based on the hourly read and write
capacity you have provisioned, not how much of that provisioned capacity you actually
consumed. This helps you govern your DynamoDB use to stay at or below a defined request
rate in order to obtain cost predictability.

You can choose to use provisioned capacity if you have steady workloads with
predictable growth, and if you can reliably forecast capacity requirements for your
application. For more information, see [DynamoDB provisioned capacity mode](provisioned-capacity-mode.md "provisioned-capacity-mode.md").
