# Result of this procedure

As a result of this setup, an RTP input exists that specifies one or two _endpoint_ URLs. These endpoints are on MediaLive and are fixed
for the lifetime of the input, regardless of changes that occur (such as modifying other
information in the input, or attaching the input to a different channel).

The upstream system has been set up to push the source content to the two endpoints
(for a standard channel) or to the first endpoint (for a single-pipeline channel). An
input security group has been associated with the input. This input security group has a
CIDR block that covers the two URLs that the upstream system pushes, which ensures that
MediaLive accepts the pushed content.

Keep in mind that with a push input, the upstream system must be pushing the video
source to the input when you start the channel. The upstream system does not need to be
pushing before then.

At runtime of the channel, MediaLive reacts to the content that is being pushed and
ingests it.

![Upstream system diagram showing IP addresses, RTP inputs, and Input Security Group.](images/rtp-push-uss-input.png)
