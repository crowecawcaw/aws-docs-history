# Troubleshooting SharePoint knowledge bases

Use this section to diagnose and resolve common issues with SharePoint knowledge
base integrations.

## Sign-in errors with user-managed setup

| User-managed setup sign-in errors          | Issue                                                       | Cause                                                                                                                                                                                                                                                  | Resolution |
| ------------------------------------------ | ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- |
| "Need admin approval" error during sign-in | Your tenant restricts user consent for third-party<br>apps. | Ask a Global Administrator to grant admin consent. For more<br>information, see<br>[Admin consent for Microsoft 365](sharepoint-kb-user-managed.md#sharepoint-kb-user-admin-consent "sharepoint-kb-user-managed.md#sharepoint-kb-user-admin-consent"). |
| Sign-in window closes without completing   | Browser popup blocker or cookie settings.                   | Allow popups from the Amazon Quick domain and ensure<br>third-party cookies are enabled.                                                                                                                                                               |
| "AADSTS65004: User declined to consent"    | User chose Cancel or Deny on the consent dialog.            | Retry the sign-in and choose<br>\*_Accept_<br>• on the consent dialog.                                                                                                                                                                                 |

## Token refresh with user-managed setup

User-managed setup uses the `offline_access` scope to obtain refresh
tokens. Delegated credentials last approximately 90 days. If the refresh token
expires or is revoked (for example, by a password change, session revocation, or
admin action), syncs fail and you need to re-authenticate.

To re-authenticate:

1. Navigate to the **Knowledge bases** list page in
   Amazon Quick.
2. Locate the knowledge base that requires a refresh. In the
   **Actions** column, choose the three-dot menu and
   choose **Edit integration**.
3. The **Edit integration** dialog opens. You can
   optionally update the integration name.
4. Choose **Save and Reauthenticate**.
5. A Microsoft sign-in window opens. Complete the sign-in flow using the
   same credentials that were originally used to create the
   integration.

###### Important

When you re-authenticate, sign in using the same Microsoft 365 account
that was used during the original setup. Using different credentials might
cause issues with connected resources. The new account might have different
SharePoint permissions than the original account.

## Common errors

| Common SharePoint knowledge base errors               | Issue                                                                                                                                                    | Cause                                                                                                                                                                                                                                                                      | Resolution |
| ----------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| Unable to access KMS key                              | The KMS key ARN is incorrect, the key does not exist in the<br>specified Region, or the KMS key has not been added in the<br>Amazon Quick admin console. | Verify the KMS key ARN and Region. Confirm the KMS key<br>has been added under **Manage account**,<br>**AWS resources**,<br>**AWS Key Management Service**. Confirm<br>the key is enabled and has not been scheduled for<br>deletion. Multi-Region keys are not supported. |
| Invalid Tenant ID                                     | The Tenant ID is malformed or does not match a valid Entra<br>tenant.                                                                                    | Copy the Tenant ID directly from the Entra admin center:<br>**Microsoft Entra ID**,<br>**Overview**.                                                                                                                                                                       |
| Invalid Client ID                                     | The Client ID is incorrect or the app registration does not<br>exist.                                                                                    | Copy the Application (Client) ID from **App<br>Registrations**, your app,<br>**Overview**.                                                                                                                                                                                 |
| Certificate validation failed                         | The thumbprint does not match the certificate in Entra, or<br>the certificate has expired.                                                               | Verify the thumbprint using the base64url-encoded SHA-1 value<br>from the certificate generation step. Ensure the certificate has<br>not expired.                                                                                                                          |
| Unable to connect to SharePoint                       | One or more credentials are incorrect, or the Entra app is<br>missing required API permissions or admin consent.                                         | Review all field values. Confirm the Entra app has the correct<br>API permissions and that admin consent has been granted.                                                                                                                                                 |
| Error loading the file picker with user-managed setup | The file picker is unable to establish a connection to<br>SharePoint on behalf of the signed-in user.                                                    | Close the error message and choose \*_Add<br>content_<br>• again to retry. If the error persists,<br>close the creation dialog, reopen the flow, and sign in to<br>SharePoint again.                                                                                       |

## Check document access (ACL verification)

If you enabled ACL management, you can verify document-level access control
for individual items using the Permission Checker in sync reports. For detailed
instructions, see [Check document access (ACL verification)](sync-reports-observability.md#sync-reports-acl-verification "sync-reports-observability.md#sync-reports-acl-verification").

If you see "No access control list found" for a SharePoint document:

- Verify **Enable ACL management** is selected in the
  knowledge base's additional settings.
- Confirm the Entra app has `User.Read.All` and
  `GroupMember.Read.All` on Microsoft Graph.
- Confirm the Entra app has `Sites.FullControl.All` on the
  SharePoint resource (or `Sites.Selected` with per-site
  permissions granted).
- Re-run a full sync after fixing permissions.

## Sync monitoring and reports

For detailed information about sync schedules, sync activity, sync
reports, filtering items, and downloading reports, see
[Sync reports and observability](sync-reports-observability.md "sync-reports-observability.md").

###### Tip

To trigger a sync on demand, choose **Sync now**
on the knowledge base detail page.

## Next steps

After you resolve the issue, verify your fix by running a sync. For more
information about sync monitoring, see
[Sync reports and observability](sync-reports-observability.md "sync-reports-observability.md").
