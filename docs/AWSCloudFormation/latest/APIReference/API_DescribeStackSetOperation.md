# DescribeStackSetOperation

Returns the description of the specified StackSet operation.

###### Note

This API provides *strongly consistent* reads meaning it will always
 return the most up-to-date data.


## Request Parameters


 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").





**CallAs** 


[Service-managed permissions] Specifies whether you are acting as an account administrator
 in the organization's management account or as a delegated administrator in a
 member account.


By default, `SELF` is specified. Use `SELF` for StackSets with
 self-managed permissions.



* If you are signed in to the management account, specify
 `SELF`.
* If you are signed in to a delegated administrator account, specify
 `DELEGATED_ADMIN`.


Your AWS account must be registered as a delegated administrator in the management account. For more information, see [Register a
 delegated administrator](../UserGuide/stacksets-orgs-delegated-admin.md "../UserGuide/stacksets-orgs-delegated-admin.md") in the *AWS CloudFormation User Guide*.

Type: String


Valid Values: `SELF | DELEGATED_ADMIN`



Required: No




**OperationId** 


The unique ID of the StackSet operation.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 128.


Pattern: `[a-zA-Z0-9][-a-zA-Z0-9]*`



Required: Yes




**StackSetName** 


The name or the unique stack ID of the StackSet for the stack operation.


Type: String


Required: Yes




## Response Elements


The following element is returned by the service.





**StackSetOperation** 


The specified StackSet operation.


Type: [StackSetOperation](API_StackSetOperation.md "API_StackSetOperation.md") object




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**OperationNotFound** 


The specified ID refers to an operation that doesn't exist.


HTTP Status Code: 404




**StackSetNotFound** 


The specified StackSet doesn't exist.


HTTP Status Code: 404




## Examples


### Describing an Update StackSet Operation


The following example returns information about a successful update of a StackSet and
 its associated stack instances.


#### Sample Request



```
https://cloudformation.us-east-1.amazonaws.com/
 ?Action=DescribeStackSetOperation
 &Version=2010-05-15
 &StackSetName=stack-set-example
 &OperationId=61806005-bde9-46f1-949d-6791example
 &X-Amz-Algorithm=AWS4-HMAC-SHA256
 &X-Amz-Credential=[Access key ID and scope]
 &X-Amz-Date=20170810T233349Z
 &X-Amz-SignedHeaders=content-type;host
 &X-Amz-Signature=[Signature]
```

#### Sample Response



```

<DescribeStackSetOperationResponse xmlns="http://internal.amazon.com/coral/com.amazonaws.maestro.service.v20160713/">
  <DescribeStackSetOperationResult>
    <StackSetOperation>
      <StackSetId>stack-set-example:c14cd6d1-cd17-40bd-82ed-ff97example</StackSetId>
      <CreationTimestamp>2017-08-04T18:01:29.508Z</CreationTimestamp>
      <OperationId>ddf16f54-ad62-4d9b-b0ab-3ed8e9example</OperationId>
      <Action>UPDATE</Action>
      <OperationPreferences>
        <FailureToleranceCount>0</FailureToleranceCount>
        <MaxConcurrentCount>1</MaxConcurrentCount>
        <RegionOrder/>
      </OperationPreferences>
      <EndTimestamp>2017-08-04T18:03:43.672Z</EndTimestamp>
      <Status>SUCCEEDED</Status>
    </StackSetOperation>
  </DescribeStackSetOperationResult>
  <ResponseMetadata>
    <RequestId>20133b62-7e1a-11e7-838a-a182example</RequestId>
  </ResponseMetadata>
</DescribeStackSetOperationResponse>
```

### Describing a Drift Detection StackSet Operation


The following example returns information about a drift detection operation run on a
 StackSet.


#### Sample Request



```

https://cloudformation.us-east-1.amazonaws.com/
 ?Action=DescribeStackSetOperation
 &Version=2010-05-15
 &StackSetName=stack-set-drift-example
 &OperationId=9cc082fa-df4c-45cd-b9a8-7e5example
 &X-Amz-Algorithm=AWS4-HMAC-SHA256
 &X-Amz-Credential=[Access key ID and scope]
 &X-Amz-Date=20191203T201942Z
 &X-Amz-SignedHeaders=content-type;host
 &X-Amz-Signature=[Signature]
```

#### Sample Response



```
<DescribeStackSetOperationResponse xmlns="http://internal.amazon.com/coral/com.amazonaws.maestro.service.v20160713/">
  <DescribeStackSetOperationResult>
    <StackSetOperation>
      <ExecutionRoleName>AWSCloudFormationStackSetExecutionRole</ExecutionRoleName>
      <AdministrationRoleARN>arn:aws:iam::012345678910:role/AWSCloudFormationStackSetAdministrationRole</AdministrationRoleARN>
      <StackSetId>stack-set-drift-example:bd1f4017-d4f9-432e-a73f-8c22eb708dd5</StackSetId>
      <OperationPreferences>
        <RegionOrder/>
      </OperationPreferences>
      <StackSetDriftDetectionDetails>
        <InSyncStackInstancesCount>2</InSyncStackInstancesCount>
        <FailedStackInstancesCount>0</FailedStackInstancesCount>
        <DriftStatus>DRIFTED</DriftStatus>
        <TotalStackInstancesCount>7</TotalStackInstancesCount>
        <DriftedStackInstancesCount>1</DriftedStackInstancesCount>
        <InProgressStackInstancesCount>4</InProgressStackInstancesCount>
        <LastDriftCheckTimestamp>2019-12-04T20:34:28.543Z</LastDriftCheckTimestamp>
      </StackSetDriftDetectionDetails>
      <CreationTimestamp>2019-12-04T20:33:13.673Z</CreationTimestamp>
      <OperationId>9cc082fa-df4c-45cd-b9a8-7e5example</OperationId>
      <Action>DETECT_DRIFT</Action>
      <Status>RUNNING</Status>
    </StackSetOperation>
  </DescribeStackSetOperationResult>
  <ResponseMetadata>
    <RequestId>e81844dc-6121-4b59-923a-e2417example</RequestId>
  </ResponseMetadata>
</DescribeStackSetOperationResponse>
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/DescribeStackSetOperation "https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/DescribeStackSetOperation")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/DescribeStackSetOperation "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/DescribeStackSetOperation")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/DescribeStackSetOperation "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/DescribeStackSetOperation")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/DescribeStackSetOperation "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/DescribeStackSetOperation")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/DescribeStackSetOperation "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/DescribeStackSetOperation")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/DescribeStackSetOperation "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/DescribeStackSetOperation")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/DescribeStackSetOperation "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/DescribeStackSetOperation")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/DescribeStackSetOperation "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/DescribeStackSetOperation")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/DescribeStackSetOperation "https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/DescribeStackSetOperation")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/DescribeStackSetOperation "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/DescribeStackSetOperation")
