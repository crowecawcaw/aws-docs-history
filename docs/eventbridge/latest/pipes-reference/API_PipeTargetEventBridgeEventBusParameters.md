

# PipeTargetEventBridgeEventBusParameters
<a name="API_PipeTargetEventBridgeEventBusParameters"></a>

The parameters for using an EventBridge event bus as a target.

## Contents
<a name="API_PipeTargetEventBridgeEventBusParameters_Contents"></a>

 ** DetailType **   <a name="eventbridge-Type-PipeTargetEventBridgeEventBusParameters-DetailType"></a>
A free-form string, with a maximum of 128 characters, used to decide what fields to expect in the event detail.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Required: No

 ** EndpointId **   <a name="eventbridge-Type-PipeTargetEventBridgeEventBusParameters-EndpointId"></a>
The URL subdomain of the endpoint. For example, if the URL for Endpoint is https://abcde.veo.endpoints.event.amazonaws.com, then the EndpointId is `abcde.veo`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 50.  
Pattern: `[A-Za-z0-9\-]+[\.][A-Za-z0-9\-]+`   
Required: No

 ** Resources **   <a name="eventbridge-Type-PipeTargetEventBridgeEventBusParameters-Resources"></a>
 AWS resources, identified by Amazon Resource Name (ARN), which the event primarily concerns. Any number, including zero, may be present.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 10 items.  
Length Constraints: Minimum length of 1. Maximum length of 1600.  
Pattern: `arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-]+):([a-z]{2,4}((-gov)|(-de)|(-iso([a-z]?)))?-[a-z]+(-\d{1})?)?:(\d{12})?:(.+)|(\$(\.[\w/_-]+(\[(\d+|\*)\])*)*)`   
Required: No

 ** Source **   <a name="eventbridge-Type-PipeTargetEventBridgeEventBusParameters-Source"></a>
The source of the event.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `.*(?=[/\.\-_A-Za-z0-9]+)((?!aws\.).*)|(\$(\.[\w/_-]+(\[(\d+|\*)\])*)*).*`   
Required: No

 ** Time **   <a name="eventbridge-Type-PipeTargetEventBridgeEventBusParameters-Time"></a>
The time stamp of the event, per [RFC3339](https://www.rfc-editor.org/rfc/rfc3339.txt). If no time stamp is provided, the time stamp of the [PutEvents](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutEvents.html) call is used.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `\$(\.[\w/_-]+(\[(\d+|\*)\])*)*`   
Required: No

## See Also
<a name="API_PipeTargetEventBridgeEventBusParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pipes-2015-10-07/PipeTargetEventBridgeEventBusParameters) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pipes-2015-10-07/PipeTargetEventBridgeEventBusParameters) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pipes-2015-10-07/PipeTargetEventBridgeEventBusParameters) 