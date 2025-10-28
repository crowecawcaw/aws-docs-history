# Ensure correct setup on the RTMP upstream

system

An operator at the upstream server must set up the source content on the upstream
system. Make sure that the operator sets up as follows:

- They set up to deliver the correct number of sources:
  - If the MediaLive channel is a standard channel, set up two sources for
    the content. Make sure that the two source contents are identical in
    terms of video resolution and bitrate.
  - If the MediaLive channel is a single-pipeline channel, set up one
    source for the content.

- They set up to make the content available at the agreed URLs, and they use
  the agreed application names and instance names. These URLs are the URLs
  that you obtained [earlier in this
  section](setup-mp4-obtain-info.md "setup-mp4-obtain-info.md"), and that you configured into the RTMP input. They
  correspond to the URLs shown in [the
  diagram after this procedure](setup-result-rtmp-push.md "setup-result-rtmp-push.md").
