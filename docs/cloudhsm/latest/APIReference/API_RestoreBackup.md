# RestoreBackup

Restores a specified AWS CloudHSM backup that is in the
 `PENDING_DELETION` state. For more information on deleting a backup, see
 [DeleteBackup](API_DeleteBackup.md "API_DeleteBackup.md").


**Cross-account use:** No. You cannot perform this operation on an AWS CloudHSM backup in a different AWS account.


## Request Syntax



```
{
   "BackupId": "`string`"
}
```

## Request Parameters


For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").


The request accepts the following data in JSON format.





**[BackupId](#API_RestoreBackup_RequestSyntax "#API_RestoreBackup_RequestSyntax")**


The ID of the backup to be restored. To find the ID of a backup, use the [DescribeBackups](API_DescribeBackups.md "API_DescribeBackups.md") operation.


Type: String


Pattern: `backup-[2-7a-zA-Z]{11,16}`



Required: Yes




## Response Syntax



```
{
   "Backup": { 
      "BackupArn": "***string***",
      "BackupId": "***string***",
      "BackupState": "***string***",
      "ClusterId": "***string***",
      "CopyTimestamp": ***number***,
      "CreateTimestamp": ***number***,
      "DeleteTimestamp": ***number***,
      "HsmType": "***string***",
      "Mode": "***string***",
      "NeverExpires": ***boolean***,
      "SourceBackup": "***string***",
      "SourceCluster": "***string***",
      "SourceRegion": "***string***",
      "TagList": [ 
         { 
            "Key": "***string***",
            "Value": "***string***"
         }
      ]
   }
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[Backup](#API_RestoreBackup_ResponseSyntax "#API_RestoreBackup_ResponseSyntax")**


Information on the `Backup` object created.


Type: [Backup](API_Backup.md "API_Backup.md") object




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




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudhsmv2-2017-04-28/RestoreBackup "https://docs.aws.amazon.com/goto/cli2/cloudhsmv2-2017-04-28/RestoreBackup")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudhsmv2-2017-04-28/RestoreBackup "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudhsmv2-2017-04-28/RestoreBackup")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudhsmv2-2017-04-28/RestoreBackup "https://docs.aws.amazon.com/goto/SdkForCpp/cloudhsmv2-2017-04-28/RestoreBackup")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudhsmv2-2017-04-28/RestoreBackup "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudhsmv2-2017-04-28/RestoreBackup")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudhsmv2-2017-04-28/RestoreBackup "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudhsmv2-2017-04-28/RestoreBackup")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudhsmv2-2017-04-28/RestoreBackup "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudhsmv2-2017-04-28/RestoreBackup")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudhsmv2-2017-04-28/RestoreBackup "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudhsmv2-2017-04-28/RestoreBackup")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudhsmv2-2017-04-28/RestoreBackup "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudhsmv2-2017-04-28/RestoreBackup")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudhsmv2-2017-04-28/RestoreBackup "https://docs.aws.amazon.com/goto/boto3/cloudhsmv2-2017-04-28/RestoreBackup")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudhsmv2-2017-04-28/RestoreBackup "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudhsmv2-2017-04-28/RestoreBackup")
