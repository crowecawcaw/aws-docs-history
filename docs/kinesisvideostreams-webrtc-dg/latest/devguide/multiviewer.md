# Multiviewer

Amazon Kinesis Video Streams Multiviewer is a cloud-based WebRTC solution that enables multiple viewers to concurrently join a real-time video streaming session from a single camera device. This feature addresses the bandwidth and computational constraints of edge devices by processing video streams in the cloud rather than requiring the camera to send separate streams to each viewer.

###### Topics

- [Overview](#multiviewer-overview "#multiviewer-overview")
- [Requirements and Resources](#multiviewer-requirements "#multiviewer-requirements")
- [Setting Up Multiviewer](#multiviewer-setup "#multiviewer-setup")
- [Integration with Ingestion](#multiviewer-integration "#multiviewer-integration")
- [API Operations](#multiviewer-apis "#multiviewer-apis")
- [Best Practices](#multiviewer-best-practices "#multiviewer-best-practices")

## Overview

Traditional peer-to-peer WebRTC connections require camera devices to send video separately to each viewer, which can quickly overwhelm devices with limited bandwidth or computational capacity. Multiviewer solves this by using a cloud-based "mixer" that:

- Receives a single video stream from the camera device
- Processes and forwards the stream to multiple viewers
- Handles audio mixing for multi-participant conversations
- Preserves edge device compute and bandwidth capacity

Multiviewer is particularly valuable for use cases including:

- **Smart Home Security:** Multiple household members can view camera feeds simultaneously without degrading performance
- **Enterprise Security:** Security teams can monitor feeds concurrently
- **Automotive Monitoring:** Fleet managers and controllers can view vehicle cameras simultaneously
- **Robotics & Drones:** Multiple operators can monitor autonomous systems
- **Education/Proctoring:** Multiple proctors can observe test sessions
- **Telehealth:** Healthcare teams can participate in remote consultations

## Requirements and Resources

To use Multiviewer, you need the following resources:

- **Kinesis Video Streams Stream:** A destination for ingestion and storage of the video and audio content
- **WebRTC Signaling Channel:** Enables connection to devices using the KVS WebRTC SDK
- **Media Storage Configuration:** Links the Stream and Channel using the UpdateMediaStorageConfiguration API

###### Important

Multiviewer is currently only available when coupled with WebRTC Ingestion. Both master or viewer can initiate a WebRTC ingestion session, and the video and audio tracks are simultaneously stored in a Kinesis Video Streams Stream while being distributed to multiple viewers.

**Device Requirements:**

- Camera devices must support the KVS WebRTC SDK
- Viewer applications must use the KVS WebRTC SDK
- All participants connect to the same signaling channel

**Track Requirements:**

- Master participants: Both audio and video tracks are required for WebRTC ingestion
- Viewer participants: Can send an optional audio track or no tracks at all. Viewers cannot send video tracks

## Setting Up Multiviewer

Follow these steps to configure Multiviewer for your application:

1. **Create Required Resources**

Create a Kinesis Video Streams Stream and WebRTC Signaling Channel using the console, CLI, or SDKs. See [Create a video stream](ingestion-create-stream.md "ingestion-create-stream.md") and [Create a signaling channel](ingestion-create-channel.md "ingestion-create-channel.md") for detailed instructions. 2. **Link Resources**

Use the UpdateMediaStorageConfiguration API to link your Stream and Channel. This configuration enables the Multiviewer functionality. See [Configure destination](configure-ingestion.md "configure-ingestion.md") for implementation details. 3. **Configure Camera Application**

Implement the camera application using the KVS WebRTC SDK to call the JoinStorageSession API. This initiates the ingestion session that other viewers can join. 4. **Configure Viewer Applications**

Implement viewer applications using the KVS WebRTC SDK to call the JoinStorageSessionAsViewer API. Multiple viewers can join the same session simultaneously.

## Integration with Ingestion

Multiviewer is built on top of the WebRTC Ingestion capability, which was launched in 2023. This integration provides several benefits:

- **Automatic Recording:** All multiviewer sessions are automatically recorded to Kinesis Video Streams Streams for later playback and analysis
- **Cloud Processing:** Video processing occurs in the cloud, reducing the computational load on edge devices
- **Scalable Architecture:** The cloud-based approach can handle multiple concurrent multiviewer sessions
- **Consistent Experience:** Viewers receive the same high-quality stream regardless of their network conditions

The workflow for a typical multiviewer session with ingestion is:

1. Camera device calls JoinStorageSession to start ingesting video to the cloud
2. Video stream is processed and stored in the configured Kinesis Video Streams Stream
3. Multiple viewer devices call JoinStorageSessionAsViewer to join the session
4. Cloud mixer distributes the video stream to all connected viewers
5. Audio from all participants is mixed and distributed appropriately

## API Operations

Multiviewer uses the same API operations as WebRTC Ingestion. The key APIs include:

- [UpdateMediaStorageConfiguration](../../../kinesisvideostreams/latest/dg/API_UpdateMediaStorageConfiguration.md "../../../kinesisvideostreams/latest/dg/API_UpdateMediaStorageConfiguration.md") - Links a signaling channel to a stream for ingestion
- [JoinStorageSession](../../../kinesisvideostreams/latest/dg/API_webrtc_JoinStorageSession.md "../../../kinesisvideostreams/latest/dg/API_webrtc_JoinStorageSession.md") - Initiates an ingestion session from the camera device
- [JoinStorageSessionAsViewer](../../../kinesisvideostreams/latest/dg/API_webrtc_JoinStorageSessionAsViewer.md "../../../kinesisvideostreams/latest/dg/API_webrtc_JoinStorageSessionAsViewer.md") - Allows viewers to join an active ingestion session
- [DescribeMediaStorageConfiguration](../../../kinesisvideostreams/latest/dg/API_DescribeMediaStorageConfiguration.md "../../../kinesisvideostreams/latest/dg/API_DescribeMediaStorageConfiguration.md") - Retrieves the current media storage configuration

For detailed API usage examples, see [Establish a WebRTC connection with the storage session](getting-started-ingestion.md#ingestion-establish-connection "getting-started-ingestion.md#ingestion-establish-connection").

## Best Practices

Follow these best practices when implementing Multiviewer:

- **Optimize for Edge Devices:** Use Multiviewer specifically when you need more than 2-3 concurrent viewers, as this is where edge device limitations typically become apparent
- **Monitor Session Health:** Implement monitoring to track session quality and viewer connections
- **Handle Connection Failures:** Implement retry logic for both camera and viewer connections
- **Audio Management:** Consider muting viewers by default to prevent audio feedback in large sessions
- **Resource Cleanup:** Ensure proper cleanup of WebRTC connections when viewers leave sessions
