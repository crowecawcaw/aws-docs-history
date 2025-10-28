# IVS Chat Infrastructure Security

As a managed service, Amazon IVS is protected by the AWS global network security
procedures. These are described in [Best
Practices for Security, Identity, & Compliance](https://aws.amazon.com/architecture/security-identity-compliance/ "https://aws.amazon.com/architecture/security-identity-compliance/").

## API Calls

You use AWS published API calls to access Amazon IVS through the network. See
[API Calls](../LowLatencyUserGuide/security-infrastructure.md#infrastructure-api-calls "../LowLatencyUserGuide/security-infrastructure.md#infrastructure-api-calls")
under Infrastructure Security in the
_IVS Low-Latency Streaming User Guide_.

## Amazon IVS Chat

Amazon IVS Chat message ingestion and delivery occurs over encrypted WSS
connections to our edge. The Amazon IVS Messaging API uses encrypted HTTPS
connections. As with video streaming and playback, TLS version 1.2 or later is
required and messaging data may be transmitted unencrypted internally for
processing.
