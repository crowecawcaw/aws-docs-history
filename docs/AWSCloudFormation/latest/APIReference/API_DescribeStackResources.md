# DescribeStackResources

Returns AWS resource descriptions for running and deleted stacks. If
 `StackName` is specified, all the associated resources that are part of the stack
 are returned. If `PhysicalResourceId` is specified, the associated resources of the
 stack that the resource belongs to are returned.

###### Note

Only the first 100 resources will be returned. If your stack has more resources than
 this, you should use `ListStackResources` instead.

For deleted stacks, `DescribeStackResources` returns resource information for
 up to 90 days after the stack has been deleted.

You must specify either `StackName` or `PhysicalResourceId`, but not
 both. In addition, you can specify `LogicalResourceId` to filter the returned
 result. For more information about resources, the `LogicalResourceId` and
 `PhysicalResourceId`, see the [AWS CloudFormation User Guide](../UserGuide.md "../UserGuide.md").

###### Note

A `ValidationError` is returned if you specify both `StackName`
 and `PhysicalResourceId` in the same request.


## Request Parameters


 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").





**LogicalResourceId** 


The logical name of the resource as specified in the template.


Type: String


Required: No




**PhysicalResourceId** 


The name or unique identifier that corresponds to a physical instance ID of a resource
 supported by CloudFormation.


For example, for an Amazon Elastic Compute Cloud (EC2) instance,
 `PhysicalResourceId` corresponds to the `InstanceId`. You can pass the
 EC2 `InstanceId` to `DescribeStackResources` to find which stack the
 instance belongs to and what other resources are part of the stack.


Required: Conditional. If you don't specify `PhysicalResourceId`, you must
 specify `StackName`.


Type: String


Required: No




**StackName** 


The name or the unique stack ID that is associated with the stack, which aren't always
 interchangeable:



* Running stacks: You can specify either the stack's name or its unique stack ID.
* Deleted stacks: You must specify the unique stack ID.

Required: Conditional. If you don't specify `StackName`, you must specify
 `PhysicalResourceId`.


Type: String


Required: No




## Response Elements


The following element is returned by the service.





**StackResources.member.N**


A list of `StackResource` structures.


Type: Array of [StackResource](API_StackResource.md "API_StackResource.md") objects




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").


## Examples


### DescribeStackResources


This example illustrates one usage of DescribeStackResources.


#### Sample Request



```

https://cloudformation.us-east-1.amazonaws.com/
 ?Action=DescribeStackResources
 &StackName=MyStack
 &Version=2010-05-15
 &SignatureVersion=2
 &Timestamp=2010-07-27T22%3A26%3A28.000Z
 &AWSAccessKeyId=[AWS Access KeyID]
 &Signature=[Signature]
```

#### Sample Response



```

<DescribeStackResourcesResponse xmlns="http://cloudformation.amazonaws.com/doc/2010-05-15/">
  <DescribeStackResourcesResult>
    <StackResources>
      <member>
        <StackId>arn:aws:cloudformation:us-east-1:123456789:stack/MyStack/aaf549a0-a413-11df-adb3-5081b3858e83</StackId>
        <StackName>MyStack</StackName>
        <LogicalResourceId>MyDBInstance</LogicalResourceId>
        <PhysicalResourceId>MyStack_DB1</PhysicalResourceId>
        <ResourceType>AWS::DBInstance</ResourceType>
        <Timestamp>2010-07-27T22:27:28Z</Timestamp>
        <ResourceStatus>CREATE_COMPLETE</ResourceStatus>
      </member>
      <member>
        <StackId>arn:aws:cloudformation:us-east-1:123456789:stack/MyStack/aaf549a0-a413-11df-adb3-5081b3858e83</StackId>
        <StackName>MyStack</StackName>
        <LogicalResourceId>MyAutoScalingGroup</LogicalResourceId>
        <PhysicalResourceId>MyStack_ASG1</PhysicalResourceId>
        <ResourceType>AWS::AutoScalingGroup</ResourceType>
        <Timestamp>2010-07-27T22:28:28Z</Timestamp>
        <ResourceStatus>CREATE_IN_PROGRESS</ResourceStatus>
      </member>
    </StackResources>
  </DescribeStackResourcesResult>
  <ResponseMetadata>
    <RequestId>b9b4b068-3a41-11e5-94eb-example</RequestId>
  </ResponseMetadata>
</DescribeStackResourcesResponse>
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/DescribeStackResources "https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/DescribeStackResources")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/DescribeStackResources "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/DescribeStackResources")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/DescribeStackResources "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/DescribeStackResources")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/DescribeStackResources "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/DescribeStackResources")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/DescribeStackResources "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/DescribeStackResources")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/DescribeStackResources "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/DescribeStackResources")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/DescribeStackResources "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/DescribeStackResources")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/DescribeStackResources "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/DescribeStackResources")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/DescribeStackResources "https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/DescribeStackResources")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/DescribeStackResources "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/DescribeStackResources")
