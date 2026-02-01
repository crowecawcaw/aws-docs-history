# DisableAWSOrganizationsAccess

Disable portfolio sharing through the AWS Organizations service. This command will not
delete your current shares, but prevents you from creating new shares throughout your
organization. Current shares are not kept in sync with your organization structure if the structure
changes after calling this API. Only the management account in the organization can call this API.

You cannot call this API if there are active delegated administrators in the organization.

Note that a delegated administrator is not authorized to invoke `DisableAWSOrganizationsAccess`.

###### Important

If you share an Service Catalog portfolio in an organization within
AWS Organizations, and then disable Organizations access for Service Catalog,
the portfolio access permissions will not sync with the latest changes to the organization
structure. Specifically, accounts that you removed from the organization after
disabling Service Catalog access will retain access to the previously shared portfolio.

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

- [AWS Command Line Interface V2](../../../goto/cli2/servicecatalog-2015-12-10/DisableAWSOrganizationsAccess.md "../../../goto/cli2/servicecatalog-2015-12-10/DisableAWSOrganizationsAccess.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/DisableAWSOrganizationsAccess.md "../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/DisableAWSOrganizationsAccess.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/DisableAWSOrganizationsAccess.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/DisableAWSOrganizationsAccess.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/servicecatalog-2015-12-10/DisableAWSOrganizationsAccess.md "../../../goto/SdkForGoV2/servicecatalog-2015-12-10/DisableAWSOrganizationsAccess.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/DisableAWSOrganizationsAccess.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/DisableAWSOrganizationsAccess.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/DisableAWSOrganizationsAccess.md "../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/DisableAWSOrganizationsAccess.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/servicecatalog-2015-12-10/DisableAWSOrganizationsAccess.md "../../../goto/SdkForKotlin/servicecatalog-2015-12-10/DisableAWSOrganizationsAccess.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/DisableAWSOrganizationsAccess.md "../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/DisableAWSOrganizationsAccess.md")
- [AWS SDK for Python](../../../goto/boto3/servicecatalog-2015-12-10/DisableAWSOrganizationsAccess.md "../../../goto/boto3/servicecatalog-2015-12-10/DisableAWSOrganizationsAccess.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/DisableAWSOrganizationsAccess.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/DisableAWSOrganizationsAccess.md")
