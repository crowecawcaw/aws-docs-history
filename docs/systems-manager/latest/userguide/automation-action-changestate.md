

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# `aws:changeInstanceState` – Change or assert instance state
<a name="automation-action-changestate"></a>

Changes or asserts the state of the instance.

This action can be used in assert mode (doesn't run the API to change the state but verifies the instance is in the desired state.) To use assert mode, set the `CheckStateOnly` parameter to true. This mode is useful when running the Sysprep command on Windows Server, which is an asynchronous command that can run in the background for a long time. You can make sure that the instance is stopped before you create an Amazon Machine Image (AMI).

**Note**  
The default timeout value for this action is 3600 seconds (one hour). You can limit or extend the timeout by specifying the `timeoutSeconds` parameter for an `aws:changeInstanceState` step.

**Note**  
The `aws:changeInstanceState` action supports automatic throttling retry. For more information, see [Configuring automatic retry for throttled operations](automation-throttling-retry.md).

**Input**

------
#### [ YAML ]

```
name: startMyInstance
action: aws:changeInstanceState
maxAttempts: 3
timeoutSeconds: 3600
onFailure: Abort
inputs:
  InstanceIds:
  - i-1234567890abcdef0
  CheckStateOnly: true
  DesiredState: running
  FailOnUnexpectedStopped: true
```

------
#### [ JSON ]

```
{
    "name":"startMyInstance",
    "action": "aws:changeInstanceState",
    "maxAttempts": 3,
    "timeoutSeconds": 3600,
    "onFailure": "Abort",
    "inputs": {
        "InstanceIds": ["i-1234567890abcdef0"],
        "CheckStateOnly": true,
        "DesiredState": "running",
        "FailOnUnexpectedStopped": true
    }
}
```

------

InstanceIds  
The IDs of the instances.  
Type: StringList  
Required: Yes

CheckStateOnly  
If false, sets the instance state to the desired state. If true, asserts the desired state using polling.  
Default: `false`  
Type: Boolean  
Required: No

DesiredState  
The desired state. When set to `running`, this action waits for the Amazon EC2 state to be `Running`, the Instance Status to be `OK`, and the System Status to be `OK` before completing.  
Type: String  
Valid values: `running` \| `stopped` \| `terminated`  
Required: Yes

Force  
If set, forces the instances to stop. The instances don't have an opportunity to flush file system caches or file system metadata. If you use this option, you must perform file system check and repair procedures. This option isn't recommended for EC2 instances for Windows Server.  
Type: Boolean  
Required: No

FailOnUnexpectedStopped  
If set to true, the automation step fails when an instance transitions to the stopped state during a start operation. This is useful for detecting cases where an instance fails to start successfully, such as when an instance has an encrypted EBS volume but lacks the required KMS key permissions.  
Type: Boolean  
Required: No

AdditionalInfo  
Reserved.  
Type: String  
Required: No

**Output**  
None