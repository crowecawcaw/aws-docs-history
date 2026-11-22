

# AzureEventHubConfiguration

Configuration of the Azure Event Hubs that the setup creates to deliver resource logs.

## Contents
<a name="API_AzureEventHubConfiguration_Contents"></a>

 ** PartitionCount **   <a name="cwoa-Type-AzureEventHubConfiguration-PartitionCount"></a>
The number of partitions in each Event Hub. The Standard tier allows 1–32 partitions and the Premium tier allows 1–100. On the Standard tier, you can't change this value after the setup creates the Event Hub.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: Yes

 ** Tier **   <a name="cwoa-Type-AzureEventHubConfiguration-Tier"></a>
The Event Hubs namespace tier.  
Type: String  
Valid Values: `Standard | Premium`   
Required: Yes

## See Also
<a name="API_AzureEventHubConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/AzureEventHubConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/AzureEventHubConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/AzureEventHubConfiguration) 