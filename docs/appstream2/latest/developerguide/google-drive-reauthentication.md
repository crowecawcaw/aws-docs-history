

# Controlling Google Drive re-authentication

When you enable Google Drive as a storage connector on a stack, users authenticate with their Google account during their first streaming session. By default, this authentication persists across subsequent sessions, so users do not need to sign in again.

You can change this behavior by configuring the storage connector authentication setting at the stack level. When you configure this setting to force re-authentication, WorkSpaces Applications clears stored Google identity provider tokens when a session ends, requiring users to re-authenticate with Google Drive at the start of each new session.

Use forced re-authentication in the following situations:
+ Shared workstation environments where multiple users might access the same streaming URL
+ Security and compliance requirements that mandate per-session authentication for Google Drive access
+ Environments where users must not retain access to previously linked Google Drive storage across sessions

You can configure this setting when creating or updating a stack using the WorkSpaces Applications API. For more information about the available values and API usage, see [CreateStack](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_CreateStack.html) and [UpdateStack](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_UpdateStack.html) in the *WorkSpaces Applications API Reference*.

**Important**  
Note the following behaviors and limitations when you configure re-authentication for Google Drive:  
This setting applies at the stack level and affects all cloud storage connectors (OneDrive for Business and Google Drive) configured on the stack. You can't set different re-authentication behaviors for individual connectors.
This setting has no effect on Home Folders.
Even with forced re-authentication disabled (authentication set to persist across sessions), Google might expire or revoke credentials based on your Google Workspace admin policies, OAuth token lifetime settings, or security events. Persistent authentication doesn't guarantee a permanent sign-in—users might still be prompted to re-authenticate based on Google credential expiration policies.