# Result of this procedure

As a result of this setup, an SRT caller input exists that specifies one or two
_source_ URLs. These sources are the URLs for
the source content on the upstream system.

At runtime of the channel, MediaLive (the caller) will perform a handshake with the
upstream system (the listener). MediaLive will connect to two URLs (for a standard
channel) or one URL (for a single-pipeline channel), and pull the source content
into the channel.

![Diagram showing data packets flowing from upstream systems to SRT caller inputs in MediaLive.](/images/medialive/latest/ug/images\srt-pull-uss-input.png)
