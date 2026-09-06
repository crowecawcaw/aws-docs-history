

# Amazon GameLift Streams release notes
<a name="release-notes"></a>

The following release notes are in reverse chronological order, with the latest updates listed first. Amazon GameLift Streams was first released in 2025.

## July 31, 2026: Managed shader caching support & stream URL released
<a name="release-notes-07312026"></a>

### Managed shader caching
<a name="release-notes-07312026-shader-caching"></a>

 Amazon GameLift Streams now supports capturing shader caches from designated stream sessions. Captured shader caches are replicated to streaming locations of compatible stream groups and applied automatically in future sessions, reducing start-up times and in-game stuttering. Monitor cache status, storage usage, and stream group associations with the [ListApplicationShaderCaches](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_ListApplicationShaderCaches.html) API or the Amazon GameLift Streams console. You are only charged for storage of the latest shader cache. 

**Learn more:**
+ [Shader Cache](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/shader-caches.html), *Amazon GameLift Streams Developer Guide*

### Stream URL
<a name="release-notes-07312026-stream-url"></a>

 Amazon GameLift Streams now offers stream URLs, which give end users temporary, unauthenticated access to a stream session in supported web browsers. No AWS credentials or client integration required. 

**Learn more:**
+ [Stream URL](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/stream-urls.html), *Amazon GameLift Streams Developer Guide*

## July 24, 2026: Custom aspect ratio and dynamic resolution released
<a name="release-notes-07242026"></a>

### Custom aspect ratio
<a name="release-notes-07242026-custom-aspect-ratio"></a>

 Amazon GameLift Streams now supports configuring a custom aspect ratio per stream session to accommodate different player devices. Supported aspect ratios include landscape, portrait, and square — delivering a full-screen experience without letterboxing or cropping. 

**Learn more:**
+ [Custom stream resolution](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/custom-stream-resolution.html), *Amazon GameLift Streams Developer Guide*

### Dynamic resolution
<a name="release-notes-07242026-dynamic-resolution"></a>

 Amazon GameLift Streams now automatically adjusts the stream resolution to deliver the best visual quality the viewer's network connection can sustain. This feature is enabled by default in Web SDK version 1.3.0 or later. 

**Dynamic resolution and video element sizing**  
When dynamic resolution is active, the stream resolution may change during a session. If the HTML video element used for playback does not have explicit fixed dimensions, the element may visibly resize when the resolution adjusts. To prevent unexpected layout changes, set fixed dimensions on your video element. For details, see [Dynamic resolution in the Amazon GameLift Streams Web SDK release notes](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/web-sdk-release-notes.html).

**Learn more:**
+ [Dynamic resolution](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/web-sdk-release-notes.html), *Amazon GameLift Streams Web SDK Release Notes*

## July 16, 2026: IAM role support for stream sessions released
<a name="release-notes-07162026"></a>

 With IAM role support for stream sessions, your application can now access AWS resources in your account, such as Amazon S3 buckets and DynamoDB tables. When you pass a role ARN on `StartStreamSession`, Amazon GameLift Streams assumes the role on your behalf and makes credentials available to your application automatically. You do not need to change your application code. 

**Learn more:**
+ [Provide AWS credentials to your streaming application](session-credentials.md), *Amazon GameLift Streams Developer Guide*

## July 6, 2026: Stream Session Admin Shell released
<a name="release-notes-07062026"></a>

 Amazon GameLift Streams now offers Stream Session Admin Shell, a secure terminal connection to the live runtime environment of a stream session. Inspect logs, query running processes, check GPU utilization, and examine application state in real time. This feature is available at no additional cost in all AWS Regions where Amazon GameLift Streams is offered. 

**Learn more:**
+ [Stream Session Admin Shell](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/troubleshoot-admin-shell-guide.html), *Amazon GameLift Streams Developer Guide*

## May 20, 2026: Generation 6e stream classes released
<a name="release-notes-05202026"></a>

 Amazon GameLift Streams now offers Generation 6e stream classes, powered by the EC2 G6e instance family. Generation 6e features NVIDIA L40S Tensor Core GPUs and 3rd generation AMD EPYC processors, delivering 2x the GPU memory and up to 2.9x faster GPU memory bandwidth compared to standard Generation 6 stream classes. These classes are designed for streaming high-fidelity, graphically demanding games and applications that benefit from additional GPU memory and performance. Generation 6e stream classes are available in select AWS Regions. 

**Learn more:**
+ [Stream classes](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/configuration-options.html#configuration-options-stream-classes), *Amazon GameLift Streams Developer Guide*

## April 23, 2026: Proton 10 runtime support released
<a name="release-notes-04232026"></a>

 Amazon GameLift Streams now offers Proton 10 as a managed runtime environment for improved compatibility with newer Windows-based applications running on Linux. You must create new Amazon GameLift Streams applications and stream groups to use this new runtime. 

**Learn more:**
+ [Runtime environments](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/configuration-options.html#configuration-options-runtime), *Amazon GameLift Streams Developer Guide*

## March 4, 2026: Additional Generation 6 stream classes released
<a name="release-notes-03042026"></a>

 Amazon GameLift Streams now offers two additional Generation 6 stream classes — gen6n\_small\_win2022 and gen6n\_medium\_win2022. These Microsoft Windows Server 2022 Base classes use NVIDIA L4 Tensor Core GPUs and 3rd generation AMD EPYC processors, providing cost-optimized options for streaming well-optimized or lower-fidelity games on Windows environments. 

**Learn more:**
+ [Stream classes](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/configuration-options.html#configuration-options-stream-classes), *Amazon GameLift Streams Developer Guide*

## January 27, 2026: New locations supported
<a name="release-notes-01272026"></a>

 Amazon GameLift Streams now offers six new locations — ap-northeast-2 (Seoul), ap-south-1 (Mumbai), ap-southeast-2 (Sydney), eu-north-1 (Stockholm), eu-west-2 (London), and sa-east-1 (São Paulo). These new locations help reduce latency and improve gameplay experience for players in those areas. 

**Learn more:**
+ [AWS Regions and streaming locations supported by Amazon GameLift Streams](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/regions-quotas-rande.html), *Amazon GameLift Streams Developer Guide*

## December 16, 2025: Maximum capacity and target-idle capacity, Generation 6 stream classes, and performance stats released
<a name="release-notes-12162025"></a>

### Maximum capacity and target-idle capacity
<a name="release-notes-12162025-capacity"></a>

 Amazon GameLift Streams now configures stream group capacity using two new parameters: maximum capacity and target-idle capacity. Target-idle capacity keeps capacity ready before players create sessions to reduce wait time and improve player experience. Maximum capacity limits the number of sessions that can run at once to help you control costs. These parameters offer improved capacity management for on-demand streaming. 

**Learn more:**
+ [Manage streaming with an Amazon GameLift Streams stream group](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/stream-groups.html), *Amazon GameLift Streams Developer Guide*

### Generation 6 stream classes
<a name="release-notes-12162025-gen6"></a>

 Amazon GameLift Streams now offers Generation 6 stream classes, powered by the EC2 G6 instance family. Generation 6 improves price-performance across a wide range of configurations, making it the best option for both performance-focused and cost-focused use cases. 

**Learn more:**
+ [Stream classes](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/configuration-options.html#configuration-options-stream-classes), *Amazon GameLift Streams Developer Guide*

### Performance stats overlay
<a name="release-notes-12162025-perf-stats"></a>

 Amazon GameLift Streams now provides performance stats for stream sessions. You can receive a live stream of performance data on the client during active sessions, and view a real-time overlay of performance stats alongside your stream on the "Test stream" page in the AWS Management Console. Additionally, the Export stream session files feature now includes a CSV of performance stats for post-session analysis. Stats include application-level data (CPU and memory usage) and shared system-level data (CPU, memory, GPU, and VRAM utilization). 

**Learn more:**
+ [Monitoring Amazon GameLift Streams](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/monitoring-overview.html), *Amazon GameLift Streams Developer Guide*

## August 21, 2025: Default applications update
<a name="release-notes-08212025"></a>

 Amazon GameLift Streams now offers enhanced flexibility for managing default applications in stream groups. You can now create new stream groups without specifying a default application, and modify or remove default applications in existing stream groups. 

**Note**  
Linking a default application is still required before streaming from a stream group.

**Learn more:**
+ [About default applications](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/multi-apps.html#multi-apps-about-linking), *Amazon GameLift Streams Developer Guide*

## August 7, 2025: Proton 9 runtime support released
<a name="release-notes-08072025"></a>

 Amazon GameLift Streams now offers Proton 9 as a managed runtime environment for improved compatibility with newer Windows-based applications running on Linux. You must create new Amazon GameLift Streams applications and stream groups to use this new runtime. 

**Learn more:**
+ [Runtime environments](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/configuration-options.html#configuration-options-runtime), *Amazon GameLift Streams Developer Guide*