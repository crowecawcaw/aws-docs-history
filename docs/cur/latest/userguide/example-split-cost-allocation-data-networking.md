

# Example of split cost allocation data for networking

The following example shows how split cost allocation data allocates a NAT gateway's data processing charge to the Amazon EC2 instances that sent traffic through it. The data processing rate in this example is for illustrative purposes only. For current charges, see [Amazon VPC pricing](https://aws.amazon.com/vpc/pricing/).

For an explanation of networking split cost allocation data, see [Understanding split cost allocation data](https://docs.aws.amazon.com/cur/latest/userguide/split-cost-allocation-data.html#split-cost-allocation-data-networking). For setup instructions, see [Enabling split cost allocation data](https://docs.aws.amazon.com/cur/latest/userguide/enabling-split-cost-allocation-data.html).

You have the following usage in a single hour:
+ A NAT gateway in account 111111111111 processes 22 GB of data.
+ Its networking flexible cost allocation policy allocates data processing usage and cost to individual Amazon EC2 instances (`ec2` reporting granularity).
+ Instance 1 (`i-1234567890abcdef0`), owned by account 222222222222, sends 5 GB through the NAT gateway.
+ Instance 2 (`i-abcdef01234567890`), owned by account 333333333333, sends 15 GB through the NAT gateway.
+ The source of the remaining 2 GB can't be identified, so that usage is unattributed.
+ In this example, assume the data processing rate is USD $0.05 per GB.

## Step 1: Compute the allocated cost
<a name="example-networking-step1"></a>

Each instance's allocated cost is its usage multiplied by the data processing rate.

`Allocated cost = Allocated usage × Data processing rate`

Instance 1's allocated cost is 5 GB × USD $0.05 per GB = USD $0.25.

Instance 2's allocated cost is 15 GB × USD $0.05 per GB = USD $0.75.

The remaining 2 GB costs USD $0.10. The following table shows the usage and cost for the hour, and the account that owns each instance:


**Usage and cost allocation for the hour**  

| Resource that generated the usage | Account that owns the instance | Usage (GB) | Cost | 
| --- | --- | --- | --- | 
| Instance 1 | 222222222222 | 5 | USD $0.25 | 
| Instance 2 | 333333333333 | 15 | USD $0.75 | 
| Unattributed | Not applicable | 2 | USD $0.10 | 
| Total | Not applicable | 22 | USD $1.10 | 

## Step 2: Reconcile the total cost
<a name="example-networking-step2"></a>

The allocated usage is 5 GB \+ 15 GB = 20 GB, and the allocated cost is USD $0.25 \+ USD $0.75 = USD $1.00. Including the unattributed usage, the NAT gateway's total data processing charge is USD $1.10:

```
Total cost = Allocated cost + Unattributed cost
           = USD $1.00 + USD $0.10
           = USD $1.10
```

The allocation provides a breakdown of the charge. It doesn't change the total charge or the account billed for the usage.

To see cost by account, sum the allocated cost for each account that owns a resource. In this example, account 222222222222 is allocated USD $0.25 and account 333333333333 is allocated USD $0.75. Account 111111111111, which owns the NAT gateway, still pays the full USD $1.10.

## Sample Cost and Usage Report
<a name="example-networking-sample-cur"></a>

All four line items for this hour have the `lineItem/UsageAccountId` of the account billed for the NAT gateway, 111111111111. They appear in that account's report and in the management account's report. They don't appear in the reports of accounts 222222222222 and 333333333333.

The following table shows how the NAT gateway's data processing charge appears in some AWS CUR columns. Costs are in USD. *NAT gateway ARN* stands for the NAT gateway's full ARN, `arn:aws:ec2:us-east-1:111111111111:natgateway/nat-0123456789abcdef0`. Not applicable means the column is empty on that line item.


**Selected NAT gateway line items**  

| Line item | `lineItem/LineItemType` | `lineItem/ResourceId` | `lineItem/UnblendedCost` | `splitLineItem/SplitCost` | `splitLineItem/ParentResourceId` | 
| --- | --- | --- | --- | --- | --- | 
| NAT gateway | Usage | NAT gateway ARN | 1.10 | 0 | Not applicable | 
| Instance 1 | Usage | i-1234567890abcdef0 | 0 | 0.25 | NAT gateway ARN | 
| Instance 2 | Usage | i-abcdef01234567890 | 0 | 0.75 | NAT gateway ARN | 
| Unattributed | Usage | NAT gateway ARN | 0 | 0.10 | NAT gateway ARN | 

On the instance line items, `lineItem/ResourceId` identifies the instance and `splitLineItem/ParentResourceId` identifies the NAT gateway whose charge is allocated. The `aws:networking-fca:allocated-account` tag on those line items identifies the account that owns each instance: 222222222222 for Instance 1 and 333333333333 for Instance 2. On the unattributed line item, `lineItem/ResourceId` is the NAT gateway ARN and the `aws:networking-fca:allocated-account` tag is `(unattributed)`.

Usage follows the same pattern as cost. `lineItem/UsageAmount` is 22 on the NAT gateway's line item and 0 on the instance and unattributed line items, whose `splitLineItem/SplitUsage` values are 5, 15, and 2.

To see the cost allocated to each instance or account, use `splitLineItem/SplitCost`. The split costs add up to the USD $1.10 on the NAT gateway's line item. Adding them to the unblended cost total counts that cost twice.