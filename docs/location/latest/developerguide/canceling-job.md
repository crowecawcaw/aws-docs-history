

# Cancel a job
<a name="canceling-job"></a>

Use the `CancelJob` operation to cancel an existing job currently in Pending or Running status. You might cancel a job if it was submitted with the wrong parameters or input data, or if you no longer need the complete results. It can take time for a job to be fully cancelled. You can use the `GetJob` action to check cancellation status. Cancelled jobs transition from **Cancelling** to **Cancelled** status when cancellation is complete.

## Examples
<a name="canceling-job-examples"></a>

### Cancel an existing address validation job
<a name="cancel-address-validation-job"></a>

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
    "JobArn": "arn:aws:geo:us-west-2:{{YOUR_ACCOUNT_ID}}:job/{{YOUR_JOB_ID}}",
    "JobId": "{{YOUR_JOB_ID}}",
    "Status": "Cancelling"
}
```

------
#### [ AWS CLI ]

```
aws location cancel-job --job-id "{{YOUR_JOB_ID}}" --region us-west-2
```

------