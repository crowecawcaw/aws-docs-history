# IVS Costs | Low-Latency Streaming

There are separate costs for Amazon IVS live video and Amazon S3 storage related to the
auto-record-to-S3 feature.

## Live Video

The [Amazon IVS pricing](https://aws.amazon.com/ivs/pricing/ "https://aws.amazon.com/ivs/pricing/") model
incorporates separate fees for video input and output.

Video-input fees depend on your channel type. For details about channel types, see
[Channel Types](streaming-config.md#streaming-config-settings-channel-types "streaming-config.md#streaming-config-settings-channel-types") in _IVS Streaming Configuration_.

For help selecting the right channel type for your use case, use the "Help me choose"
tool in the console:

1. On the console’s **Create channel** page, select
   **Custom configuration**.
2. Under **Channel type**, select **Help me choose**.
3. Follow the prompts until a recommendation is made, then choose **Select recommendation**.

For video output, you pay an hourly rate for video delivered to viewers. Rates vary by
resolution and "billing region" (where the video is delivered from). There are several
tiers of video-output costs based on usage, including a free tier.

A useful interactive tool is the [IVS Cost
Estimator](https://ivs.rocks/calculator "https://ivs.rocks/calculator"). You can plug in values for channel type, resolution, hours
streamed, number of viewers, and billing region. When estimating costs, note the
following rules of thumb:

- Viewers come and go, and on average, 50% of a stream is "delivered." The Cost
  Estimator includes a selector for "Average viewer watch duration." This defaults
  to 50%. Expect viewership for paid events to be higher; even in this case,
  though, it’s likely that not all ticket-holders will view at the same
  time.
- Some viewers watch at a lower resolution than the source resolution of the
  broadcast. This is especially true for high-resolution streams: some viewers
  will watch at lower resolutions, which are less expensive. This is due to
  various viewer constraints, including bandwidth, network conditions, ISP, and
  hardware.
- Timing matters. For instance, if your stream competes with school, work, or
  vacation, this can affect your audience size.
- It is very hard to build a live audience from non-live users. Of course, there
  are exceptions; bringing in external talent (like influencers with their own
  following) can increase audience size.

## Cost Allocation Tags

You can assign tags to your Amazon IVS resources (such as channels) and use them as
cost allocation tags to organize and track your Amazon IVS costs. A tag is a key-value
pair that you define—for example, by application, environment, team, or event.
After you activate cost allocation tags, AWS includes them in your cost allocation
report so you can categorize and track your AWS spending at a finer level of
detail.

To use cost allocation tags with Amazon IVS:

1. Tag your Amazon IVS resources. You can add tags when you create a resource or
   add them later, using the Amazon IVS console, the AWS CLI, or the Amazon IVS
   API. For tag restrictions and naming requirements, see [Best practices and strategies](../../../tag-editor/latest/userguide/tagging.md#tag-best-practices-and-strategies "../../../tag-editor/latest/userguide/tagging.md#tag-best-practices-and-strategies") in _Tagging
   AWS Resources and Tag Editor_. For the Amazon IVS tagging
   operations (such as `TagResource`), see the [Amazon IVS Low-Latency Streaming API Reference](../LowLatencyAPIReference/API_TagResource.md "../LowLatencyAPIReference/API_TagResource.md").
2. Activate your tags as cost allocation tags in the AWS Billing and Cost
   Management console. Only tags you have activated appear in your billing reports.
   See [Activating user-defined cost allocation tags](../../../awsaccountbilling/latest/aboutv2/activating-tags.md "../../../awsaccountbilling/latest/aboutv2/activating-tags.md"). After you apply tags
   to resources, it can take up to 24 hours for the tag keys to appear on the Cost
   allocation tags page, and up to another 24 hours for them to activate.
3. View your costs by tag using AWS Cost Explorer, AWS Cost and Usage
   Reports, or your monthly cost allocation report.

For more information, see [Organizing and tracking costs using AWS cost allocation tags](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md") in the
_AWS Billing User Guide_.

## Auto-Record to Amazon S3

There are no Amazon IVS charges for using the auto-record to Amazon S3 feature or for
writing to S3. There are charges for Amazon S3 storage, S3 API calls that Amazon IVS
makes on behalf of the customer, and serving the stored video to viewers.

### Storing Recorded Video

Customers can generate estimates of S3 storage needs and costs by using the IVS
console. When a customer uses the console to set up recording for a channel (either
when the channel is created or later), a data-use estimator is offered. These
data-use estimates can be plugged into the [AWS Pricing Calculator for
S3](https://calculator.aws/#/createCalculator/S3 "https://calculator.aws/#/createCalculator/S3") to estimate the monthly cost of S3 storage and data movement.

In the console, when creating a new channel or editing an existing channel, turn
on **Enable automatic recording** in the **Record and store streams** area. This displays information
about **Associated costs**.

![Select Auto-record to S3 in the Record and store streams area to display information about Associated costs.](images/Costs_Associated_Costs.png)

Select **Estimate data use** to display the data-use
calculator:

![Select Estimate data use to display the data-use calculator.](images/Costs_Estimate_Data_Use.png)

As noted on the screen, the estimates that are provided can be used with the
[AWS Pricing
Calculator](https://calculator.aws/#/createCalculator/S3 "https://calculator.aws/#/createCalculator/S3") to compute estimates of the monthly cost incurred by S3
storage and data movement.

### Serving Recorded Video

The cost of serving recorded video to viewers depends on the CDN that is used. For
example, see the Amazon CloudFront [pricing page](https://aws.amazon.com/cloudfront/pricing/ "https://aws.amazon.com/cloudfront/pricing/").

## Server Side Ad Insertion

If you use server-side ad insertion with IVS, ads are inserted using AWS
Elemental MediaTailor, which incurs separate charges for ad insertion and ad transcoding.

Each time you insert an ad break via IVS, you are billed for a MediaTailor ad insertion for each viewer of the channel.

To match the video quality of the ad content to the source content, MediaTailor transcodes ads into the following renditions:

| Resolution | Frame Rate | Bitrate                           |
| ---------- | ---------- | --------------------------------- |
| 1080p      | 30 fps     | 2.0<br>• 8.0 Mbps (13 renditions) |
| 720p       | 30 fps     | 1.7 Mbps                          |
| 480p       | 30 fps     | 800 Kbps                          |
| 360p       | 30 fps     | 400 kbps                          |
| 160p       | 30 fps     | 90 kbps                           |
| audio-only |            | 64 kbps                           |

IVS delivers ad content to viewers as part of the video stream. You will not incur MediaTailor ad delivery charges, as the delivery of ad content is included in IVS video output costs.

For more details, see the AWS Elemental MediaTailor [pricing page](https://aws.amazon.com/mediatailor/pricing/ "https://aws.amazon.com/mediatailor/pricing/").
