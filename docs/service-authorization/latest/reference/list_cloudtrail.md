

# Actions, resources, and condition keys for AWS CloudTrail
<a name="list_cloudtrail"></a>

AWS CloudTrail (service prefix: `cloudtrail`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/security_iam_service-with-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/cloudtrail/cloudtrail.json) for this service.

**Topics**
+ [API operations defined by AWS CloudTrail](#list_cloudtrail-operations)
+ [Actions defined by AWS CloudTrail](#list_cloudtrail-actions-as-permissions)
+ [Permission-only actions for AWS CloudTrail](#list_cloudtrail-permission-only-actions)
+ [Resource types defined by AWS CloudTrail](#list_cloudtrail-resources-for-iam-policies)
+ [Condition keys for AWS CloudTrail](#list_cloudtrail-policy-keys)

## API operations defined by AWS CloudTrail
<a name="list_cloudtrail-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_cloudtrail-actions-as-permissions).




- **   AddTags  **
  - **IAM action:**  [cloudtrail:AddTags](#list_cloudtrail-action-AddTags) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   CancelQuery  **
  - **IAM action:**  [cloudtrail:CancelQuery](#list_cloudtrail-action-CancelQuery) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateChannel  **
  - **IAM action:**  [cloudtrail:AddTags](#list_cloudtrail-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [cloudtrail:CreateChannel](#list_cloudtrail-action-CreateChannel)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateDashboard  **
  - **IAM action:**  [cloudtrail:AddTags](#list_cloudtrail-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [cloudtrail:CreateDashboard](#list_cloudtrail-action-CreateDashboard)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cloudtrail:StartDashboardRefresh](#list_cloudtrail-action-StartDashboardRefresh)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cloudtrail:StartQuery](#list_cloudtrail-action-StartQuery)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateEventDataStore  **
  - **IAM action:**  [cloudtrail:AddTags](#list_cloudtrail-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [cloudtrail:CreateEventDataStore](#list_cloudtrail-action-CreateEventDataStore)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateTrail  **
  - **IAM action:**  [cloudtrail:AddTags](#list_cloudtrail-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [cloudtrail:CreateTrail](#list_cloudtrail-action-CreateTrail)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** cloudtrail.amazonaws.com, cloudtrail.preprod.amazonaws.com / **Access level:** Write

- **   DeleteChannel  **
  - **IAM action:**  [cloudtrail:DeleteChannel](#list_cloudtrail-action-DeleteChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDashboard  **
  - **IAM action:**  [cloudtrail:DeleteDashboard](#list_cloudtrail-action-DeleteDashboard) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEventDataStore  **
  - **IAM action:**  [cloudtrail:DeleteEventDataStore](#list_cloudtrail-action-DeleteEventDataStore) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteResourcePolicy  **
  - **IAM action:**  [cloudtrail:DeleteResourcePolicy](#list_cloudtrail-action-DeleteResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTrail  **
  - **IAM action:**  [cloudtrail:DeleteTrail](#list_cloudtrail-action-DeleteTrail) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeregisterOrganizationDelegatedAdmin  **
  - **IAM action:**  [cloudtrail:DeregisterOrganizationDelegatedAdmin](#list_cloudtrail-action-DeregisterOrganizationDelegatedAdmin) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeQuery  **
  - **IAM action:**  [cloudtrail:DescribeQuery](#list_cloudtrail-action-DescribeQuery) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeTrails  **
  - **IAM action:**  [cloudtrail:DescribeTrails](#list_cloudtrail-action-DescribeTrails) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DisableFederation  **
  - **IAM action:**  [cloudtrail:DisableFederation](#list_cloudtrail-action-DisableFederation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   EnableFederation  **
  - **IAM action:**  [cloudtrail:EnableFederation](#list_cloudtrail-action-EnableFederation)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** cloudtrail.amazonaws.com, cloudtrail.preprod.amazonaws.com / **Access level:** Write

- **   GenerateQuery  **
  - **IAM action:**  [cloudtrail:GenerateQuery](#list_cloudtrail-action-GenerateQuery) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetChannel  **
  - **IAM action:**  [cloudtrail:GetChannel](#list_cloudtrail-action-GetChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDashboard  **
  - **IAM action:**  [cloudtrail:GetDashboard](#list_cloudtrail-action-GetDashboard) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEventConfiguration  **
  - **IAM action:**  [cloudtrail:GetEventConfiguration](#list_cloudtrail-action-GetEventConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEventDataStore  **
  - **IAM action:**  [cloudtrail:GetEventDataStore](#list_cloudtrail-action-GetEventDataStore) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEventSelectors  **
  - **IAM action:**  [cloudtrail:GetEventSelectors](#list_cloudtrail-action-GetEventSelectors) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetImport  **
  - **IAM action:**  [cloudtrail:GetImport](#list_cloudtrail-action-GetImport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetInsightSelectors  **
  - **IAM action:**  [cloudtrail:GetInsightSelectors](#list_cloudtrail-action-GetInsightSelectors) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetQueryResults  **
  - **IAM action:**  [cloudtrail:GetQueryResults](#list_cloudtrail-action-GetQueryResults) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResourcePolicy  **
  - **IAM action:**  [cloudtrail:GetResourcePolicy](#list_cloudtrail-action-GetResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTrail  **
  - **IAM action:**  [cloudtrail:GetTrail](#list_cloudtrail-action-GetTrail) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTrailStatus  **
  - **IAM action:**  [cloudtrail:GetTrailStatus](#list_cloudtrail-action-GetTrailStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListChannels  **
  - **IAM action:**  [cloudtrail:ListChannels](#list_cloudtrail-action-ListChannels) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDashboards  **
  - **IAM action:**  [cloudtrail:ListDashboards](#list_cloudtrail-action-ListDashboards) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEventDataStores  **
  - **IAM action:**  [cloudtrail:ListEventDataStores](#list_cloudtrail-action-ListEventDataStores) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListImportFailures  **
  - **IAM action:**  [cloudtrail:ListImportFailures](#list_cloudtrail-action-ListImportFailures) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListImports  **
  - **IAM action:**  [cloudtrail:ListImports](#list_cloudtrail-action-ListImports) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListInsightsData  **
  - **IAM action:**  [cloudtrail:ListInsightsData](#list_cloudtrail-action-ListInsightsData) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListInsightsMetricData  **
  - **IAM action:**  [cloudtrail:ListInsightsData](#list_cloudtrail-action-ListInsightsData)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [cloudtrail:LookupEvents](#list_cloudtrail-action-LookupEvents)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   ListPublicKeys  **
  - **IAM action:**  [cloudtrail:ListPublicKeys](#list_cloudtrail-action-ListPublicKeys) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListQueries  **
  - **IAM action:**  [cloudtrail:ListQueries](#list_cloudtrail-action-ListQueries) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTags  **
  - **IAM action:**  [cloudtrail:ListTags](#list_cloudtrail-action-ListTags) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTrails  **
  - **IAM action:**  [cloudtrail:ListTrails](#list_cloudtrail-action-ListTrails) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   LookupEvents  **
  - **IAM action:**  [cloudtrail:LookupEvents](#list_cloudtrail-action-LookupEvents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PutEventConfiguration  **
  - **IAM action:**  [cloudtrail:PutEventConfiguration](#list_cloudtrail-action-PutEventConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutEventSelectors  **
  - **IAM action:**  [cloudtrail:PutEventSelectors](#list_cloudtrail-action-PutEventSelectors) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutInsightSelectors  **
  - **IAM action:**  [cloudtrail:PutInsightSelectors](#list_cloudtrail-action-PutInsightSelectors) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutResourcePolicy  **
  - **IAM action:**  [cloudtrail:PutResourcePolicy](#list_cloudtrail-action-PutResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RegisterOrganizationDelegatedAdmin  **
  - **IAM action:**  [cloudtrail:RegisterOrganizationDelegatedAdmin](#list_cloudtrail-action-RegisterOrganizationDelegatedAdmin) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RemoveTags  **
  - **IAM action:**  [cloudtrail:RemoveTags](#list_cloudtrail-action-RemoveTags) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   RestoreEventDataStore  **
  - **IAM action:**  [cloudtrail:RestoreEventDataStore](#list_cloudtrail-action-RestoreEventDataStore) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SearchSampleQueries  **
  - **IAM action:**  [cloudtrail:SearchSampleQueries](#list_cloudtrail-action-SearchSampleQueries) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   StartDashboardRefresh  **
  - **IAM action:**  [cloudtrail:StartDashboardRefresh](#list_cloudtrail-action-StartDashboardRefresh)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cloudtrail:StartQuery](#list_cloudtrail-action-StartQuery)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   StartEventDataStoreIngestion  **
  - **IAM action:**  [cloudtrail:StartEventDataStoreIngestion](#list_cloudtrail-action-StartEventDataStoreIngestion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartImport  **
  - **IAM action:**  [cloudtrail:StartImport](#list_cloudtrail-action-StartImport)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** cloudtrail.amazonaws.com, cloudtrail.preprod.amazonaws.com / **Access level:** Write

- **   StartLogging  **
  - **IAM action:**  [cloudtrail:StartLogging](#list_cloudtrail-action-StartLogging) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartQuery  **
  - **IAM action:**  [cloudtrail:StartQuery](#list_cloudtrail-action-StartQuery) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopEventDataStoreIngestion  **
  - **IAM action:**  [cloudtrail:StopEventDataStoreIngestion](#list_cloudtrail-action-StopEventDataStoreIngestion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopImport  **
  - **IAM action:**  [cloudtrail:StopImport](#list_cloudtrail-action-StopImport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopLogging  **
  - **IAM action:**  [cloudtrail:StopLogging](#list_cloudtrail-action-StopLogging) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateChannel  **
  - **IAM action:**  [cloudtrail:UpdateChannel](#list_cloudtrail-action-UpdateChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDashboard  **
  - **IAM action:**  [cloudtrail:StartDashboardRefresh](#list_cloudtrail-action-StartDashboardRefresh)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cloudtrail:StartQuery](#list_cloudtrail-action-StartQuery)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cloudtrail:UpdateDashboard](#list_cloudtrail-action-UpdateDashboard)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UpdateEventDataStore  **
  - **IAM action:**  [cloudtrail:UpdateEventDataStore](#list_cloudtrail-action-UpdateEventDataStore) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateTrail  **
  - **IAM action:**  [cloudtrail:UpdateTrail](#list_cloudtrail-action-UpdateTrail)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** cloudtrail.amazonaws.com, cloudtrail.preprod.amazonaws.com / **Access level:** Write



## Actions defined by AWS CloudTrail
<a name="list_cloudtrail-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AddTags](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_AddTags.html)  **
  - **Description:** Grants permission to add one or more tags to a trail, event data store, channel or dashboard, up to a limit of 50
  - **Resource types (\*required):** [channel](#list_cloudtrail-resource-channel) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudtrail-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudtrail-aws_TagKeys)
  - **Resource types (\*required):** [dashboard](#list_cloudtrail-resource-dashboard) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudtrail-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudtrail-aws_TagKeys)
  - **Resource types (\*required):** [eventdatastore](#list_cloudtrail-resource-eventdatastore) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudtrail-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudtrail-aws_TagKeys)
  - **Resource types (\*required):** [trail](#list_cloudtrail-resource-trail) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudtrail-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudtrail-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [CancelQuery](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_CancelQuery.html)  **
  - **Description:** Grants permission to cancel a running query
  - **Resource types (\*required):** [eventdatastore\*](#list_cloudtrail-resource-eventdatastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateChannel](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_CreateChannel.html)  **
  - **Description:** Grants permission to create a channel
  - **Resource types (\*required):** [channel\*](#list_cloudtrail-resource-channel) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudtrail-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudtrail-aws_TagKeys)
  - **Resource types (\*required):** [eventdatastore\*](#list_cloudtrail-resource-eventdatastore) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudtrail-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudtrail-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDashboard](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_CreateDashboard.html)  **
  - **Description:** Grants permission to create a dashboard
  - **Resource types (\*required):** [dashboard\*](#list_cloudtrail-resource-dashboard)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudtrail-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudtrail-aws_TagKeys)
  - **Access level:** Write

- **   [CreateEventDataStore](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_CreateEventDataStore.html)  **
  - **Description:** Grants permission to create an event data store
  - **Resource types (\*required):** [eventdatastore\*](#list_cloudtrail-resource-eventdatastore)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudtrail-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudtrail-aws_TagKeys)
  - **Access level:** Write

- **   [CreateTrail](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_CreateTrail.html)  **
  - **Description:** Grants permission to create a trail that specifies the settings for delivery of log data to an Amazon S3 bucket
  - **Resource types (\*required):** [trail\*](#list_cloudtrail-resource-trail)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudtrail-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudtrail-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteChannel](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_DeleteChannel.html)  **
  - **Description:** Grants permission to delete a channel
  - **Resource types (\*required):** [channel\*](#list_cloudtrail-resource-channel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDashboard](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_DeleteDashboard.html)  **
  - **Description:** Grants permission to delete a dashboard
  - **Resource types (\*required):** [dashboard\*](#list_cloudtrail-resource-dashboard)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteEventDataStore](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_DeleteEventDataStore.html)  **
  - **Description:** Grants permission to delete an event data store
  - **Resource types (\*required):** [eventdatastore\*](#list_cloudtrail-resource-eventdatastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteResourcePolicy](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_DeleteResourcePolicy.html)  **
  - **Description:** Grants permission to delete a resource policy from the provided resource
  - **Resource types (\*required):** [channel](#list_cloudtrail-resource-channel) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [dashboard](#list_cloudtrail-resource-dashboard) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [eventdatastore](#list_cloudtrail-resource-eventdatastore) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTrail](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_DeleteTrail.html)  **
  - **Description:** Grants permission to delete a trail
  - **Resource types (\*required):** [trail\*](#list_cloudtrail-resource-trail)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeregisterOrganizationDelegatedAdmin](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_DeregisterOrganizationDelegatedAdmin.html)  **
  - **Description:** Grants permission to deregister an AWS Organizations member account as a delegated administrator
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DescribeQuery](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_DescribeQuery.html)  **
  - **Description:** Grants permission to list details for the query
  - **Resource types (\*required):** [eventdatastore\*](#list_cloudtrail-resource-eventdatastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeTrails](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_DescribeTrails.html)  **
  - **Description:** Grants permission to list settings for the trails associated with the current region for your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DisableFederation](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_DisableFederation.html)  **
  - **Description:** Grants permission to disable federation of event data store data by using the AWS Glue Data Catalog
  - **Resource types (\*required):** [eventdatastore\*](#list_cloudtrail-resource-eventdatastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [EnableFederation](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_EnableFederation.html)  **
  - **Description:** Grants permission to enable federation of event data store data by using the AWS Glue Data Catalog
  - **Resource types (\*required):** [eventdatastore\*](#list_cloudtrail-resource-eventdatastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GenerateQuery](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-query-generator.html)  **
  - **Description:** Grants permission to generate a query for a specified event data store using the CloudTrail Lake query generator
  - **Resource types (\*required):** [eventdatastore\*](#list_cloudtrail-resource-eventdatastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetChannel](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_GetChannel.html)  **
  - **Description:** Grants permission to return information about a specific channel
  - **Resource types (\*required):** [channel\*](#list_cloudtrail-resource-channel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDashboard](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_GetDashboard.html)  **
  - **Description:** Grants permission to list settings for the dashboard
  - **Resource types (\*required):** [dashboard\*](#list_cloudtrail-resource-dashboard)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetEventConfiguration](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_GetEventConfiguration.html)  **
  - **Description:** Grants permission to list event configurations that are configured for a trail or an event data store
  - **Resource types (\*required):** [eventdatastore](#list_cloudtrail-resource-eventdatastore) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [trail](#list_cloudtrail-resource-trail) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetEventDataStore](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_GetEventDataStore.html)  **
  - **Description:** Grants permission to list settings for the event data store
  - **Resource types (\*required):** [eventdatastore\*](#list_cloudtrail-resource-eventdatastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetEventDataStoreData](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-federation.html#query-federation-permissions)  **
  - **Description:** Grants permission to get data from an event data store by using the AWS Glue Data Catalog
  - **Resource types (\*required):** [eventdatastore\*](#list_cloudtrail-resource-eventdatastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetEventSelectors](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_GetEventSelectors.html)  **
  - **Description:** Grants permission to list settings for event selectors configured for a trail
  - **Resource types (\*required):** [trail\*](#list_cloudtrail-resource-trail)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetImport](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_GetImport.html)  **
  - **Description:** Grants permission to return information about a specific import
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetInsightSelectors](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_GetInsightSelectors.html)  **
  - **Description:** Grants permission to list CloudTrail Insights selectors that are configured for a trail or event data store
  - **Resource types (\*required):** [eventdatastore](#list_cloudtrail-resource-eventdatastore) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [trail](#list_cloudtrail-resource-trail) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetQueryResults](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_GetQueryResults.html)  **
  - **Description:** Grants permission to fetch results of a complete query
  - **Resource types (\*required):** [eventdatastore\*](#list_cloudtrail-resource-eventdatastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetResourcePolicy](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_GetResourcePolicy.html)  **
  - **Description:** Grants permission to get the resource policy attached to the provided resource
  - **Resource types (\*required):** [channel](#list_cloudtrail-resource-channel) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [dashboard](#list_cloudtrail-resource-dashboard) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [eventdatastore](#list_cloudtrail-resource-eventdatastore) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetTrail](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_GetTrail.html)  **
  - **Description:** Grants permission to list settings for the trail
  - **Resource types (\*required):** [trail\*](#list_cloudtrail-resource-trail)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetTrailStatus](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_GetTrailStatus.html)  **
  - **Description:** Grants permission to retrieve a JSON-formatted list of information about the specified trail
  - **Resource types (\*required):** [trail\*](#list_cloudtrail-resource-trail)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListChannels](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_ListChannels.html)  **
  - **Description:** Grants permission to list the channels in the current account, and their source names
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDashboards](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_ListDashboards.html)  **
  - **Description:** Grants permission to list dashboards associated with the current region for your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListEventDataStores](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_ListEventDataStores.html)  **
  - **Description:** Grants permission to list event data stores associated with the current region for your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListImportFailures](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_ListImportFailures.html)  **
  - **Description:** Grants permission to return a list of failures for the specified import
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListImports](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_ListImports.html)  **
  - **Description:** Grants permission to return information on all imports, or a select set of imports by ImportStatus or Destination
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListInsightsData](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_ListInsightsData.html)  **
  - **Description:** Grants permission to retrieve data captured by CloudTrail Insights
  - **Resource types (\*required):** [trail\*](#list_cloudtrail-resource-trail)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListPublicKeys](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_ListPublicKeys.html)  **
  - **Description:** Grants permission to list the public keys whose private keys were used to sign trail digest files within a specified time range
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListQueries](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_ListQueries.html)  **
  - **Description:** Grants permission to list queries associated with an event data store
  - **Resource types (\*required):** [eventdatastore\*](#list_cloudtrail-resource-eventdatastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTags](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_ListTags.html)  **
  - **Description:** Grants permission to list the tags for trails, event data stores, channels or dashboards in the current region
  - **Resource types (\*required):** [channel](#list_cloudtrail-resource-channel) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [dashboard](#list_cloudtrail-resource-dashboard) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [eventdatastore](#list_cloudtrail-resource-eventdatastore) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [trail](#list_cloudtrail-resource-trail) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListTrails](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_ListTrails.html)  **
  - **Description:** Grants permission to list trails associated with the current region for your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [LookupEvents](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_LookupEvents.html)  **
  - **Description:** Grants permission to look up and retrieve metric data for API activity events captured by CloudTrail that create, update, or delete resources in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [PutEventConfiguration](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_PutEventConfiguration.html)  **
  - **Description:** Grants permission to create and update event configurations for a trail or an event data store
  - **Resource types (\*required):** [eventdatastore](#list_cloudtrail-resource-eventdatastore) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [trail](#list_cloudtrail-resource-trail) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutEventSelectors](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_PutEventSelectors.html)  **
  - **Description:** Grants permission to create and update event selectors for a trail
  - **Resource types (\*required):** [trail\*](#list_cloudtrail-resource-trail)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutInsightSelectors](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_PutInsightSelectors.html)  **
  - **Description:** Grants permission to create and update CloudTrail Insights selectors for a trail or event data store
  - **Resource types (\*required):** [eventdatastore](#list_cloudtrail-resource-eventdatastore) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [trail](#list_cloudtrail-resource-trail) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutResourcePolicy](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_PutResourcePolicy.html)  **
  - **Description:** Grants permission to attach a resource policy to the provided resource
  - **Resource types (\*required):** [channel](#list_cloudtrail-resource-channel) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [dashboard](#list_cloudtrail-resource-dashboard) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [eventdatastore](#list_cloudtrail-resource-eventdatastore) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RegisterOrganizationDelegatedAdmin](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_RegisterOrganizationDelegatedAdmin.html)  **
  - **Description:** Grants permission to register an AWS Organizations member account as a delegated administrator
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [RemoveTags](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_RemoveTags.html)  **
  - **Description:** Grants permission to remove tags from a trail, event data store, channel or dashboard
  - **Resource types (\*required):** [channel](#list_cloudtrail-resource-channel) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudtrail-aws_TagKeys)
  - **Resource types (\*required):** [dashboard](#list_cloudtrail-resource-dashboard) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudtrail-aws_TagKeys)
  - **Resource types (\*required):** [eventdatastore](#list_cloudtrail-resource-eventdatastore) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudtrail-aws_TagKeys)
  - **Resource types (\*required):** [trail](#list_cloudtrail-resource-trail) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudtrail-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [RestoreEventDataStore](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_RestoreEventDataStore.html)  **
  - **Description:** Grants permission to restore an event data store
  - **Resource types (\*required):** [eventdatastore\*](#list_cloudtrail-resource-eventdatastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SearchSampleQueries](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-console-queries.html)  **
  - **Description:** Grants permission to perform semantic search for CloudTrail Lake sample queries
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [StartDashboardRefresh](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_StartDashboardRefresh.html)  **
  - **Description:** Grants permission to start a refresh on the specified dashboard
  - **Resource types (\*required):** [dashboard\*](#list_cloudtrail-resource-dashboard)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartEventDataStoreIngestion](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_StartEventDataStoreIngestion.html)  **
  - **Description:** Grants permission to start ingestion on an event data store
  - **Resource types (\*required):** [eventdatastore\*](#list_cloudtrail-resource-eventdatastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartImport](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_StartImport.html)  **
  - **Description:** Grants permission to start an import of logged trail events from a source S3 bucket to a destination event data store
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartLogging](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_StartLogging.html)  **
  - **Description:** Grants permission to start the recording of AWS API calls and log file delivery for a trail
  - **Resource types (\*required):** [trail\*](#list_cloudtrail-resource-trail)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartQuery](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_StartQuery.html)  **
  - **Description:** Grants permission to start a new query on a specified event data store
  - **Resource types (\*required):** [eventdatastore\*](#list_cloudtrail-resource-eventdatastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopEventDataStoreIngestion](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_StopEventDataStoreIngestion.html)  **
  - **Description:** Grants permission to stop ingestion on an event data store
  - **Resource types (\*required):** [eventdatastore\*](#list_cloudtrail-resource-eventdatastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopImport](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_StopImport.html)  **
  - **Description:** Grants permission to stop a specified import
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StopLogging](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_StopLogging.html)  **
  - **Description:** Grants permission to stop the recording of AWS API calls and log file delivery for a trail
  - **Resource types (\*required):** [trail\*](#list_cloudtrail-resource-trail)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateChannel](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_UpdateChannel.html)  **
  - **Description:** Grants permission to update a channel
  - **Resource types (\*required):** [channel\*](#list_cloudtrail-resource-channel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDashboard](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_UpdateDashboard.html)  **
  - **Description:** Grants permission to update a dashboard
  - **Resource types (\*required):** [dashboard\*](#list_cloudtrail-resource-dashboard)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateEventDataStore](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_UpdateEventDataStore.html)  **
  - **Description:** Grants permission to update an event data store
  - **Resource types (\*required):** [eventdatastore\*](#list_cloudtrail-resource-eventdatastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateTrail](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_UpdateTrail.html)  **
  - **Description:** Grants permission to update the settings that specify delivery of log files
  - **Resource types (\*required):** [trail\*](#list_cloudtrail-resource-trail)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for AWS CloudTrail
<a name="list_cloudtrail-permission-only-actions"></a>

The following actions are defined by AWS CloudTrail but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [CreateServiceLinkedChannel](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/viewing-service-linked-channels.html#slc-service-events)  **
  - **Description:** Grants permission to create a service-linked channel that specifies the settings for delivery of log data to an AWS service
  - **Resource types (\*required):** [channel\*](#list_cloudtrail-resource-channel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteServiceLinkedChannel](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/viewing-service-linked-channels.html#slc-service-events)  **
  - **Description:** Grants permission to delete a service-linked channel
  - **Resource types (\*required):** [channel\*](#list_cloudtrail-resource-channel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GenerateQueryResultsSummary](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-results-summary.html)  **
  - **Description:** Grants permission to generate a results summary for specified queries using the CloudTrail natural language generator
  - **Resource types (\*required):** [eventdatastore\*](#list_cloudtrail-resource-eventdatastore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetServiceLinkedChannel](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/viewing-service-linked-channels.html#slc-service-events)  **
  - **Description:** Grants permission to list settings for the service-linked channel
  - **Resource types (\*required):** [channel\*](#list_cloudtrail-resource-channel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListServiceLinkedChannels](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/viewing-service-linked-channels.html#slc-service-events)  **
  - **Description:** Grants permission to list service-linked channels associated with the current region for a specified account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [UpdateServiceLinkedChannel](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/viewing-service-linked-channels.html#slc-service-events)  **
  - **Description:** Grants permission to update the service-linked channel settings for delivery of log data to an AWS service
  - **Resource types (\*required):** [channel\*](#list_cloudtrail-resource-channel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS CloudTrail
<a name="list_cloudtrail-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [channel](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/how-cloudtrail-works.html#how-cloudtrail-works-channels)  | arn:${Partition}:cloudtrail:${Region}:${Account}:channel/${ChannelId} | [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_) | 
|  [dashboard](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-dashboard.html)  | arn:${Partition}:cloudtrail:${Region}:${Account}:dashboard/${DashboardName} | [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_) | 
|  [eventdatastore](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/how-cloudtrail-works.html#how-cloudtrail-works-lake)  | arn:${Partition}:cloudtrail:${Region}:${Account}:eventdatastore/${EventDataStoreId} | [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_) | 
|  [trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/how-cloudtrail-works.html#how-cloudtrail-works-trails)  | arn:${Partition}:cloudtrail:${Region}:${Account}:trail/${TrailName} | [aws:ResourceTag/${TagKey}](#list_cloudtrail-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS CloudTrail
<a name="list_cloudtrail-policy-keys"></a>

AWS CloudTrail defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys in a request | ArrayOfString | 