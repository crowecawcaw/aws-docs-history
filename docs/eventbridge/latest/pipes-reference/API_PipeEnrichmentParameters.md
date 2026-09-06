

# PipeEnrichmentParameters
<a name="API_PipeEnrichmentParameters"></a>

The parameters required to set up enrichment on your pipe.

## Contents
<a name="API_PipeEnrichmentParameters_Contents"></a>

 ** HttpParameters **   <a name="eventbridge-Type-PipeEnrichmentParameters-HttpParameters"></a>
Contains the HTTP parameters to use when the target is a API Gateway REST endpoint or EventBridge ApiDestination.  
If you specify an API Gateway REST API or EventBridge ApiDestination as a target, you can use this parameter to specify headers, path parameters, and query string keys/values as part of your target invoking request. If you're using ApiDestinations, the corresponding Connection can also have these values configured. In case of any conflicting keys, values from the Connection take precedence.  
Type: [PipeEnrichmentHttpParameters](API_PipeEnrichmentHttpParameters.md) object  
Required: No

 ** InputTemplate **   <a name="eventbridge-Type-PipeEnrichmentParameters-InputTemplate"></a>
Valid JSON text passed to the enrichment. In this case, nothing from the event itself is passed to the enrichment. For more information, see [The JavaScript Object Notation (JSON) Data Interchange Format](http://www.rfc-editor.org/rfc/rfc7159.txt).  
To remove an input template, specify an empty string.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 8192.  
Required: No

## See Also
<a name="API_PipeEnrichmentParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pipes-2015-10-07/PipeEnrichmentParameters) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pipes-2015-10-07/PipeEnrichmentParameters) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pipes-2015-10-07/PipeEnrichmentParameters) 