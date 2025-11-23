# Troubleshooting for Conformance Packs for AWS Config

Check the following issues to help troubleshoot issues you might run into when using conformance packs.

###### Topics

- [Failed status for a conformance pack](#w2aac22c41b7 "#w2aac22c41b7")
- [Dangling rules in a conformance pack](#w2aac22c41b9 "#w2aac22c41b9")

## Failed status for a conformance pack

If you get an error indicating that the conformance pack failed while creating, updating,
or deleting it, you can check the status of your conformance pack.

```
aws configservice describe-conformance-pack-status --conformance-pack-name MyConformancePack1
```

You should see output similar to the following.

```
"ConformancePackStatusDetails": [
    {
        "ConformancePackName": "`ConformancePackName`",
        "ConformancePackId": "`ConformancePackId`",
        "ConformancePackArn": "`ConformancePackArn`",
        "ConformancePackState": "CREATE_FAILED",
        "StackArn": "`CloudFormation stackArn`",
        "ConformancePackStatusReason": "`Failure Reason`",
        "LastUpdateRequestedTime": 1573865201.619,
        "LastUpdateCompletedTime": 1573864244.653
    }
]
```

Check the **ConformancePackStatusReason** for information about the
failure.

**When the stackArn is present in the response**

If the error message is not clear or if the failure is due to an internal error, go to the
CloudFormation console and do the following:

1. Search for the **stackArn** from the output.
2. Choose the **Events** tab of the CloudFormation stack and check for failed
   events.

The status reason indicates why the conformance pack failed.

**When the stackArn is not present in the response**

If you receive a failure while you create a conformance pack but the stackArn is not
present in the status response, the possible reason is that the stack creation failed and
CloudFormation rolled back and deleted the stack. Go to the CloudFormation console and search for stacks that
are in a **Deleted** state. The failed stack might be available there. The
CloudFormation stack contains the conformance pack name. If you find the failed stack, choose the
**Events** tab of the CloudFormation stack and check for failed events.

If none of these steps worked and if the failure reason is an internal service error, then
try operation again or contact the [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").

## Dangling rules in a conformance pack

Deploying a conformance pack involves the creation of an underlying AWS CloudFormation stack in the background to deploy the rules in the conformance pack template.
These rules are [service-linked rules](service-linked-awsconfig-rules.md "service-linked-awsconfig-rules.md") and cannot be updated or deleted outside the conformance pack.

If you make changes to the underlying CloudFormation stack, this results in a situation
where the conformance pack and its rules become unmanageable. These unmanageable rules are _dangling rules_.

**Drift between the CloudFormation stack and the conformance pack**

You can update the rule names in a conformance pack template directly from the CloudFormation console.
If you update the template directly from the CloudFormation console, this does not update the deployed conformance pack.

This drift creates a dangling rule. If you try to delete the rule from the conformance pack, you receive an error similiar to the following:

```
"An AWS service owns ServiceLinkedConfigRule. You do not have permissions to take action on this rule. (Service: AmazonConfig; Status Code: 400; Error Code: AccessDeniedException; Request ID: `my-request-ID`; Proxy: null)".
```

If you try to delete the conformance pack, the dangling rule cannot be deleted and you receive an error similiar to the following:

```
"User: arn:aws:sts::`111122223333`:assumed-role/AWSServiceRoleForConfigConforms/AwsConfigConformsWorkflow is not authorized to perform: config:DeleteConfigRule on resource: `my-dangling-rule`
```

To fix this issue, do the following steps:

1. Delete the stack. For more information, see [Deleting a stack on the CloudFormation console](../../../AWSCloudFormation/latest/UserGuide/cfn-console-delete-stack.md "../../../AWSCloudFormation/latest/UserGuide/cfn-console-delete-stack.md") in the _CloudFormation User Guide_.
2. Delete the conformance pack using the AWS Config console or using the [DeleteConformancePack](../APIReference/API_DeleteConformancePack.md "../APIReference/API_DeleteConformancePack.md") API.
   If it is an organizational conformance pack and you are using the management or delegated administrator account, use the [DeleteOrganizationConformancePack](../APIReference/API_DeleteOrganizationConformancePack.md "../APIReference/API_DeleteOrganizationConformancePack.md") API.
3. Reach out to the [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/") with the Amazon Resource Name (ARN) of the dangling rules in the conformance pack to help clean up your account.

To avoid this issue, remember these best practices:

- Never make any direct updates to the CloudFormation stack of a conformance pack.
- Never try and make changes which create drift between the conformance pack and its underlying CloudFormation stack.
- The [service-linked role (SLR) for conformance packs](security-iam-awsmanpol.md#security-iam-awsmanpol-ConfigConformsServiceRolePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-ConfigConformsServiceRolePolicy") cannot be modified. Make sure the resources you are updating are part of the permissions policy for the SLR.

**Deleted CloudFormation stack for a conformance pack**

Unless there is drift between the CloudFormation stack and the conformance pack, it is never recommended to delete rules in a conformance pack or its CloudFormation stack directly from the CloudFormation console.

To fix this issue, reach out to the [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/") with the Amazon Resource Name (ARN) of the dangling rules in the conformance pack to help clean up your account.

To avoid this issue, remember these best practices:

- Never delete the underlying CloudFormation stack for a conformance pack.
- Delete conformance packs using the [DeleteConformancePack](../APIReference/API_DeleteConformancePack.md "../APIReference/API_DeleteConformancePack.md") API.
  If it is an organizational conformance pack and you are using the management or delegated administrator account, use the [DeleteOrganizationConformancePack](../APIReference/API_DeleteOrganizationConformancePack.md "../APIReference/API_DeleteOrganizationConformancePack.md") API.
