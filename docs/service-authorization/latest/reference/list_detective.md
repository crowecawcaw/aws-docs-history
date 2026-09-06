

# Actions, resources, and condition keys for Amazon Detective
<a name="list_detective"></a>

Amazon Detective (service prefix: `detective`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/detective/latest/adminguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/detective/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/detective/latest/adminguide/security_iam_service-with-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/detective/detective.json) for this service.

**Topics**
+ [API operations defined by Amazon Detective](#list_detective-operations)
+ [Actions defined by Amazon Detective](#list_detective-actions-as-permissions)
+ [Permission-only actions for Amazon Detective](#list_detective-permission-only-actions)
+ [Resource types defined by Amazon Detective](#list_detective-resources-for-iam-policies)
+ [Condition keys for Amazon Detective](#list_detective-policy-keys)

## API operations defined by Amazon Detective
<a name="list_detective-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_detective-actions-as-permissions).




- **   AcceptInvitation  **
  - **IAM action:**  [detective:AcceptInvitation](#list_detective-action-AcceptInvitation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchGetGraphMemberDatasources  **
  - **IAM action:**  [detective:BatchGetGraphMemberDatasources](#list_detective-action-BatchGetGraphMemberDatasources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchGetMembershipDatasources  **
  - **IAM action:**  [detective:BatchGetMembershipDatasources](#list_detective-action-BatchGetMembershipDatasources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   CreateGraph  **
  - **IAM action:**  [detective:CreateGraph](#list_detective-action-CreateGraph)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [detective:TagResource](#list_detective-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateMembers  **
  - **IAM action:**  [detective:CreateMembers](#list_detective-action-CreateMembers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteGraph  **
  - **IAM action:**  [detective:DeleteGraph](#list_detective-action-DeleteGraph) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteMembers  **
  - **IAM action:**  [detective:DeleteMembers](#list_detective-action-DeleteMembers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeOrganizationConfiguration  **
  - **IAM action:**  [detective:DescribeOrganizationConfiguration](#list_detective-action-DescribeOrganizationConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DisableOrganizationAdminAccount  **
  - **IAM action:**  [detective:DisableOrganizationAdminAccount](#list_detective-action-DisableOrganizationAdminAccount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateMembership  **
  - **IAM action:**  [detective:DisassociateMembership](#list_detective-action-DisassociateMembership) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   EnableOrganizationAdminAccount  **
  - **IAM action:**  [detective:EnableOrganizationAdminAccount](#list_detective-action-EnableOrganizationAdminAccount)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:CreateServiceLinkedRole](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateServiceLinkedRole.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [organizations:EnableAWSServiceAccess](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnableAWSServiceAccess.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [organizations:RegisterDelegatedAdministrator](https://docs.aws.amazon.com/organizations/latest/APIReference/API_RegisterDelegatedAdministrator.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   GetInvestigation  **
  - **IAM action:**  [detective:GetInvestigation](#list_detective-action-GetInvestigation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMembers  **
  - **IAM action:**  [detective:GetMembers](#list_detective-action-GetMembers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListDatasourcePackages  **
  - **IAM action:**  [detective:ListDatasourcePackages](#list_detective-action-ListDatasourcePackages) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListGraphs  **
  - **IAM action:**  [detective:ListGraphs](#list_detective-action-ListGraphs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListIndicators  **
  - **IAM action:**  [detective:ListIndicators](#list_detective-action-ListIndicators) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListInvestigations  **
  - **IAM action:**  [detective:ListInvestigations](#list_detective-action-ListInvestigations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListInvitations  **
  - **IAM action:**  [detective:ListInvitations](#list_detective-action-ListInvitations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMembers  **
  - **IAM action:**  [detective:ListMembers](#list_detective-action-ListMembers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListOrganizationAdminAccounts  **
  - **IAM action:**  [detective:ListOrganizationAdminAccount](#list_detective-action-ListOrganizationAdminAccount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [detective:ListTagsForResource](#list_detective-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   RejectInvitation  **
  - **IAM action:**  [detective:RejectInvitation](#list_detective-action-RejectInvitation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartInvestigation  **
  - **IAM action:**  [detective:StartInvestigation](#list_detective-action-StartInvestigation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartMonitoringMember  **
  - **IAM action:**  [detective:StartMonitoringMember](#list_detective-action-StartMonitoringMember) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [detective:TagResource](#list_detective-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [detective:UntagResource](#list_detective-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateDatasourcePackages  **
  - **IAM action:**  [detective:UpdateDatasourcePackages](#list_detective-action-UpdateDatasourcePackages) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateInvestigationState  **
  - **IAM action:**  [detective:UpdateInvestigationState](#list_detective-action-UpdateInvestigationState) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateOrganizationConfiguration  **
  - **IAM action:**  [detective:UpdateOrganizationConfiguration](#list_detective-action-UpdateOrganizationConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon Detective
<a name="list_detective-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AcceptInvitation](https://docs.aws.amazon.com/detective/latest/APIReference/API_AcceptInvitation.html)  **
  - **Description:** Grants permission to accept an invitation to become a member of a behavior graph
  - **Resource types (\*required):** [Graph\*](#list_detective-resource-Graph)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_detective-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchGetGraphMemberDatasources](https://docs.aws.amazon.com/detective/latest/APIReference/API_BatchGetGraphMemberDatasources.html)  **
  - **Description:** Grants permission to retrieve the datasource package history for the specified member accounts in a behavior graph managed by this account
  - **Resource types (\*required):** [Graph\*](#list_detective-resource-Graph)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_detective-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchGetMembershipDatasources](https://docs.aws.amazon.com/detective/latest/APIReference/API_BatchGetMembershipDatasources.html)  **
  - **Description:** Grants permission to retrieve the datasource package history of the caller account for the specified graphs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [CreateGraph](https://docs.aws.amazon.com/detective/latest/APIReference/API_CreateGraph.html)  **
  - **Description:** Grants permission to create a behavior graph and begin to aggregate security information
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_detective-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_detective-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_detective-aws_TagKeys)
  - **Access level:** Write

- **   [CreateMembers](https://docs.aws.amazon.com/detective/latest/APIReference/API_CreateMembers.html)  **
  - **Description:** Grants permission to request the membership of one or more accounts in a behavior graph managed by this account
  - **Resource types (\*required):** [Graph\*](#list_detective-resource-Graph)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_detective-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteGraph](https://docs.aws.amazon.com/detective/latest/APIReference/API_DeleteGraph.html)  **
  - **Description:** Grants permission to delete a behavior graph and stop aggregating security information
  - **Resource types (\*required):** [Graph\*](#list_detective-resource-Graph)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_detective-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteMembers](https://docs.aws.amazon.com/detective/latest/APIReference/API_DeleteMembers.html)  **
  - **Description:** Grants permission to remove member accounts from a behavior graph managed by this account
  - **Resource types (\*required):** [Graph\*](#list_detective-resource-Graph)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_detective-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeOrganizationConfiguration](https://docs.aws.amazon.com/detective/latest/APIReference/API_DescribeOrganizationConfiguration.html)  **
  - **Description:** Grants permission to view the current configuration related to the Amazon Detective integration with AWS Organizations
  - **Resource types (\*required):** [Graph\*](#list_detective-resource-Graph)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_detective-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DisableOrganizationAdminAccount](https://docs.aws.amazon.com/detective/latest/APIReference/API_DisableOrganizationAdminAccount.html)  **
  - **Description:** Grants permission to remove the Amazon Detective delegated administrator account for an organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DisassociateMembership](https://docs.aws.amazon.com/detective/latest/APIReference/API_DisassociateMembership.html)  **
  - **Description:** Grants permission to remove the association of this account with a behavior graph
  - **Resource types (\*required):** [Graph\*](#list_detective-resource-Graph)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_detective-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [EnableOrganizationAdminAccount](https://docs.aws.amazon.com/detective/latest/APIReference/API_EnableOrganizationAdminAccount.html)  **
  - **Description:** Grants permission to designate the Amazon Detective delegated administrator account for an organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [GetInvestigation](https://docs.aws.amazon.com/detective/latest/APIReference/API_GetInvestigation.html)  **
  - **Description:** Grants permission to get an investigation's status and metadata
  - **Resource types (\*required):** [Graph\*](#list_detective-resource-Graph)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_detective-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetMembers](https://docs.aws.amazon.com/detective/latest/APIReference/API_GetMembers.html)  **
  - **Description:** Grants permission to retrieve details on specified members of a behavior graph
  - **Resource types (\*required):** [Graph\*](#list_detective-resource-Graph)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_detective-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListDatasourcePackages](https://docs.aws.amazon.com/detective/latest/APIReference/API_ListDatasourcePackages.html)  **
  - **Description:** Grants permission to list a graph's datasource package ingest states and timestamps for the most recent state changes in a behavior graph managed by this account
  - **Resource types (\*required):** [Graph\*](#list_detective-resource-Graph)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_detective-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListGraphs](https://docs.aws.amazon.com/detective/latest/APIReference/API_ListGraphs.html)  **
  - **Description:** Grants permission to list behavior graphs managed by this account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListIndicators](https://docs.aws.amazon.com/detective/latest/APIReference/API_ListIndicators.html)  **
  - **Description:** Grants permission to list the indicators of an investigation
  - **Resource types (\*required):** [Graph\*](#list_detective-resource-Graph)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_detective-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListInvestigations](https://docs.aws.amazon.com/detective/latest/APIReference/API_ListInvestigations.html)  **
  - **Description:** Grants permission to list the investigations of a behavior graph
  - **Resource types (\*required):** [Graph\*](#list_detective-resource-Graph)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_detective-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListInvitations](https://docs.aws.amazon.com/detective/latest/APIReference/API_ListInvitations.html)  **
  - **Description:** Grants permission to retrieve details on the behavior graphs to which this account has been invited to join
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListMembers](https://docs.aws.amazon.com/detective/latest/APIReference/API_ListMembers.html)  **
  - **Description:** Grants permission to retrieve details on all members of a behavior graph
  - **Resource types (\*required):** [Graph\*](#list_detective-resource-Graph)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_detective-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListOrganizationAdminAccount](https://docs.aws.amazon.com/detective/latest/APIReference/API_ListOrganizationAdminAccounts.html)  **
  - **Description:** Grants permission to view the current Amazon Detective delegated administrator account for an organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/detective/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list the tag values that are assigned to a behavior graph
  - **Resource types (\*required):** [Graph\*](#list_detective-resource-Graph)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_detective-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [RejectInvitation](https://docs.aws.amazon.com/detective/latest/APIReference/API_RejectInvitation.html)  **
  - **Description:** Grants permission to reject an invitation to become a member of a behavior graph
  - **Resource types (\*required):** [Graph\*](#list_detective-resource-Graph)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_detective-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartInvestigation](https://docs.aws.amazon.com/detective/latest/APIReference/API_StartInvestigation.html)  **
  - **Description:** Grants permission to start investigations
  - **Resource types (\*required):** [Graph\*](#list_detective-resource-Graph)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_detective-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartMonitoringMember](https://docs.aws.amazon.com/detective/latest/APIReference/API_StartMonitoringMember.html)  **
  - **Description:** Grants permission to start data ingest for a member account that has a status of ACCEPTED\_BUT\_DISABLED
  - **Resource types (\*required):** [Graph\*](#list_detective-resource-Graph)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_detective-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/detective/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to assign tag values to a behavior graph
  - **Resource types (\*required):** [Graph\*](#list_detective-resource-Graph)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_detective-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_detective-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_detective-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/detective/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tag values from a behavior graph
  - **Resource types (\*required):** [Graph\*](#list_detective-resource-Graph)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_detective-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_detective-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateDatasourcePackages](https://docs.aws.amazon.com/detective/latest/APIReference/API_UpdateDatasourcePackages.html)  **
  - **Description:** Grants permission to enable or disable datasource package(s) in a behavior graph managed by this account
  - **Resource types (\*required):** [Graph\*](#list_detective-resource-Graph)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_detective-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateInvestigationState](https://docs.aws.amazon.com/detective/latest/APIReference/API_UpdateInvestigationState.html)  **
  - **Description:** Grants permission to update an investigation's state and metadata
  - **Resource types (\*required):** [Graph\*](#list_detective-resource-Graph)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_detective-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateOrganizationConfiguration](https://docs.aws.amazon.com/detective/latest/APIReference/API_UpdateOrganizationConfiguration.html)  **
  - **Description:** Grants permission to update the current configuration related to the Amazon Detective integration with AWS Organizations
  - **Resource types (\*required):** [Graph\*](#list_detective-resource-Graph)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_detective-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for Amazon Detective
<a name="list_detective-permission-only-actions"></a>

The following actions are defined by Amazon Detective but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [GetFreeTrialEligibility](https://docs.aws.amazon.com/detective/latest/adminguide/free-trial-overview.html)  **
  - **Description:** Grants permission to retrieve a behavior graph's eligibility for a free trial period
  - **Resource types (\*required):** [Graph\*](#list_detective-resource-Graph)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_detective-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetGraphIngestState](https://docs.aws.amazon.com/detective/latest/adminguide/detective-source-data-about.html)  **
  - **Description:** Grants permission to retrieve the data ingestion state of a behavior graph
  - **Resource types (\*required):** [Graph\*](#list_detective-resource-Graph)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_detective-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPricingInformation](https://docs.aws.amazon.com/detective/latest/adminguide/usage-projected-cost-calculation.html)  **
  - **Description:** Grants permission to retrieve information about Amazon Detective's pricing
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetUsageInformation](https://docs.aws.amazon.com/detective/latest/adminguide/tracking-usage-logging.html)  **
  - **Description:** Grants permission to list usage information of a behavior graph
  - **Resource types (\*required):** [Graph\*](#list_detective-resource-Graph)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_detective-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [InvokeAssistant](https://docs.aws.amazon.com/detective/latest/userguide/finding-groups-summary.html)  **
  - **Description:** Grants permission to invoke Detective's Assistant
  - **Resource types (\*required):** [Graph\*](#list_detective-resource-Graph)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_detective-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListHighDegreeEntities](https://docs.aws.amazon.com/detective/latest/userguide/high-volume-entities.html)  **
  - **Description:** Grants permission to retrieve high volume entities whose relationships cannot be stored by Detective
  - **Resource types (\*required):** [Graph\*](#list_detective-resource-Graph)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_detective-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [SearchGraph](https://docs.aws.amazon.com/detective/latest/userguide/detective-search.html)  **
  - **Description:** Grants permission to search the data stored in a behavior graph
  - **Resource types (\*required):** [Graph\*](#list_detective-resource-Graph)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_detective-aws_ResourceTag___TagKey_)
  - **Access level:** Read



## Resource types defined by Amazon Detective
<a name="list_detective-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [Graph](https://docs.aws.amazon.com/detective/latest/adminguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-resources)  | arn:${Partition}:detective:${Region}:${Account}:graph:${ResourceId} | [aws:ResourceTag/${TagKey}](#list_detective-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon Detective
<a name="list_detective-policy-keys"></a>

Amazon Detective defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by specifying the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by specifying the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by specifying the tag keys that are passed in the request | ArrayOfString | 