

# RuntimeVersionInfo

Summary information about a runtime version returned by ListRuntimeVersions.

## Contents
<a name="API_RuntimeVersionInfo_Contents"></a>

 ** Arn **   <a name="lambdacore-Type-RuntimeVersionInfo-Arn"></a>
The Amazon Resource Name (ARN) of the runtime version.  
Type: String  
Length Constraints: Minimum length of 48. Maximum length of 2048.  
Pattern: `arn:(aws[a-zA-Z-]*):lambda:(eusc-)?[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:runtime/[a-z0-9]([a-z0-9_.-]{0,126})?[a-z0-9](/(version|alias)/[^/]{1,128})?`   
Required: Yes

 ** Created **   <a name="lambdacore-Type-RuntimeVersionInfo-Created"></a>
The date and time when the runtime version was created.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Required: Yes

 ** LastModified **   <a name="lambdacore-Type-RuntimeVersionInfo-LastModified"></a>
The date and time when the runtime version was last modified.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Required: Yes

 ** Name **   <a name="lambdacore-Type-RuntimeVersionInfo-Name"></a>
The name of the runtime version.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[A-Za-z0-9_]([A-Za-z0-9_.-]{0,126}[A-Za-z0-9_])?`   
Required: Yes

 ** ResolvedUri **   <a name="lambdacore-Type-RuntimeVersionInfo-ResolvedUri"></a>
The resolved image URI of the runtime version.  
Type: String  
Required: Yes

 ** State **   <a name="lambdacore-Type-RuntimeVersionInfo-State"></a>
The current state of the runtime version.  
Type: String  
Valid Values: `CREATING | ACTIVE | FAILED | DELETING | PENDING_DELETION`   
Required: Yes

 ** Compatibility **   <a name="lambdacore-Type-RuntimeVersionInfo-Compatibility"></a>
The compatibility matrix of the runtime version.  
Type: [Compatibility](API_Compatibility.md) object  
Required: No

 ** PendingDeletionAt **   <a name="lambdacore-Type-RuntimeVersionInfo-PendingDeletionAt"></a>
Present only when State is PENDING\_DELETION. The date and time at which the runtime version will be permanently deleted.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Required: No

 ** ReleaseNotes **   <a name="lambdacore-Type-RuntimeVersionInfo-ReleaseNotes"></a>
The release notes associated with the runtime version.  
Type: String  
Required: No

## See Also
<a name="API_RuntimeVersionInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-core-2026-04-30/RuntimeVersionInfo) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-core-2026-04-30/RuntimeVersionInfo) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-core-2026-04-30/RuntimeVersionInfo) 