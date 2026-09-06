

# ProvisionedCapacity
<a name="API_ProvisionedCapacity"></a>

Details about a connector's provisioned capacity.

## Contents
<a name="API_ProvisionedCapacity_Contents"></a>

 ** mcuCount **   <a name="MSKC-Type-ProvisionedCapacity-mcuCount"></a>
The number of microcontroller units (MCUs) allocated to each connector worker. The valid values are 1,2,4,8.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 8.  
Required: Yes

 ** workerCount **   <a name="MSKC-Type-ProvisionedCapacity-workerCount"></a>
The number of workers that are allocated to the connector.  
Type: Integer  
Required: Yes

## See Also
<a name="API_ProvisionedCapacity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kafkaconnect-2021-09-14/ProvisionedCapacity) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kafkaconnect-2021-09-14/ProvisionedCapacity) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kafkaconnect-2021-09-14/ProvisionedCapacity) 