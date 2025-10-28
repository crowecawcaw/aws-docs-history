# Glossary

## Ad Decision Service

A service that determines how to fill an advertising placement
opportunity.

## Ad Decision Splicer

A service that dynamically inserts advertisements into media,
typically in conjunction with an Ad Decision Service.

## Adaptive Bitrate (ABR) streaming

A technique for delivering media to a client by providing a set of
identical content renditions at varying qualities and allowing the
client to select the most appropriate version based on bandwidth
and decoder performance.

## Apple HTTP Live Streaming (Apple HLS)

Released by Apple as an adaptive bitrate protocol primarily for
iOS distribution, HTTP Live Streaming (HLS) has become the
standard for transmitting material to client devices. Because it
implements the MPEG Transport Stream container, the elementary
stream packetization for audio, video, captions, and ad signaling
is well understood and supported by many consuming applications.
The primary challenge for HLS contribution is the delay it
introduces. HLS segments are approximately 10 seconds in size and,
because Apple recommends a buffer of three, it’s common to
experience video decoder buffers of 30 seconds or more.

## Adobe Real-Time Messaging Protocol (Adobe RTMP)

Originally developed as a proprietary protocol by Macromedia, the
Adobe Real-Time Messaging Protocol (RTMP) has been widely used
over the past decade for progressive video delivery. In recent
years, the popularity for RTMP has subsided for client
distribution due to the proliferation of HTTP-based adaptive
bitrate protocols. However, for media contribution, it’s widely
used due to its ubiquitous presence within open source and
commercial live encoding applications. Though praised for wide
adoption and relatively low latency, RTMP is not without
challenges. Specifically, proprietary and often ad-hoc
implementations of caption and ad insertion data from in the
ecosystem can create challenges.

## AWS Global Accelerator

As a method to improve the global availability and performance of your application,
the [AWS Global Accelerator](https://aws.amazon.com/global-accelerator/ "https://aws.amazon.com/global-accelerator/") helps you build a secure, highly scalable, fault-tolerant and
multi-Region application.

## codec

A portmanteau of the words COder and DECoder, a codec is a
standard algorithm for digital media encoding. Examples include:
H.264, HEVC, AV1, and MPEG-2.

## container

Also known as a _format_ or
_package_, a container is a standard for
associating audio, video, and metadata into a file system
structure. This can be as a single file or as a collection of
multiple files, depending on the container type. Examples include:
MP4, MPEG-2 TS, QuickTime (MOV), or WMV.

## Content Delivery Network (CDN)

A distributed network of servers that delivers web content to end
users.

## content provider

A creator of media content that wants to reach an audience.

## Digital Rights Management (DRM)

Services and functionality that enable content owners to determine
who and how their content is accessed.

## encoder

A service that converts digital video from one format to another,
typically to facilitate distribution.

## Real-time Transport Protocol (RTP)

Developed by the Internet Engineering Task Force (IETF), Real-time
Transport Protocol (RTP) is a network protocol designed for
delivery of audio and video over IP. Its basis on UDP (low
latency), flexibility, and wide application for media workloads
make RTP an ideal ingest protocol. We strongly recommend using
Forward Error Correction in conjunction with RTP to account for
network packet loss. Column and row depth configurations will be
network dependent.

## origin

A service hosting content.

## packager

A service that reformats, multiplexes, or repackages media without
re-encoding.

## Quality Control (QC)

A process for ensuring that the output content is of sufficient
quality.
