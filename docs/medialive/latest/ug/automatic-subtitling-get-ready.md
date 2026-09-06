

# Get ready
<a name="automatic-subtitling-get-ready"></a>

## Pricing
<a name="automatic-subtitling-pricing"></a>

There is a charge for running a channel that has the Smart Subtitles feature enabled. The charge is applied to each pipeline, which means that it applies once in single-pipeline channels and twice in standard channels.

To stop this charge, you must disable the feature. For information about the current rates for using this feature, see [Elemental Inference pricing](https://aws.amazon.com/elemental-inference/pricing/).

## Supported languages
<a name="automatic-subtitling-supported-languages"></a>

Smart Subtitles supports the following languages:
+ `eng` – English
+ `spa` – Spanish
+ `fra` – French
+ `deu` – German
+ `ita` – Italian
+ `por` – Portuguese

## Source requirements
<a name="automatic-subtitling-source-requirements"></a>
+ Input type: All supported input types.
+ Audio codec: AAC
+ Smart Subtitles supports a single audio track only.
+ The source must contain audio in one of the supported languages.

## Output requirements
<a name="automatic-subtitling-output-requirements"></a>

Smart Subtitles generates subtitles in the following formats:
+ **TTML** – Supported as a sidecar in MediaPackage V2, CMAF Ingest, and Microsoft Smooth output groups.
+ **WebVTT** – Supported as a sidecar in HLS and MediaPackage output groups.

**Important**  
When outputting subtitles, you must create a separate captions-only output within your output group specifically for the subtitles. The subtitle output should contain only the captions encode, with no video or audio encodes. For detailed instructions on creating a sidecar captions output, see [Create sidecar or SMPTE-TT captions encodes](output-sidecar-and-smptett-mss.md).