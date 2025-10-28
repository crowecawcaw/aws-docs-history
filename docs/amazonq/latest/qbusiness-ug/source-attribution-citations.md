# Source attribution with citations in

Amazon Q Business

The Amazon Q Business web experience chat response provides in-text source
citations for responses that use the organization's data sources and knowledge base as a
source. The chat response also provides a full list of the sources used to generate the
response.

Amazon Q Business supports source attribution with citations. If you
specify the `_source_uri` metadata field when you add metadata to your
Amazon S3 bucket, the source attribution links returned by Amazon Q Business in the
chat results will direct users to the configured URL. If you don't specify a `_source_uri`,
users can still access the source documents through clickable citation links that will
download the file at query time. This allows users to verify information even when
no source URI is configured. To learn how to add metadata for your Amazon S3
connector, see [Adding document metadata in Amazon S3](s3-metadata.md "s3-metadata.md").

**In-text source citations**

In-text citations are provided in the form of a numbered list at the end of a
sentence. To view an in-text source citation, choose a citation number. Each citation
provides the following attributes:

- **Title** – The title of the source
  document.
- **URL** – A linked URL that you can follow
  to view the source document.
- **Snippet** – The snippet from the
  document from the source document that was used to generate each sentence in the
  response.
  **Source list**

Sources used to generate the response are provided at the end of the response. Each
source listed provides the following attributes:

- **Citation number** – The number provided
  at the end of the sentences in the response.
- **Title** – The title of the document
  that's the source for the generated response.
- **Text segment** – A text extract from a
  source document that's used for source attribution.
- **URL** – The URL of the document that's
  the source for the generated response.
