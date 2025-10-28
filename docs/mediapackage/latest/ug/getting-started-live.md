# Getting started with live content delivery in

AWS Elemental MediaPackage

This Getting Started tutorial shows you how to use the AWS Elemental MediaPackage (MediaPackage) console to
create a channel and endpoints for streaming live videos.

## Prerequisites

Before you can use MediaPackage, you need an AWS account and the appropriate
permissions to access, view, and edit MediaPackage components. Make sure that your
system administrator has completed the steps in [Setting up MediaPackage](setting-up.md "setting-up.md"), and
then return to this tutorial.

For supported live inputs and codecs, see [Live supported codecs and input types](supported-inputs-live.md "supported-inputs-live.md").

## Step 1: Access MediaPackage

Using your IAM credentials, sign in to the MediaPackage console:

```
https://console.aws.amazon.com/mediapackage/
```

## Step 2: Create a channel

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

## Step 3: Create endpoints

The endpoint is attached to a channel, and represents the output of the live
content. You can associate multiple endpoints to a single channel. Each endpoint
gives players and downstream CDNs (such as Amazon CloudFront) access to the content for
playback.

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

## (Optional) Step 4: Monitor MediaPackage

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

For a list of MediaPackage metrics, see [AWS Elemental MediaPackage live content metrics](metrics.md "metrics.md").

## Step 5: Clean up

To avoid extraneous charges, be sure to delete all unnecessary channels and
endpoints. You must delete all endpoints on a channel before the channel can be
deleted.

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
