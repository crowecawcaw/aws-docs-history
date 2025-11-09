# HLS input requirements

When you specify an HLS package as an input for your MediaConvert job, you need to specify the correct input file URL and ensure that the HLS input package conforms to the requirements listed on this page.

You can specify either a
multivariant or variant playlist. If the manifest is a parent that lists multiple child
manifests, MediaConvert uses the variant playlist with the highest bandwidth as the input
source.

## HLS input requirements

Your HLS input must conform to the following
requirements:

|                                         |                                                                                                                                                                                                                                                                   |
| --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Input requirement**                   | **Details**                                                                                                                                                                                                                                                       |
| Video container                         | MediaConvert supports MPEG-2 Transport Stream (MPEG-TS) files<br>for input HLS media segments.                                                                                                                                                                    |
| HLS manifest `EXT-X-VERSION`            | MediaConvert supports `EXT-X-VERSION` values of<br>\*_4 or lower_<br>• within input HLS<br>manifests.                                                                                                                                                             |
| HLS manifest `EXT-X-ENDLIST`            | Include `EXT-X-ENDLIST` or<br>`EXT-X-PLAYLIST-TYPE: VOD` in your input<br>manifest.<br>Manifest files must not change after you submit your<br>job.                                                                                                               |
| HLS manifest `EXT-X-PLAYLIST-TYPE: VOD` | Include `EXT-X-ENDLIST` or<br>`EXT-X-PLAYLIST-TYPE: VOD` in your input<br>manifest.<br>Manifest files must not change after you submit your<br>job.                                                                                                               |
| HLS manifest `EXT-X-BYTERANGE`          | If present, the start of the first subrange must be 0 and the<br>following subrange segments must continue the former one.                                                                                                                                        |
| HLS manifest `EXT-X-KEY`                | If present, `EXT-X-KEY: METHOD` must be set to<br>`NONE`.<br>MediaConvert does not support HLS encrypted inputs.                                                                                                                                                  |
| HLS manifest ignored tags               | MediaConvert ignores the following tags:<br>• `EXT-X-PROGRAM-DATE-TIME`<br>• `EXT-X-DATERANGE`<br>• `EXT-X-I-FRAMES-ONLY`<br>• `EXT-X-I-FRAME-STREAM-INF`<br>• `EXT-X-SESSION-DATA`<br>• `EXT-X-SESSION-KEY`<br>• `EXT-X-INDEPENDENT-SEGMENTS`<br>• `EXT-X-START` |
| Discontinuities                         | If present, any discontinuities must start at the beginning of<br>a segment.<br>MediaConvertdoes not support input discontinuites in the<br>subrange of a segment.                                                                                                |
| Accelerated transcoding requirements    | `EXTINF` duration must be specified using a decimal<br>floating-point, with enough accuracy to avoid perceptible errors<br>when segment durations are accumulated.                                                                                                |

## MediaConvert features compatible with HLS inputs

With HLS inputs, you can use the following input features:

- Input clipping
- Input stitching
- Image insertion
- Embedded input captions selectors

## HLS input feature

restrictions

When your input is an HLS package, your job is restricted in these
ways:

- Your input package must conform to the requirements listed in [HLS input requirements](#hls-input-package-requirements "#hls-input-package-requirements").
- Your input segments can't be encrypted with DRM. For example, your inputs
  can't be encrypted with Apple FairPlay DRM.
- You can use only embedded input captions.
