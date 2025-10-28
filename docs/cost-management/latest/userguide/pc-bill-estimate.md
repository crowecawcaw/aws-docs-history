# Bill estimates

Bill estimates allow you to estimate pre-tax costs of your usage and commitments across your
consolidated bill family. The bill estimate automatically includes your consolidated usage from
the previous month. For example, if you add 100 instance-hours for a specific EC2 instance type
in a given AWS Region, those hours will be added on top of your existing usage for that instance
type in that Region with no extra input needed. It also includes your existing commitments like
Savings Plans and Reserved Instances. Your benefit sharing preferences are applied, and any applicable
discounts, credits, or refunds are included just as they were on your most recent anniversary bill.
You can model new usage changes as well as add new commitments and modify your existing commitments.

To generate a bill estimate you must create a bill scenario. Bill scenario allows you to
model commitments in addition to usage. After you complete modeling usage and commitments in a
scenario, you can run a bill estimate.

###### Note

- Depending on the size of your workloads, generating a bill estimate can take between 20 minutes to 12 hours.
- Bill estimates are only available to management accounts and standalone AWS accounts.

###### Topics

- [Understanding the data entities used in bill estimates](#pc-bill-estimate-entities "#pc-bill-estimate-entities")
- [Creating a bill scenario](pc-create-bill-scenario.md "pc-create-bill-scenario.md")
- [Adding historical usage to your bill scenario](pc-create-bill-scenario-historical-usage.md "pc-create-bill-scenario-historical-usage.md")
- [Adding new services to my bill scenario](pc-create-bill-scenario-new-service.md "pc-create-bill-scenario-new-service.md")
- [Adding previously saved estimates to my bill scenario](pc-create-bill-scenario-previous-url.md "pc-create-bill-scenario-previous-url.md")
- [Adding Savings Plans to my bill scenario](pc-create-bill-scenario-sp.md "pc-create-bill-scenario-sp.md")
- [Adding Reserved Instances to my bill scenario](pc-create-bill-scenario-ri.md "pc-create-bill-scenario-ri.md")
- [Stale and expired bill scenarios](pc-scenario-stale.md "pc-scenario-stale.md")
- [Creating a bill estimate](pc-create-bill-estimate.md "pc-create-bill-estimate.md")
- [Viewing your Bill estimate](pc-view-bill-estimate.md "pc-view-bill-estimate.md")

## Understanding the data entities used in bill estimates

The bill estimates generation engine of AWS Pricing Calculator uses the following data entities from the specified timeframe.

| Data entity                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Member accounts                | The selection of member accounts are used to identify how usage was incurred by each member account during the last anniversary bill month and we layer your modeled usage on top of it.                                                                                                                                                                                                                                                                                       |
| Product and pricing attributes | The product and pricing attributes governs pricing. For example, a t4g.large EC2 shared tenancy instance running Linux in us-east-1 for 500 hrs for the month. A t4.large EC2 instance has 2 vCPUs, 8 GiB memory. Shared tenancy, number of vCPUs, allocated memory are the product attributes that determine the pricing for each unit of usage for this EC2 instance. We use the attributes and its pricing as of what was available during the last anniversary bill month. |
| Existing usage                 | Existing usage indicates the unchanged usage level from your last anniversary bill month upon which any of your modeled usage from a bill scenario is layered.                                                                                                                                                                                                                                                                                                                 |
| Savings Plans inventory        | This inventory indicates active Savings Plans as of the last anniversary bill month. This inventory is automatically included in your bill estimates and any new Savings Plans you model is layered on this inventory that applies to Savings Plans eligible usage.                                                                                                                                                                                                            |
| Reserved Instances inventory   | This inventory indicates active Reserved Instances as of the last anniversary bill month. This inventory is automatically included in your bill estimates and any new Reserved Instances you model is layered on this inventory that applies to Reserved Instances eligible usage.                                                                                                                                                                                             |
| Benefits sharing preference    | The accounts based on your **Reserved Instances and Savings Plans discount sharing preference** billing preference gets automatic Reserved Instances and Savings Plans discount benefits. We consider this benefit application setting as of the last anniversary bill to apply automatic benefit sharing when estimating your bill.                                                                                                                                           |
