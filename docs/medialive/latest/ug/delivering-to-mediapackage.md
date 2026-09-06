

# Delivering to MediaPackage
<a name="delivering-to-mediapackage"></a>

The **MediaPackage output group** provides a simplified setup experience. MediaLive is preconfigured with most of the information needed to package and deliver output to the MediaPackage channel you specify. Both v2 and v1 workflows use this output group type.

If you want to deliver output from AWS Elemental MediaLive to AWS Elemental MediaPackage, follow the guidance in this section to determine the correct output group configuration.

**Topics**
+ [MediaPackage v2 (recommended)](#delivering-to-mediapackage-v2)
+ [MediaPackage v1 (legacy)](#delivering-to-mediapackage-v1)

## MediaPackage v2 (recommended)
<a name="delivering-to-mediapackage-v2"></a>

If you are delivering to MediaPackage v2, configure the MediaPackage output group for **MediaPackage v2 (CMAF Ingest)**. This is the recommended path for all new workflows, including glass-to-glass low-latency delivery. The v2 configuration uses CMAF Ingest and requires the MediaPackage **channel group name** and **channel name** (rather than a channel ID).

Key benefits of MediaPackage v2:
+ Low-latency HLS (LL-HLS) delivery support
+ Multi-codec packaging
+ Cross-Region distribution (configure additional destinations for redundancy)

For setup instructions, see [Creating a MediaPackage output group](opg-mediapackage.md).

### Other output group types with MediaPackage v2
<a name="delivering-to-mediapackage-v2-other-output-groups"></a>

MediaPackage v2 also accepts input from the following output group types:
+ **CMAF Ingest output group** — delivers CMAF Ingest content directly to MediaPackage v2 ingest endpoints.
+ **HLS output group** — delivers HLS content to MediaPackage v2 ingest endpoints. This option exists for backwards compatibility with existing HLS-based workflows.

However, the MediaPackage output group is the recommended path because it provides managed connectivity between MediaLive and MediaPackage, including automatic endpoint discovery and streamlined configuration. If you use a generic CMAF Ingest or HLS output group, you will not benefit from this managed integration and may need to migrate later to access features that depend on it.

## MediaPackage v1 (legacy)
<a name="delivering-to-mediapackage-v1"></a>

**Note**  
MediaPackage v2 is the recommended path for all new deployments. If you are currently using MediaPackage v1, we recommend migrating to v2.

If you are delivering to a legacy MediaPackage v1 channel, you have two options for your output group type:

### Option 1: MediaPackage output group (v1 / HLS ingest)
<a name="delivering-to-mediapackage-v1-option1"></a>

Note the following restrictions when using the MediaPackage output group with v1:
+ The MediaLive channel and the MediaPackage channel must be in the same AWS Region.
+ There are restrictions on ID3 metadata configuration. For details, see [Working with ID3 metadata](id3-metadata.md).

For setup instructions, see [Creating a MediaPackage output group](opg-mediapackage.md).

### Option 2: HLS output group
<a name="delivering-to-mediapackage-v1-option2"></a>

Alternatively, you can use a standard HLS output group to deliver to MediaPackage v1. This option provides full control over the output configuration, including cross-Region delivery and unrestricted ID3 metadata.

Use this option if you need:
+ Cross-Region delivery between MediaLive and MediaPackage
+ Full control over ID3 metadata insertion
+ Custom packaging parameters

For setup instructions, see [Creating an HLS output group](opg-hls.md).