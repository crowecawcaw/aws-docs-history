# Customizing the paths inside HLS manifests

When you create an HLS output group in a standard MediaLive channel, you can set up custom
manifests.

Note that you can't set up custom manifests in a MediaPackage output group, or in an HLS
output group if the downstream system is MediaPackage. MediaPackage works only with the default paths.

You can customize the main manifest by changing the paths to the child manifests.
You can also customize each child manifest by change the paths the media files.
Typically, you only need to change the
syntax if the downstream system has special path requirements. Akamai CDNs usually require you to
change the syntax.

###### Note

The information in this section on HLS manifests assumes that you are familiar with the
general steps for creating a channel, as described in [Creating a channel from scratch](creating-channel-scratch.md "creating-channel-scratch.md").

The key fields in the console that relate to this feature are in the
**Location** grouping of the **HLS output group** section on
the **Create channel** page. To review the step where you complete these fields,
see [The procedure](creating-hls-output-group.md#hls-create-procedure "creating-hls-output-group.md#hls-create-procedure").

###### Topics

- [Procedure to set up custom paths](hls-custom-manifests-procedure.md "hls-custom-manifests-procedure.md")
- [How manifests work](hls-manifests-how-work.md "hls-manifests-how-work.md")
- [Rules for custom paths](hls-custom-paths-rules.md "hls-custom-paths-rules.md")
- [Guidance for setting up for custom paths](hls-custom-paths-guidance.md "hls-custom-paths-guidance.md")
- [Examples of custom
  paths](hls-custom-paths-examples.md "hls-custom-paths-examples.md")
