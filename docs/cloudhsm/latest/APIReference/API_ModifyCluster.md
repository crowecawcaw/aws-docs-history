# ModifyCluster

Modifies AWS CloudHSM cluster.


**Cross-account use:** No. You cannot perform this operation on an AWS CloudHSM cluster in a different AWS account.


## Request Syntax



```
{
   "BackupRetentionPolicy": { 
      "Type": "`string`",
      "Value": "`string`"
   },
   "ClusterId": "`string`",
   "HsmType": "`string`"
}
```

## Request Parameters


For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").


The request accepts the following data in JSON format.





**[BackupRetentionPolicy](#API_ModifyCluster_RequestSyntax "#API_ModifyCluster_RequestSyntax")**


A policy that defines how the service retains backups.


Type: [BackupRetentionPolicy](API_BackupRetentionPolicy.md "API_BackupRetentionPolicy.md") object


Required: No




**[ClusterId](#API_ModifyCluster_RequestSyntax "#API_ModifyCluster_RequestSyntax")**


The identifier (ID) of the cluster that you want to modify. To find the cluster ID, use
 [DescribeClusters](API_DescribeClusters.md "API_DescribeClusters.md").


Type: String


Pattern: `cluster-[2-7a-zA-Z]{11,16}`



Required: Yes




**[HsmType](#API_ModifyCluster_RequestSyntax "#API_ModifyCluster_RequestSyntax")**


The desired HSM type of the cluster.


Type: String


Length Constraints: Maximum length of 32.


Pattern: `((p|)hsm[0-9][a-z.]*\.[a-zA-Z]+)`



Required: No




## Response Syntax



```
{
   "Cluster": { 
      "BackupPolicy": "***string***",
      "BackupRetentionPolicy": { 
         "Type": "***string***",
         "Value": "***string***"
      },
      "Certificates": { 
         "AwsHardwareCertificate": "***string***",
         "ClusterCertificate": "***string***",
         "ClusterCsr": "***string***",
         "HsmCertificate": "***string***",
         "ManufacturerHardwareCertificate": "***string***"
      },
      "ClusterId": "***string***",
      "CreateTimestamp": ***number***,
      "Hsms": [ 
         { 
            "AvailabilityZone": "***string***",
            "ClusterId": "***string***",
            "EniId": "***string***",
            "EniIp": "***string***",
            "EniIpV6": "***string***",
            "HsmId": "***string***",
            "HsmType": "***string***",
            "State": "***string***",
            "StateMessage": "***string***",
            "SubnetId": "***string***"
         }
      ],
      "HsmType": "***string***",
      "HsmTypeRollbackExpiration": ***number***,
      "Mode": "***string***",
      "NetworkType": "***string***",
      "PreCoPassword": "***string***",
      "SecurityGroup": "***string***",
      "SourceBackupId": "***string***",
      "State": "***string***",
      "StateMessage": "***string***",
      "SubnetMapping": { 
         "***string***" : "***string***" 
      },
      "TagList": [ 
         { 
            "Key": "***string***",
            "Value": "***string***"
         }
      ],
      "VpcId": "***string***"
   }
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[Cluster](#API_ModifyCluster_ResponseSyntax "#API_ModifyCluster_ResponseSyntax")**


Contains information about an AWS CloudHSM cluster.


Type: [Cluster](API_Cluster.md "API_Cluster.md") object




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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudhsmv2-2017-04-28/ModifyCluster "https://docs.aws.amazon.com/goto/cli2/cloudhsmv2-2017-04-28/ModifyCluster")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudhsmv2-2017-04-28/ModifyCluster "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudhsmv2-2017-04-28/ModifyCluster")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudhsmv2-2017-04-28/ModifyCluster "https://docs.aws.amazon.com/goto/SdkForCpp/cloudhsmv2-2017-04-28/ModifyCluster")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudhsmv2-2017-04-28/ModifyCluster "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudhsmv2-2017-04-28/ModifyCluster")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudhsmv2-2017-04-28/ModifyCluster "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudhsmv2-2017-04-28/ModifyCluster")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudhsmv2-2017-04-28/ModifyCluster "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudhsmv2-2017-04-28/ModifyCluster")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudhsmv2-2017-04-28/ModifyCluster "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudhsmv2-2017-04-28/ModifyCluster")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudhsmv2-2017-04-28/ModifyCluster "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudhsmv2-2017-04-28/ModifyCluster")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudhsmv2-2017-04-28/ModifyCluster "https://docs.aws.amazon.com/goto/boto3/cloudhsmv2-2017-04-28/ModifyCluster")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudhsmv2-2017-04-28/ModifyCluster "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudhsmv2-2017-04-28/ModifyCluster")
