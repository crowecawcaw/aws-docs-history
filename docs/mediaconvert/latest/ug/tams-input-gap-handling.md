# Gap handling options

When processing TAMS content, you might encounter gaps where segments are missing from the
timeline. MediaConvert detects gaps by comparing the end time of each segment with the start time of
the next segment. Gaps smaller than 100 milliseconds are ignored to account for minor timing
variations. Choose from the following three options for handling these gaps:

**Skip gaps**

MediaConvert skips missing segments and creates discontinuity markers in the output. This approach reduces the total output duration by the amount of missing content and processes faster because it doesn't generate replacement content. However, it might cause audio or video sync issues in some players.

Use this option when you want to minimize processing time and output size, and when missing content is acceptable for your use case.

**Fill with black**

MediaConvert fills missing segments with black frames and silence for audio. This approach maintains the original timeline and duration, ensures consistent output duration for broadcast applications, and prevents sync issues between audio and video tracks. However, it takes longer to process and creates larger output files.

Use this option when you need consistent output duration or when maintaining the original timeline is important for your workflow.

**Hold last frame**

MediaConvert repeats the last frame before each gap and maintains audio silence. This approach preserves visual continuity while indicating missing content, maintains consistent output duration, and provides a visual cue that content is missing.

Use this option when you want to indicate missing content while maintaining visual continuity.

###### Note

Gap handling applies to both video and audio tracks. If you have separate audio and video flows, MediaConvert ensures that gap handling is consistent across both tracks.
