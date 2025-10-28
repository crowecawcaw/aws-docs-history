# Result of this procedure

As a result of this setup, an RTMP input exists that specifies one or two
_endpoint_ URLs.
These addresses
are fixed for the lifetime of the input, regardless of changes that occur (such as
modifying other information in the input, or attaching the input to a different
channel).

These endpoints are elastic network interfaces on your VPC.
MediaLive has permission to use these network interfaces for its inputs. MediaLive has
permission (through the IAM trusted entity role) to automatically manage the
network interfaces for its inputs. The upstream system has permission, through the
Amazon VPC security group, to push content to these endpoints.

The upstream system or systems have been set up to push the source content to the
two endpoints (if you are setting up for a standard channel) or to one endpoint (if
you are setting up for a single-pipeline channel). At least one VPC security group
has been associated with each subnet. The CIDR block in each security group covers
the two URLs that the upstream system pushes from, which ensures that MediaLive accepts
the pushed content.

Each output of the upstream system has an IP address in one of the specified
subnets in your VPC. The RTMP input has two IP addresses, and each address is in one
of those subnets. In this way, the delivery of the source content from the upstream
system to MediaLive takes place within the privacy of the VPC.

Keep in mind that with a push input, the upstream system must be pushing the video
source to the input when you start the channel. The upstream system does not need to
be pushing before then.

At runtime of the channel, MediaLive reacts to the content that is being pushed and
ingests it.

![Diagram showing RTMP input in MediaLive with upstream systems connecting to VPC subnets.](/images/medialive/latest/ug/images\rtmp-vpc-uss-input.png)
