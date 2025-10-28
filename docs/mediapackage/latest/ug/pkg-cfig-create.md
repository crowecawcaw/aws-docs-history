# Creating a packaging configuration

Create a packaging configuration to define how AWS Elemental MediaPackage prepares content for
delivery from an asset.

To create a packaging configuration, you can use the MediaPackage console, the
AWS CLI, or the MediaPackage
API. For information about creating a packaging configuration with the AWS CLI or MediaPackage API, see [Packaging_configurations](../../../mediapackage-vod/latest/apireference/packaging_configurations.md "../../../mediapackage-vod/latest/apireference/packaging_configurations.md") in the _AWS Elemental MediaPackage VOD API Reference_.

When you're creating a packaging configuration, don't put sensitive identifying
information like customer account numbers into free-form fields, such as the **ID** field. This applies when you're using the MediaPackage console, MediaPackage
API, AWS CLI, or AWS SDKs. Any data that you enter into MediaPackage might get picked
up for inclusion in diagnostic logs or Amazon CloudWatch Events.

###### Topics

- [Creating an HLS packaging
  configuration](pkg-cfig-create-hls.md "pkg-cfig-create-hls.md")
- [Creating a DASH packaging
  configuration](pkg-cfig-create-dash.md "pkg-cfig-create-dash.md")
- [Creating a Microsoft Smooth packaging
  configuration](pkg-cfig-create-mss.md "pkg-cfig-create-mss.md")
- [Creating a CMAF packaging configuration](pkg-cfig-create-cmaf.md "pkg-cfig-create-cmaf.md")
