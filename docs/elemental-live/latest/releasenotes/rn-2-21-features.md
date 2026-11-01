

# New features in version 2.21 and 3.21
<a name="rn-2-21-features"></a>

This topic describes the new features in version 2.21 (3.21 for Conductor Live).

## New features in Elemental Live and Statmux 2.21
<a name="rn-2-21-features-live"></a>

Elemental Live and Statmux 2.21 include the following new features.

### SMPTE ST 2110-22 JPEG XS decoding for inputs and outputs
<a name="rn-2-21-jpegxs-2110"></a>

Elemental Live now offers an add-on license for the JPEG XS codec for SMPTE ST 2110-22 inputs and outputs. Using this codec provides between 1:2 and 1:12 compression.

For an input, support for this codec means that Elemental Live can ingest SMPTE 2110 streams encoded with JPEG XS. Elemental Live automatically detects the codec. No user setup is required.

To use this codec in a SMPTE 2110 output, on the **Video** tab, select **JPEG XS** in **Video Codec**. You can use a compression ratio between 1:2 and 1:12.

### Dynamic ARIB audio stereo output
<a name="rn-2-21-arib-stereo"></a>

There is a new option in the audio stream for an output, available when the input is ARIB and the output is ARIB. In the **ARIB Dynamic Audio** field, there is a **Forced Stereo** option. This option automatically remixes the audio into stereo. It can convert any coding mode to stereo. If upmixing, Elemental Live repeats the mono input in both stereo channels. If downmixing, Elemental Live selects the first two channels from the input and discards other channels.

### SCTE 35 splice insert API support for new tags
<a name="rn-2-21-scte35-splice"></a>

Added support in the API for the following tags in Elemental Live splice insert:
+ `unique_program_id`
+ `avail_num`
+ `avails_expected`

### AWS Elemental MediaConnect input support
<a name="rn-2-21-mediaconnect"></a>

Elemental Live now includes support for inputs from AWS Elemental MediaConnect using ARN based specifiers. You can create an output from MediaConnect using the SRT listener protocol, and Elemental Live will parse required information from the MediaConnect flow ARN and MediaConnect output ARN to ingest the SRT source. AES encryption is optional. AWS Elemental MediaConnect inputs can also be configured and managed in Conductor Live.

### NMOS IS-04 and IS-05 support for SMPTE ST 2022-7 seamless protection switching for SMPTE ST 2110 inputs
<a name="rn-2-21-nmos-2022-7"></a>

Elemental Live has expanded existing NMOS IS-04 Device Discovery and IS-05 Device Connection Management to support SMPTE ST 2022-7 seamless protection switching for SMPTE ST 2110 inputs.

### RiverMax SDK upgrade
<a name="rn-2-21-rivermax"></a>

Elemental Live has upgraded to version 1.5.23 of the Mellanox RiverMax SDK.

### Power supply alerts
<a name="rn-2-21-power-alerts"></a>

When a power supply issue is detected, Elemental Live and Statmux will now display an alert in the web interface and send an SNMP trap. If Conductor Live is present, the alert is also visible there.

### Conductor Live MPTS Channel web interface updates
<a name="rn-2-21-cl-mpts-ui"></a>

On the MPTS Channel page of Conductor Live, you can now view and edit TS Endpoints, Complexity Endpoints, and Rate Allocation Endpoints for Live to Statmux communication. By default, this occurs through UDP multicast on ports 5000 to 5055.

### SRT inputs
<a name="rn-2-21-srt-inputs"></a>

Elemental Live introduces caller/listener mode support for Secure Reliable Transport (SRT) inputs, where Elemental Live is the caller and the SRT source is the listener. You can now receive secure, reliable, low latency video sources with protection against packet loss. SRT security is provided through optional Advanced Encryption Standard (AES) encryption of messages.

**To configure an event for an SRT input**

1. For the input type, select **Secure Reliable Transport** and enter a name for the input.

1. In the **Network Location** field, enter the URI of the SRT to ingest. Specify a host name and port that begins with `srt://`. For example, `srt://192.168.1.2:5000`.

1. (Optional) In the **Interface** field, enter a network interface, such as `eth1`. If you leave this field blank, the system routing table selects an interface for you.

1. (Optional) In the **Latency** field, enter the minimum number of milliseconds that the SRT sender should buffer a packet without receiving an acknowledgement before discarding it. For example, 300.
**Note**  
This is not guaranteed to be the latency value used, because SRT uses the larger of the latency values requested by the caller and listener during the connection handshake. If you do not enter a value here, the default is 120 ms.

1. In the **Encryption** field, select an encryption key length for the SRT media stream.
**Note**  
You have the option to enter **None**. If you do this, you must leave the **Passphrase** field blank.

1. In the **Passphrase** field, enter a passphrase between 10 and 72 characters for the SRT sender and receiver.
**Important**  
If you entered a value other than **None** in the **Encryption** field, you must enter a value here. If you entered **None** in the **Encryption** field, you must leave this field blank.

1. (Optional) In the **Stream ID** field, enter a unique identifier between 1 and 512 characters for the SRT sender to use during the connection handshake.

### Dolby Vision certification
<a name="rn-2-21-dolby-vision"></a>

Elemental Live is now Dolby Vision certified for profile 5 and profile 8.1.

### Auto adaptive quantization
<a name="rn-2-21-auto-aq"></a>

A new default and recommended **Auto** setting is now available for Adaptive Quantization. This setting applies to AVC encoding. The **Auto** setting uses machine learning techniques to select the optimal settings for Adaptive Quantization, Temporal AQ, Spatial AQ, and Flicker AQ. With this setting, AQ strengths can now vary across a video stream instead of remaining constant.

### Auto QVBR quality level
<a name="rn-2-21-auto-qvbr"></a>

You can now use **Auto** mode to automatically set quality level in QVBR rate control mode for AVC and HEVC. **Auto** is the new default and recommended setting. An algorithm determines the best setting for your content.

### SPTS output monitoring in Statmux
<a name="rn-2-21-spts-monitoring"></a>

Statmux now allows you to add a secondary SPTS output for monitoring use cases.

### HTML5 motion graphics
<a name="rn-2-21-html5-mg"></a>

With the motion graphics add-on pack, you can now use Elemental Live to overlay HTML motion graphics on video outputs.

**To set up a motion graphics overlay**

1. From the Elemental Live event page, set **Motion Image Inserter** to **ON**.

1. Choose **HTML** as the **Insertion Mode**, and enter the URL of the page you want to overlay in the **Input** field.

1. (Optional) Select the **Overlay Active** check box if you want HTML overlays to start activated.

1. (Optional) Select the check boxes to **Enable REST Control** and **Enable SCTE-35 Control**.
**Note**  
For SCTE-35 controlled events, SCTE-35 deactivate messages only turn off overlays that were activated with this control. SCTE-35 deactivate does not turn off overlays that were activated in other ways.

To run a motion graphics overlay event, start an event that was set up using this motion graphics overlay method.

### SDI performance enhancements
<a name="rn-2-21-sdi-perf"></a>

SDI capture cards have upgraded firmware, saving significant bandwidth and CPU utilization for workflows that convert 4:2:2 inputs to 4:2:0 outputs.

**Important**  
Firmware updates require a full power cycle after install before using Elemental Live.

## New features in Conductor Live 3.21
<a name="rn-2-21-features-cl3"></a>

Conductor Live 3.21 includes the following new features. These features are also available in Elemental Live and Statmux 2.21.

### AWS Elemental MediaConnect input support
<a name="rn-2-21-cl3-mediaconnect"></a>

Elemental Live now includes support for inputs from AWS Elemental MediaConnect using ARN based specifiers. You can create an output from MediaConnect using the SRT listener protocol, and Elemental Live will parse required information from the MediaConnect flow ARN and MediaConnect output ARN to ingest the SRT source. AES encryption is optional. AWS Elemental MediaConnect inputs can also be configured and managed in Conductor Live.

### Power supply alerts
<a name="rn-2-21-cl3-power-alerts"></a>

When a power supply issue is detected, Elemental Live and Statmux will now display an alert in the web interface and send an SNMP trap. If Conductor Live is present, the alert is also visible there.

### Conductor Live MPTS Channel web interface updates
<a name="rn-2-21-cl3-mpts-ui"></a>

On the MPTS Channel page of Conductor Live, you can now view and edit TS Endpoints, Complexity Endpoints, and Rate Allocation Endpoints for Live to Statmux communication. By default, this occurs through UDP multicast on ports 5000 to 5055.