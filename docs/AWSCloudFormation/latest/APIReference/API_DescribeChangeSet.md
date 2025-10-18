# DescribeChangeSet

Returns the inputs for the change set and a list of changes that CloudFormation will make if
 you execute the change set. For more information, see [Update
 CloudFormation stacks using change sets](../UserGuide/using-cfn-updating-stacks-changesets.md "../UserGuide/using-cfn-updating-stacks-changesets.md") in the
 *AWS CloudFormation User Guide*.


## Request Parameters


 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").





**ChangeSetName** 


The name or Amazon Resource Name (ARN) of the change set that you want to describe.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1600.


Pattern: `[a-zA-Z][-a-zA-Z0-9]*|arn:[-a-zA-Z0-9:/]*`



Required: Yes




**IncludePropertyValues** 


If `true`, the returned changes include detailed changes in the property
 values.


Type: Boolean


Required: No




**NextToken** 


A string (provided by the [DescribeChangeSet](API_DescribeChangeSet.md "API_DescribeChangeSet.md") response output) that
 identifies the next page of information that you want to retrieve.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: No




**StackName** 


If you specified the name of a change set, specify the stack name or ID (ARN) of the
 change set you want to describe.


Type: String


Length Constraints: Minimum length of 1.


Pattern: `([a-zA-Z][-a-zA-Z0-9]*)|(arn:\b(aws|aws-us-gov|aws-cn)\b:[-a-zA-Z0-9:/._+]*)`



Required: No




## Response Elements


The following elements are returned by the service.





**Capabilities.member.N**


If you execute the change set, the list of capabilities that were explicitly acknowledged
 when the change set was created.


Type: Array of strings


Valid Values: `CAPABILITY_IAM | CAPABILITY_NAMED_IAM | CAPABILITY_AUTO_EXPAND`





**Changes.member.N**


A list of `Change` structures that describes the resources CloudFormation changes
 if you execute the change set.


Type: Array of [Change](API_Change.md "API_Change.md") objects




**ChangeSetId** 


The Amazon Resource Name (ARN) of the change set.


Type: String


Length Constraints: Minimum length of 1.


Pattern: `arn:[-a-zA-Z0-9:/]*`





**ChangeSetName** 


The name of the change set.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 128.


Pattern: `[a-zA-Z][-a-zA-Z0-9]*`





**CreationTime** 


The start time when the change set was created, in UTC.


Type: Timestamp




**Description** 


Information about the change set.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.




**ExecutionStatus** 


If the change set execution status is `AVAILABLE`, you can execute the change
 set. If you can't execute the change set, the status indicates why. For example, a change set
 might be in an `UNAVAILABLE` state because CloudFormation is still creating it or in an
 `OBSOLETE` state because the stack was already updated.


Type: String


Valid Values: `UNAVAILABLE | AVAILABLE | EXECUTE_IN_PROGRESS | EXECUTE_COMPLETE | EXECUTE_FAILED | OBSOLETE`





**ImportExistingResources** 


Indicates if the change set imports resources that already exist.


###### Note

This parameter can only import resources that have [custom
 names](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-name.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-name.html") in templates. To import resources that do not accept custom names, such as
 EC2 instances, use the [resource import](../UserGuide/resource-import.md "../UserGuide/resource-import.md")
 feature instead.


Type: Boolean




**IncludeNestedStacks** 


Verifies if `IncludeNestedStacks` is set to `True`.


Type: Boolean




**NextToken** 


If the output exceeds 1 MB, a string that identifies the next page of changes. If there is
 no additional page, this value is null.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.




**NotificationARNs.member.N**


The ARNs of the Amazon SNS topics that will be associated with the stack if you execute the
 change set.


Type: Array of strings


Array Members: Maximum number of 5 items.




**OnStackFailure** 


Determines what action will be taken if stack creation fails. When this parameter is
 specified, the `DisableRollback` parameter to the [ExecuteChangeSet](API_ExecuteChangeSet.md "API_ExecuteChangeSet.md") API operation must not be specified. This must be one of these
 values:



* `DELETE` - Deletes the change set if the stack creation fails. This is only
 valid when the `ChangeSetType` parameter is set to `CREATE`. If the
 deletion of the stack fails, the status of the stack is `DELETE_FAILED`.
* `DO_NOTHING` - if the stack creation fails, do nothing. This is equivalent
 to specifying `true` for the `DisableRollback` parameter to the
 [ExecuteChangeSet](API_ExecuteChangeSet.md "API_ExecuteChangeSet.md") API operation.
* `ROLLBACK` - if the stack creation fails, roll back the stack. This is
 equivalent to specifying `false` for the `DisableRollback` parameter
 to the [ExecuteChangeSet](API_ExecuteChangeSet.md "API_ExecuteChangeSet.md") API operation.

Type: String


Valid Values: `DO_NOTHING | ROLLBACK | DELETE`





**Parameters.member.N**


A list of `Parameter` structures that describes the input parameters and their
 values used to create the change set. For more information, see the [Parameter](API_Parameter.md "API_Parameter.md") data type.


Type: Array of [Parameter](API_Parameter.md "API_Parameter.md") objects




**ParentChangeSetId** 


Specifies the change set ID of the parent change set in the current nested change set
 hierarchy.


Type: String


Length Constraints: Minimum length of 1.


Pattern: `arn:[-a-zA-Z0-9:/]*`





**RollbackConfiguration** 


The rollback triggers for CloudFormation to monitor during stack creation and updating
 operations, and for the specified monitoring period afterwards.


Type: [RollbackConfiguration](API_RollbackConfiguration.md "API_RollbackConfiguration.md") object




**RootChangeSetId** 


Specifies the change set ID of the root change set in the current nested change set
 hierarchy.


Type: String


Length Constraints: Minimum length of 1.


Pattern: `arn:[-a-zA-Z0-9:/]*`





**StackId** 


The Amazon Resource Name (ARN) of the stack that's associated with the change set.


Type: String




**StackName** 


The name of the stack that's associated with the change set.


Type: String




**Status** 


The current status of the change set, such as `CREATE_PENDING`,
 `CREATE_COMPLETE`, or `FAILED`.


Type: String


Valid Values: `CREATE_PENDING | CREATE_IN_PROGRESS | CREATE_COMPLETE | DELETE_PENDING | DELETE_IN_PROGRESS | DELETE_COMPLETE | DELETE_FAILED | FAILED`





**StatusReason** 


A description of the change set's status. For example, if your attempt to create a change
 set failed, CloudFormation shows the error message.


Type: String




**Tags.member.N**


If you execute the change set, the tags that will be associated with the stack.


Type: Array of [Tag](API_Tag.md "API_Tag.md") objects


Array Members: Maximum number of 50 items.




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**ChangeSetNotFound** 


The specified change set name or ID doesn't exit. To view valid change sets for a stack, use the
 `ListChangeSets` operation.


HTTP Status Code: 404




## Examples


### DescribeChangeSet


This example illustrates one usage of DescribeChangeSet.


#### Sample Request



```

https://cloudformation.us-east-1.amazonaws.com/
 ?Action=DescribeChangeSet
 &ChangeSetName=arn:aws:cloudformation:us-east-1:123456789012:changeSet/SampleChangeSet/12a3b456-0e10-4ce0-9052-5d484a8c4e5b
 &Version=2010-05-15
 &X-Amz-Algorithm=AWS4-HMAC-SHA256
 &X-Amz-Credential=[Access key ID and scope]
 &X-Amz-Date=20160316T233349Z
 &X-Amz-SignedHeaders=content-type;host
 &X-Amz-Signature=[Signature]
```

#### Sample Response



```

<DescribeChangeSetResponse xmlns="http://cloudformation.amazonaws.com/doc/2010-05-15/">
  <DescribeChangeSetResult>
    <StackId>arn:aws:cloudformation:us-east-1:123456789012:stack/SampleStack/12a3b456-0e10-4ce0-9052-5d484a8c4e5b</StackId>
    <Status>CREATE_COMPLETE</Status>
    <ChangeSetId>arn:aws:cloudformation:us-east-1:123456789012:changeSet/SampleChangeSet-direct/12a3b456-0e10-4ce0-9052-5d484a8c4e5b</ChangeSetId>
    <StackName>SampleStack</StackName>
    <ChangeSetName>SampleChangeSet-direct</ChangeSetName>
    <NotificationARNs/>
    <CreationTime>2016-03-17T23:35:25.813Z</CreationTime>
    <Capabilities/>
    <Parameters>
      <member>
        <ParameterValue>testing</ParameterValue>
        <ParameterKey>Purpose</ParameterKey>
      </member>
      <member>
        <ParameterValue>MyKeyName</ParameterValue>
        <ParameterKey>KeyPairName</ParameterKey>
      </member>
      <member>
        <ParameterValue>t2.micro</ParameterValue>
        <ParameterKey>InstanceType</ParameterKey>
      </member>
    </Parameters>
    <Changes>
      <member>
        <ResourceChange>
          <Replacement>False</Replacement>
          <Scope>
            <member>Tags</member>
          </Scope>
          <Details>
            <member><ChangeSource>DirectModification</ChangeSource>
              <Target>
                <RequiresRecreation>Never</RequiresRecreation>
                <Attribute>Tags</Attribute>
              </Target>
              <Evaluation>Static</Evaluation>
            </member>
          </Details>
          <LogicalResourceId>MyEC2Instance</LogicalResourceId>
          <Action>Modify</Action>
          <PhysicalResourceId>i-1abc23d4</PhysicalResourceId>
          <ResourceType>AWS::EC2::Instance</ResourceType>
        </ResourceChange>
        <Type>Resource</Type>
      </member>
    </Changes>
  </DescribeChangeSetResult>
  <ResponseMetadata>
    <RequestId>b9b4b068-3a41-11e5-94eb-example</RequestId>
  </ResponseMetadata>
</DescribeChangeSetResponse>
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/DescribeChangeSet "https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/DescribeChangeSet")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/DescribeChangeSet "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/DescribeChangeSet")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/DescribeChangeSet "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/DescribeChangeSet")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/DescribeChangeSet "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/DescribeChangeSet")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/DescribeChangeSet "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/DescribeChangeSet")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/DescribeChangeSet "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/DescribeChangeSet")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/DescribeChangeSet "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/DescribeChangeSet")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/DescribeChangeSet "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/DescribeChangeSet")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/DescribeChangeSet "https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/DescribeChangeSet")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/DescribeChangeSet "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/DescribeChangeSet")
