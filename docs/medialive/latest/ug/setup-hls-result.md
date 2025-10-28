# Result of this procedure

As a result of this setup, an HLS input exists that specifies one or two _source_ URLs. These sources are the URLs for the source
content on the upstream server. When you start the channel, MediaLive will connect to
the upstream system at this source location or locations and pull the HLS manifests
into MediaLive:

- For a channel set up as a standard channel, MediaLive expects the upstream
  system to provide two sources and will therefore attempt to pull from both
  source locations.
- For a channel set up as a single-pipeline channel, MediaLive expects the
  upstream system to provide one source and will therefore attempt to pull
  from one source location.

![Diagram showing two GET requests to upstream origin servers for curling sports content.](/images/medialive/latest/ug/images\hls-pull-uss-input.png)
