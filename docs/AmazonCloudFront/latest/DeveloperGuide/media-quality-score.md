# Media quality-aware resiliency

Media quality-aware resiliency (MQAR) is an integrated capability between [Amazon CloudFront](https://aws.amazon.com/cloudfront/ "https://aws.amazon.com/cloudfront/") and [AWS Media Services](https://aws.amazon.com/media-services/ "https://aws.amazon.com/media-services/"). MQAR provides automated cross-Region
origin selection based on Media Quality Confidence Score (MQCS). MQCS is synthesized by
AWS Elemental MediaLive based on parameters that affect media quality experience perceived by viewers.
You can configure CloudFront and AWS Media Services to deliver your live event streaming
with high resiliency by using multiple options that you can specify in the CloudFront origin
group failover criteria.

When you enable the MQAR feature for your distribution, you authorize CloudFront to
automatically select the origin that is deemed to have the highest quality score.

The quality score represents perceived media streaming quality issues from your
origins, such as black frames, frozen or dropped frames, or repeated frames. For
example, if your AWS Elemental MediaPackage v2 origins are deployed in two different AWS Regions, and
one reports a higher media quality score than the other, CloudFront will automatically switch
to the origin that reports the higher score.

To achieve this, CloudFront does the following:

1. CloudFront forwards a `GET` request to the primary MediaPackage origin, and also
   initiates a `HEAD` request to the secondary MediaPackage origin at the same
   time. CloudFront receives the media quality score in the response headers from each
   origin.
2. Next, CloudFront tracks the score for each origin and uses this information to
   determine the origin with the higher score when a new request arrives.
   The media quality score for your origins can change in real time. CloudFront determines this
   by consuming the MQCS changes, and switches between origins to ensure that viewers see
   the higher media quality content. For more information, see [Leveraging media quality scores with
   MediaPackage](../../../mediapackage/latest/userguide/mqcs.md "../../../mediapackage/latest/userguide/mqcs.md") in the _AWS Elemental MediaPackage V2 User Guide_.

MQAR helps CloudFront determine, as early as possible, whether there’s an issue that could
potentially impact customers. For example, issues such as network connection, video
processing, audio loss or drops, encoder speed problems can affect the media quality
score for your viewers.

MQAR provides seamless switching between origins, so that you can deploy a resilient,
cross-Region end-to-end media delivery workflow on AWS, and provide quality content
for your viewers.

###### Note

Currently, this feature only supports MediaPackage v2 origins.

To enable this feature for your distribution, complete the following steps:

1. If you haven't already, create your MediaPackage v2 origins and enable this feature
   in your endpoint configuration. For a cross-region deployment, create a
   secondary channel in a different AWS Region with the same settings. For more
   information, see the following topics in the see the _AWS Elemental MediaPackage V2 User
   Guide_:
   - [Create a channel and endpoint](../../../mediapackage/latest/userguide/getting-started.md "../../../mediapackage/latest/userguide/getting-started.md")
   - [Enable the media
     quality score](../../../mediapackage/latest/userguide/mqcs.md "../../../mediapackage/latest/userguide/mqcs.md")

2. To use your MediaPackage v2 origins for CloudFront, create or update a CloudFront distribution.
   See [Create a distribution](distribution-web-creating-console.md "distribution-web-creating-console.md") and [Update a distribution](HowToUpdateDistribution.md "HowToUpdateDistribution.md").
3. Create an origin group, and select your two origins as the primary and
   secondary. In your origin group, enable the **Media quality
   score** option. For more information, see [Create an origin group](high_availability_origin_failover.md#concept_origin_groups.creating "high_availability_origin_failover.md#concept_origin_groups.creating").
4. In your cache behavior for your distribution, select the [origin group](DownloadDistValuesCacheBehavior.md#DownloadDistValuesTargetOriginId "DownloadDistValuesCacheBehavior.md#DownloadDistValuesTargetOriginId") that you
   created. We recommend that the cache behavior match the channel path
   pattern.
   If CloudFront determines that both MediaPackage v2 origins have the same score, then it forwards
   the request to the primary origin as listed in the origin group. If the initially
   selected origin responds with an error code matching the failover criteria you specified
   in your origin group, then CloudFront retries the request to the alternative origin in your
   origin group regardless of its media quality score.

###### Notes

- CloudFront tracks the quality score for each cache behavior that utilizes an
  origin group enabled for media quality score. If the same origin group is
  used for multiple channels that emit a media quality score, create a
  separate cache behavior for each channel's path pattern to avoid mixing
  their scores. For more information about origin group quotas, see [General quotas on distributions](cloudfront-limits.md#limits-web-distributions "cloudfront-limits.md#limits-web-distributions").
- Currently, MQAR isn't available when you use a [Lambda@Edge](lambda-at-the-edge.md "lambda-at-the-edge.md") function in
  origin-facing triggers (origin request and origin response) that is
  associated with your distribution's cache behavior. For more information,
  see [Cache behavior
  settings](DownloadDistValuesCacheBehavior.md "DownloadDistValuesCacheBehavior.md").
- If you enabled the MQAR feature and origin access control (OAC), add the `mediapackagev2:GetHeadObject` action to the IAM policy. MQAR requires this permission to send `HEAD` requests to the MediaPackage v2 origin. For more information about OAC, see [Restrict access to an
  AWS Elemental MediaPackage v2 origin](private-content-restricting-access-to-mediapackage.md "private-content-restricting-access-to-mediapackage.md").

## MQAR log fields

CloudFront provides the following fields in real-time access logs to reflect the quality score
and the selected origin. You can enable these fields in your CloudFront real-time access logs
logs:

- `r-host`
- `sr-reason`
- `x-edge-mqcs`

For more information, see [Fields](real-time-logs.md#real-time-logs-fields "real-time-logs.md#real-time-logs-fields") 65-67.
