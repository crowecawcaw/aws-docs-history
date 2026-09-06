

# Release notes for Amazon Nova 2
<a name="release-notes"></a>

Subscribe to the RSS feed so updates to these notes are delivered to your inbox.

## Amazon Nova 2 Sonic
<a name="release-notes-nova2-sonic"></a>

The following sections list the updates and refreshes for the Amazon Nova 2 Sonic model, with the most recent release first.

## May 2026
<a name="release-notes-2026-05"></a>

The Amazon Nova 2 Sonic refresh (May 2026 release) improves speech generation quality for real-time conversational AI.
+ Reduced speech generation hallucinations by 88% on an internal data set, improving verbatim fidelity in alphanumeric codes, currency values, addresses, email addresses, and phone numbers.
+ Reduced speaker drift by 52% on an internal data set for customer service use cases, delivering more consistent voice quality throughout a conversation, turn after turn.
+ Reduced overall critical errors in speech generation by 28% on an internal data set for customer service use cases, improving the accuracy and reliability of voice interactions.
+ No regressions: speech understanding accuracy and latency remain stable.

The refresh was deployed automatically as an in-place update to the current production model. No changes to the API or model configuration are needed. Deployment began on May 21, 2026, and completed across all Regions on May 28, 2026.

Amazon Nova 2 Sonic continues to be generally available in the US East (N. Virginia), US West (Oregon), Asia Pacific (Tokyo), and Europe (Stockholm) Regions. In addition, it is available through Amazon Connect in the following Regions: Asia Pacific (Singapore), Europe (London), Asia Pacific (Seoul), and Europe (Frankfurt).

## March 2026
<a name="release-notes-2026-03"></a>

The Amazon Nova 2 Sonic refresh (March 2026 release) improves on the initial general availability launch from December 2, 2025, with the following enhancements:
+ Better speech generation quality with higher verbatim fidelity (fewer speech generation hallucinations) for customer service call automation use cases involving alphanumeric codes, currency values, addresses, email addresses, and phone numbers.
+ Amazon Polly-compatible voices for consistent voice experiences across Amazon Nova 2 Sonic and Polly text-to-speech (TTS).
+ Latency optimizations that reduce user-perceived latency at the 50th percentile (p50) by 150 ms.
+ Improved turn-taking performance on telephony speech (8 kHz).

Amazon Nova 2 Sonic continues to be generally available in the US East (N. Virginia), US West (Oregon), Asia Pacific (Tokyo), and Europe (Stockholm) Regions. In addition, it is available through Amazon Connect in the following Regions: Asia Pacific (Singapore), Europe (London), and Asia Pacific (Seoul).