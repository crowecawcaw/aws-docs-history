# DescribeBackups

Gets information about backups of AWS CloudHSM clusters. Lists either the backups you own or the backups shared with you when the Shared parameter is true.

This is a paginated operation, which means that each response might contain only a
 subset of all the backups. When the response contains only a subset of backups, it includes a
 `NextToken` value. Use this value in a subsequent `DescribeBackups`
 request to get more backups. When you receive a response with no `NextToken` (or an
 empty or null value), that means there are no more backups to get.


**Cross-account use:** Yes. Customers can describe backups in other AWS accounts that are shared with them.


## Request Syntax



```
{
   "Filters": { 
      "`string`" : [ "`string`" ]
   },
   "MaxResults": `number`,
   "NextToken": "`string`",
   "Shared": `boolean`,
   "SortAscending": `boolean`
}
```

## Request Parameters


For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").


The request accepts the following data in JSON format.





**[Filters](#API_DescribeBackups_RequestSyntax "#API_DescribeBackups_RequestSyntax")**


One or more filters to limit the items returned in the response.


Use the `backupIds` filter to return only the specified backups. Specify
 backups by their backup identifier (ID).


Use the `sourceBackupIds` filter to return only the backups created from a
 source backup. The `sourceBackupID` of a source backup is returned by the [CopyBackupToRegion](API_CopyBackupToRegion.md "API_CopyBackupToRegion.md") operation.


Use the `clusterIds` filter to return only the backups for the specified
 clusters. Specify clusters by their cluster identifier (ID).


Use the `states` filter to return only backups that match the specified
 state.


Use the `neverExpires` filter to return backups filtered by the value in the
 `neverExpires` parameter. `True` returns all backups exempt from the
 backup retention policy. `False` returns all backups with a backup retention policy
 defined at the cluster.


Type: String to array of strings map


Map Entries: Maximum number of 30 items.


Key Pattern: `[a-zA-Z0-9_-]+`



Required: No




**[MaxResults](#API_DescribeBackups_RequestSyntax "#API_DescribeBackups_RequestSyntax")**


The maximum number of backups to return in the response. When there are more backups
 than the number you specify, the response contains a `NextToken` value.


Type: Integer


Valid Range: Minimum value of 1. Maximum value of 50.


Required: No




**[NextToken](#API_DescribeBackups_RequestSyntax "#API_DescribeBackups_RequestSyntax")**


The `NextToken` value that you received in the previous response. Use this
 value to get more backups.


Type: String


Length Constraints: Maximum length of 256.


Pattern: `.*`



Required: No




**[Shared](#API_DescribeBackups_RequestSyntax "#API_DescribeBackups_RequestSyntax")**


Describe backups that are shared with you.


###### Note

By default when using this option, the command returns backups that have been shared using a standard AWS Resource Access Manager 
 resource share. In order for a backup that was shared using the PutResourcePolicy command to be returned, the share must be promoted to a 
 standard resource share using the AWS RAM
 [PromoteResourceShareCreatedFromPolicy](https://docs.aws.amazon.com/cli/latest/reference/ram/promote-resource-share-created-from-policy.html "https://docs.aws.amazon.com/cli/latest/reference/ram/promote-resource-share-created-from-policy.html") API operation.

 For more information about sharing backups, see  [Working with shared backups](../userguide/sharing.md "../userguide/sharing.md") in the AWS CloudHSM User Guide.


Type: Boolean


Required: No




**[SortAscending](#API_DescribeBackups_RequestSyntax "#API_DescribeBackups_RequestSyntax")**


Designates whether or not to sort the return backups by ascending chronological order
 of generation.


Type: Boolean


Required: No




## Response Syntax



```
{
   "Backups": [ 
      { 
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
   ],
   "NextToken": "***string***"
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[Backups](#API_DescribeBackups_ResponseSyntax "#API_DescribeBackups_ResponseSyntax")**


A list of backups.


Type: Array of [Backup](API_Backup.md "API_Backup.md") objects




**[NextToken](#API_DescribeBackups_ResponseSyntax "#API_DescribeBackups_ResponseSyntax")**


An opaque string that indicates that the response contains only a subset of backups.
 Use this value in a subsequent `DescribeBackups` request to get more
 backups.


Type: String


Length Constraints: Maximum length of 256.


Pattern: `.*`





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



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudhsmv2-2017-04-28/DescribeBackups "https://docs.aws.amazon.com/goto/cli2/cloudhsmv2-2017-04-28/DescribeBackups")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudhsmv2-2017-04-28/DescribeBackups "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudhsmv2-2017-04-28/DescribeBackups")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudhsmv2-2017-04-28/DescribeBackups "https://docs.aws.amazon.com/goto/SdkForCpp/cloudhsmv2-2017-04-28/DescribeBackups")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudhsmv2-2017-04-28/DescribeBackups "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudhsmv2-2017-04-28/DescribeBackups")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudhsmv2-2017-04-28/DescribeBackups "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudhsmv2-2017-04-28/DescribeBackups")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudhsmv2-2017-04-28/DescribeBackups "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudhsmv2-2017-04-28/DescribeBackups")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudhsmv2-2017-04-28/DescribeBackups "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudhsmv2-2017-04-28/DescribeBackups")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudhsmv2-2017-04-28/DescribeBackups "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudhsmv2-2017-04-28/DescribeBackups")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudhsmv2-2017-04-28/DescribeBackups "https://docs.aws.amazon.com/goto/boto3/cloudhsmv2-2017-04-28/DescribeBackups")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudhsmv2-2017-04-28/DescribeBackups "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudhsmv2-2017-04-28/DescribeBackups")
