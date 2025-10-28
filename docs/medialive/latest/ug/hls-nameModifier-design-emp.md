# Designing the

nameModifier

Design the `nameModifier` portions of the file name. The
child manifests and media files include this modifier in their file
names.

This `nameModifier` distinguishes each output from the
other, so it must be unique in each output.

- For an output that contains video (and possibly other
  streams), you typically describe the video. For example, if you
  have three renditions, you might use
  `-high`, `-medium`
  and `-low`. Or each modifier could
  accurately describe the resolution and the bitrate
  (`-1920x1080-5500kpbs`).
- For an output that contains only audio or only captions, you
  typically describe the audio or captions. For example,
  `-aac` or
  `-webVTT`.
  It’s a good idea to start the `nameModifier` with a
  delimiter, such as a hyphen, in order to separate the`baseFilename` from the `nameModifier`.

The `nameModifier` can include [data variables](variable-data-identifiers.md "variable-data-identifiers.md").
