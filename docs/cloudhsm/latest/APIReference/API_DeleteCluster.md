# DeleteCluster

Deletes the specified AWS CloudHSM cluster. Before you can delete a cluster, you must
 delete all HSMs in the cluster. To see if the cluster contains any HSMs, use [DescribeClusters](API_DescribeClusters.md "API_DescribeClusters.md"). To delete an HSM, use [DeleteHsm](API_DeleteHsm.md "API_DeleteHsm.md").


**Cross-account use:** No. You cannot perform this operation on an AWS CloudHSM cluster in a different AWS account.


## Request Syntax



```
{
   "ClusterId": "`string`"
}
```

## Request Parameters


For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").


The request accepts the following data in JSON format.





**[ClusterId](#API_DeleteCluster_RequestSyntax "#API_DeleteCluster_RequestSyntax")**


The identifier (ID) of the cluster that you are deleting. To find the cluster ID, use
 [DescribeClusters](API_DescribeClusters.md "API_DescribeClusters.md").


Type: String


Pattern: `cluster-[2-7a-zA-Z]{11,16}`



Required: Yes




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





**[Cluster](#API_DeleteCluster_ResponseSyntax "#API_DeleteCluster_ResponseSyntax")**


Information about the cluster that was deleted.


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




**CloudHsmTagException** 


The request was rejected because of a tagging failure. Verify the tag conditions in all applicable policies, and then retry the request.


HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudhsmv2-2017-04-28/DeleteCluster "https://docs.aws.amazon.com/goto/cli2/cloudhsmv2-2017-04-28/DeleteCluster")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudhsmv2-2017-04-28/DeleteCluster "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudhsmv2-2017-04-28/DeleteCluster")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudhsmv2-2017-04-28/DeleteCluster "https://docs.aws.amazon.com/goto/SdkForCpp/cloudhsmv2-2017-04-28/DeleteCluster")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudhsmv2-2017-04-28/DeleteCluster "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudhsmv2-2017-04-28/DeleteCluster")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudhsmv2-2017-04-28/DeleteCluster "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudhsmv2-2017-04-28/DeleteCluster")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudhsmv2-2017-04-28/DeleteCluster "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudhsmv2-2017-04-28/DeleteCluster")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudhsmv2-2017-04-28/DeleteCluster "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudhsmv2-2017-04-28/DeleteCluster")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudhsmv2-2017-04-28/DeleteCluster "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudhsmv2-2017-04-28/DeleteCluster")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudhsmv2-2017-04-28/DeleteCluster "https://docs.aws.amazon.com/goto/boto3/cloudhsmv2-2017-04-28/DeleteCluster")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudhsmv2-2017-04-28/DeleteCluster "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudhsmv2-2017-04-28/DeleteCluster")
