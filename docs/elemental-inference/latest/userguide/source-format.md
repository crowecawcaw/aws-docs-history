# Step B: Format the source media

Make sure that the source media meets the requirements.

## Format requirements

You must format the source media according to the CMAF Ingest (Interface-1)
version 1.2 specification.

The following table identifies specific requirements for Elemental Inference.

| Characteristic                 | Requirement                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Media fragments                | Fragmented CMAF Ingest containerized media fragments                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| MovieFragmentBox               | One per segment                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Initialization segment: naming | Include an initialization segment with each stream, as<br>follows:<br>• For video:<br>`Streams(default-video.cmfv)/InitializationSegment`<br>• For audio:<br>`Streams(default-audio.cmfa)/InitializationSegment`                                                                                                                                                                                                                                                                                   |
| Media segments: naming         | Media segments after the initialization segment must following<br>this naming pattern:<br>`Streams<br>default-<`type`>.<`ext`>/Segment(<`sequence-number`>)`<br>Where:<br><type> is video or audio<br><ext> is cmfv or cmfa<br><sequence-number> must increase monotonically, although it<br>doesn't have to be contiguous. Each sequence number must match<br>the sequence number in the MovieFragmentHeader box.<br>For example:<br>`Streams<br>default-video.cmfv/Segment(<`sequence-number`>)` |
| End of Stream indicator        | The last media segment in the session must be:<br>• A media segment with the `lmsg` brand<br>included in the compatible brands under the<br>SegmentTypeBox.<br>If you can't signal the end of stream in this way, there is a<br>workaround. See [Step C: Deliver the source media](deliver-source.md "deliver-source.md").                                                                                                                                                                         |

## Example

The following code shows how to use FFMPG to format the media to follow these
requirements. The commands demux, segment, and containerize the video and audio.
Note the `-init_seg_name` and `-media_seg_name` lines

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
