# Training classification models

To train a model for custom classification, you define the categories and provide example documents to train the
custom model. You train the model in either multi-class or multi-label mode. Multi-class mode associates a single
class with each document. Multi-label mode associates one or more classes with each document.

Custom classification supports two types of classifier models: plain-text models and native document models. A
plain-text model classifies documents based on their text content. A native document model also classifies documents
based on text content. A native document model can also use additional signals, such as from the layout of the
document. You train a native document model with native documents for the model to learn the layout information.

Plain-text models have the following characteristics:

- You train the model using UTF-8 encoded text documents.
- You can train the model using documents in one of following languages: English, Spanish, German, Italian,
  French, or Portuguese.
- The training documents for a given classifier must all use the same language.
- Training documents are plain text, so there are no additional charges for text extraction.
  Native document models have the following characteristics:

- You train the model using semi-structured documents, which includes the following document types:
  - Digital and scanned PDF documents.
  - Word documents (DOCX).
  - Images: JPG files, PNG files, and single-page TIFF files.
  - Textract API output JSON files.

- You train the model using English documents.
- If your training documents include scanned document files, you incur additional charges for text extraction.
  See the [Amazon Comprehend Pricing](https://aws.amazon.com/comprehend/pricing "https://aws.amazon.com/comprehend/pricing") page for details.
  You can classify any of the supported document types using either type of model. However, for the most accurate
  results, we recommend using a plain-text model to classify plain-text documents and a native document model to
  classify semi-structured documents.

###### Topics

- [Train custom classifiers (console)](create-custom-classifier-console.md "create-custom-classifier-console.md")
- [Train custom classifiers (API)](train-custom-classifier-api.md "train-custom-classifier-api.md")
- [Test the training data](testing-the-model.md "testing-the-model.md")
- [Classifier training output](train-classifier-output.md "train-classifier-output.md")
- [Custom classifier metrics](cer-doc-class.md "cer-doc-class.md")
