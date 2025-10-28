# Starting a FHIR import job

Use `StartFHIRImportJob` to start a FHIR import job into a HealthLake data store. The following
menus provide a procedure for the AWS Management Console and code examples for the AWS CLI and AWS SDKs. For
more information, see [`StartFHIRImportJob`](../APIReference/API_StartFHIRImportJob.md "../APIReference/API_StartFHIRImportJob.md")
in the _AWS HealthLake API Reference_.

###### Important

HealthLake supports the [FHIR R4
specification](https://hl7.org/fhir/R4/index.html "https://hl7.org/fhir/R4/index.html") for health care data exchange. If needed, you can work with an [AWS HealthLake Partner](https://aws.amazon.com/healthlake/partners/ "https://aws.amazon.com/healthlake/partners/") to convert your health
data to FHIR R4 format prior to import.

###### To start a FHIR import job

Choose a menu based on your access preference to AWS HealthLake.

CLI

**AWS CLI**

**To start a FHIR import job**

The following `start-fhir-import-job` example shows how to start a FHIR import job using AWS HealthLake.

```
`aws healthlake start-fhir-import-job \
 --input-data-config S3Uri="s3://(Bucket Name)/(Prefix Name)/" \
 --job-output-data-config '`{"S3Configuration": {"S3Uri":"s3://(Bucket Name)/(Prefix Name)/","KmsKeyId":"arn:aws:kms:us-east-1:012345678910:key/d330e7fc-b56c-4216-a250-f4c43ef46e83"}}`' \
 --datastore-id `(Data` `store` `ID)` \
 --data-access-role-arn `"arn:aws:iam::(AWS Account ID):role/(Role Name)"``

```

Output:

```
{
    "DatastoreId": "(Data store ID)",
    "JobStatus": "SUBMITTED",
    "JobId": "c145fbb27b192af392f8ce6e7838e34f"
}
```

- For API details, see
  [StartFHIRImportJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/healthlake/start-fhir-import-job.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/healthlake/start-fhir-import-job.html")
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


    def start_fhir_import_job(
        self,
        job_name: str,
        datastore_id: str,
        input_s3_uri: str,
        job_output_s3_uri: str,
        kms_key_id: str,
        data_access_role_arn: str,
    ) -> dict[str, str]:
        """
        Starts a HealthLake import job.
        :param job_name: The import job name.
        :param datastore_id: The data store ID.
        :param input_s3_uri: The input S3 URI.
        :param job_output_s3_uri: The job output S3 URI.
        :param kms_key_id: The KMS key ID associated with the output S3 bucket.
        :param data_access_role_arn: The data access role ARN.
        :return: The import job.
        """
        try:
            response = self.health_lake_client.start_fhir_import_job(
                JobName=job_name,
                InputDataConfig={"S3Uri": input_s3_uri},
                JobOutputDataConfig={
                    "S3Configuration": {
                        "S3Uri": job_output_s3_uri,
                        "KmsKeyId": kms_key_id,
                    }
                },
                DataAccessRoleArn=data_access_role_arn,
                DatastoreId=datastore_id,
            )
            return response
        except ClientError as err:
            logger.exception(
                "Couldn't start import job. Here's why %s",
                err.response["Error"]["Message"],
            )
            raise



```

- For API details, see
  [StartFHIRImportJob](../../../goto/boto3/healthlake-2017-07-01/StartFHIRImportJob.md "../../../goto/boto3/healthlake-2017-07-01/StartFHIRImportJob.md")
  in _AWS SDK for Python (Boto3) API Reference_.

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/healthlake#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/healthlake#code-examples").

###### Example availability

Can't find what you need? Request a code example using the **Provide
feedback** link on the right sidebar of this page.

1. Sign in to the [Data stores](https://console.aws.amazon.com/healthlake/home#/list-datastores "https://console.aws.amazon.com/healthlake/home#/list-datastores") page on the HealthLake Console.
2. Choose a data store.
3. Choose **Import**.

The **Import** page opens. 4. Under the **Input data** section, enter the following
information:

    * **Input data location in Amazon S3**

5. Under the **Import output files** section, enter the following
   information:
   - **Import output files location in Amazon S3**

   - **Import output files encryption**

6. Under the **Access permissions** section, choose **Use an
   existing IAM service role** and select the role from the **Service
   role name** menu or choose **Create an IAM role**.
7. Choose **Import data**.

###### Note

During import, choose **Copy job ID** on the banner at the top
of the page. You can use the [`JobID`](../APIReference/API_DescribeFHIRImportJob.md#HealthLake-DescribeFHIRImportJob-request-JobId "../APIReference/API_DescribeFHIRImportJob.md#HealthLake-DescribeFHIRImportJob-request-JobId") to request import job properties using the AWS CLI. For
more information, see [Getting FHIR import job properties](importing-fhir-data-describe.md "importing-fhir-data-describe.md").
