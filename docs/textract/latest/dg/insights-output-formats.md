

# Output formats for LLM and RAG workflows

Extraction can render a document as plain text, Markdown, HTML, and CSV. These formats make the output ready to feed directly to a large language model (LLM) or a retrieval-augmented generation (RAG) pipeline, without you having to reconstruct the document from JSON blocks.

## Text formats in the result
<a name="insights-output-formats-text-formats"></a>

When you enable text formats, the extraction `result.json` includes a `representation` object at the document, page, and element levels. Each representation carries the text in the formats you requested:


| **Format** | **Member** | **Typical use** | 
| --- | --- | --- | 
| Plain text | `text` | Raw text for search, embeddings, or simple prompts. | 
| Markdown | `markdown` | Structured prompts and RAG chunks that preserve headings, lists, and tables. | 
| HTML | `html` | Rendering, or feeding structured markup to a model. | 

For example, a document title appears across the formats as:

```json
"representation": {
  "text": "Example Company",
  "markdown": "# Example Company",
  "html": "<h1>Example Company</h1>"
}
```

Markdown and HTML preserve document structure — headings, paragraphs, and tables — which helps a model keep the meaning of the layout. Tables are rendered as Markdown pipe tables and HTML <table> markup in the representations.

## CSV output for tables
<a name="insights-output-formats-csv"></a>

You can also export table elements as CSV. When you request CSV output, each table element in `elements` carries a `csv` representation and a `csv_s3_uri`, and Amazon Textract Insights writes one CSV file for each table under the document's `assets/` folder:

```
<prefix>/<job-id>/0/extraction/<n>/assets/<uuid>.csv
```

Use the CSV files when you want to load tabular data straight into a spreadsheet, a dataframe, or a database rather than parsing it out of text.

## Enabling output formats
<a name="insights-output-formats-enabling"></a>

You configure output formats on the project's extraction configuration through `OutputFormat`, alongside `BoundingBox` and `Granularity`. `OutputFormat` is required whenever you send `ExtractionConfiguration`. Enabling an additional output format produces more output and increases processing time, so request only the formats you use.

`OutputFormat.TextFormat.Types` selects the representations (`PLAIN_TEXT`, `MARKDOWN`, `HTML`, `CSV`). `OutputFormat.AdditionalFileFormat.State` controls whether standalone rendered files are also written:

```
aws textract create-project \
  --project-name "rag-ingestion" \
  --extraction-configuration '{
    "BoundingBox": { "State": "ENABLED" },
    "Granularity": { "Types": ["DOCUMENT", "PAGE", "ELEMENT"] },
    "OutputFormat": {
      "AdditionalFileFormat": { "State": "ENABLED" },
      "TextFormat": { "Types": ["PLAIN_TEXT", "MARKDOWN", "HTML", "CSV"] }
    }
  }' \
  --region us-east-1
```

CSV applies to table elements only. It adds a `csv` member to each table's representation and writes the table CSV files described earlier.

When the additional file formats are enabled, Amazon Textract Insights also writes standalone rendered files next to the JSON result:

```
<prefix>/<job-id>/0/extraction/<n>/result.md
<prefix>/<job-id>/0/extraction/<n>/result.html
<prefix>/<job-id>/0/extraction/<n>/result.txt
```

These let you download a ready-to-use Markdown, HTML, or plain-text rendering of the document directly.

## Choosing formats for RAG
<a name="insights-output-formats-choosing-rag"></a>

For a RAG pipeline, a common choice is to use the Markdown representation at the granularity that matches your chunking strategy — for example, document-level Markdown for whole-document indexing, or element-level Markdown to chunk by layout element while preserving each element's structure. Pair this with the recognition confidence on `text_lines` and `text_words` if you want to filter low-confidence text before indexing.

## Next steps
<a name="insights-output-formats-next-steps"></a>
+ See the full extraction result structure in [Extraction results](insights-extraction-results.md).
+ Add generated summaries and figure captions in [Document summarization and figure captioning](insights-summarization-captioning.md).