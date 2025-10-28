# Use `DeleteDocumentClassifier` with an AWS SDK or CLI

The following code examples show how to use `DeleteDocumentClassifier`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in
context in the following code example:

- [Train a custom classifier and classify documents](example_comprehend_Usage_ComprehendClassifier_section.md "example_comprehend_Usage_ComprehendClassifier_section.md")

CLI

**AWS CLI**

**To delete a custom document classifier**

The following `delete-document-classifier` example deletes a custom document classifier model.

```
`aws comprehend delete-document-classifier \
 --document-classifier-arn `arn:aws:comprehend:us-west-2:111122223333:document-classifier/example-classifier-1``

```

This command produces no output.

For more information, see [Managing Amazon Comprehend endpoints](manage-endpoints.md "manage-endpoints.md") in the _Amazon Comprehend Developer Guide_.

- For API details, see
  [DeleteDocumentClassifier](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/delete-document-classifier.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/delete-document-classifier.html")
  in _AWS CLI Command Reference_.

Python

**SDK for Python (Boto3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/comprehend#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/comprehend#code-examples").

```
class ComprehendClassifier:
    """Encapsulates an Amazon Comprehend custom classifier."""

    def __init__(self, comprehend_client):
        """
        :param comprehend_client: A Boto3 Comprehend client.
        """
        self.comprehend_client = comprehend_client
        self.classifier_arn = None


    def delete(self):
        """
        Deletes the classifier.
        """
        try:
            self.comprehend_client.delete_document_classifier(
                DocumentClassifierArn=self.classifier_arn
            )
            logger.info("Deleted classifier %s.", self.classifier_arn)
            self.classifier_arn = None
        except ClientError:
            logger.exception("Couldn't deleted classifier %s.", self.classifier_arn)
            raise



```

- For API details, see
  [DeleteDocumentClassifier](../../../goto/boto3/comprehend-2017-11-27/DeleteDocumentClassifier.md "../../../goto/boto3/comprehend-2017-11-27/DeleteDocumentClassifier.md")
  in _AWS SDK for Python (Boto3) API Reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using Amazon Comprehend with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
