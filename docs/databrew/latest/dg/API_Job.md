# Job

Represents all of the attributes of a DataBrew job.

## Contents

###### Note

In the following list, the required parameters are described first.

**Name**

The unique name of the job.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 240.

Required: Yes

**AccountId**

The ID of the AWS account that owns the job.

Type: String

Length Constraints: Maximum length of 255.

Required: No

**CreateDate**

The date and time that the job was created.

Type: Timestamp

Required: No

**CreatedBy**

The Amazon Resource Name (ARN) of the user who created the job.

Type: String

Required: No

**DatabaseOutputs**

Represents a list of JDBC database output objects which defines the output
destination for a DataBrew recipe job to write into.

Type: Array of [DatabaseOutput](API_DatabaseOutput.md "API_DatabaseOutput.md") objects

Array Members: Minimum number of 1 item.

Required: No

**DataCatalogOutputs**

One or more artifacts that represent the AWS Glue Data Catalog output
from running the job.

Type: Array of [DataCatalogOutput](API_DataCatalogOutput.md "API_DataCatalogOutput.md") objects

Array Members: Minimum number of 1 item.

Required: No

**DatasetName**

A dataset that the job is to process.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

Required: No

**EncryptionKeyArn**

The Amazon Resource Name (ARN) of an encryption key that is used to protect the job
output. For more information, see [Encrypting data
written by DataBrew jobs](encryption-security-configuration.md "encryption-security-configuration.md")

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Required: No

**EncryptionMode**

The encryption mode for the job, which can be one of the following:

- `SSE-KMS` - Server-side encryption with keys managed by AWS KMS.
- `SSE-S3` - Server-side encryption with keys managed by Amazon S3.

Type: String

Valid Values: `SSE-KMS | SSE-S3`

Required: No

**JobSample**

A sample configuration for profile jobs only, which determines the number of rows on which the
profile job is run. If a `JobSample` value isn't provided, the default value
is used. The default value is CUSTOM_ROWS for the mode parameter and 20,000 for the
size parameter.

Type: [JobSample](API_JobSample.md "API_JobSample.md") object

Required: No

**LastModifiedBy**

The Amazon Resource Name (ARN) of the user who last modified the job.

Type: String

Required: No

**LastModifiedDate**

The modification date and time of the job.

Type: Timestamp

Required: No

**LogSubscription**

The current status of Amazon CloudWatch logging for the job.

Type: String

Valid Values: `ENABLE | DISABLE`

Required: No

**MaxCapacity**

The maximum number of nodes that can be consumed when the job processes data.

Type: Integer

Required: No

**MaxRetries**

The maximum number of times to retry the job after a job run fails.

Type: Integer

Valid Range: Minimum value of 0.

Required: No

**Outputs**

One or more artifacts that represent output from running the job.

Type: Array of [Output](API_Output.md "API_Output.md") objects

Array Members: Minimum number of 1 item.

Required: No

**ProjectName**

The name of the project that the job is associated with.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

Required: No

**RecipeReference**

A set of steps that the job runs.

Type: [RecipeReference](API_RecipeReference.md "API_RecipeReference.md") object

Required: No

**ResourceArn**

The unique Amazon Resource Name (ARN) for the job.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Required: No

**RoleArn**

The Amazon Resource Name (ARN) of the role to be assumed for this job.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Required: No

**Tags**

Metadata tags that have been applied to the job.

Type: String to string map

Map Entries: Maximum number of 200 items.

Key Length Constraints: Minimum length of 1. Maximum length of 128.

Value Length Constraints: Maximum length of 256.

Required: No

**Timeout**

The job's timeout in minutes. A job that attempts to run longer than this timeout
period ends with a status of `TIMEOUT`.

Type: Integer

Valid Range: Minimum value of 0.

Required: No

**Type**

The job type of the job, which must be one of the following:

- `PROFILE` - A job to analyze a dataset, to determine its size, data
  types, data distribution, and more.
- `RECIPE` - A job to apply one or more transformations to a
  dataset.

Type: String

Valid Values: `PROFILE | RECIPE`

Required: No

**ValidationConfigurations**

List of validation configurations that are applied to the profile job.

Type: Array of [ValidationConfiguration](API_ValidationConfiguration.md "API_ValidationConfiguration.md") objects

Array Members: Minimum number of 1 item.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/databrew-2017-07-25/Job.md "../../../goto/SdkForCpp/databrew-2017-07-25/Job.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/databrew-2017-07-25/Job.md "../../../goto/SdkForJavaV2/databrew-2017-07-25/Job.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/databrew-2017-07-25/Job.md "../../../goto/SdkForRubyV3/databrew-2017-07-25/Job.md")
