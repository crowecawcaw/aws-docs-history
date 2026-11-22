

AWS Well-Architected Agent is in preview release and is subject to change.

# Preferences

The **Preferences** page in the AWS WA Agent console contains account-level settings for managing organizational agent profiles.

## Trusted access with AWS Organizations
<a name="agent-preferences-trusted-access"></a>

Trusted access with AWS Organizations is a toggle that allows AWS WA Agent to operate across your organization. Enabling trusted access is required to create [organizational profiles](agent-concepts.md#agent-concept-profiles) and [organization reports](agent-org-reports.md).

When you enable trusted access, you enable the agent's organization integration, which creates both AWS WA Agent service-linked roles: the `` role and the `` role. For details about these roles, including how they are created and deleted, see [Using service-linked roles for AWS Well-Architected](using-service-linked-roles.md).

**Important**  
If trusted access was previously enabled, you must deregister all delegated administrators before you can disable trusted access.

**To enable trusted access with AWS Organizations**

1. In the AWS WA Agent console, choose **Preferences** in the left-hand navigation.

1. Enable the **Trusted access with AWS Organizations** toggle.

## Delegated administrators
<a name="agent-preferences-delegated-admins"></a>

You can register up to five member accounts as delegated administrators for AWS WA Agent. A delegated administrator is a member account that can manage the agent on behalf of your organization. You register delegated administrators one account at a time.

Delegated administrators can take the following actions in an organizational profile:
+  Generate organizational reports 
+ Share the organizational profile with another account
+  Use Resource Policies to provide another account with permissions to edit the profile (goals and configuration) 

**Note**  
 Delegated administrators can not create organizational profiles themselves. For more detail, see [Organizational profile prerequisites](agent-getting-started.md#agent-prerequisites-orgs). 

**To register a delegated administrator**

1. In the AWS WA Agent console, choose **Preferences** in the left-hand navigation.

1. Choose **Register delegated administrator**.

1. Select an account using one of the following methods:
   + Search for the account by name, email, account ID, or OU ID.
   + Choose the account from the organizational structure dialog that shows all accounts in your organization.
**Note**  
The management account cannot be selected as a delegated administrator.

1. Choose **Register** to add the delegated administrator.

1. Repeat these steps for each additional delegated administrator, up to a maximum of 5.

### Selecting accounts from your organization
<a name="agent-select-org-accounts"></a>

When you select accounts from your organization, AWS WA Agent shows an organizational structure dialog that lists all accounts in your organization. In this dialog, you can search for accounts by name, email, account ID, or OU ID. You can also select an OU or folder to select all accounts within that OU or section.

The behavior of the dialog depends on where you open it:
+ **Preferences, delegated administrators:** You register one account at a time, and you cannot select the management account.
+ **Profile creation:** You can select multiple accounts at once, and you can select a folder or OU to include all of its accounts. For more information, see [Step 1: Enter profile details](agent-getting-started.md#agent-create-profile).