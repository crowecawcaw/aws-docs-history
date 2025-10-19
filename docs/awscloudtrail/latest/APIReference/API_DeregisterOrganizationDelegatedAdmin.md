# DeregisterOrganizationDelegatedAdmin

Removes CloudTrail delegated administrator permissions from a member account in
 an organization.


## Request Syntax



```
{
   "DelegatedAdminAccountId": "`string`"
}
```

## Request Parameters


For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").


The request accepts the following data in JSON format.





**[DelegatedAdminAccountId](#API_DeregisterOrganizationDelegatedAdmin_RequestSyntax "#API_DeregisterOrganizationDelegatedAdmin_RequestSyntax")**


A delegated administrator account ID. This is a member account in an organization that
 is currently designated as a delegated administrator.


Type: String


Length Constraints: Minimum length of 12. Maximum length of 16.


Pattern: `\d+`



Required: Yes




## Response Elements


If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.


## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**AccountNotFoundException** 


This exception is thrown when the specified account is not found or not part of an
 organization.


HTTP Status Code: 400




**AccountNotRegisteredException** 


This exception is thrown when the specified account is not registered as the CloudTrail delegated administrator.


HTTP Status Code: 400




**CloudTrailAccessNotEnabledException** 


This exception is thrown when trusted access has not been enabled between AWS CloudTrail and AWS Organizations. For more information, see [How to enable or disable trusted access](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html#orgs_how-to-enable-disable-trusted-access "https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html#orgs_how-to-enable-disable-trusted-access") in the *AWS Organizations User Guide* and [Prepare For Creating a Trail For Your Organization](../userguide/creating-an-organizational-trail-prepare.md "../userguide/creating-an-organizational-trail-prepare.md") in the *AWS CloudTrail User Guide*.


HTTP Status Code: 400




**ConflictException** 


This exception is thrown when the specified resource is not ready for an operation. This
 can occur when you try to run an operation on a resource before CloudTrail has time
 to fully load the resource, or because another operation is modifying the resource. If this exception occurs, wait a few minutes, and then try the
 operation again.


HTTP Status Code: 400




**InsufficientDependencyServiceAccessPermissionException** 


This exception is thrown when the IAM identity that is used to create
 the organization resource lacks one or more required permissions for creating an
 organization resource in a required service.


HTTP Status Code: 400




**InvalidParameterException** 


The request includes a parameter that is not valid.


HTTP Status Code: 400




**NotOrganizationManagementAccountException** 


 This exception is thrown when the account making the request is not the organization's
 management account. 


HTTP Status Code: 400




**OperationNotPermittedException** 


This exception is thrown when the requested operation is not permitted.


HTTP Status Code: 400




**OrganizationNotInAllFeaturesModeException** 


This exception is thrown when AWS Organizations is not configured to support all
 features. All features must be enabled in Organizations to support creating an
 organization trail or event data store.


HTTP Status Code: 400




**OrganizationsNotInUseException** 


This exception is thrown when the request is made from an AWS account
 that is not a member of an organization. To make this request, sign in using the
 credentials of an account that belongs to an organization.


HTTP Status Code: 400




**UnsupportedOperationException** 


This exception is thrown when the requested operation is not supported.


HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/DeregisterOrganizationDelegatedAdmin "https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/DeregisterOrganizationDelegatedAdmin")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudtrail-2013-11-01/DeregisterOrganizationDelegatedAdmin "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudtrail-2013-11-01/DeregisterOrganizationDelegatedAdmin")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/DeregisterOrganizationDelegatedAdmin "https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/DeregisterOrganizationDelegatedAdmin")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/DeregisterOrganizationDelegatedAdmin "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/DeregisterOrganizationDelegatedAdmin")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/DeregisterOrganizationDelegatedAdmin "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/DeregisterOrganizationDelegatedAdmin")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/DeregisterOrganizationDelegatedAdmin "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/DeregisterOrganizationDelegatedAdmin")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/DeregisterOrganizationDelegatedAdmin "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/DeregisterOrganizationDelegatedAdmin")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/DeregisterOrganizationDelegatedAdmin "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/DeregisterOrganizationDelegatedAdmin")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/DeregisterOrganizationDelegatedAdmin "https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/DeregisterOrganizationDelegatedAdmin")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/DeregisterOrganizationDelegatedAdmin "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/DeregisterOrganizationDelegatedAdmin")
