

# RuntimeReleaseLifecycle

The runtime lifecycle for the runtime or alias. Optional. Used to schedule runtime deprecation. Omitting or providing an empty object removes the existing lifecycle.

## Contents
<a name="API_RuntimeReleaseLifecycle_Contents"></a>

 ** DeprecationDate **   <a name="lambdacore-Type-RuntimeReleaseLifecycle-DeprecationDate"></a>
The date (UTC) on which the runtime or alias becomes deprecated.  
Type: String  
Length Constraints: Fixed length of 10.  
Pattern: `\d{4}-\d{2}-\d{2}`   
Required: No

 ** FunctionCreateBlockDate **   <a name="lambdacore-Type-RuntimeReleaseLifecycle-FunctionCreateBlockDate"></a>
The date (UTC) on which creating new functions that use this runtime or alias is blocked.  
Type: String  
Length Constraints: Fixed length of 10.  
Pattern: `\d{4}-\d{2}-\d{2}`   
Required: No

 ** FunctionUpdateBlockDate **   <a name="lambdacore-Type-RuntimeReleaseLifecycle-FunctionUpdateBlockDate"></a>
The date (UTC) on which updating existing functions that use this runtime or alias is blocked.  
Type: String  
Length Constraints: Fixed length of 10.  
Pattern: `\d{4}-\d{2}-\d{2}`   
Required: No

 ** ReleaseState **   <a name="lambdacore-Type-RuntimeReleaseLifecycle-ReleaseState"></a>
Optional, with no default applied. DEPRECATED requires a DeprecationDate on or before today (UTC); PREVIEW and GA require a later one, or none. Reads report DEPRECATED once DeprecationDate is reached.  
Type: String  
Valid Values: `PREVIEW | GA | DEPRECATED`   
Required: No

## See Also
<a name="API_RuntimeReleaseLifecycle_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-core-2026-04-30/RuntimeReleaseLifecycle) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-core-2026-04-30/RuntimeReleaseLifecycle) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-core-2026-04-30/RuntimeReleaseLifecycle) 