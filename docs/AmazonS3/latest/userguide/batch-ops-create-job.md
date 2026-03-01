# Creating an S3 Batch Operations job

With Amazon S3 Batch Operations, you can perform large-scale batch operations on a list of
specific Amazon S3 objects. This section describes the information that you need to create an
S3 Batch Operations job and the results of a `CreateJob` request. It also provides
instructions for creating a Batch Operations job by using the Amazon S3 console, AWS Command Line Interface (AWS CLI), and
AWS SDK for Java.

When you create an S3 Batch Operations job, you can request a completion report for all tasks or
only failed tasks. As long as at least one task has been invoked successfully, S3 Batch Operations
generates a report for jobs that have been completed, have failed, or have been canceled. For
more information, see [Examples: S3 Batch Operations completion reports](batch-ops-examples-reports.md "batch-ops-examples-reports.md").

The following video provides a brief demonstration of how
to create a Batch Operations job by using the Amazon S3 console.

###### Topics

- [Batch Operations job request elements](#batch-ops-create-job-request-elements "#batch-ops-create-job-request-elements")
- [Specifying a manifest](#specify-batchjob-manifest "#specify-batchjob-manifest")
- [Generating an object list automatically and saving it as a manifest file](#automatically-generate-manifest-file "#automatically-generate-manifest-file")
- [Creating a manifest file](#create-manifest-file "#create-manifest-file")
- [Using an existing manifest](#specify-existing-manifest-file "#specify-existing-manifest-file")
- [Creating a job](#to-create-batch-ops-job "#to-create-batch-ops-job")
- [Job responses](#batch-ops-create-job-response-elements "#batch-ops-create-job-response-elements")

## Batch Operations job request elements

To create an S3 Batch Operations job, you must provide the following information:

**Operation**

Specify the operation that you want S3 Batch Operations to run against the objects in the
manifest. Each operation type accepts parameters that are specific to that operation.
With Batch Operations, you can perform an operation in bulk, with the same results as if you
performed that operation one-by-one on each object.

**Manifest**

A _manifest_ is an Amazon S3 object list that contains
the object keys that you want Amazon S3 to act upon. You can use the following methods to
specify a manifest for a Batch Operations job:

- Direct Batch Operations to generate an object list based on metadata that you specify.
  You can save this list as a manifest file and use it when you create your job. This
  option is available for any job type that you create by using the Amazon S3 console, the
  AWS CLI, AWS SDKs, or Amazon S3 REST API.
- Generate an object list automatically based on an existing replication
  configuration. You can save this list as a manifest file and use it again for future
  jobs.
- Create a new manifest file manually.
- Use an existing manifest.

###### Note

- Regardless of how you specify the objects to work on, the manifest itself must
  be stored in a general purpose bucket. Batch Operations can't import existing manifests
  from, or save generated object lists as manifests to directory buckets. Objects
  described within the manifest, however, can be stored in directory buckets. For
  more information, see [Directory
  buckets](directory-buckets-overview.md "directory-buckets-overview.md").
- If the objects in your manifest are in a versioned bucket, specifying the
  version IDs for the objects directs Batch Operations to perform the operation on a
  specific version. If no version IDs are specified, Batch Operations performs the
  operation on the latest version of the objects. If your manifest includes a
  version ID field, you must provide a version ID for all objects in the
  manifest.

For more information, see [Specifying a manifest](#specify-batchjob-manifest "#specify-batchjob-manifest").

**Priority**

Use job priorities to indicate the relative priority of this job to others running
in your account. A higher number indicates higher priority.

Job priorities only have meaning relative to the priorities that are set for other
jobs in the same account and Region. You can choose whatever numbering system works for
you. For example, you might want to assign all **Restore**
(`RestoreObject`) jobs a priority of 1, all **Copy**
(`CopyObject`) jobs a priority of 2, and all **Replace access
control lists (ACLs)** (`PutObjectAcl`) jobs a priority of 3.

S3 Batch Operations prioritizes jobs according to priority numbers, but strict ordering
isn't guaranteed. Therefore, don't use job priorities to ensure that any one job starts
or finishes before any other job. If you must ensure strict ordering, wait until one job
has finished before starting the next.

**RoleArn**

Specify an AWS Identity and Access Management (IAM) role to run the job. The IAM role that you use must
have sufficient permissions to perform the operation specified in the job. For example,
to run a `CopyObject` job, the IAM role must have the
`s3:GetObject` permission for the source bucket and the
`s3:PutObject` permission for the destination bucket. The role also needs
permissions to read the manifest and write the completion report.

The IAM role can be an existing role. Or, if you use the Amazon S3 console to create
the job, it can be an IAM role that Amazon S3 creates automatically for you. For more
information, see [Granting permissions for Batch Operations](batch-ops-iam-role-policies.md "batch-ops-iam-role-policies.md").

For more information about IAM roles, see [IAM roles](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") in the
_IAM User Guide_. For more information about Amazon S3 permissions,
see [Policy actions for Amazon S3](security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies-actions "security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies-actions").

###### Note

Batch Operations jobs that perform actions on directory buckets require specific
permissions. For more information, see [AWS Identity and Access Management (IAM) for S3
Express One Zone](s3-express-security-iam.md "s3-express-security-iam.md").

**Report**

Specify whether you want S3 Batch Operations to generate a completion report. If you
request a completion report, you must also provide the parameters for the report in
this element. The following information is required:

- The bucket where you want to store the report

###### Note

The report must be stored in a general purpose bucket. Batch Operations can't save
reports to directory buckets. For more information, see [Directory
buckets](directory-buckets-overview.md "directory-buckets-overview.md").

- The format of the report
- Whether you want the report to include the details of all tasks or only failed
  tasks
- An optional prefix string

If the `CreateJob.Report.ExpectedBucketOwner` field is supplied, it requires that the completion report bucket owner matches. If it doesn't match, then the job fails.

###### Note

Completion reports are always encrypted with server-side encryption with Amazon S3
managed keys (SSE-S3).

**Tags (optional)**

You can label and control access to your S3 Batch Operations jobs by adding
_tags_. You can use tags to identify who is responsible for a
Batch Operations job, or to control how users interact with Batch Operations jobs. The presence of
job tags can grant or limit a user's ability to cancel a job, activate a job in the
confirmation state, or change a job's priority level. For example, you could grant a
user permission to invoke the `CreateJob` operation, provided that the job is
created with the tag `"Department=Finance"`.

You can create jobs with tags attached to them, and you can add tags to jobs after
you create them.

For more information, see [Controlling access and labeling jobs using tags](batch-ops-job-tags.md "batch-ops-job-tags.md").

**Description (optional)**

To track and monitor your job, you can also provide a description of up to 256
characters. Amazon S3 includes this description whenever it returns information about a job
or displays job details on the Amazon S3 console. You can then easily sort and filter jobs
according to the descriptions that you assigned. Descriptions don't need to be unique,
so you can use descriptions as categories (for example, "Weekly Log Copy Jobs") to help
you track groups of similar jobs.

## Specifying a manifest

A _manifest_ is an Amazon S3 object list that contains the object keys that you want Amazon S3 to act
upon. You can use the following methods to specify a manifest for a Batch Operations job:

- Direct Batch Operations to generate an object list based on metadata
  that you specify. You can save this list as a manifest and use it when you create your job.
  This option is available for any job type that you create by using the Amazon S3 console, the AWS CLI, AWS SDKs, or Amazon S3 REST API.
- Generate an object list automatically based on an existing replication configuration.
  You can save this list as a manifest and use it again for future jobs.
- Create a new manifest file manually.
- Use an existing manifest.

###### Note

- Amazon S3 Batch Operations does not support cross-Region object list generation.
- Regardless of how you specify the objects to work on, the manifest itself must be stored in a
  general purpose bucket. Batch Operations can't import existing manifests from, or save
  generated object lists as manifests to directory buckets. Objects described within the
  manifest, however, can be stored in directory buckets. For more information, see [Directory buckets](directory-buckets-overview.md "directory-buckets-overview.md").

## Generating an object list automatically and saving it as a manifest file

You can direct Amazon S3 to generate an object list automatically based on metadata that you
specify. You can save this list as a manifest and use it when you create your job.
This option is available for any job type that you create by using the Amazon S3 console, the AWS CLI, AWS SDKs, or Amazon S3 REST API.

To generate an object list automatically and save it as a manifest file, you specify the
following elements as part of your job creation request:

- Information about the bucket that contains your source objects, including the bucket
  owner and Amazon Resource Name (ARN).
- Information about the manifest output, including a flag to create a manifest file,
  the output bucket owner, the ARN, the prefix, the file format, and the encryption
  type.
- Optional criteria to filter objects by their creation date, key name, size,
  encryption type, KMS key ARN, Bucket Key and storage class, In the case of replication
  jobs, you can also use tags to filter objects.

### Object filter criteria

To filter the list of objects to be included in an automatically generated object
list, you can specify the following criteria. For more information, see [JobManifestGeneratorFilter](../API/API_control_JobManifestGeneratorFilter.md "../API/API_control_JobManifestGeneratorFilter.md") in the _Amazon S3 API
Reference_.

**CreatedAfter**

If provided, the generated manifest includes only source bucket objects that
were created after this time.

**CreatedBefore**

If provided, the generated manifest includes only source bucket objects that
were created before this time.

**EligibleForReplication**

If provided, the generated manifest includes objects only if they are eligible
for replication according to the replication configuration on the source
bucket.

**KeyNameConstraint**

If provided, the generated manifest includes only source bucket objects whose
object keys match the string constraints specified for **MatchAnySubstring**, **MatchAnyPrefix**,
and **MatchAnySuffix**.

**MatchAnySubstring** – If provided, the
generated manifest includes objects if the specified string appears anywhere within
the object key string.

**MatchAnyPrefix** – If provided, the
generated manifest includes objects if the specified string appears at the start of
the object key string.

**MatchAnySuffix** – If provided, the
generated manifest includes objects if the specified string appears at the end of
the object key string.

**MatchAnyObjectEncryption**

If provided, the generated object list saved as a manifest file includes only
source bucket objects with the indicated server-side encryption type (SSE-S3, SSE-KMS,
DSSE-KMS, SSE-C, or NOT-SSE). If you select SSE- KMS or DSSE-KMS, you can optionally
further filter your results by specifying a specific KMS key ARN. If you select
SSE-KMS, you can also optionally further filter your results by Bucket Key enabled
status.

**MatchAnyStorageClass**

If provided, the generated manifest includes only source bucket objects that are
stored with the specified storage class.

**ObjectReplicationStatuses**

If provided, the generated manifest includes only source bucket objects that
have one of the specified replication statuses.

**ObjectSizeGreaterThanBytes**

If provided, the generated manifest includes only source bucket objects whose
file size is greater than the specified number of bytes.

**ObjectSizeLessThanBytes**

If provided, the generated manifest includes only source bucket objects whose
file size is less than the specified number of bytes.

###### Note

You can't clone most jobs that have automatically generated object lists saved as
manifests. Batch replication jobs can be cloned, except when they use the
`KeyNameConstraint`, `MatchAnyStorageClass`,
`ObjectSizeGreaterThanBytes`, or `ObjectSizeLessThanBytes`
manifest filter criteria.

The syntax for specifying manifest criteria varies depending on the method that you use
to create your job. For examples, see [Creating a job](#to-create-batch-ops-job "#to-create-batch-ops-job").

## Creating a manifest file

To create a manifest file manually, you specify the manifest object key, ETag (entity
tag), and optional version ID in a CSV-formatted list. The contents of the manifest must be
URL-encoded.

By default, Amazon S3 automatically uses server-side encryption with Amazon S3 managed keys
(SSE-S3) to encrypt a manifest that's uploaded to an Amazon S3 bucket. Manifests that use
server-side encryption with customer-provided keys (SSE-C) are not supported. Manifests that
use server-side encryption with AWS Key Management Service (AWS KMS) keys (SSE-KMS) are supported only when
you're using CSV-formatted inventory reports. Using a manually created manifest with AWS KMS is not supported.

Your manifest must contain the bucket name, object key, and optionally, the object
version for each object. Any other fields in the manifest are not used by
S3 Batch Operations.

###### Note

If the objects in your manifest are in a versioned bucket, specifying the version IDs
for the objects directs Batch Operations to perform the operation on a specific version. If no
version IDs are specified, Batch Operations performs the operation on the latest version of the
objects. If your manifest includes a version ID field, you must provide a version ID for
all objects in the manifest.

The following is an example manifest in CSV format without version IDs.

```
amzn-s3-demo-bucket1,objectkey1
amzn-s3-demo-bucket1,objectkey2
amzn-s3-demo-bucket1,objectkey3
amzn-s3-demo-bucket1,photos/jpgs/objectkey4
amzn-s3-demo-bucket1,photos/jpgs/newjersey/objectkey5
amzn-s3-demo-bucket1,object%20key%20with%20spaces
```

The following is an example manifest in CSV format that includes version IDs.

```
amzn-s3-demo-bucket1,objectkey1,PZ9ibn9D5lP6p298B7S9_ceqx1n5EJ0p
amzn-s3-demo-bucket1,objectkey2,YY_ouuAJByNW1LRBfFMfxMge7XQWxMBF
amzn-s3-demo-bucket1,objectkey3,jbo9_jhdPEyB4RrmOxWS0kU0EoNrU_oI
amzn-s3-demo-bucket1,photos/jpgs/objectkey4,6EqlikJJxLTsHsnbZbSRffn24_eh5Ny4
amzn-s3-demo-bucket1,photos/jpgs/newjersey/objectkey5,imHf3FAiRsvBW_EHB8GOu.NHunHO1gVs
amzn-s3-demo-bucket1,object%20key%20with%20spaces,9HkPvDaZY5MVbMhn6TMn1YTb5ArQAo3w
```

## Using an existing manifest

You can specify an existing manifest to create a Batch Operations job by using one of the
following two formats:

- **Amazon S3 Inventory report** – Must be a
  CSV-formatted Amazon S3 Inventory report. You must specify the
  `manifest.json` file that is associated with the inventory report.
  For more information about inventory reports, see [Cataloging and analyzing your data with S3 Inventory](storage-inventory.md "storage-inventory.md"). If the inventory report includes version IDs,
  S3 Batch Operations operates on the specific object versions.

###### Note

    + S3 Batch Operations supports CSV *inventory reports* that are
     encrypted with SSE-KMS.
    + If you submit an inventory report manifest that's encrypted with SSE-KMS, your
     IAM policy must include the permissions `"kms:Decrypt"` and
     `"kms:GenerateDataKey"` for the `manifest.json`
     object and all associated CSV data files.

- **CSV file** – Each row in the file must include
  the bucket name, object key, and optionally, the object version. Object keys must be
  URL-encoded, as shown in the following examples. The manifest must either include
  version IDs for all objects or omit version IDs for all objects. For more information
  about the CSV manifest format, see [JobManifestSpec](../API/API_control_JobManifestSpec.md "../API/API_control_JobManifestSpec.md") in the
  _Amazon Simple Storage Service API Reference_.

###### Note

S3 Batch Operations doesn't support CSV _manifest files_ that are
encrypted with SSE-KMS.

###### Important

When you're using a manually created manifest and a versioned bucket, we recommend
that you specify the version IDs for the objects. When you create a job, S3 Batch Operations
parses the entire manifest before running the job. However, it doesn't take a "snapshot"
of the state of the bucket.

Because manifests can contain billions of objects, jobs might take a long time to run,
which can affect which version of an object that the job acts upon. Suppose that you
overwrite an object with a new version while a job is running and you didn't specify a
version ID for that object. In this case, Amazon S3 performs the operation on the latest
version of the object, not on the version that existed when you created the job. The only
way to avoid this behavior is to specify version IDs for the objects that are listed in
the manifest.

## Creating a job

You can create S3 Batch Operations jobs by using the Amazon S3 console, AWS CLI, AWS SDKs, or Amazon S3
REST API.

For more information about creating a job request, see [Batch Operations job request elements](#batch-ops-create-job-request-elements "#batch-ops-create-job-request-elements").

###### Prerequisites

Before you create a Batch Operations job, confirm that you have configured the relevant
permissions. For more information, see [Granting permissions for Batch Operations](batch-ops-iam-role-policies.md "batch-ops-iam-role-policies.md").

###### To create a Batch Operations job using the S3 console

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. Choose **Batch Operations** on the left navigation pane of the Amazon S3
   console.
3. Choose **Create job**.
4. Under **Choose Region and scope**, choose and view the AWS Region
   where you want to create your job.

###### Note

For copy operations, you must create the job in the same Region as the destination
bucket. For all other operations, you must create the job in the same Region as the
objects in the manifest. 5. For **Scope**, specify the list of objects that your Batch Operations
job will act upon.

Under **Object list**, you can choose to generate a manifest using an
object list, generate a manifest using a replication configuration, or use an existing
manifest.

    * If you choose **Generate an object list**, an object list is
     automatically generated based on the source location and metadata that you specify. You
     can save this list as a manifest and use it again for future jobs.


    ###### Note

    To generate an object list, you must have the
     `s3:PutInventoryConfiguration` permission. The source bucket must be a
     general purpose bucket.
    * If you choose **Use an existing manifest**, you can import an
     object list from an existing manifest. A manifest is an S3 Inventory report or CV file
     that lists the specific objects that you want Batch Operations to act upon.
    * If you choose **Use a replication configuration**, you can generate
     an object list automatically based on an existing replication configuration. You can
     save this list as a manifest and use it again for future jobs.


     For this example, choose **Generate an object list**.

6. For **Source account**, choose the account that owns the source
   objects.
7. Under **Source**, enter the path to your source, for example,
   `s3://``amzn-s3-demo-bucket`.
8. Under **Object filters**, you can use filters to filter by any portion
   of the object key or to filter by the end of the object key. The **Object key
   filters** assist in refining the list of objects to be used in the manifest. For
   **Object metadata filters**, choose filters to further define the scope
   of objects to include in the manifest.
9. Under **Choose operation**, choose the operation type that you want to
   perform on all objects listed in the manifest. If your manifest references objects stored in
   a directory bucket, only use the copy or invoke AWS Lambda function operations. All other
   operations aren't supported.
10. After selecting your operation type, choose **Next**.
11. Fill out the information for **Configure additional options**.

For **Permissions**, specify the AWS Identity and Access Management (IAM) role that you want
the job to use. This can be an existing role, or a role that Amazon S3 creates automatically for
you. For more information, see [Granting permissions for Batch Operations](batch-ops-iam-role-policies.md "batch-ops-iam-role-policies.md"). Amazon S3 can create the role for you if you
configured the job to use an S3 generated object list with filters or an object list based
on a replication configuration. 12. When you finish configuring the additional options, choose
**Next**. 13. For **Review**, verify the settings. If you need to make changes,
choose **Previous**. Otherwise, you can choose **Submit
job**.
To create your Batch Operations job with the AWS CLI, choose one of the following examples,
depending on whether you're specifying an existing manifest or generating a manifest
automatically.

Specify manifest
The following example shows how to use the AWS CLI to create an S3 Batch Operations
`S3PutObjectTagging` job that acts on objects that are listed in an
existing manifest file.

###### To create a Batch Operations `S3PutObjectTagging` job by specifying a manifest

1.  Use the following commands to create an AWS Identity and Access Management (IAM) role, and then
    create an IAM policy to assign the relevant permissions. The following role
    and policy grant Amazon S3 permission to add object tags, which you will need when
    you create the job in a subsequent step.
    1. Use the following example command to create an IAM role for Batch Operations
       to use. To use this example command, replace
       `S3BatchJobRole` with the name
       that you want to give to the role.

    ```
    aws iam create-role \
     --role-name `S3BatchJobRole` \
     --assume-role-policy-document '{
       "Version": "2012-10-17"		 	 	 ,
       "Statement":[
          {
             "Effect":"Allow",
             "Principal":{
                "Service":"batchoperations.s3.amazonaws.com"
             },
             "Action":"sts:AssumeRole"
          }
       ]
    }'
    ```

    Record the role's Amazon Resource Name (ARN). You will need the ARN when
    you create a job. 2. Use the following example command to create an IAM policy with the
    necessary permissions and attach it to the IAM role that you created in
    the previous step. For more information about the necessary permissions, see
    [Granting permissions for Batch Operations](batch-ops-iam-role-policies.md "batch-ops-iam-role-policies.md").

    ###### Note

    Batch Operations jobs that perform actions on directory buckets require
    specific permissions. For more information, see [AWS Identity and Access Management
    (IAM) for S3 Express One Zone](s3-express-security-iam.md "s3-express-security-iam.md").

    To use this example command, replace the `user input
 placeholders` as follows:

        * Replace ``S3BatchJobRole`` with
         the name of your IAM role. Make sure that this name matches the name
         that you used earlier.
        * Replace
         ``PutObjectTaggingBatchJobPolicy``
         with the name that you want to give your IAM policy.
        * Replace ``amzn-s3-demo-destination-bucket`` with the name
         of the bucket that contains the objects that you want to apply tags
         to.
        * Replace
         ``amzn-s3-demo-manifest-bucket``
         with the name of the bucket that contains the manifest.
        * Replace
         ``amzn-s3-demo-completion-report-bucket``
         with the name of the bucket where you want the completion report to be
         delivered to.

    ```
    aws iam put-role-policy \
      --role-name `S3BatchJobRole` \
      --policy-name `PutObjectTaggingBatchJobPolicy` \
      --policy-document '{
      "Version": "2012-10-17"		 	 	 ,		 	 	 TCX5-2025-waiver;,
      "Statement":[
        {
          "Effect":"Allow",
          "Action":[
            "s3:PutObjectTagging",
            "s3:PutObjectVersionTagging"
          ],
          "Resource": "arn:aws:s3:::``amzn-s3-demo-destination-bucket``/*"
        },
        {
          "Effect": "Allow",
          "Action": [
            "s3:GetObject",
            "s3:GetObjectVersion",
            "s3:GetBucketLocation"
          ],
          "Resource": [
            "arn:aws:s3:::`amzn-s3-demo-manifest-bucket`",
            "arn:aws:s3:::`amzn-s3-demo-manifest-bucket`/*"
          ]
        },
        {
          "Effect":"Allow",
          "Action":[
            "s3:PutObject",
            "s3:GetBucketLocation"
          ],
          "Resource":[
            "arn:aws:s3:::`amzn-s3-demo-completion-report-bucket`",
            "arn:aws:s3:::`amzn-s3-demo-completion-report-bucket`/*"
          ]
        }
      ]
    }'
    ```

2.  Use the following example command to create an
    `S3PutObjectTagging` job.

The `manifest.csv` file provides a list of bucket and
object key values. The job applies the specified tags to the objects that are
identified in the manifest. The `ETag` is the ETag of the
`manifest.csv` object, which you can get from the Amazon S3 console.
This request specifies the `no-confirmation-required` parameter, so
that you can run the job without having to confirm it with the
`update-job-status` command. For more information, see [create-job](../../../cli/latest/reference/s3control/create-job.md "../../../cli/latest/reference/s3control/create-job.md") in the _AWS CLI Command Reference_.

To use this example command, replace the `user input
 placeholders` with your own information. Replace
`IAM-role` with the ARN of the IAM
role that you created earlier.

```
aws s3control create-job \
    --region `us-west-2` \
    --account-id `acct-id` \
    --operation '{"S3PutObjectTagging": { "TagSet": [{"Key":"`keyOne`", "Value":"`ValueOne`"}] }}' \
    --manifest '{"Spec":{"Format":"`S3BatchOperations_CSV_20180820`","Fields":["Bucket","Key"]},"Location":{"ObjectArn":"arn:aws:s3:::`amzn-s3-demo-manifest-bucket`/`manifest.csv`","ETag":"`60e460c9d1046e73f7dde5043ac3ae85`"}}' \
    --report '{"Bucket":"arn:aws:s3:::``amzn-s3-demo-completion-report-bucket``","Prefix":"`final-reports`", "Format":"`Report_CSV_20180820`","Enabled":true,"ReportScope":"AllTasks"}' \
    --priority `42` \
    --role-arn `IAM-role` \
    --client-request-token $(uuidgen) \
    --description "`job description`" \
    --no-confirmation-required
```

In response, Amazon S3 returns a job ID (for example,
`00e123a4-c0d8-41f4-a0eb-b46f9ba5b07c`). You will need the job ID
to identify, monitor, and modify the job.

Generate manifest
The following example shows how to create an S3 Batch Operations
`S3DeleteObjectTagging` job that automatically generates a manifest
based on your object filter criteria. This criteria includes the creation date, key
name, size, storage class, and tags.

###### To create a Batch Operations `S3DeleteObjectTagging` job by generating a manifest

1.  Use the following commands to create an AWS Identity and Access Management (IAM) role, and then
    create an IAM policy to assign permissions. The following role and policy
    grant Amazon S3 permission to delete object tags, which you will need when you create
    the job in a subsequent step.
    1. Use the following example command to create an IAM role for Batch Operations
       to use. To use this example command, replace
       `S3BatchJobRole` with the name
       that you want to give to the role.

    ```
    aws iam create-role \
     --role-name `S3BatchJobRole` \
     --assume-role-policy-document '{
       "Version": "2012-10-17"		 	 	 ,		 	 	 TCX5-2025-waiver;,
       "Statement":[
          {
             "Effect":"Allow",
             "Principal":{
                "Service":"batchoperations.s3.amazonaws.com"
             },
             "Action":"sts:AssumeRole"
          }
       ]
    }'
    ```

    Record the role's Amazon Resource Name (ARN). You will need the ARN when
    you create a job. 2. Use the following example command to create an IAM policy with the
    necessary permissions and attach it to the IAM role that you created in
    the previous step. For more information about the necessary permissions, see
    [Granting permissions for Batch Operations](batch-ops-iam-role-policies.md "batch-ops-iam-role-policies.md").

    ###### Note

    Batch Operations jobs that perform actions on directory buckets require
    specific permissions. For more information, see [AWS Identity and Access Management
    (IAM) for S3 Express One Zone](s3-express-security-iam.md "s3-express-security-iam.md").

    To use this example command, replace the `user input
 placeholders` as follows:

        * Replace ``S3BatchJobRole`` with
         the name of your IAM role. Make sure that this name matches the name
         that you used earlier.
        * Replace
         ``DeleteObjectTaggingBatchJobPolicy``
         with the name that you want to give your IAM policy.
        * Replace ``amzn-s3-demo-destination-bucket`` with the name
         of the bucket that contains the objects that you want to apply tags
         to.
        * Replace
         ``amzn-s3-demo-manifest-bucket``
         with the name of the bucket where you want to save the
         manifest.
        * Replace
         ``amzn-s3-demo-completion-report-bucket``
         with the name of the bucket where you want the completion report to be
         delivered to.

    ```
    aws iam put-role-policy \
      --role-name ``S3BatchJobRole`` \
      --policy-name ``DeleteObjectTaggingBatchJobPolicy`` \
      --policy-document '{
      "Version": "2012-10-17"		 	 	 ,		 	 	 TCX5-2025-waiver;,
      "Statement":[
        {
          "Effect":"Allow",
          "Action":[
            "s3:DeleteObjectTagging",
            "s3:DeleteObjectVersionTagging"
          ],
          "Resource": "arn:aws:s3:::`amzn-s3-demo-destination-bucket`/*"
        },
        {
          "Effect":"Allow",
          "Action":[
            "s3:PutInventoryConfiguration"
          ],
          "Resource": "arn:aws:s3:::`amzn-s3-demo-destination-bucket`"
        },
        {
          "Effect": "Allow",
          "Action": [
            "s3:GetObject",
            "s3:GetObjectVersion",
            "s3:ListBucket"
          ],
          "Resource": [
            "arn:aws:s3:::``amzn-s3-demo-manifest-bucket``",
            "arn:aws:s3:::``amzn-s3-demo-manifest-bucket``/*"
          ]
        },
        {
          "Effect":"Allow",
          "Action":[
            "s3:PutObject",
            "s3:ListBucket"
          ],
          "Resource":[
            "arn:aws:s3:::``amzn-s3-demo-completion-report-bucket``",
            "arn:aws:s3:::``amzn-s3-demo-completion-report-bucket``/*",
            "arn:aws:s3:::``amzn-s3-demo-manifest-bucket``/*"
          ]
        }
      ]
    }'
    ```

2.  Use the following example command to create the
    `S3DeleteObjectTagging` job.

In this example, the values in the `--report` section specify the
bucket, prefix, format, and scope of the job report that will be generated.
The `--manifest-generator` section specifies information about the
source bucket that contains the objects the job will act upon, information
about the manifest output list that will be generated for the job, and filter
criteria to narrow the scope of objects to be included in the manifest by
creation date, name constraints, size, and storage class. The command also
specifies the job's priority, IAM role, and AWS Region.

For more information, see [create-job](../../../cli/latest/reference/s3control/create-job.md "../../../cli/latest/reference/s3control/create-job.md") in the _AWS CLI Command Reference_.

To use this example command, replace the `user input
 placeholders` with your own information. Replace
`IAM-role` with the ARN of the IAM
role that you created earlier.

```
aws s3control create-job \
    --account-id `012345678901` \
    --operation '{
        "S3DeleteObjectTagging": {}
    }' \
    --report '{
        "Bucket":"arn:aws:s3:::`amzn-s3-demo-completion-report-bucket`",
        "Prefix":"`reports`",
        "Format":"Report_CSV_20180820",
        "Enabled":`true`,
        "ReportScope":"`AllTasks`"
    }' \
    --manifest-generator '{
        "S3JobManifestGenerator": {
          "ExpectedBucketOwner": "`012345678901`",
          "SourceBucket": "arn:aws:s3:::``amzn-s3-demo-source-bucket``",
          "EnableManifestOutput": true,
          "ManifestOutputLocation": {
            "ExpectedManifestBucketOwner": "`012345678901`",
            "Bucket": "arn:aws:s3:::`amzn-s3-demo-manifest-bucket`",
            "ManifestPrefix": "`prefix`",
            "ManifestFormat": "S3InventoryReport_CSV_20211130"
          },
          "Filter": {
            "CreatedAfter": "`2023-09-01`",
            "CreatedBefore": "`2023-10-01`",
            "KeyNameConstraint": {
              "MatchAnyPrefix": [
                "`prefix`"
              ],
              "MatchAnySuffix": [
                "`suffix`"
              ]
            },
            "ObjectSizeGreaterThanBytes": `100`,
            "ObjectSizeLessThanBytes": `200`,
            "MatchAnyStorageClass": [
              "`STANDARD`",
              "`STANDARD_IA`"
            ]
          }
        }
      }' \
     --priority `2` \
     --role-arn `IAM-role` \
     --region `us-east-1`
```

In response, Amazon S3 returns a job ID (for example,
`00e123a4-c0d8-41f4-a0eb-b46f9ba5b07c`). You will need this job ID
to identify, monitor, or modify the job.

To create your Batch Operations job with the AWS SDK for Java, you can choose between two approaches depending on whether you're specifying an existing manifest or generating a manifest automatically:

- _Specify existing manifest:_ Create an S3 Batch Operations job (such as `S3PutObjectTagging`) that acts on objects listed in an existing manifest file. This approach requires you to provide the manifest location, ETag, and format specifications.
- _Generate manifest automatically:_ Create an S3 Batch Operations job (such as `s3PutObjectCopy`) that automatically generates a manifest based on object filter criteria, including creation date, key name, and size constraints.
  Both approaches use the S3Control client to configure job operations, manifest specifications, job reports, IAM roles, and other job parameters including priority and confirmation requirements.

For examples of how to create S3 Batch Operations jobs with the AWS SDK for Java, see [Create a batch job to copy objects](../API/s3-control_example_s3-control_CreateJob_section.md "../API/s3-control_example_s3-control_CreateJob_section.md") in the _Amazon S3 API Reference_.

You can use the REST API to create a Batch Operations job. For more information, see [CreateJob](../API/API_control_CreateJob.md "../API/API_control_CreateJob.md") in the _Amazon Simple Storage Service API Reference_.

## Job responses

If the `CreateJob` request succeeds, Amazon S3 returns a job ID. The job ID is a
unique identifier that Amazon S3 generates automatically so that you can identify your Batch Operations
job and monitor its status.

When you create a job through the AWS CLI, AWS SDKs, or REST API, you can set
S3 Batch Operations to begin processing the job automatically. The job runs as soon as it's ready
instead of waiting behind higher-priority jobs.

When you create a job through the Amazon S3 console, you must review the job details and
confirm that you want to run the job before Batch Operations can begin to process it. If a job
remains in the suspended state for over 30 days, it will fail.
