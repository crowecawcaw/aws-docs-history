# Running asynchronous jobs

After you train a custom classifier, you can
use asynchronous jobs to analyze large documents or multiple documents in one batch.

Custom classification accepts a variety of input document types. For details, see
[Inputs for asynchronous custom analysis](idp-inputs-async.md "idp-inputs-async.md").

If you plan to analyze image files or scanned PDF documents, your IAM policy must grant permissions to use
two Amazon Textract API methods (DetectDocumentText and AnalyzeDocument). Amazon Comprehend invokes these methods during text extraction.
For an example policy, see
[Permissions required to perform document analysis
actions](security_iam_id-based-policy-examples.md#security-iam-based-policy-perform-cmp-actions "security_iam_id-based-policy-examples.md#security-iam-based-policy-perform-cmp-actions").

For classification of semi-structured documents (image, PDF, or Docx files) using a plain-text model,
use the `one document per file` input format. Also,
include the `DocumentReaderConfig` parameter in your [StartDocumentClassificationJob](../APIReference/API_StartDocumentClassificationJob.md "../APIReference/API_StartDocumentClassificationJob.md") request.

###### Topics

- [File formats for async analysis](class-inputs-async.md "class-inputs-async.md")
- [Analysis jobs for custom classification (console)](analysis-jobs-custom-classifier.md "analysis-jobs-custom-classifier.md")
- [Analysis jobs for custom classification (API)](analysis-jobs-custom-class-api.md "analysis-jobs-custom-class-api.md")
- [Outputs for asynchronous analysis jobs](outputs-class-async.md "outputs-class-async.md")
