

# Actions, resources, and condition keys for Amazon Route 53 Recovery Readiness
<a name="list_route53-recovery-readiness"></a>

Amazon Route 53 Recovery Readiness (service prefix: `route53-recovery-readiness`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/r53recovery/latest/dg/what-is-route53-recovery.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/recovery-readiness/latest/api/resources.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/r53recovery/latest/dg/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/route53-recovery-readiness/route53-recovery-readiness.json) for this service.

**Topics**
+ [API operations defined by Amazon Route 53 Recovery Readiness](#list_route53-recovery-readiness-operations)
+ [Actions defined by Amazon Route 53 Recovery Readiness](#list_route53-recovery-readiness-actions-as-permissions)
+ [Resource types defined by Amazon Route 53 Recovery Readiness](#list_route53-recovery-readiness-resources-for-iam-policies)
+ [Condition keys for Amazon Route 53 Recovery Readiness](#list_route53-recovery-readiness-policy-keys)

## API operations defined by Amazon Route 53 Recovery Readiness
<a name="list_route53-recovery-readiness-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_route53-recovery-readiness-actions-as-permissions).




- **   CreateCell  **
  - **IAM action:**  [route53-recovery-readiness:CreateCell](#list_route53-recovery-readiness-action-CreateCell)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [route53-recovery-readiness:TagResource](#list_route53-recovery-readiness-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateCrossAccountAuthorization  **
  - **IAM action:**  [route53-recovery-readiness:CreateCrossAccountAuthorization](#list_route53-recovery-readiness-action-CreateCrossAccountAuthorization) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateReadinessCheck  **
  - **IAM action:**  [route53-recovery-readiness:CreateReadinessCheck](#list_route53-recovery-readiness-action-CreateReadinessCheck)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [route53-recovery-readiness:TagResource](#list_route53-recovery-readiness-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateRecoveryGroup  **
  - **IAM action:**  [route53-recovery-readiness:CreateRecoveryGroup](#list_route53-recovery-readiness-action-CreateRecoveryGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [route53-recovery-readiness:TagResource](#list_route53-recovery-readiness-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateResourceSet  **
  - **IAM action:**  [route53-recovery-readiness:CreateResourceSet](#list_route53-recovery-readiness-action-CreateResourceSet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [route53-recovery-readiness:TagResource](#list_route53-recovery-readiness-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteCell  **
  - **IAM action:**  [route53-recovery-readiness:DeleteCell](#list_route53-recovery-readiness-action-DeleteCell) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCrossAccountAuthorization  **
  - **IAM action:**  [route53-recovery-readiness:DeleteCrossAccountAuthorization](#list_route53-recovery-readiness-action-DeleteCrossAccountAuthorization) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteReadinessCheck  **
  - **IAM action:**  [route53-recovery-readiness:DeleteReadinessCheck](#list_route53-recovery-readiness-action-DeleteReadinessCheck) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRecoveryGroup  **
  - **IAM action:**  [route53-recovery-readiness:DeleteRecoveryGroup](#list_route53-recovery-readiness-action-DeleteRecoveryGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteResourceSet  **
  - **IAM action:**  [route53-recovery-readiness:DeleteResourceSet](#list_route53-recovery-readiness-action-DeleteResourceSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetArchitectureRecommendations  **
  - **IAM action:**  [route53-recovery-readiness:GetArchitectureRecommendations](#list_route53-recovery-readiness-action-GetArchitectureRecommendations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCell  **
  - **IAM action:**  [route53-recovery-readiness:GetCell](#list_route53-recovery-readiness-action-GetCell) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCellReadinessSummary  **
  - **IAM action:**  [route53-recovery-readiness:GetCellReadinessSummary](#list_route53-recovery-readiness-action-GetCellReadinessSummary) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetReadinessCheck  **
  - **IAM action:**  [route53-recovery-readiness:GetReadinessCheck](#list_route53-recovery-readiness-action-GetReadinessCheck) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetReadinessCheckResourceStatus  **
  - **IAM action:**  [route53-recovery-readiness:GetReadinessCheckResourceStatus](#list_route53-recovery-readiness-action-GetReadinessCheckResourceStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetReadinessCheckStatus  **
  - **IAM action:**  [route53-recovery-readiness:GetReadinessCheckStatus](#list_route53-recovery-readiness-action-GetReadinessCheckStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRecoveryGroup  **
  - **IAM action:**  [route53-recovery-readiness:GetRecoveryGroup](#list_route53-recovery-readiness-action-GetRecoveryGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRecoveryGroupReadinessSummary  **
  - **IAM action:**  [route53-recovery-readiness:GetRecoveryGroupReadinessSummary](#list_route53-recovery-readiness-action-GetRecoveryGroupReadinessSummary) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResourceSet  **
  - **IAM action:**  [route53-recovery-readiness:GetResourceSet](#list_route53-recovery-readiness-action-GetResourceSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListCells  **
  - **IAM action:**  [route53-recovery-readiness:ListCells](#list_route53-recovery-readiness-action-ListCells) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListCrossAccountAuthorizations  **
  - **IAM action:**  [route53-recovery-readiness:ListCrossAccountAuthorizations](#list_route53-recovery-readiness-action-ListCrossAccountAuthorizations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListReadinessChecks  **
  - **IAM action:**  [route53-recovery-readiness:ListReadinessChecks](#list_route53-recovery-readiness-action-ListReadinessChecks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListRecoveryGroups  **
  - **IAM action:**  [route53-recovery-readiness:ListRecoveryGroups](#list_route53-recovery-readiness-action-ListRecoveryGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListResourceSets  **
  - **IAM action:**  [route53-recovery-readiness:ListResourceSets](#list_route53-recovery-readiness-action-ListResourceSets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListRules  **
  - **IAM action:**  [route53-recovery-readiness:ListRules](#list_route53-recovery-readiness-action-ListRules) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTagsForResources  **
  - **IAM action:**  [route53-recovery-readiness:ListTagsForResources](#list_route53-recovery-readiness-action-ListTagsForResources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   TagResource  **
  - **IAM action:**  [route53-recovery-readiness:TagResource](#list_route53-recovery-readiness-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [route53-recovery-readiness:UntagResource](#list_route53-recovery-readiness-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateCell  **
  - **IAM action:**  [route53-recovery-readiness:UpdateCell](#list_route53-recovery-readiness-action-UpdateCell) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateReadinessCheck  **
  - **IAM action:**  [route53-recovery-readiness:UpdateReadinessCheck](#list_route53-recovery-readiness-action-UpdateReadinessCheck) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRecoveryGroup  **
  - **IAM action:**  [route53-recovery-readiness:UpdateRecoveryGroup](#list_route53-recovery-readiness-action-UpdateRecoveryGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateResourceSet  **
  - **IAM action:**  [route53-recovery-readiness:UpdateResourceSet](#list_route53-recovery-readiness-action-UpdateResourceSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon Route 53 Recovery Readiness
<a name="list_route53-recovery-readiness-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateCell](https://docs.aws.amazon.com/recovery-readiness/latest/api/cells.html)  **
  - **Description:** Grants permission to create a new cell
  - **Resource types (\*required):** [cell\*](#list_route53-recovery-readiness-resource-cell)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_route53-recovery-readiness-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_route53-recovery-readiness-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_route53-recovery-readiness-aws_TagKeys)
  - **Access level:** Write

- **   [CreateCrossAccountAuthorization](https://docs.aws.amazon.com/recovery-readiness/latest/api/crossaccountauthorizations.html)  **
  - **Description:** Grants permission to create a cross account authorization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateReadinessCheck](https://docs.aws.amazon.com/recovery-readiness/latest/api/readinesschecks.html)  **
  - **Description:** Grants permission to create a readiness check
  - **Resource types (\*required):** [readinesscheck\*](#list_route53-recovery-readiness-resource-readinesscheck)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_route53-recovery-readiness-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_route53-recovery-readiness-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_route53-recovery-readiness-aws_TagKeys)
  - **Access level:** Write

- **   [CreateRecoveryGroup](https://docs.aws.amazon.com/recovery-readiness/latest/api/recoverygroups.html)  **
  - **Description:** Grants permission to create a recovery group
  - **Resource types (\*required):** [recoverygroup\*](#list_route53-recovery-readiness-resource-recoverygroup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_route53-recovery-readiness-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_route53-recovery-readiness-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_route53-recovery-readiness-aws_TagKeys)
  - **Access level:** Write

- **   [CreateResourceSet](https://docs.aws.amazon.com/recovery-readiness/latest/api/resourcesets.html)  **
  - **Description:** Grants permission to create a resource set
  - **Resource types (\*required):** [resourceset\*](#list_route53-recovery-readiness-resource-resourceset)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_route53-recovery-readiness-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_route53-recovery-readiness-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_route53-recovery-readiness-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteCell](https://docs.aws.amazon.com/recovery-readiness/latest/api/cells-cellname.html)  **
  - **Description:** Grants permission to delete a cell
  - **Resource types (\*required):** [cell\*](#list_route53-recovery-readiness-resource-cell)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53-recovery-readiness-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCrossAccountAuthorization](https://docs.aws.amazon.com/recovery-readiness/latest/api/crossaccountauthorizations-crossaccountauthorization.html)  **
  - **Description:** Grants permission to delete a cross account authorization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteReadinessCheck](https://docs.aws.amazon.com/recovery-readiness/latest/api/readinesschecks-readinesscheckname.html)  **
  - **Description:** Grants permission to delete a readiness check
  - **Resource types (\*required):** [readinesscheck\*](#list_route53-recovery-readiness-resource-readinesscheck)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53-recovery-readiness-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRecoveryGroup](https://docs.aws.amazon.com/recovery-readiness/latest/api/recoverygroups-recoverygroupname.html)  **
  - **Description:** Grants permission to delete a recovery group
  - **Resource types (\*required):** [recoverygroup\*](#list_route53-recovery-readiness-resource-recoverygroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53-recovery-readiness-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteResourceSet](https://docs.aws.amazon.com/recovery-readiness/latest/api/resourcesets-resourcesetname.html)  **
  - **Description:** Grants permission to delete a resource set
  - **Resource types (\*required):** [resourceset\*](#list_route53-recovery-readiness-resource-resourceset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53-recovery-readiness-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetArchitectureRecommendations](https://docs.aws.amazon.com/recovery-readiness/latest/api/recoverygroups-recoverygroupname-architecturerecommendations.html)  **
  - **Description:** Grants permission to get architecture recommendations for a recovery group
  - **Resource types (\*required):** [recoverygroup\*](#list_route53-recovery-readiness-resource-recoverygroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53-recovery-readiness-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCell](https://docs.aws.amazon.com/recovery-readiness/latest/api/cells-cellname.html)  **
  - **Description:** Grants permission to get information about a cell
  - **Resource types (\*required):** [cell\*](#list_route53-recovery-readiness-resource-cell)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53-recovery-readiness-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCellReadinessSummary](https://docs.aws.amazon.com/recovery-readiness/latest/api/cellreadiness-cellname.html)  **
  - **Description:** Grants permission to get a readiness summary for a cell
  - **Resource types (\*required):** [cell\*](#list_route53-recovery-readiness-resource-cell)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53-recovery-readiness-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetReadinessCheck](https://docs.aws.amazon.com/recovery-readiness/latest/api/readinesschecks-readinesscheckname.html)  **
  - **Description:** Grants permission to get information about a readiness check
  - **Resource types (\*required):** [readinesscheck\*](#list_route53-recovery-readiness-resource-readinesscheck)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53-recovery-readiness-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetReadinessCheckResourceStatus](https://docs.aws.amazon.com/recovery-readiness/latest/api/readinesschecks-readinesscheckname-resource-resourceidentifier-status.html)  **
  - **Description:** Grants permission to get the readiness status for an individual resource
  - **Resource types (\*required):** [readinesscheck\*](#list_route53-recovery-readiness-resource-readinesscheck)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53-recovery-readiness-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetReadinessCheckStatus](https://docs.aws.amazon.com/recovery-readiness/latest/api/readinesschecks-readinesscheckname-status.html)  **
  - **Description:** Grants permission to get the status of a readiness check (for a resource set)
  - **Resource types (\*required):** [readinesscheck\*](#list_route53-recovery-readiness-resource-readinesscheck)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53-recovery-readiness-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRecoveryGroup](https://docs.aws.amazon.com/recovery-readiness/latest/api/recoverygroups-recoverygroupname.html)  **
  - **Description:** Grants permission to get information about a recovery group
  - **Resource types (\*required):** [recoverygroup\*](#list_route53-recovery-readiness-resource-recoverygroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53-recovery-readiness-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRecoveryGroupReadinessSummary](https://docs.aws.amazon.com/recovery-readiness/latest/api/recoverygroupreadiness-recoverygroupname.html)  **
  - **Description:** Grants permission to get a readiness summary for a recovery group
  - **Resource types (\*required):** [recoverygroup\*](#list_route53-recovery-readiness-resource-recoverygroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53-recovery-readiness-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetResourceSet](https://docs.aws.amazon.com/recovery-readiness/latest/api/resourcesets-resourcesetname.html)  **
  - **Description:** Grants permission to get information about a resource set
  - **Resource types (\*required):** [resourceset\*](#list_route53-recovery-readiness-resource-resourceset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53-recovery-readiness-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListCells](https://docs.aws.amazon.com/recovery-readiness/latest/api/cells.html)  **
  - **Description:** Grants permission to list cells
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListCrossAccountAuthorizations](https://docs.aws.amazon.com/recovery-readiness/latest/api/crossaccountauthorizations.html)  **
  - **Description:** Grants permission to list cross account authorizations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListReadinessChecks](https://docs.aws.amazon.com/recovery-readiness/latest/api/readinesschecks.html)  **
  - **Description:** Grants permission to list readiness checks
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListRecoveryGroups](https://docs.aws.amazon.com/recovery-readiness/latest/api/recoverygroups.html)  **
  - **Description:** Grants permission to list recovery groups
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListResourceSets](https://docs.aws.amazon.com/recovery-readiness/latest/api/resourcesets.html)  **
  - **Description:** Grants permission to list resource sets
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListRules](https://docs.aws.amazon.com/recovery-readiness/latest/api/rules.html)  **
  - **Description:** Grants permission to list readiness rules
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListTagsForResources](https://docs.aws.amazon.com/recovery-readiness/latest/api/tags-resource-arn.html)  **
  - **Description:** Grants permission to list tags for a resource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [TagResource](https://docs.aws.amazon.com/recovery-readiness/latest/api/tags-resource-arn.html)  **
  - **Description:** Grants permission to add a tag to a resource
  - **Resource types (\*required):** [cell](#list_route53-recovery-readiness-resource-cell) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_route53-recovery-readiness-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_route53-recovery-readiness-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_route53-recovery-readiness-aws_TagKeys)
  - **Resource types (\*required):** [readinesscheck](#list_route53-recovery-readiness-resource-readinesscheck) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_route53-recovery-readiness-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_route53-recovery-readiness-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_route53-recovery-readiness-aws_TagKeys)
  - **Resource types (\*required):** [recoverygroup](#list_route53-recovery-readiness-resource-recoverygroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_route53-recovery-readiness-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_route53-recovery-readiness-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_route53-recovery-readiness-aws_TagKeys)
  - **Resource types (\*required):** [resourceset](#list_route53-recovery-readiness-resource-resourceset) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_route53-recovery-readiness-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_route53-recovery-readiness-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_route53-recovery-readiness-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/recovery-readiness/latest/api/tags-resource-arn.html)  **
  - **Description:** Grants permission to remove a tag from a resource
  - **Resource types (\*required):** [cell](#list_route53-recovery-readiness-resource-cell) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_route53-recovery-readiness-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_route53-recovery-readiness-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_route53-recovery-readiness-aws_TagKeys)
  - **Resource types (\*required):** [readinesscheck](#list_route53-recovery-readiness-resource-readinesscheck) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_route53-recovery-readiness-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_route53-recovery-readiness-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_route53-recovery-readiness-aws_TagKeys)
  - **Resource types (\*required):** [recoverygroup](#list_route53-recovery-readiness-resource-recoverygroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_route53-recovery-readiness-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_route53-recovery-readiness-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_route53-recovery-readiness-aws_TagKeys)
  - **Resource types (\*required):** [resourceset](#list_route53-recovery-readiness-resource-resourceset) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_route53-recovery-readiness-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_route53-recovery-readiness-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_route53-recovery-readiness-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateCell](https://docs.aws.amazon.com/recovery-readiness/latest/api/cells-cellname.html)  **
  - **Description:** Grants permission to update a cell
  - **Resource types (\*required):** [cell\*](#list_route53-recovery-readiness-resource-cell)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53-recovery-readiness-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_route53-recovery-readiness-aws_TagKeys)
  - **Access level:** Write

- **   [UpdateReadinessCheck](https://docs.aws.amazon.com/recovery-readiness/latest/api/readinesschecks-readinesscheckname.html)  **
  - **Description:** Grants permission to update a readiness check
  - **Resource types (\*required):** [readinesscheck\*](#list_route53-recovery-readiness-resource-readinesscheck)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53-recovery-readiness-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_route53-recovery-readiness-aws_TagKeys)
  - **Access level:** Write

- **   [UpdateRecoveryGroup](https://docs.aws.amazon.com/recovery-readiness/latest/api/recoverygroups-recoverygroupname.html)  **
  - **Description:** Grants permission to update a recovery group
  - **Resource types (\*required):** [recoverygroup\*](#list_route53-recovery-readiness-resource-recoverygroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53-recovery-readiness-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_route53-recovery-readiness-aws_TagKeys)
  - **Access level:** Write

- **   [UpdateResourceSet](https://docs.aws.amazon.com/recovery-readiness/latest/api/resourcesets-resourcesetname.html)  **
  - **Description:** Grants permission to update a resource set
  - **Resource types (\*required):** [resourceset\*](#list_route53-recovery-readiness-resource-resourceset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53-recovery-readiness-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_route53-recovery-readiness-aws_TagKeys)
  - **Access level:** Write



## Resource types defined by Amazon Route 53 Recovery Readiness
<a name="list_route53-recovery-readiness-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [cell](https://docs.aws.amazon.com/r53recovery/latest/dg/recovery-readiness.recovery-groups.html)  | arn:${Partition}:route53-recovery-readiness::${Account}:cell/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_route53-recovery-readiness-aws_ResourceTag___TagKey_) | 
|  [readinesscheck](https://docs.aws.amazon.com/r53recovery/latest/dg/recovery-readiness.readiness-checks.html)  | arn:${Partition}:route53-recovery-readiness::${Account}:readiness-check/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_route53-recovery-readiness-aws_ResourceTag___TagKey_) | 
|  [recoverygroup](https://docs.aws.amazon.com/r53recovery/latest/dg/recovery-readiness.recovery-groups.html)  | arn:${Partition}:route53-recovery-readiness::${Account}:recovery-group/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_route53-recovery-readiness-aws_ResourceTag___TagKey_) | 
|  [resourceset](https://docs.aws.amazon.com/r53recovery/latest/dg/recovery-readiness.readiness-checks.html)  | arn:${Partition}:route53-recovery-readiness::${Account}:resource-set/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_route53-recovery-readiness-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon Route 53 Recovery Readiness
<a name="list_route53-recovery-readiness-policy-keys"></a>

Amazon Route 53 Recovery Readiness defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 