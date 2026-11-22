

# TelemetryManifestSource

The resources to collect telemetry from, for one cloud provider. Specify one provider.

## Contents
<a name="API_TelemetryManifestSource_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** Azure **   <a name="cwoa-Type-TelemetryManifestSource-Azure"></a>
The Azure scope items. Each `AzureScopeItem` specifies a set of Azure resources and the telemetry types to collect from them. You can specify up to 100 scope items.  
Type: Array of [AzureScopeItem](API_AzureScopeItem.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 100 items.  
Required: No

## See Also
<a name="API_TelemetryManifestSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/TelemetryManifestSource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/TelemetryManifestSource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/TelemetryManifestSource) 