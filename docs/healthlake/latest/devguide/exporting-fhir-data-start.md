# Starting a FHIR export job

Use `StartFHIRExportJob` to start a FHIR export job from a HealthLake data store.
The following menus provide a procedure for the AWS Management Console and code examples for the AWS CLI and
AWS SDKs. For more information, see [`StartFHIRExportJob`](../APIReference/API_StartFHIRExportJob.md "../APIReference/API_StartFHIRExportJob.md") in the _AWS HealthLake API
Reference_.

###### Note

HealthLake supports the [FHIR R4
specification](https://hl7.org/fhir/R4/index.html "https://hl7.org/fhir/R4/index.html") for health care data exchange. Therefore, all health data is exported
in FHIR R4 format.

###### To start a FHIR export job

Choose a menu based on your access preference to AWS HealthLake.

CLI

**AWS CLI**

**To start a FHIR export job**

The following `start-fhir-export-job` example shows how to start a FHIR export job using AWS HealthLake.

```
`aws healthlake start-fhir-export-job \
 --output-data-config '`{"S3Configuration": {"S3Uri":"s3://(Bucket Name)/(Prefix Name)/","KmsKeyId":"arn:aws:kms:us-east-1:012345678910:key/d330e7fc-b56c-4216-a250-f4c43ef46e83"}}`' \
 --datastore-id `(Data` `store` `ID)` \
 --data-access-role-arn `arn:aws:iam::(AWS` `Account` `ID):role/(Role` `Name)``

```

Output:

```
{
    "DatastoreId": "(Data store ID)",
    "JobStatus": "SUBMITTED",
    "JobId": "9b9a51943afaedd0a8c0c26c49135a31"
}
```

- For API details, see
  [StartFHIRExportJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/healthlake/start-fhir-export-job.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/healthlake/start-fhir-export-job.html")
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


    def start_fhir_export_job(
        self,
        job_name: str,
        datastore_id: str,
        output_s3_uri: str,
        kms_key_id: str,
        data_access_role_arn: str,
    ) -> dict[str, str]:
        """
        Starts a HealthLake export job.
        :param job_name: The export job name.
        :param datastore_id: The data store ID.
        :param output_s3_uri: The output S3 URI.
        :param kms_key_id: The KMS key ID associated with the output S3 bucket.
        :param data_access_role_arn: The data access role ARN.
        :return: The export job.
        """
        try:
            response = self.health_lake_client.start_fhir_export_job(
                OutputDataConfig={
                    "S3Configuration": {"S3Uri": output_s3_uri, "KmsKeyId": kms_key_id}
                },
                DataAccessRoleArn=data_access_role_arn,
                DatastoreId=datastore_id,
                JobName=job_name,
            )

            return response
        except ClientError as err:
            logger.exception(
                "Couldn't start export job. Here's why %s",
                err.response["Error"]["Message"],
            )
            raise



```

- For API details, see
  [StartFHIRExportJob](../../../goto/boto3/healthlake-2017-07-01/StartFHIRExportJob.md "../../../goto/boto3/healthlake-2017-07-01/StartFHIRExportJob.md")
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
3. Choose **Export**.

The **Export** page opens. 4. Under the **Output data** section, enter the following
information:

    * **Output data location in Amazon S3**
    * **Output encyryption**

5. Under the **Access permissions** section, choose **Use an
   existing IAM service role** and select the role from the **Role
   name** menu or choose **Create an IAM role**.
6. Choose **Export data**.

###### Note

During export, choose **Copy job ID** on the banner at the top
of the page. You can use the [`JobID`](../APIReference/API_DescribeFHIRExportJob.md#HealthLake-DescribeFHIRExportJob-request-JobId "../APIReference/API_DescribeFHIRExportJob.md#HealthLake-DescribeFHIRExportJob-request-JobId") to request export job properties using the AWS CLI. For
more information, see [Getting FHIR export job properties](exporting-fhir-data-describe.md "exporting-fhir-data-describe.md").
