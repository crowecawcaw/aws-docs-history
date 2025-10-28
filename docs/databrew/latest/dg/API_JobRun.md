# JobRun

Represents one run of a DataBrew job.

## Contents

###### Note

In the following list, the required parameters are described first.

**Attempt**

The number of times that DataBrew has attempted to run the job.

Type: Integer

Required: No

**CompletedOn**

The date and time when the job completed processing.

Type: Timestamp

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

The name of the dataset for the job to process.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

Required: No

**ErrorMessage**

A message indicating an error (if any) that was encountered when the job ran.

Type: String

Required: No

**ExecutionTime**

The amount of time, in seconds, during which a job run consumed resources.

Type: Integer

Required: No

**JobName**

The name of the job being processed during this run.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 240.

Required: No

**JobSample**

A sample configuration for profile jobs only, which determines the number of rows on which the
profile job is run. If a `JobSample` value isn't provided, the default
is used. The default value is CUSTOM_ROWS for the mode parameter and 20,000 for the
size parameter.

Type: [JobSample](API_JobSample.md "API_JobSample.md") object

Required: No

**LogGroupName**

The name of an Amazon CloudWatch log group, where the job writes diagnostic messages
when it runs.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 512.

Required: No

**LogSubscription**

The current status of Amazon CloudWatch logging for the job run.

Type: String

Valid Values: `ENABLE | DISABLE`

Required: No

**Outputs**

One or more output artifacts from a job run.

Type: Array of [Output](API_Output.md "API_Output.md") objects

Array Members: Minimum number of 1 item.

Required: No

**RecipeReference**

The set of steps processed by the job.

Type: [RecipeReference](API_RecipeReference.md "API_RecipeReference.md") object

Required: No

**RunId**

The unique identifier of the job run.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

Required: No

**StartedBy**

The Amazon Resource Name (ARN) of the user who initiated the job run.

Type: String

Required: No

**StartedOn**

The date and time when the job run began.

Type: Timestamp

Required: No

**State**

The current state of the job run entity itself.

Type: String

Valid Values: `STARTING | RUNNING | STOPPING | STOPPED | SUCCEEDED | FAILED | TIMEOUT`

Required: No

**ValidationConfigurations**

List of validation configurations that are applied to the profile job run.

Type: Array of [ValidationConfiguration](API_ValidationConfiguration.md "API_ValidationConfiguration.md") objects

Array Members: Minimum number of 1 item.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/databrew-2017-07-25/JobRun.md "../../../goto/SdkForCpp/databrew-2017-07-25/JobRun.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/databrew-2017-07-25/JobRun.md "../../../goto/SdkForJavaV2/databrew-2017-07-25/JobRun.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/databrew-2017-07-25/JobRun.md "../../../goto/SdkForRubyV3/databrew-2017-07-25/JobRun.md")
