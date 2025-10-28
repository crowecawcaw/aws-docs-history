# PipeTargetEventBridgeEventBusParameters

The parameters for using an EventBridge event bus as a target.

## Contents

**DetailType**

A free-form string, with a maximum of 128 characters, used to decide what fields to
expect in the event detail.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Required: No

**EndpointId**

The URL subdomain of the endpoint. For example, if the URL for Endpoint is
https://abcde.veo.endpoints.event.amazonaws.com, then the EndpointId is
`abcde.veo`.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 50.

Pattern: `[A-Za-z0-9\-]+[\.][A-Za-z0-9\-]+`

Required: No

**Resources**

AWS resources, identified by Amazon Resource Name (ARN), which the event
primarily concerns. Any number, including zero, may be present.

Type: Array of strings

Array Members: Minimum number of 0 items. Maximum number of 10 items.

Length Constraints: Minimum length of 1. Maximum length of 1600.

Pattern: `arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-]+):([a-z]{2,4}((-gov)|(-de)|(-iso([a-z]?)))?-[a-z]+(-\d{1})?)?:(\d{12})?:(.+)|(\$(\.[\w/_-]+(\[(\d+|\*)\])*)*)`

Required: No

**Source**

The source of the event.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `.*(?=[/\.\-_A-Za-z0-9]+)((?!aws\.).*)|(\$(\.[\w/_-]+(\[(\d+|\*)\])*)*).*`

Required: No

**Time**

The time stamp of the event, per [RFC3339](https://www.rfc-editor.org/rfc/rfc3339.txt "https://www.rfc-editor.org/rfc/rfc3339.txt"). If no time stamp is provided, the time stamp of the [PutEvents](../APIReference/API_PutEvents.md "../APIReference/API_PutEvents.md") call is used.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `\$(\.[\w/_-]+(\[(\d+|\*)\])*)*`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/pipes-2015-10-07/PipeTargetEventBridgeEventBusParameters.md "../../../goto/SdkForCpp/pipes-2015-10-07/PipeTargetEventBridgeEventBusParameters.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/pipes-2015-10-07/PipeTargetEventBridgeEventBusParameters.md "../../../goto/SdkForJavaV2/pipes-2015-10-07/PipeTargetEventBridgeEventBusParameters.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/pipes-2015-10-07/PipeTargetEventBridgeEventBusParameters.md "../../../goto/SdkForRubyV3/pipes-2015-10-07/PipeTargetEventBridgeEventBusParameters.md")
