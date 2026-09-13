

# SMCOST03-BP01 Implement thorough video quality assessment
<a name="smcost03-bp01"></a>

Every bit saved in encoding translates directly to reduced delivery cost. A 20% bit rate reduction across a content catalog means 20% lower CDN spend. The challenge is identifying where those bits can be removed without degrading what viewers actually perceive. Organizations that don't measure quality systematically either overspend on delivery (encoding at higher bitrates than necessary) or underdeliver on experience (encoding too aggressively without knowing it).

**Desired outcome:**
+ You have automated objective quality scoring integrated into your encoding pipeline that evaluates every output against its source.
+ You have rate-quality curves per content type that identify the bit rate point where additional bits yield diminishing perceptual improvement.
+ You have real-user quality-of-experience metrics from player telemetry that validate whether lab-measured quality correlates with actual viewer satisfaction.

**Common anti-patterns:**
+ Encoding all content at a fixed high bit rate without measuring whether the quality improvement justifies the additional delivery cost.
+ Relying solely on objective metrics without validating perceived quality through subjective testing or viewer feedback.
+ Making encoding parameter changes without measuring before-and-after quality and cost impact, blocking data-driven optimization decisions.
+ Treating quality assessment as a one-time activity rather than ongoing monitoring that detects regressions from encoder updates or configuration changes.

**Benefits of establishing this best practice:**
+ Delivery costs decrease because measured quality data reveals where bit rate can be reduced without perceptible quality loss.
+ Viewer experience is maintained or improved because optimization decisions are grounded in perceptual measurement rather than arbitrary bit rate targets.
+ Encoding regressions are detected before they reach large audiences because automated scoring flags quality drops after encoder changes.
+ Content-specific optimization becomes possible because rate-quality curves reveal different bit rate requirements for different content complexity levels.

**Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

Three measurement approaches serve different purposes and no single approach is sufficient alone. Objective metrics provide automated, repeatable scoring at scale. Subjective assessment validates that objective scores correspond to human perception for your specific content. Real-user telemetry closes the loop between lab conditions and production reality.

Objective tools measure mathematical differences between source and encoded output. PSNR (Peak Signal-to-Noise Ratio) measures pixel-level differences but correlates poorly with human perception for many content types. SSIM (Structural Similarity Index) better captures structural degradation. VMAF (Video Multi-Method Assessment Fusion), developed by Netflix, combines multiple quality indicators through machine learning and generally correlates best with human judgment for streaming content. VMAF scores are available through FFmpeg with the libvmaf library and can be integrated directly into encoding pipelines. A VMAF score above 93 is typically considered excellent for streaming delivery. Scores below 70 indicate visible degradation for most viewers.

Objective metrics have blind spots. Compression artifacts like banding in gradients, mosquito noise around high-contrast edges, and temporal flickering may score acceptably on VMAF but are immediately noticeable to viewers on certain displays or content types. Subjective testing catches these cases. The testing doesn't need to be elaborate. Viewing encoded outputs on representative displays under normal viewing conditions, with attention to known problem content (dark scenes, gradients, and text overlays), identifies artifacts that metrics miss.

Real-user metrics from player telemetry connect encoding choices to actual viewer outcomes. Rebuffering events indicate bit rate exceeds available throughput for some viewers. Bit rate selection data shows which ABR ladder rungs are actually used (unused rungs represent wasted encoding compute). Time-to-first-frame correlates with initial segment size. Aggregating these metrics by content type, encoding profile, and device type reveals which encoding configurations serve viewers well and which cause problems in production conditions that lab testing can't replicate.

Rate-quality curves map the relationship between bit rate and quality score for a specific piece of content. Plotting VMAF against bit rate reveals the saturation point where additional bits produce negligible quality improvement. This point differs by content complexity. A news anchor against a static background saturates at a far lower bit rate than a high-motion sports broadcast. Identifying these saturation points per content category sets the bit rate ceiling for each category and reveals where current encoding allocates bits beyond the point of diminishing returns.

### Implementation steps
<a name="implementation-steps"></a>

1. **Integrate objective quality scoring into the encoding pipeline:** Add VMAF scoring (through FFmpeg with libvmaf or an equivalent tool) as a post-encoding step that evaluates each output rendition against the source. Store scores alongside content metadata. Set alert thresholds (for example, VMAF below 80) that flag outputs for human review before publication.

1. **Build rate-quality curves for your content categories:** Encode representative samples from each content category at multiple bit rate points:
+ News
+ Sports
+ Drama
+ Animation
+ User-generated

Plot VMAF against bit rate for each. Identify the saturation point per category where a 20% bit rate increase yields less than a 2-point VMAF improvement. Use these saturation points to set maximum bit rate targets per content category.

1. **Establish subjective quality review for edge cases:** Create a review process where team members evaluate encoded content on target displays (mobile devices, large screens, HDR displays). Focus on known problem content.
+ Dark scenes
+ Gradients
+ Text overlays
+ High-motion sequences

Document artifacts that score acceptably on objective metrics but are visually objectionable.

1. **Instrument player telemetry for quality-of-experience metrics:** Configure video players to report the following:
+ Rebuffering events
+ Bit rate selection and switches
+ Time-to-first-frame
+ Playback errors

Aggregate by content type, encoding profile, device type, and network condition. Use [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) or a streaming analytics pipeline to store and query this data.

1. **Correlate encoding configurations with viewer experience:** Join player telemetry data with encoding configuration metadata. Identify encoding profiles that correlate with high rebuffering rates (bit rate too high for audience network conditions) or low engagement (quality too low for viewer expectations). Use these correlations to adjust encoding targets.

1. **Monitor for quality regressions after changes:** Establish quality baselines per content category. After encoder software updates, configuration changes, or pipeline modifications, compare new output scores against baselines. Alert on regressions (for example, average VMAF drop of more than 2 points for the same content category). Don't assume encoder updates improve quality without measurement.

## Resources
<a name="resources"></a>

**Related best practices**
+ [SMCOST03-BP02 Optimize encoder settings based on content type](smcost03-bp02.html)
+ [SMCOST01-BP02 Optimize content delivery using edge caching and just-in-time packaging](smcost01-bp02.html)

**Related documents**
+ [VMAF - Video Multi-Method Assessment Fusion](https://github.com/Netflix/vmaf)
+ [AWS Quality-Defined Variable Bitrate (QVBR)](https://aws.amazon.com/media/tech/quality-defined-variable-bitrate-qvbr/)

**Related services**
+ [AWS Elemental MediaConvert](https://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html)
+ [AWS Elemental MediaLive](https://docs.aws.amazon.com/medialive/latest/ug/what-is.html)
+ [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)