# Elemental Live

terminology

CDN

A content distribution network (CDN) is a network of servers that is downstream of the origin server or packager. The CDN distributes
the content from the origin server to dozens or hundreds of networked servers that serve the content to your viewing users. This
distributed network ensures that content can be delivered to thousands or millions of viewing users simultaneously.

Downstream system

The _downstream system_ is a set of one or more servers that is positioned after Elemental Live in the
workflow. The downstream system handles the content that is output from Elemental Live.

Encode

An encode exists within an output. There are three types of encodes: video, audio, and captions. Each encode contains the instructions
for one video stream, one audio stream, or one captions track that the transcoding process will create. Different encodes have different
characteristics. For example, one video encode produced from the input might be high resolution while another is low resolution.

Event

An Elemental Live event ingests and transcodes (decodes and encodes) source content from the inputs that are attached to that event,
and packages the new content into outputs.

Event configuration

An Elemental Live event configuration contains information about how the event ingests, transcodes, and packages content into output.

Origin service

An origin service might be part of the downstream system that is positioned after Elemental Live in the workflow. It accepts the video
output from Elemental Live.

Output

An output exists within an output group. It is a collection of encodes that you want to handle as one set.

Output Group

An output group is a collection of outputs within the Elemental Live event.

Packager

A packager might be part of the downstream system. It accepts the video output from Elemental Live and repackages it. AWS Elemental MediaPackage is a
packager.

Playback device

A playback device is the final component of the downstream system. It is the device that the people who are your audience use to view
the video.

Source content

The video content that Elemental Live transcodes. The content typically consists of video, audio, captions, and metadata.

Upstream system

The system that is in front of Elemental Live in the workflow and that holds the source content. Examples of an upstream system are a
streaming camera or appliance that is directly connected to the internet, or a contribution encoder that is located in a stadium at a
sports event.
