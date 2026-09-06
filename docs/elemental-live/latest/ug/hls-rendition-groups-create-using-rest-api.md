

# Creating HLS rendition groups (REST API)
<a name="hls-rendition-groups-create-using-rest-api"></a>

The following information assumes that you have read [Creating HLS rendition groups (web interface)](hls-rendition-groups-create-using-web-interface.md) and are therefore familiar with the construction and association of an output containing video and rendition groups.

Via the REST API, create or modify the event to include the elements and tags in the XML body as described in the following sections.

**Topics**
+ [Creating streams for HLS rendition groups using the REST API](#hls-rendition-groups-create-using-rest-api-streams)
+ [Creating output groups for HLS rendition groups using the REST API](#hls-rendition-groups-create-using-rest-api-output-groups)
+ [Creating outputs for HLS output groups using the REST API](#hls-rendition-groups-create-using-rest-api-outputs)
+ [Sample XML body for an HLS output group with audio rendition group event](#hls-rendition-groups-create-using-rest-api-sample-xml)

## Creating streams for HLS rendition groups using the REST API
<a name="hls-rendition-groups-create-using-rest-api-streams"></a>
+ Create as many stream\_assembly elements as you require, one for each unique video stream, one for each unique audio stream, and one for each caption stream.
+ Each stream\_assembly element must contain only of these:
  + One video\_description element (plus an optional preset\_id tag and name tag), or
  +  One audio\_description element (plus an optional preset\_id tag and name tag), or
  +  One caption\_description element (plus an optional preset\_id tag and name tag).

## Creating output groups for HLS rendition groups using the REST API
<a name="hls-rendition-groups-create-using-rest-api-output-groups"></a>
+ Create as many HLS output groups as desired by creating one output group that has the value “apple\_live\_group\_settings” in its type tag and that contains one apple\_live\_group\_settings element. Set other tags as desired.

## Creating outputs for HLS output groups using the REST API
<a name="hls-rendition-groups-create-using-rest-api-outputs"></a>
+ Within each HLS output group, create as many output elements as required, one for each video stream (plus captions), one for each audio stream, and one for each captions stream.
+ Each **video** output element must contain:
  + container: m3u8
  + extension: m3u8
  + stream\_assembly\_name: The name of the one stream\_assembly to associate with this output.This value matches the value of the name tag in the corresponding stream\_assembly\_name element.
  + apple\_live\_settings element that contains:
    + audio\_rendition\_sets tag: A comma-separated list of the names of the audio rendition groups to associate with this video output to create a set. This value matches the value of the audio\_group\_id tag in each of the associated audio outputs. For example, “audio\_1” in the audio\_rendition\_sets of this video output matches the “audio\_1” in the audio\_group\_id tag of the associated audio output.
    + Other tags as you require.
+ Each **audio** output element must contain:
  + container: m3u8
  + extension: m3u8
  + stream\_assembly\_name: The name of the one stream\_assembly to associate with this output.This value matches the value of the name tag in the corresponding stream\_assembly\_name element.
  + apple\_live\_settings element that contains:
    + audio\_group\_id: The name of the audio rendition group this audio output belongs to. Specifying a value here creates the rendition group and puts this audio output into that rendition group.
    + audio\_track\_type: Either “alternate\_audio\_auto\_select\_default” or “alternate\_audio\_auto\_select” or “alternate\_audio\_not\_auto\_select” or “audio\_only\_variant\_stream”. See [Step 2. Determine defaults and auto-selection behavior](hls-rendition-groups-getting-ready-to-create.md#hls-rendition-groups-getting-ready-determine-defaults)for information.
    + Other tags as you require.
+ Each **captions** output element must contain:
  + container: m3u8
  + extension: m3u8
  + stream\_assembly\_name: The name of the one stream\_assembly to associate with this output.This value matches the value of the name tag in the corresponding stream\_assembly\_name element.
  + apple\_live\_settings element that contains the usual tags as required.

## Sample XML body for an HLS output group with audio rendition group event
<a name="hls-rendition-groups-create-using-rest-api-sample-xml"></a>

This example shows the XML body for an event that contains an HLS output group that includes audio rendition groups.

Following is the `<input>` element. There are no special rendition group requirements that affect this element.

```
<live_event>
<name>Multi Audio - one video</name>
<input>
.
.
.
</input>
.
.
.
```

Following is the `<stream_assembly>` element for one video. This stream\_assembly has the name tag set to “stream\_assembly\_0” (assigned by default).

```
<stream_assembly>
    <name>stream_assembly_0</name>
    .
    .
    .
    <video_description>
    .
    .
    .
    <h264_settings>
    .
    .
    .
    </h264_settings>
    <codec>h.264</codec>
    .
    .
    .
    </video_description>
    <caption_description>
      <language_code>eng</language_code>
      <language_description>English</language_description>
    .
    .
    .
    </caption_description>
</stream_assembly>
```

Following is the `<stream_assembly>` for the first audio. This stream\_assembly has the name tag set to “stream\_assembly\_1” (assigned by default).

```
<stream_assembly>
    <name>stream_assembly_1</name>
    <audio_description>
    <follow_input_language_code>false</follow_input_language_code>
    <language_code>eng</language_code>
    <stream_name>English</stream_name>
    .
    .
    .
    <aac_settings>
    .
    .
    .
    .
    </aac_settings>
    .
    .
    .
    <codec>aac</codec>
    <audio_source_name>Audio Selector 1</audio_source_name>
    </audio_description>
</stream_assembly>
```

Following are the `<stream_assembly>` elements for three more audios: stream\_assembly\_2, stream\_assembly\_3, and stream\_assembly\_4. 

```
<stream_assembly>
    <name>stream_assembly_2</name>
    <audio_description>
    <follow_input_language_code>false</follow_input_language_code>
    <language_code>eng</language_code>
    <stream_name>English</stream_name>
    .
    .
    .
    <aac_settings>
    .
    .
    .
    </aac_settings>
    .
    .
    .
    <codec>aac</codec>
    <audio_source_name>Audio Selector 1</audio_source_name>
    </audio_description>
</stream_assembly>
    
<stream_assembly>
    <name>stream_assembly_3</name>
    <audio_description>
    .
    .
    .
    </audio_description>
</stream_assembly>
    
<stream_assembly>
    <name>stream_assembly_4</name>
    <audio_description>
    .
    .
    .
    </audio_description>
</stream_assembly>
```

Following is the `<stream_assembly>` for the first caption. This stream\_assembly has the name tag set to “stream\_assembly\_5” (assigned by default).

```
<stream_assembly>
    <name>stream_assembly_5</name>
    <caption_description>
        <destination_type>WebVTT</destination_type>
        <language_code>eng</language_code>
        <language_description>English</language_description>
        <order>1</order>
        <caption_source_name>Caption Selector 1</caption_source_name>
    </caption_description>
</stream_assembly>
```

Following are the `<stream_assembly>` elements for three more captions: stream\_assembly\_6, stream\_assembly\_7, and stream\_assembly\_8. 

```
<stream_assembly>
    <name>stream_assembly_6</name>
    <caption_description>
    <destination_type>WebVTT</destination_type>
    <language_code>eng</language_code>
    <language_description>English</language_description>
    <order>1</order>
    <caption_source_name>Caption Selector 1</caption_source_name>
    </caption_description>
</stream_assembly>
<stream_assembly>
    <name>stream_assembly_7</name>
    .
    .
    .
</stream_assembly>
<stream_assembly>
    <name>stream_assembly_8</name>
    .
    .
    .
</stream_assembly>
```

Following is the `<output_group>` of type apple\_live\_group\_settings. 

```
<output_group>
<apple_live_group_settings>
.
.
.
</apple_live_group_settings>
<type>apple_live_group_settings</type>
```

Following is the `<output>` (nested in the HLS output\_group element) that is associated with stream\_assembly\_0 and is therefore a video output. This video is associated with the rendition groups “Audio\_aac\_hi” and “Audio\_aac\_lo.”

```
    <output>
        <extension>m3u8</extension>
        .
        .
        .
        <apple_live_settings>
        <audio_rendition_sets>Audio_aac_hi,Audio_aac_lo</audio_rendition_sets>
        .
        .
        .
        </apple_live_settings>
        <m3u8_settings>
        .
        .
        .
        </m3u8_settings>
        <stream_assembly_name>stream_assembly_0</stream_assembly_name>
        <container>m3u8</container>
    </output>
```

Following is the `<output>` (nested in the HLS output\_group element) that is associated with stream\_assembly\_1 and is therefore an audio output. This audio is part of the rendition group “Audio\_aac\_hi.”

```
    <output>
        <extension>m3u8</extension>
        .
        .
        .
        <apple_live_settings>
        <alternate_audio_track_selection>default_audio</alternate_audio_track_selection>
        <audio_group_id>Audio_aac_hi</audio_group_id>
        .
        .
        .
        </apple_live_settings>
        <m3u8_settings>
        .
        .
        .
        </m3u8_settings>
        <stream_assembly_name>stream_assembly_1</stream_assembly_name>
        <container>m3u8</container>
    </output>
```

More outputs follow, one for each audio stream assembly. Each is part of a rendition group.

```
    <output>
    .
    .
    .
    </output>
    <output>
    .
    .
    .
    </output>
    <output>
    .
    .
    .
    </output>
```

Following is the `<output>` (nested in the HLS output\_group element) that is associated with stream\_assembly\_5 and is therefore a caption output. 

```
    <output>
        <extension>m3u8</extension>
        .
        .
        .
        .
        <stream_assembly_name>stream_assembly_5</stream_assembly_name>
        <container>m3u8</container>
    </output>
```

More outputs follow, one for each caption stream assembly and one for each caption assembly. 

```
    <output>
          .
          .
          .
    </output>
    <output>
          .
          .
          .
    </output>
    <output>
          .
          .
          .
    </output>
          .
          .
          .
</output_group>
</live_event>
```