# Opting out of Generative BI

Quick accounts are charged if Generative BI is active in the account.
Generative BI is considered active if your account uses any of the following
capabilities:

- Pro users
- Topics
- Dashboard and visual indexing
- Dashboard Q&A
  To avoid being charged for Generative BI by completely deactivating it, perform the
  following steps.

###### Warning

Opting out of Generative BI will disable AI-powered features and stop related charges.
This process involves:

- Removing or changing Pro user roles to standard roles
- Deleting all topics in your account
- Disabling dashboard indexing and Q&A features
  **Before proceeding:** Review the steps carefully and ensure
  you understand which features will be disabled.

###### To opt out of Generative BI

1. Ensure there are no Pro users or user groups mapped to Pro roles in the
   account by performing the following steps:
   - To update or remove Pro users using APIs:
     - If you use Quick identity (with or without IAM
       federation):
       1. Find users that have Pro roles using the [ListUsers](../../../quicksight/latest/APIReference/API_ListUsers.md "../../../quicksight/latest/APIReference/API_ListUsers.md") API.
       2. Either change the users' roles using the [UpdateUser](../../../quicksight/latest/APIReference/API_UpdateUser.md "../../../quicksight/latest/APIReference/API_UpdateUser.md") API, or remove the users from
          the account using the [DeleteUser](../../../quicksight/latest/APIReference/API_DeleteUser.md "../../../quicksight/latest/APIReference/API_DeleteUser.md") API.

     - If you use IAM Identity Center or Microsoft Active Directory:
       1. Find group of users mapped to Pro roles using the
          [ListRoleMemberships](../../../quicksight/latest/APIReference/API_ListRoleMemberships.md "../../../quicksight/latest/APIReference/API_ListRoleMemberships.md") API.
       2. Create new user groups with the same users, but mapped
          to different roles, using the [CreateRoleMemberships](../../../quicksight/latest/APIReference/API_CreateRoleMemberships.md "../../../quicksight/latest/APIReference/API_CreateRoleMemberships.md") API.
       3. Delete the previous user groups mapped to Pro roles
          using the [DeleteRoleMemberships](../../../quicksight/latest/APIReference/API_DeleteRoleMemberships.md "../../../quicksight/latest/APIReference/API_DeleteRoleMemberships.md") API.

   - To update or remove Pro users using the Quick
     console:
     1. Open the [Quick console](https://quicksight.aws.amazon.com/ "https://quicksight.aws.amazon.com/").
     2. Choose the profile icon, then choose **Manage
        Quick**.
     3. If necessary, in the left navigation pane, choose
        **Manage users**.
        - If you use Quick identity (with or without
          IAM federation), update user roles or delete users
          using the steps in [Viewing Amazon Quick account details](managing-user-access-qs-iam.md#view-user-accounts "managing-user-access-qs-iam.md#view-user-accounts") or [Deleting a Amazon Quick user account](managing-user-access-qs-iam.md#delete-a-user-account "managing-user-access-qs-iam.md#delete-a-user-account").
        - If you use IAM Identity Center or Microsoft Active Directory, update
          group and role mappings or delete user groups using the
          steps in [Managing user access](managing-user-access-idc.md#view-user-accounts-enterprise "managing-user-access-idc.md#view-user-accounts-enterprise").

2. Ensure there are no topics in the account by performing the following
   steps:
   1. Use the [ListTopics](../../../quicksight/latest/APIReference/API_ListTopics.md "../../../quicksight/latest/APIReference/API_ListTopics.md") API to list all topics in the account for each
      AWS Region where topics are used.
   2. For each topic, do one of the following:
      - If you are an owner or co-owner of the topics, delete the
        topics using the [DeleteTopic](../../../quicksight/latest/APIReference/API_DeleteTopic.md "../../../quicksight/latest/APIReference/API_DeleteTopic.md") API.
      - If you're not an owner or co-owner of the topics:
        - Identify the owners of each topic using the [DescribeTopicPermissions](../../../quicksight/latest/APIReference/API_DescribeTopicPermissions.md "../../../quicksight/latest/APIReference/API_DescribeTopicPermissions.md") API, then ask them
          to delete their topics using the [DeleteTopic](../../../quicksight/latest/APIReference/API_DeleteTopic.md "../../../quicksight/latest/APIReference/API_DeleteTopic.md") API.
        - Make yourself a co-owner of the topics using the
          [UpdateTopicPermissions](../../../quicksight/latest/APIReference/API_UpdateTopicPermissions.md "../../../quicksight/latest/APIReference/API_UpdateTopicPermissions.md") API , then delete
          the topics using the [DeleteTopic](../../../quicksight/latest/APIReference/API_DeleteTopic.md "../../../quicksight/latest/APIReference/API_DeleteTopic.md") API.

3. Ensure that dashboard and visual indexing and Dashboard Q&A are disabled
   by performing the following steps:
   - To disable dashboard and visual indexing and Dashboard Q&A using
     APIs:
     1. Disable dashboard and visual indexing using the [UpdateQuickSightQSearchConfiguration](../../../quicksight/latest/APIReference/API_UpdateQuickSightQSearchConfiguration.md "../../../quicksight/latest/APIReference/API_UpdateQuickSightQSearchConfiguration.md") API.
     2. Disable Dashboard Q&A using the [UpdateDashboardsQAConfiguration](../../../quicksight/latest/APIReference/API_UpdateDashboardsQAConfiguration.md "../../../quicksight/latest/APIReference/API_UpdateDashboardsQAConfiguration.md") API.

   - To disable dashboard and visual indexing and Dashboard Q&A using
     the Quick console:
     1. Open the [Quick console](https://quicksight.aws.amazon.com/ "https://quicksight.aws.amazon.com/").
     2. Choose the profile icon, then choose **Manage
        Quick**.
     3. Under the **Account** section, choose
        **Amazon Q**.
     4. Disable each of the options.
