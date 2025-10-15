# DescribeStacks

Returns the description for the specified stack; if no stack name was specified, then it
 returns the description for all the stacks created. For more information about a stack's event
 history, see [Understand CloudFormation stack creation events](../UserGuide/stack-resource-configuration-complete.md "../UserGuide/stack-resource-configuration-complete.md") in the
 *AWS CloudFormation User Guide*.

###### Note

If the stack doesn't exist, a `ValidationError` is returned.


## Request Parameters


 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").





**NextToken** 


A string that identifies the next page of stacks that you want to retrieve.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: No




**StackName** 


###### Note

If you don't pass a parameter to `StackName`, the API returns a response
 that describes all resources in the account, which can impact performance. This requires
 `ListStacks` and `DescribeStacks` permissions.

Consider using the [ListStacks](API_ListStacks.md "API_ListStacks.md") API if you're not passing a parameter to
 `StackName`.

The IAM policy below can be added to IAM policies when you want to limit
 resource-level permissions and avoid returning a response when no parameter is sent in the
 request:

{ "Version": "2012-10-17", "Statement": [{ "Effect": "Deny", "Action":
 "cloudformation:DescribeStacks", "NotResource": "arn:aws:cloudformation:\*:\*:stack/\*/\*" }] }


The name or the unique stack ID that's associated with the stack, which aren't always
 interchangeable:



* Running stacks: You can specify either the stack's name or its unique stack ID.
* Deleted stacks: You must specify the unique stack ID.

Type: String


Required: No




## Response Elements


The following elements are returned by the service.





**NextToken** 


If the output exceeds 1 MB in size, a string that identifies the next page of stacks. If
 no additional page exists, this value is null.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.




**Stacks.member.N**


A list of stack structures.


Type: Array of [Stack](API_Stack.md "API_Stack.md") objects




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").


## Examples


### DescribeStacks


This example illustrates one usage of DescribeStacks.


#### Sample Request



```

https://cloudformation.us-east-1.amazonaws.com/
 ?Action=DescribeStacks
 &StackName=MyStack
 &Version=2010-05-15
 &SignatureVersion=2
 &Timestamp=2010-07-27T22%3A26%3A28.000Z
 &AWSAccessKeyId=[AWS Access KeyID]
 &Signature=[Signature]
```

#### Sample Response



```

<DescribeStacksResponse xmlns="http://cloudformation.amazonaws.com/doc/2010-05-15/">
  <DescribeStacksResult>
    <Stacks>
      <member>
        <StackName>MyStack</StackName>
        <StackId>arn:aws:cloudformation:us-east-1:123456789:stack/MyStack/aaf549a0-a413-11df-adb3-5081b3858e83</StackId>
        <CreationTime>2010-07-27T22:28:28Z</CreationTime>
        <StackStatus>CREATE_COMPLETE</StackStatus>
        <DisableRollback>false</DisableRollback>
        <Outputs>
          <member>
            <OutputKey>StartPage</OutputKey>
            <OutputValue>http://my-load-balancer.amazonaws.com:80/index.html</OutputValue>
          </member>
        </Outputs>
      </member>
    </Stacks>
  </DescribeStacksResult>
  <ResponseMetadata>
    <RequestId>b9b4b068-3a41-11e5-94eb-example</RequestId>
  </ResponseMetadata>
</DescribeStacksResponse>
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/DescribeStacks "https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/DescribeStacks")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/DescribeStacks "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/DescribeStacks")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/DescribeStacks "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/DescribeStacks")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/DescribeStacks "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/DescribeStacks")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/DescribeStacks "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/DescribeStacks")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/DescribeStacks "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/DescribeStacks")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/DescribeStacks "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/DescribeStacks")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/DescribeStacks "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/DescribeStacks")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/DescribeStacks "https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/DescribeStacks")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/DescribeStacks "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/DescribeStacks")
