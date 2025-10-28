# IVS Resilience

IVS APIs use the AWS global infrastructure and is built around AWS Regions
and Availability Zones. AWS Regions provide multiple Availability Zones, which
are:

- Physically separated and isolated.
- Connected with low-latency, high-throughput, highly-redundant
  networking.
- More available, fault tolerant, and scalable than traditional single or
  multiple data-center infrastructures.
  For more information on the APIs, see the
  [IVS Low-Latency
  Streaming API Reference](../LowLatencyAPIReference/Welcome.md "../LowLatencyAPIReference/Welcome.md"),
  [IVS Real-Time
  Streaming API Reference](../RealTimeAPIReference/Welcome.md "../RealTimeAPIReference/Welcome.md"), and
  [IVS Chat API Reference](../ChatAPIReference/Welcome.md "../ChatAPIReference/Welcome.md").
  For more information on AWS Regions and Availability Zones, see
  [AWS Global
  Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/ "https://aws.amazon.com/about-aws/global-infrastructure/").

## Amazon IVS Video Data Plane

Video ingestion and distribution run over a global content delivery network (CDN)
optimized for low-latency video. This enables Amazon IVS to provide customers with
end-to-end, high quality video served to a global audience with minimal delay. The
video CDN has global Points-of-Presence (PoPs), allowing broadcasters and viewers to
be geographically dispersed.

Regardless of the AWS region where you chose to configure your Amazon IVS
resources:

- Streamers automatically ingest video to a PoP geographically close to
  their location.
- Viewers stream video via the global video CDN.

Once ingested, video streams are processed and transcoded in one of several Amazon
IVS datacenters. Amazon IVS does not provide automated failover for ingestion or
transcoding failures. Instead, streamers should configure their encoders or
broadcasting clients to automatically re-ingest on any broadcasting failures.
