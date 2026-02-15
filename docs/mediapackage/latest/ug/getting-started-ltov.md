# Getting started with live-to-VOD content delivery

in MediaPackage

This Getting Started tutorial shows you how to use the AWS Elemental MediaPackage console to
create a live-to-VOD (video on demand) asset and make it available for playback.

To deliver live-to-VOD content, you do these three main things:

- Ingest a live HLS content stream into MediaPackage
- Extract a VOD asset from the stream
- Make the asset available for playback

###### Note

You're not required to use MediaPackage to deliver your live-to-VOD asset
to viewers. This tutorial is meant as an illustration of how you can use
MediaPackage to complete the live-to-VOD workflow.
The following sections are a guided tutorial for becoming familiar with these three
things and other supporting actions.

## Prerequisites

Before you can use AWS Elemental MediaPackage, you need an AWS account and the appropriate
permissions to access, view, and edit MediaPackage components. Make sure that your
system administrator has completed the following steps in [Setting up MediaPackage](setting-up.md "setting-up.md"), and then return to this tutorial:

- To create an AWS account, see [Signing up for AWS](setting-up-aws-sign-up.md "setting-up-aws-sign-up.md").
- To allow non-administrative roles access to MediaPackage, see [Creating policies and non-administrative roles](setting-up-create-non-admin-iam.md "setting-up-create-non-admin-iam.md").
- To allow MediaPackage to access your Amazon S3 bucket to save and retrieve the
  live-to-VOD asset, see [Allowing AWS Elemental MediaPackage to access other
  AWS services](setting-up-create-trust-rel.md "setting-up-create-trust-rel.md").

## Step 1: Access MediaPackage

Using your IAM credentials, sign in to the AWS Elemental MediaPackage console:

```
https://console.aws.amazon.com/mediapackage/
```

## Step 2: Ingest live content

To ingest a live content stream into AWS Elemental MediaPackage and extract a video on demand
(VOD) asset from it, create a channel and endpoint. The channel is the entry point
to MediaPackage, and the endpoint provides MediaPackage access to the stream so
that it can extract the VOD asset. The following sections describe how to use the
MediaPackage console to create a channel and endpoint.

### Create a channel

The channel is the first component in MediaPackage. It represents the input
to MediaPackage for incoming live content from an encoder such as AWS Elemental MediaLive.

MediaPackage does not require that you supply any customer data. There are no
fields in channels where there is an expectation that you will provide customer
data.

###### To create a channel

1. On the MediaPackage **Channels** page,
   choose **Create channel**.
2. For **ID**, enter a name that describes the channel, such as
   `channelHLS1`. The ID is the primary identifier for
   the channel, and must be unique for your account in the AWS Region.
   Supported characters are letters, numbers, underscores (\_), and dashes (-). You
   can't use spaces in the ID.
3. Keep the defaults for the remaining fields, and then choose **Create**.

MediaPackage displays the new channel's details page. 4. On the details page for the channel, note the values for **URL**, **Username**, and
**Password**. If you're using input redundancy, you need
this information for both input URLs. If you're sending only one stream to the
channel, you can note the information for either input URL.

MediaPackage securely generates the WebDAV user names and passwords when
it creates the channel. If you need to change these credentials, see [Rotating credentials on an input URL](channels-rotate-creds.md "channels-rotate-creds.md").

Provide the information from these fields to the person in charge of the
upstream encoder. In the stream configuration in the encoder, this person
must enter the destination as the input URL, and the WebDAV credentials as
the channel's user name and password. The upstream encoder must use digest
authentication and push WebDAV over HTTPS to MediaPackage, and include
these credentials. If you're using input redundancy, the input streams to
this channel must have identical encoder settings. For more information
about setting up source streams for input redundancy, see [Live input redundancy AWS Elemental MediaPackage processing
flow](what-is-flow-ir.md "what-is-flow-ir.md").

### Create an endpoint

The endpoint is attached to a channel, and represents the output of the live
content. When you create a harvest job to extract a VOD asset from the live
content, you have to indicate what endpoint you're extracting from. You can
harvest assets from clear (unencrypted) or encrypted HLS and DASH endpoints, and the endpoint
must have a startover window defined. If you have only encrypted endpoints, see
the [Creating live-to-VOD assets with AWS Elemental MediaPackage](ltov.md "ltov.md") feature reference.

MediaPackage does not require that you supply any customer data. There are no fields in
endpoints where there is an expectation that you will provide customer data.

###### To create an endpoint

1. On the **Channels** page, choose the channel that
   the endpoint will be associated with.
2. On the details page for the channel, under **Origin
   endpoints**, choose **Manage endpoints**.
3. For **ID**, enter a name that describes the endpoint, such as
   `HLSendpoint1`. The ID is the primary identifier
   for the endpoint, and must be unique for your account in the AWS Region.
   Supported characters are letters, numbers, underscores (\_), and dashes (-). You
   can't use spaces in the ID.
4. Keep the defaults for the remaining fields, and then choose **Save**.

MediaPackage displays the channel's details page, including the endpoint
that you just created. 5. On the details page for the channel, note the value in the **URL**
field for the endpoint. Provide this information to the person in charge of
the downstream device (CDN or player). In the downstream device, this person
must enter the request destination as the endpoint's URL.

## Step 3: Extract a VOD asset

To extract a live-to-VOD asset from a live content stream, create a harvest job.
The harvest job identifies what endpoint the asset is being harvested from, the
start and end of the asset, and where MediaPackage saves the asset after it's been
harvested.

###### To create a harvest job

1. On the **Harvest jobs** page, choose
   **Create harvest job**.
2. For **ID**, enter a name that describes the harvest job,
   such as `gamehighlights`. The ID is the primary
   identifier for the job. You can reuse the ID after the harvest job expires
   from your account. Supported characters are letters, numbers, underscores
   (\_), and dashes (-). You can't use spaces in the ID.
3. For **Origin endpoint**, select the endpoint for the live
   content stream that you're extracting a VOD asset from. The endpoint must
   serve clear (unencrypted) or encrypted DASH or HLS content. If you want to extract from encrypted
   live content, see [Creating live-to-VOD assets with AWS Elemental MediaPackage](ltov.md "ltov.md").
4. For **Date and time format**, keep the default.
5. For **When the live-to-VOD asset begins** and
   **When the live-to-VOD asset ends**, enter the start
   and end dates and times for the extracted VOD asset. We recommend that the
   start time be after the live stream has started and before the current time
   ("now"). The end time must be in the past.

###### Note

"Now" is the current time according to the
`EXT-X-PROGRAM-DATE-TIME`, when it's present in the
source content from the encoder. Therefore, we recommend that the
upstream encoder provides an `EXT-X-PROGRAM-DATE-TIME` tag in
the source. 6. For **IAM role ARN**, enter the IAM role that allows
MediaPackage to write your live-to-VOD asset to your Amazon S3 bucket. For help
with the role, see [Allowing AWS Elemental MediaPackage to access other
AWS services](setting-up-create-trust-rel.md "setting-up-create-trust-rel.md"). 7. For **Amazon S3 bucket name**, select the Amazon S3 bucket where you want
MediaPackage to store the live-to-VOD asset. 8. For **Manifest key**, enter the path in the Amazon S3
bucket and identifier for the parent manifest for the live-to-VOD asset.
MediaPackage creates a directory based on the path that you enter.

###### Important

The manifest key must be unique. When you use the same manifest key
for multiple harvest jobs, the newest playlist for the asset overwrites
existing playlists. The only time you should reuse a manifest key is
when you are harvesting the same content, such as if there was a problem
with a previous harvest of the content. 9. Choose **Create**.

When MediaPackage processes the harvest job, it sends a CloudWatch event when the job
fails or succeeds. The event includes the details of the harvest job. If the job
fails, the event includes information about why. This information is available only
in the CloudWatch event. For example events, see [Harvest job notification events](cloudwatch-events-example.md#hj-status-events "cloudwatch-events-example.md#hj-status-events").

## (Optional) Step 4: Output VOD content

To use MediaPackage to make the live-to-VOD asset available for playback, create
a packaging group, packaging configuration, and asset resource. The asset ingests
the live-to-VOD asset from the Amazon S3 bucket. A packaging group holds one or more
packaging configurations, which define the output format and settings.

### Create a packaging group

A packaging group holds one or more packaging configurations. The packaging
configurations enable you to define what kind of VOD outputs you want. To apply these output
definitions, associate a packaging group to multiple assets.

###### Example

You have 15 pieces of source content. You want to serve them all as DASH,
HLS, and encrypted HLS outputs. To do this, you define one packaging group
with DASH, HLS, and encrypted HLS packaging configurations. You then
associate that group to the asset resources that represent these pieces of
content. You don't have to create new configurations for each asset.

MediaPackage doesn't require that you supply any customer data. There are no fields in
packaging groups where there is an expectation that you will provide customer data.

###### To create a packaging group

1. On the **Packaging groups** page, choose **Create group**.
2. For **ID**, enter a name that describes the group, such
   as `gamehighlights`. The ID is the
   primary identifier for the group, and must be unique for your account in
   this AWS Region. Supported characters are letters, numbers, underscores (\_),
   and dashes (-). You can't use spaces in the ID.
3. Choose **Create**.

### Create a packaging configuration

A packaging configuration specifies how the output manifest is configured, such as
stream selection limitations and ordering.

MediaPackage does not require that you supply any customer data. There are no fields in
packaging configurations where there is an expectation that you will provide customer data.

###### To create a packaging configuration

1. On the **Packaging groups** page, choose the group that you just created.
2. On the details page for the packaging group, under **Packaging configurations** choose
   **Manage configurations**.
3. On the **Manage packaging configurations** page, choose **Add**, and then
   choose **New configuration**.
4. For **ID**, enter a name that describes the
   configuration, such as `hls_highlights`. The ID is
   the primary identifier for the configuration, and must be unique for
   your account in this AWS Region. Supported characters are letters,
   numbers, underscores (\_), and dashes (-). You can't use spaces in the
   ID.
5. Keep the defaults for the remaining fields, and then choose
   **Save**.

### Create an asset

An asset resource is how AWS Elemental MediaPackage ingests, packages, and serves VOD content. The asset is
associated with one or more packaging configurations. Downstream devices send playback requests to specific
packaging configurations on the asset.

MediaPackage doesn't require customer data from you, so assets don't include those fields.

###### To create an asset and ingest source content

1. From your Amazon S3 buckets, determine what file you're using as source content. Make note of the
   following:
   - The name of the Amazon S3 bucket where the file is stored
   - The full path for the file, such as _S3://bucket/path/source-file-name_
   - The IAM role that allows MediaPackage to read from
     Amazon S3

2. On the MediaPackage console, go to the
   **Assets** page, and then choose **Ingest
   assets**.
3. For **Amazon S3 bucket name**, choose the bucket where your source content is
   stored.
4. For **IAM role**, choose **Use existing role** and select the IAM role that allows MediaPackage to read from Amazon S3.
5. For **Filename**, enter the full path to
   either the [.smil manifest](supported-inputs-vod-smil.md "supported-inputs-vod-smil.md") (MP4) or the .m3u8 parent playlist (HLS) within your Amazon S3
   bucket, including the name of the source content. For example, if your content is called `lion_movie.m3u8` and
   is in a subdirectory called `thursday_night` in a
   bucket called `movies`, you would enter the
   following in the **Filename** field:

```
thursday_night/lion_movie.m3u8
```

You don't need to enter the bucket name because you chose it in
**Amazon S3 bucket name** field. 6. For **Packaging group**, choose the group
that you created in [Create a packaging group](#gs-create-grp-ltov "#gs-create-grp-ltov"). 7. Choose **Ingest assets**.

### Provide playback URLs

After creating the asset resource, AWS Elemental MediaPackage prepares to serve the
packaged manifests to viewers. This happens in the background and might take
some time depending on the size and complexity of the source content, but is
usually less than a few minutes. The URLs of the manifests are available
immediately on the asset's details page, but content is not yet available for
playback.

After the processing for each manifest is complete, MediaPackage sends an Amazon CloudWatch
event to your account.

On the asset, MediaPackage provides a URL for each packaging configuration. This
URL is how downstream devices (CDN or playback device) request VOD content from
MediaPackage.

###### To get playback URLs

1. On the MediaPackage console, go to the **Assets** page
   and choose the **ID** of the asset that you created in
   [Step 4: Create an asset](getting-started-vod.md#gs-create-asset "getting-started-vod.md#gs-create-asset").
2. On the asset's detail page, get the URL for each packaging
   configuration.
3. Provide the URLs to the person in charge of the downstream device (CDN or
   player). In the downstream device, this person must enter the request
   destination as the URL from the corresponding packaging
   configuration.

Each URL is stable. It never changes during the lifetime of the combination of
this asset and packaging configuration. Provide the URL to the person in charge of
the downstream device (CDN or player). In the downstream device, this person must
use the asset's URL as the request destination.

## (Optional) Step 5: Monitor MediaPackage

activity

Use Amazon CloudWatch to track MediaPackage activity, such as the counts of bytes that
MediaPackage has received and sent, response times, and request counts. Metrics are
grouped first by the service namespace, and then by the various dimension
combinations within each namespace.

###### To view metrics using the CloudWatch console

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Metrics**.
3. Under **All metrics**, choose the
   **AWS/MediaPackage** namespace.
4. Select the metric dimension to view the metrics (for example, choose
   `channel` to view metrics per channel).

For a list of MediaPackage metrics, see [Monitoring AWS Elemental MediaPackage with Amazon CloudWatch
metrics](monitoring-cloudwatch.md "monitoring-cloudwatch.md").

## Step 6: Clean up

To avoid incurring extra charges, delete the resources that you're no longer
using.

###### Note

Harvest jobs automatically expire off your account and can't be manually
deleted.

### Delete live resources

When you're done ingesting, serving, and harvesting from live content, delete
the channel and endpoint. You must delete all endpoints on a channel before you
can delete the channel.

###### To delete an endpoint

1. On the MediaPackage **Channels** page, choose the channel that
   the endpoint is associated with.
2. On the details page for the channel, under **Origin endpoints**, select the origin endpoint that you want to delete.
3. Select **Delete**.
4. In the **Delete endpoints** confirmation dialog box, choose **Delete**.

###### To delete a channel

1. On the **Channels** page, choose the channel you want to delete.
2. Choose **Delete**.
3. In the **Channel delete** confirmation dialog box, choose **Delete**.

MediaPackage removes the channel and all associated endpoints.

### Delete VOD resources

When you're done ingesting and serving VOD content, delete the extra
resources. If you want to make a specific output unavailable, delete the
packaging configuration from the packaging group. If you want to make an asset
no longer available for playback from any outputs, delete the asset.

###### To delete an asset

1. On the MediaPackage console, go to the **Assets**
   page, and then choose the **ID** of the asset.
2. On the asset's details page, choose
   **Delete**.
3. In the confirmation dialog box, choose
   **Delete**.

###### To delete a packaging configuration

1. On the MediaPackage console, go to the **Packaging groups**
   page.
2. Choose the **ID** of the group that has the configuration that you want to
   delete.
3. On the packaging group's details page, in the **Packaging configurations** section, locate the configuration and choose its **ID**.
4. On the packaging configuration's details page, choose **Delete**.
5. In the confirmation dialog box, choose
   **Delete**.
