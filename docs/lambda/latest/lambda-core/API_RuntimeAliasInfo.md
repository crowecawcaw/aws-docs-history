

# RuntimeAliasInfo

Summary information about a runtime alias returned by ListRuntimeAliases.

## Contents
<a name="API_RuntimeAliasInfo_Contents"></a>

 ** Arn **   <a name="lambdacore-Type-RuntimeAliasInfo-Arn"></a>
The Amazon Resource Name (ARN) of the runtime alias.  
Type: String  
Length Constraints: Minimum length of 48. Maximum length of 2048.  
Pattern: `arn:(aws[a-zA-Z-]*):lambda:(eusc-)?[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:runtime/[a-z0-9]([a-z0-9_.-]{0,126})?[a-z0-9](/(version|alias)/[^/]{1,128})?`   
Required: Yes

 ** Created **   <a name="lambdacore-Type-RuntimeAliasInfo-Created"></a>
The date and time when the runtime alias was created.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Required: Yes

 ** LastModified **   <a name="lambdacore-Type-RuntimeAliasInfo-LastModified"></a>
The date and time when the runtime alias was last modified.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Required: Yes

 ** Name **   <a name="lambdacore-Type-RuntimeAliasInfo-Name"></a>
The name of the runtime alias.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[A-Za-z0-9_]([A-Za-z0-9_.-]{0,126}[A-Za-z0-9_])?`   
Required: Yes

 ** RuntimeVersion **   <a name="lambdacore-Type-RuntimeAliasInfo-RuntimeVersion"></a>
The name of the runtime version the alias points to.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[A-Za-z0-9_]([A-Za-z0-9_.-]{0,126}[A-Za-z0-9_])?`   
Required: Yes

 ** RuntimeVersionArn **   <a name="lambdacore-Type-RuntimeAliasInfo-RuntimeVersionArn"></a>
The Amazon Resource Name (ARN) of the runtime version the alias points to.  
Type: String  
Length Constraints: Minimum length of 48. Maximum length of 2048.  
Pattern: `arn:(aws[a-zA-Z-]*):lambda:(eusc-)?[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:runtime/[a-z0-9]([a-z0-9_.-]{0,126})?[a-z0-9](/(version|alias)/[^/]{1,128})?`   
Required: Yes

 ** State **   <a name="lambdacore-Type-RuntimeAliasInfo-State"></a>
The current state of the runtime alias.  
Type: String  
Valid Values: `CREATING | ACTIVE | UPDATING | DELETING | PENDING_DELETION`   
Required: Yes

 ** Compatibility **   <a name="lambdacore-Type-RuntimeAliasInfo-Compatibility"></a>
The compatibility matrix of the runtime version the alias points to.  
Type: [Compatibility](API_Compatibility.md) object  
Required: No

 ** Description **   <a name="lambdacore-Type-RuntimeAliasInfo-Description"></a>
A description of the runtime alias.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1024.  
Pattern: `[^\p{C}]*`   
Required: No

 ** PendingDeletionAt **   <a name="lambdacore-Type-RuntimeAliasInfo-PendingDeletionAt"></a>
Present only when State is PENDING\_DELETION. The date and time at which the runtime alias will be permanently deleted.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Required: No

 ** ReleaseLifecycle **   <a name="lambdacore-Type-RuntimeAliasInfo-ReleaseLifecycle"></a>
The lifecycle for the alias. By default, this is inherited from the runtime lifecycle. Optionally, you can override the lifecycle information at the alias level, if required.  
Type: [RuntimeReleaseLifecycle](API_RuntimeReleaseLifecycle.md) object  
Required: No

## See Also
<a name="API_RuntimeAliasInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-core-2026-04-30/RuntimeAliasInfo) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-core-2026-04-30/RuntimeAliasInfo) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-core-2026-04-30/RuntimeAliasInfo) 