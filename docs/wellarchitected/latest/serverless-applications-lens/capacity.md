# DynamoDB on-demand and provisioned capacity

Amazon DynamoDB is a fully managed NoSQL database service with single-digit millisecond
performance at any scale, and is often used for serverless applications. DynamoDB has two
pricing models for read and write throughput: on-demand mode and provisioned mode.

**On-demand mode**

DynamoDB on-demand mode is a serverless throughput option that simplifies database
management and automatically scales to support your most demanding applications. DynamoDB
on-demand lets you create a table without worrying about capacity planning, monitoring
usage, and configuring scaling policies. DynamoDB on-demand mode offers pay-per-request pricing
for read and write requests so that you only pay for what you use. For on-demand mode
tables, you don't need to specify how much read and write throughput you expect your
application to perform.

On-demand mode is the default and recommended throughput option for most DynamoDB
workloads. DynamoDB handles all aspects of throughput management and scaling to support
workloads that can start small and scale to millions of requests per second. You can read
and write to your DynamoDB tables as needed without managing throughput capacity on the table.
For more information, see [DynamoDB on-demand
capacity mode](../../../amazondynamodb/latest/developerguide/on-demand-capacity-mode.md "../../../amazondynamodb/latest/developerguide/on-demand-capacity-mode.md").

**Provisioned mode**

In provisioned mode, you must specify the number of reads and writes per second that you
require for your application. You'll be charged based on the hourly read and write capacity
you have provisioned, not how much of that provisioned capacity you actually consumed. This
helps you govern your DynamoDB use to stay at or below a defined request rate in order to
obtain cost predictability.

You can choose to use provisioned capacity if you have steady workloads with predictable
growth, and if you can reliably forecast capacity requirements for your application. For
more information, see [DynamoDB
provisioned capacity mode](../../../amazondynamodb/latest/developerguide/provisioned-capacity-mode.md "../../../amazondynamodb/latest/developerguide/provisioned-capacity-mode.md").
