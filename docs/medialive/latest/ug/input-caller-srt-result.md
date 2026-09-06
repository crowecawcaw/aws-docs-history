

# Result of this procedure
<a name="input-caller-srt-result"></a>

As a result of this setup, an SRT caller input exists that specifies one or two *source* URLs. These sources are the URLs for the source content on the upstream system. 

At runtime of the channel, MediaLive (the caller) will perform a handshake with the upstream system (the listener). MediaLive will connect to two URLs (for a standard channel) or one URL (for a single-pipeline channel), and pull the source content into the channel.

![Diagram showing upstream systems sending data packets to two SRT caller input URLs in MediaLive.](http://docs.aws.amazon.com/medialive/latest/ug/images/srt-pull-uss-input.png)
