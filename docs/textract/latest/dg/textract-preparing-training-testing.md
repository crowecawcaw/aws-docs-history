# Preparing training and testing

datasets

###### Training and Testing Datasets

The training dataset is the basis for creating an adapter. You must provide an
annotated training dataset to train an adapter. This training dataset consists of
user uploaded document pages, queries, and annotated query answers. The model learns
from this dataset to improve its performance on the type of documents you
provide.

The testing dataset is used to evaluate the adapter’s performance. The testing dataset
is created by using a slice of the original dataset that the model hasn’t seen before.
This process assesses the adapter’s performance with new data, creating accurate
measurements and metrics.

You must divide all of your documents into training and test sets. The training
set is used to train the adapter. The adapter learns the patterns contained in these
annotated documents. The test set is used to evaluate the adapter performance. If
you upload fewer than 20 documents, split them equally between train and test. If
you upload more than 20 documents, assign 70% of data to training and 30% to
testing. When splitting documents in the AWS Management Console, you can let Amazon Textract
automatically split your documents. Alternatively, you can manually divide your
documents into training and testing sets.

###### Dataset components

Datasets contain the four following components, which you must prepare yourself or
by using the AWS Management Console:

- Images - Images can be JPEG, PNG, 1-page PDF, or 1-page TIFF. If you are
  submitting multipage documents, the AWS Management Console will visualize each page
  separately for annotation.
- Annotation file - The annotation file follows the Amazon Textract Block structure,
  though it contains only QUERY and QUERY_RESULT blocks.
- Prelabeling files - This is the Block structure from the Amazon Textract current
  API response, pulled from the result of either the [DetectDocumentText](API_DetectDocumentText.md "API_DetectDocumentText.md") or
  [AnalyzeDocument](API_AnalyzeDocument.md "API_AnalyzeDocument.md")
  operations. If you have already called Amazon Textract before and stored the result
  of the operation, you can provide the references to those results. Amazon Textract
  accepts multiple prelabeling files in case your document page has multiple
  response files exported from an asynchronous API.
- Manifest file - A JSONL-based file where each line points to an annotation
  file, the prelabeling file, or an image or single-page PDF. Refer to this
  manifest file format when structuring your manifest file.
  Manifest files are contain one or more JSON lines, with each line containing
  information for a single image. What follows is a single line in a manifest file:

```

{
    "source-ref": "s3://textract-adapters-sample-bucket-129090f9e-d51c-4034-a732-48caa3b532e7/adapters/0000000000/assets/1003_3_1.png",
    "source-ref-version": "uPNKaY_2I8dxj9Kp2sO0zDUt4q3MAJen",
    "source-ref-metadata": {
        "origin-ref": "s3://textract-adapters-sample-bucket-129090f9e-d51c-4034-a732-48caa3b532e7/adapters/0000000000/original_assets/1003_3.tiff",
        "page-number": 1
    },
    "annotations-ref": "s3://textract-adapters-sample-bucket-129090f9e-d51c-4034-a732-48caa3b532e7/adapters/0000000000/annotations/1003_3_1.png.json",
    "annotations-ref-version": "nwj_MC40zsAae_idwsdEa0r4ZQaVthGs",
    "annotations-ref-metadata": {
        "prelabeling-refs": [{
            "prelabeling-ref": "s3://textract-adapters-sample-bucket-129090f9e-d51c-4034-a732-48caa3b532e7/adapters/0000000000/prelabels/fd958ee156b5b5de1ee6101dd05263120790836856774c871b877baa35e2f373/1"
            "prelabeling-ref-version": "uPNKaY_2I8dxj9Kp2sO0zDUt4q3MAJen"
        ]},
        "assignment": "TRAINING",
        "include": true,
    },
    "schema-version": "1.0"
}

```

Note that the manifest file contains the following info:

- **source-ref:** (Required) The Amazon S3 location
  of the image or single page file. The format is "s3://BUCKET/OBJECT_PATH".
- **source-ref-version:** (Optional) The Amazon S3
  object version of the image or single page file.
- **source-ref-metadata:** (Optional) Metadata about
  the **source-ref** when this image of single page
  file should is part of a multipage document. This information is helpful when
  you want to evaluate the adapter on multipage documents. When not specified, we
  consider each **source-ref** as a standalone
  document.
- _origin-ref:_ (Required) The Amazon S3
  location to the original multipage document.
- _page-number:_ (Required) Page number of the
  **source-ref** in the original document.
- **annotations-ref:** (Required) The Amazon S3
  location of the customer performed annotations on the image. The format is
  "s3://BUCKET/OBJECT_PATH".
- **annotations-ref-metadata:** (Required) Metadata
  about the annotations attribute. Holds prelabeling references, along with
  assignment type of the manifest line item, and if to include/exclude the
  document from training.
- _prelabeling-refs:_ (Required) An list of
  files from the Amazon Textract asynchronous API response of the source-ref file. Each
  file in prelabeling-refs should contain a Block property, with at most of 1000
  blocks.
- _prelabeling-ref_ (Required) The Amazon S3
  location of the automatic annotations on the image using the Amazon Textract
  API.
- _prelabeling-ref-version_ (Optional) The
  Amazon S3 object version of the prelabeling file.
- _assignment:_ (Required) Specify "TRAINING" if
  the image belongs to the training dataset. Otherwise, use "TESTING".
- _include:_ (Required) Specify true to include
  the line item for training. Otherwise, use false.
- **schema-version:** (Optional) Version of the
  manifest file. The valid value is 1.0.
  For optimal accuracy improvements, see [Best practices for Amazon Textract Custom
  Queries](best-practices-adapters.md "best-practices-adapters.md").

###### Annotating the documents with queries and responses

When annotating your documents, you can choose to auto-label your documents using
the pretrained Queries feature and then edit the labels where needed. Alternatively,
you can manually label responses for each of your document queries.

When manually labeling your documents, Amazon Textract extracts the raw text from the
document. After the raw text is extracted, you can use the AWS Management Console annotation
interface to create queries for your documents. Link these queries to the relevant
answers in your documents to establish a "ground truth" for training.

When auto-labeling your documents, you specify the appropriate queries for your
document. When you finish adding queries to your documents, Amazon Textract attempts to
extract the proper elements from your documents, generating annotations. You must then
verify the accuracy of these annotations, correcting any that are incorrect. By linking
queries to answers, you teach the model what information is important in your documents.

When creating queries, consider the types of questions you will have to ask to
retrieve the relevant data in your documents. For more information about this response
structure, see [Query
Response Structures](../../../en_us/textract/latest/dg/queryresponse.md "../../../en_us/textract/latest/dg/queryresponse.md"). For more information on best practices for queries, see
[Best Practices for Queries](../../../en_us/textract/latest/dg/bestqueries.md "../../../en_us/textract/latest/dg/bestqueries.md").

You will need to train an adapter on representative samples of your documents. When
you use the AWS Management Console for annotating the documents, the console prepares these files for
you automatically.
