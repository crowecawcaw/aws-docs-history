

# IVS Chat Infrastructure Security
<a name="security-infrastructure"></a>

As a managed service, Amazon IVS is protected by the AWS global network security procedures. These are described in [Best Practices for Security, Identity, & Compliance](https://aws.amazon.com/architecture/security-identity-compliance/).

## API Calls
<a name="infrastructure-api-calls"></a>

You use AWS published API calls to access Amazon IVS through the network. See [API Calls](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/security-infrastructure.html#infrastructure-api-calls) under Infrastructure Security in the *IVS Low-Latency Streaming User Guide*. 

## Amazon IVS Chat
<a name="infrastructure-ivs-chat"></a>

Amazon IVS Chat message ingestion and delivery occurs over encrypted WSS connections to our edge. The Amazon IVS Messaging API uses encrypted HTTPS connections. As with video streaming and playback, TLS version 1.2 or later is required and messaging data may be transmitted unencrypted internally for processing.