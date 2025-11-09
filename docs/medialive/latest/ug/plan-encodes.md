# Plan the encodes

In [Map the output encodes
to the sources](channel-map-output-source.md "channel-map-output-source.md"), you sketched out a plan
for the encodes you want to create in each output group. Below is the example
of the plan from that step, showing the outputs and encodes, and the sources
for those encodes.

At some point, you must fill in the details for the encodes identified
in the second and third columns of this table. You have a choice:

- You can decide these details now.

- You can decide the details later, when you are actually creating the
  channel. If you decide to do this, we recommend you still read the
  procedures after the table, to get an idea of what is involved in defining
  an encode.

| Example   | Output group                                             | Type of encode                                                  | Encode nickname        | Characteristics of the encode | Source  | Identifier in source |
| --------- | -------------------------------------------------------- | --------------------------------------------------------------- | ---------------------- | ----------------------------- | ------- | -------------------- |
| HLS       | Video                                                    | VideoA                                                          | AVC 1920x1080, 5 Mbps  | HEVC                          | PID 600 |
| VideoB    | AVC 1280x720, 3 Mbps                                     | HEVC                                                            | PID 600                |
| VideoC    | AVC 320x240, 750 Kbps                                    | HEVC                                                            | PID 600                |
| Audio     | AudioA                                                   | AAC 2.0 in English at 192000 bps                                | AAC 2.0                | PID 759                       |
| AudioB    | AAC 2.0 in French at 192000 bps                          | AAC 2.0                                                         | PID 747                |
| Captions  | CaptionsA                                                | WebVTT (object-style) converted from embedded, in English       | Embedded               | Channel 4                     |
| CaptionsB | WebVTT (object-style) converted from embedded, in French | Embedded                                                        | Channel 2              |
| RTMP      | Video                                                    | VideoD                                                          | AVC 1920x1080, 5Mbps   | HEVC                          | PID 600 |
| Audio     | AudioC                                                   | Dolby Digital 5.1 in Spanish                                    | Dolby Digital 5.1      | PID 720                       |
| Captions  | CaptionsC                                                | RTMP CaptionInfo (converted from embedded) in Spanish           | Embedded               | Channel 2                     |
| Archive   | Video                                                    | VideoE                                                          | AVC, 1920x1080, 5 Mbps | HEVC                          | PID 600 |
| Audio     | AudioD                                                   | Dolby Digital 2.0 in Spanish                                    | AAC 2.0                | PID 746                       |
| AudioE    | Dolby Digital 2.0 in French                              | AAC 2.0                                                         | PID 747                |
| AudioF    | Dolby Digital 2.0 in English                             | AAC 2.0                                                         | PID 759                |
| Captions  | CaptionsD                                                | DVB-Sub (object-style) converted from Teletext, in 6 languages. | Teletext               | PID 815                       |

###### Design the details for each video encode

For each video encode in your table, you have already identified the
source asset, codec, resolution and bitrate. You must now identify all the
other encoding parameters you need to set.

Follow this procedure for each individual video encode.

1.  Look at the fields in the video encode section of each output. To view
    these fields, follow these steps. Don't worry about not completing all the
    sections. You only want to display the video encode fields, and you will
    then cancel the channel.
    - On the MediaLive home page, choose **Create channel**,
      and in the navigation pane, choose **Channels**.

    If you've created a channel before, you won't see the home page. In
    that case, in the MediaLive navigation pane, choose
    **Channels**, and then choose **Create
    channel**.
    - On the **Create channel** page, under
      **Output groups**, choose **Add**.

    Don't worry that you haven't completed any of the earliers sections
    in the channel. You are only trying to display all the fields for the
    video encode.
    - In the **Add output group** section, choose
      **HLS** and choose **Confirm**.
    - Under that output group, choose **Output
      1**.
    - In the **Output** section, go to the
      **Stream settings** section, and choose the
      **Video** link.
    - In the **Codec settings** field, choose the codec
      that you want for this video encode. More fields appear. Choose the field
      labels for all the sections to display all the fields.

2.  In each section, determine whether you need to change the defaults.
    - Many of the fields have defaults, which means you can leave the
      field value as is. For details about a field and its default value,
      choose the **Info** link next to the
      field.
    - There are some fields that you might need to set according to
      instructions from your downstream system, to match the expectations of
      the downstream system.
    - There are some fields where the value you enter affects the output
      charges for this channel. These are:

          + The **Width** and **Height**
           fields (which define the video resolution).
          + The **Framerate** fields.
          + The **Rate control** fields.

      For information about charges, see [the MediaLive price
      list](https://aws.amazon.com/medialive/pricing/ "https://aws.amazon.com/medialive/pricing/").

    - You can read about some of the fields in the following
      sections:
      - For information about the **Color space** fields,
        see [Handling complex color space conversions](color-space.md "color-space.md").
      - For information about the Additional encoding settings fields, see
        [Setting up enhanced VQ mode](video-enhancedvq.md "video-enhancedvq.md")
      - For information about the **Rate control**
        fields, see [Setting the rate control mode](video-encode-ratecontrol.md "video-encode-ratecontrol.md"). There are
        fields in this section that affect the output charges for this channel.
        For more information about charges, see [the MediaLive price
        list](https://aws.amazon.com/medialive/pricing/ "https://aws.amazon.com/medialive/pricing/").
      - For information about the **Timecode** fields,
        see [Working with timecodes and timestamps](timecode.md "timecode.md").

3.  Make detailed notes about the values for all the fields you plan to
    change. Do this for every video encode that you identified.

###### Design the details for each audio encode

For each audio encode in your table, you have already identified the
source asset, codec and bitrate. You must now identify all the other
encoding parameters you need to set.

Follow this procedure for each individual audio encode.

1. Look at the fields in the audio encode section of each output. To view
   these fields, follow the same steps as for the video encodes, but choose
   the **Audio 1** link.

With audio encodes, there aren't many fields for each code. But the
fields for the codecs are very different from each other. 2. Study the fields and make notes.

###### Design the details for each captions encode

For each captions encode in your table, you have already identified the
source captions, format, and language. You must now identify all the other
encoding parameters you need to set.

Follow this procedure for each individual captions encode.

1. Look at the fields in the captions encode section of each output. To
   view these fields, follow the same steps as for the video encodes, but
   choose Add caption to add a captions section, because there is no captions
   section by default.

With captions encodes, there aren't many fields for each captions
format. But the fields for the formats are very different from each
other. 2. Study the fields and make notes.
