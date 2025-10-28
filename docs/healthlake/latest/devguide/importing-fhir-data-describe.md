# Getting FHIR import job properties

Use `DescribeFHIRImportJob` to get FHIR import job properties. The following menus provide
a procedure for the AWS Management Console and code examples for the AWS CLI and AWS SDKs. For more
information, see [`DescribeFHIRImportJob`](../APIReference/API_DescribeFHIRImportJob.md "../APIReference/API_DescribeFHIRImportJob.md") in the _AWS HealthLake API Reference_.

###### To get FHIR import job properties

Choose a menu based on your access preference to AWS HealthLake.

CLI

**AWS CLI**

**To describe a FHIR import job**

The following `describe-fhir-import-job` example shows how to learn the properties of a FHIR import job using AWS HealthLake.

```
`aws healthlake describe-fhir-import-job \
 --datastore-id `(Data` `store` `ID)` \
 --job-id `c145fbb27b192af392f8ce6e7838e34f``

```

Output:

```
{
    "ImportJobProperties": {
    "InputDataConfig": {
        "S3Uri": "s3://(Bucket Name)/(Prefix Name)/"
        { "arrayitem2": 2 }
    },
    "DataAccessRoleArn": "arn:aws:iam::(AWS Account ID):role/(Role Name)",
    "JobStatus": "COMPLETED",
    "JobId": "c145fbb27b192af392f8ce6e7838e34f",
    "SubmitTime": 1606272542.161,
    "EndTime": 1606272609.497,
    "DatastoreId": "(Data store ID)"
    }
}
```

- For API details, see
  [DescribeFHIRImportJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/healthlake/describe-fhir-import-job.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/healthlake/describe-fhir-import-job.html")
  in _AWS CLI Command Reference_.

Python

**SDK for Python (Boto3)**

```
    @classmethod
    def from_client(cls) -> "HealthLakeWrapper":
        """
        Creates a HealthLakeWrapper instance with a default AWS HealthLake client.

        :return: An instance of HealthLakeWrapper initialized with the default HealthLake client.
        """
        health_lake_client = boto3.client("healthlake")
        return cls(health_lake_client)


    def describe_fhir_import_job(
        self, datastore_id: str, job_id: str
    ) -> dict[str, any]:
        """
        Describes a HealthLake import job.
        :param datastore_id: The data store ID.
        :param job_id: The import job ID.
        :return: The import job description.
        """
        try:
            response = self.health_lake_client.describe_fhir_import_job(
                DatastoreId=datastore_id, JobId=job_id
            )
            return response["ImportJobProperties"]
        except ClientError as err:
            logger.exception(
                "Couldn't describe import job with ID %s. Here's why %s",
                job_id,
                err.response["Error"]["Message"],
            )
            raise



```

- For API details, see
  [DescribeFHIRImportJob](../../../goto/boto3/healthlake-2017-07-01/DescribeFHIRImportJob.md "../../../goto/boto3/healthlake-2017-07-01/DescribeFHIRImportJob.md")
  in _AWS SDK for Python (Boto3) API Reference_.

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/healthlake#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/healthlake#code-examples").

###### Example availability

Can't find what you need? Request a code example using the **Provide
feedback** link on the right sidebar of this page.

###### Note

FHIR import job information is not available on the HealthLake Console. Instead, use the AWS CLI
with `DescribeFHIRImportJob` to request import job properties such as [`JobStatus`](../APIReference/API_ImportJobProperties.md#HealthLake-Type-ImportJobProperties-JobStatus "../APIReference/API_ImportJobProperties.md#HealthLake-Type-ImportJobProperties-JobStatus"). For more information, refer to the AWS CLI example on this
page.
