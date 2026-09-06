

# Result of this procedure
<a name="setup-result-rtmp-pull"></a>

As a result of this setup, an RTMP pull input exists that specifies one or two *source* URLs. These sources are the URLs for the source content on the upstream system. 

At runtime of the channel, the input will connect to two URLs (for a standard channel) or one URL (for a single-pipeline channel), and pull the source content identified by the application name and instance name into MediaLive.

![Diagram showing upstream systems sending GET requests to two input URLs with different IP addresses.](http://docs.aws.amazon.com/medialive/latest/ug/images/rtmp-pull-uss-input.png)
