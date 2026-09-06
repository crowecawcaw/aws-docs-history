

# Getting FHIR export job properties
<a name="exporting-fhir-data-describe"></a>

Use `DescribeFHIRExportJob` to get export job properties from a HealthLake data store. The following menus provide a procedure for the AWS Management Console and code examples for the AWS CLI and AWS SDKs. For more information, see [`DescribeFHIRExportJob`](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_DescribeFHIRExportJob.html) in the *AWS HealthLake API Reference*.

**Note**  
HealthLake supports the [FHIR R4 specification](https://hl7.org/fhir/R4/index.html) for health care data exchange. Therefore, all health data is exported in FHIR R4 format.

**To describe a FHIR export job**  
Choose a menu based on your access preference to AWS HealthLake.

## AWS CLI and SDKs
<a name="describe-export-job-cli-sdk"></a>

------
#### [ CLI ]

**AWS CLI**  
**To describe a FHIR export job**  
The following `describe-fhir-export-job` example shows how to find the properties of a FHIR export job in AWS HealthLake.  

```
aws healthlake describe-fhir-export-job \
    --datastore-id {{(Data}} {{store}} {{ID)}} \
    --job-id {{9b9a51943afaedd0a8c0c26c49135a31}}
```
Output:  

```
{
    "ExportJobProperties": {
        "DataAccessRoleArn": "arn:aws:iam::(AWS Account ID):role/(Role Name)",
        "JobStatus": "IN_PROGRESS",
        "JobId": "9009813e9d69ba7cf79bcb3468780f16",
        "SubmitTime": "2024-11-20T11:31:46.672000-05:00",
        "EndTime": "2024-11-20T11:34:01.636000-05:00",
        "OutputDataConfig": {
            "S3Configuration": {
            "S3Uri": "s3://(Bucket Name)/(Prefix Name)/",
            "KmsKeyId": "arn:aws:kms:us-east-1:012345678910:key/d330e7fc-b56c-4216-a250-f4c43ef46e83"
        }

        },
        "DatastoreId": "(Data store ID)"
    }
}
```
  
+  For API details, see [DescribeFHIRExportJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/healthlake/describe-fhir-export-job.html) in *AWS CLI Command Reference*. 

------
#### [ Python ]

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


    def describe_fhir_export_job(
        self, datastore_id: str, job_id: str
    ) -> dict[str, any]:
        """
        Describes a HealthLake export job.
        :param datastore_id: The data store ID.
        :param job_id: The export job ID.
        :return: The export job description.
        """
        try:
            response = self.health_lake_client.describe_fhir_export_job(
                DatastoreId=datastore_id, JobId=job_id
            )
            return response["ExportJobProperties"]
        except ClientError as err:
            logger.exception(
                "Couldn't describe export job with ID %s. Here's why %s",
                job_id,
                err.response["Error"]["Message"],
            )
            raise
```
+  For API details, see [DescribeFHIRExportJob](https://docs.aws.amazon.com/goto/boto3/healthlake-2017-07-01/DescribeFHIRExportJob) in *AWS SDK for Python (Boto3) API Reference*. 
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/healthlake#code-examples). 

------
#### [ SAP ABAP ]

**SDK for SAP ABAP**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/hll#code-examples). 

```
    TRY.
        " iv_datastore_id = 'a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6'
        " iv_job_id = 'a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6'
        oo_result = lo_hll->describefhirexportjob(
          iv_datastoreid = iv_datastore_id
          iv_jobid = iv_job_id
        ).
        DATA(lo_export_job_properties) = oo_result->get_exportjobproperties( ).
        IF lo_export_job_properties IS BOUND.
          DATA(lv_job_status) = lo_export_job_properties->get_jobstatus( ).
          MESSAGE |Export job status: { lv_job_status }.| TYPE 'I'.
        ENDIF.
      CATCH /aws1/cx_hllresourcenotfoundex INTO DATA(lo_notfound_ex).
        DATA(lv_error) = |Resource not found: { lo_notfound_ex->av_err_code }-{ lo_notfound_ex->av_err_msg }|.
        MESSAGE lv_error TYPE 'I'.
        RAISE EXCEPTION lo_notfound_ex.
      CATCH /aws1/cx_hllvalidationex INTO DATA(lo_validation_ex).
        lv_error = |Validation error: { lo_validation_ex->av_err_code }-{ lo_validation_ex->av_err_msg }|.
        MESSAGE lv_error TYPE 'I'.
        RAISE EXCEPTION lo_validation_ex.
    ENDTRY.
```
+  For API details, see [DescribeFHIRExportJob](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*. 

------

**Example availability**  
Can't find what you need? Request a code example using the **Provide feedback** link on the right sidebar of this page.

## AWS Console
<a name="describe-export-job-console"></a>

**Note**  
FHIR export job information is not available on the HealthLake Console. Instead, use the AWS CLI with `DescribeFHIRExportJob` to request export job properties such as [`JobStatus`](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_ExportJobProperties.html#HealthLake-Type-ExportJobProperties-JobStatus). For more information, refer to the AWS CLI example on this page.