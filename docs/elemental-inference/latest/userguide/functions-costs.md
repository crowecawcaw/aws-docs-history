

# Costs and throughput
<a name="functions-costs"></a>

A function that invokes a model calls Amazon Bedrock in your account, with your credentials. That means:
+ The model charges appear on your own Amazon Bedrock bill. AWS CloudTrail in your account records each call under the feed's access role, in a role session named `ei-function-{{feed-id}}`.
+ Elemental Inference invokes the model in the feed's Region. The invocations count against your account's Amazon Bedrock quotas for that model in that Region. To use a model in other Regions, specify a cross-Region inference profile ID as the function's model.
+ Your account must be able to invoke the model in that Region before the function can run. Elemental Inference doesn't enable model access on your behalf.

**Important**  
On-demand Amazon Bedrock throughput is shared across everything in your account that uses that model. A function on a live feed fires continuously for as long as the channel runs, which is the workload that exhausts an on-demand quota and starts throttling your other applications. For a production feed, use provisioned throughput for the model, or a cross-Region inference profile, and size it for the cadence you configured. For more information, see [Increase throughput with provisioned throughput](https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html) in the *Amazon Bedrock User Guide*.

A passthrough function invokes no model, so it incurs no model charges and consumes no Amazon Bedrock quota.

For Elemental Inference pricing, see [Pricing for AWS Elemental Inference](pricing-for-inference.md).