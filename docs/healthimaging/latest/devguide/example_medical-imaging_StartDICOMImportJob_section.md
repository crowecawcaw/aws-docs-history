# Use `StartDICOMImportJob` with an AWS SDK or CLI

The following code examples show how to use `StartDICOMImportJob`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in
context in the following code example:

- [Get started with image sets and image frames](example_medical-imaging_Scenario_ImageSetsAndFrames_section.md "example_medical-imaging_Scenario_ImageSetsAndFrames_section.md")

C++

**SDK for C++**

```
//! Routine which starts a HealthImaging import job.
/*!
  \param dataStoreID: The HealthImaging data store ID.
  \param inputBucketName: The name of the Amazon S3 bucket containing the DICOM files.
  \param inputDirectory: The directory in the S3 bucket containing the DICOM files.
  \param outputBucketName: The name of the S3 bucket for the output.
  \param outputDirectory: The directory in the S3 bucket to store the output.
  \param roleArn: The ARN of the IAM role with permissions for the import.
  \param importJobId: A string to receive the import job ID.
  \param clientConfig: Aws client configuration.
  \return bool: Function succeeded.
  */
bool AwsDoc::Medical_Imaging::startDICOMImportJob(
        const Aws::String &dataStoreID, const Aws::String &inputBucketName,
        const Aws::String &inputDirectory, const Aws::String &outputBucketName,
        const Aws::String &outputDirectory, const Aws::String &roleArn,
        Aws::String &importJobId,
        const Aws::Client::ClientConfiguration &clientConfig) {
    Aws::MedicalImaging::MedicalImagingClient medicalImagingClient(clientConfig);
    Aws::String inputURI = "s3://" + inputBucketName + "/" + inputDirectory + "/";
    Aws::String outputURI = "s3://" + outputBucketName + "/" + outputDirectory + "/";
    Aws::MedicalImaging::Model::StartDICOMImportJobRequest startDICOMImportJobRequest;
    startDICOMImportJobRequest.SetDatastoreId(dataStoreID);
    startDICOMImportJobRequest.SetDataAccessRoleArn(roleArn);
    startDICOMImportJobRequest.SetInputS3Uri(inputURI);
    startDICOMImportJobRequest.SetOutputS3Uri(outputURI);

    Aws::MedicalImaging::Model::StartDICOMImportJobOutcome startDICOMImportJobOutcome = medicalImagingClient.StartDICOMImportJob(
            startDICOMImportJobRequest);

    if (startDICOMImportJobOutcome.IsSuccess()) {
        importJobId = startDICOMImportJobOutcome.GetResult().GetJobId();
    }
    else {
        std::cerr << "Failed to start DICOM import job because "
                  << startDICOMImportJobOutcome.GetError().GetMessage() << std::endl;
    }

    return startDICOMImportJobOutcome.IsSuccess();
}



```

- For API details, see
  [StartDICOMImportJob](../../../goto/SdkForCpp/medical-imaging-2023-07-19/StartDICOMImportJob.md "../../../goto/SdkForCpp/medical-imaging-2023-07-19/StartDICOMImportJob.md")
  in _AWS SDK for C++ API Reference_.

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/medical-imaging/#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/medical-imaging/#code-examples").

CLI

**AWS CLI**

**To start a dicom import job**

The following `start-dicom-import-job` code example starts a dicom import job.

```
`aws medical-imaging start-dicom-import-job \
 --job-name `"my-job"` \
 --datastore-id `"12345678901234567890123456789012"` \
 --input-s3-uri `"s3://medical-imaging-dicom-input/dicom_input/"` \
 --output-s3-uri `"s3://medical-imaging-output/job_output/"` \
 --data-access-role-arn `"arn:aws:iam::123456789012:role/ImportJobDataAccessRole"``

```

Output:

```
{
    "datastoreId": "12345678901234567890123456789012",
    "jobId": "09876543210987654321098765432109",
    "jobStatus": "SUBMITTED",
    "submittedAt": "2022-08-12T11:28:11.152000+00:00"
}
```

- For API details, see
  [StartDICOMImportJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medical-imaging/start-dicom-import-job.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medical-imaging/start-dicom-import-job.html")
  in _AWS CLI Command Reference_.

Java

**SDK for Java 2.x**

```
    public static String startDicomImportJob(MedicalImagingClient medicalImagingClient,
            String jobName,
            String datastoreId,
            String dataAccessRoleArn,
            String inputS3Uri,
            String outputS3Uri) {

        try {
            StartDicomImportJobRequest startDicomImportJobRequest = StartDicomImportJobRequest.builder()
                    .jobName(jobName)
                    .datastoreId(datastoreId)
                    .dataAccessRoleArn(dataAccessRoleArn)
                    .inputS3Uri(inputS3Uri)
                    .outputS3Uri(outputS3Uri)
                    .build();
            StartDicomImportJobResponse response = medicalImagingClient.startDICOMImportJob(startDicomImportJobRequest);
            return response.jobId();
        } catch (MedicalImagingException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }

        return "";
    }


```

- For API details, see
  [StartDICOMImportJob](../../../goto/SdkForJavaV2/medical-imaging-2023-07-19/StartDICOMImportJob.md "../../../goto/SdkForJavaV2/medical-imaging-2023-07-19/StartDICOMImportJob.md")
  in _AWS SDK for Java 2.x API Reference_.

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/medicalimaging#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/medicalimaging#code-examples").

JavaScript

**SDK for JavaScript (v3)**

```
import { StartDICOMImportJobCommand } from "@aws-sdk/client-medical-imaging";
import { medicalImagingClient } from "../libs/medicalImagingClient.js";

/**
 * @param {string} jobName - The name of the import job.
 * @param {string} datastoreId - The ID of the data store.
 * @param {string} dataAccessRoleArn - The Amazon Resource Name (ARN) of the role that grants permission.
 * @param {string} inputS3Uri - The URI of the S3 bucket containing the input files.
 * @param {string} outputS3Uri - The URI of the S3 bucket where the output files are stored.
 */
export const startDicomImportJob = async (
  jobName = "test-1",
  datastoreId = "12345678901234567890123456789012",
  dataAccessRoleArn = "arn:aws:iam::xxxxxxxxxxxx:role/ImportJobDataAccessRole",
  inputS3Uri = "s3://medical-imaging-dicom-input/dicom_input/",
  outputS3Uri = "s3://medical-imaging-output/job_output/",
) => {
  const response = await medicalImagingClient.send(
    new StartDICOMImportJobCommand({
      jobName: jobName,
      datastoreId: datastoreId,
      dataAccessRoleArn: dataAccessRoleArn,
      inputS3Uri: inputS3Uri,
      outputS3Uri: outputS3Uri,
    }),
  );
  console.log(response);
  // {
  //     '$metadata': {
  //     httpStatusCode: 200,
  //         requestId: '6e81d191-d46b-4e48-a08a-cdcc7e11eb79',
  //         extendedRequestId: undefined,
  //         cfId: undefined,
  //         attempts: 1,
  //         totalRetryDelay: 0
  // },
  //     datastoreId: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
  //     jobId: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
  //     jobStatus: 'SUBMITTED',
  //     submittedAt: 2023-09-22T14:48:45.767Z
  // }
  return response;
};


```

- For API details, see
  [StartDICOMImportJob](../../../AWSJavaScriptSDK/v3/latest/client/medical-imaging/command/StartDICOMImportJobCommand.md "../../../AWSJavaScriptSDK/v3/latest/client/medical-imaging/command/StartDICOMImportJobCommand.md")
  in _AWS SDK for JavaScript API Reference_.

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/medical-imaging#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/medical-imaging#code-examples").

Python

**SDK for Python (Boto3)**

```
class MedicalImagingWrapper:
    def __init__(self, health_imaging_client):
        self.health_imaging_client = health_imaging_client


    def start_dicom_import_job(
        self, job_name, datastore_id, role_arn, input_s3_uri, output_s3_uri
    ):
        """
        Start a DICOM import job.

        :param job_name: The name of the job.
        :param datastore_id: The ID of the data store.
        :param role_arn: The Amazon Resource Name (ARN) of the role to use for the job.
        :param input_s3_uri: The S3 bucket input prefix path containing the DICOM files.
        :param output_s3_uri: The S3 bucket output prefix path for the result.
        :return: The job ID.
        """
        try:
            job = self.health_imaging_client.start_dicom_import_job(
                jobName=job_name,
                datastoreId=datastore_id,
                dataAccessRoleArn=role_arn,
                inputS3Uri=input_s3_uri,
                outputS3Uri=output_s3_uri,
            )
        except ClientError as err:
            logger.error(
                "Couldn't start DICOM import job. Here's why: %s: %s",
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise
        else:
            return job["jobId"]



```

The following code instantiates the MedicalImagingWrapper object.

```
    client = boto3.client("medical-imaging")
    medical_imaging_wrapper = MedicalImagingWrapper(client)


```

- For API details, see
  [StartDICOMImportJob](../../../goto/boto3/medical-imaging-2023-07-19/StartDICOMImportJob.md "../../../goto/boto3/medical-imaging-2023-07-19/StartDICOMImportJob.md")
  in _AWS SDK for Python (Boto3) API Reference_.

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/medical-imaging#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/medical-imaging#code-examples").

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
