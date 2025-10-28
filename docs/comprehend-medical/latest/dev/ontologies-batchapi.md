# Ontology linking batch analysis

Use Amazon Comprehend Medical to detect entities in clinical text stored in an Amazon Simple Storage Service (Amazon S3) bucket and to link those entities to standardized ontologies. You can use ontology linking batch analysis to analyze either a collection of documents or a single document with up to 20,000 characters. By using either the console or the ontology linking batch API operations, you can perform operations to start, stop, list, and describe ongoing batch analysis jobs.

For pricing information for batch analysis and other Amazon Comprehend Medical operations, see [Amazon Comprehend Medical Pricing](https://aws.amazon.com/comprehend/medical/pricing/ "https://aws.amazon.com/comprehend/medical/pricing/").

## Performing batch

analysis

You can run a batch analysis job using either the Amazon Comprehend Medical console or the Amazon Comprehend Medical batch API operations.

### Performing batch analysis using the API operations

**Prerequisites**

When you are using the Amazon Comprehend Medical API, create an AWS Identity Access and
Management (IAM) policy and attach it to an IAM role. To learn more about
IAM roles and trust policies, see [IAM Policies and
Permissions](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md").

1. Upload your data into an S3 bucket.
2. To start a new analysis job, use the **StartICD10CMInferenceJob**, **StartSNOMEDCTInferenceJob**, or the **StartRxNormInferenceJob** operations. Provide the name of the Amazon S3 bucket that contains the input files and the name of the Amazon S3 bucket where you want to send the output files.
3. Monitor the progress of the job by using **DescribeICD10CMInferenceJob**, **DescribeSNOMEDCTInferenceJob**, or **DescribeRxNormInferenceJob** operations. Additionally, you can use **ListICD10CMInferenceJobs**, **ListSNOMEDCTInferenceJobs**, and **ListRxNormInferenceJobs** to see the status of all ontology linking batch analysis jobs.
4. If you need to stop a job in progress, use
   **StopICD10CMInferenceJob**,
   **StopSNOMEDCTInferenceJob**, or
   **StopRxNormInferenceJob** to stop analysis.
5. To view the results of your analysis job, see the output S3 bucket that you configured when you started the job.

### Performing batch analysis

using the console

######

1. Upload your data into an S3 bucket.
2. To start a new analysis job, select the type of analysis you will be performing. Then, provide the name of the S3 bucket that contains the input files and the name of the S3 bucket where you want to send the output files.
3. Monitor the status of your job while it is ongoing. From the console,
   you are can view all batch analysis operations and their status,
   including when analysis was started and ended.
4. To see the results of your analysis job, see the output S3 bucket that
   you configured when you started the job.

## IAM policies for batch

operations

The IAM role that calls the Amazon Comprehend Medical batch API operations must have a policy that grants access to the S3 buckets that contain the input and output files. The IAM role must also be assigned a trust relationship so that the Amazon Comprehend Medical service can assume the role. To learn more about IAM roles and trust policies, see [IAM Roles](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md").

The role must have the following policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "s3:GetObject"
 ],
 "Resource": [
 "arn:aws:s3:::`input-bucket`/*"
 ],
 "Effect": "Allow"
 },
 {
 "Action": [
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::`input-bucket`",
 "arn:aws:s3:::`output-bucket`"
 ],
 "Effect": "Allow"
 },
 {
 "Action": [
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::`output-bucket`/*"
 ],
 "Effect": "Allow"
 }
 ]
}`

```

The role must have the following trust relationship. It is recommended that you use the `aws:SourceAccount` and `aws:SourceArn` condition keys to prevent the confused deputy security issue. To learn more about the confused deputy problem and how to protect your AWS account, see [The confused deputy problem](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md") in the IAM documentation.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":{
 "Service":[
 "comprehendmedical.amazonaws.com"
 ]
 },
 "Action":"sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "account_id"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:comprehendmedical:region:account_id:*"
 }
 }
 }
 ]
}`

```

## Batch analysis output files

Amazon Comprehend Medical creates one output file for each input file in the batch. The file has the extension `.out`. Amazon Comprehend Medical first creates a directory in the output S3 bucket using the `AwsAccountId`-`JobType`-`JobId` as the name, and then it writes all of the output files for the batch to this directory. Amazon Comprehend Medical creates this new directory so that output from one job doesn't overwrite the output of another job.

A batch operation produces the same output as a synchronous operation.

Each batch operation produces the following three manifest files that contain information about the job:

- `Manifest` – Summarizes the job. Provides information
  about the parameters used for the job, the total size of the job, and the
  number of files processed.
- `Success` – Provides information about the files that
  were successfully processed. Includes the input and output file name and the
  size of the input file.
- `Unprocessed` – Lists files that the batch job did not
  process with error codes and error messages per file.

Amazon Comprehend Medical writes the files to the output directory that you specified for the batch job.
The summary manifest file will be written to the output folder, along with a folder titled
`Manifest_AccountId-Operation-JobId`. Within the manifest folder is the `success`
folder, which contains the success manifest, and the `failed` folder, which contains the
unprocessed file manifest. The following sections show the structure of the manifest files.

### Batch manifest file

The following is the JSON structure of the batch manifest file.

```
{"Summary" :
    {"Status" : "COMPLETED | FAILED | PARTIAL_SUCCESS | STOPPED",
    "JobType" : "ICD10CMInference | RxNormInference | SNOMEDCTInference",
    "InputDataConfiguration" : {
        "Bucket" : "input bucket",
        "Path" : "path to files/account ID-job type-job ID"
    }, "OutputDataConfiguration" : {
        "Bucket" : "output bucket",
        "Path" : "path to files"
    },
    "InputFileCount" : number of files in input bucket,
    "TotalMeteredCharacters" : total characters processed from all files,
    "UnprocessedFilesCount" : number of files not processed,
    "SuccessFilesCount" : total number of files processed,
    "TotalDurationSeconds" : time required for processing,
    "SuccessfulFilesListLocation" : "path to file",
    "UnprocessedFilesListLocation" : "path to file",
    "FailedJobErrorMessage": "error message or if not applicable,
              The status of the job is completed"
    }
}

```

### Success manifest file

The following is the JSON structure of the file that contains information
about successfully processed files.

```
{
    "Files": [{
            "Input": "`input path`/`input file name`",
            "Output": "`output path`/`output file name`",
            "InputSize": `size in bytes of input file`
        },
        {
            "Input": "`input path`/`input file name`",
            "Output": "`output path`/`output file name`",
            "InputSize": `size in bytes of input file`
     }]
}
```

### Unprocessed manifest

file

Following is the JSON structure of the manifest file that contains
information about unprocessed files.

```
{
  "Files" : [ {
      "Input": "file_name_that_failed",
      "ErrorCode": "error code for exception",
      "ErrorMessage": "explanation of the error code and suggestions"
  },
  { ...}
  ]
}

```
