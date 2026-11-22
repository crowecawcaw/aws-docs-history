

# Extraction results

Extraction produces a structured JSON representation of a document: its text and layout, reading order, per-page detail, and statistics. This page is a field reference for the extraction `result.json`, keyed to a trimmed example.

Extraction results are written to `extraction/<n>/result.json`, where `<n>` is the document index. The sections that appear depend on the granularity you configured (see [Granularity](#insights-extraction-results-granularity)). For the surrounding file layout, see [Output location and file structure](insights-output-location.md).

## Top-level structure
<a name="insights-extraction-results-top-level"></a>

An extraction `result.json` has these top-level members:


| **Member** | **Description** | 
| --- | --- | 
| `metadata` | Information about the source document and this extraction segment. | 
| `document` | Document-level representations, optional summary and description, and statistics. | 
| `pages` | Per-page detail (appears with `PAGE` granularity). | 
| `elements` | Layout elements such as titles, paragraphs, and tables (appears with `ELEMENT` granularity). | 
| `text_lines` | Line-level text (appears with `LINE` granularity). | 
| `text_words` | Word-level text (appears with `WORD` granularity). | 

The following example is trimmed and uses placeholder content.

```json
{
  "metadata": {
    "asset_id": "0",
    "logical_subdocument_id": "0",
    "semantic_modality": "DOCUMENT",
    "s3_bucket": "amzn-s3-demo-bucket",
    "s3_key": "invoice.pdf",
    "number_of_pages": 5,
    "start_page_index": 0,
    "end_page_index": 4,
    "file_type": "PDF"
  },
  "document": {
    "representation": {
      "text": "Example Company\n\nInvoice Number #000009 ...",
      "markdown": "# Example Company\n\n| | |\n|--|--|\n| Invoice Number | #000009 | ...",
      "html": "<html><body><h1>Example Company</h1> ..."
    },
    "description": "This is an invoice about goods sold",
    "summary": "This document is an invoice from one company to another, dated ... . The invoice lists the products sold and their prices. ...",
    "statistics": {
      "element_count": 42,
      "table_count": 13,
      "figure_count": 0,
      "word_count": 1637,
      "line_count": 1085,
      "hyperlink_count": 9
    }
  },
  "pages": [ "... (one entry per page)" ],
  "elements": [ "... (one entry per layout element)" ],
  "text_lines": [ "... (one entry per line)" ],
  "text_words": [ "... (one entry per word)" ]
}
```

## metadata
<a name="insights-extraction-results-metadata"></a>


| **Field** | **Description** | 
| --- | --- | 
| `asset_id` | Identifier of the input file (0 for a single input). | 
| `logical_subdocument_id` | Identifier of the logical document within the input, after any splitting. | 
| `semantic_modality` | The modality of the content, for example `DOCUMENT`. | 
| `s3_bucket`, `s3_key` | Location of the source document in Amazon S3. | 
| `number_of_pages` | Number of pages in this segment. | 
| `start_page_index`, `end_page_index` | Zero-based page range of this segment within the input file. | 
| `file_type` | Input file type, for example `PDF`. | 

## document
<a name="insights-extraction-results-document"></a>

The `document` member holds document-level output:


| **Field** | **Description** | 
| --- | --- | 
| `representation` | The whole document rendered as `text`, `markdown`, and `html`, depending on the output formats you enabled. See [Output formats for LLM and RAG workflows](insights-output-formats.md). | 
| `description` | A single sentence naming the document type and its subject, for example "This is an invoice about goods sold." Present only when summarization is enabled. See [Document summarization and figure captioning](insights-summarization-captioning.md). | 
| `summary` | A natural-language summary, present only when summarization is enabled. See [Document summarization and figure captioning](insights-summarization-captioning.md). | 
| `statistics` | Counts for the document — `element_count`, `table_count`, `figure_count`, `word_count`, `line_count`, and `hyperlink_count`. | 

With `PAGE` granularity but no `DOCUMENT` granularity, the `document` member still exists but contains only `statistics`.

## pages
<a name="insights-extraction-results-pages"></a>

Each entry in `pages` describes one page:


| **Field** | **Description** | 
| --- | --- | 
| `id` | Unique page identifier. | 
| `page_index` | Zero-based page number. | 
| `representation` | The page rendered as `text`, `markdown`, and `html`. | 
| `statistics` | Per-page counts, same shape as the document statistics. | 
| `asset_metadata` | Page image assets: `rectified_image` (the S3 URI of the deskewed page image), `rectified_image_width_pixels`, `rectified_image_height_pixels`, and `corners` (the page corner coordinates). | 

## elements
<a name="insights-extraction-results-elements"></a>

Each entry in `elements` is a layout element in reading order:


| **Field** | **Description** | 
| --- | --- | 
| `type` | `TEXT`, `TABLE`, or `FIGURE`. | 
| `sub_type` | For `TEXT`: the layout role, such as `TITLE`, `PARAGRAPH`, `HEADER`, `FOOTER`, or `PAGE_NUMBER`. | 
| `id` | Unique element identifier. | 
| `reading_order` | The element's position in the document reading order. | 
| `page_indices` | The pages the element spans. | 
| `representation` | The element rendered as `text`, `markdown`, and `html`. | 
| `locations` | A list of `{page_index, bounding_box}` entries locating the element on the page. | 

A `TABLE` element adds a `csv` representation, a `csv_s3_uri` pointing at the exported CSV, and `title`, `headers`, and `footers`.

```json
{
  "type": "TEXT",
  "sub_type": "TITLE",
  "id": "fc47ab5a690644bd92aa5ad594aaada1",
  "reading_order": 0,
  "page_indices": [0],
  "representation": {
    "text": "Example Company",
    "markdown": "# Example Company",
    "html": "<h1>Example Company</h1>"
  },
  "locations": [
    {
      "page_index": 0,
      "bounding_box": { "left": 0.0519, "top": 0.1980, "width": 0.2051, "height": 0.0405 }
    }
  ]
}
```

## text\_lines and text\_words
<a name="insights-extraction-results-lines-words"></a>

`text_lines` and `text_words` give line- and word-level text with recognition confidence:


| **Field** | **Description** | 
| --- | --- | 
| `id` | Unique line or word identifier. | 
| `text` | The recognized text. | 
| `confidence` | Recognition confidence, from 0 to 1. Other Amazon Textract APIs, such as `AnalyzeDocument`, report confidence from 0 to 100, so rescale before you compare values across APIs. | 
| `reading_order` | Position in the reading order. | 
| `page_index` | The page the line or word is on. | 
| `locations` | A list of `{page_index, bounding_box}` entries. | 

A word additionally has a `line_id` linking it to its line.

## Bounding boxes
<a name="insights-extraction-results-bounding-boxes"></a>

Every `bounding_box` is expressed as ratios of the page width and height, from 0 to 1:


| **Field** | **Description** | 
| --- | --- | 
| `left` | Distance from the left edge, as a fraction of page width. | 
| `top` | Distance from the top edge, as a fraction of page height. | 
| `width` | Width, as a fraction of page width. | 
| `height` | Height, as a fraction of page height. | 

To convert to pixels, multiply by the page's pixel dimensions (for example `rectified_image_width_pixels` and `rectified_image_height_pixels` from `asset_metadata`).

## Granularity
<a name="insights-extraction-results-granularity"></a>

`Granularity.Types` in the project's extraction configuration controls which sections appear in the result:


| **Granularity type** | **Section produced** | 
| --- | --- | 
| `DOCUMENT` | `document` | 
| `PAGE` | `pages` | 
| `ELEMENT` | `elements` | 
| `LINE` | `text_lines` | 
| `WORD` | `text_words` | 

## Next steps
<a name="insights-extraction-results-next-steps"></a>
+ Configure which text formats appear in `representation` in [Output formats for LLM and RAG workflows](insights-output-formats.md).
+ Add a summary and figure captions in [Document summarization and figure captioning](insights-summarization-captioning.md).