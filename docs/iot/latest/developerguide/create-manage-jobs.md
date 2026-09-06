

# Managing jobs
<a name="create-manage-jobs"></a>

Use jobs to notify devices of a software or firmware update. You can use the [AWS IoT console](https://console.aws.amazon.com/iot/), the [Job management and control API operations](jobs-management-control-api.md#jobs-http-api), the [AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/reference/iot/index.html), or the [AWS SDKs](http://aws.amazon.com/tools/#sdk) to create and manage jobs.

## Code signing for jobs
<a name="create-manage-jobs-code-signing"></a>

 When sending code to devices, for devices to detect whether the code has been modified in transit, we recommend that you sign the code file by using the AWS CLI. For instructions, see [Create and manage jobs by using the AWS CLI](manage-job-cli.md).

For more information, see [What Is Code Signing for AWS IoT?](https://docs.aws.amazon.com/signer/latest/developerguide/Welcome.html).

## Job document
<a name="create-manage-jobs-job-doc"></a>

Before you create a job, you must create a job document. If you're using code signing for AWS IoT, you must upload your job document to a versioned Amazon S3 bucket. For more information about creating an Amazon S3 bucket and uploading files to it, see [Getting Started with Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/GetStartedWithS3.html) in the *Amazon S3 Getting Started Guide*.

**Tip**  
For job document examples, see the [jobs-agent.js](https://www.npmjs.com/package/aws-iot-device-sdk#jobs-agentjs) example in the AWS IoT SDK for JavaScript.

## Presigned URLs
<a name="create-manage-jobs-presigned-URLs"></a>

Your job document can contain a presigned Amazon S3 URL that points to your code file (or other file). Presigned Amazon S3 URLs are valid only for a limited amount of time and are generated when a device requests a job document. Because the presigned URL isn't created when you're creating the job document, use a placeholder URL in your job document instead. A placeholder URL looks like the following:

`${aws:iot:s3-presigned-url-v2:https://s3.region.amazonaws.com/{{<bucket>}}/{{<code file>}}}`

where:
+ {{bucket}} is the Amazon S3 bucket that contains the code file.
+ {{code file}} is the Amazon S3 key of the code file.

When a device requests the job document, AWS IoT generates the presigned URL and replaces the placeholder URL with the presigned URL. Your job document is then sent to the device.

**IAM role to grant permission to download files from S3**  
When you create a job that uses presigned Amazon S3 URLs, you must provide an IAM role. The role must grant permission to download files from the Amazon S3 bucket where the data or updates are stored. The role must also grant permission for AWS IoT to assume the role.

You can specify an optional timeout for the presigned URL. For more information, see [CreateJob](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateJob.html).

**Grant AWS IoT Jobs permission to assume your role**

1. Go to the [Roles hub of the IAM console](https://console.aws.amazon.com/iamv2/home#/roles) and choose your role.

1. On the **Trust Relationships** tab, choose **Edit Trust Relationship** and replace the policy document with the following JSON. Choose **Update Trust Policy**.  
****  

   ```
   {
     "Version":"2012-10-17",		 	 	 
     "Statement": [
       {
         "Sid": "",
         "Effect": "Allow",
         "Principal": {
           "Service": [
             "iot.amazonaws.com"
           ]
         },
         "Action": "sts:AssumeRole"
       }
     ]
   }
   ```

1. To protect against the confused deputy problem, add the global condition context keys [`aws:SourceArn`](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourcearn) and [`aws:SourceAccount`](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourceaccount) to the policy.
**Important**  
Your `aws:SourceArn` must comply with the format: `arn:aws:iot:{{region}}:{{account-id}}:*`. Make sure that {{region}} matches your AWS IoT Region and {{account-id}} matches your customer account ID. For more information, see [Cross-service confused deputy prevention](cross-service-confused-deputy-prevention.md). 

   ```
   {
     "Effect": "Allow",
     "Statement": [
       {
         "Effect": "Allow",
         "Principal": {
           "Service": 
             "iot.amazonaws.com"        
          },
         "Action": "sts:AssumeRole",
         "Condition": {
            "StringEquals": {
               "aws:SourceAccount": "123456789012"
            },
            "ArnLike": {
                 "aws:SourceArn": "arn:aws:iot:*:123456789012:job/*"
            }
          }
        }
      ]
   }
   ```

1. If your job uses a job document that's an Amazon S3 object, choose **Permissions** and use the following JSON. This adds a policy that grants permission to download files from your Amazon S3 bucket:  
****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Effect": "Allow",
               "Action": "s3:GetObject",
               "Resource": "arn:aws:s3:::{{your_S3_bucket}}/*"
           }
       ]
   }
   ```

## Presigned URL for file upload
<a name="create-manage-jobs-presigned-URLs-upload"></a>

If your devices need to upload files to an Amazon S3 bucket during a job deployment, then you can include the following presigned URL placeholder in your job document: 

```
${aws:iot:s3-presigned-url-upload:https://s3.region.amazonaws.com/{{<bucket>}}/{{<key>}}} 
```

You can use a max of two of each of `${thingName}`, `${jobId}`, and `${executionNumber}` as reserved keywords within the `key` attribute in the file upload placeholder URL located in your job document. The local placeholder representing those reserved keywords in the `key` attribute will be parsed and replaced when the job execution is created. Using a local placeholder with reserved keywords specific to each device ensures each uploaded file from a device is specific to that device and not overwritten by a similar uploaded file from another device targeted by the same job deployment. For information on troubleshooting local placeholders within a presigned URL placeholder for uploading files during a job deployment, see [General Troubleshooting Error Messages](software-package-catalog-troubleshooting.md#spc-general-troubleshooting).

**Note**  
The Amazon S3 bucket name can't contain the local placeholder representing the reserved keywords for the uploaded file. The local placeholder must be located in the `key` attribute.

This presigned URL placeholder will be converted to an Amazon S3 presigned upload URL in your job document when a device receives it. Your devices will use this to upload files to a destination Amazon S3 bucket.

**Note**  
When the Amazon S3 bucket and key are not provided in the above placeholder URL, AWS IoT Jobs will automatically generate a key for each device using a max of two of each of `${thingName}`, `${jobId}`, and `${executionNumber}`.

## Presigned URL using Amazon S3 versioning
<a name="create-manage-jobs-presigned-URLs-versioning"></a>

Safeguarding the integrity of a file stored in an Amazon S3 bucket is critical for ensuring secure job deployments using that file to your device fleet. With the use of Amazon S3 versioning, you can add a version identifier for each variant of the file stored in your Amazon S3 bucket for tracking each verison of the file. This provides insight into what version of the file is deployed to your device fleet using AWS IoT Jobs. For more information on Amazon S3 buckets using versioning, see [Using versioning in Amazon S3 buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html).

If the file is stored in Amazon S3 and the job document contains a presigned URL placeholder, AWS IoT Jobs will generate a presigned URL in the job document using the Amazon S3 bucket, bucket key, and version of the file stored in the Amazon S3 bucket. This presigned URL generated in the job document will replace the presigned URL placeholder originally in the job document. If you update the file stored in your Amazon S3 bucket, a new version of the file and subsequent `versionId` will be created to signal the updates made and provide the ability to target that specific file in future job deployments.

Refer to the following examples for a before and during look of the Amazon S3 presigned URLs in your job document using the `versionId`:

**Amazon S3 Presigned URL placeholder (Before Job Deployment)**

```
//Virtual-hosted style URL
${aws:iot:s3-presigned-url-v2:https://{{bucket-name}}.s3.{{region-code}}.amazonaws.com/{{key-name}}%3FversionId%3D{{version-id}}}

//Path-style URL
${aws:iot:s3-presigned-url-v2:https://s3.{{region-code}}.amazonaws.com/{{bucket-name}}/{{key-name}}%3FversionId%3D{{version-id}}}
```

**Amazon S3 Presigned URL (During Job Deployment)**

```
//Virtual-hosted style URL
${aws:iot:s3-presigned-url-v2:https://{{sample-bucket-name}}.s3.{{us-west-2}}.amazonaws.com/{{sample-code-file.png}}%3FversionId%3D{{version1}}}

//Path-style
${aws:iot:s3-presigned-url-v2:https://s3.{{us-west-2}}.amazonaws.com/{{sample-bucket-name}}/{{sample-code-file.png}}%3FversionId%3D{{version1}}}
```

For more information on Amazon S3 virtual-hosted and path-style object URLs, see [Virtual-hosted-style requests](https://docs.aws.amazon.com/AmazonS3/latest/userguide/VirtualHosting.html#virtual-hosted-style-access) and [Path-style requests](https://docs.aws.amazon.com/AmazonS3/latest/userguide/VirtualHosting.html#path-style-access).

**Note**  
If you want to append `versionId` to a Amazon S3 presigned URL, it must conform to URL encoding supporting AWS SDK for Java 2.x. For more information, see [Changes in parsing Amazon S3 URIs from version 1 to version 2](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-s3-uri-parser.html#migration-3-uri-parser-api-changes).

**Amazon S3 Presigned URL placeholder version differences**

The following list outlines the differences between Amazon S3 presigned URL placeholders `${aws:iot:s3-presigned-url-v1` (version 1) and `${aws:iot:s3-presigned-url-v2` (version 2):
+  The Amazon S3 presigned URL placeholder `${aws:iot:s3-presigned-url-v1` does not support `version-id`.
+ The Amazon S3 presigned URL placeholder `${aws:iot:s3-presigned-url-v1` receives the Amazon S3 URL as unencoded. The Amazon S3 Presigned URL placeholder `${aws:iot:s3-presigned-url-v2` requires the Amazon S3 URL to be encoded to conform with the Amazon S3 SDK standard.

**Topics**
+ [Code signing for jobs](#create-manage-jobs-code-signing)
+ [Job document](#create-manage-jobs-job-doc)
+ [Presigned URLs](#create-manage-jobs-presigned-URLs)
+ [Presigned URL for file upload](#create-manage-jobs-presigned-URLs-upload)
+ [Presigned URL using Amazon S3 versioning](#create-manage-jobs-presigned-URLs-versioning)
+ [Create and manage jobs by using the AWS Management Console](manage-job-console.md)
+ [Create and manage jobs by using the AWS CLI](manage-job-cli.md)