

# New features in version 2.26 and 3.26
<a name="rn-2-26-features"></a>

## New features in Elemental Live and Statmux 2.26
<a name="rn-2-26-features-live"></a>

This release includes the following new features.

### Access to /home/elemental (GLV-2979)
<a name="rn-2-26-home-permissions"></a>

**Note**  
The following permissions apply only to a fresh install of AWS Elemental software, starting with Elemental Live 2.26.4 and Conductor Live 3.26.4.

The default folder permissions for `/home/elemental` have been changed from `755` to `750`. This means that the folder is no longer world readable and writable.

The default UMASK has also been changed from `022` to `027` in `/etc/login.defs`. This means that any new files or directories that are created on the system are no longer world readable.

### Accessibility signaling (GLV-3177)
<a name="rn-2-26-accessibility-signaling"></a>

In audio and captions in a CMAF Ingest output, you can now include accessibility data. This data describes the type of accessibility that the encode represents. For example, an audio track might actually be a spoken description of what's happening in the video. Or a captions track might provide a written translation (into another language) of the speech in the content. Accessibility data is also known as accessibility signaling.

Elemental Live supports accessibility signaling using DASH role audio, DASH role captions, and DVB DASH accessibility (for both audio and captions).

You set up for accessibility signaling in the individual audio and captions encodes in each CMAF Ingest output group.

### CMAF Ingest output group (GLV-3172)
<a name="rn-2-26-cmaf-ingest"></a>

CMAF Ingest output groups are now supported on Elemental Live.

### NMOS – New parameter for NMOS manifest (GLV-4655)
<a name="rn-2-26-nmos-manifest-param"></a>

The NMOS `node-config.json` file contains a new parameter, `manifest_href_base_url`:
+ **Description** – The URL for the HREF in the NMOS manifest.
+ **Default value** – `https://<name of Live machine>`

### NMOS controlled by Conductor Live
<a name="rn-2-26-nmos-conductor"></a>

Elemental Live now supports NMOS events that are controlled by Conductor Live. Support for this control includes failover when a Live node fails. The new implementation allows you to set up and manage the NMOS configuration independently of the event that will use that configuration. In other words, the configuration is decoupled from the event.

### Performance – Improved density on AWS Elemental Live 98x appliances
<a name="rn-2-26-density-98x"></a>

This version of AWS Elemental Live includes density improvements in SDI UHD inputs on AWS Elemental Live 98x appliances.

### Routers and HTTPS (GLV-2903)
<a name="rn-2-26-routers-https"></a>

Routes under `/routers` now require authentication when user authentication is enabled.

In addition, the `/settings/cluster` route has been removed from Elemental Live because clustering is handled by Conductor Live.

### SCP disabled by default (GLV-2805)
<a name="rn-2-26-scp-disabled"></a>

Starting with kickstart version `5.9.29` (which aligns with Elemental Live 2.26.4, Statmux 2.26.4, and Conductor Live 3.26.4), the AWS Elemental software now disables support for SCP by default. We have made this change because SCP has been deprecated in RHEL 9.

For more details, see [OpenSSH SCP deprecation in RHEL 9: What you need to know](https://www.redhat.com/en/blog/openssh-scp-deprecation-rhel-9-what-you-need-know) on the Red Hat website.

### SDI – Configuring SDI devices (GLV-3658)
<a name="rn-2-26-sdi-config"></a>

You can now configure an SDI input device name from the web interface.

### SMPTE 2110 input performance (GLV-3839)
<a name="rn-2-26-2110-performance"></a>

With SMPTE 2110 inputs, you no longer have to alternate between primary and secondary interfaces to ensure maximum performance.

### Support for SSSD in RHEL 9 (GLV-3721)
<a name="rn-2-26-sssd"></a>

Elemental Live now provides packages to support SSSD in RHEL 9. For detailed instructions, see the knowledge article with the title *How to integrate RHEL 9 Elemental Live appliance with Active Directory using SSSD* in the [AWS Elemental Support Center](https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/supportcenter).

### Tiled media
<a name="rn-2-26-tiled-media"></a>

AWS Elemental Live now supports the tiled media feature.

### Timecodes
<a name="rn-2-26-timecodes"></a>

AWS Elemental Live now includes a **Program-Date-Time-Clock** field. This field lets you set the PDT clock to **System Clock**, in order to automatically resynchronize PDT to the wall clock when PDT drifts.

The default value for this field is **Initialize From Output Timecode**, which means that there is no automatic resynchronization of PDT.

### Upgrade – Improvement to the process for upgrading a standalone Live node (GLV-3786)
<a name="rn-2-26-upgrade-standalone"></a>

The events on a standalone Elemental Live node will now restart automatically if you intentionally stop the `elemental_se` service. You might shut down, for example, to perform a software upgrade. When you restart `elemental_se`, the events that were previously running will automatically restart.

This change doesn't apply to channels that are managed through Conductor Live. Those channels won't automatically resume, but instead will continue to use the failover feature of Conductor Live. In other words, when you stop `elemental_se` on node A, the events fail over to a backup node. When you restart `elemental_se` on node A, the events continue to run on the backup node.

### Video quality – Bandwidth reduction filter (GLV-3746)
<a name="rn-2-26-brf"></a>

Bandwidth Reduction Filtering (BRF) is now available as a video pre-processor. BRF is an in-loop filter that is designed to increase compression efficiency, allowing you to reduce output bitrates while maintaining the same or a similar picture quality. We recommend that you set BRF to **Auto** and, if desired, test each of the post sharpening strengths, starting with the lowest strength.

### Virtual input switching – Improvement to virtual input switching (GLV-3467)
<a name="rn-2-26-virtual-input-switching"></a>

We have made internal improvements to input switching that mean that when a switch occurs, black video will no longer occur for a few frames.

### Video quality improvements
<a name="rn-2-26-video-quality"></a>

This version of AWS Elemental Live introduces core improvements to video quality in HEVC outputs, specifically in the handling of dark scenes and moving objects.

### Zixi outputs – SDK for Zixi outputs (GLV-929)
<a name="rn-2-26-zixi-sdk"></a>

Elemental Live now implements version 16.10.44864 of the Zixi Feeder SDK.

## New features in Conductor Live 3.26
<a name="rn-2-26-features-cl3"></a>

These release notes don't list separate new features for Conductor Live 3.26. Some of the features in the previous section, such as NMOS controlled by Conductor Live, also apply to Conductor Live 3.26.