# Setting up ad insertion with MediaTailor

To insert personalized ads into your channel's stream, your channel's endpoint URL is the
content source for AWS Elemental MediaTailor. This guide shows how to set up MediaTailor for ad insertion.

## Prerequisites

Before you begin, make sure that you meet the following requirements:

- Prepare your HLS and DASH streams for MediaTailor ad insertion.
  - If you haven't prepared content streams already, see [Step 2: Prepare a stream](getting-started-ad-insertion.md#getting-started-prep-stream "getting-started-ad-insertion.md#getting-started-prep-stream")
    in the _Getting started with MediaTailor ad insertion_
    topic.

- Have
  an ad decision server (ADS).
- Configure **Ad break** settings in the program. For more information,
  see the [Configuring ad breaks for your program](channel-assembly-adding-programs.md#channel-assembly-programs-ad-breaks "channel-assembly-adding-programs.md#channel-assembly-programs-ad-breaks") procedure.

As a best practice, consider using a content delivery network (CDN) in between channel
assembly and MediaTailor ad insertion. The MediaTailor ad insertion service can generate additional
origin requests. Therefore, it's a best practice to configure your CDN to proxy the
manifests from channel assembly, then use the CDN prefixed URLs at the content source
URL.

## Configure MediaTailor for ad insertion

The following shows how to configure MediaTailor console settings so that you can insert
personalized ads into your channel's stream.

###### To configure MediaTailor for ad insertion

1. Open the MediaTailor console at [https://console.aws.amazon.com/mediatailor/](https://console.aws.amazon.com/mediatailor/ "https://console.aws.amazon.com/mediatailor/").
2. In the navigation pane, choose **Configurations**.
3. Under **Required settings**, enter the basic required information
   about your configuration:
   - **Name**: The name of your configuration.
   - **Content source**: Enter the playback URL from your channel's
     output, minus the file name and extension. For advanced information about MediaTailor
     configuration, see [Required settings](configurations-create.md#configurations-create-main "configurations-create.md#configurations-create-main").
   - **Ad decision server**: Enter the URL for your ADS.

4. You can optionally configure the **Configuration aliases**,
   **Personalization details**, and **Advanced
   settings**. For information about those settings, see [Optional configuration
   settings](configurations-create.md#configurations-create-addl "configurations-create.md#configurations-create-addl").
5. On the navigation bar, choose **Create configuration**.
   Now that you've set up MediaTailor for ad insertion, you can also set up ad breaks. For detailed
   instructions, see [Getting started with MediaTailor ad
   insertion](getting-started-ad-insertion.md "getting-started-ad-insertion.md").
