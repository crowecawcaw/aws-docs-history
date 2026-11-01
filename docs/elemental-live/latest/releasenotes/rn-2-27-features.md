

# New features in version 2.27 and 3.27
<a name="rn-2-27-features"></a>

The following sections describe the new features in each release of version 2.27 (3.27 for Conductor Live), with the newest release first. Version 2.27.1 (3.27.1) has no new features.

## New features in version 2.27.5 and 3.27.5
<a name="rn-2-27-features-5"></a>

Web interface – DVB subtitle type  
A new option lets you specify the DVB subtitle type. You can choose between `normal` and `hearing impaired` labels for DVB subtitle tracks.

HLS outputs – PDT tags in I-frame playlists  
Program date time (PDT) tags have been added to I-frame playlists, for compliance with the HLS specification.

## New features in version 2.27.4 and 3.27.4
<a name="rn-2-27-features-4"></a>

CMAF Ingest outputs – explicit frame rate  
CMAF Ingest outputs now require an explicit frame rate (numerator and denominator) for H.264 outputs. Previously, **Initialize from source** was allowed.

Web interface – MediaPackage v2 settings  
The CMAF Ingest output group settings now include an EMPv2 settings section when a MediaPackage v2 endpoint is configured.  
MediaPackage v2 destination settings now include these fields: HLS auto-select, HLS default, audio rendition sets, and audio group ID.

Updated video engine  
This release includes an updated video engine with general improvements to the quality of AVC and HEVC encoded video.

## New features in version 2.27.3 and 3.27.3
<a name="rn-2-27-features-3"></a>

Security updates  
This release includes updates that address potential security issues.

Maximum audio output encodes (GLV-6306)  
The maximum number of audio output encodes in one output group has increased from 16 to 32.

SMPTE 2110 with NMOS – multiple bitrates (GLV-6311)  
Elemental Live now supports SMPTE 2110 inputs that have different bitrates in the same event.

## New features in version 2.27.2 and 3.27.2
<a name="rn-2-27-features-2"></a>

### Color space conversion – support for 3D LUT files
<a name="rn-2-27-2-3d-luts"></a>

You can now configure an event that is set up for color conversion to use 3D LUT files for color correction. You provide a list of 3D LUT files. Each 3D LUT file contains color mapping information for a specific source and output combination. For example, one file contains information for converting Rec. 709 to HDR10.

**Rules for using 3D LUT files**
+ Source of the files – You must provide the 3D LUT files. Elemental Live doesn't have built-in files.
+ One file for each combination – You must provide a file for each source and output combination. For example, a file for converting Rec. 601 to HDR10.
+ Maximum of 8 files – You can provide a maximum of 8 files for each channel. This means that Elemental Live supports up to 8 source and output conversion combinations.
+ Global application – Elemental Live uses a specific file in all the outputs where that file applies. For example, if there is a file to convert Rec. 601 to HDR10, Elemental Live uses that file in every output that it applies to. You can't configure some outputs to use the standard mechanism for conversion.

**Rules for the contents of 3D LUT files**
+ Format – Each 3D LUT file must follow the `.cube` 3D LUT format.
+ Maximum of one file for each combination – You can provide only one 3D LUT file for each combination. You can't configure some outputs to use a different 3D LUT file. When Elemental Live reads the list of 3D LUT files, it uses the first file that it finds for a source and output combination.
+ HDR10 luminance – Elemental Live supports conversion of HDR10 content with a maximum luminance of 1000–4000 nits, but it supports only one maximum luminance. When Elemental Live reads the list of 3D LUT files, it uses the first file that it finds for each conversion from HDR10. For example, if you provide one file for 1000 nits and one file for 4000 nits, Elemental Live uses only the first file. Therefore, follow these guidelines:
  + Make sure that all the HDR10 content in all the inputs in one channel has the same maximum luminance. If a source has a different maximum luminance, Elemental Live converts the content, but the outputs have sub-optimal luminance.
  + In each 3D LUT file that converts from HDR10, make sure that the luminance handling is appropriate for the luminance of the source.

**To set up 3D LUT files**

1. Place the 3D LUT files in a location that Elemental Live can access:
   + A location that is local to the Elemental Live appliance. For example, `/data/assets/LUTS`.
   + A remote server that Elemental Live accesses through a mount point. For example, `/data/mnt/assets/LUTS`.
   + An Amazon S3 bucket. For example, `s3ssl://amzn-s3-demo-bucket/LUTS`.

1. On the Elemental Live web interface, open the event. On the **Global Processors** section, turn on **Color Mapping**.

1. Choose **Add Color Map** to display up to 8 lines. In each line, enter the following information:
   + The location of the 3D LUT file.
   + The input (source) color space that this file handles.
   + The output color space that this file handles. To set up a combination that works when converting to Dolby Vision 8.1, select HDR10 as the output color space.

1. Set up the inputs and the outputs in the usual way, as described in the [AWS Elemental Live User Guide](https://docs.aws.amazon.com/elemental-live/latest/ug/).

### Audio limits
<a name="rn-2-27-2-audio-limits"></a>

This release changes the following audio limits:

Audio inputs – limits for SMPTE 2110 audio inputs (GLV-5504)  
Previously, there was a limit of 16 audio channels in an SMPTE ST 2110-30 or SMPTE ST 2110-31 input stream. Elemental Live now supports up to the limits that are defined in Table 2 of SMPTE ST 2110-30:2017.

Audio outputs – limit for each event  
The maximum number of audio output encodes in a single event has increased from 20 to 32.

## New features in version 2.27.0 and 3.27.0
<a name="rn-2-27-features-0"></a>

### Dolby Digital Plus with Atmos – decode
<a name="rn-2-27-0-atmos"></a>

Elemental Live now supports decoding audio that is Dolby Digital Plus with Dolby Atmos (EAC3 Atmos). You can set up an EAC3 Atmos input to an EAC3 Atmos output in two ways:
+ Pass the audio through, as in earlier versions.
+ Re-encode the audio by choosing **EAC3 ATMOS** as the output codec. In this case, the Audio Decoder Package must be installed on the node.

Version 2.27.0 and later also use newer Dolby Digital libraries, which results in general improvements.

### EBU-TT-D captions (GLV-2573)
<a name="rn-2-27-0-ebu-tt-d"></a>

EBU-TT-D captions now include a new metadata section that conforms to the standard. For example:

```
<metadata>
  <ebuttm:documentMetadata>
    <ebuttm:conformsToStandard>urn:ebu:tt:distribution:2018-04</ebuttm:conformsToStandard>
    <ebuttm:documentOriginatingSystem>Elemental Media Engine(TM) Live 64-bit v2.27.0.0</ebuttm:documentOriginatingSystem>
  </ebuttm:documentMetadata>
</metadata>
```

### ID3 segment tagging in HLS (GLV-4956)
<a name="rn-2-27-0-id3-hls"></a>

HLS output groups now support ID3 segment tagging.

### Installer – user authentication (GLV-4468)
<a name="rn-2-27-0-installer-auth"></a>

The installer now includes options that enable or disable user authentication without authentication prompts. This change allows hands-free installs.
+ To install without enabling authentication, include the `--skip-auth` option.
+ To install with authentication enabled, include both the `--admin-login` and `--admin-password` options.

On an existing deployment, you have these options:
+ To change the configuration without changing the current user authentication status, enter **./configure --skip-auth**.
+ To enable or disable authentication, enter **./configure --config-auth**. The script prompts you to enable or disable authentication.

**Note**  
In earlier versions of the software, `--skip-all` skipped the user authentication prompts. Starting with version 2.27.0, `--skip-all` doesn't skip those prompts.

For help, search the knowledge articles or open a case in the [AWS Elemental Support Center](https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/supportcenter).

### Installer – port restrictions (GLV-4464)
<a name="rn-2-27-0-installer-ports"></a>

When the firewall is enabled, the installer now restricts ports 22, 80, and 443 to private subnets by default. The default private subnets are `10.0.0.0/8`, `172.16.0.0/12`, and `192.168.0.0/16`.
+ To customize the CIDR ranges for port restrictions, use the `--cidrs` option in the install command, or perform an interactive install.
+ To use the default configuration, use the `--skip-all` or `--skip-cidrs` option.

For help, search the knowledge articles or open a case in the [AWS Elemental Support Center](https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/supportcenter).

### Licenses (GLV-4322)
<a name="rn-2-27-0-licenses"></a>

The JPEG XS license is now restricted to 75 events running at the same time. Contact AWS Elemental Support if you run into issues with this restriction.

### Logging (GLV-5129)
<a name="rn-2-27-0-logging"></a>

Video backend logging now includes more detail about the configuration of the color corrector, scaler, and encodes.

### NMOS next generation – 2110 receiver groups (GLV-3754)
<a name="rn-2-27-0-receiver-groups"></a>

Elemental Live now supports 2110 receiver groups as a way to handle NMOS-controlled 2110 inputs. You create a 2110 receiver group and add 2110 streams to it. You then create or modify an event to use the 2110 receiver group, instead of creating 2110 inputs directly in the event.

The 2110 receiver groups are independent of the event. You can modify an event to detach a 2110 receiver group, and the 2110 receiver group continues to exist. You can also modify a 2110 receiver group without modifying the event. You can modify the 2110 receiver group when the associated event, if there is one, is running, which lets you perform NMOS receiver patching. For more information, see [NMOS next generation – receiver patching with two modes (GLV-4965)](#rn-2-27-0-patching-modes).

**To set up a 2110 receiver group on the web interface**

1. On the main menu, choose **Settings**, then choose **Input Devices**. Choose **Create 2110 Receiver Group**.

1. In the **SMPTE 2110 Receiver Groups** section, in the **NMOS Label** field, enter a name for the 2110 receiver group.

1. Complete the **Video Receiver** row to configure the video stream: complete the **NMOS Label** field, the **Interface** field (for example, `ETH6`), and the optional **Secondary Interface** field.

1. To add audio or ancillary streams, choose **Add Audio SDP** or **Add Ancillary SDP**, and complete each **Label** row that appears.

1. Choose **Save 2110 Receiver Groups**.

**To use the 2110 receiver group in an event that you are creating or editing**

1. Choose **Add Input**. In the selector field, choose the 2110 receiver group that you created.

1. Choose **Add Input** again and choose the same 2110 receiver group.

1. For both of the 2110 receiver group inputs, choose **Advanced**, and turn on **NMOS Patching Pair**. Each 2110 receiver group input needs this additional patching pair input.

### NMOS next generation – receiver patching with two modes (GLV-4965)
<a name="rn-2-27-0-patching-modes"></a>

Before version 2.27.0, Elemental Live supported only break-before-make receiver patching. Starting with version 2.27.0, Elemental Live also supports make-before-break receiver patching.
+ Break-before-make (BBM) – Elemental Live tears down the 2110 input before it starts to build up the new input processing. The benefit of this mode is that it doesn't require extra network bandwidth when patching. The drawback is that streams are patched one by one, which results in short periods of video fill and audio silence.

  Version 2.27.0 includes one change in the implementation: you must create a shadow input for each 2110 receiver group input. Elemental Live tears down the first 2110 input, then starts to build up the shadow 2110 input. For more information, see [Shadow inputs are required for 2110 receiver group inputs (GLV-4730)](#rn-2-27-0-shadow-inputs).
+ Make-before-break (MBB) – Elemental Live builds up the second input and makes it ready before it seamlessly switches from the original input to the new input. This mode requires double the network bandwidth while the second input is being prepared.

**To configure BBM or MBB**

1. On the main menu, choose **Settings**, then choose **NMOS**.

1. In **Enable NMOS Access**, choose **Yes**. More fields appear.

1. In the **Use make-before-break for NMOS Receiver patching** field, choose a value:
   + **Yes** – Use MBB. This is the default.
   + **No** – Use BBM.

### Shadow inputs are required for 2110 receiver group inputs (GLV-4730)
<a name="rn-2-27-0-shadow-inputs"></a>

To use a 2110 receiver group input, you must create a shadow input for that input. This requirement applies to both break-before-make (BBM) and make-before-break (MBB) patching.

**To set up a shadow input in an event that you are creating or editing**

1. Go to the input that uses a 2110 receiver group.

1. Find the **NMOS Patching Pair** field, which is above the **Add Failover Condition** button.

1. Set the **NMOS Patching Pair** field to **Yes**.

### Web interface and API support for 2110 receiver groups (GLV-3736)
<a name="rn-2-27-0-nmos-api"></a>

2110 receiver groups are exposed in the NMOS Node APIs. You can disable NMOS support, including 2110 receiver groups, through the NMOS settings API or the web interface.

### TLS (GLV-4695, GLV-3389)
<a name="rn-2-27-0-tls"></a>

TLS handling has been improved. The cryptographic security for SSL/TLS connections has been strengthened.