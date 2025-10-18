# DescribeStackDriftDetectionStatus

Returns information about a stack drift detection operation. A stack drift detection
 operation detects whether a stack's actual configuration differs, or has
 *drifted*, from its expected configuration, as defined in the stack
 template and any values specified as template parameters. A stack is considered to have
 drifted if one or more of its resources have drifted. For more information about stack and
 resource drift, see [Detect unmanaged
 configuration changes to stacks and resources with drift detection](../UserGuide/using-cfn-stack-drift.md "../UserGuide/using-cfn-stack-drift.md").

Use [DetectStackDrift](API_DetectStackDrift.md "API_DetectStackDrift.md") to initiate a stack drift detection operation.
 `DetectStackDrift` returns a `StackDriftDetectionId` you can use to
 monitor the progress of the operation using `DescribeStackDriftDetectionStatus`.
 Once the drift detection operation has completed, use [DescribeStackResourceDrifts](API_DescribeStackResourceDrifts.md "API_DescribeStackResourceDrifts.md") to return drift information about the stack and its
 resources.


## Request Parameters


 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").





**StackDriftDetectionId** 


The ID of the drift detection results of this operation.


CloudFormation generates new results, with a new drift detection ID, each time this operation
 is run. However, the number of drift results CloudFormation retains for any given stack, and for
 how long, may vary.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 36.


Required: Yes




## Response Elements


The following elements are returned by the service.





**DetectionStatus** 


The status of the stack drift detection operation.



* `DETECTION_COMPLETE`: The stack drift detection operation has successfully
 completed for all resources in the stack that support drift detection. (Resources that
 don't currently support stack detection remain unchecked.)


If you specified logical resource IDs for CloudFormation to use as a filter for the stack
 drift detection operation, only the resources with those logical IDs are checked for
 drift.
* `DETECTION_FAILED`: The stack drift detection operation has failed for at
 least one resource in the stack. Results will be available for resources on which
 CloudFormation successfully completed drift detection.
* `DETECTION_IN_PROGRESS`: The stack drift detection operation is currently
 in progress.

Type: String


Valid Values: `DETECTION_IN_PROGRESS | DETECTION_FAILED | DETECTION_COMPLETE`





**DetectionStatusReason** 


The reason the stack drift detection operation has its current status.


Type: String




**DriftedStackResourceCount** 


Total number of stack resources that have drifted. This is NULL until the drift detection
 operation reaches a status of `DETECTION_COMPLETE`. This value will be 0 for stacks
 whose drift status is `IN_SYNC`.


Type: Integer




**StackDriftDetectionId** 


The ID of the drift detection results of this operation.


CloudFormation generates new results, with a new drift detection ID, each time this operation
 is run. However, the number of reports CloudFormation retains for any given stack, and for how
 long, may vary.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 36.




**StackDriftStatus** 


Status of the stack's actual configuration compared to its expected configuration.



* `DRIFTED`: The stack differs from its expected template configuration. A
 stack is considered to have drifted if one or more of its resources have drifted.
* `NOT_CHECKED`: CloudFormation hasn't checked if the stack differs from its
 expected template configuration.
* `IN_SYNC`: The stack's actual configuration matches its expected template
 configuration.
* `UNKNOWN`: CloudFormation could not run drift detection for a resource in the
 stack. See the `DetectionStatusReason` for details.

Type: String


Valid Values: `DRIFTED | IN_SYNC | UNKNOWN | NOT_CHECKED`





**StackId** 


The ID of the stack.


Type: String




**Timestamp** 


Time at which the stack drift detection operation was initiated.


Type: Timestamp




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").


## Examples


### DescribeStackDriftDetectionStatus


This example illustrates one usage of DescribeStackDriftDetectionStatus.


#### Sample Request



```

https://cloudformation.us-east-1.amazonaws.com/
 ?Action=DescribeStackDriftDetectionStatus
 &Version=2010-05-15
 &StackDriftDetectionId=b78ac9b0-dec1-11e7-a451-503a3example
 &X-Amz-Algorithm=AWS4-HMAC-SHA256
 &X-Amz-Credential=[Access key ID and scope]
 &X-Amz-Date=20171211T230005Z
 &X-Amz-SignedHeaders=content-type;host
 &X-Amz-Signature=[Signature]
```

#### Sample Response



```

<DescribeStackDriftDetectionStatusResponse xmlns="http://cloudformation.amazonaws.com/doc/2010-05-15/">
  <DescribeStackDriftDetectionStatusResult>
    <DetectionStatus>DETECTION_COMPLETE</DetectionStatus>
    <StackDriftDetectionId>b78ac9b0-dec1-11e7-a451-503a3example</StackDriftDetectionId>
    <DriftedStackResourceCount>0</DriftedStackResourceCount>
    <StackId>arn:aws:cloudformation:us-east-1:012345678910:stack/example/cb438120-6cc7-11e7-998e-50example</StackId>
    <StackDriftStatus>IN_SYNC</StackDriftStatus>
    <Timestamp>2017-12-11T22:22:04.747Z</Timestamp>
  </DescribeStackDriftDetectionStatusResult>
  <ResponseMetadata>
    <RequestId>f89bbda1-dec1-11e7-83c6-d92bexample</RequestId>
  </ResponseMetadata>
</DescribeStackDriftDetectionStatusResponse>
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/DescribeStackDriftDetectionStatus "https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/DescribeStackDriftDetectionStatus")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/DescribeStackDriftDetectionStatus "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/DescribeStackDriftDetectionStatus")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/DescribeStackDriftDetectionStatus "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/DescribeStackDriftDetectionStatus")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/DescribeStackDriftDetectionStatus "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/DescribeStackDriftDetectionStatus")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/DescribeStackDriftDetectionStatus "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/DescribeStackDriftDetectionStatus")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/DescribeStackDriftDetectionStatus "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/DescribeStackDriftDetectionStatus")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/DescribeStackDriftDetectionStatus "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/DescribeStackDriftDetectionStatus")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/DescribeStackDriftDetectionStatus "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/DescribeStackDriftDetectionStatus")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/DescribeStackDriftDetectionStatus "https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/DescribeStackDriftDetectionStatus")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/DescribeStackDriftDetectionStatus "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/DescribeStackDriftDetectionStatus")
