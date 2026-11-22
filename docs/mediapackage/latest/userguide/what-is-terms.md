

# AWS Elemental MediaPackage concepts and terminology

The following are AWS Elemental MediaPackage concepts and terms to be familiar with.

**Channel group**  
A *channel group* is the top-level resource that consists of channels and origin endpoints that are associated with it and that provides predictable URLs for stream delivery. All channels and origin endpoints within the channel group are guaranteed to share the DNS.

**Channel**  
A *channel* represents the entry point for a content stream into MediaPackage. Upstream encoders such as AWS Elemental MediaLive send content to the channel. When MediaPackage receives a content stream, it packages the content and outputs the stream from an endpoint that you create on the channel. There's one channel for each incoming set of adaptive bitrate (ABR) streams.

**Endpoint**  
An *endpoint* is part of a channel and represents the packaging aspect of MediaPackage. When you create an endpoint on a channel, you choose a container type, packaging parameters, and features for the output stream. Downstream devices request content from the endpoint. A channel can have multiple endpoints.

**Just-in-time packaging**  
MediaPackage performs *just-in-time packaging* (JITP). When a playback device requests content, MediaPackage dynamically customizes the live video streams and creates a manifest in a format that's compatible with the requesting device.

**Origination service**  
MediaPackage is considered an *origination service* because it's the point of distribution for media content delivery.

**Packager**  
A *packager* prepares output streams for access by different types of players. MediaPackage delivers Apple HTTP Live Streaming (HLS), low-latency HLS, Dynamic Adaptive Streaming over HTTP (DASH), and Microsoft Smooth Streaming (MSS) manifests. Additional packager settings include buffer and update durations and manifest tag handling instructions.  
A packager is part of an endpoint. Each endpoint has one container type, and a single endpoint can deliver several manifest formats at once, depending on its container type. A channel can have several endpoints, so you can deliver the same content in more than one container type. For instructions on creating an endpoint, see [Creating an origin endpoint](endpoints-create.md).  
The following table lists each container type and the manifest formats it supports.  


<table>
<thead>
  <tr><th>Container type</th><th>Description</th><th>Manifest formats</th></tr>
</thead>
<tbody>
  <tr><td><code>TS</code></td><td>MPEG-2 transport stream</td><td>HLS, low-latency HLS</td></tr>
  <tr><td><code>CMAF</code></td><td>Common Media Application Format</td><td>HLS, low-latency HLS, DASH</td></tr>
  <tr><td><code>ISM</code></td><td>Container for Microsoft Smooth Streaming</td><td>MSS</td></tr>
</tbody>
</table>


**Source Content**  
*Source contents* are live streams and video files that MediaPackage ingests.   
+ For live video, source content comes from an upstream encoder, such as AWS Elemental MediaLive. MediaPackage supports HLS and CMAF source content. For details, see [Supported inputs and outputs](supported-inputs.md).

**Stream**  
A *stream* refers to the content input and output of MediaPackage.   
For live workflows, an upstream encoder sends a live stream as an input to MediaPackage to the channel. When a downstream device requests playback of the content, MediaPackage dynamically packages the stream (applying the endpoint's container type and manifest formats, adding encryption, and configuring track outputs) and delivers it to the requesting device as an output of the endpoint. An endpoint can produce multiple streams.

**Track**  
*Tracks* make up the output content stream. MediaPackage includes selected video, audio, and subtitles or captions tracks in the output stream. The stream delivers the tracks to the player (either directly or through a CDN), and the player plays back the tracks based on player logic or network conditions (such as available bandwidth).