# DescribeStackResourceDrifts

Returns drift information for the resources that have been checked for drift in the
 specified stack. This includes actual and expected configuration values for resources where
 CloudFormation detects configuration drift.

For a given stack, there will be one `StackResourceDrift` for each stack
 resource that has been checked for drift. Resources that haven't yet been checked for drift
 aren't included. Resources that don't currently support drift detection aren't checked, and so
 not included. For a list of resources that support drift detection, see [Resource
 type support for imports and drift detection](../UserGuide/resource-import-supported-resources.md "../UserGuide/resource-import-supported-resources.md").

Use [DetectStackResourceDrift](API_DetectStackResourceDrift.md "API_DetectStackResourceDrift.md") to detect drift on individual resources, or
 [DetectStackDrift](API_DetectStackDrift.md "API_DetectStackDrift.md") to detect drift on all supported resources for a given
 stack.


## Request Parameters


 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").





**MaxResults** 


The maximum number of results to be returned with a single call. If the number of
 available results exceeds this maximum, the response includes a `NextToken` value
 that you can assign to the `NextToken` request parameter to get the next set of
 results.


Type: Integer


Valid Range: Minimum value of 1. Maximum value of 100.


Required: No




**NextToken** 


A string that identifies the next page of stack resource drift results.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: No




**StackName** 


The name of the stack for which you want drift information.


Type: String


Length Constraints: Minimum length of 1.


Pattern: `([a-zA-Z][-a-zA-Z0-9]*)|(arn:\b(aws|aws-us-gov|aws-cn)\b:[-a-zA-Z0-9:/._+]*)`



Required: Yes




**StackResourceDriftStatusFilters.member.N**


The resource drift status values to use as filters for the resource drift results
 returned.



* `DELETED`: The resource differs from its expected template configuration in
 that the resource has been deleted.
* `MODIFIED`: One or more resource properties differ from their expected
 template values.
* `IN_SYNC`: The resource's actual configuration matches its expected
 template configuration.
* `NOT_CHECKED`: CloudFormation doesn't currently return this value.
* `UNKNOWN`: CloudFormation could not run drift detection for the
 resource.

Type: Array of strings


Array Members: Minimum number of 1 item. Maximum number of 4 items.


Valid Values: `IN_SYNC | MODIFIED | DELETED | NOT_CHECKED | UNKNOWN`



Required: No




## Response Elements


The following elements are returned by the service.





**NextToken** 


If the request doesn't return all the remaining results, `NextToken` is set to
 a token. To retrieve the next set of results, call `DescribeStackResourceDrifts`
 again and assign that token to the request object's `NextToken` parameter. If the
 request returns all results, `NextToken` is set to `null`.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.




**StackResourceDrifts.member.N**


Drift information for the resources that have been checked for drift in the specified
 stack. This includes actual and expected configuration values for resources where CloudFormation
 detects drift.


For a given stack, there will be one `StackResourceDrift` for each stack
 resource that has been checked for drift. Resources that haven't yet been checked for drift
 aren't included. Resources that do not currently support drift detection aren't checked, and
 so not included. For a list of resources that support drift detection, see [Resource
 type support for imports and drift detection](../UserGuide/resource-import-supported-resources.md "../UserGuide/resource-import-supported-resources.md").


Type: Array of [StackResourceDrift](API_StackResourceDrift.md "API_StackResourceDrift.md") objects




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").


## Examples


### DescribeStackResourceDrifts


This example illustrates one usage of DescribeStackResourceDrifts.


#### Sample Request



```

https://cloudformation.us-east-1.amazonaws.com/
 ?Action=DescribeStackResourceDrifts
 &Version=2010-05-15
 &StackName=my-stack-with-resource-drift
 &StackResourceDriftStatusFilters.member.1=MODIFIED
 &X-Amz-Algorithm=AWS4-HMAC-SHA256
 &X-Amz-Credential=[Access key ID and scope]
 &X-Amz-Date=20171228T233658Z
 &X-Amz-SignedHeaders=content-type;host
 &X-Amz-Signature=[Signature]
```

#### Sample Response



```

<DescribeStackResourceDriftsResponse xmlns="http://cloudformation.amazonaws.com/doc/2010-05-15/">
  <DescribeStackResourceDriftsResult>
    <StackResourceDrifts>
      <member>
        <PropertyDifferences>
          <member>
            <ActualValue>120</ActualValue>
            <ExpectedValue>20</ExpectedValue>
            <DifferenceType>NOT_EQUAL</DifferenceType>
            <PropertyPath>/DelaySeconds</PropertyPath>
          </member>
          <member>
            <ActualValue>12</ActualValue>
            <ExpectedValue>10</ExpectedValue>
            <DifferenceType>NOT_EQUAL</DifferenceType>
            <PropertyPath>/RedrivePolicy/maxReceiveCount</PropertyPath>
          </member>
        </PropertyDifferences>
        <PhysicalResourceId>https://sqs.us-east-1.amazonaws.com/012345678910/my-stack-with-resource-drift-Queue-494PBHCO76H4</PhysicalResourceId>
        <ExpectedProperties>{
          "ReceiveMessageWaitTimeSeconds":0,
          "DelaySeconds":20,
          "RedrivePolicy":{
            "deadLetterTargetArn":"arn:aws:sqs:us-east-1:012345678910:my-stack-with-resource-drift-DLQ-1BCY7HHD5QIM3",
            "maxReceiveCount":10
            },
          "MessageRetentionPeriod":345600,
          "MaximumMessageSize":262144,
          "VisibilityTimeout":60,
          "QueueName":"my-stack-with-resource-drift-Queue-494PBHCO76H4"
        }
        </ExpectedProperties>
        <StackResourceDriftStatus>MODIFIED</StackResourceDriftStatus>
        <StackId>arn:aws:cloudformation:us-east-1:012345678910:stack/my-stack-with-resource-drift/489e5570-df85-11e7-a7d9-503acac5c0fd</StackId>
        <LogicalResourceId>Queue</LogicalResourceId>
        <ActualProperties>{
          "ReceiveMessageWaitTimeSeconds":0,
          "DelaySeconds":120,
          "RedrivePolicy":{
            "deadLetterTargetArn":"arn:aws:sqs:us-east-1:012345678910:my-stack-with-resource-drift-DLQ-1BCY7HHD5QIM3",
            "maxReceiveCount":12
            },
          "MessageRetentionPeriod":345600,
          "MaximumMessageSize":262144,
          "VisibilityTimeout":60,
          "QueueName":"my-stack-with-resource-drift-Queue-494PBHCO76H4"
          }
        </ActualProperties>
        <Timestamp>2017-12-28T23:18:45.997Z</Timestamp>
        <ResourceType>AWS::SQS::Queue</ResourceType>
      </member>
    </StackResourceDrifts>
  </DescribeStackResourceDriftsResult>
  <ResponseMetadata>
    <RequestId>fee6d615-ec27-11e7-948a-0bec95751ba6</RequestId>
  </ResponseMetadata>
</DescribeStackResourceDriftsResponse>
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/DescribeStackResourceDrifts "https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/DescribeStackResourceDrifts")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/DescribeStackResourceDrifts "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/DescribeStackResourceDrifts")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/DescribeStackResourceDrifts "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/DescribeStackResourceDrifts")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/DescribeStackResourceDrifts "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/DescribeStackResourceDrifts")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/DescribeStackResourceDrifts "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/DescribeStackResourceDrifts")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/DescribeStackResourceDrifts "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/DescribeStackResourceDrifts")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/DescribeStackResourceDrifts "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/DescribeStackResourceDrifts")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/DescribeStackResourceDrifts "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/DescribeStackResourceDrifts")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/DescribeStackResourceDrifts "https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/DescribeStackResourceDrifts")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/DescribeStackResourceDrifts "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/DescribeStackResourceDrifts")
