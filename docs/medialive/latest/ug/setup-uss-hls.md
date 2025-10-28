# Ensure correct setup on the HLS upstream

server

An operator at the upstream server must set up the source content on the upstream
system. Make sure that the operator sets up as follows:

- They set up to deliver the correct number of sources:
  - If the MediaLive channel is a standard channel, the operator must set
    up two sources for the content. They must make sure that the two
    sources are identical in terms of video resolution and
    bitrate.
  - If the MediaLive channel is a single-pipeline channel, the operator
    must set up one source for the content.

- They set up to make the M3U8 manifest files available at the agreed URLs.
  These are the URLs that you obtained in [step 1](setup-input-link-obtain-info.md "setup-input-link-obtain-info.md"), and that you
  configured into the HLS input. They correspond to the URLs shown in [the diagram after this
  procedure](setup-hls-result.md "setup-hls-result.md").
