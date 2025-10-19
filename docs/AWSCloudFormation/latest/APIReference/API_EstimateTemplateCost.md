# EstimateTemplateCost

Returns the estimated monthly cost of a template. The return value is an AWS Simple
 Monthly Calculator URL with a query string that describes the resources required to run the
 template.


## Request Parameters


 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").





**Parameters.member.N**


A list of `Parameter` structures that specify input parameters.


Type: Array of [Parameter](API_Parameter.md "API_Parameter.md") objects


Required: No




**TemplateBody** 


Structure that contains the template body with a minimum length of 1 byte and a maximum
 length of 51,200 bytes.


Conditional: You must pass `TemplateBody` or `TemplateURL`. If both
 are passed, only `TemplateBody` is used.


Type: String


Length Constraints: Minimum length of 1.


Required: No




**TemplateURL** 


The URL of a file that contains the template body. The URL must point to a template that's
 located in an Amazon S3 bucket or a Systems Manager document. The location for an Amazon S3 bucket must
 start with `https://`. URLs from S3 static websites are not supported.


Conditional: You must pass `TemplateURL` or `TemplateBody`. If both
 are passed, only `TemplateBody` is used.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 5120.


Required: No




## Response Elements


The following element is returned by the service.





**Url** 


An AWS Simple Monthly Calculator URL with a query string that describes the resources
 required to run the template.


Type: String




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").


## Examples


### EstimateTemplateCost


This example illustrates one usage of EstimateTemplateCost.


#### Sample Request



```

https://cloudformation.us-east-1.amazonaws.com/
 ?Action=EstimateTemplateCost
 &TemplateURL= https://s3.amazonaws.com/cloudformation-samples-us-east-1/Drupal_Simple.template
 &Version=2010-05-15
 &SignatureVersion=2
 &Timestamp=2011-12-04T22%3A26%3A28.000Z
 &AWSAccessKeyId=[AWS Access KeyID]
 &Signature=[Signature]
```

#### Sample Response



```

<Response xmlns="http://cloudformation.amazonaws.com/doc/2010-05-15/">
  <EstimateTemplateCostResult>
    <Url>http://calculator.s3.amazonaws.com/calc5.html?key=cf-2e351785-e821-450c-9d58-625e1e1ebfb6</Url>
  </EstimateTemplateCostResult>
  <ResponseMetadata>
    <RequestId>b9b4b068-3a41-11e5-94eb-example</RequestId>
  </ResponseMetadata>
</Response>
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/EstimateTemplateCost "https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/EstimateTemplateCost")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/EstimateTemplateCost "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/EstimateTemplateCost")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/EstimateTemplateCost "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/EstimateTemplateCost")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/EstimateTemplateCost "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/EstimateTemplateCost")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/EstimateTemplateCost "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/EstimateTemplateCost")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/EstimateTemplateCost "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/EstimateTemplateCost")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/EstimateTemplateCost "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/EstimateTemplateCost")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/EstimateTemplateCost "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/EstimateTemplateCost")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/EstimateTemplateCost "https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/EstimateTemplateCost")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/EstimateTemplateCost "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/EstimateTemplateCost")
