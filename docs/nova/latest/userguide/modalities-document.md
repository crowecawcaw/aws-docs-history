# Document understanding

The Amazon Nova models allow you to include documents in the payload through the Converse API
document support, which can be provided as bytes to the API. The document support has two
different variants as explained below:

- First, **text based document types** like (TXT, CSV,
  MD, and so on) where the emphasis is on text understanding. These use cases include
  answering based on textual elements in the documents.
- Second, **Media based document types** like (PDF,
  DOCX), where the emphasis is on vision-based understanding to answer questions.
  These use cases include answering questions based on charts, graphs, and so
  on.

JPEG2000 and JBIG2 aren't supported in PDF files in Amazon Nova.

## Document size limitations

Any text documents (CSV, XLS, XLSX, HTML, TXT, MD or DOC) that you include must not
exceed 4.5 MB per document. All included media documents, including PDF and DOCX files,
must not exceed 25 MB in total when uploaded from your computer or 2 GB when uploaded from Amazon S3. You can include a maximum of 5 documents from your computer or Amazon S3. Any documents
that exceed these limits are rejected by Amazon Nova.
