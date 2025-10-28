# GetAWSOrganizationsAccessStatus

Get the Access Status for AWS Organizations portfolio share feature. This API can only be
called by the management account in the organization or by a delegated admin.

## Response Syntax

```
{
   "AccessStatus": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[AccessStatus](#API_GetAWSOrganizationsAccessStatus_ResponseSyntax "#API_GetAWSOrganizationsAccessStatus_ResponseSyntax")**

The status of the portfolio share feature.

Type: String

Valid Values: `ENABLED | UNDER_CHANGE | DISABLED`

## Errors

**OperationNotSupportedException**

The operation is not supported.

HTTP Status Code: 400

**ResourceNotFoundException**

The specified resource was not found.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/servicecatalog-2015-12-10/GetAWSOrganizationsAccessStatus.md "../../../goto/cli2/servicecatalog-2015-12-10/GetAWSOrganizationsAccessStatus.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/servicecatalog-2015-12-10/GetAWSOrganizationsAccessStatus.md "../../../goto/DotNetSDKV3/servicecatalog-2015-12-10/GetAWSOrganizationsAccessStatus.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/GetAWSOrganizationsAccessStatus.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/GetAWSOrganizationsAccessStatus.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/servicecatalog-2015-12-10/GetAWSOrganizationsAccessStatus.md "../../../goto/SdkForGoV2/servicecatalog-2015-12-10/GetAWSOrganizationsAccessStatus.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/GetAWSOrganizationsAccessStatus.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/GetAWSOrganizationsAccessStatus.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/GetAWSOrganizationsAccessStatus.md "../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/GetAWSOrganizationsAccessStatus.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/servicecatalog-2015-12-10/GetAWSOrganizationsAccessStatus.md "../../../goto/SdkForKotlin/servicecatalog-2015-12-10/GetAWSOrganizationsAccessStatus.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/GetAWSOrganizationsAccessStatus.md "../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/GetAWSOrganizationsAccessStatus.md")
- [AWS SDK for Python](../../../goto/boto3/servicecatalog-2015-12-10/GetAWSOrganizationsAccessStatus.md "../../../goto/boto3/servicecatalog-2015-12-10/GetAWSOrganizationsAccessStatus.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/GetAWSOrganizationsAccessStatus.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/GetAWSOrganizationsAccessStatus.md")
