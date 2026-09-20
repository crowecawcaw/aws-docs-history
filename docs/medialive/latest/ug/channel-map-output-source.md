

# Map the output encodes to the sources
<a name="channel-map-output-source"></a>

In the first step of planning the channel, you identified the number of encodes you need in each output group. You must now determine which assets from the source you can use to produce those encodes.

**Result of this procedure**  
After you have performed this procedure, you will have identified the following key components that you will create in the channel:
+ The video input selectors 
+ The audio input selectors
+ The captions input selectors

Identifying these components is the last step in planning the *input* side of the channel. 

**To map the output to the sources**

1. Obtain the *list of output encodes* you want to produce. You created this list in the [previous step](planning-encodes.md). It is useful to organize this list into a table. For example:


**Example**  

<table>
<thead>
  <tr><th>Output group</th><th>Type of encode</th><th>Encode nickname</th><th>Characteristics of the encode</th></tr>
</thead>
<tbody>
  <tr><td rowspan="7">HLS</td><td rowspan="3">Video</td><td>VideoA</td><td>AVC 1920x1080, 5 Mbps</td></tr>
  <tr><td>VideoB</td><td>AVC 1280x720, 3 Mbps</td></tr>
  <tr><td>VideoC</td><td>AVC 320x240, 750 Kbps</td></tr>
  <tr><td rowspan="2">Audio</td><td>AudioA</td><td>AAC 2.0 in English at 192000 bps</td></tr>
  <tr><td>AudioB</td><td>AAC 2.0 in French at 192000 bps</td></tr>
  <tr><td rowspan="2">Captions</td><td>CaptionsA</td><td>WebVTT (object-style) converted from embedded, in English</td></tr>
  <tr><td>CaptionsB</td><td>WebVTT (object-style) converted from embedded, in French</td></tr>
  <tr><td rowspan="3">RTMP</td><td>Video</td><td>VideoD</td><td>AVC 1920x1080, 5Mbps </td></tr>
  <tr><td>Audio</td><td>AudioC</td><td>Dolby Digital 5.1 in Spanish</td></tr>
  <tr><td>Captions</td><td>CaptionsC</td><td>RTMP CaptionInfo (converted from embedded) in Spanish</td></tr>
  <tr><td rowspan="5">Archive</td><td>Video</td><td>VideoE</td><td>AVC, 1920x1080, 8.5 Mbps</td></tr>
  <tr><td rowspan="3">Audio</td><td>AudioD</td><td>Dolby Digital 2.0 in Spanish </td></tr>
  <tr><td>AudioE</td><td>Dolby Digital 2.0 in French</td></tr>
  <tr><td>AudioF</td><td>Dolby Digital 2.0 in English</td></tr>
  <tr><td>Captions</td><td>CaptionsD</td><td>DVB-Sub (object-style) converted from Teletext, in 6 languages. </td></tr>
</tbody>
</table>


1. Obtain the *list of sources* that you created when you assessed the source content and collected identifiers. For an example of such a list, see [Assess the upstream system](evaluate-upstream-system.md).

1. In your table of output encodes, add two more columns, labeled *Source* and *Identifier in source*. 

1. For each encode (column 2), find a line in the *list of sources* that can produce that encode. Add the source codec and the identifier of that source codec. This example shows a completed table.


**Example**  

<table>
<thead>
  <tr><th>Output group</th><th>Type of encode</th><th>Encode nickname</th><th>Characteristics of the encode</th><th>Source</th><th>Identifier in source</th></tr>
</thead>
<tbody>
  <tr><td rowspan="7">HLS</td><td rowspan="3">Video</td><td>VideoA</td><td>AVC 1920x1080, 5 Mbps</td><td>HEVC </td><td>PID 600</td></tr>
  <tr><td>VideoB</td><td>AVC 1280x720, 3 Mbps</td><td>HEVC </td><td>PID 600</td></tr>
  <tr><td>VideoC</td><td>AVC 320x240, 750 Kbps</td><td>HEVC </td><td>PID 600</td></tr>
  <tr><td rowspan="2">Audio</td><td>AudioA</td><td>AAC 2.0 in English at 192000 bps</td><td>AAC 2.0</td><td>PID 759</td></tr>
  <tr><td>AudioB</td><td>AAC 2.0 in French at 192000 bps</td><td>AAC 2.0 </td><td>PID 747</td></tr>
  <tr><td rowspan="2">Captions</td><td>CaptionsA</td><td>WebVTT (object-style) converted from embedded, in English</td><td>Embedded</td><td>Channel 4</td></tr>
  <tr><td>CaptionsB</td><td>WebVTT (object-style) converted from embedded, in French</td><td>Embedded</td><td>Channel 2</td></tr>
  <tr><td rowspan="3">RTMP</td><td>Video</td><td>VideoD</td><td>AVC 1920x1080, 5Mbps </td><td>HEVC </td><td>PID 600</td></tr>
  <tr><td>Audio</td><td>AudioC</td><td>Dolby Digital 5.1 in Spanish</td><td>Dolby Digital 5.1 </td><td>PID 720</td></tr>
  <tr><td>Captions</td><td>CaptionsC</td><td>RTMP CaptionInfo (converted from embedded) in Spanish</td><td>Embedded</td><td>Channel 3</td></tr>
  <tr><td rowspan="5">Archive</td><td>Video</td><td>VideoE</td><td>AVC, 1920x1080, 5 Mbps</td><td>HEVC </td><td>PID 600</td></tr>
  <tr><td rowspan="3">Audio</td><td>AudioD</td><td>Dolby Digital 2.0 in Spanish </td><td>AAC 2.0</td><td>PID 746</td></tr>
  <tr><td>AudioE</td><td>Dolby Digital 2.0 in French</td><td>AAC 2.0 </td><td>PID 747</td></tr>
  <tr><td>AudioF</td><td>Dolby Digital 2.0 in English</td><td>AAC 2.0</td><td>PID 759</td></tr>
  <tr><td>Captions</td><td>CaptionsD</td><td>DVB-Sub (object-style) converted from Teletext, in 6 languages. </td><td>Teletext</td><td>PID 815</td></tr>
</tbody>
</table>


   You will use this information when you create the channel:
   + You will use the source and source identifier information when you [create the input selectors](input-video-selector.md).
   + You will use the characteristics information when you [create the encodes](creating-a-channel-step6.md) in the output groups.

1. After you have identified the source assets, group those assets that are being used more than once, to remove the duplicates.

1. Label each asset by its type—video, audio, or captions.


**Example**  

<table>
<thead>
  <tr><th>Input asset</th><th>Asset nickname</th><th>Source</th><th>Characteristics</th><th>Identifier in Source</th></tr>
</thead>
<tbody>
  <tr><td>video 1</td><td>Video1</td><td>Video</td><td>HEVC </td><td>PID 600</td></tr>
  <tr><td>audio 1</td><td>Audio1</td><td>Audio</td><td>AAC 2.0 Spanish</td><td>PID 746</td></tr>
  <tr><td>audio 2</td><td>Audio2</td><td></td><td>AAC 2.0 French </td><td>PID 747</td></tr>
  <tr><td>audio 3</td><td>Audio3</td><td></td><td>AAC 2.0 English</td><td>PID 759</td></tr>
  <tr><td>audio 4</td><td>Audio4</td><td></td><td>Dolby Digital 5.1 Spanish</td><td>PID 720</td></tr>
  <tr><td>captions 1</td><td>Captions1</td><td>Captions</td><td>Embedded French</td><td>Channel 2</td></tr>
  <tr><td>captions 2</td><td>Captions2</td><td></td><td>Embedded Spanish</td><td>Channel 3</td></tr>
  <tr><td>captions 3</td><td>Captions3</td><td></td><td>Embedded English</td><td>Channel 4</td></tr>
  <tr><td>captions 4</td><td>Captions4</td><td></td><td>Teletext, all languages</td><td>PID 815</td></tr>
</tbody>
</table>


## Example of mapping
<a name="channel-map-example"></a>

The following diagrams illustrate the mapping of the output encodes back to source assets. The first diagram shows the outputs (at the top) and the sources (at the bottom). The other three diagrams shows the same outputs and sources with the mappings for video, for audio, and for captions.

**Encodes and assets**

![Diagram showing HLS, RTMP, and Archive sections with various video, audio, and caption sources.](https://docs.aws.amazon.com/medialive/latest/ug/images/channel-design-map-in-out.png)


**Mapping video encodes to assets**

![Diagram showing video, audio, and caption sources mapped to HLS, RTMP, and Archive outputs.](https://docs.aws.amazon.com/medialive/latest/ug/images/channel-design-map-in-out-V.png)


**Mapping audio encodes to assets**

![Diagram showing audio and video sources mapped to HLS, RTMP, and Archive outputs.](https://docs.aws.amazon.com/medialive/latest/ug/images/channel-design-map-in-out-A.png)


**Mapping captions encodes to assets**

![Diagram showing video, audio, and caption sources mapped to HLS, RTMP, and Archive outputs.](https://docs.aws.amazon.com/medialive/latest/ug/images/channel-design-map-in-out-C.png)
