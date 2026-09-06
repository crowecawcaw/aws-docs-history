

# Amazon Location Jobs
<a name="jobs"></a>

Amazon Location Jobs provides asynchronous bulk processing capabilities that enable you to perform actions on large batches of location data efficiently and cost-effectively. Instead of making multiple API calls to perform the same action on each data entry individually, you can process thousands of actions on large batches of data in a single operation using the Jobs API.

Amazon Location Jobs currently supports address validation as a job action type. For details about address validation capabilities, see [Address validation](address-validation-concepts.md).

## Features
<a name="jobs-features"></a>

**Bulk processing**  
Process thousands of records in a single job operation rather than making individual API calls for each record.

**Asynchronous operations**  
Submit jobs and monitor their progress while they run in the background, freeing your application to perform other tasks.

**Amazon S3 integration**  
Seamlessly integrate with Amazon S3 for both input data storage and output result delivery using [Apache Parquet](https://parquet.apache.org/docs/overview/) format.

**Event notifications**  
Receive real-time updates about job status changes through Amazon EventBridge integration.

## Use cases
<a name="jobs-use-cases"></a>

Amazon Location Jobs supports various use cases depending on the action type. Each action type addresses different bulk processing needs for location data.

For address validation use cases, see [Address validation use cases](address-validation-concepts.md#address-validation-use-cases).

## Jobs APIs overview
<a name="jobs-apis"></a>

The Jobs API provides four core operations for managing bulk processing workflows:


| API name | Description | Additional resources | 
| --- | --- | --- | 
| StartJob | Initiates a new job with specified input and output configurations. | [StartJob](start-job-api.md) | 
| GetJob | Retrieves detailed information about a specific job, including current status, configuration, and processing results. | [GetJob](get-job-api.md) | 
| CancelJob | Cancels a running or pending job when processing is no longer needed. | [CancelJob](cancel-job-api.md) | 
| ListJobs | Retrieves a list of jobs with optional filtering and pagination support for job management. | [ListJobs](list-jobs-api.md) | 