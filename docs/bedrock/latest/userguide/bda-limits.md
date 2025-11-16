# Prerequisites for using Bedrock Data Automation

Files for BDA need to meet certain requirements in order to be processed. The following tables show what those
requirements are for different file types.

| Document file requirements                                     | Requirement Description                                                                                                                                                                                                                                                                                           | Requirement Details |
| -------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- |
| (Console) Maximum number of pages per document file            | 20                                                                                                                                                                                                                                                                                                                |
| Maximum Number of pages per document while splitter is enabled | 3000                                                                                                                                                                                                                                                                                                              |
| (Console) Maximum file size (MB)                               | 200                                                                                                                                                                                                                                                                                                               |
| Maximum file size (MB)                                         | 500                                                                                                                                                                                                                                                                                                               |
| Supported File Formats                                         | PDF, TIFF, JPEG, PNG, DOCX                                                                                                                                                                                                                                                                                        |
| PDF Specific Limits                                            | The maximum height and width<br>is 40 inches and 9000 points. PDFs cannot be password protected.<br>PDFs can contain JPEG 2000 formatted images.                                                                                                                                                                  |
| Document Rotation and Image Size                               | BDA supports all in-plane document rotations, for example<br>45-degree in-plane rotation.<br>BDA supports images with a resolution less than or equal to<br>10000 pixels on all sides.                                                                                                                            |
| Text Alignment                                                 | Text can be text aligned horizontally within the document.<br>Horizontally arrayed text can be read regardless of the degree of<br>rotation of a document. BDA does not support vertical text<br>(text written vertically, as is common in languages like Japanese<br>and Chinese) alignment within the document. |
| Character Size                                                 | The minimum height for text to be detected is 15 pixels.<br>At 150 DPI, this would be the same as 8 point font.                                                                                                                                                                                                   |
| Character Type                                                 | BDA supports both handwritten and printed character recognition.                                                                                                                                                                                                                                                  |

###### Note

To process DOCX files, they are converted into PDFs. This means page number mapping
will not work for DOCX files. Images of the converted PDFs will be uploaded to your
output bucket if the JSON+ option and page granularity are selected.

| Image file requirements | Requirement Description | Requirement Details |
| ----------------------- | ----------------------- | ------------------- |
| Maximum File Size (MB)  | 5                       |
| Maximum Resolution      | 8k                      |
| Supported File Formats  | JPEG, PNG               |

| Video file requirements                              | Requirement Description                                                                                            | Requirement Details |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | ------------------- |
| Maximum File Size (MB)                               | 10240                                                                                                              |
| Maximum Video Length (Minutes)                       | 240                                                                                                                |
| Supported File Formats                               | MP4, MOV, AVI, MKV, or WEBM container formats with H.264, H.265/HEVC, VP8, VP9, AV1, or MPEG-4 Visual video codecs |
| Maximum Video Blueprints per Project                 | 1                                                                                                                  |
| Maximum Video Blueprints per Start Inference request | 1                                                                                                                  |
| Minimum resolution                                   | 224                                                                                                                |
| Maximum resolution                                   | 7680                                                                                                               |
| Minimum framerate (Frames per second)                | 1                                                                                                                  |
| Maximum framerate (Frames per second)                | 60                                                                                                                 |

| Audio file requirements                              | Requirement Description                                                                                                                                          | Requirement Details |
| ---------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- |
| Supported Input Languages                            | English, Germany, Spanish, French, Italian, Portuguese, Japanese, Korean, Chinese, Taiwanese and Cantonese.<br>_\*All locales supported of the above languages._ |
| Supported Output Languages                           | English, or the dominant language of the audio.                                                                                                                  |
| Minimum Audio Sample Rate (Hz)                       | 8000                                                                                                                                                             |
| Maximum Audio Sample Rate (Hz)                       | 48000                                                                                                                                                            |
| Maximum File Size (MB)                               | 2048                                                                                                                                                             |
| Maximum Audio Length (Minutes)                       | 240                                                                                                                                                              |
| Minimum Audio Length (Milliseconds)                  | 500                                                                                                                                                              |
| Supported File Formats                               | AMR, FLAC, M4A, MP3, Ogg, WAV                                                                                                                                    |
| Maximum Audio Blueprints per Project                 | 1                                                                                                                                                                |
| Maximum Audio Blueprints per Start Inference request | 1                                                                                                                                                                |
| Maximum Audio Channels for Audio files               | 2                                                                                                                                                                |
