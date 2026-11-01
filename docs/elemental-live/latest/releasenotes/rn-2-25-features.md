

# New features in version 2.25 and 3.25
<a name="rn-2-25-features"></a>

## New features in Elemental Live and Statmux 2.25
<a name="rn-2-25-features-live"></a>

This release includes the following new features.

### Stream ID field in SRT outputs (SOCK-38864)
<a name="rn-2-25-features-live-srt-stream-id"></a>

The SRT output in the Reliable TS output group now includes the **Stream ID** field.

### Default passwords (GLV-1758)
<a name="rn-2-25-features-live-default-passwords"></a>

There is a change to the password rules for the operating system root password. Starting with version 2.25.6, if you kickstart the operating system, you must change the root password from the default value.

This password requirement is in addition to the current requirement that you always change the default password for the `elemental` user.

### Dolby Vision and tvOS devices and operating systems (GLV-722)
<a name="rn-2-25-features-live-dolby-vision-tvos"></a>

A change has been made to the HLS manifest, to support Dolby Vision 8.1 with tvOS devices and operating systems. Previously, the `#EXT-X-STREAM-INF` tags were split into two lines for video. Starting with version 2.25.5, Elemental Live signals Dolby Vision 8.1 with one `#EXT-X-STREAM-INF` tag that includes both the `CODECS` and `SUPPLEMENTAL-CODECS` attributes.

### RTMP outputs and fill behavior (SOCK-38971)
<a name="rn-2-25-features-live-rtmp-fill"></a>

There is a change to how you can configure an RTMP output group when you have set up the video for constant bitrate.

Elemental Live might achieve a constant bitrate for the video by including filler units (FILL NAL units) within the elementary video stream. Elemental Live does this when the video is not complex and doesn't need to use the full specified bitrate.

Before version 2.25.2, in an RTMP output group, Elemental Live stripped the filler units from the output video. Stripping out the units results in video that isn't really a constant bitrate. This variable bitrate can cause problems for some downstream systems.

With version 2.25.2, an RTMP output group includes the **Include Filler NAL Units** field. This field lets you control whether to keep or strip out the filler. The field has an effect only when you have set up the video for CBR. It is ignored with other bitrates.

**Setup in the web interface**

In the Elemental Live event, in **Output Groups**, choose the **Adobe RTMP** tab. Find the **Include Filler NAL units** field, and choose the preferred option. The options are **Auto**, **Drop** (the default), and **Include**. We recommend that you choose **Auto**.
+ If you choose **Auto** and you find that the video quality drops, then change the value to **Include**.
+ If you know that your downstream system definitely can't handle a bitrate that varies a lot over time, then choose **Include**. Elemental Live includes the filler so that the bitrate of the entire stream is constant.
+ If you know that your video quality doesn't vary in complexity, then you might want to choose **Drop**, to clearly define the behavior that you want.

**API change**

The new field is located in the XML file as follows:

```
<output_group>
     <rtmp_group_settings>
          <include_filler_nal_units>
```

### Audio attenuation for AC3 (SOCK-39052)
<a name="rn-2-25-features-live-ac3-attenuation"></a>

Elemental Live now supports audio attenuation for AC3 (Dolby Digital) output audio when the coding mode is 3/2 LFE. Previously, this feature was supported only with EAC3 (Dolby Digital Plus).

### KLV metadata (SOCK-28219)
<a name="rn-2-25-features-live-klv"></a>

Elemental Live now supports ingest of KLV data included in the SMPTE-2038 in a transport stream. The ingested metadata can then be passed through in an HLS (with a TS container) output group or a UDP/TS output group. Previously, passthrough was supported only on UDP/TS outputs.

To pass through the KLV metadata, follow these steps:

1. In the input, expand the **Advanced** section and enable **Prefer SMPTE 2038**.

1. In the HLS or UDP/TS output group, expand the **Advanced** section and set these fields:
   + **KLV Passthrough** – Enable this field.
   + **KLV PID** – Enter the PID or PIDs for the metadata. Valid values are in the range 32 to 8182. Enter the value in decimal or hexadecimal. Multiple values are accepted, and can be entered in ranges and/or by comma separation.

In a UDP/TS output group, these settings are in the m2ts container. In an HLS output group, they are in the m3u8Settings container.

**API change**

In the XML file, the fields are located as follows:
+ `<prefer_smpte2038>` is located at `<input>`.
+ `<klv_passthrough>` is located at `<output_group><output>` under `<m3u8_settings>` or `<m2ts_settings>`.
+ `<klv_data_pids>` is located at `<output_group><output>` under `<m3u8_settings>` or `<m2ts_settings>`.

### Delivering to AWS Elemental MediaPackage using SigV4 credentials
<a name="rn-2-25-features-live-mediapackage-sigv4"></a>

Elemental Live now supports SigV4 authentication for outputs to AWS Elemental MediaPackage Live v2. MediaPackage v2 supports both HLS and low-latency HLS.

There are no changes to the API for this feature.

The [AWS Elemental Live User Guide](https://docs.aws.amazon.com/elemental-live/latest/ug/) has been updated to include information about this output.

### Low latency workflows using AWS Elemental MediaPackage
<a name="rn-2-25-features-live-mediapackage-low-latency"></a>

If you are delivering HLS output to MediaPackage that is using MediaPackage v2, you can implement a glass-to-glass low latency HLS workflow that uses AWS Elemental Live for encoding and AWS Elemental MediaPackage as the origin server. For this workflow, there are specific setup steps in both Elemental Live and MediaPackage:
+ The Elemental Live event must have a short segment: 1 second. If the segment length is longer, you will probably not achieve end-to-end low latency. Other fields can also affect latency.
+ The MediaPackage channel must use MediaPackage v2.

There are no changes to the API for this feature.

The [AWS Elemental Live User Guide](https://docs.aws.amazon.com/elemental-live/latest/ug/) has been updated to include information about this output.

### Improved video quality
<a name="rn-2-25-features-live-video-quality"></a>

Version 2.25.0 includes enhancements that result in better video quality.

## New features in Conductor Live 3.25
<a name="rn-2-25-features-cl3"></a>

This release includes the following new features.

### Default passwords (GLV-1758)
<a name="rn-2-25-features-cl3-default-passwords"></a>

There is a change to the password rules for the operating system root password. Starting with version 2.25.6, if you kickstart the operating system, you must change the root password from the default value.

This password requirement is in addition to the current requirement that you always change the default password for the `elemental` user.