# PipeEnrichmentHttpParameters

These are custom parameter to be used when the target is an API Gateway REST APIs
or EventBridge ApiDestinations. In the latter case, these are merged with any
InvocationParameters specified on the Connection, with any values from the Connection
taking precedence.

## Contents

**HeaderParameters**

The headers that need to be sent as part of request invoking the API Gateway REST
API or EventBridge ApiDestination.

Type: String to string map

Key Length Constraints: Minimum length of 0. Maximum length of 512.

Key Pattern: `[!#$%&'*+-.^_`|~0-9a-zA-Z]+|(\$(\.[\w/_-]+(\[(\d+|\*)\])_)_)`

Value Length Constraints: Minimum length of 0. Maximum length of 512.

Value Pattern: `[ \t]*[\x20-\x7E]+([ \t]+[\x20-\x7E]+)*[ \t]*|(\$(\.[\w/_-]+(\[(\d+|\*)\])*)*)`

Required: No

**PathParameterValues**

The path parameter values to be used to populate API Gateway REST API or EventBridge ApiDestination path wildcards ("\*").

Type: Array of strings

Pattern: `(?!\s*$).+|(\$(\.[\w/_-]+(\[(\d+|\*)\])*)*)`

Required: No

**QueryStringParameters**

The query string keys/values that need to be sent as part of request invoking the
API Gateway REST API or EventBridge ApiDestination.

Type: String to string map

Key Length Constraints: Minimum length of 0. Maximum length of 512.

Key Pattern: `[^\x00-\x1F\x7F]+|(\$(\.[\w/_-]+(\[(\d+|\*)\])*)*)`

Value Length Constraints: Minimum length of 0. Maximum length of 512.

Value Pattern: `[^\x00-\x09\x0B\x0C\x0E-\x1F\x7F]+|(\$(\.[\w/_-]+(\[(\d+|\*)\])*)*)`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/pipes-2015-10-07/PipeEnrichmentHttpParameters.md "../../../goto/SdkForCpp/pipes-2015-10-07/PipeEnrichmentHttpParameters.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/pipes-2015-10-07/PipeEnrichmentHttpParameters.md "../../../goto/SdkForJavaV2/pipes-2015-10-07/PipeEnrichmentHttpParameters.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/pipes-2015-10-07/PipeEnrichmentHttpParameters.md "../../../goto/SdkForRubyV3/pipes-2015-10-07/PipeEnrichmentHttpParameters.md")
