

# New features in version 2.23 and 3.23
<a name="rn-2-23-features"></a>

This version includes the following new features.

## New features in Elemental Live and Statmux 2.23
<a name="rn-2-23-features-live"></a>

Elemental Live and Statmux version 2.23 include the following new features.

### Passthrough in an MPTS
<a name="rn-2-23-mpts-passthrough"></a>

Version 2.23.4 (3.23.4 for Conductor Live) introduces support for two MPTS passthrough features:
+ **Program passthrough** – An MPTS can now include programs that are encoded by third-party encoders. The passthrough program must be a CBR.
+ **Passthrough of a stream that is an SI/PSI table** – An MPTS can now include a stream that corresponds to an SI/PSI table. To support this feature, Statmux includes the ability to suppress any SI/PSI table that Statmux normally generates in the MPTS.

For information about these features, see [Including passthrough programs](https://docs.aws.amazon.com/elemental-cl3/latest/ug/mpts-passthrough-program.html), [Passing through custom streams](https://docs.aws.amazon.com/elemental-cl3/latest/ug/mpts-passthrough-high-pids.html), and [Passing through SI/PSI tables](https://docs.aws.amazon.com/elemental-cl3/latest/ug/mpts-passthrough-PSI-pids.html).

### Video enhancements
<a name="rn-2-23-video-enhancements"></a>

Enhancements have been made to these existing fields that control video quality:
+ **Input** > **Video Selector** > **Filter Strength** field: This field now includes an **Auto** value that lets Elemental Live choose the best strength. We recommend choosing **Auto** as the initial value. This field controls a filter on the input side.
+ **Outputs** > **Stream** > **Video** > **Preprocessors** > **Noise Reducer**: When the **Filter** field is set to **Sharpen**, there are now different values in the **Strength** field that set the strength of the sharpen filter. This filter previously had an on/off choice, to sharpen the edges or not. The field now has more values: 0 (off) and 1 (low) up to 3 (high). The new default is 1 (low). This field is a filter on the output side.

### Logging utility
<a name="rn-2-23-logging-utility"></a>

All the products in the AWS Elemental Live family now include a utility that lets you capture and deliver a wide array of diagnostics data, and send the data to AWS Elemental Support for troubleshooting purposes. The utility is available on Conductor Live, Elemental Live, and Statmux nodes.

For more information, search the knowledge articles in the [AWS Elemental Support Center](https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/supportcenter) for *How to collect diagnostics data with elemental log collector utility*.

### 12G SDI input
<a name="rn-2-23-12g-sdi"></a>

AWS Elemental Live now supports ingest of uncompressed 12G-SDI content. Using this input type means that you no longer need to implement a quadrant ingest of 4 x 3G to ingest a 12G source.

This input type is enabled only for AWS Elemental Live appliances L859 and L889 that include a 12G SDI card. The new appliances provide maximum flexibility because they let you implement SD-SDI inputs, HD-SDI inputs, 3G-SDI inputs, and 12G-SDI inputs.

With a 12G-SDI input, you can implement the following workflows:
+ 1 x 4K HEVC workflow, on the L859 appliance
+ 2 x 4K HEVC workflow, on the L889 appliance
+ 1 x 4K HEVC ABR stack, on the L889 appliance

These maximums apply even though the card includes four ports. None of these appliances support ingest of four 12G sources at one time.

There is a new section about 12G inputs in the Inputs section of the [AWS Elemental Live User Guide](https://docs.aws.amazon.com/elemental-live/latest/ug/).

### Performance optimizations for SMPTE 2110 inputs
<a name="rn-2-23-perf-2110"></a>

Version 2.23.3 includes performance optimizations for SMPTE 2110 inputs and SMPTE 2022-6 inputs. These inputs require an appliance that includes the Mellanox 25 GbE card. These optimizations improve read density at the device interface. Customers with SMPTE 2110 inputs and SMPTE 2022-6 inputs will see density improvements for some workflows.

If you already implement SMPTE 2110 inputs or outputs, or SMPTE 2022-6 inputs, you might need to perform an extra step after you upgrade to Elemental Live version 2.23.3. For more details, see [Changes to usage of the Mellanox card](rn-2-23-essential.md#rn-2-23-essential-mellanox).

### Support for auto adaptive quantization with HEVC outputs
<a name="rn-2-23-hevc-aq"></a>

Version 2.21 of AWS Elemental Live introduced auto adaptive quantization for AVC outputs. This feature is now also the default for HEVC outputs.

The **Auto** setting uses machine learning techniques to select the optimal settings for Adaptive Quantization, Temporal AQ, Spatial AQ, and Flicker AQ. With this setting, AQ strengths can now vary across a video stream instead of remaining constant.

### Enhancement for Teletext source captions
<a name="rn-2-23-teletext-captions"></a>

Previously, there was a problem with how Elemental Live handled some characters when converting Teletext source captions to another format. To solve this problem, the **Input** > **Captions** selector section of the event now includes a **Language code** field when the source captions are set to Teletext. When Elemental Live has information about the language, it can select the correct character set to use when converting.

Before you use this feature, see issue SOCK-38330 in the newly identified issues for version 2.23.

### Latency improvements for SMPTE 2110 outputs
<a name="rn-2-23-2110-latency"></a>

Improvements continue to be made to reduce the latency of SMPTE 2110 outputs. For Live to EMX to Live workloads, streamlining audio and video packet sends has reduced latency by up to 50%. For 1080p60 outputs, latency has been reduced from 500ms to 250ms.

### Installing and upgrading – configuring OCR conversion
<a name="rn-2-23-ocr-conversion"></a>

There are three new options for enabling OCR when you install, upgrade, or configure Live:
+ The first option is to skip OCR prompts and not enable OCR.
+ The second option is for a node with an internet connection. The install includes a step to download OCR libraries.
+ The third option is for a node with no connection. The install uses libraries that you previously downloaded and copied to the node.

The [AWS Elemental Live Installation Guide](https://docs.aws.amazon.com/elemental-live/latest/installguide/) has been updated with this information.

### Input switching using a POIS
<a name="rn-2-23-pois-input-switching"></a>

AWS Elemental Live includes two features for switching inputs using a POIS.

#### Virtual input switching
<a name="rn-2-23-virtual-input-switching"></a>

AWS Elemental Live version 2.20.2 introduced the virtual input switching feature. The feature lets you set up so that a POIS controls switching from one event to another. This method has these key features:
+ Support for input switching based on SCTE-35 messages in the input.
+ Support for the POIS to send unsolicited requests to switch inputs.

#### Asynchronous input switching with ESAM
<a name="rn-2-23-async-input-switching-esam"></a>

Version 2.23.0 introduces the asynchronous input switching feature. You can set up any event so that a POIS server can send asynchronous input switching requests to Elemental Live. The requests are handled using the ESAM protocol. You can set up for POIS input switching with the following types of inputs:
+ TS inputs from an MPTS. These inputs let you include live sources in the event.
+ File inputs. These inputs let you include VOD sources.

For more information about these features, see the [AWS Elemental Live User Guide](https://docs.aws.amazon.com/elemental-live/latest/ug/).

### Dialnorm for Dolby inputs
<a name="rn-2-23-dialnorm-dolby"></a>

A new environment variable lets you control the processing of Dolby audio inputs. This variable is useful for events that have a Dolby input and a non-Dolby output. In these scenarios, you can't change the dialnorm on the output. But you can set this environment variable to change it on the input side, to reduce the loudness of the entire output.

To use this feature, set the environment variable `DOLBY_DYNAMIC_RANGE_CONTROL_MODE`. Set the variable to one of these values:
+ `1`: Sets the dialnorm of the input audio to -20 decibels.
+ `2`: Sets the dialnorm of the input audio to -31 decibels.
+ `3`: Passes through the dialnorm of the input audio.

To set the variable, search the knowledge articles in the [AWS Elemental Support Center](https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/supportcenter) for *How to add environment variables in CentOS 7/RHEL 7 from the CLI*. You must have an AWS account to access the AWS Elemental Support Center.

If you don't set this variable, Live sets the dialnorm of the input audio to -20 decibels, which is the same value as setting `1` in the environment variable.

### Dolby Digital Plus and fourCC value
<a name="rn-2-23-eac3-fourcc"></a>

A new environment variable lets you specify the fourCC value for EAC3 (Dolby Digital Plus) signaling for a TS output.

To use this feature, set the environment variable `FORCE_EAC3_FOURCC_TS_SIGNALING`. Set the variable to one of these values:
+ `Enabled`: Sets the value to `EAC3`.
+ `Disabled`: Sets the value to `ec-3`.

To set the variable, search the knowledge articles in the [AWS Elemental Support Center](https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/supportcenter) for *How to add environment variables in CentOS 7/RHEL 7 from the CLI*. You must have an AWS account to access the AWS Elemental Support Center.

If you don't set up this environment variable, Live sets the fourCC value to `ec-3`.

## New features in Conductor Live 3.23
<a name="rn-2-23-features-cl3"></a>

There are no new features for Conductor Live in this version.