# Streaming media layer

The streaming media layer includes five focus areas that we define
as the components necessary to transmit audio and video from
content publishers to audiences — Ingest, Processing, Origin,
Delivery, and Client.

## Ingest

Ingest components contribute real-time and file-based content to
your streaming media workload. Ingest includes the devices and
network used to deliver media sources to cloud entry points for
content processing and distribution. 

Ingest design will vary greatly depending on the level of
control and the access that you have to the content provider
infrastructure. Focus should be on the source quality, latency,
network performance (jitter, link loss, throughput), security
(in-transit encryption, entry point authentication), and
redundancy of the ingest architecture.

Encoding devices, such as **AWS Elemental
Live** and **AWS Elemental
Link**, convert live uncompressed video and audio from
Serial Digital Interface (SDI), IP, or HDMI into a compressed
format necessary for contributing to AWS over IP network. These
devices are deployed on-site at the event or broadcast facility.

Content owners need to manage and transport real-time content
throughout the cloud for redundancy or to grant partners or
affiliates access. You might ingest source content directly to
an Amazon EC2 host entry point, but reliably managing this
infrastructure can become
burdensome. **AWS Elemental MediaConnect** lets you securely and reliably transport
high-quality live video between a remote event site to the AWS Cloud, between services within AWS Regions, or between partners
and affiliates. For live production workloads working with
uncompressed video, the **AWS Cloud
Digital Interface** allows you to integrate
uncompressed video transport into your workflow.

For reliability or performance objectives that require a
dedicated network connection from your facility or event site to
AWS, **AWS Direct Connect**
establishes a more consistent network experience for live
streaming or bulk upload of file-based content.

For file-based content, if you aren’t able to leverage Direct
Connect due to source location,
**Amazon** **S3
Transfer Acceleration** and **AWS Global Accelerator**let you use the Amazon CloudFront
global edge network to optimize the network path for content
upload. Transfer Acceleration can be combined with
**Amazon** **S3
Multipart Upload** to ingest large media files as a set
of parts uploaded in parallel. When all parts of your asset are
uploaded, Amazon S3 then presents it as a single object. 

For bulk file-based ingest tasks, such as archive migrations and
content acquisition that exceed the limitations of network
transfer,**AWS Snow
Family** provides data migration and edge computing
devices that are well suited for large-scale data transfer.
**AWS Snowball Edge Edge** provides
multiple device options optimized for data transfer
(storage-optimized) and edge compute (compute-optimized with
optional GPU) for use cases like video analysis and metadata
generation in disconnected production environments. 

## Processing

To ensure quality distribution, many organizations ingest media
at a bitrate that is higher than will be distributed to end
users, but much lower than uncompressed video. Using an
intermediary, mezzanine format affords the flexibility to
re-format content in accordance with the evolving landscape of
audience device requirements and compression algorithm evolution
without requesting new sources from the content provider.
Processing content from a mezzanine source also improves the
audio and visual quality of the compressed content delivered to
your audience.

The purpose of the processing component is to convert video from
an intermediary mezzanine format into a format that is optimized
for streaming. Processing has two main stages — transcoding the
audio samples and video frames, and packaging the media essence
data into a container format suitable for client consumption.
Transcoding converts content from high-quality, high-bitrate
mezzanine codecs into codecs optimized for web delivery, such as
h.264. Packaging puts the media tracks (audio, video, captions)
into a format that is compatible with consumer devices,
typically an Adaptive Bitrate (ABR) format. Processing content
into ABR formats like Apple HTTP Live Streaming (Apple HLS) or
MPEG-DASH allows content to be streamed at scale over HTTP and
enables the device to select the appropriate rendition given the
network throughput to the user. It’s also common to embed
advertising opportunity signals, insert captions or subtitles
for accessibility, and apply content protection schemes while
processing media.

**AWS Elemental MediaLive** and
**AWS Elemental MediaConvert**
providebroadcast-grade,
fully managed video processing and packaging for multi-screen
and intermediate formats.  Using these services for processing
tasks allows you to offload operational and reliability concerns
of managing a processing fleet to AWS. Your processing component
might also include control plane logic to run a sequence of
tasks associated with processing, such as metadata extraction
and quality control. Use serverless technologies,
like **AWS Step Functions, AWS Lambda,** and messaging services, like
**Amazon SQS,** to coordinate
workflow tasks for content processing. 

## Origin

The origin serves streaming media in response to client requests
proxied through a content delivery network (CDN).

**Amazon Simple Storage Service**
(**Amazon S3**)provides highly
available, highly durable, object storage that can be used as a
simple origin for streaming media content when combined with
a CDN, such as **Amazon CloudFront**.  If you prefer the simplicity and
performance of an object store but are looking for
media-specific optimizations like stale-manifest
deletion, **AWS Elemental
MediaStore** provides a performance-optimized content
origination service with low request latencies and strong
read-after-update consistency necessary for adaptive bitrate
protocol manifests.

In addition to serving content, some origin components can apply
just-in-time packaging logic to the delivery based on context
from the requesting devices. For example, a
just-in-time-packaging origin can re-package to multiple
protocols or apply different types of DRM from a single set of
adaptive bitrate media. If you have business requirements to
support dynamic re-packaging of content based on the requesting
device, apply multi-DRM, filter adaptive bitrate renditions, or
provide DVR-like functionality (start-over, pause, rewind, etc.)
to your live stream. Just-in-time packaging origins
like **AWS Elemental
MediaPackage** make it easy to implement intelligent
origination features for live and video-on-demand streaming.

To monetize streaming media content, server-side ad insertion
services like **AWS Elemental
MediaTailor** manipulates the manifest served by the
content origin to insert personalized advertisements. This can
be done on Live streaming content or VOD content. Advertisements
are seamlessly stitched into the content and can be tailored to
individual viewers, maximizing monetization opportunities for
every ad break and mitigating ad blocking.

## Delivery

The delivery component is the boundary between your
infrastructure and last-mile internet service providers that
connect you with end users. Typically, this is a CDN with many
points of presence (PoP) in major metropolitan areas for edge
caching of media, improving client performance and offloading
requests from your origination layer. A CDN can also help you
secure and control access to content with features such as
geo-blocking, SSL termination, and URL tokenization.
**Amazon CloudFront** is a CDN
service that offers security features such
as **AWS WAF** and
**AWS Shield**, which can protect
your application from malicious requests and distributed denial
of service (DDoS) attacks.

Workloads with high-scale and global audiences often use
multiple CDNs, but this can increase origin load and reduce
cache efficiency. A centralized caching layer, often called an
origin shield, helps scale your origin layer by providing a
single caching layer to collapse requests from viewers or CDNs
into a single origin request. **Amazon CloudFront Origin Shield** is an additional layer
within the CloudFront caching infrastructure that can minimize
your origin’s load, improve its availability, and reduce its
operating costs. 

Delivering content to a wide device ecosystem might require
customizations performed through HTTP header manipulation or
stream manifest manipulation. **AWS Lambda@Edge** and **Amazon CloudFront Functions** let you run code closer to users
so that you can perform optimizations during request and
response without imposing requirements on your origin
infrastructure.

## Client

A client is any mobile device, personal computer, smart TV, or
connected hardware device that can communicate over HTTP,
retrieve web assets from the application layer, and render the
viewer experience. For streaming media, the client presents a
user interface, requests media streams, decodes media, and sends
telemetry information about the playback experience to your
monitoring and analytics systems. The client is also responsible
for working with the browser or device hardware to securely
decrypt media. You’re responsible for building, deploying, and
maintaining your client applications, but
**Amazon Interactive Video
Service** provides a player and frameworks like
**AWS Amplify** help to
accelerate your development effort. 

## Monitoring

The monitoring component provides you with information on the
current state of your streaming media workload and quality of
experience for the audience. 

Monitoring your streaming infrastructure is necessary to detect
system-wide performance changes, optimize resource utilization,
and to baseline workload operational health. For example, if
you’re receiving live content from a content provider, you
should monitor for the expected number of ingest bytes per
second and respond to alerts when ingest fails to meet baseline
expectations. AWS services, including AWS Media Services,
publish metrics and alerts like these
to **Amazon CloudWatch**,
which provides data and actionable insights to monitor your
streaming media workload.

Re-buffering, failed starts, and long load times will quickly
degrade viewer experience and satisfaction. Capturing telemetry
information from playback sessions will help you optimize your
streaming workload and troubleshoot poor playback experiences.
Viewer analytics (seek, skip, play time) should be used also to
curate content recommendations or to enable your business
leaders make content production decisions. Capturing telemetry
and analytics from your streaming media applications is
difficult to deploy and scale for high-viewership
platforms. **Amazon Kinesis Data Streams**is a massively scalable and durable real-time
data streaming service. Kinesis Data Streams can continuously
capture gigabytes of data per second from hundreds of thousands
of viewers.
