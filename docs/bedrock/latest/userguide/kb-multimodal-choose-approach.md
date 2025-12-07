# Choosing your multimodal processing

approach

Amazon Bedrock Knowledge Bases offers two approaches for processing multimodal content: Nova Multimodal
Embeddings for visual similarity searches, and Bedrock Data Automation (BDA) for
text-based processing of multimedia content. You can also use foundation models as your
parser if your input modality is image but not for audio or video.

This section describes using Nova Multimodal Embeddings and BDA as your processing
approach for multimodal content. Each approach is optimized for different use cases and
query patterns.

###### Topics

- [Multimodal processing
  approach](#kb-multimodal-processing-approach "#kb-multimodal-processing-approach")
- [Regional availability](#kb-multimodal-processing-regions "#kb-multimodal-processing-regions")
- [Selection criteria by content
  type](#kb-multimodal-selection-guidance "#kb-multimodal-selection-guidance")
- [Supported file types and data
  sources](#kb-multimodal-supported-files "#kb-multimodal-supported-files")
- [Capabilities and
  limitations](#kb-multimodal-approach-details "#kb-multimodal-approach-details")

## Multimodal processing

approach

The following table shows a comparison between Nova Multimodal Embeddings and BDA
for processing multimodal content.

| Processing approach comparison | Characteristic                                                 | Nova Multimodal Embeddings                                                                                                                                                             | Bedrock Data Automation (BDA) |
| ------------------------------ | -------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| Processing method              | Generates embeddings without intermediate text conversion      | Converts multimedia to text, then creates embeddings                                                                                                                                   |
| Query types supported          | Text queries or image queries                                  | Text queries only                                                                                                                                                                      |
| Primary use cases              | Visual similarity search, product matching, image<br>discovery | Speech transcription, text-based search, content analysis                                                                                                                              |
| RAG functionality              | Limited to text content only                                   | Full `RetrieveAndGenerate` support                                                                                                                                                     |
| Storage requirements           | Multimodal storage destination required                        | Multimodal storage destination optional though if not specified,<br>only text data will be processed by BDA. For non-text input, you<br>must specify a multimodal storage destination. |

## Regional availability

| Regional availability      | Nova Multimodal Embeddings                                                                                                                                                                         | Bedrock Data Automation (BDA) |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| US East (N. Virginia) only | • US West (Oregon)<br>• US East (N. Virginia)<br>• Europe (Frankfurt)<br>• Europe (London)<br>• Europe (Ireland)<br>• Asia Pacific (Mumbai)<br>• Asia Pacific (Sydney)<br>• AWS GovCloud (US-West) |

## Selection criteria by content

type

Use this decision matrix to choose the appropriate processing approach based on
your content and use case requirements:

###### Note

If you use the BDA parser with the Amazon Nova Multimodal Embeddings model,
the embeddings model will act like a text embeddings model. When working with
multimodal content, use one of the processing approaches for best results
depending on your use case.

| Processing approach recommendations by content type | Content Type                                                                   | Nova Multimodal Embeddings                                                   | Bedrock Data Automation (BDA) |
| --------------------------------------------------- | ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------- | ----------------------------- |
| Product catalogs and images                         | Recommended<br>• Enables visual similarity matching and image-based<br>queries | Limited<br>• Only extracts text through OCR                                  |
| Meeting recordings and calls                        | Cannot process speech content<br>meaningfully                                  | Recommended<br>• Provides full speech transcription and searchable<br>text   |
| Training and educational videos                     | Partial<br>• Handles visual content but misses speech                          | Recommended<br>• Captures both speech transcripts and visual<br>descriptions |
| Customer support recordings                         | Not recommended<br>• Speech content cannot be processed<br>effectively         | Recommended<br>• Creates complete searchable conversation<br>transcripts     |
| Technical diagrams and charts                       | Recommended<br>• Excellent for visual similarity and pattern<br>matching       | Limited<br>• Extracts text labels but misses visual<br>relationships         |

## Supported file types and data

sources

The supported file types depend on your chosen processing approach:

| Supported file types by processing approach | File Type                                              | Nova Multimodal Embeddings              | Bedrock Data Automation (BDA) |
| ------------------------------------------- | ------------------------------------------------------ | --------------------------------------- | ----------------------------- |
| Images                                      | .png, .jpg, .jpeg, .gif, .webp                         | .png, .jpg, .jpeg                       |
| Audio                                       | .mp3, .ogg, .wav                                       | .amr, .flac, .m4a, .mp3, .ogg, .wav     |
| Video                                       | .mp4, .mov, .mkv, .webm, .flv, .mpeg, .mpg, .wmv, .3gp | .mp4, .mov                              |
| Documents                                   | Processed as text                                      | .pdf (plus text extraction from images) |

###### **Supported data sources**

Multimodal content is supported with the following data sources:

- **Amazon S3:** Full support for all multimodal
  file types
- **Custom data sources:** Support for inline
  content up to 10MB base64 encoded

###### Important

Multimodal retrieval is currently available only for Amazon S3 data sources. Other
data sources (Confluence, SharePoint, Salesforce, Web Crawler) do not process
multimodal files during ingestion. These files are skipped and will not be
available for multimodal queries.

## Capabilities and

limitations

**Nova Multimodal Embeddings**

**Key capabilities:**

- Native multimodal processing preserves original content format
  for optimal visual similarity matching
- Image-based queries allow users to upload images and find
  visually similar content
- Excellent performance for product catalogs, visual search, and
  content discovery applications

**Limitations:**

- Cannot effectively process speech or audio content - spoken
  information is not searchable
- `RetrieveAndGenerate` and rerank functionality
  limited to text content only
- Requires configuration of a dedicated multimodal storage
  destination

**Bedrock Data Automation (BDA)**

**Key capabilities:**

- Comprehensive speech transcription using Automatic Speech
  Recognition (ASR) technology
- Visual content analysis generates descriptive text for images
  and video scenes
- Full `RetrieveAndGenerate` support enables complete
  RAG functionality across all content
- Text-based search works consistently across all multimedia
  content types

**Limitations:**

- No support for image-based queries when used without Nova Multimodal Embeddings - all searches must use
  text input
- Cannot perform visual similarity matching or image-to-image
  searches
- Longer ingestion processing time due to content conversion
  requirements
- Supports fewer multimedia file formats compared to Nova
  Multimodal Embeddings

###### Speech content processing

Nova Multimodal Embeddings cannot effectively process speech content in audio
or video files. If your multimedia content contains important spoken information
that users need to search, choose the BDA approach to ensure full transcription
and searchability.
