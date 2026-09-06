

# CMAF ingest in AWS Elemental MediaPackage
<a name="cmaf-ingest"></a>

AWS Elemental MediaPackage Version 2 (v2) supports CMAF ingest. CMAF ingest delivers content to viewers in multiple streaming formats from a single ingest workflow. CMAF ingest provides flexibility and features to optimize your streaming experience.

The topics in this section cover CMAF ingest.

## Choosing a MediaLive output group for MediaPackage CMAF ingest
<a name="choosing-medialive-output-group"></a>

When configuring AWS Elemental MediaLive to send content to MediaPackage, you can choose between two output group types for CMAF ingest. Your choice affects which capabilities are available for stream control and presentation in your streaming workflow.

### When to use each output group
<a name="medialive-output-group-comparison"></a>

Use this guidance to determine the output group that best fits your streaming requirements:

When to use CMAF Ingest output group  
+ You have a simpler workflow that doesn't require custom stream ordering or naming
+ You want to configure the system simply with minimal setup
+ Stream order and custom properties are not critical for your use case

When to use MediaPackage output group  
+ You need additional passthrough capabilities for stream metadata
+ You want to preserve the exact order of streams as configured in MediaLive
+ You need enhanced control over stream presentation and properties

### How each output group works
<a name="medialive-output-group-details"></a>

CMAF Ingest output group  
The CMAF Ingest output group provides straightforward CMAF ingest with minimal configuration. MediaPackage extracts metadata from the initialization segments and uses MP4 segments to generate manifests. This output group requires simpler setup but provides standard stream handling.

MediaPackage output group  
The MediaPackage output group enables additional passthrough capabilities and desired stream ordering when customers choose this output group instead of the CMAF Ingest output group. This provides enhanced control over how streams are presented in output manifests.

The following table compares the capabilities available with each MediaLive output group:


**Capability comparison between MediaLive output groups**  

| Capability | CMAF Ingest Output Group | MediaPackage Output Group | 
| --- | --- | --- | 
| Stream order preservation | Standard (alphabetical order in output manifest) | Enhanced (preserves desired stream ordering) | 
| Stream metadata passthrough | Standard | Enhanced (additional passthrough capabilities) | 
| Setup complexity | Simple | More configuration options | 

## Enhanced CMAF capabilities with MediaPackage output groups
<a name="enhanced-cmaf-capabilities"></a>

When using the MediaPackage output group in MediaLive, AWS Elemental MediaPackage provides additional passthrough capabilities and desired stream ordering. These enhanced capabilities give you greater control over how streams are presented to viewers in your streaming applications.

### Stream ordering preservation
<a name="cmaf-stream-ordering"></a>

When you choose the MediaPackage output group in MediaLive, the desired stream ordering configured in MediaLive is preserved in the output manifests. This allows you to control how different video, audio, and subtitle streams appear to viewers.

Stream ordering preservation helps you:
+ Ensure viewers start with your intended default streams
+ Present quality choices in your preferred order
+ Organize streams logically for better viewer navigation

### Additional passthrough capabilities
<a name="cmaf-passthrough-capabilities"></a>

The MediaPackage output group provides additional passthrough capabilities that enable enhanced stream metadata to be preserved from MediaLive to the output manifests.

These capabilities support:
+ Enhanced stream identification and presentation
+ Improved viewer experience through better stream organization
+ More control over how streams appear in player interfaces

## Output locking mode for CMAF channels
<a name="output-locking-mode"></a>

When you create a CMAF channel in AWS Elemental MediaPackage, you choose an output locking mode. Use this mode to control how segments are aligned and presented in output manifests. The output locking mode affects segment duration, media sequence numbering, and DRM key rotation behavior.

### Understanding output locking modes
<a name="output-locking-mode-options"></a>

MediaPackage supports two output locking modes for CMAF channels:

Epoch locked (default)  
Epoch-locked mode synchronizes segment boundaries across channels relative to a fixed epoch reference point. Use this mode when you need cross-region synchronization or failover capabilities. This is the default behavior for CMAF channels.

Non-epoch locked  
Non-epoch-locked mode decouples segment alignment from the epoch reference point. Use this mode for single-region workflows where you don't need cross-region synchronization and you want predictable segment durations and target duration values in output manifests.

**Important**  
You can't change the output locking mode after you create a channel. To switch modes, you must create a new channel.

### When to use each mode
<a name="output-locking-mode-when-to-use"></a>

Consider the following factors to choose the output locking mode for your workflow:

When to use epoch-locked mode  
+ You need cross-region synchronization or failover.
+ You have redundant channels in multiple AWS Regions that must produce identical manifests.
+ You want DRM key rotation at fixed intervals from a common reference point.

When to use non-epoch-locked mode  
+ You have a single-region workflow that doesn't require cross-region failover.
+ You want the HLS target duration to be the same as the configured output segment duration.
+ You don't need to maintain epoch alignment, which can create large segments for the service to maintain alignment with epoch boundaries.
+ You want your upstream encoder to be able to change frame rate or input segment duration during a session.
+ You want DRM key rotation based on the endpoint's last modified time instead of a fixed epoch.

### Behavior differences between modes
<a name="output-locking-mode-differences"></a>

The following table compares how each output locking mode affects manifest and segment behavior:


**Comparison of output locking modes**  

| Behavior | Epoch locked | Non-epoch locked | 
| --- | --- | --- | 
| HLS EXT-X-TARGETDURATION | Inflates up to 2x the configured segment duration when SCTE is enabled. | Equals the configured segment duration. | 
| HLS MediaSequenceNumber | The service derives this value from the epoch reference. | Starts at 0 and increases monotonically. | 
| Segment durations | Can produce large combined segments for epoch alignment. | Cluster around the configured segment duration value. | 
| DASH period start times | Aligned to epoch reference. | Uses actual start times. | 
| DRM key rotation interval | Fixed intervals from epoch 0. | Fixed intervals from endpoint or DRM configuration last modified time. | 
| Encoder frame rate and input segment duration changes | Not supported during a session. | Supported during a session. | 
| Cross-region synchronization | Supported. | Not supported. | 

### Output timestamp mode for non-epoch-locked channels
<a name="output-timestamp-mode"></a>

For non-epoch-locked CMAF channels, you can configure an output timestamp mode on the origin endpoint's segment configuration. Use this setting to control how presentation timestamp (PTS) values appear in output segments.

MediaPackage supports the following output timestamp modes:

Passthrough (default)  
Preserves the raw PTS values from the input stream without modification.

Rebased to channel start  
Rebases output PTS values to start close to 0 relative to the first input segment. This produces smaller PTS values in output segments.

**Note**  
The output timestamp mode is only available for non-epoch-locked CMAF channels. You can't change this setting after you create the origin endpoint.

If you use the rebased-to-channel-start mode and the upstream encoder restarts, we recommend that you reset the origin endpoint. For more information about resetting, see [Resetting channel history in AWS Elemental MediaPackage](channel-reset.md).