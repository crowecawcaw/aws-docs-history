# IVS Costs | Real-Time Streaming

See the [IVS Pricing page](https://aws.amazon.com/ivs/pricing/ "https://aws.amazon.com/ivs/pricing/") for details about costs for IVS.

- **Subscribing and publishing to stages** — Subscribing and publishing consume resources,
  and you will incur an hourly rate for the time you are connected to the stage.
- **Recording** — Individual participant recording incurs no additional Amazon IVS charges,
  while composite recording incurs charges for the hourly rate for the video encoded. Both recording options incur standard
  S3 storage and request costs. Thumbnails incur no additional IVS charges.
- **Participant replication**
  — Replica participants are billed the same as regular participants.

For example, suppose you have two stages, Stage A with Participant A and Stage B with Participant B.
You are charged for two participants.

If Participant A is replicated to Stage B, you now have three connected participants (Participant A,
Participant B, and the replica of Participant A). For the duration of the replication, you are charged for
three participants.
More information is on the IVS Pricing page.

## Cost Allocation Tags

You can assign tags to your Amazon IVS resources (such as stages) and use them as
cost allocation tags to organize and track your Amazon IVS real-time streaming costs.
A tag is a key-value pair that you define—for example, by application,
environment, team, or event. After you activate cost allocation tags, AWS includes
them in your cost allocation report so you can categorize and track your AWS spending
at a finer level of detail.

To use cost allocation tags with Amazon IVS:

1. Tag your Amazon IVS resources. You can add tags when you create a resource
   or add them later, using the Amazon IVS console, the AWS CLI, or the
   Amazon IVS API. For tag restrictions and naming requirements, see
   [Best
   practices and strategies](../../../tag-editor/latest/userguide/tagging.md#tag-best-practices-and-strategies "../../../tag-editor/latest/userguide/tagging.md#tag-best-practices-and-strategies") in
   _Tagging AWS Resources and Tag Editor_.
   For the Amazon IVS tagging operations (such as
   `TagResource`), see the
   [Amazon
   IVS Real-Time Streaming API Reference](../RealTimeAPIReference/API_TagResource.md "../RealTimeAPIReference/API_TagResource.md").
2. Activate your tags as cost allocation tags in the AWS Billing and Cost
   Management console. Only tags you have activated appear in your billing
   reports. See
   [Activating
   user-defined cost allocation tags](../../../awsaccountbilling/latest/aboutv2/activating-tags.md "../../../awsaccountbilling/latest/aboutv2/activating-tags.md"). After you apply tags to resources,
   it can take up to 24 hours for the tag keys to appear on the Cost allocation
   tags page, and up to another 24 hours for them to activate.
3. View your costs by tag using AWS Cost Explorer, AWS Cost and Usage
   Reports, or your monthly cost allocation report.

For more information, see
[Organizing
and tracking costs using AWS cost allocation tags](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md") in the
_AWS Billing User Guide_.
