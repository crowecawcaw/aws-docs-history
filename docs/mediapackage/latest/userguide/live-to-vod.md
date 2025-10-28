# Creating live-to-VOD assets with MediaPackage

You can use the AWS Elemental MediaPackage v2 live-to-VOD harvester to extract portions of live video streams and save them as Video on Demand (VOD) assets. This feature is useful for creating highlight reels from live sports events, archiving broadcasts, or any other scenario where you need to convert live content into on-demand assets.

The following topics provide more information about live-to-VOD assets in
MediaPackage v2.

###### Topics

- [Requirements](#live-to-vod-requirements "#live-to-vod-requirements")
- [What is a harvest job?](#what-is-harvest-job "#what-is-harvest-job")
- [How live-to-VOD works](#how-live-to-vod-works "#how-live-to-vod-works")
- [Creating a harvest job](#create-harvest-job "#create-harvest-job")
- [Viewing harvest jobs](#view-harvest-jobs "#view-harvest-jobs")
- [Canceling a harvest job](#cancel-harvest-job "#cancel-harvest-job")

## Requirements

When creating live-to-VOD assets in MediaPackage v2, keep the following requirements in mind:

###### Endpoint requirements

- The endpoint must be a MediaPackage v2 endpoint. MediaPackage v1 endpoints are not compatible.
- The endpoint must grant MediaPackage v2 `GetObject` and `HarvestObject` access. For more information, see [MediaPackage L2V Harvester](endpoint-auth.md#mediapackage-endpoint "endpoint-auth.md#mediapackage-endpoint").

###### Live-to-VOD asset requirements

- The start time of the harvest job must be in the past.
- The maximum job duration is 24 hours.
- Any harvested manifest must not include start, end, or clip start time in the manifest filter configuration.

## What is a harvest job?

A harvest job represents a request to extract a live-to-VOD asset from an endpoint for a specific timeframe. MediaPackage uses information from the harvest job to determine the start and end times of the asset, and where to store it after the harvest job is complete.

A harvest job runs only once after it's created. MediaPackage keeps a record of the job on your account for reference only. You can't modify or delete a record after you create the harvest job.

###### Harvest job features

- Multiple manifests can be harvested in a single request.
- Real-time harvesting is supported for ongoing streams.
- Rendition filtering is available through a combination of `ManifestFilter` in `FilterConfiguration` (in `OriginEndpoint` configuration) and `HarvestedManifests` (in `HarvestJob` configuration).
- All included segments across different manifests will be de-duplicated to be moved to your S3
  bucket only once. (The segments are shared between different manifests.)

## How live-to-VOD works

In the processing flow for live-to-VOD (video on demand) content, MediaPackage v2 extracts a clip of video from a live content stream. MediaPackage saves this clip as a live-to-VOD asset in Amazon S3. You can use the VOD content processing functionality in MediaPackage to deliver the asset to playback devices, or you can use a VOD encoding service that supports HLS or DASH inputs.

The following sections provide an overview of the live-to-VOD processes.

### Live-to-VOD

`HarvestJob`

You can schedule a harvest job to take place at a specified timeframe in your live
content stream.

The process looks like this:

1. You create a channel group, channel, and origin endpoint in MediaPackage v2 to
   ingest and package your live stream.
2. You must grant the MediaPackage v2 service principal access to
   `PutObject` in your S3 bucket policy and
   `HarvestObject` in your MediaPackage v2 endpoint.
3. You create a harvest job using the `CreateHarvestJob` API
   operation or the AWS Management Console. This job defines the live-to-VOD asset you want
   to extract from the live stream.
4. MediaPackage v2 processes the harvest job, extracting the specified timeframe
   from the live stream.
5. The harvested asset is saved to the S3 bucket that you specified in the
   harvest job configuration.
6. The live-to-VOD asset is now available in your S3 bucket for further
   processing or delivery.

###### Note

When using harvested content with AWS Elemental MediaTailor, be aware that the harvesting
process can result in `BANDWIDTH` values that differ from the
original live stream. If `BANDWIDTH` values differ by 15% or more,
MediaTailor might determine that previously transcoded ads no longer match and require
re-transcoding. For more information about this behavior and troubleshooting
steps, see [BANDWIDTH variance threshold](../../../mediatailor/latest/ug/troubleshooting-new-creative-skipping.md#harvest-job-bandwidth-variance "../../../mediatailor/latest/ug/troubleshooting-new-creative-skipping.md#harvest-job-bandwidth-variance") in the _MediaTailor User
Guide_.

### Live-to-VOD `HarvestObject`

You can specify a packaged manifest or segments to harvest from your live content
stream. For information about the `HarvestObject` API operation, see [HarvestObject](dataplane-apis.md#dataplane-apis-harvestobject "dataplane-apis.md#dataplane-apis-harvestobject").

The process looks like this:

1. You create a channel group, channel, and origin endpoint in MediaPackage v2 to
   ingest and package your live stream.
2. You must grant the MediaPackage v2 service principal access to
   `PutObject` in your S3 bucket policy and
   `HarvestObject` in your MediaPackage v2 endpoint.
3. You harvest a packaged live-to-VOD asset using the
   `HarvestObject` dataplane API operation. This request
   specifies the manifest or segments that you want to save and indicates where
   they should be saved.
4. MediaPackage v2 processes the request and saves the asset to the S3 bucket that
   you specified.
5. The live-to-VOD asset is now available in your S3 bucket for further
   processing or delivery.

## Creating a harvest job

Create a harvest job to extract a live-to-VOD asset from an encrypted or clear (unencrypted) live HLS or DASH stream.

###### Important

To run a harvest job and save the live-to-VOD asset, MediaPackage must have permissions to write to the S3 bucket where the asset will be stored. MediaPackage must also have `GetObject` and `HarvestObject` access to the MediaPackage v2 endpoint where the asset will be harvested from.

You can use the MediaPackage console, the AWS CLI, or the MediaPackage API to create a harvest job. For information, see the [MediaPackage V2 Live API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

When you're creating a harvest job, don't put sensitive identifying information like account numbers into free-form fields, such as the ID field. Any data that you enter into MediaPackage might get picked up for inclusion in diagnostic logs or CloudWatch Events.

###### To create a harvest job

1. Open the MediaPackage console at [https://console.aws.amazon.com/mediapackage/](https://console.aws.amazon.com/mediapackage "https://console.aws.amazon.com/mediapackage").
2. Choose **Channel group**.
3. Choose a channel.
4. Choose the **Harvest jobs** table in the channel view.
5. Choose **Create harvest job**.
6. Enter a **Harvest job name**. You can reuse the name after the harvest job expires from your account. The harvest job expires within 15 days of job creation.
7. For **Channel group name**, select the channel group that serves the live stream that you're harvesting the live-to-VOD asset from. By default, you can have up to 10 active harvest jobs within a channel group.
8. For **Channel name**, select the channel that serves the live stream that you're harvesting the live-to-VOD asset from.
9. For **Origin endpoint name**, select the endpoint that serves the live stream that you're harvesting the live-to-VOD asset from. Note the following considerations:
   - Your harvest job start time must fall within your MediaPackage endpoint's startover window. The startover window determines the time frame that assets can be harvested from your endpoint. For example, if your endpoint has a startover window of three days, you can harvest your asset anytime within that time frame. To adjust your endpoint's startover window, see [Viewing an origin endpoint in AWS Elemental MediaPackage](endpoints-view.md "endpoints-view.md").
   - Your harvested live-to-VOD asset can have a maximum duration of 24 hours.
   - Your endpoint must serve either clear (unencrypted) or encrypted DASH, HLS, or CMAF
     content.

10. For **Harvested manifest name**, select the endpoint that serves the live stream that you're harvesting the live-to-VOD asset from. You can set up the manifest filter in your filter configuration, but not clip start time, start time, end time, or time delay seconds. For more information, see [FilterConfiguration](../APIReference/API_FilterConfiguration.md "../APIReference/API_FilterConfiguration.md") in the _MediaPackage V2 Live API Reference_.
11. For **Schedule configuration**, select a **Start date and time** and **End date and time**. The maximum time range is 24 hours.
    - Select a date and time for **When the live-to-VOD asset starts**. The asset's begin time must be at the same time or after the live event started, and it must be in the past. The start time must also be within the startover window on the endpoint. If the endpoint has a window of 5 hours and the start time is 6 hours ago, the harvest job fails.
    - Select a date and time for **When the live-to-VOD asset ends**. The length of the asset can't exceed the startover window on the endpoint. The end time can be in the future.

12. For **Destination**, select the **S3 bucket name** in which to store the live-to-VOD asset. The bucket must be in the same AWS Region that MediaPackage is harvesting from.
13. For **S3 destination path**, enter the path to the asset in the bucket. Include the file name for the parent manifest of the asset. If the directory structure doesn't already exist in the bucket, MediaPackage creates it.
14. Choose **Create harvest job**.

## Viewing harvest jobs

You can view all harvest jobs that you created within the last 15 days. After that, harvest jobs expire from your account.

###### To view a harvest job

1. Open the MediaPackage console at [https://console.aws.amazon.com/mediapackage/](https://console.aws.amazon.com/mediapackage "https://console.aws.amazon.com/mediapackage").
2. Choose **Channel group**.
3. Choose a channel.
4. Choose the **Harvest jobs** tab.
5. Choose a harvest job name to view the details.

Error messages for failed jobs will be returned in the `ErrorMessage` field.

## Canceling a harvest job

You can cancel a harvest job that is in `Queued` or `In progress` status. This stops MediaPackage from moving content into your S3 bucket.

###### To cancel a harvest job

1. Open the MediaPackage console at [https://console.aws.amazon.com/mediapackage/](https://console.aws.amazon.com/mediapackage "https://console.aws.amazon.com/mediapackage").
2. Choose **Channel group**.
3. Choose a channel.
4. Choose the **Harvest jobs** tab.
5. Choose a harvest job that is in `Queued` or `In progress` status.
6. Choose **Cancel harvest job**.
