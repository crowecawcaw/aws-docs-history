

# Actions, resources, and condition keys for Amazon QuickSight
<a name="list_quicksight"></a>

Amazon QuickSight (service prefix: `quicksight`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/quicksight/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/quicksight/latest/user/identity.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/quicksight/quicksight.json) for this service.

**Topics**
+ [API operations defined by Amazon QuickSight](#list_quicksight-operations)
+ [Actions defined by Amazon QuickSight](#list_quicksight-actions-as-permissions)
+ [Permission-only actions for Amazon QuickSight](#list_quicksight-permission-only-actions)
+ [Resource types defined by Amazon QuickSight](#list_quicksight-resources-for-iam-policies)
+ [Condition keys for Amazon QuickSight](#list_quicksight-policy-keys)

## API operations defined by Amazon QuickSight
<a name="list_quicksight-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_quicksight-actions-as-permissions).




- **   BatchCreateTopicReviewedAnswer  **
  - **IAM action:**  [quicksight:BatchCreateTopicReviewedAnswer](#list_quicksight-action-BatchCreateTopicReviewedAnswer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchDeleteKnowledgeBase  **
  - **IAM action:**  [quicksight:BatchDeleteKnowledgeBase](#list_quicksight-action-BatchDeleteKnowledgeBase)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [quicksight:DeleteKnowledgeBase](#list_quicksight-action-DeleteKnowledgeBase)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   BatchDeleteTopicReviewedAnswer  **
  - **IAM action:**  [quicksight:BatchDeleteTopicReviewedAnswer](#list_quicksight-action-BatchDeleteTopicReviewedAnswer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchDescribeUserLimits  **
  - **IAM action:**  [quicksight:BatchDescribeUserLimits](#list_quicksight-action-BatchDescribeUserLimits) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   CancelIngestion  **
  - **IAM action:**  [quicksight:CancelIngestion](#list_quicksight-action-CancelIngestion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateAccountCustomization  **
  - **IAM action:**  [quicksight:CreateAccountCustomization](#list_quicksight-action-CreateAccountCustomization)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [quicksight:TagResource](#list_quicksight-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateAccountSubscription  **
  - **IAM action:**  [quicksight:CreateAccountSubscription](#list_quicksight-action-CreateAccountSubscription)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [quicksight:Subscribe](#list_quicksight-action-Subscribe)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [quicksight:TagResource](#list_quicksight-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateActionConnector  **
  - **IAM action:**  [quicksight:CreateActionConnector](#list_quicksight-action-CreateActionConnector)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [quicksight:TagResource](#list_quicksight-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** quicksight.amazonaws.com / **Access level:** Write

- **   CreateAgent  **
  - **IAM action:**  [quicksight:CreateAgent](#list_quicksight-action-CreateAgent)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [quicksight:TagResource](#list_quicksight-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateAnalysis  **
  - **IAM action:**  [quicksight:CreateAnalysis](#list_quicksight-action-CreateAnalysis)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [quicksight:CreateFolderMembership](#list_quicksight-action-CreateFolderMembership)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [quicksight:DescribeTemplate](#list_quicksight-action-DescribeTemplate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [quicksight:DescribeTheme](#list_quicksight-action-DescribeTheme)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [quicksight:PassDataSet](#list_quicksight-action-PassDataSet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [quicksight:PassTopic](#list_quicksight-action-PassTopic)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [quicksight:TagResource](#list_quicksight-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateApprovalPolicy  **
  - **IAM action:**  [quicksight:CreateApprovalPolicy](#list_quicksight-action-CreateApprovalPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateBrand  **
  - **IAM action:**  [quicksight:CreateBrand](#list_quicksight-action-CreateBrand)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [quicksight:TagResource](#list_quicksight-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateCustomPermissions  **
  - **IAM action:**  [quicksight:CreateCustomPermissions](#list_quicksight-action-CreateCustomPermissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [quicksight:TagResource](#list_quicksight-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateDashboard  **
  - **IAM action:**  [quicksight:CreateDashboard](#list_quicksight-action-CreateDashboard)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [quicksight:CreateFolderMembership](#list_quicksight-action-CreateFolderMembership)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [quicksight:DescribeTemplate](#list_quicksight-action-DescribeTemplate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [quicksight:DescribeTheme](#list_quicksight-action-DescribeTheme)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [quicksight:PassDataSet](#list_quicksight-action-PassDataSet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [quicksight:TagResource](#list_quicksight-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateDataSet  **
  - **IAM action:**  [quicksight:CreateDataSet](#list_quicksight-action-CreateDataSet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [quicksight:CreateFolderMembership](#list_quicksight-action-CreateFolderMembership)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [quicksight:PassDataSet](#list_quicksight-action-PassDataSet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [quicksight:PassDataSource](#list_quicksight-action-PassDataSource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [quicksight:TagResource](#list_quicksight-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateDataSource  **
  - **IAM action:**  [quicksight:CreateDataSource](#list_quicksight-action-CreateDataSource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [quicksight:CreateFolderMembership](#list_quicksight-action-CreateFolderMembership)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [quicksight:TagResource](#list_quicksight-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** quicksight.amazonaws.com / **Access level:** Write

- **   CreateDlpSetting  **
  - **IAM action:**  [quicksight:CreateDlpSetting](#list_quicksight-action-CreateDlpSetting)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [quicksight:TagResource](#list_quicksight-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateFlow  **
  - **IAM action:**  [quicksight:CreateFlow](#list_quicksight-action-CreateFlow)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [quicksight:TagResource](#list_quicksight-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateFolder  **
  - **IAM action:**  [quicksight:CreateFolder](#list_quicksight-action-CreateFolder)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [quicksight:TagResource](#list_quicksight-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateFolderMembership  **
  - **IAM action:**  [quicksight:CreateFolderMembership](#list_quicksight-action-CreateFolderMembership)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [quicksight:UpdateAnalysisPermissions](#list_quicksight-action-UpdateAnalysisPermissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [quicksight:UpdateDashboardPermissions](#list_quicksight-action-UpdateDashboardPermissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [quicksight:UpdateDataSetPermissions](#list_quicksight-action-UpdateDataSetPermissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [quicksight:UpdateDataSourcePermissions](#list_quicksight-action-UpdateDataSourcePermissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [quicksight:UpdateTopicPermissions](#list_quicksight-action-UpdateTopicPermissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write

- **   CreateGroup  **
  - **IAM action:**  [quicksight:CreateGroup](#list_quicksight-action-CreateGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateGroupMembership  **
  - **IAM action:**  [quicksight:CreateGroupMembership](#list_quicksight-action-CreateGroupMembership) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateIAMPolicyAssignment  **
  - **IAM action:**  [quicksight:CreateIAMPolicyAssignment](#list_quicksight-action-CreateIAMPolicyAssignment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateIngestion  **
  - **IAM action:**  [quicksight:CreateIngestion](#list_quicksight-action-CreateIngestion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateKnowledgeBase  **
  - **IAM action:**  [quicksight:CreateKnowledgeBase](#list_quicksight-action-CreateKnowledgeBase)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [quicksight:PassDataSource](#list_quicksight-action-PassDataSource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [quicksight:TagResource](#list_quicksight-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateLimitsProfile  **
  - **IAM action:**  [quicksight:CreateLimitsProfile](#list_quicksight-action-CreateLimitsProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateNamespace  **
  - **IAM action:**  [quicksight:CreateNamespace](#list_quicksight-action-CreateNamespace)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [quicksight:TagResource](#list_quicksight-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateOAuthClientApplication  **
  - **IAM action:**  [quicksight:CreateDataSource](#list_quicksight-action-CreateDataSource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [quicksight:CreateOAuthClientApplication](#list_quicksight-action-CreateOAuthClientApplication)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [quicksight:TagResource](#list_quicksight-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateRefreshSchedule  **
  - **IAM action:**  [quicksight:CreateRefreshSchedule](#list_quicksight-action-CreateRefreshSchedule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateRoleMembership  **
  - **IAM action:**  [quicksight:CreateRoleMembership](#list_quicksight-action-CreateRoleMembership)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [quicksight:SetGroupMapping](#list_quicksight-action-SetGroupMapping)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateSpace  **
  - **IAM action:**  [quicksight:CreateSpace](#list_quicksight-action-CreateSpace)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [quicksight:TagResource](#list_quicksight-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateTemplate  **
  - **IAM action:**  [quicksight:CreateTemplate](#list_quicksight-action-CreateTemplate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [quicksight:DescribeAnalysis](#list_quicksight-action-DescribeAnalysis)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [quicksight:DescribeTemplate](#list_quicksight-action-DescribeTemplate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [quicksight:TagResource](#list_quicksight-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateTemplateAlias  **
  - **IAM action:**  [quicksight:CreateTemplateAlias](#list_quicksight-action-CreateTemplateAlias) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateTheme  **
  - **IAM action:**  [quicksight:CreateTheme](#list_quicksight-action-CreateTheme)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [quicksight:TagResource](#list_quicksight-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateThemeAlias  **
  - **IAM action:**  [quicksight:CreateThemeAlias](#list_quicksight-action-CreateThemeAlias) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateTopic  **
  - **IAM action:**  [quicksight:CreateFolderMembership](#list_quicksight-action-CreateFolderMembership)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [quicksight:CreateTopic](#list_quicksight-action-CreateTopic)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [quicksight:PassDataSet](#list_quicksight-action-PassDataSet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [quicksight:TagResource](#list_quicksight-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateTopicRefreshSchedule  **
  - **IAM action:**  [quicksight:CreateTopicRefreshSchedule](#list_quicksight-action-CreateTopicRefreshSchedule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateTopicV2  **
  - **IAM action:**  [quicksight:CreateFolderMembership](#list_quicksight-action-CreateFolderMembership)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [quicksight:CreateTopic](#list_quicksight-action-CreateTopic)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [quicksight:PassDataSet](#list_quicksight-action-PassDataSet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [quicksight:TagResource](#list_quicksight-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateVPCConnection  **
  - **IAM action:**  [quicksight:CreateVPCConnection](#list_quicksight-action-CreateVPCConnection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [quicksight:TagResource](#list_quicksight-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** quicksight.amazonaws.com / **Access level:** Write

- **   DeleteAccountCustomPermission  **
  - **IAM action:**  [quicksight:DeleteAccountCustomPermission](#list_quicksight-action-DeleteAccountCustomPermission) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAccountCustomization  **
  - **IAM action:**  [quicksight:DeleteAccountCustomization](#list_quicksight-action-DeleteAccountCustomization) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAccountSubscription  **
  - **IAM action:**  [quicksight:DeleteAccountSubscription](#list_quicksight-action-DeleteAccountSubscription)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [quicksight:Unsubscribe](#list_quicksight-action-Unsubscribe)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteActionConnector  **
  - **IAM action:**  [quicksight:DeleteActionConnector](#list_quicksight-action-DeleteActionConnector) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAgent  **
  - **IAM action:**  [quicksight:DeleteAgent](#list_quicksight-action-DeleteAgent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAnalysis  **
  - **IAM action:**  [quicksight:DeleteAnalysis](#list_quicksight-action-DeleteAnalysis) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteApp  **
  - **IAM action:**  [quicksight:DeleteApp](#list_quicksight-action-DeleteApp) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteApprovalPolicy  **
  - **IAM action:**  [quicksight:DeleteApprovalPolicy](#list_quicksight-action-DeleteApprovalPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteBrand  **
  - **IAM action:**  [quicksight:DeleteBrand](#list_quicksight-action-DeleteBrand) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteBrandAssignment  **
  - **IAM action:**  [quicksight:DeleteBrandAssignment](#list_quicksight-action-DeleteBrandAssignment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCustomPermissions  **
  - **IAM action:**  [quicksight:DeleteCustomPermissions](#list_quicksight-action-DeleteCustomPermissions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDashboard  **
  - **IAM action:**  [quicksight:DeleteDashboard](#list_quicksight-action-DeleteDashboard) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDataSet  **
  - **IAM action:**  [quicksight:DeleteDataSet](#list_quicksight-action-DeleteDataSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDataSetRefreshProperties  **
  - **IAM action:**  [quicksight:DeleteDataSetRefreshProperties](#list_quicksight-action-DeleteDataSetRefreshProperties) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDataSource  **
  - **IAM action:**  [quicksight:DeleteDataSource](#list_quicksight-action-DeleteDataSource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDefaultQBusinessApplication  **
  - **IAM action:**  [quicksight:DeleteDefaultQBusinessApplication](#list_quicksight-action-DeleteDefaultQBusinessApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDlpSetting  **
  - **IAM action:**  [quicksight:DeleteDlpSetting](#list_quicksight-action-DeleteDlpSetting) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteFlow  **
  - **IAM action:**  [quicksight:DeleteFlow](#list_quicksight-action-DeleteFlow) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteFolder  **
  - **IAM action:**  [quicksight:DeleteFolder](#list_quicksight-action-DeleteFolder) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteFolderMembership  **
  - **IAM action:**  [quicksight:DeleteFolderMembership](#list_quicksight-action-DeleteFolderMembership)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [quicksight:UpdateAnalysisPermissions](#list_quicksight-action-UpdateAnalysisPermissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [quicksight:UpdateDashboardPermissions](#list_quicksight-action-UpdateDashboardPermissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [quicksight:UpdateDataSetPermissions](#list_quicksight-action-UpdateDataSetPermissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [quicksight:UpdateDataSourcePermissions](#list_quicksight-action-UpdateDataSourcePermissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [quicksight:UpdateTopicPermissions](#list_quicksight-action-UpdateTopicPermissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write

- **   DeleteGroup  **
  - **IAM action:**  [quicksight:DeleteGroup](#list_quicksight-action-DeleteGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteGroupMembership  **
  - **IAM action:**  [quicksight:DeleteGroupMembership](#list_quicksight-action-DeleteGroupMembership) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteIAMPolicyAssignment  **
  - **IAM action:**  [quicksight:DeleteIAMPolicyAssignment](#list_quicksight-action-DeleteIAMPolicyAssignment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteIdentityPropagationConfig  **
  - **IAM action:**  [quicksight:DeleteIdentityPropagationConfig](#list_quicksight-action-DeleteIdentityPropagationConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteKnowledgeBase  **
  - **IAM action:**  [quicksight:DeleteKnowledgeBase](#list_quicksight-action-DeleteKnowledgeBase) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteLimitsProfile  **
  - **IAM action:**  [quicksight:DeleteLimitsProfile](#list_quicksight-action-DeleteLimitsProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteNamespace  **
  - **IAM action:**  [quicksight:DeleteNamespace](#list_quicksight-action-DeleteNamespace) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteOAuthClientApplication  **
  - **IAM action:**  [quicksight:DeleteDataSource](#list_quicksight-action-DeleteDataSource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [quicksight:DeleteOAuthClientApplication](#list_quicksight-action-DeleteOAuthClientApplication)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteRefreshSchedule  **
  - **IAM action:**  [quicksight:DeleteRefreshSchedule](#list_quicksight-action-DeleteRefreshSchedule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRoleCustomPermission  **
  - **IAM action:**  [quicksight:DeleteRoleCustomPermission](#list_quicksight-action-DeleteRoleCustomPermission) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRoleMembership  **
  - **IAM action:**  [quicksight:DeleteRoleMembership](#list_quicksight-action-DeleteRoleMembership)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [quicksight:SetGroupMapping](#list_quicksight-action-SetGroupMapping)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteSpace  **
  - **IAM action:**  [quicksight:DeleteSpace](#list_quicksight-action-DeleteSpace) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTemplate  **
  - **IAM action:**  [quicksight:DeleteTemplate](#list_quicksight-action-DeleteTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTemplateAlias  **
  - **IAM action:**  [quicksight:DeleteTemplateAlias](#list_quicksight-action-DeleteTemplateAlias) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTheme  **
  - **IAM action:**  [quicksight:DeleteTheme](#list_quicksight-action-DeleteTheme) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteThemeAlias  **
  - **IAM action:**  [quicksight:DeleteThemeAlias](#list_quicksight-action-DeleteThemeAlias) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTopic  **
  - **IAM action:**  [quicksight:DeleteTopic](#list_quicksight-action-DeleteTopic) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTopicRefreshSchedule  **
  - **IAM action:**  [quicksight:DeleteTopicRefreshSchedule](#list_quicksight-action-DeleteTopicRefreshSchedule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTopicV2  **
  - **IAM action:**  [quicksight:DeleteTopic](#list_quicksight-action-DeleteTopic) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteUser  **
  - **IAM action:**  [quicksight:DeleteUser](#list_quicksight-action-DeleteUser) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteUserByPrincipalId  **
  - **IAM action:**  [quicksight:DeleteUserByPrincipalId](#list_quicksight-action-DeleteUserByPrincipalId) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteUserCustomPermission  **
  - **IAM action:**  [quicksight:DeleteUserCustomPermission](#list_quicksight-action-DeleteUserCustomPermission)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [quicksight:UpdateUser](#list_quicksight-action-UpdateUser)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteVPCConnection  **
  - **IAM action:**  [quicksight:DeleteVPCConnection](#list_quicksight-action-DeleteVPCConnection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** quicksight.amazonaws.com / **Access level:** Write

- **   DescribeAccountCustomPermission  **
  - **IAM action:**  [quicksight:DescribeAccountCustomPermission](#list_quicksight-action-DescribeAccountCustomPermission) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAccountCustomization  **
  - **IAM action:**  [quicksight:DescribeAccountCustomization](#list_quicksight-action-DescribeAccountCustomization) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAccountSettings  **
  - **IAM action:**  [quicksight:DescribeAccountSettings](#list_quicksight-action-DescribeAccountSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAccountSubscription  **
  - **IAM action:**  [quicksight:DescribeAccountSubscription](#list_quicksight-action-DescribeAccountSubscription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeActionConnector  **
  - **IAM action:**  [quicksight:DescribeActionConnector](#list_quicksight-action-DescribeActionConnector) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeActionConnectorPermissions  **
  - **IAM action:**  [quicksight:DescribeActionConnectorPermissions](#list_quicksight-action-DescribeActionConnectorPermissions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAgent  **
  - **IAM action:**  [quicksight:DescribeAgent](#list_quicksight-action-DescribeAgent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAgentPermissions  **
  - **IAM action:**  [quicksight:DescribeAgentPermissions](#list_quicksight-action-DescribeAgentPermissions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAnalysis  **
  - **IAM action:**  [quicksight:DescribeAnalysis](#list_quicksight-action-DescribeAnalysis) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAnalysisDefinition  **
  - **IAM action:**  [quicksight:DescribeAnalysis](#list_quicksight-action-DescribeAnalysis) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAnalysisPermissions  **
  - **IAM action:**  [quicksight:DescribeAnalysisPermissions](#list_quicksight-action-DescribeAnalysisPermissions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeApp  **
  - **IAM action:**  [quicksight:DescribeApp](#list_quicksight-action-DescribeApp) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAppPermissions  **
  - **IAM action:**  [quicksight:DescribeAppPermissions](#list_quicksight-action-DescribeAppPermissions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeApprovalPolicy  **
  - **IAM action:**  [quicksight:DescribeApprovalPolicy](#list_quicksight-action-DescribeApprovalPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAssetBundleExportJob  **
  - **IAM action:**  [quicksight:DescribeAssetBundleExportJob](#list_quicksight-action-DescribeAssetBundleExportJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAssetBundleImportJob  **
  - **IAM action:**  [quicksight:DescribeAssetBundleImportJob](#list_quicksight-action-DescribeAssetBundleImportJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAutomationJob  **
  - **IAM action:**  [quicksight:DescribeAutomationJob](#list_quicksight-action-DescribeAutomationJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeBrand  **
  - **IAM action:**  [quicksight:DescribeBrand](#list_quicksight-action-DescribeBrand) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeBrandAssignment  **
  - **IAM action:**  [quicksight:DescribeBrandAssignment](#list_quicksight-action-DescribeBrandAssignment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeBrandPublishedVersion  **
  - **IAM action:**  [quicksight:DescribeBrandPublishedVersion](#list_quicksight-action-DescribeBrandPublishedVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeCustomPermissions  **
  - **IAM action:**  [quicksight:DescribeCustomPermissions](#list_quicksight-action-DescribeCustomPermissions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDashboard  **
  - **IAM action:**  [quicksight:DescribeDashboard](#list_quicksight-action-DescribeDashboard) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDashboardDefinition  **
  - **IAM action:**  [quicksight:DescribeDashboard](#list_quicksight-action-DescribeDashboard) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDashboardPermissions  **
  - **IAM action:**  [quicksight:DescribeDashboardPermissions](#list_quicksight-action-DescribeDashboardPermissions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDashboardSnapshotJob  **
  - **IAM action:**  [quicksight:DescribeDashboardSnapshotJob](#list_quicksight-action-DescribeDashboardSnapshotJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDashboardSnapshotJobResult  **
  - **IAM action:**  [quicksight:DescribeDashboardSnapshotJobResult](#list_quicksight-action-DescribeDashboardSnapshotJobResult) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDashboardsQAConfiguration  **
  - **IAM action:**  [quicksight:DescribeDashboardsQAConfiguration](#list_quicksight-action-DescribeDashboardsQAConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDataSet  **
  - **IAM action:**  [quicksight:DescribeDataSet](#list_quicksight-action-DescribeDataSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDataSetPermissions  **
  - **IAM action:**  [quicksight:DescribeDataSetPermissions](#list_quicksight-action-DescribeDataSetPermissions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDataSetRefreshProperties  **
  - **IAM action:**  [quicksight:DescribeDataSetRefreshProperties](#list_quicksight-action-DescribeDataSetRefreshProperties) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDataSource  **
  - **IAM action:**  [quicksight:DescribeDataSource](#list_quicksight-action-DescribeDataSource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDataSourcePermissions  **
  - **IAM action:**  [quicksight:DescribeDataSourcePermissions](#list_quicksight-action-DescribeDataSourcePermissions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDefaultQBusinessApplication  **
  - **IAM action:**  [quicksight:DescribeDefaultQBusinessApplication](#list_quicksight-action-DescribeDefaultQBusinessApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDlpSetting  **
  - **IAM action:**  [quicksight:DescribeDlpSetting](#list_quicksight-action-DescribeDlpSetting) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeFlow  **
  - **IAM action:**  [quicksight:DescribeFlow](#list_quicksight-action-DescribeFlow) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeFolder  **
  - **IAM action:**  [quicksight:DescribeFolder](#list_quicksight-action-DescribeFolder) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeFolderPermissions  **
  - **IAM action:**  [quicksight:DescribeFolderPermissions](#list_quicksight-action-DescribeFolderPermissions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeFolderResolvedPermissions  **
  - **IAM action:**  [quicksight:DescribeFolderResolvedPermissions](#list_quicksight-action-DescribeFolderResolvedPermissions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeGroup  **
  - **IAM action:**  [quicksight:DescribeGroup](#list_quicksight-action-DescribeGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeGroupMembership  **
  - **IAM action:**  [quicksight:DescribeGroupMembership](#list_quicksight-action-DescribeGroupMembership) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeIAMPolicyAssignment  **
  - **IAM action:**  [quicksight:DescribeIAMPolicyAssignment](#list_quicksight-action-DescribeIAMPolicyAssignment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeIngestion  **
  - **IAM action:**  [quicksight:DescribeIngestion](#list_quicksight-action-DescribeIngestion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeIpRestriction  **
  - **IAM action:**  [quicksight:DescribeIpRestriction](#list_quicksight-action-DescribeIpRestriction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeKeyRegistration  **
  - **IAM action:**  [quicksight:DescribeKeyRegistration](#list_quicksight-action-DescribeKeyRegistration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [quicksight:ListCustomerManagedKeys](#list_quicksight-action-ListCustomerManagedKeys)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   DescribeKnowledgeBase  **
  - **IAM action:**  [quicksight:DescribeKnowledgeBase](#list_quicksight-action-DescribeKnowledgeBase) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeKnowledgeBasePermissions  **
  - **IAM action:**  [quicksight:DescribeKnowledgeBasePermissions](#list_quicksight-action-DescribeKnowledgeBasePermissions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DescribeLimitsProfile  **
  - **IAM action:**  [quicksight:DescribeLimitsProfile](#list_quicksight-action-DescribeLimitsProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeNamespace  **
  - **IAM action:**  [quicksight:DescribeNamespace](#list_quicksight-action-DescribeNamespace) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeOAuthClientApplication  **
  - **IAM action:**  [quicksight:DescribeDataSource](#list_quicksight-action-DescribeDataSource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [quicksight:DescribeOAuthClientApplication](#list_quicksight-action-DescribeOAuthClientApplication)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   DescribeQPersonalizationConfiguration  **
  - **IAM action:**  [quicksight:DescribeQPersonalizationConfiguration](#list_quicksight-action-DescribeQPersonalizationConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeQuickSightQSearchConfiguration  **
  - **IAM action:**  [quicksight:DescribeQuickSightQSearchConfiguration](#list_quicksight-action-DescribeQuickSightQSearchConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeRefreshSchedule  **
  - **IAM action:**  [quicksight:DescribeRefreshSchedule](#list_quicksight-action-DescribeRefreshSchedule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeRoleCustomPermission  **
  - **IAM action:**  [quicksight:DescribeRoleCustomPermission](#list_quicksight-action-DescribeRoleCustomPermission) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeSelfUpgradeConfiguration  **
  - **IAM action:**  [quicksight:DescribeSelfUpgradeConfiguration](#list_quicksight-action-DescribeSelfUpgradeConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeSpace  **
  - **IAM action:**  [quicksight:DescribeSpace](#list_quicksight-action-DescribeSpace) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeSpacePermissions  **
  - **IAM action:**  [quicksight:DescribeSpacePermissions](#list_quicksight-action-DescribeSpacePermissions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DescribeTemplate  **
  - **IAM action:**  [quicksight:DescribeTemplate](#list_quicksight-action-DescribeTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeTemplateAlias  **
  - **IAM action:**  [quicksight:DescribeTemplateAlias](#list_quicksight-action-DescribeTemplateAlias) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeTemplateDefinition  **
  - **IAM action:**  [quicksight:DescribeTemplate](#list_quicksight-action-DescribeTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeTemplatePermissions  **
  - **IAM action:**  [quicksight:DescribeTemplatePermissions](#list_quicksight-action-DescribeTemplatePermissions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeTheme  **
  - **IAM action:**  [quicksight:DescribeTheme](#list_quicksight-action-DescribeTheme) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeThemeAlias  **
  - **IAM action:**  [quicksight:DescribeThemeAlias](#list_quicksight-action-DescribeThemeAlias) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeThemePermissions  **
  - **IAM action:**  [quicksight:DescribeThemePermissions](#list_quicksight-action-DescribeThemePermissions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeTopic  **
  - **IAM action:**  [quicksight:DescribeTopic](#list_quicksight-action-DescribeTopic) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeTopicPermissions  **
  - **IAM action:**  [quicksight:DescribeTopicPermissions](#list_quicksight-action-DescribeTopicPermissions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DescribeTopicPermissionsV2  **
  - **IAM action:**  [quicksight:DescribeTopicPermissions](#list_quicksight-action-DescribeTopicPermissions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DescribeTopicRefresh  **
  - **IAM action:**  [quicksight:DescribeTopicRefresh](#list_quicksight-action-DescribeTopicRefresh) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeTopicRefreshSchedule  **
  - **IAM action:**  [quicksight:DescribeTopicRefreshSchedule](#list_quicksight-action-DescribeTopicRefreshSchedule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeTopicV2  **
  - **IAM action:**  [quicksight:DescribeTopic](#list_quicksight-action-DescribeTopic) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeUser  **
  - **IAM action:**  [quicksight:DescribeUser](#list_quicksight-action-DescribeUser) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeVPCConnection  **
  - **IAM action:**  [quicksight:DescribeVPCConnection](#list_quicksight-action-DescribeVPCConnection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GenerateEmbedUrlForAnonymousUser  **
  - **IAM action:**  [quicksight:GenerateEmbedUrlForAnonymousUser](#list_quicksight-action-GenerateEmbedUrlForAnonymousUser) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GenerateEmbedUrlForRegisteredUser  **
  - **IAM action:**  [quicksight:GenerateEmbedUrlForRegisteredUser](#list_quicksight-action-GenerateEmbedUrlForRegisteredUser) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GenerateEmbedUrlForRegisteredUserWithIdentity  **
  - **IAM action:**  [quicksight:GenerateEmbedUrlForRegisteredUserWithIdentity](#list_quicksight-action-GenerateEmbedUrlForRegisteredUserWithIdentity) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetDashboardEmbedUrl  **
  - **IAM action:**  [quicksight:GetAnonymousUserEmbedUrl](#list_quicksight-action-GetAnonymousUserEmbedUrl)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [quicksight:GetAuthCode](#list_quicksight-action-GetAuthCode)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [quicksight:GetDashboardEmbedUrl](#list_quicksight-action-GetDashboardEmbedUrl)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetFlowMetadata  **
  - **IAM action:**  [quicksight:GetFlowMetadata](#list_quicksight-action-GetFlowMetadata) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetFlowPermissions  **
  - **IAM action:**  [quicksight:GetFlowPermissions](#list_quicksight-action-GetFlowPermissions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetIdentityContext  **
  - **IAM action:**  [quicksight:GetIdentityContext](#list_quicksight-action-GetIdentityContext) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSessionEmbedUrl  **
  - **IAM action:**  [quicksight:GetAuthCode](#list_quicksight-action-GetAuthCode)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [quicksight:GetSessionEmbedUrl](#list_quicksight-action-GetSessionEmbedUrl)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   ListActionConnectors  **
  - **IAM action:**  [quicksight:ListActionConnectors](#list_quicksight-action-ListActionConnectors) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAgents  **
  - **IAM action:**  [quicksight:ListAgents](#list_quicksight-action-ListAgents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAnalyses  **
  - **IAM action:**  [quicksight:ListAnalyses](#list_quicksight-action-ListAnalyses) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListApprovalPolicies  **
  - **IAM action:**  [quicksight:ListApprovalPolicies](#list_quicksight-action-ListApprovalPolicies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListApps  **
  - **IAM action:**  [quicksight:ListApps](#list_quicksight-action-ListApps) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAssetBundleExportJobs  **
  - **IAM action:**  [quicksight:ListAssetBundleExportJobs](#list_quicksight-action-ListAssetBundleExportJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAssetBundleImportJobs  **
  - **IAM action:**  [quicksight:ListAssetBundleImportJobs](#list_quicksight-action-ListAssetBundleImportJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListBrands  **
  - **IAM action:**  [quicksight:ListBrands](#list_quicksight-action-ListBrands) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCustomPermissions  **
  - **IAM action:**  [quicksight:ListCustomPermissions](#list_quicksight-action-ListCustomPermissions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDashboardVersions  **
  - **IAM action:**  [quicksight:ListDashboardVersions](#list_quicksight-action-ListDashboardVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDashboards  **
  - **IAM action:**  [quicksight:ListDashboards](#list_quicksight-action-ListDashboards) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDataSets  **
  - **IAM action:**  [quicksight:ListDataSets](#list_quicksight-action-ListDataSets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDataSources  **
  - **IAM action:**  [quicksight:ListDataSources](#list_quicksight-action-ListDataSources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDlpSettings  **
  - **IAM action:**  [quicksight:ListDlpSettings](#list_quicksight-action-ListDlpSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFlows  **
  - **IAM action:**  [quicksight:ListFlows](#list_quicksight-action-ListFlows) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFolderMembers  **
  - **IAM action:**  [quicksight:ListFolderMembers](#list_quicksight-action-ListFolderMembers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListFolders  **
  - **IAM action:**  [quicksight:ListFolders](#list_quicksight-action-ListFolders) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFoldersForResource  **
  - **IAM action:**  [quicksight:ListFoldersForResource](#list_quicksight-action-ListFoldersForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListGroupMemberships  **
  - **IAM action:**  [quicksight:ListGroupMemberships](#list_quicksight-action-ListGroupMemberships) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListGroups  **
  - **IAM action:**  [quicksight:ListGroups](#list_quicksight-action-ListGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListIAMPolicyAssignments  **
  - **IAM action:**  [quicksight:ListIAMPolicyAssignments](#list_quicksight-action-ListIAMPolicyAssignments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListIAMPolicyAssignmentsForUser  **
  - **IAM action:**  [quicksight:ListIAMPolicyAssignmentsForUser](#list_quicksight-action-ListIAMPolicyAssignmentsForUser) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListIdentityPropagationConfigs  **
  - **IAM action:**  [quicksight:ListIdentityPropagationConfigs](#list_quicksight-action-ListIdentityPropagationConfigs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListIngestions  **
  - **IAM action:**  [quicksight:ListIngestions](#list_quicksight-action-ListIngestions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListKnowledgeBases  **
  - **IAM action:**  [quicksight:ListKnowledgeBases](#list_quicksight-action-ListKnowledgeBases) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListLimitsProfiles  **
  - **IAM action:**  [quicksight:ListLimitsProfiles](#list_quicksight-action-ListLimitsProfiles) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListNamespaces  **
  - **IAM action:**  [quicksight:ListNamespaces](#list_quicksight-action-ListNamespaces) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListOAuthClientApplications  **
  - **IAM action:**  [quicksight:ListDataSources](#list_quicksight-action-ListDataSources)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [quicksight:ListOAuthClientApplications](#list_quicksight-action-ListOAuthClientApplications)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ListRefreshSchedules  **
  - **IAM action:**  [quicksight:ListRefreshSchedules](#list_quicksight-action-ListRefreshSchedules) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRoleMemberships  **
  - **IAM action:**  [quicksight:GetGroupMapping](#list_quicksight-action-GetGroupMapping)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [quicksight:ListRoleMemberships](#list_quicksight-action-ListRoleMemberships)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ListSelfUpgrades  **
  - **IAM action:**  [quicksight:ListSelfUpgrades](#list_quicksight-action-ListSelfUpgrades) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSpaceResources  **
  - **IAM action:**  [quicksight:ListSpaceResources](#list_quicksight-action-ListSpaceResources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSpaces  **
  - **IAM action:**  [quicksight:ListSpaces](#list_quicksight-action-ListSpaces) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [quicksight:ListTagsForResource](#list_quicksight-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTemplateAliases  **
  - **IAM action:**  [quicksight:ListTemplateAliases](#list_quicksight-action-ListTemplateAliases) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTemplateVersions  **
  - **IAM action:**  [quicksight:ListTemplateVersions](#list_quicksight-action-ListTemplateVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTemplates  **
  - **IAM action:**  [quicksight:ListTemplates](#list_quicksight-action-ListTemplates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListThemeAliases  **
  - **IAM action:**  [quicksight:ListThemeAliases](#list_quicksight-action-ListThemeAliases) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListThemeVersions  **
  - **IAM action:**  [quicksight:ListThemeVersions](#list_quicksight-action-ListThemeVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListThemes  **
  - **IAM action:**  [quicksight:ListThemes](#list_quicksight-action-ListThemes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTopicRefreshSchedules  **
  - **IAM action:**  [quicksight:ListTopicRefreshSchedules](#list_quicksight-action-ListTopicRefreshSchedules) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTopicReviewedAnswers  **
  - **IAM action:**  [quicksight:ListTopicReviewedAnswers](#list_quicksight-action-ListTopicReviewedAnswers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTopics  **
  - **IAM action:**  [quicksight:ListTopics](#list_quicksight-action-ListTopics) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTopicsV2  **
  - **IAM action:**  [quicksight:ListTopics](#list_quicksight-action-ListTopics) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListUserGroups  **
  - **IAM action:**  [quicksight:ListUserGroups](#list_quicksight-action-ListUserGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListUsers  **
  - **IAM action:**  [quicksight:ListUsers](#list_quicksight-action-ListUsers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListUsersIndexCapacity  **
  - **IAM action:**  [quicksight:ListUsersIndexCapacity](#list_quicksight-action-ListUsersIndexCapacity) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListVPCConnections  **
  - **IAM action:**  [quicksight:ListVPCConnections](#list_quicksight-action-ListVPCConnections) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PredictQAResults  **
  - **IAM action:**  [quicksight:PredictQAResults](#list_quicksight-action-PredictQAResults) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PutDataSetRefreshProperties  **
  - **IAM action:**  [quicksight:PutDataSetRefreshProperties](#list_quicksight-action-PutDataSetRefreshProperties) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RegisterUser  **
  - **IAM action:**  [quicksight:RegisterUser](#list_quicksight-action-RegisterUser)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [quicksight:TagResource](#list_quicksight-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   RestoreAnalysis  **
  - **IAM action:**  [quicksight:CreateFolderMembership](#list_quicksight-action-CreateFolderMembership)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [quicksight:ListFoldersForResource](#list_quicksight-action-ListFoldersForResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [quicksight:RestoreAnalysis](#list_quicksight-action-RestoreAnalysis)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   SearchActionConnectors  **
  - **IAM action:**  [quicksight:SearchActionConnectors](#list_quicksight-action-SearchActionConnectors) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   SearchAgents  **
  - **IAM action:**  [quicksight:SearchAgents](#list_quicksight-action-SearchAgents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   SearchAnalyses  **
  - **IAM action:**  [quicksight:SearchAnalyses](#list_quicksight-action-SearchAnalyses) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   SearchApps  **
  - **IAM action:**  [quicksight:SearchApps](#list_quicksight-action-SearchApps) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   SearchDashboards  **
  - **IAM action:**  [quicksight:SearchDashboards](#list_quicksight-action-SearchDashboards) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   SearchDataSets  **
  - **IAM action:**  [quicksight:SearchDataSets](#list_quicksight-action-SearchDataSets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   SearchDataSources  **
  - **IAM action:**  [quicksight:SearchDataSources](#list_quicksight-action-SearchDataSources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   SearchFlows  **
  - **IAM action:**  [quicksight:SearchFlows](#list_quicksight-action-SearchFlows) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   SearchFolders  **
  - **IAM action:**  [quicksight:SearchFolders](#list_quicksight-action-SearchFolders) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   SearchGroups  **
  - **IAM action:**  [quicksight:SearchGroups](#list_quicksight-action-SearchGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   SearchKnowledgeBases  **
  - **IAM action:**  [quicksight:SearchKnowledgeBases](#list_quicksight-action-SearchKnowledgeBases) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   SearchSpaces  **
  - **IAM action:**  [quicksight:SearchSpaces](#list_quicksight-action-SearchSpaces) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   SearchTopics  **
  - **IAM action:**  [quicksight:SearchTopics](#list_quicksight-action-SearchTopics) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   SearchTopicsV2  **
  - **IAM action:**  [quicksight:SearchTopics](#list_quicksight-action-SearchTopics) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   StartAssetBundleExportJob  **
  - **IAM action:**  [quicksight:StartAssetBundleExportJob](#list_quicksight-action-StartAssetBundleExportJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartAssetBundleImportJob  **
  - **IAM action:**  [quicksight:StartAssetBundleImportJob](#list_quicksight-action-StartAssetBundleImportJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartAutomationJob  **
  - **IAM action:**  [quicksight:StartAutomationJob](#list_quicksight-action-StartAutomationJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartDashboardSnapshotJob  **
  - **IAM action:**  [quicksight:StartDashboardSnapshotJob](#list_quicksight-action-StartDashboardSnapshotJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartDashboardSnapshotJobSchedule  **
  - **IAM action:**  [quicksight:StartDashboardSnapshotJobSchedule](#list_quicksight-action-StartDashboardSnapshotJobSchedule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [quicksight:TagResource](#list_quicksight-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [quicksight:UntagResource](#list_quicksight-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateAccountCustomPermission  **
  - **IAM action:**  [quicksight:UpdateAccountCustomPermission](#list_quicksight-action-UpdateAccountCustomPermission) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateAccountCustomization  **
  - **IAM action:**  [quicksight:UpdateAccountCustomization](#list_quicksight-action-UpdateAccountCustomization) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateAccountSettings  **
  - **IAM action:**  [quicksight:UpdateAccountSettings](#list_quicksight-action-UpdateAccountSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateActionConnector  **
  - **IAM action:**  [quicksight:UpdateActionConnector](#list_quicksight-action-UpdateActionConnector)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** quicksight.amazonaws.com / **Access level:** Write

- **   UpdateActionConnectorPermissions  **
  - **IAM action:**  [quicksight:UpdateActionConnectorPermissions](#list_quicksight-action-UpdateActionConnectorPermissions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   UpdateAgent  **
  - **IAM action:**  [quicksight:UpdateAgent](#list_quicksight-action-UpdateAgent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateAgentPermissions  **
  - **IAM action:**  [quicksight:UpdateAgentPermissions](#list_quicksight-action-UpdateAgentPermissions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   UpdateAnalysis  **
  - **IAM action:**  [quicksight:DescribeTemplate](#list_quicksight-action-DescribeTemplate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [quicksight:DescribeTheme](#list_quicksight-action-DescribeTheme)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [quicksight:PassDataSet](#list_quicksight-action-PassDataSet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [quicksight:PassTopic](#list_quicksight-action-PassTopic)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [quicksight:UpdateAnalysis](#list_quicksight-action-UpdateAnalysis)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UpdateAnalysisPermissions  **
  - **IAM action:**  [quicksight:UpdateAnalysisPermissions](#list_quicksight-action-UpdateAnalysisPermissions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   UpdateAppPermissions  **
  - **IAM action:**  [quicksight:UpdateAppPermissions](#list_quicksight-action-UpdateAppPermissions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   UpdateApplicationWithTokenExchangeGrant  **
  - **IAM action:**  [quicksight:UpdateApplicationWithTokenExchangeGrant](#list_quicksight-action-UpdateApplicationWithTokenExchangeGrant) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateApprovalPolicy  **
  - **IAM action:**  [quicksight:UpdateApprovalPolicy](#list_quicksight-action-UpdateApprovalPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateBrand  **
  - **IAM action:**  [quicksight:UpdateBrand](#list_quicksight-action-UpdateBrand) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateBrandAssignment  **
  - **IAM action:**  [quicksight:UpdateBrandAssignment](#list_quicksight-action-UpdateBrandAssignment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateBrandPublishedVersion  **
  - **IAM action:**  [quicksight:UpdateBrandPublishedVersion](#list_quicksight-action-UpdateBrandPublishedVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateCustomPermissions  **
  - **IAM action:**  [quicksight:UpdateCustomPermissions](#list_quicksight-action-UpdateCustomPermissions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDashboard  **
  - **IAM action:**  [quicksight:DescribeTemplate](#list_quicksight-action-DescribeTemplate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [quicksight:DescribeTheme](#list_quicksight-action-DescribeTheme)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [quicksight:PassDataSet](#list_quicksight-action-PassDataSet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [quicksight:UpdateDashboard](#list_quicksight-action-UpdateDashboard)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UpdateDashboardLinks  **
  - **IAM action:**  [quicksight:UpdateDashboardLinks](#list_quicksight-action-UpdateDashboardLinks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDashboardPermissions  **
  - **IAM action:**  [quicksight:UpdateDashboardPermissions](#list_quicksight-action-UpdateDashboardPermissions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   UpdateDashboardPublishedVersion  **
  - **IAM action:**  [quicksight:UpdateDashboardPublishedVersion](#list_quicksight-action-UpdateDashboardPublishedVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDashboardsQAConfiguration  **
  - **IAM action:**  [quicksight:UpdateDashboardsQAConfiguration](#list_quicksight-action-UpdateDashboardsQAConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDataSet  **
  - **IAM action:**  [quicksight:PassDataSet](#list_quicksight-action-PassDataSet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [quicksight:PassDataSource](#list_quicksight-action-PassDataSource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [quicksight:UpdateDataSet](#list_quicksight-action-UpdateDataSet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UpdateDataSetPermissions  **
  - **IAM action:**  [quicksight:UpdateDataSetPermissions](#list_quicksight-action-UpdateDataSetPermissions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   UpdateDataSource  **
  - **IAM action:**  [quicksight:UpdateDataSource](#list_quicksight-action-UpdateDataSource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** quicksight.amazonaws.com / **Access level:** Write

- **   UpdateDataSourcePermissions  **
  - **IAM action:**  [quicksight:UpdateDataSourcePermissions](#list_quicksight-action-UpdateDataSourcePermissions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   UpdateDefaultQBusinessApplication  **
  - **IAM action:**  [quicksight:UpdateDefaultQBusinessApplication](#list_quicksight-action-UpdateDefaultQBusinessApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDlpSetting  **
  - **IAM action:**  [quicksight:UpdateDlpSetting](#list_quicksight-action-UpdateDlpSetting) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateFlow  **
  - **IAM action:**  [quicksight:UpdateFlow](#list_quicksight-action-UpdateFlow) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateFlowPermissions  **
  - **IAM action:**  [quicksight:UpdateFlowPermissions](#list_quicksight-action-UpdateFlowPermissions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   UpdateFolder  **
  - **IAM action:**  [quicksight:UpdateFolder](#list_quicksight-action-UpdateFolder) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateFolderPermissions  **
  - **IAM action:**  [quicksight:UpdateFolderPermissions](#list_quicksight-action-UpdateFolderPermissions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   UpdateGroup  **
  - **IAM action:**  [quicksight:UpdateGroup](#list_quicksight-action-UpdateGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateIAMPolicyAssignment  **
  - **IAM action:**  [quicksight:UpdateIAMPolicyAssignment](#list_quicksight-action-UpdateIAMPolicyAssignment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateIdentityPropagationConfig  **
  - **IAM action:**  [quicksight:UpdateIdentityPropagationConfig](#list_quicksight-action-UpdateIdentityPropagationConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateIpRestriction  **
  - **IAM action:**  [quicksight:UpdateIpRestriction](#list_quicksight-action-UpdateIpRestriction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateKeyRegistration  **
  - **IAM action:**  [quicksight:RegisterCustomerManagedKey](#list_quicksight-action-RegisterCustomerManagedKey)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [quicksight:RemoveCustomerManagedKey](#list_quicksight-action-RemoveCustomerManagedKey)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [quicksight:UpdateKeyRegistration](#list_quicksight-action-UpdateKeyRegistration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UpdateKnowledgeBase  **
  - **IAM action:**  [quicksight:UpdateKnowledgeBase](#list_quicksight-action-UpdateKnowledgeBase) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateKnowledgeBasePermissions  **
  - **IAM action:**  [quicksight:UpdateKnowledgeBasePermissions](#list_quicksight-action-UpdateKnowledgeBasePermissions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   UpdateLimitsProfile  **
  - **IAM action:**  [quicksight:UpdateLimitsProfile](#list_quicksight-action-UpdateLimitsProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateOAuthClientApplication  **
  - **IAM action:**  [quicksight:UpdateDataSource](#list_quicksight-action-UpdateDataSource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [quicksight:UpdateOAuthClientApplication](#list_quicksight-action-UpdateOAuthClientApplication)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UpdatePublicSharingSettings  **
  - **IAM action:**  [quicksight:UpdatePublicSharingSettings](#list_quicksight-action-UpdatePublicSharingSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateQPersonalizationConfiguration  **
  - **IAM action:**  [quicksight:UpdateQPersonalizationConfiguration](#list_quicksight-action-UpdateQPersonalizationConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateQuickSightQSearchConfiguration  **
  - **IAM action:**  [quicksight:UpdateQuickSightQSearchConfiguration](#list_quicksight-action-UpdateQuickSightQSearchConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRefreshSchedule  **
  - **IAM action:**  [quicksight:UpdateRefreshSchedule](#list_quicksight-action-UpdateRefreshSchedule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRoleCustomPermission  **
  - **IAM action:**  [quicksight:UpdateRoleCustomPermission](#list_quicksight-action-UpdateRoleCustomPermission) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSPICECapacityConfiguration  **
  - **IAM action:**  [quicksight:UpdateSPICECapacityConfiguration](#list_quicksight-action-UpdateSPICECapacityConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSelfUpgrade  **
  - **IAM action:**  [quicksight:UpdateSelfUpgrade](#list_quicksight-action-UpdateSelfUpgrade) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSelfUpgradeConfiguration  **
  - **IAM action:**  [quicksight:UpdateSelfUpgradeConfiguration](#list_quicksight-action-UpdateSelfUpgradeConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSpace  **
  - **IAM action:**  [quicksight:UpdateSpace](#list_quicksight-action-UpdateSpace) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSpacePermissions  **
  - **IAM action:**  [quicksight:UpdateSpacePermissions](#list_quicksight-action-UpdateSpacePermissions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   UpdateSpaceResources  **
  - **IAM action:**  [quicksight:UpdateSpaceResources](#list_quicksight-action-UpdateSpaceResources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateTemplate  **
  - **IAM action:**  [quicksight:DescribeAnalysis](#list_quicksight-action-DescribeAnalysis)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [quicksight:DescribeTemplate](#list_quicksight-action-DescribeTemplate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [quicksight:UpdateTemplate](#list_quicksight-action-UpdateTemplate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UpdateTemplateAlias  **
  - **IAM action:**  [quicksight:UpdateTemplateAlias](#list_quicksight-action-UpdateTemplateAlias) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateTemplatePermissions  **
  - **IAM action:**  [quicksight:UpdateTemplatePermissions](#list_quicksight-action-UpdateTemplatePermissions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   UpdateTheme  **
  - **IAM action:**  [quicksight:UpdateTheme](#list_quicksight-action-UpdateTheme) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateThemeAlias  **
  - **IAM action:**  [quicksight:UpdateThemeAlias](#list_quicksight-action-UpdateThemeAlias) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateThemePermissions  **
  - **IAM action:**  [quicksight:UpdateThemePermissions](#list_quicksight-action-UpdateThemePermissions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   UpdateTopic  **
  - **IAM action:**  [quicksight:PassDataSet](#list_quicksight-action-PassDataSet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [quicksight:UpdateTopic](#list_quicksight-action-UpdateTopic)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UpdateTopicPermissions  **
  - **IAM action:**  [quicksight:UpdateTopicPermissions](#list_quicksight-action-UpdateTopicPermissions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   UpdateTopicPermissionsV2  **
  - **IAM action:**  [quicksight:UpdateTopicPermissions](#list_quicksight-action-UpdateTopicPermissions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   UpdateTopicRefreshSchedule  **
  - **IAM action:**  [quicksight:UpdateTopicRefreshSchedule](#list_quicksight-action-UpdateTopicRefreshSchedule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateTopicV2  **
  - **IAM action:**  [quicksight:PassDataSet](#list_quicksight-action-PassDataSet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [quicksight:UpdateTopic](#list_quicksight-action-UpdateTopic)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UpdateUser  **
  - **IAM action:**  [quicksight:UpdateUser](#list_quicksight-action-UpdateUser) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateUserCustomPermission  **
  - **IAM action:**  [quicksight:UpdateUser](#list_quicksight-action-UpdateUser)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [quicksight:UpdateUserCustomPermission](#list_quicksight-action-UpdateUserCustomPermission)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UpdateVPCConnection  **
  - **IAM action:**  [quicksight:UpdateVPCConnection](#list_quicksight-action-UpdateVPCConnection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** quicksight.amazonaws.com / **Access level:** Write



## Actions defined by Amazon QuickSight
<a name="list_quicksight-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [BatchCreateTopicReviewedAnswer](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_BatchCreateTopicReviewedAnswer.html)  **
  - **Description:** Grants permission to create reviewed answers for a topic
  - **Resource types (\*required):** [topic\*](#list_quicksight-resource-topic)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Access level:** Write

- **   [BatchDeleteKnowledgeBase](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_BatchDeleteKnowledgeBase.html)  **
  - **Description:** Grants permission to delete one or more knowledge bases
  - **Resource types (\*required):** [knowledgeBase\*](#list_quicksight-resource-knowledgeBase)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchDeleteTopicReviewedAnswer](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_BatchDeleteTopicReviewedAnswer.html)  **
  - **Description:** Grants permission to delete reviewed answers for a topic
  - **Resource types (\*required):** [topic\*](#list_quicksight-resource-topic)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Access level:** Write

- **   [BatchDescribeUserLimits](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_BatchDescribeUserLimits.html)  **
  - **Description:** Grants permission to describe the effective resource limits for users
  - **Resource types (\*required):** [limitsProfile\*](#list_quicksight-resource-limitsProfile)
  - **Condition keys:**  
  - **Access level:** Read

- **   [CancelIngestion](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CancelIngestion.html)  **
  - **Description:** Grants permission to cancel a SPICE ingestions on a dataset
  - **Resource types (\*required):** [ingestion\*](#list_quicksight-resource-ingestion)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Access level:** Write

- **   [CreateAccountCustomization](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateAccountCustomization.html)  **
  - **Description:** Grants permission to create an account customization for QuickSight account or namespace
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Access level:** Write

- **   [CreateAccountSubscription](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateAccountSubscription.html)  **
  - **Description:** Grants permission to subscribe to QuickSight
  - **Resource types (\*required):** 
  - **Condition keys:** [quicksight:DirectoryType](#list_quicksight-quicksight_DirectoryType)<br />[quicksight:Edition](#list_quicksight-quicksight_Edition)
  - **Access level:** Write

- **   [CreateActionConnector](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateActionConnector.html)  **
  - **Description:** Grants permission to create an action connector
  - **Resource types (\*required):** [actionconnector\*](#list_quicksight-resource-actionconnector)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Access level:** Write

- **   [CreateAgent](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateAgent.html)  **
  - **Description:** Grants permission to create an agent
  - **Resource types (\*required):** [agent\*](#list_quicksight-resource-agent)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateAnalysis](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateAnalysis.html)  **
  - **Description:** Grants permission to create an analysis from a template
  - **Resource types (\*required):** [analysis\*](#list_quicksight-resource-analysis)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Access level:** Write

- **   [CreateApprovalPolicy](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateApprovalPolicy.html)  **
  - **Description:** Grants permission to create an approval policy for governed actions
  - **Resource types (\*required):** [approvalPolicy\*](#list_quicksight-resource-approvalPolicy)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateBrand](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateBrand.html)  **
  - **Description:** Grants permission to create an Amazon QuickSight brand
  - **Resource types (\*required):** [brand\*](#list_quicksight-resource-brand)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Access level:** Write

- **   [CreateCustomPermissions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateCustomPermissions.html)  **
  - **Description:** Grants permission to create a QuickSight custom permissions resource
  - **Resource types (\*required):** [custompermissions\*](#list_quicksight-resource-custompermissions)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDashboard](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateDashboard.html)  **
  - **Description:** Grants permission to create a QuickSight Dashboard
  - **Resource types (\*required):** [dashboard\*](#list_quicksight-resource-dashboard)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDataSet](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateDataSet.html)  **
  - **Description:** Grants permission to create a dataset
  - **Resource types (\*required):** [datasource\*](#list_quicksight-resource-datasource)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDataSource](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateDataSource.html)  **
  - **Description:** Grants permission to create a data source
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDlpSetting](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateDlpSetting.html)  **
  - **Description:** Grants permission to create a DLP setting
  - **Resource types (\*required):** [dlpSetting\*](#list_quicksight-resource-dlpSetting)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Access level:** Write

- **   [CreateFlow](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateFlow.html)  **
  - **Description:** Grants permission to create a flow
  - **Resource types (\*required):** [flow\*](#list_quicksight-resource-flow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateFolder](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateFolder.html)  **
  - **Description:** Grants permission to create a QuickSight folder
  - **Resource types (\*required):** [folder\*](#list_quicksight-resource-folder)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Access level:** Write

- **   [CreateFolderMembership](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateFolderMembership.html)  **
  - **Description:** Grants permission to add a QuickSight Dashboard, Analysis or Dataset to a QuickSight Folder
  - **Resource types (\*required):** [analysis](#list_quicksight-resource-analysis) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [dashboard](#list_quicksight-resource-dashboard) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [dataset](#list_quicksight-resource-dataset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [folder\*](#list_quicksight-resource-folder) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateGroup](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateGroup.html)  **
  - **Description:** Grants permission to create a QuickSight group
  - **Resource types (\*required):** [group\*](#list_quicksight-resource-group)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateGroupMembership](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateGroupMembership.html)  **
  - **Description:** Grants permission to add a QuickSight user to a QuickSight group
  - **Resource types (\*required):** [group\*](#list_quicksight-resource-group)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)<br />[quicksight:UserName](#list_quicksight-quicksight_UserName)
  - **Access level:** Write

- **   [CreateIAMPolicyAssignment](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateIAMPolicyAssignment.html)  **
  - **Description:** Grants permission to create an assignment with one specified IAM Policy ARN that will be assigned to specified groups or users of QuickSight
  - **Resource types (\*required):** [assignment\*](#list_quicksight-resource-assignment)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateIngestion](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateIngestion.html)  **
  - **Description:** Grants permission to start a SPICE ingestion on a dataset
  - **Resource types (\*required):** [ingestion\*](#list_quicksight-resource-ingestion)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Access level:** Write

- **   [CreateKnowledgeBase](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateKnowledgeBase.html)  **
  - **Description:** Grants permission to create a knowledge base
  - **Resource types (\*required):** [datasource\*](#list_quicksight-resource-datasource) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Resource types (\*required):** [knowledgeBase\*](#list_quicksight-resource-knowledgeBase) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Access level:** Write

- **   [CreateLimitsProfile](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateLimitsProfile.html)  **
  - **Description:** Grants permission to create a limits profile
  - **Resource types (\*required):** [limitsProfile\*](#list_quicksight-resource-limitsProfile)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateNamespace](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateNamespace.html)  **
  - **Description:** Grants permission to create an QuickSight namespace
  - **Resource types (\*required):** [namespace\*](#list_quicksight-resource-namespace)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Access level:** Write

- **   [CreateOAuthClientApplication](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateOAuthClientApplication.html)  **
  - **Description:** Grants permission to create an OAuth client application
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Access level:** Write

- **   [CreateRefreshSchedule](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateRefreshSchedule.html)  **
  - **Description:** Grants permission to create a refresh schedule for a dataset
  - **Resource types (\*required):** [refreshschedule\*](#list_quicksight-resource-refreshschedule)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateRoleMembership](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateRoleMembership.html)  **
  - **Description:** Grants permission to add a group member to a role
  - **Resource types (\*required):** 
  - **Condition keys:** [quicksight:Group](#list_quicksight-quicksight_Group)
  - **Access level:** Write

- **   [CreateSpace](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateSpace.html)  **
  - **Description:** Grants permission to create a space
  - **Resource types (\*required):** [space\*](#list_quicksight-resource-space)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateTemplate](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateTemplate.html)  **
  - **Description:** Grants permission to create a template
  - **Resource types (\*required):** [template\*](#list_quicksight-resource-template)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Access level:** Write

- **   [CreateTemplateAlias](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateTemplateAlias.html)  **
  - **Description:** Grants permission to create a template alias
  - **Resource types (\*required):** [template\*](#list_quicksight-resource-template)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Access level:** Write

- **   [CreateTheme](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateTheme.html)  **
  - **Description:** Grants permission to create a theme
  - **Resource types (\*required):** [theme\*](#list_quicksight-resource-theme)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Access level:** Write

- **   [CreateThemeAlias](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateThemeAlias.html)  **
  - **Description:** Grants permission to create an alias for a theme version
  - **Resource types (\*required):** [theme\*](#list_quicksight-resource-theme)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Access level:** Write

- **   [CreateTopic](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateTopic.html)  **
  - **Description:** Grants permission to create a topic
  - **Resource types (\*required):** [dataset\*](#list_quicksight-resource-dataset)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Access level:** Write

- **   [CreateTopicRefreshSchedule](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateTopicRefreshSchedule.html)  **
  - **Description:** Grants permission to create a refresh schedule for a topic
  - **Resource types (\*required):** [topic\*](#list_quicksight-resource-topic)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateVPCConnection](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateVPCConnection.html)  **
  - **Description:** Grants permission to create a vpc connection
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteAccountCustomPermission](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteAccountCustomPermission.html)  **
  - **Description:** Grants permission to remove the custom permission associated with an account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteAccountCustomization](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteAccountCustomization.html)  **
  - **Description:** Grants permission to delete an account customization for QuickSight account or namespace
  - **Resource types (\*required):** [customization\*](#list_quicksight-resource-customization)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAccountSubscription](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteAccountSubscription.html)  **
  - **Description:** Grants permission to delete a QuickSight account
  - **Resource types (\*required):** [account\*](#list_quicksight-resource-account)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteActionConnector](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteActionConnector.html)  **
  - **Description:** Grants permission to delete an action connector
  - **Resource types (\*required):** [actionconnector\*](#list_quicksight-resource-actionconnector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAgent](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteAgent.html)  **
  - **Description:** Grants permission to delete an agent
  - **Resource types (\*required):** [agent\*](#list_quicksight-resource-agent)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteAnalysis](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteAnalysis.html)  **
  - **Description:** Grants permission to delete an analysis
  - **Resource types (\*required):** [analysis\*](#list_quicksight-resource-analysis)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteApp](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteApp.html)  **
  - **Description:** Grants permission to delete a QuickSight app
  - **Resource types (\*required):** [app\*](#list_quicksight-resource-app)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteApprovalPolicy](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteApprovalPolicy.html)  **
  - **Description:** Grants permission to delete an approval policy
  - **Resource types (\*required):** [approvalPolicy\*](#list_quicksight-resource-approvalPolicy)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteBrand](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteBrand.html)  **
  - **Description:** Grants permission to delete an Amazon QuickSight brand
  - **Resource types (\*required):** [brand\*](#list_quicksight-resource-brand)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteBrandAssignment](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteBrandAssignment.html)  **
  - **Description:** Grants permission to delete a brand assignment
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteCustomPermissions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteCustomPermissions.html)  **
  - **Description:** Grants permission to delete a QuickSight custom permissions resource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteDashboard](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteDashboard.html)  **
  - **Description:** Grants permission to delete a QuickSight Dashboard
  - **Resource types (\*required):** [dashboard\*](#list_quicksight-resource-dashboard)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDataSet](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteDataSet.html)  **
  - **Description:** Grants permission to delete a dataset
  - **Resource types (\*required):** [dataset\*](#list_quicksight-resource-dataset)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteDataSetRefreshProperties](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteDataSetRefreshProperties.html)  **
  - **Description:** Grants permission to delete dataset refresh properties for a dataset
  - **Resource types (\*required):** [dataset\*](#list_quicksight-resource-dataset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDataSource](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteDataSource.html)  **
  - **Description:** Grants permission to delete a data source
  - **Resource types (\*required):** [datasource\*](#list_quicksight-resource-datasource)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteDefaultQBusinessApplication](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteDefaultQBusinessApplication.html)  **
  - **Description:** Grants permission to delete linked QBusiness application for QuickSight account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteDlpSetting](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteDlpSetting.html)  **
  - **Description:** Grants permission to delete a DLP setting
  - **Resource types (\*required):** [dlpSetting\*](#list_quicksight-resource-dlpSetting)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteFlow](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteFlow.html)  **
  - **Description:** Grants permission to delete a flow
  - **Resource types (\*required):** [flow\*](#list_quicksight-resource-flow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteFolder](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteFolder.html)  **
  - **Description:** Grants permission to delete a QuickSight Folder
  - **Resource types (\*required):** [folder\*](#list_quicksight-resource-folder)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteFolderMembership](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteFolderMembership.html)  **
  - **Description:** Grants permission to remove a QuickSight Dashboard, Analysis or Dataset from a QuickSight Folder
  - **Resource types (\*required):** [analysis](#list_quicksight-resource-analysis) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [dashboard](#list_quicksight-resource-dashboard) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [dataset](#list_quicksight-resource-dataset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [folder\*](#list_quicksight-resource-folder) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteGroup](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteGroup.html)  **
  - **Description:** Grants permission to remove a user group from QuickSight
  - **Resource types (\*required):** [group\*](#list_quicksight-resource-group)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteGroupMembership](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteGroupMembership.html)  **
  - **Description:** Grants permission to remove a user from a group so that he/she is no longer a member of the group
  - **Resource types (\*required):** [group\*](#list_quicksight-resource-group)
  - **Condition keys:** [quicksight:UserName](#list_quicksight-quicksight_UserName)
  - **Access level:** Write

- **   [DeleteIAMPolicyAssignment](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteIAMPolicyAssignment.html)  **
  - **Description:** Grants permission to update an existing assignment
  - **Resource types (\*required):** [assignment\*](#list_quicksight-resource-assignment)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteIdentityPropagationConfig](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteIdentityPropagationConfig.html)  **
  - **Description:** Grants permission to remove AWS services for trusted identity propagation in QuickSight
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteKnowledgeBase](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteKnowledgeBase.html)  **
  - **Description:** Grants permission to delete a knowledge base
  - **Resource types (\*required):** [knowledgeBase\*](#list_quicksight-resource-knowledgeBase)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteLimitsProfile](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteLimitsProfile.html)  **
  - **Description:** Grants permission to delete a limits profile
  - **Resource types (\*required):** [limitsProfile\*](#list_quicksight-resource-limitsProfile)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteNamespace](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteNamespace.html)  **
  - **Description:** Grants permission to delete a QuickSight namespace
  - **Resource types (\*required):** [namespace\*](#list_quicksight-resource-namespace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteOAuthClientApplication](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteOAuthClientApplication.html)  **
  - **Description:** Grants permission to delete an OAuth client application
  - **Resource types (\*required):** [oauthClientApplication\*](#list_quicksight-resource-oauthClientApplication)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteRefreshSchedule](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteRefreshSchedule.html)  **
  - **Description:** Grants permission to delete a refresh schedule for a dataset
  - **Resource types (\*required):** [refreshschedule\*](#list_quicksight-resource-refreshschedule)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteRoleCustomPermission](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteRoleCustomPermission.html)  **
  - **Description:** Grants permission to remove the custom permission associated with a role
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteRoleMembership](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteRoleMembership.html)  **
  - **Description:** Grants permission to remove a group member from a role
  - **Resource types (\*required):** 
  - **Condition keys:** [quicksight:Group](#list_quicksight-quicksight_Group)
  - **Access level:** Write

- **   [DeleteSpace](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteSpace.html)  **
  - **Description:** Grants permission to delete a space
  - **Resource types (\*required):** [space\*](#list_quicksight-resource-space)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteTemplate](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteTemplate.html)  **
  - **Description:** Grants permission to delete a template
  - **Resource types (\*required):** [template\*](#list_quicksight-resource-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTemplateAlias](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteTemplateAlias.html)  **
  - **Description:** Grants permission to delete a template alias
  - **Resource types (\*required):** [template\*](#list_quicksight-resource-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTheme](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteTheme.html)  **
  - **Description:** Grants permission to delete a theme
  - **Resource types (\*required):** [theme\*](#list_quicksight-resource-theme)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteThemeAlias](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteThemeAlias.html)  **
  - **Description:** Grants permission to delete the alias of a theme
  - **Resource types (\*required):** [theme\*](#list_quicksight-resource-theme)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTopic](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteTopic.html)  **
  - **Description:** Grants permission to delete a topic
  - **Resource types (\*required):** [topic\*](#list_quicksight-resource-topic)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteTopicRefreshSchedule](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteTopicRefreshSchedule.html)  **
  - **Description:** Grants permission to delete a refresh schedule for a topic
  - **Resource types (\*required):** [topic\*](#list_quicksight-resource-topic)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteUser](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteUser.html)  **
  - **Description:** Grants permission to delete a QuickSight user, given the user name
  - **Resource types (\*required):** [user\*](#list_quicksight-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteUserByPrincipalId](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteUserByPrincipalId.html)  **
  - **Description:** Grants permission to delete a user identified by its principal ID
  - **Resource types (\*required):** [user\*](#list_quicksight-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteUserCustomPermission](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteUserCustomPermission.html)  **
  - **Description:** Grants permission to remove the custom permission associated with a user
  - **Resource types (\*required):** [user\*](#list_quicksight-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteVPCConnection](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteVPCConnection.html)  **
  - **Description:** Grants permission to delete a vpc connection
  - **Resource types (\*required):** [vpcconnection\*](#list_quicksight-resource-vpcconnection)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Access level:** Write

- **   [DescribeAccountCustomPermission](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeAccountCustomPermission.html)  **
  - **Description:** Grants permission to describe the custom permission associated with an account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeAccountCustomization](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeAccountCustomization.html)  **
  - **Description:** Grants permission to describe an account customization for QuickSight account or namespace
  - **Resource types (\*required):** [customization\*](#list_quicksight-resource-customization)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeAccountSettings](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeAccountSettings.html)  **
  - **Description:** Grants permission to describe the administrative account settings for QuickSight account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeAccountSubscription](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeAccountSubscription.html)  **
  - **Description:** Grants permission to describe a QuickSight account
  - **Resource types (\*required):** [account\*](#list_quicksight-resource-account)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeActionConnector](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeActionConnector.html)  **
  - **Description:** Grants permission to describe an action connector
  - **Resource types (\*required):** [actionconnector\*](#list_quicksight-resource-actionconnector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeActionConnectorPermissions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeActionConnectorPermissions.html)  **
  - **Description:** Grants permission to describe permissions for an action connector
  - **Resource types (\*required):** [actionconnector\*](#list_quicksight-resource-actionconnector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeAgent](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeAgent.html)  **
  - **Description:** Grants permission to describe an agent
  - **Resource types (\*required):** [agent\*](#list_quicksight-resource-agent)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeAgentPermissions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeAgentPermissions.html)  **
  - **Description:** Grants permission to describe agent's permissions
  - **Resource types (\*required):** [agent\*](#list_quicksight-resource-agent)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeAnalysis](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeAnalysis.html)  **
  - **Description:** Grants permission to describe an analysis
  - **Resource types (\*required):** [analysis\*](#list_quicksight-resource-analysis)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeAnalysisPermissions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeAnalysisPermissions.html)  **
  - **Description:** Grants permission to describe permissions for an analysis
  - **Resource types (\*required):** [analysis\*](#list_quicksight-resource-analysis)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeApp](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeApp.html)  **
  - **Description:** Grants permission to describe a QuickSight app
  - **Resource types (\*required):** [app\*](#list_quicksight-resource-app)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeAppPermissions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeAppPermissions.html)  **
  - **Description:** Grants permission to describe permissions for a QuickSight app
  - **Resource types (\*required):** [app\*](#list_quicksight-resource-app)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeApprovalPolicy](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeApprovalPolicy.html)  **
  - **Description:** Grants permission to describe an approval policy
  - **Resource types (\*required):** [approvalPolicy\*](#list_quicksight-resource-approvalPolicy)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeAssetBundleExportJob](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeAssetBundleExportJob.html)  **
  - **Description:** Grants permission to describe an asset bundle export job
  - **Resource types (\*required):** [assetBundleExportJob\*](#list_quicksight-resource-assetBundleExportJob)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeAssetBundleImportJob](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeAssetBundleImportJob.html)  **
  - **Description:** Grants permission to describe an asset bundle import job
  - **Resource types (\*required):** [assetBundleImportJob\*](#list_quicksight-resource-assetBundleImportJob)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeAutomationJob](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeAutomationJob.html)  **
  - **Description:** Grants permission to describe an automation job
  - **Resource types (\*required):** [automationJob\*](#list_quicksight-resource-automationJob)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeBrand](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeBrand.html)  **
  - **Description:** Grants permission to describe a brand
  - **Resource types (\*required):** [brand\*](#list_quicksight-resource-brand)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeBrandAssignment](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeBrandAssignment.html)  **
  - **Description:** Grants permission to describe a brand assignment
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeBrandPublishedVersion](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeBrandPublishedVersion.html)  **
  - **Description:** Grants permission to describes the published version of the brand
  - **Resource types (\*required):** [brand\*](#list_quicksight-resource-brand)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeCustomPermissions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeCustomPermissions.html)  **
  - **Description:** Grants permission to describe a custom permissions resource in a QuickSight account
  - **Resource types (\*required):** [custompermissions\*](#list_quicksight-resource-custompermissions)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeDashboard](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeDashboard.html)  **
  - **Description:** Grants permission to describe a QuickSight Dashboard
  - **Resource types (\*required):** [dashboard\*](#list_quicksight-resource-dashboard)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeDashboardPermissions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeDashboardPermissions.html)  **
  - **Description:** Grants permission to describe permissions for a QuickSight Dashboard
  - **Resource types (\*required):** [dashboard\*](#list_quicksight-resource-dashboard)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeDashboardSnapshotJob](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeDashboardSnapshotJob.html)  **
  - **Description:** Grants permission to describe a dashboard snapshot job
  - **Resource types (\*required):** [dashboardSnapshotJob\*](#list_quicksight-resource-dashboardSnapshotJob)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeDashboardSnapshotJobResult](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeDashboardSnapshotJobResult.html)  **
  - **Description:** Grants permission to describe result of a dashboard snapshot job
  - **Resource types (\*required):** [dashboardSnapshotJob\*](#list_quicksight-resource-dashboardSnapshotJob)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeDashboardsQAConfiguration](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeDashboardsQAConfiguration.html)  **
  - **Description:** Grants permission to describe dashboards qa configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeDataSet](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeDataSet.html)  **
  - **Description:** Grants permission to describe a dataset
  - **Resource types (\*required):** [dataset\*](#list_quicksight-resource-dataset)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Access level:** Read

- **   [DescribeDataSetPermissions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeDataSetPermissions.html)  **
  - **Description:** Grants permission to describe the resource policy of a dataset
  - **Resource types (\*required):** [dataset\*](#list_quicksight-resource-dataset)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Access level:** Read

- **   [DescribeDataSetRefreshProperties](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeDataSetRefreshProperties.html)  **
  - **Description:** Grants permission to describe refresh properties for a dataset
  - **Resource types (\*required):** [dataset\*](#list_quicksight-resource-dataset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeDataSource](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeDataSource.html)  **
  - **Description:** Grants permission to describe a data source
  - **Resource types (\*required):** [datasource\*](#list_quicksight-resource-datasource)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Access level:** Read

- **   [DescribeDataSourcePermissions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeDataSourcePermissions.html)  **
  - **Description:** Grants permission to describe the resource policy of a data source
  - **Resource types (\*required):** [datasource\*](#list_quicksight-resource-datasource)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Access level:** Read

- **   [DescribeDefaultQBusinessApplication](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeDefaultQBusinessApplication.html)  **
  - **Description:** Grants permission to describe linked QBusiness application Id for QuickSight account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeDlpSetting](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeDlpSetting.html)  **
  - **Description:** Grants permission to describe a DLP setting
  - **Resource types (\*required):** [dlpSetting\*](#list_quicksight-resource-dlpSetting)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeFlow](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeFlow.html)  **
  - **Description:** Grants permission to describe a flow
  - **Resource types (\*required):** [flow\*](#list_quicksight-resource-flow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeFolder](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeFolder.html)  **
  - **Description:** Grants permission to describe a QuickSight Folder
  - **Resource types (\*required):** [folder\*](#list_quicksight-resource-folder)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeFolderPermissions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeFolderPermissions.html)  **
  - **Description:** Grants permission to describe permissions for a QuickSight Folder
  - **Resource types (\*required):** [folder\*](#list_quicksight-resource-folder)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeFolderResolvedPermissions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeFolderResolvedPermissions.html)  **
  - **Description:** Grants permission to describe resolved permissions for a QuickSight Folder
  - **Resource types (\*required):** [folder\*](#list_quicksight-resource-folder)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeGroup](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeGroup.html)  **
  - **Description:** Grants permission to describe a QuickSight group
  - **Resource types (\*required):** [group\*](#list_quicksight-resource-group)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeGroupMembership](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeGroupMembership.html)  **
  - **Description:** Grants permission to describe a QuickSight group member
  - **Resource types (\*required):** [group\*](#list_quicksight-resource-group)
  - **Condition keys:** [quicksight:UserName](#list_quicksight-quicksight_UserName)
  - **Access level:** Read

- **   [DescribeIAMPolicyAssignment](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeIAMPolicyAssignment.html)  **
  - **Description:** Grants permission to describe an existing assignment
  - **Resource types (\*required):** [assignment\*](#list_quicksight-resource-assignment)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeIngestion](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeIngestion.html)  **
  - **Description:** Grants permission to describe a SPICE ingestion on a dataset
  - **Resource types (\*required):** [ingestion\*](#list_quicksight-resource-ingestion)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Access level:** Read

- **   [DescribeIpRestriction](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeIpRestriction.html)  **
  - **Description:** Grants permission to describe the IP restrictions for QuickSight account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeKeyRegistration](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeKeyRegistration.html)  **
  - **Description:** Grants permission to describe QuickSight key registration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeKnowledgeBase](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeKnowledgeBase.html)  **
  - **Description:** Grants permission to describe a knowledge base
  - **Resource types (\*required):** [knowledgeBase\*](#list_quicksight-resource-knowledgeBase)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeKnowledgeBasePermissions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeKnowledgeBasePermissions.html)  **
  - **Description:** Grants permission to describe the resource policy of a knowledge base
  - **Resource types (\*required):** [knowledgeBase\*](#list_quicksight-resource-knowledgeBase)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [DescribeLimitsProfile](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeLimitsProfile.html)  **
  - **Description:** Grants permission to describe a limits profile
  - **Resource types (\*required):** [limitsProfile\*](#list_quicksight-resource-limitsProfile)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeNamespace](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeNamespace.html)  **
  - **Description:** Grants permission to describe a QuickSight namespace
  - **Resource types (\*required):** [namespace\*](#list_quicksight-resource-namespace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeOAuthClientApplication](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeOAuthClientApplication.html)  **
  - **Description:** Grants permission to describe an OAuth client application
  - **Resource types (\*required):** [oauthClientApplication\*](#list_quicksight-resource-oauthClientApplication)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Access level:** Read

- **   [DescribeQPersonalizationConfiguration](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeQPersonalizationConfiguration.html)  **
  - **Description:** Grants permission to describe a personalization configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeQuickSightQSearchConfiguration](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeQuickSightQSearchConfiguration.html)  **
  - **Description:** Grants permission to describe QuickSight Q Search configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeRefreshSchedule](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeRefreshSchedule.html)  **
  - **Description:** Grants permission to describe a refresh schedule for a dataset
  - **Resource types (\*required):** [refreshschedule\*](#list_quicksight-resource-refreshschedule)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeRoleCustomPermission](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeRoleCustomPermission.html)  **
  - **Description:** Grants permission to describe the custom permission associated with a role
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeSelfUpgradeConfiguration](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeSelfUpgradeConfiguration.html)  **
  - **Description:** Grants permission to describe the administrative self upgrade configuration associated with an account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeSpace](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeSpace.html)  **
  - **Description:** Grants permission to describe a space
  - **Resource types (\*required):** [space\*](#list_quicksight-resource-space)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeSpacePermissions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeSpacePermissions.html)  **
  - **Description:** Grants permission to describe permissions for a space
  - **Resource types (\*required):** [space\*](#list_quicksight-resource-space)
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [DescribeTemplate](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeTemplate.html)  **
  - **Description:** Grants permission to describe a template
  - **Resource types (\*required):** [template\*](#list_quicksight-resource-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeTemplateAlias](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeTemplateAlias.html)  **
  - **Description:** Grants permission to describe a template alias
  - **Resource types (\*required):** [template\*](#list_quicksight-resource-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeTemplatePermissions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeTemplatePermissions.html)  **
  - **Description:** Grants permission to describe permissions for a template
  - **Resource types (\*required):** [template\*](#list_quicksight-resource-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeTheme](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeTheme.html)  **
  - **Description:** Grants permission to describe a theme
  - **Resource types (\*required):** [theme\*](#list_quicksight-resource-theme)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeThemeAlias](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeThemeAlias.html)  **
  - **Description:** Grants permission to describe a theme alias
  - **Resource types (\*required):** [theme\*](#list_quicksight-resource-theme)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeThemePermissions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeThemePermissions.html)  **
  - **Description:** Grants permission to describe permissions for a theme
  - **Resource types (\*required):** [theme\*](#list_quicksight-resource-theme)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeTopic](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeTopic.html)  **
  - **Description:** Grants permission to describe a topic
  - **Resource types (\*required):** [topic\*](#list_quicksight-resource-topic)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Access level:** Read

- **   [DescribeTopicPermissions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeTopicPermissions.html)  **
  - **Description:** Grants permission to describe the resource policy of a topic
  - **Resource types (\*required):** [topic\*](#list_quicksight-resource-topic)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Access level:** Permissions management, Write

- **   [DescribeTopicRefresh](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeTopicRefresh.html)  **
  - **Description:** Grants permission to describe the refresh status of a topic
  - **Resource types (\*required):** [topic\*](#list_quicksight-resource-topic)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Access level:** Read

- **   [DescribeTopicRefreshSchedule](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeTopicRefreshSchedule.html)  **
  - **Description:** Grants permission to describe a refresh schedule for a topic
  - **Resource types (\*required):** [topic\*](#list_quicksight-resource-topic)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeUser](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeUser.html)  **
  - **Description:** Grants permission to describe a QuickSight user given the user name
  - **Resource types (\*required):** [user\*](#list_quicksight-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeVPCConnection](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeVPCConnection.html)  **
  - **Description:** Grants permission to describe a vpc connection
  - **Resource types (\*required):** [vpcconnection\*](#list_quicksight-resource-vpcconnection)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Access level:** Read

- **   [GenerateEmbedUrlForAnonymousUser](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_GenerateEmbedUrlForAnonymousUser.html)  **
  - **Description:** Grants permission to generate a URL used to embed a QuickSight Dashboard or Q Topic for a user not registered with QuickSight
  - **Resource types (\*required):** [dashboard](#list_quicksight-resource-dashboard) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[quicksight:AllowedEmbeddingDomains](#list_quicksight-quicksight_AllowedEmbeddingDomains)
  - **Resource types (\*required):** [namespace\*](#list_quicksight-resource-namespace) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[quicksight:AllowedEmbeddingDomains](#list_quicksight-quicksight_AllowedEmbeddingDomains)
  - **Resource types (\*required):** [theme](#list_quicksight-resource-theme) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[quicksight:AllowedEmbeddingDomains](#list_quicksight-quicksight_AllowedEmbeddingDomains)
  - **Resource types (\*required):** [topic](#list_quicksight-resource-topic) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[quicksight:AllowedEmbeddingDomains](#list_quicksight-quicksight_AllowedEmbeddingDomains)
  - **Access level:** Write

- **   [GenerateEmbedUrlForRegisteredUser](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_GenerateEmbedUrlForRegisteredUser.html)  **
  - **Description:** Grants permission to generate a URL used to embed a QuickSight Dashboard for a user registered with QuickSight
  - **Resource types (\*required):** [user\*](#list_quicksight-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[quicksight:AllowedEmbeddingDomains](#list_quicksight-quicksight_AllowedEmbeddingDomains)
  - **Access level:** Write

- **   [GenerateEmbedUrlForRegisteredUserWithIdentity](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_GenerateEmbedUrlForRegisteredUserWithIdentity.html)  **
  - **Description:** Grants permission to generate a URL used to embed a QuickSight Experience for a user registered with QuickSight using Identity-enhanced role session
  - **Resource types (\*required):** 
  - **Condition keys:** [quicksight:AllowedEmbeddingDomains](#list_quicksight-quicksight_AllowedEmbeddingDomains)
  - **Access level:** Write

- **   [GetDashboardEmbedUrl](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_GetDashboardEmbedUrl.html)  **
  - **Description:** Grants permission to get a URL used to embed a QuickSight Dashboard
  - **Resource types (\*required):** [dashboard\*](#list_quicksight-resource-dashboard)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetFlowMetadata](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_GetFlowMetadata.html)  **
  - **Description:** Grants permission to get metadata for a flow
  - **Resource types (\*required):** [flow\*](#list_quicksight-resource-flow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetFlowPermissions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_GetFlowPermissions.html)  **
  - **Description:** Grants permission to get permissions for a flow
  - **Resource types (\*required):** [flow\*](#list_quicksight-resource-flow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetIdentityContext](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_GetIdentityContext.html)  **
  - **Description:** Grants permission to get identity context for a user
  - **Resource types (\*required):** [user\*](#list_quicksight-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSessionEmbedUrl](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_GetSessionEmbedUrl.html)  **
  - **Description:** Grants permission to get a URL to embed QuickSight console experience
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListActionConnectors](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListActionConnectors.html)  **
  - **Description:** Grants permission to list action connectors
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAgents](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListAgents.html)  **
  - **Description:** Grants permission to list agents
  - **Resource types (\*required):** [agent\*](#list_quicksight-resource-agent)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAnalyses](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListAnalyses.html)  **
  - **Description:** Grants permission to list all analyses in an account
  - **Resource types (\*required):** [analysis\*](#list_quicksight-resource-analysis)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListApprovalPolicies](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListApprovalPolicies.html)  **
  - **Description:** Grants permission to list approval policies
  - **Resource types (\*required):** [approvalPolicy\*](#list_quicksight-resource-approvalPolicy)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListApps](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListApps.html)  **
  - **Description:** Grants permission to list all apps in a QuickSight account
  - **Resource types (\*required):** [app\*](#list_quicksight-resource-app)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListAssetBundleExportJobs](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListAssetBundleExportJobs.html)  **
  - **Description:** Grants permission to list all asset bundle export jobs
  - **Resource types (\*required):** [assetBundleExportJob\*](#list_quicksight-resource-assetBundleExportJob)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAssetBundleImportJobs](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListAssetBundleImportJobs.html)  **
  - **Description:** Grants permission to list all asset bundle import jobs
  - **Resource types (\*required):** [assetBundleImportJob\*](#list_quicksight-resource-assetBundleImportJob)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListBrands](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListBrands.html)  **
  - **Description:** Grants permission to lists all brands in an Amazon QuickSight account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCustomPermissions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListCustomPermissions.html)  **
  - **Description:** Grants permission to list custom permissions resources in QuickSight account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDashboardVersions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListDashboardVersions.html)  **
  - **Description:** Grants permission to list all versions of a QuickSight Dashboard
  - **Resource types (\*required):** [dashboard\*](#list_quicksight-resource-dashboard)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDashboards](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListDashboards.html)  **
  - **Description:** Grants permission to list all Dashboards in a QuickSight Account
  - **Resource types (\*required):** [dashboard\*](#list_quicksight-resource-dashboard)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDataSets](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListDataSets.html)  **
  - **Description:** Grants permission to list all datasets
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Access level:** List

- **   [ListDataSources](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListDataSources.html)  **
  - **Description:** Grants permission to list all data sources
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Access level:** List

- **   [ListDlpSettings](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListDlpSettings.html)  **
  - **Description:** Grants permission to list DLP settings in an account
  - **Resource types (\*required):** [dlpSetting\*](#list_quicksight-resource-dlpSetting)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListFlows](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListFlows.html)  **
  - **Description:** Grants permission to list all flows in an Amazon QuickSight account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListFolderMembers](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListFolderMembers.html)  **
  - **Description:** Grants permission to list all members in a folder
  - **Resource types (\*required):** [folder\*](#list_quicksight-resource-folder)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListFolders](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListFolders.html)  **
  - **Description:** Grants permission to list all Folders in a QuickSight Account
  - **Resource types (\*required):** [folder\*](#list_quicksight-resource-folder)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListFoldersForResource](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListFoldersForResource.html)  **
  - **Description:** Grants permission to list all Folders in which a QuickSight resource is a member
  - **Resource types (\*required):** [analysis](#list_quicksight-resource-analysis) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [dashboard](#list_quicksight-resource-dashboard) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [dataset](#list_quicksight-resource-dataset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [datasource](#list_quicksight-resource-datasource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [topic](#list_quicksight-resource-topic) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListGroupMemberships](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListGroupMemberships.html)  **
  - **Description:** Grants permission to list member users in a group
  - **Resource types (\*required):** [group\*](#list_quicksight-resource-group)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListGroups](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListGroups.html)  **
  - **Description:** Grants permission to list all user groups in QuickSight
  - **Resource types (\*required):** [group\*](#list_quicksight-resource-group)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListIAMPolicyAssignments](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListIAMPolicyAssignments.html)  **
  - **Description:** Grants permission to list all assignments in the current Amazon QuickSight account
  - **Resource types (\*required):** [assignment\*](#list_quicksight-resource-assignment)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListIAMPolicyAssignmentsForUser](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListIAMPolicyAssignmentsForUser.html)  **
  - **Description:** Grants permission to list all assignments assigned to a user and the groups it belongs
  - **Resource types (\*required):** [assignment\*](#list_quicksight-resource-assignment)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListIdentityPropagationConfigs](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListIdentityPropagationConfigs.html)  **
  - **Description:** Grants permission to list AWS services enabled for trusted identity propagation in QuickSight
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListIngestions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListIngestions.html)  **
  - **Description:** Grants permission to list all SPICE ingestions on a dataset
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Access level:** List

- **   [ListKnowledgeBases](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListKnowledgeBases.html)  **
  - **Description:** Grants permission to list all knowledge bases in an account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListLimitsProfiles](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListLimitsProfiles.html)  **
  - **Description:** Grants permission to list limits profiles
  - **Resource types (\*required):** [limitsProfile\*](#list_quicksight-resource-limitsProfile)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListNamespaces](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListNamespaces.html)  **
  - **Description:** Grants permission to lists all namespaces in a QuickSight account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListOAuthClientApplications](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListOAuthClientApplications.html)  **
  - **Description:** Grants permission to list OAuth client applications in an account
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Access level:** List

- **   [ListRefreshSchedules](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListRefreshSchedules.html)  **
  - **Description:** Grants permission to list all refresh schedules on a dataset
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRoleMemberships](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListRoleMemberships.html)  **
  - **Description:** Grants permission to list the members of a role
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSelfUpgrades](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListSelfUpgrades.html)  **
  - **Description:** Grants permission to list all of the pending self upgrade requests associated with an account
  - **Resource types (\*required):** [user\*](#list_quicksight-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListSpaceResources](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListSpaceResources.html)  **
  - **Description:** Grants permission to list resources in a space
  - **Resource types (\*required):** [space\*](#list_quicksight-resource-space)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSpaces](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListSpaces.html)  **
  - **Description:** Grants permission to list spaces
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags of a QuickSight resource
  - **Resource types (\*required):** [actionconnector](#list_quicksight-resource-actionconnector) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [analysis](#list_quicksight-resource-analysis) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [app](#list_quicksight-resource-app) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [brand](#list_quicksight-resource-brand) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [customization](#list_quicksight-resource-customization) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [custompermissions](#list_quicksight-resource-custompermissions) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [dashboard](#list_quicksight-resource-dashboard) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [dataset](#list_quicksight-resource-dataset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [datasource](#list_quicksight-resource-datasource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [dlpSetting](#list_quicksight-resource-dlpSetting) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [emailCustomizationTemplate](#list_quicksight-resource-emailCustomizationTemplate) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [flow](#list_quicksight-resource-flow) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [folder](#list_quicksight-resource-folder) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [namespace](#list_quicksight-resource-namespace) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [oauthClientApplication](#list_quicksight-resource-oauthClientApplication) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [template](#list_quicksight-resource-template) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [theme](#list_quicksight-resource-theme) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [topic](#list_quicksight-resource-topic) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [user](#list_quicksight-resource-user) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [vpcconnection](#list_quicksight-resource-vpcconnection) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListTemplateAliases](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListTemplateAliases.html)  **
  - **Description:** Grants permission to list all aliases for a template
  - **Resource types (\*required):** [template\*](#list_quicksight-resource-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTemplateVersions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListTemplateVersions.html)  **
  - **Description:** Grants permission to list all versions of a template
  - **Resource types (\*required):** [template\*](#list_quicksight-resource-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTemplates](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListTemplates.html)  **
  - **Description:** Grants permission to list all templates in a QuickSight account
  - **Resource types (\*required):** [template\*](#list_quicksight-resource-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListThemeAliases](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListThemeAliases.html)  **
  - **Description:** Grants permission to list all aliases of a theme
  - **Resource types (\*required):** [theme\*](#list_quicksight-resource-theme)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListThemeVersions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListThemeVersions.html)  **
  - **Description:** Grants permission to list all versions of a theme
  - **Resource types (\*required):** [theme\*](#list_quicksight-resource-theme)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListThemes](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListThemes.html)  **
  - **Description:** Grants permission to list all themes in an account
  - **Resource types (\*required):** [theme\*](#list_quicksight-resource-theme)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTopicRefreshSchedules](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListTopicRefreshSchedules.html)  **
  - **Description:** Grants permission to list all refresh schedules on a topic
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTopicReviewedAnswers](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListTopicReviewedAnswers.html)  **
  - **Description:** Grants permission to list all reviewed answers for topic
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Access level:** List

- **   [ListTopics](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListTopics.html)  **
  - **Description:** Grants permission to list all topics
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Access level:** List

- **   [ListUserGroups](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListUserGroups.html)  **
  - **Description:** Grants permission to list groups that a given user is a member of
  - **Resource types (\*required):** [user\*](#list_quicksight-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListUsers](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListUsers.html)  **
  - **Description:** Grants permission to list all of the QuickSight users belonging to this account
  - **Resource types (\*required):** [user\*](#list_quicksight-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListVPCConnections](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListVPCConnections.html)  **
  - **Description:** Grants permission to list all vpc connections
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Access level:** List

- **   [PredictQAResults](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_PredictQAResults.html)  **
  - **Description:** Grants permission to predict QA results
  - **Resource types (\*required):** [dashboard](#list_quicksight-resource-dashboard) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [topic](#list_quicksight-resource-topic) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [PutDataSetRefreshProperties](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_PutDataSetRefreshProperties.html)  **
  - **Description:** Grants permission to put dataset refresh properties for a dataset
  - **Resource types (\*required):** [dataset\*](#list_quicksight-resource-dataset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RegisterUser](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_RegisterUser.html)  **
  - **Description:** Grants permission to create a QuickSight user, whose identity is associated with the IAM identity/role specified in the request
  - **Resource types (\*required):** [user\*](#list_quicksight-resource-user)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)<br />[quicksight:IamArn](#list_quicksight-quicksight_IamArn)<br />[quicksight:SessionName](#list_quicksight-quicksight_SessionName)
  - **Access level:** Write

- **   [RestoreAnalysis](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_RestoreAnalysis.html)  **
  - **Description:** Grants permission to restore a deleted analysis
  - **Resource types (\*required):** [analysis\*](#list_quicksight-resource-analysis)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SearchActionConnectors](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_SearchActionConnectors.html)  **
  - **Description:** Grants permission to search action connectors
  - **Resource types (\*required):** [actionconnector\*](#list_quicksight-resource-actionconnector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [SearchAgents](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_SearchAgents.html)  **
  - **Description:** Grants permission to search agents
  - **Resource types (\*required):** [agent\*](#list_quicksight-resource-agent)
  - **Condition keys:**  
  - **Access level:** List

- **   [SearchAnalyses](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_SearchAnalyses.html)  **
  - **Description:** Grants permission to search for a sub-set of analyses
  - **Resource types (\*required):** [analysis\*](#list_quicksight-resource-analysis)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [SearchApps](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_SearchApps.html)  **
  - **Description:** Grants permission to search for apps in a QuickSight account
  - **Resource types (\*required):** [app\*](#list_quicksight-resource-app)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [SearchDashboards](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_SearchDashboards.html)  **
  - **Description:** Grants permission to search for a sub-set of QuickSight Dashboards
  - **Resource types (\*required):** [dashboard\*](#list_quicksight-resource-dashboard)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [SearchDataSets](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_SearchDataSets.html)  **
  - **Description:** Grants permission to search for a sub-set of QuickSight DatSets
  - **Resource types (\*required):** [dataset\*](#list_quicksight-resource-dataset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [SearchDataSources](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_SearchDataSources.html)  **
  - **Description:** Grants permission to search for a sub-set of QuickSight Data Sources
  - **Resource types (\*required):** [datasource\*](#list_quicksight-resource-datasource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [SearchFlows](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_SearchFlows.html)  **
  - **Description:** Grants permission to search flows in an Amazon QuickSight account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [SearchFolders](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_SearchFolders.html)  **
  - **Description:** Grants permission to search for a sub-set of QuickSight Folders
  - **Resource types (\*required):** [folder\*](#list_quicksight-resource-folder)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [SearchGroups](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_SearchGroups.html)  **
  - **Description:** Grants permission to search for a sub-set of QuickSight groups
  - **Resource types (\*required):** [group\*](#list_quicksight-resource-group)
  - **Condition keys:**  
  - **Access level:** List

- **   [SearchKnowledgeBases](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_SearchKnowledgeBases.html)  **
  - **Description:** Grants permission to search for a sub-set of knowledge bases
  - **Resource types (\*required):** [knowledgeBase\*](#list_quicksight-resource-knowledgeBase)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [SearchSpaces](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_SearchSpaces.html)  **
  - **Description:** Grants permission to search spaces
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [SearchTopics](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_SearchTopics.html)  **
  - **Description:** Grants permission to search for a sub-set of topics
  - **Resource types (\*required):** [topic\*](#list_quicksight-resource-topic)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [StartAssetBundleExportJob](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_StartAssetBundleExportJob.html)  **
  - **Description:** Grants permission to start an asset bundle export job
  - **Resource types (\*required):** [assetBundleExportJob\*](#list_quicksight-resource-assetBundleExportJob)
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartAssetBundleImportJob](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_StartAssetBundleImportJob.html)  **
  - **Description:** Grants permission to start an asset bundle import job
  - **Resource types (\*required):** [assetBundleImportJob\*](#list_quicksight-resource-assetBundleImportJob)
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartAutomationJob](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_StartAutomationJob.html)  **
  - **Description:** Grants permission to start an automation job
  - **Resource types (\*required):** [automation\*](#list_quicksight-resource-automation)
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartDashboardSnapshotJob](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_StartDashboardSnapshotJob.html)  **
  - **Description:** Grants permission to start a dashboard snapshot job
  - **Resource types (\*required):** [dashboardSnapshotJob\*](#list_quicksight-resource-dashboardSnapshotJob)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartDashboardSnapshotJobSchedule](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_StartDashboardSnapshotJobSchedule.html)  **
  - **Description:** Grants permission to start a dashboard snapshot job schedule
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add tags to a QuickSight resource
  - **Resource types (\*required):** [actionconnector](#list_quicksight-resource-actionconnector) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Resource types (\*required):** [analysis](#list_quicksight-resource-analysis) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Resource types (\*required):** [app](#list_quicksight-resource-app) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Resource types (\*required):** [brand](#list_quicksight-resource-brand) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Resource types (\*required):** [customization](#list_quicksight-resource-customization) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Resource types (\*required):** [custompermissions](#list_quicksight-resource-custompermissions) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Resource types (\*required):** [dashboard](#list_quicksight-resource-dashboard) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Resource types (\*required):** [dataset](#list_quicksight-resource-dataset) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Resource types (\*required):** [datasource](#list_quicksight-resource-datasource) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Resource types (\*required):** [dlpSetting](#list_quicksight-resource-dlpSetting) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Resource types (\*required):** [emailCustomizationTemplate](#list_quicksight-resource-emailCustomizationTemplate) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Resource types (\*required):** [flow](#list_quicksight-resource-flow) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Resource types (\*required):** [folder](#list_quicksight-resource-folder) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Resource types (\*required):** [ingestion](#list_quicksight-resource-ingestion) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Resource types (\*required):** [namespace](#list_quicksight-resource-namespace) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Resource types (\*required):** [oauthClientApplication](#list_quicksight-resource-oauthClientApplication) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Resource types (\*required):** [template](#list_quicksight-resource-template) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Resource types (\*required):** [theme](#list_quicksight-resource-theme) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Resource types (\*required):** [topic](#list_quicksight-resource-topic) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Resource types (\*required):** [user](#list_quicksight-resource-user) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Resource types (\*required):** [vpcconnection](#list_quicksight-resource-vpcconnection) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from a QuickSight resource
  - **Resource types (\*required):** [actionconnector](#list_quicksight-resource-actionconnector) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Resource types (\*required):** [analysis](#list_quicksight-resource-analysis) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Resource types (\*required):** [app](#list_quicksight-resource-app) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Resource types (\*required):** [brand](#list_quicksight-resource-brand) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Resource types (\*required):** [customization](#list_quicksight-resource-customization) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Resource types (\*required):** [custompermissions](#list_quicksight-resource-custompermissions) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Resource types (\*required):** [dashboard](#list_quicksight-resource-dashboard) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Resource types (\*required):** [dataset](#list_quicksight-resource-dataset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Resource types (\*required):** [datasource](#list_quicksight-resource-datasource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Resource types (\*required):** [dlpSetting](#list_quicksight-resource-dlpSetting) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Resource types (\*required):** [emailCustomizationTemplate](#list_quicksight-resource-emailCustomizationTemplate) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Resource types (\*required):** [flow](#list_quicksight-resource-flow) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Resource types (\*required):** [folder](#list_quicksight-resource-folder) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Resource types (\*required):** [ingestion](#list_quicksight-resource-ingestion) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Resource types (\*required):** [namespace](#list_quicksight-resource-namespace) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Resource types (\*required):** [oauthClientApplication](#list_quicksight-resource-oauthClientApplication) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Resource types (\*required):** [template](#list_quicksight-resource-template) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Resource types (\*required):** [theme](#list_quicksight-resource-theme) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Resource types (\*required):** [topic](#list_quicksight-resource-topic) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Resource types (\*required):** [user](#list_quicksight-resource-user) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Resource types (\*required):** [vpcconnection](#list_quicksight-resource-vpcconnection) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateAccountCustomPermission](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateAccountCustomPermission.html)  **
  - **Description:** Grants permission to update the custom permission associated with an account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateAccountCustomization](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateAccountCustomization.html)  **
  - **Description:** Grants permission to update an account customization for QuickSight account or namespace
  - **Resource types (\*required):** [customization\*](#list_quicksight-resource-customization)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateAccountSettings](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateAccountSettings.html)  **
  - **Description:** Grants permission to update the administrative account settings for QuickSight account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateActionConnector](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateActionConnector.html)  **
  - **Description:** Grants permission to update an action connector
  - **Resource types (\*required):** [actionconnector\*](#list_quicksight-resource-actionconnector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateActionConnectorPermissions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateActionConnectorPermissions.html)  **
  - **Description:** Grants permission to update permissions for an action connector
  - **Resource types (\*required):** [actionconnector\*](#list_quicksight-resource-actionconnector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [UpdateAgent](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateAgent.html)  **
  - **Description:** Grants permission to update an agent
  - **Resource types (\*required):** [agent\*](#list_quicksight-resource-agent)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateAgentPermissions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateAgentPermissions.html)  **
  - **Description:** Grants permission to update agent permissions
  - **Resource types (\*required):** [agent\*](#list_quicksight-resource-agent)
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [UpdateAnalysis](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateAnalysis.html)  **
  - **Description:** Grants permission to update an analysis
  - **Resource types (\*required):** [analysis\*](#list_quicksight-resource-analysis)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateAnalysisPermissions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateAnalysisPermissions.html)  **
  - **Description:** Grants permission to update permissions for an analysis
  - **Resource types (\*required):** [analysis\*](#list_quicksight-resource-analysis)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [UpdateAppPermissions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateAppPermissions.html)  **
  - **Description:** Grants permission to update permissions for a QuickSight app
  - **Resource types (\*required):** [app\*](#list_quicksight-resource-app)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [UpdateApplicationWithTokenExchangeGrant](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateApplicationWithTokenExchangeGrant.html)  **
  - **Description:** Grants permission to update QuickSight IAM Identity Center application with Token Exchange grant
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateApprovalPolicy](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateApprovalPolicy.html)  **
  - **Description:** Grants permission to update an approval policy
  - **Resource types (\*required):** [approvalPolicy\*](#list_quicksight-resource-approvalPolicy)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateBrand](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateBrand.html)  **
  - **Description:** Grants permission to update a brand
  - **Resource types (\*required):** [brand\*](#list_quicksight-resource-brand)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateBrandAssignment](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateBrandAssignment.html)  **
  - **Description:** Grants permission to update a brand assignment
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateBrandPublishedVersion](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateBrandPublishedVersion.html)  **
  - **Description:** Grants permission to update the published version of a brand
  - **Resource types (\*required):** [brand\*](#list_quicksight-resource-brand)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateCustomPermissions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateCustomPermissions.html)  **
  - **Description:** Grants permission to update a QuickSight custom permissions resource
  - **Resource types (\*required):** [custompermissions\*](#list_quicksight-resource-custompermissions)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDashboard](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateDashboard.html)  **
  - **Description:** Grants permission to update a QuickSight Dashboard
  - **Resource types (\*required):** [dashboard\*](#list_quicksight-resource-dashboard)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDashboardLinks](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateDashboardLinks.html)  **
  - **Description:** Grants permission to update a QuickSight Dashboard's links
  - **Resource types (\*required):** [dashboard\*](#list_quicksight-resource-dashboard)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDashboardPermissions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateDashboardPermissions.html)  **
  - **Description:** Grants permission to update permissions for a QuickSight Dashboard
  - **Resource types (\*required):** [dashboard\*](#list_quicksight-resource-dashboard)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [UpdateDashboardPublishedVersion](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateDashboardPublishedVersion.html)  **
  - **Description:** Grants permission to update a QuickSight Dashboard's Published Version
  - **Resource types (\*required):** [dashboard\*](#list_quicksight-resource-dashboard)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDashboardsQAConfiguration](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateDashboardsQAConfiguration.html)  **
  - **Description:** Grants permission to update dashboards qa configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateDataSet](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateDataSet.html)  **
  - **Description:** Grants permission to update a dataset
  - **Resource types (\*required):** [dataset\*](#list_quicksight-resource-dataset) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Resource types (\*required):** [datasource](#list_quicksight-resource-datasource) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Access level:** Write

- **   [UpdateDataSetPermissions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateDataSetPermissions.html)  **
  - **Description:** Grants permission to update the resource policy of a dataset
  - **Resource types (\*required):** [dataset\*](#list_quicksight-resource-dataset)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Access level:** Permissions management, Write

- **   [UpdateDataSource](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateDataSource.html)  **
  - **Description:** Grants permission to update a data source
  - **Resource types (\*required):** [datasource\*](#list_quicksight-resource-datasource)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Access level:** Write

- **   [UpdateDataSourcePermissions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateDataSourcePermissions.html)  **
  - **Description:** Grants permission to update the resource policy of a data source
  - **Resource types (\*required):** [datasource\*](#list_quicksight-resource-datasource)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Access level:** Permissions management, Write

- **   [UpdateDefaultQBusinessApplication](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateDefaultQBusinessApplication.html)  **
  - **Description:** Grants permission to update linked QBusiness application Id for QuickSight account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateDlpSetting](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateDlpSetting.html)  **
  - **Description:** Grants permission to update a DLP setting
  - **Resource types (\*required):** [dlpSetting\*](#list_quicksight-resource-dlpSetting)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateFlow](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateFlow.html)  **
  - **Description:** Grants permission to update a flow
  - **Resource types (\*required):** [flow\*](#list_quicksight-resource-flow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateFlowPermissions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateFlowPermissions.html)  **
  - **Description:** Grants permission to update permissions for a flow
  - **Resource types (\*required):** [flow\*](#list_quicksight-resource-flow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [UpdateFolder](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateFolder.html)  **
  - **Description:** Grants permission to update a QuickSight Folder
  - **Resource types (\*required):** [folder\*](#list_quicksight-resource-folder)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateFolderPermissions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateFolderPermissions.html)  **
  - **Description:** Grants permission to update permissions for a QuickSight Folder
  - **Resource types (\*required):** [folder\*](#list_quicksight-resource-folder)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [UpdateGroup](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateGroup.html)  **
  - **Description:** Grants permission to change group description
  - **Resource types (\*required):** [group\*](#list_quicksight-resource-group)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateIAMPolicyAssignment](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateIAMPolicyAssignment.html)  **
  - **Description:** Grants permission to update an existing assignment
  - **Resource types (\*required):** [assignment\*](#list_quicksight-resource-assignment)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateIdentityPropagationConfig](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateIdentityPropagationConfig.html)  **
  - **Description:** Grants permission to add and update AWS services for trusted identity propagation in QuickSight
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateIpRestriction](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateIpRestriction.html)  **
  - **Description:** Grants permission to update the IP restrictions for QuickSight account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateKeyRegistration](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateKeyRegistration.html)  **
  - **Description:** Grants permission to update QuickSight key registration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateKnowledgeBase](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateKnowledgeBase.html)  **
  - **Description:** Grants permission to update a knowledge base
  - **Resource types (\*required):** [knowledgeBase\*](#list_quicksight-resource-knowledgeBase)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateKnowledgeBasePermissions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateKnowledgeBasePermissions.html)  **
  - **Description:** Grants permission to update the resource policy of a knowledge base
  - **Resource types (\*required):** [knowledgeBase\*](#list_quicksight-resource-knowledgeBase)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [UpdateLimitsProfile](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateLimitsProfile.html)  **
  - **Description:** Grants permission to update a limits profile
  - **Resource types (\*required):** [limitsProfile\*](#list_quicksight-resource-limitsProfile)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateOAuthClientApplication](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateOAuthClientApplication.html)  **
  - **Description:** Grants permission to update an OAuth client application
  - **Resource types (\*required):** [oauthClientApplication\*](#list_quicksight-resource-oauthClientApplication)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Access level:** Write

- **   [UpdatePublicSharingSettings](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdatePublicSharingSettings.html)  **
  - **Description:** Grants permission to enable or disable public sharing on an account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateQPersonalizationConfiguration](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateQPersonalizationConfiguration.html)  **
  - **Description:** Grants permission to update a personalization configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateQuickSightQSearchConfiguration](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateQuickSightQSearchConfiguration.html)  **
  - **Description:** Grants permission to update QuickSight Q Search configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateRefreshSchedule](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateRefreshSchedule.html)  **
  - **Description:** Grants permission to update a refresh schedule for a dataset
  - **Resource types (\*required):** [refreshschedule\*](#list_quicksight-resource-refreshschedule)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateRoleCustomPermission](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateRoleCustomPermission.html)  **
  - **Description:** Grants permission to update the custom permission associated with a role
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateSPICECapacityConfiguration](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateSPICECapacityConfiguration.html)  **
  - **Description:** Grants permission to update QuickSight SPICE capacity configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateSelfUpgrade](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateSelfUpgrade.html)  **
  - **Description:** Grants permission to take action on pending self upgrade requests associated with an account
  - **Resource types (\*required):** [user\*](#list_quicksight-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSelfUpgradeConfiguration](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateSelfUpgradeConfiguration.html)  **
  - **Description:** Grants permission to update the administrative self upgrade configuration associated with an account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateSpace](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateSpace.html)  **
  - **Description:** Grants permission to update a space
  - **Resource types (\*required):** [space\*](#list_quicksight-resource-space)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateSpacePermissions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateSpacePermissions.html)  **
  - **Description:** Grants permission to update permissions for a space
  - **Resource types (\*required):** [space\*](#list_quicksight-resource-space)
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [UpdateSpaceResources](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateSpaceResources.html)  **
  - **Description:** Grants permission to update resources in a space
  - **Resource types (\*required):** [space\*](#list_quicksight-resource-space)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateTemplate](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateTemplate.html)  **
  - **Description:** Grants permission to update a template
  - **Resource types (\*required):** [template\*](#list_quicksight-resource-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateTemplateAlias](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateTemplateAlias.html)  **
  - **Description:** Grants permission to update a template alias
  - **Resource types (\*required):** [template\*](#list_quicksight-resource-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateTemplatePermissions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateTemplatePermissions.html)  **
  - **Description:** Grants permission to update permissions for a template
  - **Resource types (\*required):** [template\*](#list_quicksight-resource-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [UpdateTheme](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateTheme.html)  **
  - **Description:** Grants permission to update a theme
  - **Resource types (\*required):** [theme\*](#list_quicksight-resource-theme)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateThemeAlias](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateThemeAlias.html)  **
  - **Description:** Grants permission to update the alias of a theme
  - **Resource types (\*required):** [theme\*](#list_quicksight-resource-theme)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateThemePermissions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateThemePermissions.html)  **
  - **Description:** Grants permission to update permissions for a theme
  - **Resource types (\*required):** [theme\*](#list_quicksight-resource-theme)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [UpdateTopic](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateTopic.html)  **
  - **Description:** Grants permission to update a topic
  - **Resource types (\*required):** [dataset](#list_quicksight-resource-dataset) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Resource types (\*required):** [topic\*](#list_quicksight-resource-topic) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Access level:** Write

- **   [UpdateTopicPermissions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateTopicPermissions.html)  **
  - **Description:** Grants permission to update the resource policy of a topic
  - **Resource types (\*required):** [topic\*](#list_quicksight-resource-topic)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Access level:** Permissions management, Write

- **   [UpdateTopicRefreshSchedule](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateTopicRefreshSchedule.html)  **
  - **Description:** Grants permission to update a refresh schedule for a topic
  - **Resource types (\*required):** [topic\*](#list_quicksight-resource-topic)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateUser](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateUser.html)  **
  - **Description:** Grants permission to update an Amazon QuickSight user
  - **Resource types (\*required):** [user\*](#list_quicksight-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateUserCustomPermission](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateUserCustomPermission.html)  **
  - **Description:** Grants permission to update the custom permission associated with a user
  - **Resource types (\*required):** [user\*](#list_quicksight-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateVPCConnection](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateVPCConnection.html)  **
  - **Description:** Grants permission to update a vpc connection
  - **Resource types (\*required):** [vpcconnection\*](#list_quicksight-resource-vpcconnection)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Access level:** Write



## Permission-only actions for Amazon QuickSight
<a name="list_quicksight-permission-only-actions"></a>

The following actions are defined by Amazon QuickSight but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [AccountConfigurations](https://docs.aws.amazon.com/quicksight/latest/user/accessing-data-sources.html)  **
  - **Description:** Grants permission to enable setting default access to AWS resources
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [AllowVendedLogDeliveryForResource](https://docs.aws.amazon.com/quicksight/latest/user/iam-actions.html)  **
  - **Description:** Grants permission to configure log delivery for QuickSuite instance
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [BatchGetPreferences](https://docs.aws.amazon.com/quicksight/latest/user/iam-actions.html)  **
  - **Description:** Grants permission to get user preferences
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [BatchUpdatePreferences](https://docs.aws.amazon.com/quicksight/latest/user/iam-actions.html)  **
  - **Description:** Grants permission to update user preferences
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateAdmin](https://docs.aws.amazon.com/quicksight/latest/user/iam-actions.html)  **
  - **Description:** Grants permission to provision Amazon QuickSight administrators, authors, and readers
  - **Resource types (\*required):** [user\*](#list_quicksight-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateEmailCustomizationTemplate](https://docs.aws.amazon.com/quicksight/latest/user/customizing-quicksight-email-templates.html)  **
  - **Description:** Grants permission to create a QuickSight email customization template
  - **Resource types (\*required):** [emailCustomizationTemplate\*](#list_quicksight-resource-emailCustomizationTemplate)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Access level:** Write

- **   [CreateExtension](https://docs.aws.amazon.com/quicksight/latest/user/iam-actions.html)  **
  - **Description:** Grants permission to create an extension
  - **Resource types (\*required):** [extension\*](#list_quicksight-resource-extension)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateExtensionAccess](https://docs.aws.amazon.com/quicksight/latest/user/iam-actions.html)  **
  - **Description:** Grants permission to create an extension access
  - **Resource types (\*required):** [extensionaccess\*](#list_quicksight-resource-extensionaccess)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateReader](https://docs.aws.amazon.com/quicksight/latest/user/iam-actions.html)  **
  - **Description:** Grants permission to provision Amazon QuickSight readers
  - **Resource types (\*required):** [user\*](#list_quicksight-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateUser](https://docs.aws.amazon.com/quicksight/latest/user/iam-actions.html)  **
  - **Description:** Grants permission to provision Amazon QuickSight authors and readers
  - **Resource types (\*required):** [user\*](#list_quicksight-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteEmailCustomizationTemplate](https://docs.aws.amazon.com/quicksight/latest/user/customizing-quicksight-email-templates.html)  **
  - **Description:** Grants permission to delete a QuickSight email customization template
  - **Resource types (\*required):** [emailCustomizationTemplate\*](#list_quicksight-resource-emailCustomizationTemplate)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteExtension](https://docs.aws.amazon.com/quicksight/latest/user/iam-actions.html)  **
  - **Description:** Grants permission to delete an extension
  - **Resource types (\*required):** [extension\*](#list_quicksight-resource-extension)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteExtensionAccess](https://docs.aws.amazon.com/quicksight/latest/user/iam-actions.html)  **
  - **Description:** Grants permission to delete an extension access
  - **Resource types (\*required):** [extensionaccess\*](#list_quicksight-resource-extensionaccess)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DescribeChatConfiguration](https://docs.aws.amazon.com/quicksight/latest/user/iam-actions.html)  **
  - **Description:** Grants permission to describe chat configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeDlpJob](https://docs.aws.amazon.com/quick/latest/userguide/data-loss-prevention.html)  **
  - **Description:** Grants permission to describe a DLP evaluation job
  - **Resource types (\*required):** [dlpSetting\*](#list_quicksight-resource-dlpSetting)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeEmailCustomizationTemplate](https://docs.aws.amazon.com/quicksight/latest/user/customizing-quicksight-email-templates.html)  **
  - **Description:** Grants permission to describe a QuickSight email customization template
  - **Resource types (\*required):** [emailCustomizationTemplate\*](#list_quicksight-resource-emailCustomizationTemplate)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeExtension](https://docs.aws.amazon.com/quicksight/latest/user/iam-actions.html)  **
  - **Description:** Grants permission to describe an extension
  - **Resource types (\*required):** [extension\*](#list_quicksight-resource-extension)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeExtensionAccess](https://docs.aws.amazon.com/quicksight/latest/user/iam-actions.html)  **
  - **Description:** Grants permission to describe an extension access
  - **Resource types (\*required):** [extensionaccess\*](#list_quicksight-resource-extensionaccess)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeExtensionPermissions](https://docs.aws.amazon.com/quicksight/latest/user/iam-actions.html)  **
  - **Description:** Grants permission to describe the permissions of an extension
  - **Resource types (\*required):** [extension\*](#list_quicksight-resource-extension)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeQuickIndexCapacity](https://docs.aws.amazon.com/quicksight/latest/user/iam-actions.html)  **
  - **Description:** Grants permission to describe index capacity
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetAnonymousUserEmbedUrl](https://docs.aws.amazon.com/quicksight/latest/user/iam-actions.html)  **
  - **Description:** Grants permission to get a URL used to embed a QuickSight Dashboard for a user not registered with QuickSight
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetAuthCode](https://docs.aws.amazon.com/quicksight/latest/user/iam-actions.html)  **
  - **Description:** Grants permission to get an auth code representing a QuickSight user
  - **Resource types (\*required):** [user\*](#list_quicksight-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCustomPermissionsSummary](https://docs.aws.amazon.com/quicksight/latest/user/iam-actions.html)  **
  - **Description:** Grants permission to get information about the custom permissions in an account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetGroupMapping](https://docs.aws.amazon.com/quicksight/latest/user/iam-actions.html)  **
  - **Description:** Grants permission to use Amazon QuickSight, in Enterprise edition, to identify and display the Microsoft Active Directory (Microsoft Active Directory) directory groups that are mapped to roles in Amazon QuickSight
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListCustomPermissionAssignments](https://docs.aws.amazon.com/quicksight/latest/user/iam-actions.html)  **
  - **Description:** Grants permission to list assignment information of the custom permission profile in an account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCustomerManagedKeys](https://docs.aws.amazon.com/quicksight/latest/user/key-management.html)  **
  - **Description:** Grants permission to list all registered customer managed keys
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDlpLabels](https://docs.aws.amazon.com/quick/latest/userguide/data-loss-prevention.html)  **
  - **Description:** Grants permission to list sensitivity labels available from a DLP provider
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListExtensionAccesses](https://docs.aws.amazon.com/quicksight/latest/user/iam-actions.html)  **
  - **Description:** Grants permission to list extension accesses
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListExtensions](https://docs.aws.amazon.com/quicksight/latest/user/iam-actions.html)  **
  - **Description:** Grants permission to list extensions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListKMSKeysForUser](https://docs.aws.amazon.com/quicksight/latest/user/key-management.html)  **
  - **Description:** Grants permission to list a user's KMS keys
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListUsersIndexCapacity](https://docs.aws.amazon.com/quicksight/latest/user/iam-actions.html)  **
  - **Description:** Grants permission to list users index capacity
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [PassDataSet](https://docs.aws.amazon.com/quicksight/latest/APIReference/qs-api-overview.html)  **
  - **Description:** Grants permission to use a dataset for a template
  - **Resource types (\*required):** [dataset\*](#list_quicksight-resource-dataset)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Access level:** Read

- **   [PassDataSource](https://docs.aws.amazon.com/quicksight/latest/APIReference/qs-api-overview.html)  **
  - **Description:** Grants permission to use a data source for a data set
  - **Resource types (\*required):** [datasource\*](#list_quicksight-resource-datasource)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Access level:** Read

- **   [PassTopic](https://docs.aws.amazon.com/quicksight/latest/APIReference/qs-api-overview.html)  **
  - **Description:** Grants permission to use a topic for a template
  - **Resource types (\*required):** [topic\*](#list_quicksight-resource-topic)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_quicksight-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_quicksight-aws_TagKeys)
  - **Access level:** Read

- **   [QuickSuiteUsageMetrics](https://docs.aws.amazon.com/quicksight/latest/user/iam-actions.html)  **
  - **Description:** Grants permission to get QuickSuite usage metrics
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [RegisterCustomerManagedKey](https://docs.aws.amazon.com/quicksight/latest/user/key-management.html)  **
  - **Description:** Grants permission to register a customer managed key
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [RemoveCustomerManagedKey](https://docs.aws.amazon.com/quicksight/latest/user/key-management.html)  **
  - **Description:** Grants permission to remove a customer managed key
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [ScopeDownPolicy](https://docs.aws.amazon.com/quicksight/latest/user/accessing-data-sources.html)  **
  - **Description:** Grants permission to manage scoping policies for permissions to AWS resources
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [SearchDirectoryGroups](https://docs.aws.amazon.com/quicksight/latest/user/iam-actions.html)  **
  - **Description:** Grants permission to use Amazon QuickSight, in Enterprise edition, to display your Microsoft Active Directory directory groups so that you can choose which ones to map to roles in Amazon QuickSight
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [SearchUsers](https://docs.aws.amazon.com/quicksight/latest/user/iam-actions.html)  **
  - **Description:** Grants permission to search the QuickSight users belonging to this account
  - **Resource types (\*required):** [user\*](#list_quicksight-resource-user)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [SetGroupMapping](https://docs.aws.amazon.com/quicksight/latest/user/iam-actions.html)  **
  - **Description:** Grants permission to use Amazon QuickSight, in Enterprise edition, to display your Microsoft Active Directory directory groups so that you can choose which ones to map to roles in Amazon QuickSight
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartDlpJob](https://docs.aws.amazon.com/quick/latest/userguide/data-loss-prevention.html)  **
  - **Description:** Grants permission to start a DLP evaluation job
  - **Resource types (\*required):** [dlpSetting\*](#list_quicksight-resource-dlpSetting)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartExtensionInstallation](https://docs.aws.amazon.com/quicksight/latest/user/iam-actions.html)  **
  - **Description:** Grants permission to start installation of an extension
  - **Resource types (\*required):** [extension\*](#list_quicksight-resource-extension)
  - **Condition keys:**  
  - **Access level:** Write

- **   [Subscribe](https://docs.aws.amazon.com/quicksight/latest/user/iam-actions.html)  **
  - **Description:** Grants permission to subscribe to Amazon QuickSight, and also to allow the user to upgrade the subscription to Enterprise edition
  - **Resource types (\*required):** 
  - **Condition keys:** [quicksight:DirectoryType](#list_quicksight-quicksight_DirectoryType)<br />[quicksight:Edition](#list_quicksight-quicksight_Edition)
  - **Access level:** Write

- **   [UnpublishFlow](https://docs.aws.amazon.com/quicksight/latest/user/iam-actions.html)  **
  - **Description:** Grants permission to unpublish a flow
  - **Resource types (\*required):** [flow\*](#list_quicksight-resource-flow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [Unsubscribe](https://docs.aws.amazon.com/quicksight/latest/user/iam-actions.html)  **
  - **Description:** Grants permission to unsubscribe from Amazon QuickSight, which permanently deletes all users and their resources from Amazon QuickSight
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateChatConfiguration](https://docs.aws.amazon.com/quicksight/latest/user/iam-actions.html)  **
  - **Description:** Grants permission to update chat configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateEmailCustomizationTemplate](https://docs.aws.amazon.com/quicksight/latest/user/customizing-quicksight-email-templates.html)  **
  - **Description:** Grants permission to update a QuickSight email customization template
  - **Resource types (\*required):** [emailCustomizationTemplate\*](#list_quicksight-resource-emailCustomizationTemplate)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateExtension](https://docs.aws.amazon.com/quicksight/latest/user/iam-actions.html)  **
  - **Description:** Grants permission to update an extension
  - **Resource types (\*required):** [extension\*](#list_quicksight-resource-extension)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateExtensionAccess](https://docs.aws.amazon.com/quicksight/latest/user/iam-actions.html)  **
  - **Description:** Grants permission to update an extension access
  - **Resource types (\*required):** [extensionaccess\*](#list_quicksight-resource-extensionaccess)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateExtensionPermissions](https://docs.aws.amazon.com/quicksight/latest/user/iam-actions.html)  **
  - **Description:** Grants permission to update the permissions of an extension
  - **Resource types (\*required):** [extension\*](#list_quicksight-resource-extension)
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [UpdateQuickIndexCapacity](https://docs.aws.amazon.com/quicksight/latest/user/iam-actions.html)  **
  - **Description:** Grants permission to update index capacity
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateResourcePermissions](https://docs.aws.amazon.com/quicksight/latest/user/security_iam_service-with-iam.html)  **
  - **Description:** Grants permission to update resource-level permissions in QuickSight
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write



## Resource types defined by Amazon QuickSight
<a name="list_quicksight-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [account](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_AccountInfo.html)  | arn:${Partition}:quicksight:${Region}:${Account}:account/${ResourceId} |   | 
|  [actionconnector](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ActionConnectorDetail.html)  | arn:${Partition}:quicksight:${Region}:${Account}:action-connector/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_) | 
|  [agent](https://docs.aws.amazon.com/quicksight/latest/user/iam-actions.html)  | arn:${Partition}:quicksight:${Region}:${Account}:agent/${ResourceId} |   | 
|  [analysis](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_Analysis.html)  | arn:${Partition}:quicksight:${Region}:${Account}:analysis/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_) | 
|  [app](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_AppSummary.html)  | arn:${Partition}:quicksight:${Region}:${Account}:app/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_) | 
|  [approvalPolicy](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ApprovalPolicy.html)  | arn:${Partition}:quicksight:${Region}:${Account}:approval-policy/${ResourceId} |   | 
|  [assetBundleExportJob](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_StartAssetBundleExportJob.html)  | arn:${Partition}:quicksight:${Region}:${Account}:asset-bundle-export-job/${ResourceId} |   | 
|  [assetBundleImportJob](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_StartAssetBundleImportJob.html)  | arn:${Partition}:quicksight:${Region}:${Account}:asset-bundle-import-job/${ResourceId} |   | 
|  [assignment](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_IAMPolicyAssignment.html)  | arn:${Partition}:quicksight::${Account}:assignment/${ResourceId} |   | 
|  [automation](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_Automation.html)  | arn:${Partition}:quicksight:${Region}:${Account}:automation-group/${AutomationGroupId}/automation/${ResourceId} |   | 
|  [automationGroup](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_AutomationGroup.html)  | arn:${Partition}:quicksight:${Region}:${Account}:automation-group/${ResourceId} |   | 
|  [automationJob](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_AutomationJob.html)  | arn:${Partition}:quicksight:${Region}:${Account}:automation-group/${AutomationGroupId}/automation/${AutomationId}/job/${ResourceId} |   | 
|  [brand](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_BrandDetail.html)  | arn:${Partition}:quicksight:${Region}:${Account}:brand/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_) | 
|  [customization](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_AccountCustomization.html)  | arn:${Partition}:quicksight:${Region}:${Account}:customization/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_) | 
|  [custompermissions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CustomPermissions.html)  | arn:${Partition}:quicksight:${Region}:${Account}:custompermissions/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_) | 
|  [dashboard](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_Dashboard.html)  | arn:${Partition}:quicksight:${Region}:${Account}:dashboard/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_) | 
|  [dashboardSnapshotJob](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DashboardSnapshotJob.html)  | arn:${Partition}:quicksight:${Region}:${Account}:dashboard/${DashboardId}/snapshot-job/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_) | 
|  [dataset](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DataSet.html)  | arn:${Partition}:quicksight:${Region}:${Account}:dataset/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_) | 
|  [datasource](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DataSource.html)  | arn:${Partition}:quicksight:${Region}:${Account}:datasource/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_) | 
|  [dlpSetting](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateDlpSetting.html)  | arn:${Partition}:quicksight:${Region}:${Account}:dlpsetting/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_) | 
|  [emailCustomizationTemplate](https://docs.aws.amazon.com/quicksight/latest/user/customizing-quicksight-email-templates.html)  | arn:${Partition}:quicksight:${Region}:${Account}:email-customization-template/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_) | 
|  [extension](https://docs.aws.amazon.com/quicksight/latest/user/iam-actions.html)  | arn:${Partition}:quicksight:${Region}:${Account}:extension/${ResourceId} |   | 
|  [extensionaccess](https://docs.aws.amazon.com/quicksight/latest/user/iam-actions.html)  | arn:${Partition}:quicksight:${Region}:${Account}:extension-access/${ResourceId} |   | 
|  [flow](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_Flow.html)  | arn:${Partition}:quicksight:${Region}:${Account}:flow/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_) | 
|  [folder](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_Folder.html)  | arn:${Partition}:quicksight:${Region}:${Account}:folder/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_) | 
|  [group](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_Group.html)  | arn:${Partition}:quicksight:${Region}:${Account}:group/${ResourceId} |   | 
|  [ingestion](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_Ingestion.html)  | arn:${Partition}:quicksight:${Region}:${Account}:dataset/${DatasetId}/ingestion/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_) | 
|  [knowledgeBase](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_KnowledgeBase.html)  | arn:${Partition}:quicksight:${Region}:${Account}:knowledge-base/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_) | 
|  [limitsProfile](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_LimitsProfile.html)  | arn:${Partition}:quicksight:${Region}:${Account}:limits-profile/${ResourceId} |   | 
|  [namespace](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_NamespaceInfoV2.html)  | arn:${Partition}:quicksight:${Region}:${Account}:namespace/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_) | 
|  [oauthClientApplication](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_OAuthClientApplication.html)  | arn:${Partition}:quicksight:${Region}:${Account}:oauthClientApplication/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_) | 
|  [refreshschedule](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_RefreshSchedule.html)  | arn:${Partition}:quicksight:${Region}:${Account}:dataset/${DatasetId}/refresh-schedule/${ResourceId} |   | 
|  [space](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_Space.html)  | arn:${Partition}:quicksight:${Region}:${Account}:space/${ResourceId} |   | 
|  [template](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_Template.html)  | arn:${Partition}:quicksight:${Region}:${Account}:template/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_) | 
|  [theme](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_Theme.html)  | arn:${Partition}:quicksight:${Region}:${Account}:theme/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_) | 
|  [topic](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_TopicDetails.html)  | arn:${Partition}:quicksight:${Region}:${Account}:topic/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_) | 
|  [user](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_User.html)  | arn:${Partition}:quicksight:${Region}:${Account}:user/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_) | 
|  [vpcconnection](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_VPCConnection.html)  | arn:${Partition}:quicksight:${Region}:${Account}:vpcConnection/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_quicksight-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon QuickSight
<a name="list_quicksight-policy-keys"></a>

Amazon QuickSight defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by tag keys | ArrayOfString | 
|   [quicksight:AllowedEmbeddingDomains](https://docs.aws.amazon.com/quicksight/latest/user/embedded-dashboards-for-authenticated-users-step-1.html)  | Filters access by the allowed embedding domains | ArrayOfString | 
|   [quicksight:DirectoryType](https://docs.aws.amazon.com/quicksight/latest/user/security-scp.html)  | Filters access by the user management options | String | 
|   [quicksight:Edition](https://docs.aws.amazon.com/quicksight/latest/user/security-scp.html)  | Filters access by the edition of QuickSight | String | 
|   [quicksight:Group](https://docs.aws.amazon.com/quicksight/latest/user/iam-actions.html)  | Filters access by QuickSight group ARN | ARN | 
|   [quicksight:IamArn](https://docs.aws.amazon.com/quicksight/latest/user/iam-actions.html)  | Filters access by IAM user or role ARN | ARN | 
|   [quicksight:KmsKeyArns](https://docs.aws.amazon.com/quicksight/latest/user/key-management.html)  | Filters access by KMS key ARNs | ArrayOfARN | 
|   [quicksight:SessionName](https://docs.aws.amazon.com/quicksight/latest/user/iam-actions.html)  | Filters access by session name | String | 
|   [quicksight:UserName](https://docs.aws.amazon.com/quicksight/latest/user/iam-actions.html)  | Filters access by user name | String | 