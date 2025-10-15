# ListExports

Lists all exported output values in the account and Region in which you call this action.
 Use this action to see the exported output values that you can import into other stacks. To
 import values, use the  [Fn::ImportValue](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-importvalue.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-importvalue.html") function.

For more information, see [Get exported outputs
 from a deployed CloudFormation stack](../UserGuide/using-cfn-stack-exports.md "../UserGuide/using-cfn-stack-exports.md").


## Request Parameters


 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").





**NextToken** 


A string (provided by the [ListExports](API_ListExports.md "API_ListExports.md") response output) that identifies
 the next page of exported output values that you asked to retrieve.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: No




## Response Elements


The following elements are returned by the service.





**Exports.member.N**


The output for the [ListExports](API_ListExports.md "API_ListExports.md") action.


Type: Array of [Export](API_Export.md "API_Export.md") objects




**NextToken** 


If the output exceeds 100 exported output values, a string that identifies the next page
 of exports. If there is no additional page, this value is null.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").


## Examples


### ListExports


This example illustrates one usage of ListExports.


#### Sample Request



```

https://cloudformation.us-east-1.amazonaws.com/
 ?Action=ListExports
 &Version=2010-05-15
 &X-Amz-Algorithm=AWS4-HMAC-SHA256
 &X-Amz-Credential=[Access key ID and scope]
 &X-Amz-Date=20160316T233349Z
 &X-Amz-SignedHeaders=content-type;host
 &X-Amz-Signature=[Signature]
```

#### Sample Response



```

<ListExportsResponse xmlns="http://cloudformation.amazonaws.com/doc/2010-05-15/">
  <ListExportsResult>
    <Exports>
      <member>
        <Name>mySampleStack1-SecurityGroupID</Name>
        <ExportingStackId>arn:aws:cloudformation:us-east-1:123456789012:stack/mySampleStack1/12a3b456-0e10-4ce0-9052-5d484a8c4e5b</ExportingStackId>
        <Value>sg-0a123b45</Value>
      </member>
      <member>
        <Name>mySampleStack1-SubnetID</Name>
        <ExportingStackId>arn:aws:cloudformation:us-east-1:123456789012:stack/mySampleStack1/12a3b456-0e10-4ce0-9052-5d484a8c4e5b</ExportingStackId>
        <Value>subnet-0a123b45</Value>
      </member>
      <member>
        <Name>mySampleStack1-VPCID</Name>
        <ExportingStackId>arn:aws:cloudformation:us-east-1:123456789012:stack/mySampleStack1/12a3b456-0e10-4ce0-9052-5d484a8c4e5b</ExportingStackId>
        <Value>vpc-0a123b45</Value>
      </member>
      <member>
        <Name>WebSiteURL</Name>
        <ExportingStackId>arn:aws:cloudformation:us-east-1:123456789012:stack/myS3StaticSite/12a3b456-0e10-4ce0-9052-5d484a8c4e5b</ExportingStackId>
        <Value>http://testsite.com.s3-website-us-east-1.amazonaws.com</Value>
      </member>
    </Exports>
  </ListExportsResult>
  <ResponseMetadata>
    <RequestId>5ccc7dcd-744c-11e5-be70-1b08c228efb3</RequestId>
  </ResponseMetadata>
</ListExportsResponse>
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/ListExports "https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/ListExports")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/ListExports "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/ListExports")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/ListExports "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/ListExports")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/ListExports "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/ListExports")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/ListExports "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/ListExports")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/ListExports "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/ListExports")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/ListExports "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/ListExports")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/ListExports "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/ListExports")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/ListExports "https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/ListExports")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/ListExports "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/ListExports")
