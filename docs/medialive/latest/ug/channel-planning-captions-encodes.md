# Identify the captions encodes

You must decide on the number of captions encodes. Follow this procedure for each output
group.

1. Determine the maximum number of captions encodes that are allowed in the output group.
   The following rules apply for each type of output group.

| Type of output group | Rule for captions encodes                                                                                                                                       |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Archive              | Zero or more captions encodes. The captions are either embedded or<br>object-style captions.                                                                    |
| CMAF Ingest          | Zero or more captions encodes. Typically, there are caption languages to<br>match the audio languages. The captions are<br>embedded<br>or sidecar captions.     |
| Frame Capture        | Zero captions encodes.                                                                                                                                          |
| HLS or MediaPackage  | Zero or more captions encodes. Typically, there are caption languages to<br>match the audio languages. The captions are either embedded or sidecar<br>captions. |
| Microsoft Smooth     | Zero or more captions encodes. Typically, there are caption languages to<br>match the audio languages. The captions are always sidecar captions.                |
| RTMP                 | Zero or one caption encodes. The captions are either embedded or object-style<br>captions.                                                                      |
| SRT                  | Zero or more captions encodes. The captions are either embedded or<br>object-style captions.                                                                    |
| UDP                  | One or more captions encodes. The captions are either embedded or<br>object-style captions.                                                                     |

2. Identify the category that each caption format belongs to. See the list in [Captions categories](categories-captions.md "categories-captions.md"). For example, WebVTT captions are sidecar
   captions.
3. Use this category to identify the number of captions encodes you need in the output
   group.
   - For embedded captions, you always create one captions encode.
   - For object-style captions and sidecar captions, you create one captions encode for
     each format and language that you want to include.
