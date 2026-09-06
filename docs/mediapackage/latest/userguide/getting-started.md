

# Getting started with AWS Elemental MediaPackage
<a name="getting-started"></a>

This tutorial describes how to get started with MediaPackage, using the console to create a channel and endpoints for streaming live videos.

**Topics**
+ [Prerequisites](#create-iam)
+ [Step 1: Access MediaPackage](#access-emp)
+ [Step 2: Create a channel group](#create-channel-group)
+ [Step 3: Create a channel](#create-channel)
+ [Step 4: Create an endpoint](#create-endpoint)
+ [Step 5: Clean up](#clean-up)

## Prerequisites
<a name="create-iam"></a>

Before you can use MediaPackage, you need an AWS account and the appropriate permissions to access, view, and edit MediaPackage components. Make sure that your system administrator has completed the steps in [Setting up MediaPackage](setting-up.md), and then return to this tutorial.

For supported live inputs and codecs, see [Supported inputs and outputs](supported-inputs.md).

## Step 1: Access MediaPackage
<a name="access-emp"></a>

Using your IAM credentials, sign in to the AWS Elemental MediaPackage console:

```
https://console.aws.amazon.com/mediapackage/
```

## Step 2: Create a channel group
<a name="create-channel-group"></a>

A channel group is the top-level resource that streamlines the organization of multiple channels and origin endpoints associated with it.

**To create a channel group**

1. Open the MediaPackage console at [https://console.aws.amazon.com/mediapackage/](https://console.aws.amazon.com/mediapackage/).

1. On the **Channel groups** page, choose **Create channel group**.

1. Enter a unique name that describes the channel group and, optionally, a description.

1. Choose **Create**.

   MediaPackage displays the new channel group's details page.

## Step 3: Create a channel
<a name="create-channel"></a>

The channel represents the input to MediaPackage for incoming live content from an encoder such as AWS Elemental MediaLive. The channel receives content, and after packaging it, outputs it through an endpoint to downstream devices (such as video players or CDNs) that request the content.

MediaPackage does not require that you supply any customer data. There are no fields in channels where there is an expectation that you will provide customer data.

**To create a channel**

1. Access the channel group that the channel will be associated with.

1. In the **Channel group details** page, under **Channels**, choose **Create channel**.

1. Enter a unique name that describes the channel and, optionally, a description.

1. Choose your channel's IAM policy that defines the permissions of your channel.

1. Choose **Create**.

   MediaPackage displays the new channel's details page. The channel is active and can start receiving content as soon as it's created.

## Step 4: Create an endpoint
<a name="create-endpoint"></a>

The endpoint is attached to a channel, and represents the output of the live content. You can associate multiple endpoints to a single channel. Each endpoint gives players and downstream CDNs (such as Amazon CloudFront) access to the content for playback. 

**To create an endpoint**

1. On the **Channels** page, choose the channel that the endpoint will be associated with.

1. On the details page for the channel, under **Origin endpoints**, choose **Create endpoint**.

1. Enter a unique name that describes the endpoint and, optionally, a description.

1. Choose the container type and define the corresponding settings.

1. Choose your origin endpoint's IAM policy that defines the permissions of your endpoint.

1. Define the manifests emitted from the origin endpoint.

1. Choose **Save**.

   MediaPackage displays the channel's details page, including the endpoint that you just created.

## Step 5: Clean up
<a name="clean-up"></a>

To avoid extraneous charges, be sure to delete all unnecessary channel groups, channels, and endpoints. You must delete the channels and endpoints before you can delete the channel group.

1. Delete the endpoint as described in [Deleting an endpoint in AWS Elemental MediaPackage](endpoints-delete.md).

1. Delete a channel as described in [Deleting a channel in AWS Elemental MediaPackage](channels-delete.md).

1. Delete the channel group as described in [Deleting a channel group from AWS Elemental MediaPackage](channel-group-delete.md).