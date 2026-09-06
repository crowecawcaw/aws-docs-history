

# Creating A/B forensic video watermarks
<a name="feature-ab-watermark"></a>

A/B forensic video watermarking embeds an imperceptible forensic identifier into frames of live video. You can use forensic watermarks to trace the source of unauthorized redistribution. A/B forensic watermarking is a MediaLive feature that watermarking providers implement. Irdeto is the first A/B forensic watermarking implementation available in MediaLive.

When you enable A/B watermarking for a supported output group, MediaLive produces two variants (A and B) of each video rendition in that output group. Each variant carries a different watermark payload. MediaLive sends the A variant to the output group's regular A destination and the B variant to a paired B alternate destination that you specify. The downstream watermark-aware origin or CDN selects the corresponding A or B segment copy for each viewer request, constructing a unique per-session watermark sequence. MediaLive does not perform per-viewer selection or create viewer-facing manifests—that responsibility belongs to the downstream system. MediaLive doesn't change other output groups in the channel.

**Note**  
A/B forensic watermarking applies to video. It is separate from Nielsen watermarking, which inserts watermarks into audio. For information about Nielsen audio watermarking, see [Creating and inserting Nielsen watermarks](feature-nielsen-watermark.md).

**Applicable outputs**

A/B forensic video watermarking applies only to the following types of output groups:
+ CMAF Ingest
+ MediaPackage v2

MediaLive doesn't support other output group types for A/B watermarking.

For information about creating and configuring the supported output groups, see [Creating a CMAF Ingest output group](opg-cmafi.md) and [Creating a MediaPackage output group](opg-mediapackage.md).

**Requirements**

A/B forensic video watermarking has the following requirements:
+ The output width must be from 240 through 3840 pixels, and the output height must be from 240 through 2160 pixels.
+ The channel must use epoch locking as the output locking mode. A/B forensic video watermarking doesn't support pipeline locking. The input must carry an embedded UTC timecode because epoch locking and watermark sequencing depend on it. If the input doesn't supply a usable embedded UTC timecode, the channel still runs, but the watermark isn't correctly sequenced and can't be reliably detected downstream. For the full set of epoch locking requirements and to verify that your pipeline can epoch lock successfully, see [Configuring output locking and setting the mode](pipeline-locking-set-up.md#pipeline-locking-mode).
+ The output frame rate must be specified explicitly for every video encode in the watermarked output group. Don't use **Initialize from source** for frame rate control. Frame rates that don't divide evenly between input and output produce inaccurate watermark sequence numbers. Fractional frame rates such as 29.97 and 59.94 are supported when you specify them explicitly.
+ The regular A destination and the paired B alternate destination must be coordinated with the downstream system. For CMAF Ingest output groups, provide destination URLs. For MediaPackage v2 output groups, select the channel group, channel name, region, and endpoint for each destination.

**Important**  
Complete the following before you configure A/B watermarking:  
Arrange a valid watermarking license directly with Irdeto and obtain the Irdeto-provided operator ID and watermark ID length values. These values must match the license.
Store the license in AWS Secrets Manager and have the secret name available. You enter this identifier when you configure the watermarking settings. An invalid, expired, truncated, or unavailable license prevents the watermark from being applied.
Ensure that the IAM role that MediaLive assumes has `secretsmanager:GetSecretValue` permission for the license secret. For general information about the trusted-entity role, see [IAM permissions for MediaLive as a trusted entity](setting-up-trusted-entity.md). For the complete list of operations that the role might need, see [Create the trusted entity - complex option](setup-trusted-entity-complex.md).

**Topics**
+ [Setting up A/B video watermarking](ab-watermark-configure.md)
+ [Troubleshooting](ab-watermark-troubleshooting.md)