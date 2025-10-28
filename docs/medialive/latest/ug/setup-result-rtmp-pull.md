# Result of this procedure

As a result of this setup, an RTMP pull input exists that specifies one or two
_source_ URLs. These sources are the URLs for
the source content on the upstream system.

At runtime of the channel, the input will connect to two URLs (for a standard
channel) or one URL (for a single-pipeline channel), and pull the source content
identified by the application name and instance name into MediaLive.

![Diagram showing two GET requests to rtmp URLs for upstream systems input.](/images/medialive/latest/ug/images\rtmp-pull-uss-input.png)
