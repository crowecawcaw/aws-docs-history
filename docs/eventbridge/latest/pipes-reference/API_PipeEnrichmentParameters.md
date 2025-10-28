# PipeEnrichmentParameters

The parameters required to set up enrichment on your pipe.

## Contents

**HttpParameters**

Contains the HTTP parameters to use when the target is a API Gateway REST
endpoint or EventBridge ApiDestination.

If you specify an API Gateway REST API or EventBridge ApiDestination as a
target, you can use this parameter to specify headers, path parameters, and query string
keys/values as part of your target invoking request. If you're using ApiDestinations, the
corresponding Connection can also have these values configured. In case of any conflicting
keys, values from the Connection take precedence.

Type: [PipeEnrichmentHttpParameters](API_PipeEnrichmentHttpParameters.md "API_PipeEnrichmentHttpParameters.md") object

Required: No

**InputTemplate**

Valid JSON text passed to the enrichment. In this case, nothing from the event itself is
passed to the enrichment. For more information, see [The JavaScript Object Notation (JSON)
Data Interchange Format](http://www.rfc-editor.org/rfc/rfc7159.txt "http://www.rfc-editor.org/rfc/rfc7159.txt").

To remove an input template, specify an empty string.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 8192.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/pipes-2015-10-07/PipeEnrichmentParameters.md "../../../goto/SdkForCpp/pipes-2015-10-07/PipeEnrichmentParameters.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/pipes-2015-10-07/PipeEnrichmentParameters.md "../../../goto/SdkForJavaV2/pipes-2015-10-07/PipeEnrichmentParameters.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/pipes-2015-10-07/PipeEnrichmentParameters.md "../../../goto/SdkForRubyV3/pipes-2015-10-07/PipeEnrichmentParameters.md")
