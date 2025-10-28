# Amazon Kinesis Video Streams system requirements

The following sections contain hardware, software, and storage requirements for
Amazon Kinesis Video Streams.

###### Topics

- [Camera requirements](#system-requirements-cameras "#system-requirements-cameras")
- [Tested operating systems](#system-requirements-cameras-os "#system-requirements-cameras-os")
- [SDK storage requirements](#system-requirements-sdk "#system-requirements-sdk")

## Camera requirements

Cameras that are used for running the Kinesis Video Streams producer SDK and samples have the
following memory requirements:

- The SDK content view requires 16 MB of memory.
- The sample application default configuration is 512 MB. This value is
  appropriate for producers that have good network connectivity and no
  requirements for additional buffering. If the network connectivity is poor and
  more buffering is required, you can calculate the memory requirement per second
  of buffering by multiplying the frame rate per second by the frame memory size.
  For more information about allocating memory, see [StorageInfo](producer-reference-structures-producer.md#producer-reference-structures-producer-storageinfo "producer-reference-structures-producer.md#producer-reference-structures-producer-storageinfo").

We recommend using USB or RTSP (Real Time Streaming Protocol) cameras that encode data
using H.264 because this removes the encoding workload from the CPU.

Currently, the demo application doesn't support the User Datagram Protocol (UDP) for RTSP streaming. This
capability will be added in the future.

The producer SDK supports the following types of cameras:

- Web cameras.
- USB cameras.
- Cameras with H.264 encoding (preferred).
- Cameras without H.264 encoding.
- Raspberry Pi camera module. This is preferred for Raspberry Pi devices because
  it connects to the GPU for video data transfer, so there is no overhead for CPU
  processing.
- RTSP (network) cameras. These cameras are preferred because the video streams
  are already encoded with H.264.

## Tested operating systems

We have tested web cameras and RTSP cameras with the following devices and
operating systems:

- Mac mini
  - High Sierra

- MacBook Pro laptops
  - Sierra (10.12)
  - El Capitan (10.11)

- HP laptops running Ubuntu 16.04
- Ubuntu 17.10 (Docker container)
- Raspberry Pi 3

## SDK storage requirements

Installing the [Upload to Kinesis Video Streams](producer-sdk.md "producer-sdk.md") has a
minimum storage requirement of 170 MB and a recommended storage requirement of 512
MB.
