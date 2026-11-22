

# ThirdPartyTelemetryEnrichmentSummary

Summary information about a third-party telemetry enrichment, as returned by `ListThirdPartyTelemetryEnrichments`.

## Contents
<a name="API_ThirdPartyTelemetryEnrichmentSummary_Contents"></a>

 ** Name **   <a name="cwoa-Type-ThirdPartyTelemetryEnrichmentSummary-Name"></a>
The name of the enrichment.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-zA-Z][a-zA-Z0-9\-]*`   
Required: No

 ** Status **   <a name="cwoa-Type-ThirdPartyTelemetryEnrichmentSummary-Status"></a>
The current status of the enrichment. Valid values:  
+  `Initializing` - CloudWatch is setting up the enrichment. Some telemetry can be enriched before setup completes.
+  `Running` - The enrichment is active.
+  `Stopped` - The enrichment is stopped.
+  `Impaired` - The enrichment has a problem. `StatusReason` describes the problem.
Type: String  
Valid Values: `Initializing | Running | Stopped | Impaired`   
Required: No

 ** TelemetrySource **   <a name="cwoa-Type-ThirdPartyTelemetryEnrichmentSummary-TelemetrySource"></a>
The third-party telemetry source of the enrichment.  
Type: String  
Valid Values: `Azure`   
Required: No

## See Also
<a name="API_ThirdPartyTelemetryEnrichmentSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/ThirdPartyTelemetryEnrichmentSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/ThirdPartyTelemetryEnrichmentSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/ThirdPartyTelemetryEnrichmentSummary) 