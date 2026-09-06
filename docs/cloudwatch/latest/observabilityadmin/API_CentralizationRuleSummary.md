

# CentralizationRuleSummary
<a name="API_CentralizationRuleSummary"></a>

A summary of a centralization rule's key properties and status.

## Contents
<a name="API_CentralizationRuleSummary_Contents"></a>

 ** CreatedRegion **   <a name="cwoa-Type-CentralizationRuleSummary-CreatedRegion"></a>
The AWS region where the organization centralization rule was created.  
Type: String  
Length Constraints: Minimum length of 1.  
Required: No

 ** CreatedTimeStamp **   <a name="cwoa-Type-CentralizationRuleSummary-CreatedTimeStamp"></a>
The timestamp when the organization centralization rule was created.  
Type: Long  
Required: No

 ** CreatorAccountId **   <a name="cwoa-Type-CentralizationRuleSummary-CreatorAccountId"></a>
The AWS Account that created the organization centralization rule.  
Type: String  
Required: No

 ** DestinationAccountId **   <a name="cwoa-Type-CentralizationRuleSummary-DestinationAccountId"></a>
The primary destination account of the organization centralization rule.  
Type: String  
Required: No

 ** DestinationRegion **   <a name="cwoa-Type-CentralizationRuleSummary-DestinationRegion"></a>
The primary destination region of the organization centralization rule.  
Type: String  
Length Constraints: Minimum length of 1.  
Required: No

 ** FailureReason **   <a name="cwoa-Type-CentralizationRuleSummary-FailureReason"></a>
The reason why an organization centralization rule is marked UNHEALTHY.  
Type: String  
Valid Values: `TRUSTED_ACCESS_NOT_ENABLED | DESTINATION_ACCOUNT_NOT_IN_ORGANIZATION | INTERNAL_SERVER_ERROR`   
Required: No

 ** LastUpdateTimeStamp **   <a name="cwoa-Type-CentralizationRuleSummary-LastUpdateTimeStamp"></a>
The timestamp when the organization centralization rule was last updated.  
Type: Long  
Required: No

 ** RuleArn **   <a name="cwoa-Type-CentralizationRuleSummary-RuleArn"></a>
The Amazon Resource Name (ARN) of the organization centralization rule.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1011.  
Pattern: `arn:aws([a-z0-9\-]+)?:([a-zA-Z0-9\-]+):([a-z0-9\-]+)?:([0-9]{12})?:(.+)`   
Required: No

 ** RuleHealth **   <a name="cwoa-Type-CentralizationRuleSummary-RuleHealth"></a>
The health status of the organization centralization rule.  
Type: String  
Valid Values: `Healthy | Unhealthy | Provisioning`   
Required: No

 ** RuleName **   <a name="cwoa-Type-CentralizationRuleSummary-RuleName"></a>
The name of the organization centralization rule.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[0-9A-Za-z-_.#/]+`   
Required: No

 ** TagPropagationFailureReason **   <a name="cwoa-Type-CentralizationRuleSummary-TagPropagationFailureReason"></a>
The reason tag propagation is unhealthy for this rule. Only present when `TagPropagationStatus` is `Unhealthy`.  
Type: String  
Valid Values: `RoleNotAssumable | RoleLacksPermissions`   
Required: No

 ** TagPropagationStatus **   <a name="cwoa-Type-CentralizationRuleSummary-TagPropagationStatus"></a>
The health status of tag propagation for this rule. This status is independent of the overall `RuleHealth` for log delivery. Returns `Healthy` when the most recent tag-propagation attempt succeeded, or `Unhealthy` when the most recent attempt failed.  
Type: String  
Valid Values: `Healthy | Unhealthy`   
Required: No

## See Also
<a name="API_CentralizationRuleSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/CentralizationRuleSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/CentralizationRuleSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/CentralizationRuleSummary) 