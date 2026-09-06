

# Plan the encodes
<a name="plan-encodes"></a>

In [Map the output encodes to the sources](channel-map-output-source.md), you sketched out a plan for the encodes you want to create in each output group. Below is the example of the plan from that step, showing the outputs and encodes, and the sources for those encodes.

At some point, you must fill in the details for the encodes identified in the second and third columns of this table. You have a choice:
+ You can decide these details now. 
+ You can decide the details later, when you are actually creating the channel. If you decide to do this, we recommend you still read the procedures after the table, to get an idea of what is involved in defining an encode.


**Example**  


- **HLS**
  - **Type of encode:** Video / **Encode nickname:** VideoA / **Characteristics of the encode:** AVC 1920x1080, 5 Mbps / **Source:** HEVC  / **Identifier in source:** PID 600
  - **Encode nickname:** VideoB / **Characteristics of the encode:** AVC 1280x720, 3 Mbps / **Source:** HEVC  / **Identifier in source:** PID 600
  - **Encode nickname:** VideoC / **Characteristics of the encode:** AVC 320x240, 750 Kbps / **Source:** HEVC  / **Identifier in source:** PID 600
  - **Type of encode:** Audio / **Encode nickname:** AudioA / **Characteristics of the encode:** AAC 2.0 in English at 192000 bps / **Source:** AAC 2.0 / **Identifier in source:** PID 759
  - **Encode nickname:** AudioB / **Characteristics of the encode:** AAC 2.0 in French at 192000 bps / **Source:** AAC 2.0  / **Identifier in source:** PID 747
  - **Type of encode:** Captions / **Encode nickname:** CaptionsA / **Characteristics of the encode:** WebVTT (object-style) converted from embedded, in English / **Source:** Embedded / **Identifier in source:** Channel 4
  - **Encode nickname:** CaptionsB / **Characteristics of the encode:** WebVTT (object-style) converted from embedded, in French / **Source:** Embedded / **Identifier in source:** Channel 2

- **RTMP**
  - **Type of encode:** Video / **Encode nickname:** VideoD / **Characteristics of the encode:** AVC 1920x1080, 5Mbps  / **Source:** HEVC  / **Identifier in source:** PID 600
  - **Type of encode:** Audio / **Encode nickname:** AudioC / **Characteristics of the encode:** Dolby Digital 5.1 in Spanish / **Source:** Dolby Digital 5.1  / **Identifier in source:** PID 720
  - **Type of encode:** Captions / **Encode nickname:** CaptionsC / **Characteristics of the encode:** RTMP CaptionInfo (converted from embedded) in Spanish / **Source:** Embedded / **Identifier in source:** Channel 2

- **Archive**
  - **Type of encode:** Video / **Encode nickname:** VideoE / **Characteristics of the encode:** AVC, 1920x1080, 5 Mbps / **Source:** HEVC  / **Identifier in source:** PID 600
  - **Type of encode:** Audio / **Encode nickname:** AudioD / **Characteristics of the encode:** Dolby Digital 2.0 in Spanish  / **Source:** AAC 2.0 / **Identifier in source:** PID 746
  - **Encode nickname:** AudioE / **Characteristics of the encode:** Dolby Digital 2.0 in French / **Source:** AAC 2.0  / **Identifier in source:** PID 747
  - **Encode nickname:** AudioF / **Characteristics of the encode:** Dolby Digital 2.0 in English / **Source:** AAC 2.0 / **Identifier in source:** PID 759
  - **Type of encode:** Captions / **Encode nickname:** CaptionsD / **Characteristics of the encode:** DVB-Sub (object-style) converted from Teletext, in 6 languages.  / **Source:** Teletext / **Identifier in source:** PID 815



**Design the details for each video encode**

For each video encode in your table, you have already identified the source asset, codec, resolution and bitrate. You must now identify all the other encoding parameters you need to set.

Follow this procedure for each individual video encode.

1. Look at the fields in the video encode section of each output. To view these fields, follow these steps. Don't worry about not completing all the sections. You only want to display the video encode fields, and you will then cancel the channel.
   + On the MediaLive home page, choose **Create channel**, and in the navigation pane, choose **Channels**. 

     If you've created a channel before, you won't see the home page. In that case, in the MediaLive navigation pane, choose **Channels**, and then choose **Create channel**.
   + On the **Create channel** page, under **Output groups**, choose **Add**. 

     Don't worry that you haven't completed any of the earliers sections in the channel. You are only trying to display all the fields for the video encode.
   + In the **Add output group** section, choose **HLS** and choose **Confirm**.
   + Under that output group, choose **Output 1**.
   + In the **Output** section, go to the **Stream settings** section, and choose the **Video** link. 
   + In the **Codec settings** field, choose the codec that you want for this video encode. More fields appear. Choose the field labels for all the sections to display all the fields.

1. In each section, determine whether you need to change the defaults. 
   + Many of the fields have defaults, which means you can leave the field value as is. For details about a field and its default value, choose the **Info** link next to the field.
   + There are some fields that you might need to set according to instructions from your downstream system, to match the expectations of the downstream system.
   + There are some fields where the value you enter affects the output charges for this channel. These are:
     + The **Width** and **Height** fields (which define the video resolution).
     + The **Framerate** fields.
     + The **Rate control** fields.

     For information about charges, see [the MediaLive price list](https://aws.amazon.com/medialive/pricing/).
   + You can read about some of the fields in the following sections:
     + For information about the **Color space** fields, see [Handling complex color space conversions](color-space.md).
     + For information about the Additional encoding settings fields, see [Setting up enhanced VQ mode](video-enhancedvq.md)
     + For information about the **Rate control** fields, see [Setting the rate control mode](video-encode-ratecontrol.md). There are fields in this section that affect the output charges for this channel. For more information about charges, see [the MediaLive price list](https://aws.amazon.com/medialive/pricing/).
     + For information about the **Timecode** fields, see [Working with timecodes and timestamps](timecode.md).

1. Make detailed notes about the values for all the fields you plan to change. Do this for every video encode that you identified.

**Design the details for each audio encode**

For each audio encode in your table, you have already identified the source asset, codec and bitrate. You must now identify all the other encoding parameters you need to set.

Follow this procedure for each individual audio encode.

1. Look at the fields in the audio encode section of each output. To view these fields, follow the same steps as for the video encodes, but choose the **Audio 1** link. 

   With audio encodes, there aren't many fields for each code. But the fields for the codecs are very different from each other.

1. Study the fields and make notes. 

**Design the details for each captions encode**

For each captions encode in your table, you have already identified the source captions, format, and language. You must now identify all the other encoding parameters you need to set.

Follow this procedure for each individual captions encode.

1. Look at the fields in the captions encode section of each output. To view these fields, follow the same steps as for the video encodes, but choose Add caption to add a captions section, because there is no captions section by default. 

   With captions encodes, there aren't many fields for each captions format. But the fields for the formats are very different from each other.

1. Study the fields and make notes. 