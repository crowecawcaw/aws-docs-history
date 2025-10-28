# Viewing packaging configuration details

To ensure that the content is available in all necessary stream formats, view all
packaging configurations that are associated with a specific packaging group or with an
asset.

To view packaging configurations, you can use the AWS Elemental MediaPackage console, the AWS CLI, or the MediaPackage API.
For information about viewing a packaging configuration with the AWS CLI or MediaPackage API, see [Packaging_configurations id](../../../mediapackage-vod/latest/apireference/packaging_configurations-id.md "../../../mediapackage-vod/latest/apireference/packaging_configurations-id.md") in the _AWS Elemental MediaPackage VOD API Reference_.

###### To view packaging configurations in a packaging group (console)

1. Open the MediaPackage console at [https://console.aws.amazon.com/mediapackage/](https://console.aws.amazon.com/mediapackage/ "https://console.aws.amazon.com/mediapackage/").
2. In the navigation pane, under **Video on demand**, choose
   **Packaging groups**.
3. On the **Packaging groups** page, choose the
   group that contains the configurations that you want to view.

The **Packaging configurations** section displays all of the
configurations that are in this group. 4. To view the details of a specific packaging configuration, choose the
**Id** of that configuration.
MediaPackage displays summary information, such as the assets associated with
this packaging configuration.

###### To view all packaging configurations associated with an asset (console)

1. Open the MediaPackage console at [https://console.aws.amazon.com/mediapackage/](https://console.aws.amazon.com/mediapackage/ "https://console.aws.amazon.com/mediapackage/").
2. In the navigation pane, under **Video on demand**, choose
   **Assets**.
3. On the **Assets** page, choose the asset that you
   want to audit.

The **Playback details** section displays all of the
configurations that are associated with this asset. On this page, you can view
the playback status of the asset in the **Status** column. The
available statuses are as follows:

- **Not processed** - The asset hasn't been processed
  yet.
- **Processing** - MediaPackage is processing the asset. The asset
  isn't available for playback yet.
- **Processed** - The asset has been processed, and is
  available for playback.
- **Failed** - Processing failed.

###### Note

Status information isn't available for most assets ingested before September 30th, 2021.
