# Getting started with VOD content delivery in

MediaPackage

This Getting Started tutorial shows you how to use the AWS Elemental MediaPackage console to
ingest video on demand (VOD) content and make it available for playback.

## Prerequisites

Before you can use AWS Elemental MediaPackage VOD capability, you must meet the following
conditions:

- You have an AWS account and the appropriate permissions to access, view,
  and edit MediaPackage components. Make sure that your system administrator
  has completed the steps in [Setting up MediaPackage](setting-up.md "setting-up.md"), and then return to
  this tutorial.
- You have file-based source content in one or more Amazon S3 buckets.

For supported VOD inputs and codecs, see [VOD supported codecs and input types](supported-inputs-vod.md "supported-inputs-vod.md").

## Step 1: Access MediaPackage

Using your IAM credentials, sign in to the AWS Elemental MediaPackage console:

```
https://`region`.console.aws.amazon.com/mediapackage/home
```

## Step 2: Create a packaging

group

A packaging group holds one or more packaging configurations. The packaging
configurations enable you to define what kind of VOD outputs you want. To apply these output
definitions, associate a packaging group to multiple assets.

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

## Step 3: Create a packaging configuration

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

## Step 4: Create an asset

An asset resource is how MediaPackage ingests, packages, and serves VOD content. The asset is associated with one or more packaging configurations. Downstream devices send playback requests to specific packaging configurations on the asset.

MediaPackage doesn't require customer data from you, so assets don't include those fields.

###### To create an asset

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
   either the .smil manifest (MP4) or the .m3u8 parent playlist (HLS) within your Amazon S3
   bucket, including the name of the source content. You don't need to enter the bucket name because you chose it in
   **Amazon S3 bucket name** field. For example, if your content is called `lion_movie.m3u8` and
   is in a subdirectory called `thursday_night` in a
   bucket called `movies`, you would enter the
   following in the **Filename** field:

```
thursday_night/lion_movie.m3u8
```

For more information about using .smil manifests with MediaPackage, see [Requirements for .smil manifests](supported-inputs-vod-smil.md "supported-inputs-vod-smil.md"). 6. For **Packaging group**, choose the group that
you created in [Step 2: Create a packaging
group](#gs-create-grp "#gs-create-grp"). 7. Choose **Ingest assets**.

## Step 5: Provide playback URLs

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
   [Step 4: Create an asset](#gs-create-asset "#gs-create-asset").
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

## (Optional) Step 6: Monitor MediaPackage

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

For a list of MediaPackage metrics, see [AWS Elemental MediaPackage VOD content metrics](metrics-vod.md "metrics-vod.md").

## Step 7: Clean up

To avoid incurring extra charges, delete your VOD resources. If you want to make a
specific output unavailable, delete the packaging configuration from the packaging
group. If you want to make an asset no longer available for playback from any
outputs, delete the asset.

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
