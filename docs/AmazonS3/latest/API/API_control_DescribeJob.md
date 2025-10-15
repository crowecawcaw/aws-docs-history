# DescribeJob

Retrieves the configuration parameters and status for a Batch Operations job. For more
 information, see [S3 Batch Operations](../userguide/batch-ops.md "../userguide/batch-ops.md") in the *Amazon S3 User Guide*.



Permissions

To use the `DescribeJob` operation, you must have permission to
 perform the `s3:DescribeJob` action.



Related actions include:


* [CreateJob](API_control_CreateJob.md "API_control_CreateJob.md")
* [ListJobs](API_control_ListJobs.md "API_control_ListJobs.md")
* [UpdateJobPriority](API_control_UpdateJobPriority.md "API_control_UpdateJobPriority.md")
* [UpdateJobStatus](API_control_UpdateJobStatus.md "API_control_UpdateJobStatus.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
GET /v20180820/jobs/`id` HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: `AccountId`

```

## URI Request Parameters


The request uses the following URI parameters.





**[id](#API_control_DescribeJob_RequestSyntax "#API_control_DescribeJob_RequestSyntax")**


The ID for the job whose information you want to retrieve.


Length Constraints: Minimum length of 5. Maximum length of 36.


Pattern: `[a-zA-Z0-9\-\_]+`



Required: Yes




**[x-amz-account-id](#API_control_DescribeJob_RequestSyntax "#API_control_DescribeJob_RequestSyntax")**


The AWS account ID associated with the S3 Batch Operations job.


Length Constraints: Maximum length of 64.


Pattern: `^\d{12}$`



Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<[DescribeJobResult](#AmazonS3-control_DescribeJob-response-DescribeJobResult "#AmazonS3-control_DescribeJob-response-DescribeJobResult")>
   <[Job](#AmazonS3-control_DescribeJob-response-Job "#AmazonS3-control_DescribeJob-response-Job")>
      <[ConfirmationRequired](API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-ConfirmationRequired "API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-ConfirmationRequired")>***boolean***</[ConfirmationRequired](API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-ConfirmationRequired "API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-ConfirmationRequired")>
      <[CreationTime](API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-CreationTime "API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-CreationTime")>***timestamp***</[CreationTime](API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-CreationTime "API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-CreationTime")>
      <[Description](API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-Description "API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-Description")>***string***</[Description](API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-Description "API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-Description")>
      <[FailureReasons](API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-FailureReasons "API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-FailureReasons")>
         <JobFailure>
            <[FailureCode](API_control_JobFailure.md#AmazonS3-Type-control_JobFailure-FailureCode "API_control_JobFailure.md#AmazonS3-Type-control_JobFailure-FailureCode")>***string***</[FailureCode](API_control_JobFailure.md#AmazonS3-Type-control_JobFailure-FailureCode "API_control_JobFailure.md#AmazonS3-Type-control_JobFailure-FailureCode")>
            <[FailureReason](API_control_JobFailure.md#AmazonS3-Type-control_JobFailure-FailureReason "API_control_JobFailure.md#AmazonS3-Type-control_JobFailure-FailureReason")>***string***</[FailureReason](API_control_JobFailure.md#AmazonS3-Type-control_JobFailure-FailureReason "API_control_JobFailure.md#AmazonS3-Type-control_JobFailure-FailureReason")>
         </JobFailure>
      </[FailureReasons](API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-FailureReasons "API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-FailureReasons")>
      <[GeneratedManifestDescriptor](API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-GeneratedManifestDescriptor "API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-GeneratedManifestDescriptor")>
         <[Format](API_control_S3GeneratedManifestDescriptor.md#AmazonS3-Type-control_S3GeneratedManifestDescriptor-Format "API_control_S3GeneratedManifestDescriptor.md#AmazonS3-Type-control_S3GeneratedManifestDescriptor-Format")>***string***</[Format](API_control_S3GeneratedManifestDescriptor.md#AmazonS3-Type-control_S3GeneratedManifestDescriptor-Format "API_control_S3GeneratedManifestDescriptor.md#AmazonS3-Type-control_S3GeneratedManifestDescriptor-Format")>
         <[Location](API_control_S3GeneratedManifestDescriptor.md#AmazonS3-Type-control_S3GeneratedManifestDescriptor-Location "API_control_S3GeneratedManifestDescriptor.md#AmazonS3-Type-control_S3GeneratedManifestDescriptor-Location")>
            <[ETag](API_control_JobManifestLocation.md#AmazonS3-Type-control_JobManifestLocation-ETag "API_control_JobManifestLocation.md#AmazonS3-Type-control_JobManifestLocation-ETag")>***string***</[ETag](API_control_JobManifestLocation.md#AmazonS3-Type-control_JobManifestLocation-ETag "API_control_JobManifestLocation.md#AmazonS3-Type-control_JobManifestLocation-ETag")>
            <[ObjectArn](API_control_JobManifestLocation.md#AmazonS3-Type-control_JobManifestLocation-ObjectArn "API_control_JobManifestLocation.md#AmazonS3-Type-control_JobManifestLocation-ObjectArn")>***string***</[ObjectArn](API_control_JobManifestLocation.md#AmazonS3-Type-control_JobManifestLocation-ObjectArn "API_control_JobManifestLocation.md#AmazonS3-Type-control_JobManifestLocation-ObjectArn")>
            <[ObjectVersionId](API_control_JobManifestLocation.md#AmazonS3-Type-control_JobManifestLocation-ObjectVersionId "API_control_JobManifestLocation.md#AmazonS3-Type-control_JobManifestLocation-ObjectVersionId")>***string***</[ObjectVersionId](API_control_JobManifestLocation.md#AmazonS3-Type-control_JobManifestLocation-ObjectVersionId "API_control_JobManifestLocation.md#AmazonS3-Type-control_JobManifestLocation-ObjectVersionId")>
         </[Location](API_control_S3GeneratedManifestDescriptor.md#AmazonS3-Type-control_S3GeneratedManifestDescriptor-Location "API_control_S3GeneratedManifestDescriptor.md#AmazonS3-Type-control_S3GeneratedManifestDescriptor-Location")>
      </[GeneratedManifestDescriptor](API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-GeneratedManifestDescriptor "API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-GeneratedManifestDescriptor")>
      <[JobArn](API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-JobArn "API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-JobArn")>***string***</[JobArn](API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-JobArn "API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-JobArn")>
      <[JobId](API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-JobId "API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-JobId")>***string***</[JobId](API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-JobId "API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-JobId")>
      <[Manifest](API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-Manifest "API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-Manifest")>
         <[Location](API_control_JobManifest.md#AmazonS3-Type-control_JobManifest-Location "API_control_JobManifest.md#AmazonS3-Type-control_JobManifest-Location")>
            <[ETag](API_control_JobManifestLocation.md#AmazonS3-Type-control_JobManifestLocation-ETag "API_control_JobManifestLocation.md#AmazonS3-Type-control_JobManifestLocation-ETag")>***string***</[ETag](API_control_JobManifestLocation.md#AmazonS3-Type-control_JobManifestLocation-ETag "API_control_JobManifestLocation.md#AmazonS3-Type-control_JobManifestLocation-ETag")>
            <[ObjectArn](API_control_JobManifestLocation.md#AmazonS3-Type-control_JobManifestLocation-ObjectArn "API_control_JobManifestLocation.md#AmazonS3-Type-control_JobManifestLocation-ObjectArn")>***string***</[ObjectArn](API_control_JobManifestLocation.md#AmazonS3-Type-control_JobManifestLocation-ObjectArn "API_control_JobManifestLocation.md#AmazonS3-Type-control_JobManifestLocation-ObjectArn")>
            <[ObjectVersionId](API_control_JobManifestLocation.md#AmazonS3-Type-control_JobManifestLocation-ObjectVersionId "API_control_JobManifestLocation.md#AmazonS3-Type-control_JobManifestLocation-ObjectVersionId")>***string***</[ObjectVersionId](API_control_JobManifestLocation.md#AmazonS3-Type-control_JobManifestLocation-ObjectVersionId "API_control_JobManifestLocation.md#AmazonS3-Type-control_JobManifestLocation-ObjectVersionId")>
         </[Location](API_control_JobManifest.md#AmazonS3-Type-control_JobManifest-Location "API_control_JobManifest.md#AmazonS3-Type-control_JobManifest-Location")>
         <[Spec](API_control_JobManifest.md#AmazonS3-Type-control_JobManifest-Spec "API_control_JobManifest.md#AmazonS3-Type-control_JobManifest-Spec")>
            <[Fields](API_control_JobManifestSpec.md#AmazonS3-Type-control_JobManifestSpec-Fields "API_control_JobManifestSpec.md#AmazonS3-Type-control_JobManifestSpec-Fields")>
               <member>***string***</member>
            </[Fields](API_control_JobManifestSpec.md#AmazonS3-Type-control_JobManifestSpec-Fields "API_control_JobManifestSpec.md#AmazonS3-Type-control_JobManifestSpec-Fields")>
            <[Format](API_control_JobManifestSpec.md#AmazonS3-Type-control_JobManifestSpec-Format "API_control_JobManifestSpec.md#AmazonS3-Type-control_JobManifestSpec-Format")>***string***</[Format](API_control_JobManifestSpec.md#AmazonS3-Type-control_JobManifestSpec-Format "API_control_JobManifestSpec.md#AmazonS3-Type-control_JobManifestSpec-Format")>
         </[Spec](API_control_JobManifest.md#AmazonS3-Type-control_JobManifest-Spec "API_control_JobManifest.md#AmazonS3-Type-control_JobManifest-Spec")>
      </[Manifest](API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-Manifest "API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-Manifest")>
      <[ManifestGenerator](API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-ManifestGenerator "API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-ManifestGenerator")>
         <[S3JobManifestGenerator](API_control_JobManifestGenerator.md#AmazonS3-Type-control_JobManifestGenerator-S3JobManifestGenerator "API_control_JobManifestGenerator.md#AmazonS3-Type-control_JobManifestGenerator-S3JobManifestGenerator")>
            <[EnableManifestOutput](API_control_S3JobManifestGenerator.md#AmazonS3-Type-control_S3JobManifestGenerator-EnableManifestOutput "API_control_S3JobManifestGenerator.md#AmazonS3-Type-control_S3JobManifestGenerator-EnableManifestOutput")>***boolean***</[EnableManifestOutput](API_control_S3JobManifestGenerator.md#AmazonS3-Type-control_S3JobManifestGenerator-EnableManifestOutput "API_control_S3JobManifestGenerator.md#AmazonS3-Type-control_S3JobManifestGenerator-EnableManifestOutput")>
            <[ExpectedBucketOwner](API_control_S3JobManifestGenerator.md#AmazonS3-Type-control_S3JobManifestGenerator-ExpectedBucketOwner "API_control_S3JobManifestGenerator.md#AmazonS3-Type-control_S3JobManifestGenerator-ExpectedBucketOwner")>***string***</[ExpectedBucketOwner](API_control_S3JobManifestGenerator.md#AmazonS3-Type-control_S3JobManifestGenerator-ExpectedBucketOwner "API_control_S3JobManifestGenerator.md#AmazonS3-Type-control_S3JobManifestGenerator-ExpectedBucketOwner")>
            <[Filter](API_control_S3JobManifestGenerator.md#AmazonS3-Type-control_S3JobManifestGenerator-Filter "API_control_S3JobManifestGenerator.md#AmazonS3-Type-control_S3JobManifestGenerator-Filter")>
               <[CreatedAfter](API_control_JobManifestGeneratorFilter.md#AmazonS3-Type-control_JobManifestGeneratorFilter-CreatedAfter "API_control_JobManifestGeneratorFilter.md#AmazonS3-Type-control_JobManifestGeneratorFilter-CreatedAfter")>***timestamp***</[CreatedAfter](API_control_JobManifestGeneratorFilter.md#AmazonS3-Type-control_JobManifestGeneratorFilter-CreatedAfter "API_control_JobManifestGeneratorFilter.md#AmazonS3-Type-control_JobManifestGeneratorFilter-CreatedAfter")>
               <[CreatedBefore](API_control_JobManifestGeneratorFilter.md#AmazonS3-Type-control_JobManifestGeneratorFilter-CreatedBefore "API_control_JobManifestGeneratorFilter.md#AmazonS3-Type-control_JobManifestGeneratorFilter-CreatedBefore")>***timestamp***</[CreatedBefore](API_control_JobManifestGeneratorFilter.md#AmazonS3-Type-control_JobManifestGeneratorFilter-CreatedBefore "API_control_JobManifestGeneratorFilter.md#AmazonS3-Type-control_JobManifestGeneratorFilter-CreatedBefore")>
               <[EligibleForReplication](API_control_JobManifestGeneratorFilter.md#AmazonS3-Type-control_JobManifestGeneratorFilter-EligibleForReplication "API_control_JobManifestGeneratorFilter.md#AmazonS3-Type-control_JobManifestGeneratorFilter-EligibleForReplication")>***boolean***</[EligibleForReplication](API_control_JobManifestGeneratorFilter.md#AmazonS3-Type-control_JobManifestGeneratorFilter-EligibleForReplication "API_control_JobManifestGeneratorFilter.md#AmazonS3-Type-control_JobManifestGeneratorFilter-EligibleForReplication")>
               <[KeyNameConstraint](API_control_JobManifestGeneratorFilter.md#AmazonS3-Type-control_JobManifestGeneratorFilter-KeyNameConstraint "API_control_JobManifestGeneratorFilter.md#AmazonS3-Type-control_JobManifestGeneratorFilter-KeyNameConstraint")>
                  <[MatchAnyPrefix](API_control_KeyNameConstraint.md#AmazonS3-Type-control_KeyNameConstraint-MatchAnyPrefix "API_control_KeyNameConstraint.md#AmazonS3-Type-control_KeyNameConstraint-MatchAnyPrefix")>
                     <member>***string***</member>
                  </[MatchAnyPrefix](API_control_KeyNameConstraint.md#AmazonS3-Type-control_KeyNameConstraint-MatchAnyPrefix "API_control_KeyNameConstraint.md#AmazonS3-Type-control_KeyNameConstraint-MatchAnyPrefix")>
                  <[MatchAnySubstring](API_control_KeyNameConstraint.md#AmazonS3-Type-control_KeyNameConstraint-MatchAnySubstring "API_control_KeyNameConstraint.md#AmazonS3-Type-control_KeyNameConstraint-MatchAnySubstring")>
                     <member>***string***</member>
                  </[MatchAnySubstring](API_control_KeyNameConstraint.md#AmazonS3-Type-control_KeyNameConstraint-MatchAnySubstring "API_control_KeyNameConstraint.md#AmazonS3-Type-control_KeyNameConstraint-MatchAnySubstring")>
                  <[MatchAnySuffix](API_control_KeyNameConstraint.md#AmazonS3-Type-control_KeyNameConstraint-MatchAnySuffix "API_control_KeyNameConstraint.md#AmazonS3-Type-control_KeyNameConstraint-MatchAnySuffix")>
                     <member>***string***</member>
                  </[MatchAnySuffix](API_control_KeyNameConstraint.md#AmazonS3-Type-control_KeyNameConstraint-MatchAnySuffix "API_control_KeyNameConstraint.md#AmazonS3-Type-control_KeyNameConstraint-MatchAnySuffix")>
               </[KeyNameConstraint](API_control_JobManifestGeneratorFilter.md#AmazonS3-Type-control_JobManifestGeneratorFilter-KeyNameConstraint "API_control_JobManifestGeneratorFilter.md#AmazonS3-Type-control_JobManifestGeneratorFilter-KeyNameConstraint")>
               <[MatchAnyObjectEncryption](API_control_JobManifestGeneratorFilter.md#AmazonS3-Type-control_JobManifestGeneratorFilter-MatchAnyObjectEncryption "API_control_JobManifestGeneratorFilter.md#AmazonS3-Type-control_JobManifestGeneratorFilter-MatchAnyObjectEncryption")>
                  <ObjectEncryption>
                     <[DSSE-KMS](API_control_ObjectEncryptionFilter.md#AmazonS3-Type-control_ObjectEncryptionFilter-DSSEKMS "API_control_ObjectEncryptionFilter.md#AmazonS3-Type-control_ObjectEncryptionFilter-DSSEKMS")>
                        <[KmsKeyArn](API_control_DSSEKMSFilter.md#AmazonS3-Type-control_DSSEKMSFilter-KmsKeyArn "API_control_DSSEKMSFilter.md#AmazonS3-Type-control_DSSEKMSFilter-KmsKeyArn")>***string***</[KmsKeyArn](API_control_DSSEKMSFilter.md#AmazonS3-Type-control_DSSEKMSFilter-KmsKeyArn "API_control_DSSEKMSFilter.md#AmazonS3-Type-control_DSSEKMSFilter-KmsKeyArn")>
                     </[DSSE-KMS](API_control_ObjectEncryptionFilter.md#AmazonS3-Type-control_ObjectEncryptionFilter-DSSEKMS "API_control_ObjectEncryptionFilter.md#AmazonS3-Type-control_ObjectEncryptionFilter-DSSEKMS")>
                     <[NOT-SSE](API_control_ObjectEncryptionFilter.md#AmazonS3-Type-control_ObjectEncryptionFilter-NOTSSE "API_control_ObjectEncryptionFilter.md#AmazonS3-Type-control_ObjectEncryptionFilter-NOTSSE")>
                     </[NOT-SSE](API_control_ObjectEncryptionFilter.md#AmazonS3-Type-control_ObjectEncryptionFilter-NOTSSE "API_control_ObjectEncryptionFilter.md#AmazonS3-Type-control_ObjectEncryptionFilter-NOTSSE")>
                     <[SSE-C](API_control_ObjectEncryptionFilter.md#AmazonS3-Type-control_ObjectEncryptionFilter-SSEC "API_control_ObjectEncryptionFilter.md#AmazonS3-Type-control_ObjectEncryptionFilter-SSEC")>
                     </[SSE-C](API_control_ObjectEncryptionFilter.md#AmazonS3-Type-control_ObjectEncryptionFilter-SSEC "API_control_ObjectEncryptionFilter.md#AmazonS3-Type-control_ObjectEncryptionFilter-SSEC")>
                     <[SSE-KMS](API_control_ObjectEncryptionFilter.md#AmazonS3-Type-control_ObjectEncryptionFilter-SSEKMS "API_control_ObjectEncryptionFilter.md#AmazonS3-Type-control_ObjectEncryptionFilter-SSEKMS")>
                        <[BucketKeyEnabled](API_control_SSEKMSFilter.md#AmazonS3-Type-control_SSEKMSFilter-BucketKeyEnabled "API_control_SSEKMSFilter.md#AmazonS3-Type-control_SSEKMSFilter-BucketKeyEnabled")>***boolean***</[BucketKeyEnabled](API_control_SSEKMSFilter.md#AmazonS3-Type-control_SSEKMSFilter-BucketKeyEnabled "API_control_SSEKMSFilter.md#AmazonS3-Type-control_SSEKMSFilter-BucketKeyEnabled")>
                        <[KmsKeyArn](API_control_SSEKMSFilter.md#AmazonS3-Type-control_SSEKMSFilter-KmsKeyArn "API_control_SSEKMSFilter.md#AmazonS3-Type-control_SSEKMSFilter-KmsKeyArn")>***string***</[KmsKeyArn](API_control_SSEKMSFilter.md#AmazonS3-Type-control_SSEKMSFilter-KmsKeyArn "API_control_SSEKMSFilter.md#AmazonS3-Type-control_SSEKMSFilter-KmsKeyArn")>
                     </[SSE-KMS](API_control_ObjectEncryptionFilter.md#AmazonS3-Type-control_ObjectEncryptionFilter-SSEKMS "API_control_ObjectEncryptionFilter.md#AmazonS3-Type-control_ObjectEncryptionFilter-SSEKMS")>
                     <[SSE-S3](API_control_ObjectEncryptionFilter.md#AmazonS3-Type-control_ObjectEncryptionFilter-SSES3 "API_control_ObjectEncryptionFilter.md#AmazonS3-Type-control_ObjectEncryptionFilter-SSES3")>
                     </[SSE-S3](API_control_ObjectEncryptionFilter.md#AmazonS3-Type-control_ObjectEncryptionFilter-SSES3 "API_control_ObjectEncryptionFilter.md#AmazonS3-Type-control_ObjectEncryptionFilter-SSES3")>
                  </ObjectEncryption>
               </[MatchAnyObjectEncryption](API_control_JobManifestGeneratorFilter.md#AmazonS3-Type-control_JobManifestGeneratorFilter-MatchAnyObjectEncryption "API_control_JobManifestGeneratorFilter.md#AmazonS3-Type-control_JobManifestGeneratorFilter-MatchAnyObjectEncryption")>
               <[MatchAnyStorageClass](API_control_JobManifestGeneratorFilter.md#AmazonS3-Type-control_JobManifestGeneratorFilter-MatchAnyStorageClass "API_control_JobManifestGeneratorFilter.md#AmazonS3-Type-control_JobManifestGeneratorFilter-MatchAnyStorageClass")>
                  <member>***string***</member>
               </[MatchAnyStorageClass](API_control_JobManifestGeneratorFilter.md#AmazonS3-Type-control_JobManifestGeneratorFilter-MatchAnyStorageClass "API_control_JobManifestGeneratorFilter.md#AmazonS3-Type-control_JobManifestGeneratorFilter-MatchAnyStorageClass")>
               <[ObjectReplicationStatuses](API_control_JobManifestGeneratorFilter.md#AmazonS3-Type-control_JobManifestGeneratorFilter-ObjectReplicationStatuses "API_control_JobManifestGeneratorFilter.md#AmazonS3-Type-control_JobManifestGeneratorFilter-ObjectReplicationStatuses")>
                  <member>***string***</member>
               </[ObjectReplicationStatuses](API_control_JobManifestGeneratorFilter.md#AmazonS3-Type-control_JobManifestGeneratorFilter-ObjectReplicationStatuses "API_control_JobManifestGeneratorFilter.md#AmazonS3-Type-control_JobManifestGeneratorFilter-ObjectReplicationStatuses")>
               <[ObjectSizeGreaterThanBytes](API_control_JobManifestGeneratorFilter.md#AmazonS3-Type-control_JobManifestGeneratorFilter-ObjectSizeGreaterThanBytes "API_control_JobManifestGeneratorFilter.md#AmazonS3-Type-control_JobManifestGeneratorFilter-ObjectSizeGreaterThanBytes")>***long***</[ObjectSizeGreaterThanBytes](API_control_JobManifestGeneratorFilter.md#AmazonS3-Type-control_JobManifestGeneratorFilter-ObjectSizeGreaterThanBytes "API_control_JobManifestGeneratorFilter.md#AmazonS3-Type-control_JobManifestGeneratorFilter-ObjectSizeGreaterThanBytes")>
               <[ObjectSizeLessThanBytes](API_control_JobManifestGeneratorFilter.md#AmazonS3-Type-control_JobManifestGeneratorFilter-ObjectSizeLessThanBytes "API_control_JobManifestGeneratorFilter.md#AmazonS3-Type-control_JobManifestGeneratorFilter-ObjectSizeLessThanBytes")>***long***</[ObjectSizeLessThanBytes](API_control_JobManifestGeneratorFilter.md#AmazonS3-Type-control_JobManifestGeneratorFilter-ObjectSizeLessThanBytes "API_control_JobManifestGeneratorFilter.md#AmazonS3-Type-control_JobManifestGeneratorFilter-ObjectSizeLessThanBytes")>
            </[Filter](API_control_S3JobManifestGenerator.md#AmazonS3-Type-control_S3JobManifestGenerator-Filter "API_control_S3JobManifestGenerator.md#AmazonS3-Type-control_S3JobManifestGenerator-Filter")>
            <[ManifestOutputLocation](API_control_S3JobManifestGenerator.md#AmazonS3-Type-control_S3JobManifestGenerator-ManifestOutputLocation "API_control_S3JobManifestGenerator.md#AmazonS3-Type-control_S3JobManifestGenerator-ManifestOutputLocation")>
               <[Bucket](API_control_S3ManifestOutputLocation.md#AmazonS3-Type-control_S3ManifestOutputLocation-Bucket "API_control_S3ManifestOutputLocation.md#AmazonS3-Type-control_S3ManifestOutputLocation-Bucket")>***string***</[Bucket](API_control_S3ManifestOutputLocation.md#AmazonS3-Type-control_S3ManifestOutputLocation-Bucket "API_control_S3ManifestOutputLocation.md#AmazonS3-Type-control_S3ManifestOutputLocation-Bucket")>
               <[ExpectedManifestBucketOwner](API_control_S3ManifestOutputLocation.md#AmazonS3-Type-control_S3ManifestOutputLocation-ExpectedManifestBucketOwner "API_control_S3ManifestOutputLocation.md#AmazonS3-Type-control_S3ManifestOutputLocation-ExpectedManifestBucketOwner")>***string***</[ExpectedManifestBucketOwner](API_control_S3ManifestOutputLocation.md#AmazonS3-Type-control_S3ManifestOutputLocation-ExpectedManifestBucketOwner "API_control_S3ManifestOutputLocation.md#AmazonS3-Type-control_S3ManifestOutputLocation-ExpectedManifestBucketOwner")>
               <[ManifestEncryption](API_control_S3ManifestOutputLocation.md#AmazonS3-Type-control_S3ManifestOutputLocation-ManifestEncryption "API_control_S3ManifestOutputLocation.md#AmazonS3-Type-control_S3ManifestOutputLocation-ManifestEncryption")>
                  <[SSE-KMS](API_control_GeneratedManifestEncryption.md#AmazonS3-Type-control_GeneratedManifestEncryption-SSEKMS "API_control_GeneratedManifestEncryption.md#AmazonS3-Type-control_GeneratedManifestEncryption-SSEKMS")>
                     <[KeyId](API_control_SSEKMSEncryption.md#AmazonS3-Type-control_SSEKMSEncryption-KeyId "API_control_SSEKMSEncryption.md#AmazonS3-Type-control_SSEKMSEncryption-KeyId")>***string***</[KeyId](API_control_SSEKMSEncryption.md#AmazonS3-Type-control_SSEKMSEncryption-KeyId "API_control_SSEKMSEncryption.md#AmazonS3-Type-control_SSEKMSEncryption-KeyId")>
                  </[SSE-KMS](API_control_GeneratedManifestEncryption.md#AmazonS3-Type-control_GeneratedManifestEncryption-SSEKMS "API_control_GeneratedManifestEncryption.md#AmazonS3-Type-control_GeneratedManifestEncryption-SSEKMS")>
                  <[SSE-S3](API_control_GeneratedManifestEncryption.md#AmazonS3-Type-control_GeneratedManifestEncryption-SSES3 "API_control_GeneratedManifestEncryption.md#AmazonS3-Type-control_GeneratedManifestEncryption-SSES3")>
                  </[SSE-S3](API_control_GeneratedManifestEncryption.md#AmazonS3-Type-control_GeneratedManifestEncryption-SSES3 "API_control_GeneratedManifestEncryption.md#AmazonS3-Type-control_GeneratedManifestEncryption-SSES3")>
               </[ManifestEncryption](API_control_S3ManifestOutputLocation.md#AmazonS3-Type-control_S3ManifestOutputLocation-ManifestEncryption "API_control_S3ManifestOutputLocation.md#AmazonS3-Type-control_S3ManifestOutputLocation-ManifestEncryption")>
               <[ManifestFormat](API_control_S3ManifestOutputLocation.md#AmazonS3-Type-control_S3ManifestOutputLocation-ManifestFormat "API_control_S3ManifestOutputLocation.md#AmazonS3-Type-control_S3ManifestOutputLocation-ManifestFormat")>***string***</[ManifestFormat](API_control_S3ManifestOutputLocation.md#AmazonS3-Type-control_S3ManifestOutputLocation-ManifestFormat "API_control_S3ManifestOutputLocation.md#AmazonS3-Type-control_S3ManifestOutputLocation-ManifestFormat")>
               <[ManifestPrefix](API_control_S3ManifestOutputLocation.md#AmazonS3-Type-control_S3ManifestOutputLocation-ManifestPrefix "API_control_S3ManifestOutputLocation.md#AmazonS3-Type-control_S3ManifestOutputLocation-ManifestPrefix")>***string***</[ManifestPrefix](API_control_S3ManifestOutputLocation.md#AmazonS3-Type-control_S3ManifestOutputLocation-ManifestPrefix "API_control_S3ManifestOutputLocation.md#AmazonS3-Type-control_S3ManifestOutputLocation-ManifestPrefix")>
            </[ManifestOutputLocation](API_control_S3JobManifestGenerator.md#AmazonS3-Type-control_S3JobManifestGenerator-ManifestOutputLocation "API_control_S3JobManifestGenerator.md#AmazonS3-Type-control_S3JobManifestGenerator-ManifestOutputLocation")>
            <[SourceBucket](API_control_S3JobManifestGenerator.md#AmazonS3-Type-control_S3JobManifestGenerator-SourceBucket "API_control_S3JobManifestGenerator.md#AmazonS3-Type-control_S3JobManifestGenerator-SourceBucket")>***string***</[SourceBucket](API_control_S3JobManifestGenerator.md#AmazonS3-Type-control_S3JobManifestGenerator-SourceBucket "API_control_S3JobManifestGenerator.md#AmazonS3-Type-control_S3JobManifestGenerator-SourceBucket")>
         </[S3JobManifestGenerator](API_control_JobManifestGenerator.md#AmazonS3-Type-control_JobManifestGenerator-S3JobManifestGenerator "API_control_JobManifestGenerator.md#AmazonS3-Type-control_JobManifestGenerator-S3JobManifestGenerator")>
      </[ManifestGenerator](API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-ManifestGenerator "API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-ManifestGenerator")>
      <[Operation](API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-Operation "API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-Operation")>
         <[LambdaInvoke](API_control_JobOperation.md#AmazonS3-Type-control_JobOperation-LambdaInvoke "API_control_JobOperation.md#AmazonS3-Type-control_JobOperation-LambdaInvoke")>
            <[FunctionArn](API_control_LambdaInvokeOperation.md#AmazonS3-Type-control_LambdaInvokeOperation-FunctionArn "API_control_LambdaInvokeOperation.md#AmazonS3-Type-control_LambdaInvokeOperation-FunctionArn")>***string***</[FunctionArn](API_control_LambdaInvokeOperation.md#AmazonS3-Type-control_LambdaInvokeOperation-FunctionArn "API_control_LambdaInvokeOperation.md#AmazonS3-Type-control_LambdaInvokeOperation-FunctionArn")>
            <[InvocationSchemaVersion](API_control_LambdaInvokeOperation.md#AmazonS3-Type-control_LambdaInvokeOperation-InvocationSchemaVersion "API_control_LambdaInvokeOperation.md#AmazonS3-Type-control_LambdaInvokeOperation-InvocationSchemaVersion")>***string***</[InvocationSchemaVersion](API_control_LambdaInvokeOperation.md#AmazonS3-Type-control_LambdaInvokeOperation-InvocationSchemaVersion "API_control_LambdaInvokeOperation.md#AmazonS3-Type-control_LambdaInvokeOperation-InvocationSchemaVersion")>
            <[UserArguments](API_control_LambdaInvokeOperation.md#AmazonS3-Type-control_LambdaInvokeOperation-UserArguments "API_control_LambdaInvokeOperation.md#AmazonS3-Type-control_LambdaInvokeOperation-UserArguments")>
               <entry>
                  <key>***string***</key>
                  <value>***string***</value>
               </entry>
            </[UserArguments](API_control_LambdaInvokeOperation.md#AmazonS3-Type-control_LambdaInvokeOperation-UserArguments "API_control_LambdaInvokeOperation.md#AmazonS3-Type-control_LambdaInvokeOperation-UserArguments")>
         </[LambdaInvoke](API_control_JobOperation.md#AmazonS3-Type-control_JobOperation-LambdaInvoke "API_control_JobOperation.md#AmazonS3-Type-control_JobOperation-LambdaInvoke")>
         <[S3ComputeObjectChecksum](API_control_JobOperation.md#AmazonS3-Type-control_JobOperation-S3ComputeObjectChecksum "API_control_JobOperation.md#AmazonS3-Type-control_JobOperation-S3ComputeObjectChecksum")>
            <[ChecksumAlgorithm](API_control_S3ComputeObjectChecksumOperation.md#AmazonS3-Type-control_S3ComputeObjectChecksumOperation-ChecksumAlgorithm "API_control_S3ComputeObjectChecksumOperation.md#AmazonS3-Type-control_S3ComputeObjectChecksumOperation-ChecksumAlgorithm")>***string***</[ChecksumAlgorithm](API_control_S3ComputeObjectChecksumOperation.md#AmazonS3-Type-control_S3ComputeObjectChecksumOperation-ChecksumAlgorithm "API_control_S3ComputeObjectChecksumOperation.md#AmazonS3-Type-control_S3ComputeObjectChecksumOperation-ChecksumAlgorithm")>
            <[ChecksumType](API_control_S3ComputeObjectChecksumOperation.md#AmazonS3-Type-control_S3ComputeObjectChecksumOperation-ChecksumType "API_control_S3ComputeObjectChecksumOperation.md#AmazonS3-Type-control_S3ComputeObjectChecksumOperation-ChecksumType")>***string***</[ChecksumType](API_control_S3ComputeObjectChecksumOperation.md#AmazonS3-Type-control_S3ComputeObjectChecksumOperation-ChecksumType "API_control_S3ComputeObjectChecksumOperation.md#AmazonS3-Type-control_S3ComputeObjectChecksumOperation-ChecksumType")>
         </[S3ComputeObjectChecksum](API_control_JobOperation.md#AmazonS3-Type-control_JobOperation-S3ComputeObjectChecksum "API_control_JobOperation.md#AmazonS3-Type-control_JobOperation-S3ComputeObjectChecksum")>
         <[S3DeleteObjectTagging](API_control_JobOperation.md#AmazonS3-Type-control_JobOperation-S3DeleteObjectTagging "API_control_JobOperation.md#AmazonS3-Type-control_JobOperation-S3DeleteObjectTagging")>
         </[S3DeleteObjectTagging](API_control_JobOperation.md#AmazonS3-Type-control_JobOperation-S3DeleteObjectTagging "API_control_JobOperation.md#AmazonS3-Type-control_JobOperation-S3DeleteObjectTagging")>
         <[S3InitiateRestoreObject](API_control_JobOperation.md#AmazonS3-Type-control_JobOperation-S3InitiateRestoreObject "API_control_JobOperation.md#AmazonS3-Type-control_JobOperation-S3InitiateRestoreObject")>
            <[ExpirationInDays](API_control_S3InitiateRestoreObjectOperation.md#AmazonS3-Type-control_S3InitiateRestoreObjectOperation-ExpirationInDays "API_control_S3InitiateRestoreObjectOperation.md#AmazonS3-Type-control_S3InitiateRestoreObjectOperation-ExpirationInDays")>***integer***</[ExpirationInDays](API_control_S3InitiateRestoreObjectOperation.md#AmazonS3-Type-control_S3InitiateRestoreObjectOperation-ExpirationInDays "API_control_S3InitiateRestoreObjectOperation.md#AmazonS3-Type-control_S3InitiateRestoreObjectOperation-ExpirationInDays")>
            <[GlacierJobTier](API_control_S3InitiateRestoreObjectOperation.md#AmazonS3-Type-control_S3InitiateRestoreObjectOperation-GlacierJobTier "API_control_S3InitiateRestoreObjectOperation.md#AmazonS3-Type-control_S3InitiateRestoreObjectOperation-GlacierJobTier")>***string***</[GlacierJobTier](API_control_S3InitiateRestoreObjectOperation.md#AmazonS3-Type-control_S3InitiateRestoreObjectOperation-GlacierJobTier "API_control_S3InitiateRestoreObjectOperation.md#AmazonS3-Type-control_S3InitiateRestoreObjectOperation-GlacierJobTier")>
         </[S3InitiateRestoreObject](API_control_JobOperation.md#AmazonS3-Type-control_JobOperation-S3InitiateRestoreObject "API_control_JobOperation.md#AmazonS3-Type-control_JobOperation-S3InitiateRestoreObject")>
         <[S3PutObjectAcl](API_control_JobOperation.md#AmazonS3-Type-control_JobOperation-S3PutObjectAcl "API_control_JobOperation.md#AmazonS3-Type-control_JobOperation-S3PutObjectAcl")>
            <[AccessControlPolicy](API_control_S3SetObjectAclOperation.md#AmazonS3-Type-control_S3SetObjectAclOperation-AccessControlPolicy "API_control_S3SetObjectAclOperation.md#AmazonS3-Type-control_S3SetObjectAclOperation-AccessControlPolicy")>
               <[AccessControlList](API_control_S3AccessControlPolicy.md#AmazonS3-Type-control_S3AccessControlPolicy-AccessControlList "API_control_S3AccessControlPolicy.md#AmazonS3-Type-control_S3AccessControlPolicy-AccessControlList")>
                  <[Grants](API_control_S3AccessControlList.md#AmazonS3-Type-control_S3AccessControlList-Grants "API_control_S3AccessControlList.md#AmazonS3-Type-control_S3AccessControlList-Grants")>
                     <S3Grant>
                        <[Grantee](API_control_S3Grant.md#AmazonS3-Type-control_S3Grant-Grantee "API_control_S3Grant.md#AmazonS3-Type-control_S3Grant-Grantee")>
                           <[DisplayName](API_control_S3Grantee.md#AmazonS3-Type-control_S3Grantee-DisplayName "API_control_S3Grantee.md#AmazonS3-Type-control_S3Grantee-DisplayName")>***string***</[DisplayName](API_control_S3Grantee.md#AmazonS3-Type-control_S3Grantee-DisplayName "API_control_S3Grantee.md#AmazonS3-Type-control_S3Grantee-DisplayName")>
                           <[Identifier](API_control_S3Grantee.md#AmazonS3-Type-control_S3Grantee-Identifier "API_control_S3Grantee.md#AmazonS3-Type-control_S3Grantee-Identifier")>***string***</[Identifier](API_control_S3Grantee.md#AmazonS3-Type-control_S3Grantee-Identifier "API_control_S3Grantee.md#AmazonS3-Type-control_S3Grantee-Identifier")>
                           <[TypeIdentifier](API_control_S3Grantee.md#AmazonS3-Type-control_S3Grantee-TypeIdentifier "API_control_S3Grantee.md#AmazonS3-Type-control_S3Grantee-TypeIdentifier")>***string***</[TypeIdentifier](API_control_S3Grantee.md#AmazonS3-Type-control_S3Grantee-TypeIdentifier "API_control_S3Grantee.md#AmazonS3-Type-control_S3Grantee-TypeIdentifier")>
                        </[Grantee](API_control_S3Grant.md#AmazonS3-Type-control_S3Grant-Grantee "API_control_S3Grant.md#AmazonS3-Type-control_S3Grant-Grantee")>
                        <[Permission](API_control_S3Grant.md#AmazonS3-Type-control_S3Grant-Permission "API_control_S3Grant.md#AmazonS3-Type-control_S3Grant-Permission")>***string***</[Permission](API_control_S3Grant.md#AmazonS3-Type-control_S3Grant-Permission "API_control_S3Grant.md#AmazonS3-Type-control_S3Grant-Permission")>
                     </S3Grant>
                  </[Grants](API_control_S3AccessControlList.md#AmazonS3-Type-control_S3AccessControlList-Grants "API_control_S3AccessControlList.md#AmazonS3-Type-control_S3AccessControlList-Grants")>
                  <[Owner](API_control_S3AccessControlList.md#AmazonS3-Type-control_S3AccessControlList-Owner "API_control_S3AccessControlList.md#AmazonS3-Type-control_S3AccessControlList-Owner")>
                     <[DisplayName](API_control_S3ObjectOwner.md#AmazonS3-Type-control_S3ObjectOwner-DisplayName "API_control_S3ObjectOwner.md#AmazonS3-Type-control_S3ObjectOwner-DisplayName")>***string***</[DisplayName](API_control_S3ObjectOwner.md#AmazonS3-Type-control_S3ObjectOwner-DisplayName "API_control_S3ObjectOwner.md#AmazonS3-Type-control_S3ObjectOwner-DisplayName")>
                     <[ID](API_control_S3ObjectOwner.md#AmazonS3-Type-control_S3ObjectOwner-ID "API_control_S3ObjectOwner.md#AmazonS3-Type-control_S3ObjectOwner-ID")>***string***</[ID](API_control_S3ObjectOwner.md#AmazonS3-Type-control_S3ObjectOwner-ID "API_control_S3ObjectOwner.md#AmazonS3-Type-control_S3ObjectOwner-ID")>
                  </[Owner](API_control_S3AccessControlList.md#AmazonS3-Type-control_S3AccessControlList-Owner "API_control_S3AccessControlList.md#AmazonS3-Type-control_S3AccessControlList-Owner")>
               </[AccessControlList](API_control_S3AccessControlPolicy.md#AmazonS3-Type-control_S3AccessControlPolicy-AccessControlList "API_control_S3AccessControlPolicy.md#AmazonS3-Type-control_S3AccessControlPolicy-AccessControlList")>
               <[CannedAccessControlList](API_control_S3AccessControlPolicy.md#AmazonS3-Type-control_S3AccessControlPolicy-CannedAccessControlList "API_control_S3AccessControlPolicy.md#AmazonS3-Type-control_S3AccessControlPolicy-CannedAccessControlList")>***string***</[CannedAccessControlList](API_control_S3AccessControlPolicy.md#AmazonS3-Type-control_S3AccessControlPolicy-CannedAccessControlList "API_control_S3AccessControlPolicy.md#AmazonS3-Type-control_S3AccessControlPolicy-CannedAccessControlList")>
            </[AccessControlPolicy](API_control_S3SetObjectAclOperation.md#AmazonS3-Type-control_S3SetObjectAclOperation-AccessControlPolicy "API_control_S3SetObjectAclOperation.md#AmazonS3-Type-control_S3SetObjectAclOperation-AccessControlPolicy")>
         </[S3PutObjectAcl](API_control_JobOperation.md#AmazonS3-Type-control_JobOperation-S3PutObjectAcl "API_control_JobOperation.md#AmazonS3-Type-control_JobOperation-S3PutObjectAcl")>
         <[S3PutObjectCopy](API_control_JobOperation.md#AmazonS3-Type-control_JobOperation-S3PutObjectCopy "API_control_JobOperation.md#AmazonS3-Type-control_JobOperation-S3PutObjectCopy")>
            <[AccessControlGrants](API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-AccessControlGrants "API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-AccessControlGrants")>
               <S3Grant>
                  <[Grantee](API_control_S3Grant.md#AmazonS3-Type-control_S3Grant-Grantee "API_control_S3Grant.md#AmazonS3-Type-control_S3Grant-Grantee")>
                     <[DisplayName](API_control_S3Grantee.md#AmazonS3-Type-control_S3Grantee-DisplayName "API_control_S3Grantee.md#AmazonS3-Type-control_S3Grantee-DisplayName")>***string***</[DisplayName](API_control_S3Grantee.md#AmazonS3-Type-control_S3Grantee-DisplayName "API_control_S3Grantee.md#AmazonS3-Type-control_S3Grantee-DisplayName")>
                     <[Identifier](API_control_S3Grantee.md#AmazonS3-Type-control_S3Grantee-Identifier "API_control_S3Grantee.md#AmazonS3-Type-control_S3Grantee-Identifier")>***string***</[Identifier](API_control_S3Grantee.md#AmazonS3-Type-control_S3Grantee-Identifier "API_control_S3Grantee.md#AmazonS3-Type-control_S3Grantee-Identifier")>
                     <[TypeIdentifier](API_control_S3Grantee.md#AmazonS3-Type-control_S3Grantee-TypeIdentifier "API_control_S3Grantee.md#AmazonS3-Type-control_S3Grantee-TypeIdentifier")>***string***</[TypeIdentifier](API_control_S3Grantee.md#AmazonS3-Type-control_S3Grantee-TypeIdentifier "API_control_S3Grantee.md#AmazonS3-Type-control_S3Grantee-TypeIdentifier")>
                  </[Grantee](API_control_S3Grant.md#AmazonS3-Type-control_S3Grant-Grantee "API_control_S3Grant.md#AmazonS3-Type-control_S3Grant-Grantee")>
                  <[Permission](API_control_S3Grant.md#AmazonS3-Type-control_S3Grant-Permission "API_control_S3Grant.md#AmazonS3-Type-control_S3Grant-Permission")>***string***</[Permission](API_control_S3Grant.md#AmazonS3-Type-control_S3Grant-Permission "API_control_S3Grant.md#AmazonS3-Type-control_S3Grant-Permission")>
               </S3Grant>
            </[AccessControlGrants](API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-AccessControlGrants "API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-AccessControlGrants")>
            <[BucketKeyEnabled](API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-BucketKeyEnabled "API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-BucketKeyEnabled")>***boolean***</[BucketKeyEnabled](API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-BucketKeyEnabled "API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-BucketKeyEnabled")>
            <[CannedAccessControlList](API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-CannedAccessControlList "API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-CannedAccessControlList")>***string***</[CannedAccessControlList](API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-CannedAccessControlList "API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-CannedAccessControlList")>
            <[ChecksumAlgorithm](API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-ChecksumAlgorithm "API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-ChecksumAlgorithm")>***string***</[ChecksumAlgorithm](API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-ChecksumAlgorithm "API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-ChecksumAlgorithm")>
            <[MetadataDirective](API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-MetadataDirective "API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-MetadataDirective")>***string***</[MetadataDirective](API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-MetadataDirective "API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-MetadataDirective")>
            <[ModifiedSinceConstraint](API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-ModifiedSinceConstraint "API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-ModifiedSinceConstraint")>***timestamp***</[ModifiedSinceConstraint](API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-ModifiedSinceConstraint "API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-ModifiedSinceConstraint")>
            <[NewObjectMetadata](API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-NewObjectMetadata "API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-NewObjectMetadata")>
               <[CacheControl](API_control_S3ObjectMetadata.md#AmazonS3-Type-control_S3ObjectMetadata-CacheControl "API_control_S3ObjectMetadata.md#AmazonS3-Type-control_S3ObjectMetadata-CacheControl")>***string***</[CacheControl](API_control_S3ObjectMetadata.md#AmazonS3-Type-control_S3ObjectMetadata-CacheControl "API_control_S3ObjectMetadata.md#AmazonS3-Type-control_S3ObjectMetadata-CacheControl")>
               <[ContentDisposition](API_control_S3ObjectMetadata.md#AmazonS3-Type-control_S3ObjectMetadata-ContentDisposition "API_control_S3ObjectMetadata.md#AmazonS3-Type-control_S3ObjectMetadata-ContentDisposition")>***string***</[ContentDisposition](API_control_S3ObjectMetadata.md#AmazonS3-Type-control_S3ObjectMetadata-ContentDisposition "API_control_S3ObjectMetadata.md#AmazonS3-Type-control_S3ObjectMetadata-ContentDisposition")>
               <[ContentEncoding](API_control_S3ObjectMetadata.md#AmazonS3-Type-control_S3ObjectMetadata-ContentEncoding "API_control_S3ObjectMetadata.md#AmazonS3-Type-control_S3ObjectMetadata-ContentEncoding")>***string***</[ContentEncoding](API_control_S3ObjectMetadata.md#AmazonS3-Type-control_S3ObjectMetadata-ContentEncoding "API_control_S3ObjectMetadata.md#AmazonS3-Type-control_S3ObjectMetadata-ContentEncoding")>
               <[ContentLanguage](API_control_S3ObjectMetadata.md#AmazonS3-Type-control_S3ObjectMetadata-ContentLanguage "API_control_S3ObjectMetadata.md#AmazonS3-Type-control_S3ObjectMetadata-ContentLanguage")>***string***</[ContentLanguage](API_control_S3ObjectMetadata.md#AmazonS3-Type-control_S3ObjectMetadata-ContentLanguage "API_control_S3ObjectMetadata.md#AmazonS3-Type-control_S3ObjectMetadata-ContentLanguage")>
               <[ContentLength](API_control_S3ObjectMetadata.md#AmazonS3-Type-control_S3ObjectMetadata-ContentLength "API_control_S3ObjectMetadata.md#AmazonS3-Type-control_S3ObjectMetadata-ContentLength")>***long***</[ContentLength](API_control_S3ObjectMetadata.md#AmazonS3-Type-control_S3ObjectMetadata-ContentLength "API_control_S3ObjectMetadata.md#AmazonS3-Type-control_S3ObjectMetadata-ContentLength")>
               <[ContentMD5](API_control_S3ObjectMetadata.md#AmazonS3-Type-control_S3ObjectMetadata-ContentMD5 "API_control_S3ObjectMetadata.md#AmazonS3-Type-control_S3ObjectMetadata-ContentMD5")>***string***</[ContentMD5](API_control_S3ObjectMetadata.md#AmazonS3-Type-control_S3ObjectMetadata-ContentMD5 "API_control_S3ObjectMetadata.md#AmazonS3-Type-control_S3ObjectMetadata-ContentMD5")>
               <[ContentType](API_control_S3ObjectMetadata.md#AmazonS3-Type-control_S3ObjectMetadata-ContentType "API_control_S3ObjectMetadata.md#AmazonS3-Type-control_S3ObjectMetadata-ContentType")>***string***</[ContentType](API_control_S3ObjectMetadata.md#AmazonS3-Type-control_S3ObjectMetadata-ContentType "API_control_S3ObjectMetadata.md#AmazonS3-Type-control_S3ObjectMetadata-ContentType")>
               <[HttpExpiresDate](API_control_S3ObjectMetadata.md#AmazonS3-Type-control_S3ObjectMetadata-HttpExpiresDate "API_control_S3ObjectMetadata.md#AmazonS3-Type-control_S3ObjectMetadata-HttpExpiresDate")>***timestamp***</[HttpExpiresDate](API_control_S3ObjectMetadata.md#AmazonS3-Type-control_S3ObjectMetadata-HttpExpiresDate "API_control_S3ObjectMetadata.md#AmazonS3-Type-control_S3ObjectMetadata-HttpExpiresDate")>
               <[RequesterCharged](API_control_S3ObjectMetadata.md#AmazonS3-Type-control_S3ObjectMetadata-RequesterCharged "API_control_S3ObjectMetadata.md#AmazonS3-Type-control_S3ObjectMetadata-RequesterCharged")>***boolean***</[RequesterCharged](API_control_S3ObjectMetadata.md#AmazonS3-Type-control_S3ObjectMetadata-RequesterCharged "API_control_S3ObjectMetadata.md#AmazonS3-Type-control_S3ObjectMetadata-RequesterCharged")>
               <[SSEAlgorithm](API_control_S3ObjectMetadata.md#AmazonS3-Type-control_S3ObjectMetadata-SSEAlgorithm "API_control_S3ObjectMetadata.md#AmazonS3-Type-control_S3ObjectMetadata-SSEAlgorithm")>***string***</[SSEAlgorithm](API_control_S3ObjectMetadata.md#AmazonS3-Type-control_S3ObjectMetadata-SSEAlgorithm "API_control_S3ObjectMetadata.md#AmazonS3-Type-control_S3ObjectMetadata-SSEAlgorithm")>
               <[UserMetadata](API_control_S3ObjectMetadata.md#AmazonS3-Type-control_S3ObjectMetadata-UserMetadata "API_control_S3ObjectMetadata.md#AmazonS3-Type-control_S3ObjectMetadata-UserMetadata")>
                  <entry>
                     <key>***string***</key>
                     <value>***string***</value>
                  </entry>
               </[UserMetadata](API_control_S3ObjectMetadata.md#AmazonS3-Type-control_S3ObjectMetadata-UserMetadata "API_control_S3ObjectMetadata.md#AmazonS3-Type-control_S3ObjectMetadata-UserMetadata")>
            </[NewObjectMetadata](API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-NewObjectMetadata "API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-NewObjectMetadata")>
            <[NewObjectTagging](API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-NewObjectTagging "API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-NewObjectTagging")>
               <S3Tag>
                  <[Key](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key")>***string***</[Key](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key")>
                  <[Value](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value")>***string***</[Value](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value")>
               </S3Tag>
            </[NewObjectTagging](API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-NewObjectTagging "API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-NewObjectTagging")>
            <[ObjectLockLegalHoldStatus](API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-ObjectLockLegalHoldStatus "API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-ObjectLockLegalHoldStatus")>***string***</[ObjectLockLegalHoldStatus](API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-ObjectLockLegalHoldStatus "API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-ObjectLockLegalHoldStatus")>
            <[ObjectLockMode](API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-ObjectLockMode "API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-ObjectLockMode")>***string***</[ObjectLockMode](API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-ObjectLockMode "API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-ObjectLockMode")>
            <[ObjectLockRetainUntilDate](API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-ObjectLockRetainUntilDate "API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-ObjectLockRetainUntilDate")>***timestamp***</[ObjectLockRetainUntilDate](API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-ObjectLockRetainUntilDate "API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-ObjectLockRetainUntilDate")>
            <[RedirectLocation](API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-RedirectLocation "API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-RedirectLocation")>***string***</[RedirectLocation](API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-RedirectLocation "API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-RedirectLocation")>
            <[RequesterPays](API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-RequesterPays "API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-RequesterPays")>***boolean***</[RequesterPays](API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-RequesterPays "API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-RequesterPays")>
            <[SSEAwsKmsKeyId](API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-SSEAwsKmsKeyId "API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-SSEAwsKmsKeyId")>***string***</[SSEAwsKmsKeyId](API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-SSEAwsKmsKeyId "API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-SSEAwsKmsKeyId")>
            <[StorageClass](API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-StorageClass "API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-StorageClass")>***string***</[StorageClass](API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-StorageClass "API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-StorageClass")>
            <[TargetKeyPrefix](API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-TargetKeyPrefix "API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-TargetKeyPrefix")>***string***</[TargetKeyPrefix](API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-TargetKeyPrefix "API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-TargetKeyPrefix")>
            <[TargetResource](API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-TargetResource "API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-TargetResource")>***string***</[TargetResource](API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-TargetResource "API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-TargetResource")>
            <[UnModifiedSinceConstraint](API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-UnModifiedSinceConstraint "API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-UnModifiedSinceConstraint")>***timestamp***</[UnModifiedSinceConstraint](API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-UnModifiedSinceConstraint "API_control_S3CopyObjectOperation.md#AmazonS3-Type-control_S3CopyObjectOperation-UnModifiedSinceConstraint")>
         </[S3PutObjectCopy](API_control_JobOperation.md#AmazonS3-Type-control_JobOperation-S3PutObjectCopy "API_control_JobOperation.md#AmazonS3-Type-control_JobOperation-S3PutObjectCopy")>
         <[S3PutObjectLegalHold](API_control_JobOperation.md#AmazonS3-Type-control_JobOperation-S3PutObjectLegalHold "API_control_JobOperation.md#AmazonS3-Type-control_JobOperation-S3PutObjectLegalHold")>
            <[LegalHold](API_control_S3SetObjectLegalHoldOperation.md#AmazonS3-Type-control_S3SetObjectLegalHoldOperation-LegalHold "API_control_S3SetObjectLegalHoldOperation.md#AmazonS3-Type-control_S3SetObjectLegalHoldOperation-LegalHold")>
               <[Status](API_control_S3ObjectLockLegalHold.md#AmazonS3-Type-control_S3ObjectLockLegalHold-Status "API_control_S3ObjectLockLegalHold.md#AmazonS3-Type-control_S3ObjectLockLegalHold-Status")>***string***</[Status](API_control_S3ObjectLockLegalHold.md#AmazonS3-Type-control_S3ObjectLockLegalHold-Status "API_control_S3ObjectLockLegalHold.md#AmazonS3-Type-control_S3ObjectLockLegalHold-Status")>
            </[LegalHold](API_control_S3SetObjectLegalHoldOperation.md#AmazonS3-Type-control_S3SetObjectLegalHoldOperation-LegalHold "API_control_S3SetObjectLegalHoldOperation.md#AmazonS3-Type-control_S3SetObjectLegalHoldOperation-LegalHold")>
         </[S3PutObjectLegalHold](API_control_JobOperation.md#AmazonS3-Type-control_JobOperation-S3PutObjectLegalHold "API_control_JobOperation.md#AmazonS3-Type-control_JobOperation-S3PutObjectLegalHold")>
         <[S3PutObjectRetention](API_control_JobOperation.md#AmazonS3-Type-control_JobOperation-S3PutObjectRetention "API_control_JobOperation.md#AmazonS3-Type-control_JobOperation-S3PutObjectRetention")>
            <[BypassGovernanceRetention](API_control_S3SetObjectRetentionOperation.md#AmazonS3-Type-control_S3SetObjectRetentionOperation-BypassGovernanceRetention "API_control_S3SetObjectRetentionOperation.md#AmazonS3-Type-control_S3SetObjectRetentionOperation-BypassGovernanceRetention")>***boolean***</[BypassGovernanceRetention](API_control_S3SetObjectRetentionOperation.md#AmazonS3-Type-control_S3SetObjectRetentionOperation-BypassGovernanceRetention "API_control_S3SetObjectRetentionOperation.md#AmazonS3-Type-control_S3SetObjectRetentionOperation-BypassGovernanceRetention")>
            <[Retention](API_control_S3SetObjectRetentionOperation.md#AmazonS3-Type-control_S3SetObjectRetentionOperation-Retention "API_control_S3SetObjectRetentionOperation.md#AmazonS3-Type-control_S3SetObjectRetentionOperation-Retention")>
               <[Mode](API_control_S3Retention.md#AmazonS3-Type-control_S3Retention-Mode "API_control_S3Retention.md#AmazonS3-Type-control_S3Retention-Mode")>***string***</[Mode](API_control_S3Retention.md#AmazonS3-Type-control_S3Retention-Mode "API_control_S3Retention.md#AmazonS3-Type-control_S3Retention-Mode")>
               <[RetainUntilDate](API_control_S3Retention.md#AmazonS3-Type-control_S3Retention-RetainUntilDate "API_control_S3Retention.md#AmazonS3-Type-control_S3Retention-RetainUntilDate")>***timestamp***</[RetainUntilDate](API_control_S3Retention.md#AmazonS3-Type-control_S3Retention-RetainUntilDate "API_control_S3Retention.md#AmazonS3-Type-control_S3Retention-RetainUntilDate")>
            </[Retention](API_control_S3SetObjectRetentionOperation.md#AmazonS3-Type-control_S3SetObjectRetentionOperation-Retention "API_control_S3SetObjectRetentionOperation.md#AmazonS3-Type-control_S3SetObjectRetentionOperation-Retention")>
         </[S3PutObjectRetention](API_control_JobOperation.md#AmazonS3-Type-control_JobOperation-S3PutObjectRetention "API_control_JobOperation.md#AmazonS3-Type-control_JobOperation-S3PutObjectRetention")>
         <[S3PutObjectTagging](API_control_JobOperation.md#AmazonS3-Type-control_JobOperation-S3PutObjectTagging "API_control_JobOperation.md#AmazonS3-Type-control_JobOperation-S3PutObjectTagging")>
            <[TagSet](API_control_S3SetObjectTaggingOperation.md#AmazonS3-Type-control_S3SetObjectTaggingOperation-TagSet "API_control_S3SetObjectTaggingOperation.md#AmazonS3-Type-control_S3SetObjectTaggingOperation-TagSet")>
               <S3Tag>
                  <[Key](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key")>***string***</[Key](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key")>
                  <[Value](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value")>***string***</[Value](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value")>
               </S3Tag>
            </[TagSet](API_control_S3SetObjectTaggingOperation.md#AmazonS3-Type-control_S3SetObjectTaggingOperation-TagSet "API_control_S3SetObjectTaggingOperation.md#AmazonS3-Type-control_S3SetObjectTaggingOperation-TagSet")>
         </[S3PutObjectTagging](API_control_JobOperation.md#AmazonS3-Type-control_JobOperation-S3PutObjectTagging "API_control_JobOperation.md#AmazonS3-Type-control_JobOperation-S3PutObjectTagging")>
         <[S3ReplicateObject](API_control_JobOperation.md#AmazonS3-Type-control_JobOperation-S3ReplicateObject "API_control_JobOperation.md#AmazonS3-Type-control_JobOperation-S3ReplicateObject")>
         </[S3ReplicateObject](API_control_JobOperation.md#AmazonS3-Type-control_JobOperation-S3ReplicateObject "API_control_JobOperation.md#AmazonS3-Type-control_JobOperation-S3ReplicateObject")>
      </[Operation](API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-Operation "API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-Operation")>
      <[Priority](API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-Priority "API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-Priority")>***integer***</[Priority](API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-Priority "API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-Priority")>
      <[ProgressSummary](API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-ProgressSummary "API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-ProgressSummary")>
         <[NumberOfTasksFailed](API_control_JobProgressSummary.md#AmazonS3-Type-control_JobProgressSummary-NumberOfTasksFailed "API_control_JobProgressSummary.md#AmazonS3-Type-control_JobProgressSummary-NumberOfTasksFailed")>***long***</[NumberOfTasksFailed](API_control_JobProgressSummary.md#AmazonS3-Type-control_JobProgressSummary-NumberOfTasksFailed "API_control_JobProgressSummary.md#AmazonS3-Type-control_JobProgressSummary-NumberOfTasksFailed")>
         <[NumberOfTasksSucceeded](API_control_JobProgressSummary.md#AmazonS3-Type-control_JobProgressSummary-NumberOfTasksSucceeded "API_control_JobProgressSummary.md#AmazonS3-Type-control_JobProgressSummary-NumberOfTasksSucceeded")>***long***</[NumberOfTasksSucceeded](API_control_JobProgressSummary.md#AmazonS3-Type-control_JobProgressSummary-NumberOfTasksSucceeded "API_control_JobProgressSummary.md#AmazonS3-Type-control_JobProgressSummary-NumberOfTasksSucceeded")>
         <[Timers](API_control_JobProgressSummary.md#AmazonS3-Type-control_JobProgressSummary-Timers "API_control_JobProgressSummary.md#AmazonS3-Type-control_JobProgressSummary-Timers")>
            <[ElapsedTimeInActiveSeconds](API_control_JobTimers.md#AmazonS3-Type-control_JobTimers-ElapsedTimeInActiveSeconds "API_control_JobTimers.md#AmazonS3-Type-control_JobTimers-ElapsedTimeInActiveSeconds")>***long***</[ElapsedTimeInActiveSeconds](API_control_JobTimers.md#AmazonS3-Type-control_JobTimers-ElapsedTimeInActiveSeconds "API_control_JobTimers.md#AmazonS3-Type-control_JobTimers-ElapsedTimeInActiveSeconds")>
         </[Timers](API_control_JobProgressSummary.md#AmazonS3-Type-control_JobProgressSummary-Timers "API_control_JobProgressSummary.md#AmazonS3-Type-control_JobProgressSummary-Timers")>
         <[TotalNumberOfTasks](API_control_JobProgressSummary.md#AmazonS3-Type-control_JobProgressSummary-TotalNumberOfTasks "API_control_JobProgressSummary.md#AmazonS3-Type-control_JobProgressSummary-TotalNumberOfTasks")>***long***</[TotalNumberOfTasks](API_control_JobProgressSummary.md#AmazonS3-Type-control_JobProgressSummary-TotalNumberOfTasks "API_control_JobProgressSummary.md#AmazonS3-Type-control_JobProgressSummary-TotalNumberOfTasks")>
      </[ProgressSummary](API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-ProgressSummary "API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-ProgressSummary")>
      <[Report](API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-Report "API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-Report")>
         <[Bucket](API_control_JobReport.md#AmazonS3-Type-control_JobReport-Bucket "API_control_JobReport.md#AmazonS3-Type-control_JobReport-Bucket")>***string***</[Bucket](API_control_JobReport.md#AmazonS3-Type-control_JobReport-Bucket "API_control_JobReport.md#AmazonS3-Type-control_JobReport-Bucket")>
         <[Enabled](API_control_JobReport.md#AmazonS3-Type-control_JobReport-Enabled "API_control_JobReport.md#AmazonS3-Type-control_JobReport-Enabled")>***boolean***</[Enabled](API_control_JobReport.md#AmazonS3-Type-control_JobReport-Enabled "API_control_JobReport.md#AmazonS3-Type-control_JobReport-Enabled")>
         <[ExpectedBucketOwner](API_control_JobReport.md#AmazonS3-Type-control_JobReport-ExpectedBucketOwner "API_control_JobReport.md#AmazonS3-Type-control_JobReport-ExpectedBucketOwner")>***string***</[ExpectedBucketOwner](API_control_JobReport.md#AmazonS3-Type-control_JobReport-ExpectedBucketOwner "API_control_JobReport.md#AmazonS3-Type-control_JobReport-ExpectedBucketOwner")>
         <[Format](API_control_JobReport.md#AmazonS3-Type-control_JobReport-Format "API_control_JobReport.md#AmazonS3-Type-control_JobReport-Format")>***string***</[Format](API_control_JobReport.md#AmazonS3-Type-control_JobReport-Format "API_control_JobReport.md#AmazonS3-Type-control_JobReport-Format")>
         <[Prefix](API_control_JobReport.md#AmazonS3-Type-control_JobReport-Prefix "API_control_JobReport.md#AmazonS3-Type-control_JobReport-Prefix")>***string***</[Prefix](API_control_JobReport.md#AmazonS3-Type-control_JobReport-Prefix "API_control_JobReport.md#AmazonS3-Type-control_JobReport-Prefix")>
         <[ReportScope](API_control_JobReport.md#AmazonS3-Type-control_JobReport-ReportScope "API_control_JobReport.md#AmazonS3-Type-control_JobReport-ReportScope")>***string***</[ReportScope](API_control_JobReport.md#AmazonS3-Type-control_JobReport-ReportScope "API_control_JobReport.md#AmazonS3-Type-control_JobReport-ReportScope")>
      </[Report](API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-Report "API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-Report")>
      <[RoleArn](API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-RoleArn "API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-RoleArn")>***string***</[RoleArn](API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-RoleArn "API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-RoleArn")>
      <[Status](API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-Status "API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-Status")>***string***</[Status](API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-Status "API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-Status")>
      <[StatusUpdateReason](API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-StatusUpdateReason "API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-StatusUpdateReason")>***string***</[StatusUpdateReason](API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-StatusUpdateReason "API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-StatusUpdateReason")>
      <[SuspendedCause](API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-SuspendedCause "API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-SuspendedCause")>***string***</[SuspendedCause](API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-SuspendedCause "API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-SuspendedCause")>
      <[SuspendedDate](API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-SuspendedDate "API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-SuspendedDate")>***timestamp***</[SuspendedDate](API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-SuspendedDate "API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-SuspendedDate")>
      <[TerminationDate](API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-TerminationDate "API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-TerminationDate")>***timestamp***</[TerminationDate](API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-TerminationDate "API_control_JobDescriptor.md#AmazonS3-Type-control_JobDescriptor-TerminationDate")>
   </[Job](#AmazonS3-control_DescribeJob-response-Job "#AmazonS3-control_DescribeJob-response-Job")>
</[DescribeJobResult](#AmazonS3-control_DescribeJob-response-DescribeJobResult "#AmazonS3-control_DescribeJob-response-DescribeJobResult")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[DescribeJobResult](#API_control_DescribeJob_ResponseSyntax "#API_control_DescribeJob_ResponseSyntax")**


Root level tag for the DescribeJobResult parameters.


Required: Yes




**[Job](#API_control_DescribeJob_ResponseSyntax "#API_control_DescribeJob_ResponseSyntax")**


Contains the configuration parameters and status for the job specified in the
 `Describe Job` request.


Type: [JobDescriptor](API_control_JobDescriptor.md "API_control_JobDescriptor.md") data type




## Errors





**BadRequestException** 



HTTP Status Code: 400




**InternalServiceException** 



HTTP Status Code: 500




**NotFoundException** 



HTTP Status Code: 400




**TooManyRequestsException** 



HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/DescribeJob "https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/DescribeJob")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/DescribeJob "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/DescribeJob")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/DescribeJob "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/DescribeJob")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/DescribeJob "https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/DescribeJob")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/DescribeJob "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/DescribeJob")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/DescribeJob "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/DescribeJob")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/DescribeJob "https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/DescribeJob")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/DescribeJob "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/DescribeJob")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/DescribeJob "https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/DescribeJob")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/DescribeJob "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/DescribeJob")
