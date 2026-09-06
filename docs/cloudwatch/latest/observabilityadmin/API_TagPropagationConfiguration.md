

# TagPropagationConfiguration
<a name="API_TagPropagationConfiguration"></a>

Specifies configuration for propagating resource tags from source log groups to centralized destination log groups. The service uses a customer-managed IAM role in the destination account to add, update, and remove tags on destination log groups.

## Contents
<a name="API_TagPropagationConfiguration_Contents"></a>

 ** DestinationRoleArn **   <a name="cwoa-Type-TagPropagationConfiguration-DestinationRoleArn"></a>
The ARN of a customer-managed IAM role in the destination account. The service assumes this role to propagate tags to destination log groups. You must have `iam:PassRole` permission on this role.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:aws[a-zA-Z-]*:iam::\d{12}:role/[\w+=,.@/-]+`   
Required: Yes

 ** TagConflictResolutionStrategy **   <a name="cwoa-Type-TagPropagationConfiguration-TagConflictResolutionStrategy"></a>
The strategy for resolving conflicts when a tag key exists on both the source and destination log groups. If not specified, defaults to `UPDATE_SYNC`.  
+  `ADD_ONLY` – Only adds new tags from the source without modifying existing destination tags.
+  `UPDATE_SYNC` – Adds new tags and updates existing tags from the source. Does not remove destination tags that are absent from the source.
+  `IN_SYNC` – Keeps destination tags fully synchronized with source tags, including removing destination tags that do not exist on the source.
Type: String  
Valid Values: `IN_SYNC | ADD_ONLY | UPDATE_SYNC`   
Required: No

## See Also
<a name="API_TagPropagationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/TagPropagationConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/TagPropagationConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/TagPropagationConfiguration) 