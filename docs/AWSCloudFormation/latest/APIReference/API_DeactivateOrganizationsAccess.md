# DeactivateOrganizationsAccess

Deactivates trusted access with AWS Organizations. If trusted access is deactivated,
 the management account does not have permissions to create and manage
 service-managed StackSets for your organization.


## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**InvalidOperation** 


The specified operation isn't valid.


HTTP Status Code: 400




**OperationNotFound** 


The specified ID refers to an operation that doesn't exist.


HTTP Status Code: 404




## Examples


### DeactivateOrganizationsAccess


This example illustrates one usage of DeactivateOrganizationsAccess.


#### Sample Request



```

https://cloudformation.us-east-1.amazonaws.com/
    ?Action=DeactivateOrganizationsAccess
```

#### Sample Response



```

<DeactivateOrganizationsAccessResponse xmlns="http://internal.amazon.com/coral/com.amazonaws.maestro.service.v20160713/">
  <DeactivateOrganizationsAccessResult/>
  <ResponseMetadata>
    <RequestId>f2038c6a-2ef6-45d0-a045-f2b4d15647ba</RequestId>
  </ResponseMetadata>
</DeactivateOrganizationsAccessResponse>
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/DeactivateOrganizationsAccess "https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/DeactivateOrganizationsAccess")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/DeactivateOrganizationsAccess "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/DeactivateOrganizationsAccess")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/DeactivateOrganizationsAccess "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/DeactivateOrganizationsAccess")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/DeactivateOrganizationsAccess "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/DeactivateOrganizationsAccess")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/DeactivateOrganizationsAccess "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/DeactivateOrganizationsAccess")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/DeactivateOrganizationsAccess "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/DeactivateOrganizationsAccess")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/DeactivateOrganizationsAccess "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/DeactivateOrganizationsAccess")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/DeactivateOrganizationsAccess "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/DeactivateOrganizationsAccess")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/DeactivateOrganizationsAccess "https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/DeactivateOrganizationsAccess")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/DeactivateOrganizationsAccess "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/DeactivateOrganizationsAccess")
