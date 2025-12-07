# Multimodal understanding

Amazon Nova 2 Lite can understand multiple input modalities. This model is equipped with vision
capabilities that enable it to comprehend and analyze images, documents, videos and speech
to infer and answer questions based on the content provided.

This section outlines guidelines for working with images, documents and videos in Amazon Nova
including preprocessing strategies employed, code examples and relevant limitations to
consider.

## Supported-content-type-by-modality

The following information details the file formats supported by media file and the accepted input method.

| Media file type | File formats supported                                                                                             | Input method                                                                                                                                    | Size limitations | Number of objects |
| --------------- | ------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ----------------- |
| Image           | PNG, JPEG, GIF, WebP<br>\*_Note:_<br>• If you use an animated GIF or WebP file, only the first frame will be used. | Embedding data in the request<br>If you use the Converse API, encode data as bytes.<br>If you use the Invoke API, encode data as Base64 string. | 25 MB            | 5                 |
| Amazon S3 URI   | 2 GB total                                                                                                         | 1000                                                                                                                                            |
| Video           | MP4, MOV, MKV, WebM, FLV, MPEG, MPG, WMV, 3GP                                                                      | Embedding data in the request<br>If you use the Converse API, encode data as bytes.<br>If you use the Invoke API, encode data as Base64 string. | 25 MB            | 1                 |
| Amazon S3 URI   | 1 GB                                                                                                               | 1                                                                                                                                               |

###### Topics

- [Image understanding](#image-understanding "#image-understanding")
- [Video understanding](#video-understanding "#video-understanding")
- [Document understanding](#document-understanding "#document-understanding")
- [Examples: Using Nova's document understanding via API and S3](#document-understanding-api-s3 "#document-understanding-api-s3")

## Image understanding

Image understanding refers to Amazon Nova's ability to process an image and conduct a
variety of computer vision tasks such as:

- Performing object detection
- Answering questions about images through Visual Question Answering
  (VQA)
- Classifying and summarizing images
- Performing bounding box detection
- Optical Character Recognition (OCR)
- Object counting

Images can be included as a prompt passed to the API as byte arrays or via S3
URI.

### Key technical information

The following is key technical information to note when you work with this
capability.

#### Image sizing and rescaling

Amazon Nova automatically rescales images to optimize quality and
performance:

- Determines the closest aspect ratio (such as 1:1, 1:2, 2:3 and so
  on)
- Rescales so that one side ≥ 896 px or matches the shorter side of the
  original image—whichever is larger
- Maintains the aspect ratio
- Supports up to 8,000 × 8,000 px resolution

**Bounding box coordinates:**

- Useful for tasks such as identifying elements in screenshots or image
  grounding
- Coordinates can be rescaled to match the image's original dimensions
  in post-processing
- Returns bounding boxes on a [0, 1000] scale.

### Image-token estimation

Amazon Nova converts each image into tokens for processing. The number of tokens
depends on the resolution and aspect ratio of the image.

The following are examples of approximate token counts based on image
resolution:

| Image resolution | Estimated tokens |
| ---------------- | ---------------- |
| 900 x 450        | 515              |
| 900 x 900        | ~1,035           |
| 1400 x 900       | ~1,600           |
| 1800 x 900       | ~2,060           |
| 1300 x 1300      | ~2,155           |

### Image understanding examples

For an example of how to embed image data directly in the request, refer to the Multimodal input using embedded asset - Converse API (non-streaming) example in the [Code library](code-library.md "code-library.md").

To upload large image files or multiple image files, where the overall payload is greater than 25 MB, use Amazon S3. For a full example of how use Amazon S3 URI references for image input, refer to refer to the Multimodal input using S3 URI - Converse API (non-streaming) example in the [Code library](code-library.md "code-library.md").

###### Note

When using S3, ensure the Amazon Bedrock service has permission to access the bucket and
object.

### Limitations

The following list outlines current limitations of image understanding
models:

- **Multilingual image understanding**: The
  models have limited understanding of multilingual images and video frames
  and can struggle or hallucinate on simple tasks.
- **People identification**: Amazon Nova 2 models do
  not support the capability to identify or name individuals in images,
  documents or videos.
- **Spatial reasoning**: Amazon Nova 2 models have limited spatial
  reasoning capabilities. They may struggle with tasks that require precise localization
  or layout analysis.
- **Small text in images and videos**: If the text in the image or
  video is too small, consider increasing relative size of the text in the image by cropping to relevant
  section while preserving necessary context.

## Video understanding

Video understanding refers to Amazon Nova's ability to process video inputs and perform a
range of video comprehension tasks such as:

- Analyzing key frames and summarizing video content
- Answering questions about video segments (Video Question Answering, or Video
  QA)
- Detecting and tracking objects across frames
- Identifying actions, scenes and events
- Performing temporal segmentation to locate specific moments
- Generating descriptive captions or summaries of video sequences

### Key technical information

The following is key technical information to note when you work with this
capability.

#### Video size information

Amazon Nova video understanding capabilities support multi-aspect ratio. All videos
are resized with distortion (up or down, based on the original aspect ratio) to
672 × 672 square dimensions before they are input to the model.

The model utilizes a dynamic sampling strategy based on video length. For
videos 16 minutes or less in length, Amazon Nova 2 Lite samples 1 frame per second
(FPS). For videos longer than 16 minutes, the sampling rate decreases to maintain a consistent 960 frames sampled, with the frame sampling rate varying accordingly. This approach is designed to provide more accurate scene-level video understanding for shorter videos compared to longer video content.

We recommend that you keep the video length less than 1 hour for low motion
and less than 16 minutes for anything with high motion.

There should be no difference when analyzing a 4k version of a video and a
Full HD version. Similarly, because the sampling rate is 1 FPS, a 60 FPS video should perform as well as a 30 FPS video. Using a resolution and FPS that is higher than what is required is not beneficial because of the 1 GB limit in video size. Doing so will limit the video length that fits in that size limit, so, you may want to pre-process videos longer than 1 GB.

#### Video tokens

The length of the video is the main factor impacting the number of tokens
generated. To calculate the approximate cost, multiply the estimated number of video tokens by the per-token price for the specific model being utilized.

The following table provides some approximations of frame sampling and token
utilization per video length for Amazon Nova 2 Lite:

| Video length | Frames to sample | Sample rate fps | Approximate tokens |
| ------------ | ---------------- | --------------- | ------------------ |
| 10 seconds   | 10               | 1               | 2,880              |
| 30 seconds   | 30               | 1               | 8,640              |
| 16 minutes   | 960              | 1               | 276,480            |
| 20 minutes   | 1200             | 1               | 345,600            |
| 30 minutes   | 1800             | 1               | 518,400            |
| 45 minutes   | 2700             | 1               | 777,600            |

#### Video understanding

examples

For an example of how to embed video data directly in the request, refer to the Multimodal input using embedded asset - Converse API (non-streaming) example in the [Code library](code-library.md "code-library.md").

For an example of how to use S3 URI references in video input, refer to the Multimodal input using S3 URI - Converse API (non-streaming) example in the [Code library](code-library.md "code-library.md").

### Key limitations

The following are key model limitations, where model accuracy and performance
might not be guaranteed:

- **No audio support**: The Amazon Nova models are
  currently trained to process and understand video content solely based on
  the visual frames. Audio tracks in videos are not processed or
  analyzed.
- **Multilingual image understanding**: The
  Amazon Nova models have limited understanding of multilingual images and video
  frames. They might struggle or hallucinate on simple tasks.
- **People identification**: The Amazon Nova models
  do not support the capability to identify or name individuals in images,
  documents, or videos. The models will not provide names or identities of
  people in visual content.
- **Small text in videos**: If the text in the
  image or video is too small, consider increasing relative size of the text
  in the video.
- **Spatial reasoning**: Amazon Nova 2 models have
  limited spatial reasoning capabilities. They may struggle with tasks that
  require precise understanding of object positions, distances, or spatial
  relationships in videos.
- **Inappropriate content**: The Nova models
  will not process inappropriate or explicit images that violate the
  Acceptable Use Policy.
- **Healthcare applications**: Due to the
  sensitive nature of these artifacts, even though Nova models could give
  general analysis on some healthcare images or videos, we do not recommend
  their use to interpret sensitive medical images like complex diagnostic
  scans. The response of Nova models should never be considered a substitute
  for professional medical advice.

## Document understanding

Amazon Nova's document understanding capability allows you to include entire documents
(PDFs, Word files, spreadsheets and so on) as part of your prompt. This enables the
model to analyze, summarize, extract information from, or answer questions about
document content.

Amazon Nova 2 Lite can interpret both the text and visual elements (like charts or tables) within these documents. This enables use cases such as question-answering, summarization, and analysis of lengthy reports or scanned documents.

Key document understanding features include a very large context window (1M tokens)
for long documents and the ability to handle multiple documents in one query.

### Supported document modalities and formats

Amazon Nova distinguishes between two types of document inputs:

- **Text-based documents**, like TXT, CSV,
  HTML, Markdown, or DOC files, are processed primarily for their textual
  content. Amazon Nova understands and extracts information from the text in these documents.
- **Media-based documents**, like PDF or DOCX
  files, may contain complex layouts, images, charts, or embedded graphics.
  For media-based documents, Amazon Nova employs vision-based understanding to interpret visual content—such as charts, tables, diagrams, or screenshots—alongside the document's text.

Supported file formats include common document types such as:

- Plain text and structured text files: CSV, TXT
- Spreadsheets: XLS, XLSX, HTML, Markdown
- Standard image formats (for images within documents): PNG, JPG, GIF, WebP
- Document formats: DOC, DOCX, PDF
- PDFs that contain image encodings, such as CYMK or SVG are not supported.

### Document size limits and usage guidelines

| Constraint                  | Limit                                                                                                                                                                                                                                                            |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Maximum number of documents | Up to 5 documents per request (applies to both direct upload and Amazon S3)                                                                                                                                                                                      |
| Text-based document size    | Each text document must be equal to or less than 4.5 MB                                                                                                                                                                                                          |
| Media-based document size   | For PDF and DOCX files, there is no individual file size limit. When using direct upload, the combined size of all media documents must be less or equal to 25 MB. When using Amazon S3, the combined size of all media documents must be less or equal to 2 GB. |
| Unsupported PDF content     | PDFs that contain CMYK color profiles or SVG images are not supported.                                                                                                                                                                                           |

### Pricing

Amazon Nova uses token-based pricing: you pay for input tokens (everything you send,
including attached documents) and output tokens (the model's response).

**Estimating tokens for PDFs:** For planning, assume
a standard 8.5x11 inch PDF page ≈ 2,560 input tokens (this estimate covers both text
and visual elements on a typical page).

## Examples: Using Nova's document understanding via API and S3

For an example of how to use it via API, refer to the Multimodal input using embedded asset - Converse API (non-streaming) example in the [Code library](code-library.md "code-library.md").

For an example of how to use it via S3, refer to the Multimodal input using S3 URI - Converse API (non-streaming) example in the [Code library](code-library.md "code-library.md").
