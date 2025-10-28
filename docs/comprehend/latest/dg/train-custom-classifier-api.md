# Train custom classifiers (API)

To create and train a custom classifier, use the [CreateDocumentClassifier](../APIReference/API_CreateDocumentClassifier.md "../APIReference/API_CreateDocumentClassifier.md") operation.

You can monitor the progress of the request using the [DescribeDocumentClassifier](../APIReference/API_DescribeDocumentClassifier.md "../APIReference/API_DescribeDocumentClassifier.md") operation. After
the `Status` field transitions to `TRAINED`, you can use the classifier to classify documents.
If the status is `TRAINED_WITH_WARNINGS`, review the skipped files folder in the [Classifier training output](train-classifier-output.md "train-classifier-output.md") from the
`CreateDocumentClassifier` operation.

###### Topics

- [Training custom classification using the AWS Command Line Interface](#get-started-api-customclass-cli "#get-started-api-customclass-cli")
- [Using the AWS SDK for Java or SDK for Python](#get-started-api-customclass-java "#get-started-api-customclass-java")

## Training custom classification using the AWS Command Line Interface

The following examples show how to use the `CreateDocumentClassifier` operation, the
`DescribeDocumentClassificationJob` operation, and other custom classifier APIs with the AWS CLI.

The examples are formatted for Unix, Linux, and macOS. For Windows, replace the
backslash (\) Unix continuation character at the end of each line with a caret
(^).

Create a plain-text custom classifier using the `create-document-classifier`
operation.

```
aws comprehend create-document-classifier \
     --region `region` \
     --document-classifier-name testDelete \
     --language-code en \
     --input-data-config S3Uri=s3://`S3Bucket`/docclass/`file name` \
     --data-access-role-arn arn:aws:iam::`account number`:role/testFlywheelDataAccess
```

To create a native custom classifier, provide the following additional parameters in the
`create-document-classifier` request.

1. DocumentType: set the value to SEMI_STRUCTURED_DOCUMENT.
2. Documents: the S3 location for the training documents (and, optionally, the test documents).
3. OutputDataConfig: provide the S3 location for the output documents (and an optional KMS key).
4. DocumentReaderConfig: Optional field for text extraction settings.

```
aws comprehend create-document-classifier \
     --region `region` \
     --document-classifier-name testDelete \
     --language-code en \
     --input-data-config
          S3Uri=s3://`S3Bucket`/docclass/`file name` \
           DocumentType \
             Documents  \
     --output-data-config S3Uri=s3://`S3Bucket`/docclass/`file name` \
     --data-access-role-arn arn:aws:iam::`account number`:role/testFlywheelDataAccess
```

Get information on a custom classifier with the document classifier ARN using the
`DescribeDocumentClassifier` operation.

```
aws comprehend describe-document-classifier \
     --region `region` \
     --document-classifier-arn arn:aws:comprehend:`region`:`account number`:document-classifier/`file name`
```

Delete a custom classifier using the `DeleteDocumentClassifier`
operation.

```
aws comprehend delete-document-classifier \
     --region `region` \
     --document-classifier-arn arn:aws:comprehend:`region`:`account number`:document-classifier/testDelete
```

List all custom classifiers in the account using the
`ListDocumentClassifiers` operation.

```
aws comprehend list-document-classifiers
     --region `region`
```

## Using the AWS SDK for Java or SDK for Python

For SDK examples of how to create and train a custom classifier , see [Use CreateDocumentClassifier with an AWS SDK or CLI](example_comprehend_CreateDocumentClassifier_section.md "example_comprehend_CreateDocumentClassifier_section.md").
