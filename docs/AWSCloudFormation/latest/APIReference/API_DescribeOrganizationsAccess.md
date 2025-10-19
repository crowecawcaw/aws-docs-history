# DescribeOrganizationsAccess

Retrieves information about the account's `OrganizationAccess` status. This API
 can be called either by the management account or the delegated administrator by using the
 `CallAs` parameter. This API can also be called without the `CallAs`
 parameter by the management account.


## Request Parameters


 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").





**CallAs** 


[Service-managed permissions] Specifies whether you are acting as an account administrator
 in the organization's management account or as a delegated administrator in a
 member account.


By default, `SELF` is specified.



* If you are signed in to the management account, specify
 `SELF`.
* If you are signed in to a delegated administrator account, specify
 `DELEGATED_ADMIN`.


Your AWS account must be registered as a delegated administrator in the management account. For more information, see [Register a
 delegated administrator](../UserGuide/stacksets-orgs-delegated-admin.md "../UserGuide/stacksets-orgs-delegated-admin.md") in the *AWS CloudFormation User Guide*.

Type: String


Valid Values: `SELF | DELEGATED_ADMIN`



Required: No




## Response Elements


The following element is returned by the service.





**Status** 


Presents the status of the `OrganizationAccess`.


Type: String


Valid Values: `ENABLED | DISABLED | DISABLED_PERMANENTLY`





## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**InvalidOperation** 


The specified operation isn't valid.


HTTP Status Code: 400




**OperationNotFound** 


The specified ID refers to an operation that doesn't exist.


HTTP Status Code: 404




## Examples


### DescribeOrganizationsAccess


This example illustrates one usage of DescribeOrganizationsAccess.


#### Sample Request



```

https://cloudformation.us-east-1.amazonaws.com/
    ?Action=DescribeOrganizationsAccess
```

#### Sample Response



```

<DescribeOrganizationsAccessResponse xmlns="http://internal.amazon.com/coral/com.amazonaws.maestro.service.v20160713/">
  <DescribeOrganizationsAccessResult>
    <Status>ENABLED</Status>
  </DescribeOrganizationsAccessResult>
  <ResponseMetadata>
    <RequestId>240f1cd7-48d6-41a6-b61b-65c7c81893e9</RequestId>
  </ResponseMetadata>
</DescribeOrganizationsAccessResponse>
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/DescribeOrganizationsAccess "https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/DescribeOrganizationsAccess")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/DescribeOrganizationsAccess "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/DescribeOrganizationsAccess")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/DescribeOrganizationsAccess "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/DescribeOrganizationsAccess")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/DescribeOrganizationsAccess "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/DescribeOrganizationsAccess")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/DescribeOrganizationsAccess "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/DescribeOrganizationsAccess")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/DescribeOrganizationsAccess "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/DescribeOrganizationsAccess")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/DescribeOrganizationsAccess "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/DescribeOrganizationsAccess")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/DescribeOrganizationsAccess "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/DescribeOrganizationsAccess")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/DescribeOrganizationsAccess "https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/DescribeOrganizationsAccess")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/DescribeOrganizationsAccess "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/DescribeOrganizationsAccess")
