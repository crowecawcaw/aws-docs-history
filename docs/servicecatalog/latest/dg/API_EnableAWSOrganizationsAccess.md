# EnableAWSOrganizationsAccess

Enable portfolio sharing feature through AWS Organizations. This API will allow AWS Service Catalog to receive updates on your organization in order to sync your shares with the
current structure. This API can only be called by the management account in the organization.

When you call this API, Service Catalog calls `organizations:EnableAWSServiceAccess` on your behalf so that your shares stay in sync with any changes in your AWS Organizations structure.

Note that a delegated administrator is not authorized to invoke `EnableAWSOrganizationsAccess`.

###### Important

If you have previously disabled Organizations access for Service Catalog, and then
enable access again, the portfolio access permissions might not sync with the latest changes to
the organization structure. Specifically, accounts that you removed from the organization after
disabling Service Catalog access, and before you enabled access again, can retain access to the
previously shared portfolio. As a result, an account that has been removed from the organization
might still be able to create or manage AWS resources when it is no longer
authorized to do so. AWS is working to resolve this issue.

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

**InvalidStateException**

An attempt was made to modify a resource that is in a state that is not valid.
Check your resources to ensure that they are in valid states before retrying the operation.

HTTP Status Code: 400

**OperationNotSupportedException**

The operation is not supported.

HTTP Status Code: 400

**ResourceNotFoundException**

The specified resource was not found.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/servicecatalog-2015-12-10/EnableAWSOrganizationsAccess.md "../../../goto/cli2/servicecatalog-2015-12-10/EnableAWSOrganizationsAccess.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/servicecatalog-2015-12-10/EnableAWSOrganizationsAccess.md "../../../goto/DotNetSDKV3/servicecatalog-2015-12-10/EnableAWSOrganizationsAccess.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/EnableAWSOrganizationsAccess.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/EnableAWSOrganizationsAccess.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/servicecatalog-2015-12-10/EnableAWSOrganizationsAccess.md "../../../goto/SdkForGoV2/servicecatalog-2015-12-10/EnableAWSOrganizationsAccess.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/EnableAWSOrganizationsAccess.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/EnableAWSOrganizationsAccess.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/EnableAWSOrganizationsAccess.md "../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/EnableAWSOrganizationsAccess.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/servicecatalog-2015-12-10/EnableAWSOrganizationsAccess.md "../../../goto/SdkForKotlin/servicecatalog-2015-12-10/EnableAWSOrganizationsAccess.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/EnableAWSOrganizationsAccess.md "../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/EnableAWSOrganizationsAccess.md")
- [AWS SDK for Python](../../../goto/boto3/servicecatalog-2015-12-10/EnableAWSOrganizationsAccess.md "../../../goto/boto3/servicecatalog-2015-12-10/EnableAWSOrganizationsAccess.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/EnableAWSOrganizationsAccess.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/EnableAWSOrganizationsAccess.md")
