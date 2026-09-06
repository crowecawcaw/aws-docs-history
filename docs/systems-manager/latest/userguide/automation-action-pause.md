

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# `aws:pause` – Pause an automation
<a name="automation-action-pause"></a>

This action pauses the automation. Once paused, the automation status is *Waiting*. To continue the automation, use the [SendAutomationSignal](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_SendAutomationSignal.html) API operation with the `Resume` signal type. We recommend using the `aws:sleep` or `aws:approve` action for more granular control of your workflows.

**Note**  
The default timeout for this action is 7 days (604800 seconds) and the maximum value is 30 days (2592000 seconds). You can limit or extend the timeout by specifying the `timeoutSeconds` parameter for an `aws:pause` step.

**Input**  
The input is as follows.

------
#### [ YAML ]

```
name: pauseThis
action: aws:pause
timeoutSeconds: 1209600
inputs: {}
```

------
#### [ JSON ]

```
{
    "name": "pauseThis",
    "action": "aws:pause",
    "timeoutSeconds": "1209600",
    "inputs": {}
}
```

------Output

None  
