# ListStackResources

Returns descriptions of all resources of the specified stack.

For deleted stacks, ListStackResources returns resource information for up to 90 days
 after the stack has been deleted.


## Request Parameters


 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").





**NextToken** 


A string that identifies the next page of stack resources that you want to
 retrieve.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: No




**StackName** 


The name or the unique stack ID that is associated with the stack, which aren't always
 interchangeable:



* Running stacks: You can specify either the stack's name or its unique stack ID.
* Deleted stacks: You must specify the unique stack ID.

Type: String


Required: Yes




## Response Elements


The following elements are returned by the service.





**NextToken** 


If the output exceeds 1 MB, a string that identifies the next page of stack resources. If
 no additional page exists, this value is null.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.




**StackResourceSummaries.member.N**


A list of `StackResourceSummary` structures.


Type: Array of [StackResourceSummary](API_StackResourceSummary.md "API_StackResourceSummary.md") objects




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").


## Examples


### ListStackResources


This example illustrates one usage of ListStackResources.


#### Sample Request



```

https://cloudformation.us-east-1.amazonaws.com/
 ?Action=ListStackResources
 &StackName=MyStack
 &Version=2010-05-15
 &SignatureVersion=2
 &Timestamp=2011-07-08T22%3A26%3A28.000Z
 &AWSAccessKeyId=[AWS Access KeyID]
 &Signature=[Signature]
```

#### Sample Response



```

<ListStackResourcesResponse xmlns="http://cloudformation.amazonaws.com/doc/2010-05-15/">
  <ListStackResourcesResult>
    <StackResourceSummaries>
      <member>
        <ResourceStatus>CREATE_COMPLETE</ResourceStatus>
        <LogicalResourceId>DBSecurityGroup</LogicalResourceId>
        <LastUpdatedTimestamp>2011-06-21T20:15:58Z</LastUpdatedTimestamp>
        <PhysicalResourceId>gmarcteststack-dbsecuritygroup-1s5m0ez5lkk6w</Physic
alResourceId>
        <ResourceType>AWS::RDS::DBSecurityGroup</ResourceType>
      </member>
      <member>
        <ResourceStatus>CREATE_COMPLETE</ResourceStatus>
        <LogicalResourceId>SampleDB</LogicalResourceId>
        <LastUpdatedTimestamp>2011-06-21T20:25:57Z</LastUpdatedTimestamp>
        <PhysicalResourceId>MyStack-sampledb-ycwhk1v830lx</PhysicalResour
ceId>
        <ResourceType>AWS::RDS::DBInstance</ResourceType>
      </member>
      <member>
        <ResourceStatus>CREATE_COMPLETE</ResourceStatus>
        <LogicalResourceId>SampleApplication</LogicalResourceId>
        <LastUpdatedTimestamp>2011-06-21T20:26:12Z</LastUpdatedTimestamp>
        <PhysicalResourceId>MyStack-SampleApplication-1MKNASYR3RBQL</Phys
icalResourceId>
        <ResourceType>AWS::ElasticBeanstalk::Application</ResourceType>
      </member>
      <member>
        <ResourceStatus>CREATE_COMPLETE</ResourceStatus>
        <LogicalResourceId>SampleEnvironment</LogicalResourceId>
        <LastUpdatedTimestamp>2011-06-21T20:28:48Z</LastUpdatedTimestamp>
        <PhysicalResourceId>myst-Samp-1AGU6ERZX6M3Q</PhysicalResourceId>
        <ResourceType>AWS::ElasticBeanstalk::Environment</ResourceType>
      </member>
      <member>
        <ResourceStatus>CREATE_COMPLETE</ResourceStatus>
        <LogicalResourceId>AlarmTopic</LogicalResourceId>
        <LastUpdatedTimestamp>2011-06-21T20:29:06Z</LastUpdatedTimestamp>
        <PhysicalResourceId>arn:aws:sns:us-east-1:803981987763:MyStack-Al
armTopic-SW4IQELG7RPJ</PhysicalResourceId>
        <ResourceType>AWS::SNS::Topic</ResourceType>
      </member>
      <member>
        <ResourceStatus>CREATE_COMPLETE</ResourceStatus>
        <LogicalResourceId>CPUAlarmHigh</LogicalResourceId>
        <LastUpdatedTimestamp>2011-06-21T20:29:23Z</LastUpdatedTimestamp>
        <PhysicalResourceId>MyStack-CPUAlarmHigh-POBWQPDJA81F</PhysicalRe
sourceId>
        <ResourceType>AWS::CloudWatch::Alarm</ResourceType>
      </member>
    </StackResourceSummaries>
  </ListStackResourcesResult>
  <ResponseMetadata>
    <RequestId>2d06e36c-ac1d-11e0-a958-example</RequestId>
  </ResponseMetadata>
</ListStackResourcesResponse>
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/ListStackResources "https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/ListStackResources")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/ListStackResources "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/ListStackResources")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/ListStackResources "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/ListStackResources")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/ListStackResources "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/ListStackResources")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/ListStackResources "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/ListStackResources")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/ListStackResources "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/ListStackResources")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/ListStackResources "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/ListStackResources")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/ListStackResources "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/ListStackResources")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/ListStackResources "https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/ListStackResources")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/ListStackResources "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/ListStackResources")
