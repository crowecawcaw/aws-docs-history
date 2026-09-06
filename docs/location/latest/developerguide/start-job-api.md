

# StartJob
<a name="start-job-api"></a>

The `StartJob` operation initiates a new Amazon Location data processing job. You specify the action type, input and output Amazon S3 locations, and an IAM execution role that grants the service access to your buckets. The operation returns a job identifier, Amazon Resource Name (ARN), and initial status that you can use to monitor job progress.

You can request additional features using the `ActionOptions` parameter in `StartJob` requests. These features provide enhanced options for data processing and results.

For `ValidateAddress` jobs, the **Position** feature includes latitude and longitude coordinates in [World Geodetic System (WGS 84)](https://earth-info.nga.mil/index.php?dir=wgs84&action=wgs84) format. **CountrySpecificAttributes** includes additional data specific to each country, such as carrier route information, census data, and postal identifiers.

For more information, see [StartJob](https://docs.aws.amazon.com/location/latest/APIReference/API_geojobs_StartJob.html) in the *Amazon Location Service API Reference*.

For example requests, responses, and CLI commands for this API, see [How to start a job](https://docs.aws.amazon.com/location/latest/developerguide/starting-a-job.html).

## Use cases
<a name="start-job-use-cases"></a>
+ **Data migration and system consolidation:** Clean and standardize large volumes of address data when migrating between systems or consolidating multiple data sources into a unified database.
+ **Marketing campaign preparation:** Validate customer address databases before launching direct mail campaigns to reduce returned mail costs and improve delivery success rates.
+ **Database maintenance and compliance:** Regularly validate existing customer address databases to maintain data quality standards and meet shipping and logistics compliance requirements.

## Understand the request
<a name="start-job-request-parameters"></a>

The `StartJob` request requires configuration details that specify the job action, data locations, and permissions. This configuration determines how your data is processed and where results are stored.

The request includes the following parameters:

**Job action and permissions**  
Required parameters that define the operation type and access permissions.  
+ `Action`: The type of operation to perform. Currently only `ValidateAddress` is supported.
+ `ExecutionRoleArn`: IAM role ARN that Amazon Location assumes to access your Amazon S3 buckets during job execution.

**Input configuration**  
Required parameters that specify where to read input data and its format.  
+ `InputOptions`: Object containing input data configuration.
  + `Location`: Amazon S3 ARN or URI where input files are stored.
  + `Format`: Input data format. Currently only `Parquet` is supported.

**Output configuration**  
Required parameters that specify where to write results and their format.  
+ `OutputOptions`: Object containing output data configuration.
  + `Location`: Amazon S3 ARN or URI where output files are written.
  + `Format`: Output data format. Currently only `Parquet` is supported.

**Optional parameters**  
Parameters that provide additional job configuration and features.  
+ `Name`: Human-readable job name for easier identification. Must be 1-100 characters matching pattern `[-._\w]+`.
+ `ClientToken`: Idempotency token to ensure the same job is not created multiple times. Must be 1-64 characters matching pattern `^[!-~]+$`.
+ `ActionOptions`: Object containing additional features for the specified action.
  + `ValidateAddress`: Object containing options specific to address validation.
    + `AdditionalFeatures`: Array of feature names to include in results. Valid values:
      + `Position`: Includes latitude and longitude in [WGS 84](https://earth-info.nga.mil/index.php?dir=wgs84&action=wgs84) format for each validated address.
      + `CountrySpecificAttributes`: Includes additional data specific to each country, such as carrier route information, census data, and postal identifiers.

## Understand the response
<a name="start-job-response-details"></a>

The `StartJob` response provides essential information for monitoring and managing the newly created job. Use these values to track job progress and retrieve results when processing completes.

The response includes the following fields:

**Job identification**  
Unique identifiers for the created job.  
+ `JobId`: Unique job identifier used for monitoring and management operations.
+ `JobArn`: ARN that uniquely identifies the job within AWS.

**Job status and timing**  
Initial status and creation timestamp.  
+ `Status`: Initial job status. Always `Pending` for newly created jobs.
+ `CreatedAt`: Job creation timestamp in ISO 8601 format.