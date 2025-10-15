# DetectStackDrift

Detects whether a stack's actual configuration differs, or has
 *drifted*, from its expected configuration, as defined in the stack
 template and any values specified as template parameters. For each resource in the stack that
 supports drift detection, CloudFormation compares the actual configuration of the resource with
 its expected template configuration. Only resource properties explicitly defined in the stack
 template are checked for drift. A stack is considered to have drifted if one or more of its
 resources differ from their expected template configurations. For more information, see [Detect unmanaged configuration changes to stacks and resources with drift
 detection](../UserGuide/using-cfn-stack-drift.md "../UserGuide/using-cfn-stack-drift.md").

Use `DetectStackDrift` to detect drift on all supported resources for a given
 stack, or [DetectStackResourceDrift](API_DetectStackResourceDrift.md "API_DetectStackResourceDrift.md") to detect drift on individual
 resources.

For a list of stack resources that currently support drift detection, see [Resource
 type support for imports and drift detection](../UserGuide/resource-import-supported-resources.md "../UserGuide/resource-import-supported-resources.md").


`DetectStackDrift` can take up to several minutes, depending on the number of
 resources contained within the stack. Use [DescribeStackDriftDetectionStatus](API_DescribeStackDriftDetectionStatus.md "API_DescribeStackDriftDetectionStatus.md")
 to monitor the progress of a detect stack drift operation. Once the drift detection operation
 has completed, use [DescribeStackResourceDrifts](API_DescribeStackResourceDrifts.md "API_DescribeStackResourceDrifts.md") to return drift information
 about the stack and its resources.

When detecting drift on a stack, CloudFormation doesn't detect drift on any nested stacks
 belonging to that stack. Perform `DetectStackDrift` directly on the nested stack
 itself.


## Request Parameters


 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").





**LogicalResourceIds.member.N**


The logical names of any resources you want to use as filters.


Type: Array of strings


Array Members: Minimum number of 1 item. Maximum number of 200 items.


Required: No




**StackName** 


The name of the stack for which you want to detect drift.


Type: String


Length Constraints: Minimum length of 1.


Pattern: `([a-zA-Z][-a-zA-Z0-9]*)|(arn:\b(aws|aws-us-gov|aws-cn)\b:[-a-zA-Z0-9:/._+]*)`



Required: Yes




## Response Elements


The following element is returned by the service.





**StackDriftDetectionId** 


The ID of the drift detection results of this operation.


CloudFormation generates new results, with a new drift detection ID, each time this operation
 is run. However, the number of drift results CloudFormation retains for any given stack, and for
 how long, may vary.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 36.




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").


## Examples


### DetectStackDrift


This example illustrates one usage of DetectStackDrift.


#### Sample Request



```

https://cloudformation.us-east-1.amazonaws.com/
 ?Action=DetectStackDrift
 &Version=2010-05-15
 &StackName=my-stack-with-resource-drift
 &X-Amz-Algorithm=AWS4-HMAC-SHA256
 &X-Amz-Credential=[Access key ID and scope]
 &X-Amz-Date=20171211T230005Z
 &X-Amz-SignedHeaders=content-type;host
 &X-Amz-Signature=[Signature]
```

#### Sample Response



```

<DetectStackDriftResponse xmlns="http://cloudformation.amazonaws.com/doc/2010-05-15/">
  <DetectStackDriftResult>
    <StackDriftDetectionId>2f2b2d60-df86-11e7-bea1-500c2example</StackDriftDetectionId>
  </DetectStackDriftResult>
  <ResponseMetadata>
    <RequestId>2f07c75d-df86-11e7-8270-89489example</RequestId>
  </ResponseMetadata>
</DetectStackDriftResponse>
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/DetectStackDrift "https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/DetectStackDrift")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/DetectStackDrift "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/DetectStackDrift")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/DetectStackDrift "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/DetectStackDrift")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/DetectStackDrift "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/DetectStackDrift")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/DetectStackDrift "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/DetectStackDrift")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/DetectStackDrift "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/DetectStackDrift")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/DetectStackDrift "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/DetectStackDrift")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/DetectStackDrift "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/DetectStackDrift")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/DetectStackDrift "https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/DetectStackDrift")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/DetectStackDrift "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/DetectStackDrift")
