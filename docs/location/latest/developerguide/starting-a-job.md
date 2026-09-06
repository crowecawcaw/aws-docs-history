

# Start a job
<a name="starting-a-job"></a>

Submit a `StartJob` request with your job configuration. Specify the action you want to perform, provide your execution role ARN, and configure input and output options with your Amazon S3 bucket locations.

Some action types support optional additional features that enhance the results. The available features depend on the action type. For address validation additional features, see [Address validation features](address-validation-concepts.md#address-validation-features).

Provide a meaningful job name to help identify the job in monitoring and management operations. Consider including timestamps or batch identifiers in job names for easier tracking.

## Address validation examples
<a name="start-job-examples"></a>

The following examples show how to start an address validation job. Use these as a reference for the request structure.

### Start an asynchronous address validation job
<a name="start-address-validation-example"></a>

------
#### [ Sample request ]

```
{
   "Action": "ValidateAddress",
   "Name": "MyFirstValidationJob",
   "ExecutionRoleArn": "arn:aws:iam::{{YOUR_ACCOUNT_ID}}:role/LocationServiceJobExecutionRole",
   "InputOptions": {
       "Location": "arn:aws:s3:::{{YOUR_INPUT_BUCKET_NAME}}",
       "Format": "Parquet"
   },
   "OutputOptions": {
       "Location": "arn:aws:s3:::{{YOUR_OUTPUT_BUCKET_NAME}}",
       "Format": "Parquet"
   }
}
```

------
#### [ Sample response ]

```
{
   "CreatedAt": "2024-01-01T00:00:00Z",
   "JobArn": "arn:aws:geo:us-west-2:{{YOUR_ACCOUNT_ID}}:job/MyFirstValidationJob-12345678-abcd-1234-5678-abcdef123456",
   "JobId": "MyFirstValidationJob-12345678-abcd-1234-5678-abcdef123456",
   "Status": "Pending"
}
```

------
#### [ AWS CLI ]

```
aws location start-job \
  --action ValidateAddress \
  --execution-role-arn "arn:aws:iam::{{YOUR_ACCOUNT_ID}}:role/LocationServiceJobExecutionRole" \
  --input-options Location=arn:aws:s3:::{{YOUR_INPUT_BUCKET}},Format=Parquet \
  --name "MyFirstCLIJob" \
  --output-options Location=arn:aws:s3:::{{YOUR_OUTPUT_BUCKET}},Format=Parquet \
  --region us-west-2
```

------

### Start a job with additional features
<a name="start-job-with-features-example"></a>

The following example includes the `Position` and `CountrySpecificAttributes` additional features:

------
#### [ Sample request ]

```
{
   "Action": "ValidateAddress",
   "Name": "ValidationJobWithFeatures",
   "ExecutionRoleArn": "arn:aws:iam::{{YOUR_ACCOUNT_ID}}:role/LocationServiceJobExecutionRole",
   "InputOptions": {
       "Location": "arn:aws:s3:::{{YOUR_INPUT_BUCKET_NAME}}",
       "Format": "Parquet"
   },
   "OutputOptions": {
       "Location": "arn:aws:s3:::{{YOUR_OUTPUT_BUCKET_NAME}}",
       "Format": "Parquet"
   },
   "ActionOptions": {
       "ValidateAddress": {
           "AdditionalFeatures": [
               "Position",
               "CountrySpecificAttributes"
           ]
       }
   }
}
```

------
#### [ AWS CLI ]

```
aws location start-job \
  --action ValidateAddress \
  --execution-role-arn "arn:aws:iam::{{YOUR_ACCOUNT_ID}}:role/LocationServiceJobExecutionRole" \
  --input-options Location=arn:aws:s3:::{{YOUR_INPUT_BUCKET}},Format=Parquet \
  --name "ValidationJobWithFeatures" \
  --output-options Location=arn:aws:s3:::{{YOUR_OUTPUT_BUCKET}},Format=Parquet \
  --action-options '{"ValidateAddress":{"AdditionalFeatures":["Position","CountrySpecificAttributes"]}}' \
  --region us-west-2
```

------