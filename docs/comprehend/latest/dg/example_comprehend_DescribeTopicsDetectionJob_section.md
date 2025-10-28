# Use `DescribeTopicsDetectionJob` with an AWS SDK or CLI

The following code examples show how to use `DescribeTopicsDetectionJob`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in
context in the following code example:

- [Run a topic modeling job on sample data](example_comprehend_Usage_TopicModeler_section.md "example_comprehend_Usage_TopicModeler_section.md")

CLI

**AWS CLI**

**To describe a topics detection job**

The following `describe-topics-detection-job` example gets the properties of an asynchronous topics detection job.

```
`aws comprehend describe-topics-detection-job \
 --job-id `123456abcdeb0e11022f22a11EXAMPLE``

```

Output:

```
{
    "TopicsDetectionJobProperties": {
        "JobId": "123456abcdeb0e11022f22a11EXAMPLE",
        "JobArn": "arn:aws:comprehend:us-west-2:111122223333:topics-detection-job/123456abcdeb0e11022f22a11EXAMPLE",
        "JobName": "example_topics_detection",
        "JobStatus": "IN_PROGRESS",
        "SubmitTime": "2023-06-09T18:44:43.414000+00:00",
        "InputDataConfig": {
            "S3Uri": "s3://amzn-s3-demo-bucket",
            "InputFormat": "ONE_DOC_PER_LINE"
        },
        "OutputDataConfig": {
            "S3Uri": "s3://amzn-s3-demo-destination-bucket/testfolder/111122223333-TOPICS-123456abcdeb0e11022f22a11EXAMPLE/output/output.tar.gz"
        },
        "NumberOfTopics": 10,
        "DataAccessRoleArn": "arn:aws:iam::111122223333:role/service-role/AmazonComprehendServiceRole-examplerole"
    }
}
```

For more information, see [Async analysis for Amazon Comprehend insights](api-async-insights.md "api-async-insights.md") in the _Amazon Comprehend Developer Guide_.

- For API details, see
  [DescribeTopicsDetectionJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/describe-topics-detection-job.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/describe-topics-detection-job.html")
  in _AWS CLI Command Reference_.

Python

**SDK for Python (Boto3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/comprehend#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/comprehend#code-examples").

```
class ComprehendTopicModeler:
    """Encapsulates a Comprehend topic modeler."""

    def __init__(self, comprehend_client):
        """
        :param comprehend_client: A Boto3 Comprehend client.
        """
        self.comprehend_client = comprehend_client


    def describe_job(self, job_id):
        """
        Gets metadata about a topic modeling job.

        :param job_id: The ID of the job to look up.
        :return: Metadata about the job.
        """
        try:
            response = self.comprehend_client.describe_topics_detection_job(
                JobId=job_id
            )
            job = response["TopicsDetectionJobProperties"]
            logger.info("Got topic detection job %s.", job_id)
        except ClientError:
            logger.exception("Couldn't get topic detection job %s.", job_id)
            raise
        else:
            return job



```

- For API details, see
  [DescribeTopicsDetectionJob](../../../goto/boto3/comprehend-2017-11-27/DescribeTopicsDetectionJob.md "../../../goto/boto3/comprehend-2017-11-27/DescribeTopicsDetectionJob.md")
  in _AWS SDK for Python (Boto3) API Reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using Amazon Comprehend with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
