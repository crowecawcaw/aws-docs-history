# ContinueUpdateRollback

Continues rolling back a stack from `UPDATE_ROLLBACK_FAILED` to
 `UPDATE_ROLLBACK_COMPLETE` state. Depending on the cause of the failure, you can
 manually fix the error and continue the rollback. By continuing the rollback, you can return
 your stack to a working state (the `UPDATE_ROLLBACK_COMPLETE` state) and then try
 to update the stack again.

A stack enters the `UPDATE_ROLLBACK_FAILED` state when CloudFormation can't roll
 back all changes after a failed stack update. For example, this might occur when a stack
 attempts to roll back to an old database that was deleted outside of CloudFormation. Because
 CloudFormation doesn't know the instance was deleted, it assumes the instance still exists and
 attempts to roll back to it, causing the update rollback to fail.

For more information, see [Continue rolling back an update](../UserGuide/using-cfn-updating-stacks-continueupdaterollback.md "../UserGuide/using-cfn-updating-stacks-continueupdaterollback.md") in the *AWS CloudFormation User Guide*. For
 information for troubleshooting a failed update rollback, see [Update rollback failed](../UserGuide/troubleshooting.md#troubleshooting-errors-update-rollback-failed "../UserGuide/troubleshooting.md#troubleshooting-errors-update-rollback-failed").


## Request Parameters


 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").





**ClientRequestToken** 


A unique identifier for this `ContinueUpdateRollback` request. Specify this
 token if you plan to retry requests so that CloudFormation knows that you're not attempting to
 continue the rollback to a stack with the same name. You might retry
 `ContinueUpdateRollback` requests to ensure that CloudFormation successfully received
 them.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 128.


Pattern: `[a-zA-Z0-9][-a-zA-Z0-9]*`



Required: No




**ResourcesToSkip.member.N**


A list of the logical IDs of the resources that CloudFormation skips during the continue
 update rollback operation. You can specify only resources that are in the
 `UPDATE_FAILED` state because a rollback failed. You can't specify resources that
 are in the `UPDATE_FAILED` state for other reasons, for example, because an update
 was canceled. To check why a resource update failed, use the [DescribeStackResources](API_DescribeStackResources.md "API_DescribeStackResources.md") action, and view the resource status reason.


###### Important

Specify this property to skip rolling back resources that CloudFormation can't successfully
 roll back. We recommend that you  [troubleshoot](../UserGuide/troubleshooting.md#troubleshooting-errors-update-rollback-failed "../UserGuide/troubleshooting.md#troubleshooting-errors-update-rollback-failed") resources before skipping them. CloudFormation sets the status of the
 specified resources to `UPDATE_COMPLETE` and continues to roll back the stack.
 After the rollback is complete, the state of the skipped resources will be inconsistent with
 the state of the resources in the stack template. Before performing another stack update,
 you must update the stack or resources to be consistent with each other. If you don't,
 subsequent stack updates might fail, and the stack will become unrecoverable.


Specify the minimum number of resources required to successfully roll back your stack. For
 example, a failed resource update might cause dependent resources to fail. In this case, it
 might not be necessary to skip the dependent resources.


To skip resources that are part of nested stacks, use the following format:
 `NestedStackName.ResourceLogicalID`. If you want to specify the logical ID of a
 stack resource (`Type: AWS::CloudFormation::Stack`) in the
 `ResourcesToSkip` list, then its corresponding embedded stack must be in one of
 the following states: `DELETE_IN_PROGRESS`, `DELETE_COMPLETE`, or
 `DELETE_FAILED`.


###### Note

Don't confuse a child stack's name with its corresponding logical ID defined in the
 parent stack. For an example of a continue update rollback operation with nested stacks, see
 [Continue rolling back from failed nested stack updates](../UserGuide/using-cfn-updating-stacks-continueupdaterollback.md#nested-stacks "../UserGuide/using-cfn-updating-stacks-continueupdaterollback.md#nested-stacks").


Type: Array of strings


Pattern: `[a-zA-Z0-9]+|[a-zA-Z][-a-zA-Z0-9]*\.[a-zA-Z0-9]+`



Required: No




**RoleARN** 


The Amazon Resource Name (ARN) of an IAM role that CloudFormation assumes to roll back the
 stack. CloudFormation uses the role's credentials to make calls on your behalf. CloudFormation always
 uses this role for all future operations on the stack. Provided that users have permission to
 operate on the stack, CloudFormation uses this role even if the users don't have permission to
 pass it. Ensure that the role grants least permission.


If you don't specify a value, CloudFormation uses the role that was previously associated with
 the stack. If no role is available, CloudFormation uses a temporary session that's generated from
 your user credentials.


Type: String


Length Constraints: Minimum length of 20. Maximum length of 2048.


Required: No




**StackName** 


The name or the unique ID of the stack that you want to continue rolling back.


###### Note

Don't specify the name of a nested stack (a stack that was created by using the
 `AWS::CloudFormation::Stack` resource). Instead, use this operation on the
 parent stack (the stack that contains the `AWS::CloudFormation::Stack`
 resource).


Type: String


Length Constraints: Minimum length of 1.


Pattern: `([a-zA-Z][-a-zA-Z0-9]*)|(arn:\b(aws|aws-us-gov|aws-cn)\b:[-a-zA-Z0-9:/._+]*)`



Required: Yes




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**TokenAlreadyExists** 


A client request token already exists.


HTTP Status Code: 400




## Examples


### ContinueUpdateRollback


This example illustrates one usage of ContinueUpdateRollback.


#### Sample Request



```

https://cloudformation.us-east-1.amazonaws.com/
 ?Action=ContinueUpdateRollback
 &StackName=MyUpdatRollbackFailedStack
 &Version=2010-05-15
 &SignatureVersion=2
 &Timestamp=2010-07-27T22%3A26%3A28.000Z
 &AWSAccessKeyId=[AWS Access KeyID]
 &Signature=[Signature]
```

#### Sample Response



```

<ContinueUpdateRollbackResponse xmlns="http://cloudformation.amazonaws.com/doc/2010-05-15/">
  <ResponseMetadata>
    <RequestId>5ccc7dcd-744c-11e5-be70-1b08c228efb3</RequestId>
  </ResponseMetadata>
</ContinueUpdateRollbackResponse>
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/ContinueUpdateRollback "https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/ContinueUpdateRollback")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/ContinueUpdateRollback "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/ContinueUpdateRollback")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/ContinueUpdateRollback "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/ContinueUpdateRollback")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/ContinueUpdateRollback "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/ContinueUpdateRollback")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/ContinueUpdateRollback "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/ContinueUpdateRollback")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/ContinueUpdateRollback "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/ContinueUpdateRollback")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/ContinueUpdateRollback "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/ContinueUpdateRollback")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/ContinueUpdateRollback "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/ContinueUpdateRollback")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/ContinueUpdateRollback "https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/ContinueUpdateRollback")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/ContinueUpdateRollback "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/ContinueUpdateRollback")
