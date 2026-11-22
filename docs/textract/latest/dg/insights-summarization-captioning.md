

# Document summarization and figure captioning

Amazon Textract Insights can generate a natural-language summary of a document and captions for the figures it contains. You enable these through the project's generative configuration, and they appear in the extraction results.

## Enabling generative output
<a name="insights-summarization-captioning-enabling"></a>

You configure generative output on the project through `GenerativeConfiguration`, which has two independent capabilities:
+ **Summarization** – Generates a summary of the document. If your document includes several document types, Amazon Textract Insights creates a separate summary for each logical sub-document.
+ **FigureCaption** – Generates captions for the figures detected in the document. By default, captioning is limited to five figures per page.

You enable the generative configuration when you create or update a project, alongside the extraction configuration. Each capability you turn on adds processing work, so enable only the ones you need. See [Working with projects](insights-working-with-projects.md).

```
aws textract create-project \
  --project-name "summaries-and-captions" \
  --extraction-configuration '{
    "BoundingBox": { "State": "ENABLED" },
    "Granularity": { "Types": ["DOCUMENT", "ELEMENT"] },
    "OutputFormat": {"TextFormat": {"Types": ["MARKDOWN"]}, "AdditionalFileFormat": {"State": "DISABLED"}}
  }' \
  --generative-configuration '{
    "Summarization": { "State": "ENABLED" },
    "FigureCaption": { "State": "ENABLED" }
  }' \
  --region us-east-1
```

To turn either capability off later, call `update-project` with the full `GenerativeConfiguration`, setting that capability's `State` to `DISABLED`. Omitting `--generative-configuration` on `create-project` leaves all generative output disabled.

## Document summaries
<a name="insights-summarization-captioning-summaries"></a>

When summarization is enabled, the `document` member of the extraction `result.json` includes two fields:
+ **summary** – A natural-language summary of the document's content, typically a few sentences.
+ **description** – A single sentence that names the document type and its subject, for example "This is an invoice about goods sold."

```json
"document": {
  "description": "This is an invoice about goods sold.",
  "summary": "This document is an invoice from one company to another, dated earlier this year. It lists the products sold and their unit prices, along with the invoice total.",
  "statistics": { "...": "..." }
}
```

If summarization is not enabled, both `summary` and `description` are absent.

Use the summary to give downstream consumers — a reviewer, a search index, or an LLM prompt — a quick orientation to the document without reading the full extracted text.

## Figure captions
<a name="insights-summarization-captioning-figures"></a>

When figure captioning is enabled, Amazon Textract Insights writes a descriptive caption for each figure it detects, such as a chart, graph, or image. Where the caption appears depends on the granularity you request:
+ **With ELEMENT granularity**, each figure is an element of `type` `FIGURE` with a `sub_type` (for example `CHART`), a `title` taken from the document, and a `summary` that holds the generated caption. The caption is also rendered into the element's `representation`, for example as Markdown image alt text. `statistics.figure_count` reports how many figures were found.
+ **Without ELEMENT granularity** (for example `PAGE` only), there is no `elements` section, but the caption is still embedded in the page `text` representation at the figure's position.

```json
{
  "type": "FIGURE",
  "sub_type": "CHART",
  "title": "FIG. 3. Comparison between the experimental group and control over 28 days.",
  "summary": "Title: Comparison of Bone Healing Between Experimental and Control Groups Over 28 Days\nThe figure presents a comparison between the experimental group and the control group...",
  "reading_order": 9,
  "locations": [ { "page_index": 0, "bounding_box": { "left": 0.06, "top": 0.76, "width": 0.43, "height": 0.19 } } ],
  "representation": { "markdown": "![Title: Comparison of Bone Healing Between Experimental and Control Groups Over 28 Days\n..." }
}
```

A document with no figures has a `figure_count` of 0 and produces no captions.

Enabling figure captioning limits the maximum number of pages supported per document. If you enable figure captioning on a longer document, the job fails with `ErrorType` `DocumentTooLargeException`. Summarization has no separate page limit. For these and other limits, see [Limits and quotas](insights-quotas.md).

## Relationship to granularity
<a name="insights-summarization-captioning-granularity"></a>

Generative output appears in the extraction result, so the sections it populates depend on the granularity you configure:
+ The document summary appears in the `document` member. Include `DOCUMENT` in `Granularity.Types` to receive the summary together with the whole-document text.
+ Captions appear as `FIGURE` elements when you request `ELEMENT` granularity, and inline in the page text otherwise.

See [Extraction results](insights-extraction-results.md) for the full structure and [Output formats for LLM and RAG workflows](insights-output-formats.md) for the text formats the summary and captions are rendered in.

## Next steps
<a name="insights-summarization-captioning-next-steps"></a>
+ Review the extraction results structure in [Extraction results](insights-extraction-results.md).
+ Extract defined fields instead of free text with [Custom extraction with blueprints](insights-custom-extraction.md).