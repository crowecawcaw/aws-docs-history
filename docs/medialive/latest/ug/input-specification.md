

# Input specifications settings

 

The **Input Specifications** settings include three fields that characterize the video in the input that you intend to use with this MediaLive channel. The fields are the following: 
+ Input codec
+ Input resolution
+ Maximum input bitrate 

You should have obtained information about these video characteristics when you [assessed the upstream system](evaluate-upstream-system.md) for each input source.

## How MediaLive uses this information
<a name="input-specification-how-used"></a>

MediaLive uses these values for billing and resource allocation purposes.
+ For billing, MediaLive uses these fields to calculate the charges that you will incur on the input side. You pay for the option that you specify. For example, if you specify HD but the inputs are all actually SD, you will still be charged for HD. 
+ For resource allocation, MediaLive uses these fields to allocate processing resources when you run this channel. If you don't choose the correct option, MediaLive might not allocate sufficient processing resources. Insufficient processing resources might mean that your channel output starts to degrade when the channel is running.

MediaLive doesn't use these values to determine what is actually in the video for decoding purposes. At ingest time, it still inspects the video to detect the source codec, resolution, and bitrate. 

## Completing the settings – option A
<a name="input-specification-option-a"></a>

Follow this procedure if you will run the channel in the AWS Cloud, not in a [MediaLive Anywhere cluster](setup-emla.md).

**Note**  
If the channel ingests JPEG XS (TR-07) video, don't follow this procedure. See [Completing the settings – JPEG XS (TR-07)](#input-specification-jpegxs).

1. Find the following codec, resolution, and bitrate:
   + Find the most resource-intensive codec among all the inputs. The codecs, from least to most intensive, are MPEG-2, then AVC, then HEVC. Make a note of the codec. The input it appears in isn't relevant.
   + Find the highest resolution tier among all the inputs. The tiers, from lowest to highest, are SD, HD, UHD. Make a note of the tier. The input it appears in isn't relevant. 
   + Find the highest bitrate among all the inputs. Make a note of the bitrate. The input it appears in isn't relevant.

1. For each field, choose an option that meets or exceeds the value you identified for that field. 

   Follow these tips: 
   + If you aren't sure about the processing requirements of your inputs, choose a higher option. For example, if you aren't sure of the bitrate and you are trying to choose between 10 Mbps and 20 Mbps, then choose 20 Mbps, to be on the safe side. Or if you aren't sure if your inputs use AVC (H.264) or HEVC (H.265), then choose HEVC. 
   + If your channel contains only one input and it's from an AWS Elemental Link device, complete the fields so that MediaLive allocates resources correctly. 

     Then make sure that you [configure the **Input resolution **in the device](device-edit.md), so that MediaLive calculates the billing correctly.
**Note**  
If the input resolution is HD and the device is a Link UHD, make sure that you [configure the **Input resolution **in the device](device-edit.md) to make sure that you don't get charged UHD rates.

## Completing the settings – option B
<a name="input-specification-option-b"></a>

Follow this procedure if you plan to run the channel in a [MediaLive Anywhere cluster](setup-emla.md).

Leave the default values in all the fields. MediaLive doesn't use the input specification for billing, and MediaLive isn't responsible for resource allocation.

JPEG XS (TR-07) isn't supported on an MediaLive Anywhere channel.

## Completing the settings – JPEG XS (TR-07)
<a name="input-specification-jpegxs"></a>

Use this section to complete the input specification for a channel that ingests JPEG XS video in an MPEG-2 transport stream, as defined by Video Services Forum Technical Recommendation 07 (TR-07). JPEG XS is available in the regions where the feature launches. See [Regional availability](#input-specification-jpegxs-regions).

A JPEG XS channel doesn't use the [standard input specification](input-specification.md). Instead, it uses a separate JPEG XS input specification. In the API, you set the `jpegXsInputSpecification` field instead of the `inputSpecification` field. The field is available in the `CreateChannel`, `UpdateChannel`, `DescribeChannel`, and `ListChannels` operations.

The JPEG XS input specification has three fields. All three are required, and each has only one valid value.


| Console field | API field | Value | 
| --- | --- | --- | 
| Input codec | codec | JPEGXS | 
| Resolution | resolution | HD | 
| Maximum input bitrate | maximumBitrate | MAX\_500\_MBPS (500 Mbps) | 

**Requirements**
+ Every input that is attached to the channel must be a MediaConnect input or a MediaConnect Router input.
+ The channel class can be STANDARD or SINGLE\_PIPELINE.
+ The channel can't be an MediaLive Anywhere channel.
+ The channel can't have a multiplex output destination.
+ The channel can't also have a CDI input specification.
+ To change a channel from the standard input specification to the JPEG XS input specification, or the reverse, the channel must be idle. Stop the channel first.

**To complete the settings (console)**

1. In the **Channel and input details** section, in **Input specifications**, choose the input type **Typical (all input types except CDI and Elemental Link)**. JPEG XS isn't available for the CDI or Elemental Link input types.

1. In **Input codec**, choose **JPEGXS**.

   The **Resolution** field (HD) and the **Maximum input bitrate** field (500 Mbps) are set automatically and are disabled. The **Slice mode** field isn't shown.

For more information about the MediaConnect input types, see [Setting up a MediaConnect input](input-create-push-mediaconnect.md) and [Setting up a MediaConnect Router input](input-create-mediaconnect-router.md). For the codecs that each input type supports, see [Supported codecs by input type](inputs-supported-codecs-by-input-type.md).

### Validation errors
<a name="input-specification-jpegxs-errors"></a>

When you create or update a channel, MediaLive checks the JPEG XS input specification. If a rule isn't met, the request fails with an HTTP 400 error. The following table lists the rules and the error messages.


| Situation | Error message | 
| --- | --- | 
| The channel sets both input specifications. | inputSpecification and jpegXsInputSpecification cannot both be set. Set jpegXsInputSpecification for a JPEG XS channel, or inputSpecification otherwise. | 
| The channel also has a CDI input specification. | jpegXsInputSpecification and cdiInputSpecification cannot both be set. | 
| The channel is an MediaLive Anywhere channel. | jpegXsInputSpecification is not supported on a MediaLive Anywhere channel. | 
| The channel has a multiplex output destination. | jpegXsInputSpecification is not supported on a channel with a multiplex output destination. | 
| An attached input isn't a MediaConnect or MediaConnect Router input. | A channel with jpegXsInputSpecification supports only MEDIACONNECT and MEDIACONNECT\_ROUTER inputs. | 
| The standard input specification uses the JPEGXS codec. | inputSpecification.codec JPEGXS is not supported. Use jpegXsInputSpecification for a JPEG XS channel. | 
| You switch between the two input specifications when the channel isn't idle. | Cannot switch between inputSpecification and jpegXsInputSpecification while the channel is in {{state}} state. Stop the channel first. | 

### Regional availability
<a name="input-specification-jpegxs-regions"></a>

JPEG XS (TR-07) input is available in the following AWS Regions:
+ US East (Ohio)
+ US East (N. Virginia)
+ US West (Oregon)
+ Asia Pacific (Hyderabad)
+ Asia Pacific (Malaysia)
+ Asia Pacific (Melbourne)
+ Asia Pacific (Mumbai)
+ Asia Pacific (Seoul)
+ Asia Pacific (Singapore)
+ Asia Pacific (Sydney)
+ Asia Pacific (Tokyo)
+ Europe (Frankfurt)
+ Europe (Ireland)
+ Europe (London)
+ Europe (Paris)
+ Europe (Stockholm)
+ Middle East (UAE)
+ South America (São Paulo)