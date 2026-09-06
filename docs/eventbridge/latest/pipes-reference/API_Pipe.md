

# Pipe
<a name="API_Pipe"></a>

An object that represents a pipe. Amazon EventBridgePipes connect event sources to targets and reduces the need for specialized knowledge and integration code.

## Contents
<a name="API_Pipe_Contents"></a>

 ** Arn **   <a name="eventbridge-Type-Pipe-Arn"></a>
The ARN of the pipe.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1600.  
Pattern: `arn:aws([a-z]|\-)*:([a-zA-Z0-9\-]+):([a-z]|\d|\-)*:([0-9]{12})?:(.+)`   
Required: No

 ** CreationTime **   <a name="eventbridge-Type-Pipe-CreationTime"></a>
The time the pipe was created.  
Type: Timestamp  
Required: No

 ** CurrentState **   <a name="eventbridge-Type-Pipe-CurrentState"></a>
The state the pipe is in.  
Type: String  
Valid Values: `RUNNING | STOPPED | CREATING | UPDATING | DELETING | STARTING | STOPPING | CREATE_FAILED | UPDATE_FAILED | START_FAILED | STOP_FAILED | DELETE_FAILED | CREATE_ROLLBACK_FAILED | DELETE_ROLLBACK_FAILED | UPDATE_ROLLBACK_FAILED`   
Required: No

 ** DesiredState **   <a name="eventbridge-Type-Pipe-DesiredState"></a>
The state the pipe should be in.  
Type: String  
Valid Values: `RUNNING | STOPPED`   
Required: No

 ** Enrichment **   <a name="eventbridge-Type-Pipe-Enrichment"></a>
The ARN of the enrichment resource.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1600.  
Pattern: `$|arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-]+):([a-z]{2,4}((-gov)|(-de)|(-iso([a-z]?)))?-[a-z]+(-\d{1})?)?:(\d{12})?:(.+)`   
Required: No

 ** LastModifiedTime **   <a name="eventbridge-Type-Pipe-LastModifiedTime"></a>
When the pipe was last updated, in [ISO-8601 format](https://www.w3.org/TR/NOTE-datetime) (YYYY-MM-DDThh:mm:ss.sTZD).  
Type: Timestamp  
Required: No

 ** Name **   <a name="eventbridge-Type-Pipe-Name"></a>
The name of the pipe.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[\.\-_A-Za-z0-9]+`   
Required: No

 ** Source **   <a name="eventbridge-Type-Pipe-Source"></a>
The ARN of the source resource.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1600.  
Pattern: `smk://(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9]):[0-9]{1,5}|arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-]+):([a-z]{2,4}((-gov)|(-de)|(-iso([a-z]?)))?-[a-z]+(-\d{1})?)?:(\d{12})?:(.+)`   
Required: No

 ** StateReason **   <a name="eventbridge-Type-Pipe-StateReason"></a>
The reason the pipe is in its current state.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 512.  
Pattern: `.*`   
Required: No

 ** Target **   <a name="eventbridge-Type-Pipe-Target"></a>
The ARN of the target resource.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1600.  
Pattern: `arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-]+):([a-z]{2,4}((-gov)|(-de)|(-iso([a-z]?)))?-[a-z]+(-\d{1})?)?:(\d{12})?:(.+)`   
Required: No

## See Also
<a name="API_Pipe_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pipes-2015-10-07/Pipe) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pipes-2015-10-07/Pipe) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pipes-2015-10-07/Pipe) 