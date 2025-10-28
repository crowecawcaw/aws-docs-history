# Use `DescribeDocumentClassificationJob` with an AWS SDK or CLI

The following code examples show how to use `DescribeDocumentClassificationJob`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in
context in the following code example:

- [Train a custom classifier and classify documents](example_comprehend_Usage_ComprehendClassifier_section.md "example_comprehend_Usage_ComprehendClassifier_section.md")

CLI

**AWS CLI**

**To describe a document classification job**

The following `describe-document-classification-job` example gets the properties of an asynchronous document classification job.

```
`aws comprehend describe-document-classification-job \
 --job-id `123456abcdeb0e11022f22a11EXAMPLE``

```

Output:

```
{
    "DocumentClassificationJobProperties": {
        "JobId": "123456abcdeb0e11022f22a11EXAMPLE",
        "JobArn": "arn:aws:comprehend:us-west-2:111122223333:document-classification-job/123456abcdeb0e11022f22a11EXAMPLE",
        "JobName": "exampleclassificationjob",
        "JobStatus": "COMPLETED",
        "SubmitTime": "2023-06-14T17:09:51.788000+00:00",
        "EndTime": "2023-06-14T17:15:58.582000+00:00",
        "DocumentClassifierArn": "arn:aws:comprehend:us-west-2:111122223333:document-classifier/mymodel/version/1",
        "InputDataConfig": {
            "S3Uri": "s3://amzn-s3-demo-bucket/jobdata/",
            "InputFormat": "ONE_DOC_PER_LINE"
        },
        "OutputDataConfig": {
            "S3Uri": "s3://amzn-s3-demo-destination-bucket/testfolder/111122223333-CLN-123456abcdeb0e11022f22a11EXAMPLE/output/output.tar.gz"
        },
        "DataAccessRoleArn": "arn:aws:iam::111122223333:role/service-role/AmazonComprehendServiceRole-servicerole"
    }
}
```

For more information, see [Custom Classification](how-document-classification.md "how-document-classification.md") in the _Amazon Comprehend Developer Guide_.

- For API details, see
  [DescribeDocumentClassificationJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/describe-document-classification-job.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/describe-document-classification-job.html")
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


    def describe_job(self, job_id):
        """
        Gets metadata about a classification job.

        :param job_id: The ID of the job to look up.
        :return: Metadata about the job.
        """
        try:
            response = self.comprehend_client.describe_document_classification_job(
                JobId=job_id
            )
            job = response["DocumentClassificationJobProperties"]
            logger.info("Got classification job %s.", job["JobName"])
        except ClientError:
            logger.exception("Couldn't get classification job %s.", job_id)
            raise
        else:
            return job



```

- For API details, see
  [DescribeDocumentClassificationJob](../../../goto/boto3/comprehend-2017-11-27/DescribeDocumentClassificationJob.md "../../../goto/boto3/comprehend-2017-11-27/DescribeDocumentClassificationJob.md")
  in _AWS SDK for Python (Boto3) API Reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using Amazon Comprehend with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
