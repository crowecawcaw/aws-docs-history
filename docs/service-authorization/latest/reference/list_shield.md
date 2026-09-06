

# Actions, resources, and condition keys for AWS Shield
<a name="list_shield"></a>

AWS Shield (service prefix: `shield`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/waf/latest/developerguide/shield-chapter.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/waf/latest/developerguide/waf-auth-and-access-control.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/shield/shield.json) for this service.

**Topics**
+ [API operations defined by AWS Shield](#list_shield-operations)
+ [Actions defined by AWS Shield](#list_shield-actions-as-permissions)
+ [Permission-only actions for AWS Shield](#list_shield-permission-only-actions)
+ [Resource types defined by AWS Shield](#list_shield-resources-for-iam-policies)
+ [Condition keys for AWS Shield](#list_shield-policy-keys)

## API operations defined by AWS Shield
<a name="list_shield-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_shield-actions-as-permissions).




- **   AssociateDRTLogBucket  **
  - **IAM action:**  [shield:AssociateDRTLogBucket](#list_shield-action-AssociateDRTLogBucket) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociateDRTRole  **
  - **IAM action:**  [shield:AssociateDRTRole](#list_shield-action-AssociateDRTRole)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** drt.shield.amazonaws.com / **Access level:** Write

- **   AssociateHealthCheck  **
  - **IAM action:**  [shield:AssociateHealthCheck](#list_shield-action-AssociateHealthCheck) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociateProactiveEngagementDetails  **
  - **IAM action:**  [shield:AssociateProactiveEngagementDetails](#list_shield-action-AssociateProactiveEngagementDetails) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateProtection  **
  - **IAM action:**  [shield:CreateProtection](#list_shield-action-CreateProtection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [shield:TagResource](#list_shield-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateProtectionGroup  **
  - **IAM action:**  [shield:CreateProtectionGroup](#list_shield-action-CreateProtectionGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [shield:TagResource](#list_shield-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateSubscription  **
  - **IAM action:**  [shield:CreateSubscription](#list_shield-action-CreateSubscription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteProtection  **
  - **IAM action:**  [shield:DeleteProtection](#list_shield-action-DeleteProtection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteProtectionGroup  **
  - **IAM action:**  [shield:DeleteProtectionGroup](#list_shield-action-DeleteProtectionGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSubscription  **
  - **IAM action:**  [shield:DeleteSubscription](#list_shield-action-DeleteSubscription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeAttack  **
  - **IAM action:**  [shield:DescribeAttack](#list_shield-action-DescribeAttack)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [shield:DescribeProtectionGroup](#list_shield-action-DescribeProtectionGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   DescribeAttackStatistics  **
  - **IAM action:**  [shield:DescribeAttackStatistics](#list_shield-action-DescribeAttackStatistics) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDRTAccess  **
  - **IAM action:**  [shield:DescribeDRTAccess](#list_shield-action-DescribeDRTAccess) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeEmergencyContactSettings  **
  - **IAM action:**  [shield:DescribeEmergencyContactSettings](#list_shield-action-DescribeEmergencyContactSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeProtection  **
  - **IAM action:**  [shield:DescribeProtection](#list_shield-action-DescribeProtection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeProtectionGroup  **
  - **IAM action:**  [shield:DescribeProtectionGroup](#list_shield-action-DescribeProtectionGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeSubscription  **
  - **IAM action:**  [shield:DescribeSubscription](#list_shield-action-DescribeSubscription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DisableApplicationLayerAutomaticResponse  **
  - **IAM action:**  [shield:DisableApplicationLayerAutomaticResponse](#list_shield-action-DisableApplicationLayerAutomaticResponse) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisableProactiveEngagement  **
  - **IAM action:**  [shield:DisableProactiveEngagement](#list_shield-action-DisableProactiveEngagement) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateDRTLogBucket  **
  - **IAM action:**  [shield:DisassociateDRTLogBucket](#list_shield-action-DisassociateDRTLogBucket) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateDRTRole  **
  - **IAM action:**  [shield:DisassociateDRTRole](#list_shield-action-DisassociateDRTRole) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateHealthCheck  **
  - **IAM action:**  [shield:DisassociateHealthCheck](#list_shield-action-DisassociateHealthCheck) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   EnableApplicationLayerAutomaticResponse  **
  - **IAM action:**  [shield:EnableApplicationLayerAutomaticResponse](#list_shield-action-EnableApplicationLayerAutomaticResponse) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   EnableProactiveEngagement  **
  - **IAM action:**  [shield:EnableProactiveEngagement](#list_shield-action-EnableProactiveEngagement) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetSubscriptionState  **
  - **IAM action:**  [shield:GetSubscriptionState](#list_shield-action-GetSubscriptionState) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAttacks  **
  - **IAM action:**  [shield:ListAttacks](#list_shield-action-ListAttacks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListProtectionGroups  **
  - **IAM action:**  [shield:ListProtectionGroups](#list_shield-action-ListProtectionGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListProtections  **
  - **IAM action:**  [shield:ListProtections](#list_shield-action-ListProtections) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListResourcesInProtectionGroup  **
  - **IAM action:**  [shield:ListResourcesInProtectionGroup](#list_shield-action-ListResourcesInProtectionGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [shield:ListTagsForResource](#list_shield-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   TagResource  **
  - **IAM action:**  [shield:TagResource](#list_shield-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [shield:UntagResource](#list_shield-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateApplicationLayerAutomaticResponse  **
  - **IAM action:**  [shield:UpdateApplicationLayerAutomaticResponse](#list_shield-action-UpdateApplicationLayerAutomaticResponse) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateEmergencyContactSettings  **
  - **IAM action:**  [shield:UpdateEmergencyContactSettings](#list_shield-action-UpdateEmergencyContactSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateProtectionGroup  **
  - **IAM action:**  [shield:UpdateProtectionGroup](#list_shield-action-UpdateProtectionGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSubscription  **
  - **IAM action:**  [shield:UpdateSubscription](#list_shield-action-UpdateSubscription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Shield
<a name="list_shield-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AssociateDRTLogBucket](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_AssociateDRTLogBucket.html)  **
  - **Description:** Grants permission to authorize the DDoS Response team to access the specified Amazon S3 bucket containing your flow logs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [AssociateDRTRole](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_AssociateDRTRole.html)  **
  - **Description:** Grants permission to authorize the DDoS Response team using the specified role, to access your AWS account to assist with DDoS attack mitigation during potential attacks
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [AssociateHealthCheck](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_AssociateHealthCheck.html)  **
  - **Description:** Grants permission to add health-based detection to the Shield Advanced protection for a resource
  - **Resource types (\*required):** [protection\*](#list_shield-resource-protection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_shield-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AssociateProactiveEngagementDetails](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_AssociateProactiveEngagementDetails.html)  **
  - **Description:** Grants permission to initialize proactive engagement and set the list of contacts for the DDoS Response Team (DRT) to use
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateProtection](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_CreateProtection.html)  **
  - **Description:** Grants permission to activate DDoS protection service for a given resource ARN
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_shield-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_shield-aws_TagKeys)
  - **Access level:** Write

- **   [CreateProtectionGroup](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_CreateProtectionGroup.html)  **
  - **Description:** Grants permission to create a grouping of protected resources so they can be handled as a collective
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_shield-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_shield-aws_TagKeys)
  - **Access level:** Write

- **   [CreateSubscription](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_CreateSubscription.html)  **
  - **Description:** Grants permission to activate subscription
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteProtection](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_DeleteProtection.html)  **
  - **Description:** Grants permission to delete an existing protection
  - **Resource types (\*required):** [protection\*](#list_shield-resource-protection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_shield-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteProtectionGroup](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_DeleteProtectionGroup.html)  **
  - **Description:** Grants permission to remove the specified protection group
  - **Resource types (\*required):** [protection-group\*](#list_shield-resource-protection-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_shield-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSubscription](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_DeleteSubscription.html)  **
  - **Description:** Grants permission to deactivate subscription
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DescribeAttack](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_DescribeAttack.html)  **
  - **Description:** Grants permission to get attack details. For getting attack details protected by AWS WAF anti-DDoS managed rule group, this action additionally calls wafv2:DescribeTopContributorsByEvent to retrieve application layer attack contributors, which requires to have wafv2:DescribeTopContributorsByEvent permission in IAM policy
  - **Resource types (\*required):** [attack\*](#list_shield-resource-attack)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeAttackStatistics](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_DescribeAttackStatistics.html)  **
  - **Description:** Grants permission to describe information about the number and type of attacks AWS Shield has detected in the last year
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeDRTAccess](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_DescribeDRTAccess.html)  **
  - **Description:** Grants permission to describe the current role and list of Amazon S3 log buckets used by the DDoS Response team to access your AWS account while assisting with attack mitigation
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeEmergencyContactSettings](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_DescribeEmergencyContactSettings.html)  **
  - **Description:** Grants permission to list the email addresses that the DRT can use to contact you during a suspected attack
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeProtection](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_DescribeProtection.html)  **
  - **Description:** Grants permission to get protection details
  - **Resource types (\*required):** [protection\*](#list_shield-resource-protection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_shield-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeProtectionGroup](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_DescribeProtectionGroup.html)  **
  - **Description:** Grants permission to describe the specification for the specified protection group
  - **Resource types (\*required):** [protection-group\*](#list_shield-resource-protection-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_shield-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeSubscription](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_DescribeSubscription.html)  **
  - **Description:** Grants permission to get subscription details, such as start time
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DisableApplicationLayerAutomaticResponse](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_DisableApplicationLayerAutomaticResponse.html)  **
  - **Description:** Grants permission to disable application layer automatic response for Shield Advanced protection for a resource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DisableProactiveEngagement](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_DisableProactiveEngagement.html)  **
  - **Description:** Grants permission to remove authorization from the DDoS Response Team (DRT) to notify contacts about escalations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DisassociateDRTLogBucket](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_DisassociateDRTLogBucket.html)  **
  - **Description:** Grants permission to remove the DDoS Response team's access to the specified Amazon S3 bucket containing your flow logs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DisassociateDRTRole](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_DisassociateDRTRole.html)  **
  - **Description:** Grants permission to remove the DDoS Response team's access to your AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DisassociateHealthCheck](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_DisassociateHealthCheck.html)  **
  - **Description:** Grants permission to remove health-based detection from the Shield Advanced protection for a resource
  - **Resource types (\*required):** [protection\*](#list_shield-resource-protection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_shield-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [EnableApplicationLayerAutomaticResponse](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_EnableApplicationLayerAutomaticResponse.html)  **
  - **Description:** Grants permission to enable application layer automatic response for Shield Advanced protection for a resource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [EnableProactiveEngagement](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_EnableProactiveEngagement.html)  **
  - **Description:** Grants permission to authorize the DDoS Response Team (DRT) to use email and phone to notify contacts about escalations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [GetSubscriptionState](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_GetSubscriptionState.html)  **
  - **Description:** Grants permission to get subscription state
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListAttacks](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_ListAttacks.html)  **
  - **Description:** Grants permission to list all existing attacks
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListProtectionGroups](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_ListProtectionGroups.html)  **
  - **Description:** Grants permission to retrieve the protection groups for the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListProtections](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_ListProtections.html)  **
  - **Description:** Grants permission to list all existing protections
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListResourcesInProtectionGroup](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_ListResourcesInProtectionGroup.html)  **
  - **Description:** Grants permission to retrieve the resources that are included in the protection group
  - **Resource types (\*required):** [protection-group\*](#list_shield-resource-protection-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_shield-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to get information about AWS tags for a specified Amazon Resource Name (ARN) in AWS Shield
  - **Resource types (\*required):** [protection](#list_shield-resource-protection) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_shield-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [protection-group](#list_shield-resource-protection-group) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_shield-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [TagResource](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add or updates tags for a resource in AWS Shield
  - **Resource types (\*required):** [protection](#list_shield-resource-protection) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_shield-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_shield-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_shield-aws_TagKeys)
  - **Resource types (\*required):** [protection-group](#list_shield-resource-protection-group) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_shield-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_shield-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_shield-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from a resource in AWS Shield
  - **Resource types (\*required):** [protection](#list_shield-resource-protection) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_shield-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_shield-aws_TagKeys)
  - **Resource types (\*required):** [protection-group](#list_shield-resource-protection-group) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_shield-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_shield-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateApplicationLayerAutomaticResponse](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_UpdateApplicationLayerAutomaticResponse.html)  **
  - **Description:** Grants permission to update application layer automatic response for Shield Advanced protection for a resource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateEmergencyContactSettings](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_UpdateEmergencyContactSettings.html)  **
  - **Description:** Grants permission to update the details of the list of email addresses that the DRT can use to contact you during a suspected attack
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateProtectionGroup](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_UpdateProtectionGroup.html)  **
  - **Description:** Grants permission to update an existing protection group
  - **Resource types (\*required):** [protection-group\*](#list_shield-resource-protection-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_shield-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSubscription](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_UpdateSubscription.html)  **
  - **Description:** Grants permission to update the details of an existing subscription
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write



## Permission-only actions for AWS Shield
<a name="list_shield-permission-only-actions"></a>

The following actions are defined by AWS Shield but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [DescribeAttackContributors](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsshield.html)  **
  - **Description:** Grants permission to get detailed information about the contributors to a specific DDoS attack
  - **Resource types (\*required):** [attack\*](#list_shield-resource-attack) / **Condition keys:**  
  - **Resource types (\*required):** [protection-group](#list_shield-resource-protection-group) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_shield-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetGlobalThreatData](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsshield.html)  **
  - **Description:** Grants permission to retrieve global threat intelligence data and trends from AWS Shield's threat monitoring systems
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListMitigations](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsshield.html)  **
  - **Description:** Grants permission to retrieve a list of mitigation actions that have been applied during DDoS attacks
  - **Resource types (\*required):** [attack\*](#list_shield-resource-attack)
  - **Condition keys:**  
  - **Access level:** List



## Resource types defined by AWS Shield
<a name="list_shield-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [attack](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_AttackDetail.html)  | arn:${Partition}:shield::${Account}:attack/${Id} |   | 
|  [protection](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_Protection.html)  | arn:${Partition}:shield::${Account}:protection/${Id} | [aws:ResourceTag/${TagKey}](#list_shield-aws_ResourceTag___TagKey_) | 
|  [protection-group](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_ProtectionGroup.html)  | arn:${Partition}:shield::${Account}:protection-group/${Id} | [aws:ResourceTag/${TagKey}](#list_shield-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Shield
<a name="list_shield-policy-keys"></a>

AWS Shield defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters actions based on the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters actions based on tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters actions based on the presence of tag keys in the request | ArrayOfString | 