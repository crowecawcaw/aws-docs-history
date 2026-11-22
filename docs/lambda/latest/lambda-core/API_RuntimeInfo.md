

# RuntimeInfo

Summary information about a runtime returned by ListRuntimes.

## Contents
<a name="API_RuntimeInfo_Contents"></a>

 ** Arn **   <a name="lambdacore-Type-RuntimeInfo-Arn"></a>
The Amazon Resource Name (ARN) of the runtime.  
Type: String  
Length Constraints: Minimum length of 48. Maximum length of 2048.  
Pattern: `arn:(aws[a-zA-Z-]*):lambda:(eusc-)?[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:runtime/[a-z0-9]([a-z0-9_.-]{0,126})?[a-z0-9](/(version|alias)/[^/]{1,128})?`   
Required: Yes

 ** Created **   <a name="lambdacore-Type-RuntimeInfo-Created"></a>
The date and time when the runtime was created.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Required: Yes

 ** LastModified **   <a name="lambdacore-Type-RuntimeInfo-LastModified"></a>
The date and time when the runtime was last modified.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Required: Yes

 ** Name **   <a name="lambdacore-Type-RuntimeInfo-Name"></a>
The name of the runtime.  
Type: String  
Length Constraints: Minimum length of 2. Maximum length of 128.  
Pattern: `[a-z0-9]([a-z0-9_.-]{0,126})?[a-z0-9]`   
Required: Yes

 ** Description **   <a name="lambdacore-Type-RuntimeInfo-Description"></a>
The description of the runtime.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1024.  
Required: No

 ** LicenseInfo **   <a name="lambdacore-Type-RuntimeInfo-LicenseInfo"></a>
The license information for the runtime.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1024.  
Required: No

 ** PendingDeletionAt **   <a name="lambdacore-Type-RuntimeInfo-PendingDeletionAt"></a>
Present only when State is PENDING\_DELETION. The date and time at which the runtime will be permanently deleted.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Required: No

 ** ReleaseLifecycle **   <a name="lambdacore-Type-RuntimeInfo-ReleaseLifecycle"></a>
The runtime lifecycle for the runtime. Used to schedule runtime deprecation.  
Type: [RuntimeReleaseLifecycle](API_RuntimeReleaseLifecycle.md) object  
Required: No

 ** State **   <a name="lambdacore-Type-RuntimeInfo-State"></a>
The current state of the runtime.  
Type: String  
Valid Values: `ACTIVE | PENDING_DELETION | DELETING | FAILED`   
Required: No

## See Also
<a name="API_RuntimeInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-core-2026-04-30/RuntimeInfo) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-core-2026-04-30/RuntimeInfo) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-core-2026-04-30/RuntimeInfo) 