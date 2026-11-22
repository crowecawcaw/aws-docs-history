

# Estimating Amazon S3 costs by prefix with S3 Storage Lens and AWS Cost and Usage Reports

You can use Amazon S3 Storage Lens to publish prefix-level metrics to AWS Billing and Cost Management, and use *split cost allocation data for Amazon S3* to view prefix-level storage and (Tier 1/2) request costs in the AWS Cost and Usage Report (CUR). With this data, you can attribute estimated Amazon S3 spending to the teams, applications, or tenants that share a general purpose bucket under different prefixes. In the Amazon S3 API, you configure this feature with the `CostAndUsageReportsPublish` member of a S3 Storage Lens configuration. For more information about AWS Cost and Usage Reports, see [What are AWS Cost and Usage Reports?](https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html) in the *AWS Data Exports User Guide*.

## How it works
<a name="storage-lens-cur-how-it-works"></a>

To allocate your Amazon S3 costs by prefix, you complete two steps:

1. **In S3 Storage Lens** – Enable AWS Billing and Cost Management publishing for an advanced tier dashboard configuration, and choose the range of prefix levels that you want costs reported for.

1. **In AWS Billing and Cost Management** – Enable split cost allocation data for Amazon S3. You can enable split cost allocation data only from the management account of your organization or from a standalone account. For more information, see [Split cost allocation data](https://docs.aws.amazon.com/cur/latest/userguide/split-cost-allocation-data.html) in the *AWS Data Exports User Guide*.

S3 Storage Lens doesn't calculate costs. It publishes prefix-level storage and (Tier 1/Tier 2) request metrics for your general purpose buckets to AWS Billing and Cost Management. If you enable split cost allocation data for Amazon S3 in a Cost and Usage Report, AWS Billing and Cost Management uses this data to calculate and report the estimated costs of your prefixes.

To view and query your prefix costs, use your Cost and Usage Report. For more information, see [Split cost allocation data](https://docs.aws.amazon.com/cur/latest/userguide/split-cost-allocation-data.html) in the *AWS Data Exports User Guide*.

## Prerequisites and considerations
<a name="storage-lens-cur-prerequisites"></a>

Before you enable AWS Billing and Cost Management publishing, review the following requirements and considerations:
+ **Prefix delimiter** – The `PrefixDelimiter` for the S3 Storage Lens configuration must be `/` (forward slash).
+ **Bucket type** – This feature supports general purpose buckets only. It doesn't support directory buckets, table buckets, or vector buckets.
+ **Permissions** – You don't need new IAM permissions to enable AWS Billing and Cost Management publishing in S3 Storage Lens. The existing S3 Storage Lens configuration permissions apply. For more information, see [Setting Amazon S3 Storage Lens permissions](storage_lens_iam_permissions.md). Enabling split cost allocation data in AWS Billing and Cost Management might require additional permissions, and you can enable it only from the management account of your organization or from a standalone account. For more information, see the [Split cost allocation data](https://docs.aws.amazon.com/cur/latest/userguide/split-cost-allocation-data.html) documentation in the *AWS Data Exports User Guide*.

**Note**  
AWS Billing and Cost Management publishing is available for dashboards that are upgraded to the S3 Storage Lens advanced tier. For S3 Storage Lens advanced tier pricing, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing) on the AWS website. No additional charges apply for AWS Billing and Cost Management publishing.

## Selecting prefix depth range
<a name="storage-lens-cur-prefix-depth"></a>

A *prefix level* is the depth of a prefix under a bucket. Prefix level 1 is the first prefix segment under the bucket name. Root objects directly under a bucket don't belong to any prefix. You choose the range of prefix levels for which costs are reported by setting a minimum depth (`MinDepth`) and a maximum depth (`MaxDepth`).

The following rules apply to `MinDepth` and `MaxDepth`:
+ Both values are integers from 1 through 15.
+ You must specify both values or neither. You can't specify only one. If you specify neither, the default values `MinDepth`=1 and `MaxDepth`=3 are used.
+ `MinDepth` must be less than or equal to `MaxDepth`.
+ `MaxDepth` minus `MinDepth` can't exceed 4. You can report costs for at most 5 adjacent prefix levels.

**Example – Prefix depth settings**  
Suppose that you store an object with the key `department/team/application/file.csv`, and you configure publishing for prefix levels 1 through 3. In your selected Cost and Usage Report, costs are reported for the following prefixes:
+ Level 1 – `department/`
+ Level 2 – `department/team/`
+ Level 3 – `department/team/application/`

To better understand how prefixes are reported in your Cost and Usage Report, see [Split cost allocation data](https://docs.aws.amazon.com/cur/latest/userguide/split-cost-allocation-data.html) in the *AWS Data Exports User Guide*.

## Prefix level costs included in the AWS Cost and Usage Reports
<a name="storage-lens-cur-costs-included"></a>

After enabling the feature on S3 Storage Lens dashboard configuration and AWS Billing and Cost Management console, your Cost and Usage Report will include the following estimated cost for each prefix:
+ Storage costs
+ Tier 1 and Tier 2 request costs

**Note**  
Your Cost and Usage Report doesn't include the following:  
Storage and request costs for [annotations](annotations-overview.md)
Request costs for [cross-Region replication](replication.md#crr-scenario)
All unattributed Amazon S3 costs and root-level object costs are captured at bucket level in unattributed cost category. Root-level objects are objects that don't belong to any prefix.

**Note**  
For buckets that have [Requester Pays](RequesterPaysBuckets.md) enabled, prefix-level request cost estimates include requests from all AWS accounts. This includes requests that are billed to the requester rather than the bucket owner.

## Limits
<a name="storage-lens-cur-data-availability"></a>

**Prefix limit** – S3 Storage Lens supports up to 10,000 prefixes per bucket at the configured depth. If a bucket exceeds the limit at a level, S3 Storage Lens falls back to the previous (shallower) level, down to the level at `MinDepth`. If the level at `MinDepth` already exceeds the limit, that bucket gets no prefix cost data.

Split cost allocation data in AWS Billing and Cost Management has its own limits. For more information, see [Split cost allocation data](https://docs.aws.amazon.com/cur/latest/userguide/split-cost-allocation-data.html) in the *AWS Data Exports User Guide*.