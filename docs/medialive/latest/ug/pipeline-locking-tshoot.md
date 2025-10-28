# Troubleshooting

Pipeline locking ensures that the two pipelines in a standard channel are frame
accurate with each other, in the output groups where MediaLive performs pipeline
locking.

If you or the operator at the downstream system notices that the pipelines are not
synchronized, you can perform the following troubleshooting:

- Make sure that MediaLive [supports
  pipeline locking](pipeline-locking-verify-input.md "pipeline-locking-verify-input.md") for the type of input in your channel.
- Verify that the timecode requirements are met:

      + Make sure that the input source has an embedded timecode.


      + If you chose epoch-locking mode, make sure that the embedded timecode
       is within 2 minutes of epoch time.

  If an input source has sections where there is no embedded timecode, MediaLive
  stops performing frame-accurate pipeline locking. MediaLive automatically falls back
  to performing approximate pipeline locking. Whenever the embedded timecode
  reappears, MediaLive resumes frame-accurate pipeline locking.

- Make sure that the affected outputs are eligible for pipeline locking.
  Pipeline locking applies [only to specific types of
  outputs](pipeline-lock.md "pipeline-lock.md").

- Make sure that you changed the **Framerate control** so that
  it is _not_ **Initialize_from_source**.
- Make sure that the input framerate and output framerate are a [simple conversion](pipeline-locking-verify-input.md "pipeline-locking-verify-input.md") of each
  other.
- If the framerate within the source changes, it's possible that MediaLive can't
  perform pipeline locking for the duration because for that section of video,
  there is no simple framerate conversion.
- Make sure that you remembered to set up segmentation markers in a UDP output
  group. For the other supported output groups, you don't need to worry about this
  because their outputs are always segmented.
- Make sure that you set up the segmentation marker type that your downstream
  system expects.
