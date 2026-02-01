• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# `aws:pause` – Pause an

automation

This action pauses the automation. Once paused, the automation status is
_Waiting_. To continue the automation, use the [SendAutomationSignal](../APIReference/API_SendAutomationSignal.md "../APIReference/API_SendAutomationSignal.md") API
operation with the `Resume` signal type. We recommend using the
`aws:sleep` or `aws:approve` action for more granular control
of your workflows.

###### Note

The default timeout for this action is 7 days (604800 seconds) and the maximum
value is 30 days (2592000 seconds). You can limit or extend the timeout by
specifying the `timeoutSeconds` parameter for an `aws:pause`
step.

###### Input

The input is as follows.

YAML

```
name: pauseThis
action: aws:pause
timeoutSeconds: 1209600
inputs: {}
```

JSON

```
{
    "name": "pauseThis",
    "action": "aws:pause",
    "timeoutSeconds": "1209600",
    "inputs": {}
}
```

###### Output

None
