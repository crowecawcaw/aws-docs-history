

# TelemetryManifest

Declares which resources in a cloud provider to collect telemetry from and which telemetry types to collect.

## Contents
<a name="API_TelemetryManifest_Contents"></a>

 ** Source **   <a name="cwoa-Type-TelemetryManifest-Source"></a>
The resources to collect telemetry from and the telemetry types to collect.  
Type: [TelemetryManifestSource](API_TelemetryManifestSource.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** Infrastructure **   <a name="cwoa-Type-TelemetryManifest-Infrastructure"></a>
The choices for the infrastructure that the setup creates in your cloud provider, such as the subscription that contains the Event Hubs and their size. If you omit this value, the setup uses default settings. If an `AzureScopeItem` collects `ResourceLogs`, you must specify at least the Azure `SubscriptionId`.  
Type: [TelemetryManifestInfrastructure](API_TelemetryManifestInfrastructure.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

## See Also
<a name="API_TelemetryManifest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/TelemetryManifest) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/TelemetryManifest) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/TelemetryManifest) 