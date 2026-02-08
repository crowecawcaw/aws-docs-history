# Result of this procedure

As a result of this setup, an SRT Listener input exists with one or two
_destination_ URLs. These destinations are the URLs
that MediaLive allocated for receiving the source content.

At runtime of the channel, the upstream system (the caller) will perform a handshake
with MediaLive (the listener). The upstream system will connect to two URLs (for a standard
channel) or one URL (for a single-pipeline channel), and push the source content
into the channel.

![](/images/medialive/latest/ug/images\srt-push-uss-input.png)
