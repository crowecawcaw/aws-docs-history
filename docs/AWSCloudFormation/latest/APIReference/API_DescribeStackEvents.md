# DescribeStackEvents

Returns all stack related events for a specified stack in reverse chronological order. For
 more information about a stack's event history, see [Understand CloudFormation stack creation events](../UserGuide/stack-resource-configuration-complete.md "../UserGuide/stack-resource-configuration-complete.md") in the
 *AWS CloudFormation User Guide*.

###### Note

You can list events for stacks that have failed to create or have been deleted by
 specifying the unique stack identifier (stack ID).


## Request Parameters


 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").





**NextToken** 


A string that identifies the next page of events that you want to retrieve.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: No




**StackName** 


The name or the unique stack ID that's associated with the stack, which aren't always
 interchangeable:



* Running stacks: You can specify either the stack's name or its unique stack ID.
* Deleted stacks: You must specify the unique stack ID.

Type: String


Required: Yes




## Response Elements


The following elements are returned by the service.





**NextToken** 


If the output exceeds 1 MB in size, a string that identifies the next page of events. If
 no additional page exists, this value is null.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.




**StackEvents.member.N**


A list of `StackEvents` structures.


Type: Array of [StackEvent](API_StackEvent.md "API_StackEvent.md") objects




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").


## Examples


### DescribeStackEvents


This example illustrates one usage of DescribeStackEvents.


#### Sample Request



```

            https://cloudformation.us-east-1.amazonaws.com/
 ?Action=DescribeStackEvents
 &StackName=MyStack
 &Version=2010-05-15
 &X-Amz-Algorithm=AWS4-HMAC-SHA256
 &X-Amz-Credential=[Access key ID and scope]
 &X-Amz-Date=20160316T233349Z
 &X-Amz-SignedHeaders=content-type;host
 &X-Amz-Signature=[Signature]
```

#### Sample Response



```

<DescribeStackEventsResponse xmlns="http://cloudformation.amazonaws.com/doc/2010-05-15/">
  <DescribeStackEventsResult>
    <StackEvents>
      <member>
        <Timestamp>2016-03-15T20:54:31.809Z</Timestamp>
        <ResourceStatus>CREATE_COMPLETE</ResourceStatus>
        <StackId>arn:aws:cloudformation:us-east-1:123456789012:stack/SampleStack/12a3b456-0e10-4ce0-9052-5d484a8c4e5b</StackId>
        <EventId>1dedea10-eaf0-11e5-8451-500c5242948e</EventId>
        <LogicalResourceId>SampleStack</LogicalResourceId>
        <StackName>SampleStack</StackName>
        <PhysicalResourceIdI>arn:aws:cloudformation:us-east-1:123456789012:stack/SampleStack/12a3b456-0e10-4ce0-9052-5d484a8c4e5b</PhysicalResourceId>
        <ResourceType>AWS::CloudFormation::Stack</ResourceType>
      </member>
      <member>
        <Timestamp>2016-03-15T20:54:30.174Z</Timestamp>
        <ResourceStatus>CREATE_COMPLETE</ResourceStatus>
        <StackId>arn:aws:cloudformation:us-east-1:123456789012:stack/SampleStack/12a3b456-0e10-4ce0-9052-5d484a8c4e5b</StackId>
        <EventId>MyEC2Instance-CREATE_COMPLETE-2016-03-15T20:54:30.174Z</EventId>
        <LogicalResourceId>MyEC2Instance</LogicalResourceId>
        <StackName>SampleStack</StackName>
        <PhysicalResourceId>i-1abc23d4</PhysicalResourceId>
        <ResourceProperties>{"ImageId":ami-8fcee4e5",...}</ResourceProperties>
        <ResourceType>AWS::EC2::Instance</ResourceType>
      </member>
      <member>
        <Timestamp>2016-03-15T20:53:17.660Z</Timestamp>
        <ResourceStatus>CREATE_IN_PROGRESS</ResourceStatus>
        <StackId>arn:aws:cloudformation:us-east-1:123456789012:stack/SampleStack/12a3b456-0e10-4ce0-9052-5d484a8c4e5b</StackId>
        <EventId>MyEC2Instance-CREATE_IN_PROGRESS-2016-03-15T20:53:17.660Z</EventId>
        <LogicalResourceId>MyEC2Instance</LogicalResourceId>
        <ResourceStatusReason>Resource creation Initiated</ResourceStatusReason>
        <StackName>SampleStack</StackName>
        <PhysicalResourceId>i-1abc23d4</PhysicalResourceId>
        <ResourceProperties>{"ImageId":ami-8fcee4e5",...}</ResourceProperties>
        <ResourceType>AWS::EC2::Instance</ResourceType>
      </member>
      <member>
        <Timestamp>2016-03-15T20:53:16.516Z</Timestamp>
        <ResourceStatus>CREATE_IN_PROGRESS</ResourceStatus>
        <StackId>arn:aws:cloudformation:us-east-1:123456789012:stack/SampleStack/12a3b456-0e10-4ce0-9052-5d484a8c4e5b</StackId>
        <EventId>MyEC2Instance-CREATE_IN_PROGRESS-2016-03-15T20:53:16.516Z</EventId>
        <LogicalResourceId>MyEC2Instance</LogicalResourceId>
        <StackName>SampleStack</StackName>
        <PhysicalResourceId/>
        <ResourceProperties>{"ImageId":ami-8fcee4e5",...}</ResourceProperties>
        <ResourceType>AWS::EC2::Instance</ResourceType>
      </member>
      <member>
        <Timestamp>2016-03-15T20:53:11.231Z</Timestamp>
        <ResourceStatus>CREATE_IN_PROGRESS</ResourceStatus>
        <StackId>arn:aws:cloudformation:us-east-1:123456789012:stack/SampleStack/12a3b456-0e10-4ce0-9052-5d484a8c4e5b</StackId>
        <EventId>edbf2ac0-eaef-11e5-adeb-500c28903236</EventId>
        <LogicalResourceId>SampleStack</LogicalResourceId>
        <ResourceStatusReason>User Initiated</ResourceStatusReason>
        <StackName>SampleStack</StackName>
        <PhysicalResourceIdI>arn:aws:cloudformation:us-east-1:123456789012:stack/SampleStack/12a3b456-0e10-4ce0-9052-5d484a8c4e5b</PhysicalResourceId>
        <ResourceType>AWS::CloudFormation::Stack</ResourceType>
      </member>
    </StackEvents>
  </DescribeStackEventsResult>
  <ResponseMetadata>
    <RequestId>b9b4b068-3a41-11e5-94eb-example</RequestId>
  </ResponseMetadata>
</DescribeStackEventsResponse>
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/DescribeStackEvents "https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/DescribeStackEvents")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/DescribeStackEvents "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/DescribeStackEvents")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/DescribeStackEvents "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/DescribeStackEvents")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/DescribeStackEvents "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/DescribeStackEvents")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/DescribeStackEvents "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/DescribeStackEvents")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/DescribeStackEvents "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/DescribeStackEvents")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/DescribeStackEvents "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/DescribeStackEvents")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/DescribeStackEvents "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/DescribeStackEvents")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/DescribeStackEvents "https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/DescribeStackEvents")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/DescribeStackEvents "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/DescribeStackEvents")
