

# Step B: Format the source media
<a name="source-format"></a>

Make sure that the source media meets the requirements.

## Format requirements
<a name="source-format-requirements"></a>

You must format the source media according to the CMAF Ingest (Interface-1) version 1.2 specification. 

The following table identifies specific requirements for Elemental Inference.


| Characteristic | Requirement | 
| --- | --- | 
| Media fragments | Fragmented CMAF Ingest containerized media fragments | 
| MovieFragmentBox | One per segment | 
| Initialization segment: naming | Include an initialization segment with each stream, as follows:+  For video: `Streams(default-video.cmfv)/InitializationSegment` <br />+  For audio: `Streams(default-audio.cmfa)/InitializationSegment`  | 
| Media segments: naming | Media segments after the initialization segment must following this naming pattern:<br />`Streams default-<{{type}}>.<{{ext}}>/Segment(<{{sequence-number}}>)`<br />Where:<br /><type> is video or audio<br /><ext> is cmfv or cmfa<br /><sequence-number> must increase monotonically, although it doesn't have to be contiguous. Each sequence number must match the sequence number in the MovieFragmentHeader box.<br />For example:<br />`Streams default-video.cmfv/Segment(<{{sequence-number}}>)` | 
| End of Stream indicator | The last media segment in the session must be:+  A media segment with the `lmsg` brand included in the compatible brands under the SegmentTypeBox. <br />If you can't signal the end of stream in this way, there is a workaround. See [Step C: Deliver the source media](deliver-source.md). | 

## Example
<a name="source-format-requirements-example"></a>

The following code shows how to use FFMPG to format the media to follow these requirements. The commands demux, segment, and containerize the video and audio. Note the `-init_seg_name` and `-media_seg_name` lines

```
$ mkdir 'Streams(default-video.cmfv)'
$ ffmpeg -i input.mp4 \
-map 0:v:0 -c:v libx264 \
    -profile:v main -pix_fmt yuv420p \
    -g 30 -keyint_min 30 -sc_threshold 0 \
    -force_key_frames 'expr:gte(t,n_forced*1)' \
    -f dash -seg_duration 1 -use_timeline 0 \
    -use_template 1 -remove_at_exit 0  \
    -init_seg_name 'Streams(default-video.cmfv)/InitializationSegment' \
    -media_seg_name 'Streams(default-video.cmfv)/Segment($Number%09d$)' \
    'video.mpd'

$ mkdir 'Streams(default-audio.cmfa)'$ ffmpeg -i input.mp4 \
    -map 0:a:0 -c:a aac -ar 48000 -ac 2 \
    -f dash -seg_duration 1 -use_timeline 0 \
    -use_template 1 -remove_at_exit 0 \
    -init_seg_name 'Streams(default-audio.cmfa)/InitializationSegment' \
    -media_seg_name 'Streams(default-audio.cmfa)/Segment($Number%09d$)' \
    'audio.mpd'
```