

# SMSEC03-BP01 Implement content or sessions forensics
<a name="smsec03-bp01"></a>

If content is found outside of your normal operation workflows, you will want to can identify where or how the content was accessed to close a gap.

**Desired outcome:**
+ With monitoring, you can trace content back to where it was originally accessed to lock down any unauthorized access. You will have a full content protection scheme across all distribution channels and formats

**Common anti-patterns:**
+ Organizations distribute premium content without any watermarking or forensic tracking capability, making it impossible to identify the source of leaked content when pirated copies appear online.
+ Teams implement only visible watermarks that can be cropped or obscured, without complementary invisible forensic watermarks that survive re-encoding and screen capture.
+ Organizations use a single watermark identifier across all viewers rather than per-session watermarking, so that attribution of leaked content to a specific user or device isn't possible.
+ Teams fail to maintain a mapping between watermark identifiers and viewer sessions, rendering forensic watermarks useless for tracing content leaks back to their source.
+ Organizations don't monitor piracy detection services or torrent sites for their watermarked content, missing opportunities to identify and close unauthorized distribution channels.

**Benefits of establishing this best practice:**
+ Per-session forensic watermarks enable identification of the specific viewer account or device responsible for content leaks, supporting legal action and account termination.
+ Visible and invisible watermarking creates a credible threat of detection that discourages unauthorized recording and redistribution by viewers aware of the tracking capability.
+ Automated detection of watermarked content on piracy sites enables swift takedown requests and identification of compromised distribution channels before widespread redistribution occurs.
+ Demonstrating strong forensic watermarking capability to content owners and studios strengthens licensing negotiations and satisfies security requirements for premium content access.
+ Forensic analysis of leaked content reveals which distribution channel or device type was compromised, enabling targeted security improvements to close specific vulnerabilities.

**Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

As an example, you might have seen content on an inflight entertainment system that had the name of the airline embedded on the content. This overlay might appear periodically or throughout the entire piece of content and is used by content owners to determine if leaked content originated from an airline. Video encoders like AWS Elemental MediaConvert can burn in these visible watermarks into your content as an identifiable image overlay. While straightforward and effective for a few unique watermarks, this method requires a unique piece of content for each watermark and is therefore limited by the cost of storing multiple versions of the same content.

For large-scale per-viewer, implement a content identification strategy to trace back to specific clients, such as per-user session-based watermarking. With this approach, media is conditioned during transcoding and the origin serves a uniquely identifiable pattern of media segments to the end user. A session to a user-mapping service receives encrypted user ID information in the header or cookies of the request context and uses this information to determine the uniquely identifiable pattern of media segments to serve to the viewer. This approach requires multiple distinctly watermarked copies of content to be transcoded, with a minimum of two sets of content for A/B watermarking. Forensic watermarking also requires YUV decompression, so encoding time for 4K feature length content may take longer than normal. Digital rights management (DRM) service providers in the AWS Partner Network (APN) are available to aid in the deployment of per-viewer content forensics.

### Implementation steps
<a name="implementation-steps"></a>

1. **Implement watermarking for video on demand (VOD) content:** [Implement Nielsen watermarking in MediaConvert](https://docs.aws.amazon.com/mediaconvert/latest/ug/setting-up-non-linear-watermarking.html) for VOD content.

1. **Evaluate partner solutions:** [Consider partner solutions for additional watermarking workflows](https://aws.amazon.com/blogs/media/securing-media-content-using-watermarking-at-the-edge/).

## Resources
<a name="resources"></a>

**Related best practices**
+ [SMSEC06-BP02 Select a content protection scheme that meets business objectives](smsec06-bp02.html)

**Related documents**
+ [Securing Media Content Using Watermarking at the Edge](https://aws.amazon.com/blogs/media/securing-media-content-using-watermarking-at-the-edge/)

**Related services**
+ [AWS CloudFront](https://aws.amazon.com/cloudfront/)
+ [AWS Elemental MediaConvert](https://aws.amazon.com/mediaconvert/)