

# Use `DeleteDocumentClassifier` with an AWS SDK or CLI
<a name="example_comprehend_DeleteDocumentClassifier_section"></a>

The following code examples show how to use `DeleteDocumentClassifier`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example: 
+  [Train a custom classifier and classify documents](example_comprehend_Usage_ComprehendClassifier_section.md) 

------
#### [ CLI ]

**AWS CLI**  
**To delete a custom document classifier**  
The following `delete-document-classifier` example deletes a custom document classifier model.  

```
aws comprehend delete-document-classifier \
    --document-classifier-arn {{arn:aws:comprehend:us-west-2:111122223333:document-classifier/example-classifier-1}}
```
This command produces no output.  
For more information, see [Managing Amazon Comprehend endpoints](https://docs.aws.amazon.com/comprehend/latest/dg/manage-endpoints.html) in the *Amazon Comprehend Developer Guide*.  
+  For API details, see [DeleteDocumentClassifier](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/delete-document-classifier.html) in *AWS CLI Command Reference*. 

------
#### [ Python ]

**SDK for Python (Boto3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/comprehend#code-examples). 

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
+  For API details, see [DeleteDocumentClassifier](https://docs.aws.amazon.com/goto/boto3/comprehend-2017-11-27/DeleteDocumentClassifier) in *AWS SDK for Python (Boto3) API Reference*. 

------
#### [ SAP ABAP ]

**SDK for SAP ABAP**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/cpd#code-examples). 

```
    TRY.
        oo_result = lo_cpd->deletedocumentclassifier(
          iv_documentclassifierarn = iv_classifier_arn
        ).
        MESSAGE 'Document classifier deleted.' TYPE 'I'.
      CATCH /aws1/cx_cpdinvalidrequestex.
        MESSAGE 'Invalid request.' TYPE 'E'.
      CATCH /aws1/cx_cpdtoomanyrequestsex.
        MESSAGE 'Too many requests.' TYPE 'E'.
      CATCH /aws1/cx_cpdresourcenotfoundex.
        MESSAGE 'Resource not found.' TYPE 'E'.
      CATCH /aws1/cx_cpdresourceinuseex.
        MESSAGE 'Resource in use.' TYPE 'E'.
      CATCH /aws1/cx_cpdinternalserverex.
        MESSAGE 'Internal server error occurred.' TYPE 'E'.
    ENDTRY.
```
+  For API details, see [DeleteDocumentClassifier](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using Amazon Comprehend with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.