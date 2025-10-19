# CopyBackupToRegion

Copy an AWS CloudHSM cluster backup to a different region.


**Cross-account use:** No. You cannot perform this operation on an AWS CloudHSM backup in a different AWS account.


## Request Syntax



```
{
   "BackupId": "`string`",
   "DestinationRegion": "`string`",
   "TagList": [ 
      { 
         "Key": "`string`",
         "Value": "`string`"
      }
   ]
}
```

## Request Parameters


For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").


The request accepts the following data in JSON format.





**[BackupId](#API_CopyBackupToRegion_RequestSyntax "#API_CopyBackupToRegion_RequestSyntax")**


The ID of the backup that will be copied to the destination region. 


Type: String


Pattern: `backup-[2-7a-zA-Z]{11,16}`



Required: Yes




**[DestinationRegion](#API_CopyBackupToRegion_RequestSyntax "#API_CopyBackupToRegion_RequestSyntax")**


The AWS region that will contain your copied AWS CloudHSM cluster backup.


Type: String


Pattern: `[a-z]{2}(-(gov))?-(east|west|north|south|central){1,2}-\d`



Required: Yes




**[TagList](#API_CopyBackupToRegion_RequestSyntax "#API_CopyBackupToRegion_RequestSyntax")**


Tags to apply to the destination backup during creation. If you specify tags, only these tags will be applied to the destination backup. If you do not specify tags, the service copies tags from the source backup to the destination backup.


Type: Array of [Tag](API_Tag.md "API_Tag.md") objects


Array Members: Minimum number of 1 item. Maximum number of 50 items.


Required: No




## Response Syntax



```
{
   "DestinationBackup": { 
      "CreateTimestamp": ***number***,
      "SourceBackup": "***string***",
      "SourceCluster": "***string***",
      "SourceRegion": "***string***"
   }
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[DestinationBackup](#API_CopyBackupToRegion_ResponseSyntax "#API_CopyBackupToRegion_ResponseSyntax")**


Information on the backup that will be copied to the destination region, including
 CreateTimestamp, SourceBackup, SourceCluster, and Source Region. CreateTimestamp of the
 destination backup will be the same as that of the source backup.


You will need to use the `sourceBackupID` returned in this operation to use
 the [DescribeBackups](API_DescribeBackups.md "API_DescribeBackups.md") operation on the backup that will be copied to the
 destination region.


Type: [DestinationBackup](API_DestinationBackup.md "API_DestinationBackup.md") object




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**CloudHsmAccessDeniedException** 


The request was rejected because the requester does not have permission to perform the
 requested operation.


HTTP Status Code: 400




**CloudHsmInternalFailureException** 


The request was rejected because of an AWS CloudHSM internal failure. The request can
 be retried.


HTTP Status Code: 500




**CloudHsmInvalidRequestException** 


The request was rejected because it is not a valid request.


HTTP Status Code: 400




**CloudHsmResourceNotFoundException** 


The request was rejected because it refers to a resource that cannot be
 found.


HTTP Status Code: 400




**CloudHsmServiceException** 


The request was rejected because an error occurred.


HTTP Status Code: 400




**CloudHsmTagException** 


The request was rejected because of a tagging failure. Verify the tag conditions in all applicable policies, and then retry the request.


HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudhsmv2-2017-04-28/CopyBackupToRegion "https://docs.aws.amazon.com/goto/cli2/cloudhsmv2-2017-04-28/CopyBackupToRegion")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudhsmv2-2017-04-28/CopyBackupToRegion "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudhsmv2-2017-04-28/CopyBackupToRegion")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudhsmv2-2017-04-28/CopyBackupToRegion "https://docs.aws.amazon.com/goto/SdkForCpp/cloudhsmv2-2017-04-28/CopyBackupToRegion")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudhsmv2-2017-04-28/CopyBackupToRegion "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudhsmv2-2017-04-28/CopyBackupToRegion")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudhsmv2-2017-04-28/CopyBackupToRegion "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudhsmv2-2017-04-28/CopyBackupToRegion")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudhsmv2-2017-04-28/CopyBackupToRegion "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudhsmv2-2017-04-28/CopyBackupToRegion")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudhsmv2-2017-04-28/CopyBackupToRegion "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudhsmv2-2017-04-28/CopyBackupToRegion")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudhsmv2-2017-04-28/CopyBackupToRegion "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudhsmv2-2017-04-28/CopyBackupToRegion")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudhsmv2-2017-04-28/CopyBackupToRegion "https://docs.aws.amazon.com/goto/boto3/cloudhsmv2-2017-04-28/CopyBackupToRegion")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudhsmv2-2017-04-28/CopyBackupToRegion "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudhsmv2-2017-04-28/CopyBackupToRegion")
