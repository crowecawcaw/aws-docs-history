# DynamoDB reserved capacity

For provisioned capacity tables that use the Standard [table class](HowItWorks.md "HowItWorks.md"), DynamoDB offers the ability
to purchase reserved capacity for your read and write capacity. A reserved capacity
purchase is an agreement to pay for a minimum amount of provisioned throughput
capacity, for the duration of the term of the agreement, in exchange for discounted
pricing.

###### Note

You can't purchase reserved capacity for replicated write capacity units
(rWCUs). Reserved capacity is applied only to the Region in which it was
purchased. Reserved capacity is also not available for tables using the DynamoDB
Standard-IA table class or on-demand capacity mode.

Reserved capacity is purchased in allocations of 100 WCUs or 100 RCUs. The
smallest reserved capacity offering is 100 capacity units (reads or writes). DynamoDB
reserved capacity is offered as either a one-year commitment or in select Regions as
a three-year commitment. You can save up to 54% off standard rates for a one-year
term and 77% off standard rates for a three-year term. For more information about
how and when you should purchase, see [Amazon DynamoDB Reserved Capacity](https://aws.amazon.com/dynamodb/reserved-capacity/ "https://aws.amazon.com/dynamodb/reserved-capacity/").

When you purchase DynamoDB reserved capacity, you pay a one-time partial upfront
payment and receive a discounted hourly rate for the committed provisioned usage.
You pay for the entire committed provisioned usage, regardless of actual usage, so
your cost savings are closely tied to use. Any capacity that you provision in excess
of the purchased reserved capacity is billed at standard provisioned capacity rates.
By reserving your read and write capacity units ahead of time, you realize
significant cost savings on your provisioned capacity costs.

You can't sell, cancel, or transfer reserved capacity to another Region or
account.
