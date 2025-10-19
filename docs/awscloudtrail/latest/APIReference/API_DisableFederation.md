# DisableFederation


 Disables Lake query federation on the specified event data store. When you disable federation, CloudTrail disables 
 the integration with AWS Glue, AWS Lake Formation, and Amazon Athena. 
 After disabling Lake query federation, you can no longer query your event data in Amazon Athena.

No CloudTrail Lake data is deleted when you disable federation and you can continue to run queries in CloudTrail Lake.


## Request Syntax



```
{
   "EventDataStore": "`string`"
}
```

## Request Parameters


For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").


The request accepts the following data in JSON format.





**[EventDataStore](#API_DisableFederation_RequestSyntax "#API_DisableFederation_RequestSyntax")**



 The ARN (or ID suffix of the ARN) of the event data store for which you want to disable Lake query federation.
 


Type: String


Length Constraints: Minimum length of 3. Maximum length of 256.


Pattern: `^[a-zA-Z0-9._/\-:]+$`



Required: Yes




## Response Syntax



```
{
   "EventDataStoreArn": "***string***",
   "FederationStatus": "***string***"
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[EventDataStoreArn](#API_DisableFederation_ResponseSyntax "#API_DisableFederation_ResponseSyntax")**



 The ARN of the event data store for which you disabled Lake query federation.
 


Type: String


Length Constraints: Minimum length of 3. Maximum length of 256.


Pattern: `^[a-zA-Z0-9._/\-:]+$`





**[FederationStatus](#API_DisableFederation_ResponseSyntax "#API_DisableFederation_ResponseSyntax")**



 The federation status.
 


Type: String


Valid Values: `ENABLING | ENABLED | DISABLING | DISABLED`





## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**AccessDeniedException** 



 You do not have sufficient access to perform this action.
 


HTTP Status Code: 400




**CloudTrailAccessNotEnabledException** 


This exception is thrown when trusted access has not been enabled between AWS CloudTrail and AWS Organizations. For more information, see [How to enable or disable trusted access](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html#orgs_how-to-enable-disable-trusted-access "https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html#orgs_how-to-enable-disable-trusted-access") in the *AWS Organizations User Guide* and [Prepare For Creating a Trail For Your Organization](../userguide/creating-an-organizational-trail-prepare.md "../userguide/creating-an-organizational-trail-prepare.md") in the *AWS CloudTrail User Guide*.


HTTP Status Code: 400




**ConcurrentModificationException** 



 You are trying to update a resource when another request is in progress. Allow sufficient wait time for the previous request to complete, then retry your request. 
 


HTTP Status Code: 400




**EventDataStoreARNInvalidException** 


The specified event data store ARN is not valid or does not map to an event data store
 in your account.


HTTP Status Code: 400




**EventDataStoreNotFoundException** 


The specified event data store was not found.


HTTP Status Code: 400




**InactiveEventDataStoreException** 


The event data store is inactive.


HTTP Status Code: 400




**InsufficientDependencyServiceAccessPermissionException** 


This exception is thrown when the IAM identity that is used to create
 the organization resource lacks one or more required permissions for creating an
 organization resource in a required service.


HTTP Status Code: 400




**InvalidParameterException** 


The request includes a parameter that is not valid.


HTTP Status Code: 400




**NoManagementAccountSLRExistsException** 


 This exception is thrown when the management account does not have a service-linked
 role. 


HTTP Status Code: 400




**NotOrganizationMasterAccountException** 


This exception is thrown when the AWS account making the request to
 create or update an organization trail or event data store is not the management account
 for an organization in AWS Organizations. For more information, see [Prepare For Creating a Trail For Your Organization](../userguide/creating-an-organizational-trail-prepare.md "../userguide/creating-an-organizational-trail-prepare.md") or [Organization event data stores](../userguide/cloudtrail-lake-organizations.md "../userguide/cloudtrail-lake-organizations.md").


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




## Examples


### Example


The following example shows how to disable CloudTrail Lake federation on an event data store.



```
{
   "EventDataStore": "arn:aws:cloudtrail:us-east-2:123456789012:eventdatastore/EXAMPLE-f852-4e8f-8bd1-bcf6cEXAMPLE"
}
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/DisableFederation "https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/DisableFederation")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudtrail-2013-11-01/DisableFederation "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudtrail-2013-11-01/DisableFederation")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/DisableFederation "https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/DisableFederation")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/DisableFederation "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/DisableFederation")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/DisableFederation "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/DisableFederation")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/DisableFederation "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/DisableFederation")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/DisableFederation "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/DisableFederation")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/DisableFederation "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/DisableFederation")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/DisableFederation "https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/DisableFederation")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/DisableFederation "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/DisableFederation")
