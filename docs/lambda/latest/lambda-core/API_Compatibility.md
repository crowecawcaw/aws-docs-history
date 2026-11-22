

# Compatibility

Defines the compatibility matrix for a runtime version, indicating supported integration models, architectures, and feature availability.

## Contents
<a name="API_Compatibility_Contents"></a>

 ** Architectures **   <a name="lambdacore-Type-Compatibility-Architectures"></a>
Supported architectures for the runtime version.  
Type: Array of strings  
Valid Values: `x86_64 | arm64`   
Required: No

 ** IntegrationModels **   <a name="lambdacore-Type-Compatibility-IntegrationModels"></a>
Supported integration models for the runtime version.  
Type: Array of strings  
Valid Values: `RuntimeAPI`   
Required: No

 ** ManagedInstances **   <a name="lambdacore-Type-Compatibility-ManagedInstances"></a>
Whether the runtime version is compatible with managed instances.  
Type: String  
Valid Values: `Supported | NotSupported`   
Required: No

## See Also
<a name="API_Compatibility_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-core-2026-04-30/Compatibility) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-core-2026-04-30/Compatibility) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-core-2026-04-30/Compatibility) 