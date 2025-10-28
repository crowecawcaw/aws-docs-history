# Text analysis API operations

Use Amazon Comprehend Medical to examine clinical documents and to gain various insights about their content using pre-trained natural language processing (NLP) models. You can perform analysis both on single files or as a batch analysis on multiple files stored in an Amazon Simple Storage Service (S3) bucket.

With Amazon Comprehend Medical, you can perform the following on your documents:

- [Detect entities (Version 2)](textanalysis-entitiesv2.md "textanalysis-entitiesv2.md") — Examine unstructured clinical text to detect textual references to medical information such as medical condition, treatment, tests and results, and medications. This version uses a different model than the original Detect entities API, and there are a few changes in the output.
- [Detect PHI](textanalysis-phi.md "textanalysis-phi.md") — Examine unstructured clinical text to detect textual references to protected health information (PHI) such as names and addresses.
  Amazon Comprehend Medical also includes multiple API operations that you can use to perform batch text analysis on clinical documents. To learn more about how to use these API operations, see [Text analysis batch APIs](textanalysis-batchapi.md "textanalysis-batchapi.md").

###### Topics

- [Detect entities (Version 2)](textanalysis-entitiesv2.md "textanalysis-entitiesv2.md")
- [Detect PHI](textanalysis-phi.md "textanalysis-phi.md")
- [Text analysis batch APIs](textanalysis-batchapi.md "textanalysis-batchapi.md")
