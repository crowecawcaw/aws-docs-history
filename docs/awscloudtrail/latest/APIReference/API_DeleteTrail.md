# DeleteTrail

Deletes a trail. This operation must be called from the Region in which the trail was
 created. `DeleteTrail` cannot be called on the shadow trails (replicated trails
 in other Regions) of a trail that is enabled in all Regions.

###### Important


 While deleting a CloudTrail trail is an irreversible action, CloudTrail does not
 delete log files in the Amazon S3 bucket for that trail, the Amazon S3 bucket itself, or the
 CloudWatchlog group to which the trail delivers events. Deleting a multi-Region trail
 will stop logging of events in all AWS Regions enabled in your AWS account. Deleting a
 single-Region trail will stop logging of events in that Region only. It will not stop
 logging of events in other Regions even if the trails in those other Regions have
 identical names to the deleted trail.
 

For information about account closure and deletion of CloudTrail trails, see [https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-account-closure.html](../userguide/cloudtrail-account-closure.md "../userguide/cloudtrail-account-closure.md").


## Request Syntax



```
{
   "Name": "`string`"
}
```

## Request Parameters


For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").


The request accepts the following data in JSON format.





**[Name](#API_DeleteTrail_RequestSyntax "#API_DeleteTrail_RequestSyntax")**


Specifies the name or the CloudTrail ARN of the trail to be deleted. The
 following is the format of a trail ARN.
 `arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail`



Type: String


Required: Yes




## Response Elements


If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.


## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**CloudTrailARNInvalidException** 


This exception is thrown when an operation is called with an ARN that is not valid.


The following is the format of a trail ARN: `arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail`



The following is the format of an event data store ARN:
 `arn:aws:cloudtrail:us-east-2:123456789012:eventdatastore/EXAMPLE-f852-4e8f-8bd1-bcf6cEXAMPLE`



The following is the format of a dashboard ARN: `arn:aws:cloudtrail:us-east-1:123456789012:dashboard/exampleDash`



The following is the format of a channel ARN:
 `arn:aws:cloudtrail:us-east-2:123456789012:channel/01234567890`



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




**InvalidHomeRegionException** 


This exception is thrown when an operation is called on a trail from a Region other than
 the Region in which the trail was created.


HTTP Status Code: 400




**InvalidTrailNameException** 


This exception is thrown when the provided trail name is not valid. Trail names must
 meet the following requirements:



* Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores
 (\_), or dashes (-)
* Start with a letter or number, and end with a letter or number
* Be between 3 and 128 characters
* Have no adjacent periods, underscores or dashes. Names like
 `my-_namespace` and `my--namespace` are not valid.
* Not be in IP address format (for example, 192.168.5.4)

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




**ThrottlingException** 



 This exception is thrown when the request rate exceeds the limit. 
 


HTTP Status Code: 400




**TrailNotFoundException** 


This exception is thrown when the trail with the given name is not found.


HTTP Status Code: 400




**UnsupportedOperationException** 


This exception is thrown when the requested operation is not supported.


HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/DeleteTrail "https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/DeleteTrail")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudtrail-2013-11-01/DeleteTrail "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudtrail-2013-11-01/DeleteTrail")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/DeleteTrail "https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/DeleteTrail")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/DeleteTrail "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/DeleteTrail")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/DeleteTrail "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/DeleteTrail")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/DeleteTrail "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/DeleteTrail")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/DeleteTrail "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/DeleteTrail")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/DeleteTrail "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/DeleteTrail")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/DeleteTrail "https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/DeleteTrail")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/DeleteTrail "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/DeleteTrail")
