# Neptune ML management API errors and exceptions

All Neptune ML management API exceptions return a 400 HTTP code. After receiving
any of these exceptions, the command that generated the exception should not be
retried.

######

- **`MissingParameterException`**   –   Error message:

`Required credentials are missing. Please add IAM role to
 the cluster or pass as a parameter to this request.`

- **`InvalidParameterException`**   –   Error messages:
  - `Invalid ML instance type.`
  - `Invalid ID provided. ID can be 1-48 alphanumeric characters.`
  - `Invalid ID provided. Must contain only letters, digits, or hyphens.`
  - `Invalid ID provided. Please check whether a resource with the given ID exists.`
  - `Another resource with same ID already exists. Please use a new ID.`
  - `Failed to stop the job because it has already completed or failed.`

- **`BadRequestException`**   –   Error messages:
  - `Invalid S3 URL or incorrect S3 permissions. Please check your S3 configuration.`
  - `Provided ModelTraining job has not completed.`
  - `Provided SageMaker AI Training job has not completed.`
  - `Provided MLDataProcessing job is not completed.`
  - `Provided MLModelTraining job doesn't exist.`
  - `Provided ModelTransformJob doesn't exist.`
  - `Unable to find SageMaker AI resource. Please check your input.`
