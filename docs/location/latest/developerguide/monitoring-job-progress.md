

# Monitor job progress
<a name="monitoring-job-progress"></a>

Use the `GetJob` operation to check job status periodically. Jobs typically progress from **Pending** to **Running** to **Completed**, though processing time varies based on the number of addresses and requested features.

Monitor the job status field to determine when processing is complete. The **Completed** status indicates successful processing with results available in your output bucket. The **Failed** status indicates an error occurred, with details available in the job response.

Consider implementing Amazon EventBridge integration to receive automatic notifications of job status changes rather than polling the API continuously.

## Examples
<a name="monitor-job-status-examples"></a>

### Monitor the status of an existing address validation job
<a name="monitor-job"></a>

------
#### [ Sample request ]

```
{  
    "JobId": "{{YOUR_JOB_ID}}"
}
```

------
#### [ Sample response ]

```
{
    "Action": "ValidateAddress",
    "CreatedAt": "2023-01-01T00:00:00Z",
    "EndedAt": "2023-01-01T01:00:00Z",
    "ExecutionRoleArn": "arn:aws:iam::{{YOUR_ACCOUNT_ID}}:role/LocationServiceJobExecutionRole",
    "InputOptions": {
        "Location": "arn:aws:s3:::{{YOUR_INPUT_BUCKET}}",
        "Format": "Parquet"
    },
    "JobArn": "arn:aws:geo:us-west-2:{{YOUR_ACCOUNT_ID}}:job/{{YOUR_JOB_ID}}",
    "JobId": "{{YOUR_JOB_ID}}",
    "Name": "MyFirstValidationJob",
    "OutputOptions": {
        "Format": "Parquet",
        "Location": "arn:aws:s3:::{{YOUR_OUTPUT_BUCKET}}"
    },
    "Status": "Completed",
    "UpdatedAt": "2023-01-01T01:00:00Z",
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
aws location get-job --job-id "{{YOUR_JOB_ID}}" --region us-west-2
```

------