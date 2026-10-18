

# Controlling OneDrive Re-authentication
<a name="onedrive-reauthentication"></a>

When you enable OneDrive for Business as a storage connector on a stack, users authenticate with their Microsoft account during their first streaming session. By default, this authentication persists across subsequent sessions, so users do not need to sign in again.

You can change this behavior by configuring the storage connector authentication setting at the stack level. When configured to force re-authentication, stored Microsoft identity provider tokens are cleared when a session ends, requiring users to re-authenticate with OneDrive for Business at the start of each new session.

When to use forced re-authentication:
+ Shared workstation environments where multiple users may access the same streaming URL
+ Security and compliance requirements that mandate per-session authentication for OneDrive access
+ Environments where users should not retain access to previously linked OneDrive storage across sessions

You can configure this setting when creating or updating a stack using the WorkSpaces Applications API. For details on the available values and API usage, see [CreateStack](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_CreateStack.html) and [UpdateStack](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_UpdateStack.html) in the *WorkSpaces Applications API Reference*.

**Important**  
This setting applies at the stack level and affects all cloud storage connectors (OneDrive for Business and Google Drive) configured on the stack. You cannot set different re-authentication behaviors for individual connectors.
This setting has no effect on Home Folders.
Even with forced re-authentication disabled (authentication set to persist across sessions), Microsoft may expire or revoke credentials based on your Entra ID tenant policies, token lifetime configurations, or security events. Persistent authentication does not guarantee a permanent sign-in — users may still be prompted to re-authenticate based on Microsoft's credential expiration policies.