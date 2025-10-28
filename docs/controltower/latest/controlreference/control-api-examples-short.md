# Control API examples

Each control in AWS Control Tower has a unique identifier for use with the control APIs. The
identifier for each control is shown in the **API controlIdentifier**
field, on the **Control details** page in the AWS Control Tower console. This
identifier is distinct from the **ControlID** field, which is a
classification system for controls.

###### Note

When you invoke `EnableControl` on an account or OU, the
`operationIdentifier` value is returned by means of
`ListEnabledControls` or `GetEnabledControl` even if the
enable operation fails. In the AWS Control Tower console, you can determine whether the
`EnableControl` operation was successful, by verifying that the
control is enabled on the account or OU. Programatically, you can track the status
of the `EnableControl` operation with the
`GetControlOperation` API command, by passing it the value of
`operationIdentifier` as shown in an example that follows.

## EnableControl

For more information about this API operation, see [EnableControl](../APIReference/API_EnableControl.md "../APIReference/API_EnableControl.md").

**Example input for EnableControl:**

This example shows how to specify the control you wish to enable, and activate that
control for the target OU that you identify.

```
{
   controlIdentifier: "arn:aws:controltower:us-west-2::control/AWS-GR_AUTOSCALING_LAUNCH_CONFIG_PUBLIC_IP_DISABLED",
   targetIdentifier: "arn:aws:organizations::123456789123:ou/o-kg8aXXXXXX/ou-prlj-a5kXXXXX"
}
```

**Example output for EnableControl:**

As an example of how to use this output parameter, you can pass the
**operationIdentifier** parameter as an input to the
**GetControlOperation** API, to track the status of your
**EnableControl** task.

```
{
    "operationIdentifier":"e2bXXXXX-6cab-XXXX-bde7-XX0c6fXXXXXX"
}
```

**Example CLI command:**

```
aws controltower enable-control \
--control-identifier arn:aws:controltower:us-west-2::control/AWS-GR_AUDIT_BUCKET_POLICY_CHANGES_PROHIBITED \
--target-identifier arn:aws:organizations::123456789123:ou/o-qnilXXXXXX/ou-vwxu-qqlXXXXX \
--region us-west-2
```

## DisableControl

For more information about this API operation, see [DisableControl](../APIReference/API_DisableControl.md "../APIReference/API_DisableControl.md").

**Example input for DisableControl:**

```
{
    controlIdentifier: "arn:aws:controltower:us-west-2::control/AWS-GR_AUTOSCALING_LAUNCH_CONFIG_PUBLIC_IP_DISABLED",
    targetIdentifier: "arn:aws:organizations::123456789123:ou/o-kg8aXXXXXX/ou-prlj-a5kXXXXX"
}
```

**Example output for DisableControl:**

```
{
    "operationIdentifier":"e2bXXXXX-8xai-XXXX-bde7-XX0c6fXXXXXX"
}
```

## GetControlOperation

For more information about this API operation, see [GetControlOperation](../APIReference/API_GetControlOperation.md "../APIReference/API_GetControlOperation.md").

**Example input for GetControlOperation:**

When you give an **operationIdentifier** as input, you receive a
status message as output.

```
{
    operationIdentifier: "e2bXXXXX-6cab-XXXX-bde7-XX0c6fXXXXXX"
}
```

**Example output for GetControlOperation:**

```
{
    "ControlOperationStatus":{
        "OperationType": "ENABLE_CONTROL",
        "StartTime": "2022-02-02T20:52:08.034Z",
        "Status": "IN_PROGRESS"
    }
}
```

**Example output for GetControlOperation:**

```
{
    "ControlOperationStatus": {
        "EndTime": "2022-04-28T19:36:31Z",
        "OperationType": "DISABLE_CONTROL",
        "StartTime": "2022-04-28T19:35:00Z",
        "Status": "SUCCEEDED"
    }
}
```

```
{
    "ControlOperationStatus": {
        "EndTime": "2022-04-28T19:36:31Z",
        "OperationType": "DISABLE_CONTROL",
        "StartTime": "2022-04-28T19:35:00Z",
        "Status": "FAILED",
        "StatusMessage": "AWS Control Tower cannot add the SCP because the IAM user or role does not have permission to perform the requested operation in AWS Organizations. To continue, update your access permissions for AWS Organizations. For more information, see Access Management in the IAM User Guide."
    }
}
```

## GetEnabledControl

For more information about this API operation, see [GetEnabledControl](../APIReference/API_GetEnabledControl.md "../APIReference/API_GetEnabledControl.md").

**Example for GetEnabledControl**

```
aws controltower get-enabled-control --enabled-control-identifier arn:aws:controltower:us-east-1:123456789012:enabledcontrol/49DVF3KP34ANNC57{
    "enabledControlDetails": {
        "arn": "arn:aws:controltower:us-east-1:123456789012:enabledcontrol/49DVF3KP34ANNC57",
        "controlIdentifier": "arn:aws:controltower:us-east-1::control/AWS-GR_EBS_OPTIMIZED_INSTANCE",
        "targetIdentifier": "arn:aws:organizations::123456789012:ou/o-ct7amci1en/ou-slfp-nay7ybhu",
        "targetRegions": [
            {
                "name": "eu-north-1"
            },
            {
                "name": "eu-west-2"
            }
        ],
        "statusSummary": {
            "status": "SUCCEEDED",
            "lastOperationIdentifier": "12e51344-a73a-439a-8477-fb3cd7f8b410"
        },
        "driftStatusSummary": {
            "driftStatus": "NOT_CHECKING"
        }
    }
}
```

## ListControlOperations

For more information about this API operation, see [ListControlOperations](../APIReference/API_ListControlOperations.md "../APIReference/API_ListControlOperations.md").

**Example input and output for ListControlOperations:**

```
aws controltower list-control-operations --max-items 13
```

```
{
    "controlOperations": [
        {
            "startTime": "2024-02-19T19:22:08+00:00",
            "operationType": "ENABLE_CONTROL",
            "status": "IN_PROGRESS",
            "statusMessage": "Operation is in progress.",
            "operationIdentifier": "f9f43b45-db27-44df-89d8-f9129e3632XX",
            "controlIdentifier": "arn:aws:controltower:us-west-2::control/SKIBWKYUQAAC",
            "targetIdentifier": "arn:aws:organizations::123456789012:ou/o-yy67i3pfv2/ou-slt4-8abknXXX",
            "enabledControlIdentifier": "arn:aws:controltower:us-west-2:123456789012:enabledcontrol/RWZFSHV2BBRU6JSE"
        },
        {
            "startTime": "2024-02-19T19:21:09+00:00",
            "operationType": "ENABLE_CONTROL",
            "status": "IN_PROGRESS",
            "statusMessage": "Operation is in progress."
            "operationIdentifier": "171ee0b1-e926-486e-9775-005bd244ccXX",
            "controlIdentifier": "arn:aws:controltower:us-west-2::control/PDKYAANJEWJE",
            "targetIdentifier": "arn:aws:organizations::123456789012:ou/o-yy67i3pfv2/ou-slt4-fl6miXXX",
            "enabledControlIdentifier": "arn:aws:controltower:us-west-2:123456789012:enabledcontrol/XCNJARWZFSHV6JSE"
        },
        {
            "startTime": "2024-02-19T19:20:08+00:00",
            "operationType": "DISABLE_CONTROL",
            "status": "IN_PROGRESS",
            "statusMessage": "Operation is in progress.",
            "operationIdentifier": "6345643b-3bd1-44dc-b1e5-9e9ae5df41XX",
            "controlIdentifier": "arn:aws:controltower:us-west-2::control/XAZHJTQBXMLM",
            "targetIdentifier": "arn:aws:organizations::123456789012:ou/o-yy67i3pfv2/ou-slt4-quinbXXX",
            "enabledControlIdentifier": "arn:aws:controltower:us-west-2:123456789012:enabledcontrol/NCHASYHFBJNEBFU"
        },
        {
            "startTime": "2024-02-19T19:19:12+00:00",
            "operationType": "ENABLE_CONTROL",
            "status": "IN_PROGRESS",
            "statusMessage": "Operation is in progress.",
            "operationIdentifier": "a6d26135-7234-409c-ace8-7a0020996bXX",
            "controlIdentifier": "arn:aws:controltower:us-west-2::control/ELALMJSUVZGW",
            "targetIdentifier": "arn:aws:organizations::123456789012:ou/o-yy67i3pfv2/ou-slt4-8abknXXX",
            "enabledControlIdentifier": "arn:aws:controltower:us-west-2:123456789012:enabledcontrol/ANDPATBCJALUFNXY"
        },
        {
            "startTime": "2024-02-19T19:18:08+00:00",
            "operationType": "ENABLE_CONTROL",
            "status": "IN_PROGRESS",
            "statusMessage": "Operation is in progress.",
            "operationIdentifier": "8fdd8688-e6ef-4def-9b7f-820b2393f1XX",
            "controlIdentifier": "arn:aws:controltower:us-west-2::control/LUZSILPCBBOK",
            "targetIdentifier": "arn:aws:organizations::123456789012:ou/o-yy67i3pfv2/ou-slt4-8abknXXX",
            "enabledControlIdentifier": "arn:aws:controltower:us-west-2:123456789012:enabledcontrol/RBFOAMNVHYAZBCTG"
        },
        {
            "startTime": "2024-02-19T19:17:20+00:00",
            "operationType": "DISABLE_CONTROL",
            "status": "IN_PROGRESS",
            "statusMessage": "Operation is in progress.",
            "operationIdentifier": "d01e0afc-722b-4762-bb93-afece269feXX",
            "controlIdentifier": "arn:aws:controltower:us-west-2::control/DVIYOYZQQBH",
            "targetIdentifier": "arn:aws:organizations::123456789012:ou/o-yy67i3pfv2/ou-slt4-8abknXXX",
            "enabledControlIdentifier": "arn:aws:controltower:us-west-2:123456789012:enabledcontrol/MXBDYAQPLCGATSDI"
        },
        {
            "startTime": "2024-02-19T19:16:08+00:00",
            "operationType": "ENABLE_CONTROL",
            "status": "IN_PROGRESS",
            "statusMessage": "Operation is in progress.",
            "operationIdentifier": "a2e7cc66-a937-4b76-96e5-87e6e5c4a7XX",
            "controlIdentifier": "arn:aws:controltower:us-west-2::control/EVWTVVCSKQMU",
            "targetIdentifier": "arn:aws:organizations::123456789012:ou/o-yy67i3pfv2/ou-slt4-quinbXXX",
            "enabledControlIdentifier": "arn:aws:controltower:us-west-2:123456789012:enabledcontrol/PMANDUTVCBHDKLXY"
        },
        {
            "startTime": "2024-02-19T19:15:21+00:00",
            "operationType": "ENABLE_CONTROL",
            "status": "IN_PROGRESS",
            "statusMessage": "Operation is in progress.",
            "operationIdentifier": "53718bd4-1445-417a-94fa-53c5cc0cf3XX",
            "controlIdentifier": "arn:aws:controltower:us-west-2::control/AWS-GR_EBS_OPTIMIZED_INSTANCE",
            "targetIdentifier": "arn:aws:organizations::123456789012:ou/o-yy67i3pfv2/ou-slt4-fl6miXXX",
            "enabledControlIdentifier": "arn:aws:controltower:us-west-2:123456789012:enabledcontrol/MCBAYDFGXBVAQTSP"
        },
        {
            "startTime": "2024-02-19T19:14:08+00:00",
            "operationType": "DISABLE_CONTROL",
            "status": "IN_PROGRESS",
            "statusMessage": "Operation is in progress.",
            "operationIdentifier": "33b1b0d7-508c-4159-a18c-48dd692f99XX",
            "controlIdentifier": "arn:aws:controltower:us-west-2::control/AWS-GR_EBS_SNAPSHOT_PUBLIC_RESTORABLE_CHECK",
            "targetIdentifier": "arn:aws:organizations::123456789012:ou/o-yy67i3pfv2/ou-slt4-8abknXXX",
            "enabledControlIdentifier": "arn:aws:controltower:us-west-2:123456789012:enabledcontrol/KDGCVAZNJHFKDNCO"
        },
        {
            "startTime": "2024-02-19T19:13:09+00:00",
            "operationType": "ENABLE_CONTROL",
            "status": "IN_PROGRESS",
            "statusMessage": "Operation is in progress.",
            "operationIdentifier": "2f9e3c21-fc5f-4606-b64a-a5e63814f0XX",
            "controlIdentifier": "arn:aws:controltower:us-west-2::control/AWS-GR_EC2_INSTANCE_NO_PUBLIC_IP",
            "targetIdentifier": "arn:aws:organizations::123456789012:ou/o-yy67i3pfv2/ou-slt4-quinbXXX",
            "enabledControlIdentifier": "arn:aws:controltower:us-west-2:123456789012:enabledcontrol/DSRTFJNCMLDIFTAY"
        },
        {
            "startTime": "2024-02-19T19:12:38+00:00",
            "operationType": "ENABLE_CONTROL",
            "status": "SUCCEEDED",
            "statusMessage": "Operation was successful.",
            "operationIdentifier": "d808bd59-96b0-42cc-b2fd-b5f4069adcXX",
            "controlIdentifier": "arn:aws:controltower:us-west-2::control/AWS-GR_EC2_VOLUME_INUSE_CHECK",
            "targetIdentifier": "arn:aws:organizations::123456789012:ou/o-yy67i3pfv2/ou-slt4-8abknXXX",
            "enabledControlIdentifier": "arn:aws:controltower:us-west-2:123456789012:enabledcontrol/VBYGOPDHNAGDTRWP"
        },
        {
            "startTime": "2024-02-19T19:11:08+00:00",
            "operationType": "DISABLE_CONTROL",
            "status": "SUCCEEDED",
            "statusMessage": "Operation was successful.",
            "operationIdentifier": "5decdb1e-79f7-4fe5-b1a6-b4736f1780XX",
            "controlIdentifier": "arn:aws:controltower:us-west-2::control/AWS-GR_NO_UNRESTRICTED_ROUTE_TO_IGW",
            "targetIdentifier": "arn:aws:organizations::123456789012:ou/o-yy67i3pfv2/ou-slt4-fl6miXXX",
            "enabledControlIdentifier": "arn:aws:controltower:us-west-2:123456789012:enabledcontrol/ZLPEBCHAYDGHJEYC"
        },
        {
            "startTime": "2024-02-19T19:10:11+00:00",
            "operationType": "ENABLE_CONTROL",
            "status": "FAILED",
            "statusMessage": "AWS Control Tower cannot add the SCP because the IAM user or role does not have permission to perform the requested operation in AWS Organizations. To continue, update your access permissions for AWS Organizations. For more information, see Access Management in the IAM User Guide."
            "operationIdentifier": "a2629bd6-8777-40b2-9998-5d89dd37dcXX",
            "controlIdentifier": "arn:aws:controltower:us-west-2::control/TKCJNPHIDFHI",
            "targetIdentifier": "arn:aws:organizations::123456789012:ou/o-yy67i3pfv2/ou-slt4-8abknXXX",
            "enabledControlIdentifier": "arn:aws:controltower:us-west-2:123456789012:enabledcontrol/NCBDYANCODHAZBCP"
        }
    ],
    "NextToken": "eyJuZXh0VG9rZW4iOiBudWxsLCAiYm90b190cnVuY2F0ZV9hbW91bnQiOiAxfQ=="
}
```

## ListEnabledControls

For more information about this API operation, see [ListEnabledControls](../APIReference/API_ListEnabledControls.md "../APIReference/API_ListEnabledControls.md").

**Example input for ListEnabledControls:**

This example shows how to specify the target OU as input, so you can receive a list of
controls as output.

```
{
    targetIdentifier: "arn:aws:organizations::123456789123:ou/o-kg8aXXXXXX/ou-prlj-a5kXXXXX",
    nextToken: "bde7-XX0c6fXXXXXX",
    maxResults: 2
}
```

**Example output for ListEnabledControls:**

```
{
    "enabledControls": [
        {
            "controlIdentifier": "arn:aws:controltower:us-west-2::control/AWS-GR_AUTOSCALING_LAUNCH_CONFIG_PUBLIC_IP_DISABLED"
        },
        {
            "controlIdentifier": "arn:aws:controltower:us-west-2::control/AWS-GR_RESTRICT_ROOT_USER"
        }
    ],
    "nextToken": "e2bXXXXX-6cab-XXXX"
}
```

**This example shows a larger set of returned values for ListEnabledControls.**

```
aws controltower list-enabled-controls --target-identifier arn:aws:organizations::072569612342:ou/o-yy67i3pfv2/ou-slt4-fl6mi3bd --max-items 3
{
    "enabledControls": [
        {
            "arn": "arn:aws:controltower:us-west-2::enabledcontrol/SOME_ENABLED_CONTROL",
            "controlIdentifier": "arn:aws:controltower:us-west-2::control/SOME_CONTROL",
            "targetIdentifier": "arn:aws:organizations::072569612342:ou/o-yy67i3pfv2/ou-slt4-fl6mi3bd",
            "statusSummary": {
                "status": "SUCCEEDED",
                "lastOperationIdentifier": "12e51344-a73a-439a-8477-fb3cd7f8b410"
            },
            "driftStatusSummary": {
                "driftStatus": "NOT_CHECKING"
            }
        },
        {
            "arn": "arn:aws:controltower:us-west-2::enabledcontrol/OTHER_ENABLED_CONTROL",
            "controlIdentifier": "arn:aws:controltower:us-west-2::control/OTHER_CONTROL",
            "targetIdentifier": "arn:aws:organizations::072569612342:ou/o-yy67i3pfv2/ou-slt4-fl6mi3bd",
            "statusSummary": {
                "status": "FAILED",
                "lastOperationIdentifier": "12e51344-a73a-439a-8477-fb3cd7f8b410"
            },
            "driftStatusSummary": {
                "driftStatus": "UNKNOWN"
            }
        },
        {
            "arn": "arn:aws:controltower:us-west-2::enabledcontrol/ANOTHER_ENABLED_CONTROL",
            "controlIdentifier": "arn:aws:controltower:us-west-2::control/ANOTHER_CONTROL",
            "targetIdentifier": "arn:aws:organizations::072569612342:ou/o-yy67i3pfv2/ou-slt4-fl6mi3bd",
            "statusSummary": {
                "status": "SUCCEEDED",
                "lastOperationIdentifier": "12e51344-a73a-439a-8477-fb3cd7f8b410"
            },
            "driftStatusSummary": {
                "driftStatus": "IN_SYNC"
            }
        }
    ],
    "nextToken": "eyJuZXh0VG9rZW4iOiBudWxsLCAiYm90b190cnVuY2F0ZV9hbW91bnQiOiAyfQ=="
}
```

## ListTagsForResource

For more information about this API operation, see [ListTagsForResource](../APIReference/API_ListTagsForResource.md "../APIReference/API_ListTagsForResource.md").

**Example for ListTagsForResource**

```
aws controltower list-tags-for-resource --resource-arn "arn:aws:controltower:us-east-1:123456789012:enabledcontrol/49DVF3KP34ANNC57"
{
  "TestTagKey": "TestTagValue"
}

```

## ResetEnabledControl

For more information about this API operation, see [ResetEnabledControl](../APIReference/API_ResetEnabledControl.md "../APIReference/API_ResetEnabledControl.md").

**Example for ResetEnabledControl**

```
aws controltower reset-enabled-control \
    —enabled-control-identifier arn:aws:controltower:us-east-1:01234567890:enabledcontrol/EXAMPLE_NAME
```

## TagResource

For more information about this API operation, see [TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md").

**Example for TagResource**

```
aws controltower tag-resource --resource-arn "arn:aws:controltower:us-east-1:123456789012:enabledcontrol/49DVF3KP34ANNC57"} --tags "TestTagKey=TestTagValue"
{
}

```

## UntagResource

For more information about this API operation, see [UntagResource](../APIReference/API_UntagResource.md "../APIReference/API_UntagResource.md").

**Example for UntagResource**

```
aws controltower untag-resource --resource-arn "arn:aws:controltower:us-east-1:123456789012:enabledcontrol/49DVF3KP34ANNC57" --tag-keys "TestTagKey"
{
}

```

## UpdateEnabledControl

For more information about this API operation, see [UpdateEnabledControl](../APIReference/API_UpdateEnabledControl.md "../APIReference/API_UpdateEnabledControl.md").

**Change the parameters of a control:**

```
aws controltower update-enabled-control \
    --enabled-control-identifier arn:aws:controltower:us-east-1:01234567890:enabledcontrol/EXAMPLE_NAME \
    --parameters '[{"key":"AllowedRegions","value":["us-east-1","us-west-1","us-west-2","us-east-2"]},{"key":"ExemptedPrincipalArns","value":["arn:aws:iam::*:role/ReadOnly","arn:aws:sts::*:assumed-role/ReadOnly/*"]},{"key":"ExemptedActions","value":["logs:DescribeLogGroups","logs:StartQuery","logs:GetQueryResults","cloudwatch:Get*","cloudwatch:Describe*"]}]'
```

**Here's a more readable version of parameters input:**

```
[
    {
        "key": "AllowedRegions",
        "value":
        [
            "us-east-1",
            "us-west-1",
            "us-west-2",
            "us-east-2"
        ]
    },
    {
        "key": "ExemptedPrincipalArns",
        "value":
        [
            "arn:aws:iam::*:role/ReadOnly",
            "arn:aws:sts::*:assumed-role/ReadOnly/*"
        ]
    },
    {
        "key": "ExemptedActions",
        "value":
        [
            "logs:DescribeLogGroups",
            "logs:StartQuery",
            "logs:GetQueryResults",
            "cloudwatch:Get*",
            "cloudwatch:Describe*"
        ]
    }
]
```

## View parameters

You can view the existing parameters for a control with the `GetEnabledControl` API call.

Example input:

```
aws controltower get-enabled-control --enabled-control-identifier arn:aws:controltower:us-east-1:01234567890:enabledcontrol/EXAMPLE_NAME \
```

Example output:

```
{
    "enabledControlDetails": {
        "arn": "arn:aws:controltower:us-east-1:01234567890:enabledcontrol/EXAMPLE_NAME",
        "controlIdentifier": "arn:aws:controltower:us-east-1::control/EXAMPLE_NAME",
        "targetIdentifier": "arn:aws:organizations::01234567890:ou/o-EXAMPLE/ou-zzxx-zzx0zzz2",
        ...
        ...
        ...
        "parameters": [
            {
                "key": "ExemptedPrincipalArns",
                "value": [
                    "arn:aws:iam::*:role/ReadOnly"
                ]
            },
            {
                "key": "AllowedRegions",
                "value": [
                    "us-east-1",
                    "us-west-1"
                ]
            },
            {
                "key": "ExemptedActions",
                "value": [
                    "logs:DescribeLogGroups",
                    "logs:StartQuery",
                    "logs:GetQueryResults"
                ]
            }
        ]
    }
}
```

For examples of how to work with the AWS Control Tower baseline APIs, see [Examples for baseline API usage](../userguide/baseline-api-examples.md "../userguide/baseline-api-examples.md").
