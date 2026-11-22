

# Example of split cost allocation data for Amazon S3

The following example shows how split cost allocation data allocates a bucket's storage charge for one day to the prefixes in the bucket. The storage rate in this example is for illustrative purposes only. For current charges, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/).

For an explanation of Amazon S3 split cost allocation data, see [Understanding split cost allocation data](https://docs.aws.amazon.com/cur/latest/userguide/split-cost-allocation-data.html#split-cost-allocation-data-s3). For setup instructions, see [Enabling split cost allocation data](https://docs.aws.amazon.com/cur/latest/userguide/enabling-split-cost-allocation-data.html).

You have the following usage on one day of a 30-day month:
+ Bucket `amzn-s3-demo-bucket` in account 111111111111, in the US East (N. Virginia) Region, stores 1,200 GB in the S3 Standard storage class all day. That is 40 GB-Mo (1,200 GB × 24 hours ÷ 720 hours).
+ Its S3 Storage Lens dashboard publishes prefix levels 1 through 2.
+ Objects directly under `finance/`, such as `finance/budget.csv`, total 300 GB (10 GB-Mo).
+ Objects under `finance/billing/` total 600 GB (20 GB-Mo).
+ Objects under `marketing/` total 240 GB (8 GB-Mo).
+ Objects at the bucket root, such as `readme.txt`, total 60 GB (2 GB-Mo). They match no prefix, so their usage is unattributed.
+ In this example, assume the storage rate is USD $0.023 per GB-Mo.

## Step 1: Compute the allocated cost
<a name="example-split-cost-allocation-data-s3-step1"></a>

Each prefix's allocated cost is its usage multiplied by the storage rate.

`Allocated cost = Allocated usage × Storage rate`

The `finance/` prefix's allocated cost is 10 GB-Mo × USD $0.023 per GB-Mo = USD $0.230.

The `finance/billing/` prefix's allocated cost is 20 GB-Mo × USD $0.023 per GB-Mo = USD $0.460.

The `marketing/` prefix's allocated cost is 8 GB-Mo × USD $0.023 per GB-Mo = USD $0.184.

The remaining 2 GB-Mo costs USD $0.046.

The following table shows the usage and cost for the day, and the prefix tags on each line item:


**Usage and cost allocation for the day**  

| Prefix | `aws:s3:PrefixLevel1` | `aws:s3:PrefixLevel2` | Usage (GB-Mo) | Cost | 
| --- | --- | --- | --- | --- | 
| finance/ | finance | Not applicable | 10 | USD $0.230 | 
| finance/billing/ | finance | billing | 20 | USD $0.460 | 
| marketing/ | marketing | Not applicable | 8 | USD $0.184 | 
| Unattributed | (unattributed) | Not applicable | 2 | USD $0.046 | 
| Total | Not applicable | Not applicable | 40 | USD $0.920 | 

Each object is reported once, on the deepest published prefix that matches its key. Objects directly under `finance/` are on the `finance/` line item, and objects under `finance/billing/` are on the `finance/billing/` line item.

## Step 2: Reconcile the total cost
<a name="example-split-cost-allocation-data-s3-step2"></a>

The allocated usage is 10 GB-Mo \+ 20 GB-Mo \+ 8 GB-Mo = 38 GB-Mo, and the allocated cost is USD $0.230 \+ USD $0.460 \+ USD $0.184 = USD $0.874. Including the unattributed usage, the bucket's total storage charge for the day is USD $0.920:

```
Total cost = Allocated cost + Unattributed cost
           = USD $0.874 + USD $0.046
           = USD $0.920
```

The allocation provides a breakdown of the charge. It doesn't change the total charge or the account billed for the bucket.

To see cost for everything under a top-level prefix, group by the `aws:s3:PrefixLevel1` tag. In this example, `finance` is allocated USD $0.230 \+ USD $0.460 = USD $0.690 and `marketing` is allocated USD $0.184. Account 111111111111, which owns the bucket, still pays the full USD $0.920.

## Sample Cost and Usage Report
<a name="example-split-cost-allocation-data-s3-sample"></a>

All five line items for this day have the `lineItem/UsageAccountId` of the account billed for the bucket, 111111111111. The bucket's own line item is unchanged, and the four prefix line items are added.

The following table shows how the bucket's storage charge appears in some AWS CUR columns. Costs are in USD. *Prefix ARN* stands for the full ARN `arn:aws:s3:us-east-1:111111111111:prefix/amzn-s3-demo-bucket/` followed by the prefix path. For example, the `finance/billing/` prefix ARN is `arn:aws:s3:us-east-1:111111111111:prefix/amzn-s3-demo-bucket/finance/billing`. Not applicable means the column is empty on that line item.


**Selected bucket line items**  

| Line item | `lineItem/Operation` | `lineItem/ResourceId` | `lineItem/UnblendedCost` | `splitLineItem/SplitCost` | `splitLineItem/ParentResourceId` | 
| --- | --- | --- | --- | --- | --- | 
| Bucket | StandardStorage | amzn-s3-demo-bucket | 0.920 | Not applicable | Not applicable | 
| finance/ | S3Prefix | Prefix ARN | 0 | 0.230 | amzn-s3-demo-bucket | 
| finance/billing/ | S3Prefix | Prefix ARN | 0 | 0.460 | amzn-s3-demo-bucket | 
| marketing/ | S3Prefix | Prefix ARN | 0 | 0.184 | amzn-s3-demo-bucket | 
| Unattributed | S3Prefix | amzn-s3-demo-bucket | 0 | 0.046 | amzn-s3-demo-bucket | 

On the prefix line items, `lineItem/ResourceId` identifies the prefix and `splitLineItem/ParentResourceId` identifies the bucket whose charge is allocated. The `aws:s3:PrefixLevel1` and `aws:s3:PrefixLevel2` tags on those line items identify the prefix path. On the unattributed line item, `lineItem/ResourceId` is the bucket name and the `aws:s3:PrefixLevel1` tag is `(unattributed)`. Usage follows the same pattern as cost. `lineItem/UsageAmount` is 40 on the bucket's line item and 0 on the prefix and unattributed line items, whose `splitLineItem/SplitUsage` values are 10, 20, 8, and 2. To see the cost allocated to each prefix, use `splitLineItem/SplitCost`. The split costs add up to the USD $0.920 on the bucket's line item.