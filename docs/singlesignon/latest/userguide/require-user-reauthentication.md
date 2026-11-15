

# Require user re-authentication
<a name="require-user-reauthentication"></a>

User re-authentication is a setting on your external identity provider (IdP) configuration in IAM Identity Center. By default, it's set to **Not required**: when a user's IAM Identity Center session expires, IAM Identity Center renews it through the user's existing IdP session, and the user isn't prompted to sign in to the AWS access portal again.

When user re-authentication is set to **Required** and a user's [user interactive session](user-interactive-sessions.md) expires, IAM Identity Center prompts the user to authenticate with your external IdP again. This applies only to service provider (SP)-initiated sign-ins, where users sign in to AWS through your AWS access portal URL.

Set user re-authentication to **Required** when your security or compliance requirements call for users to prove their identity at the start of every IAM Identity Center session. To request re-authentication, IAM Identity Center adds the SAML 2.0 `ForceAuthn` attribute to the SAML request that it sends to your IdP when a user signs in through the AWS access portal.

To complete the steps on this page, you need an instance of IAM Identity Center that's connected to an external IdP as its identity source. For more information, see [External identity providers](manage-your-identity-source-idp.md). Review [Considerations for requiring user re-authentication](#require-user-reauthentication-considerations) on this page before you change the setting.

AWS CloudTrail logs changes to this setting. To audit them, filter on the event name `UpdateExternalIdPConfigurationForDirectory`. For more information, see [Logging IAM Identity Center API calls with AWS CloudTrail](logging-using-cloudtrail.md).

In the CloudTrail event, the setting appears in `requestParameters.idpSAMLConfig` as `forceAuthn`, with the value `ENABLED` when user re-authentication is required.

The following example shows the relevant fields of a CloudTrail event in which an administrator set user re-authentication to **Required**.

```
{
  "eventName": "UpdateExternalIdPConfigurationForDirectory",
  "eventSource": "sso-directory.amazonaws.com",
  "requestParameters": {
    "idpSAMLConfig": {
      "forceAuthn": "ENABLED"
    }
  }
}
```

## Setting user re-authentication for an external IdP
<a name="set-user-reauthentication"></a>

**To set user re-authentication to Required**

1. Open the [IAM Identity Center console](https://console.aws.amazon.com/singlesignon).

1. Choose **Settings**.

1. On the **Settings** page, choose the **Identity source** tab. In the **Sign-in** section, choose **Manage authentication**.

1. On the **User sign-in configurations** card, next to **Require user re-authentication**, choose **Edit**.

1. Under **User re-authentication**, select one of the following:

   1. **Require** – Users must authenticate with your IdP each time their IAM Identity Center session expires, even if they have an active IdP session.

   1. **Do not require** – Users stay signed in as long as they have an active IdP session. This is the default.

1. Choose **Save changes**.

Expected result: On the **Identity source** tab, **Require user re-authentication** shows **Required** or **Not required**, depending on the option that you selected.

**Note**  
The change applies to new SP-initiated sign-ins, which start from your AWS access portal URL. Sessions that are active when you save aren't interrupted or ended.

## Testing user re-authentication
<a name="test-user-reauthentication"></a>

After you set user re-authentication to **Required**, you can confirm that it works by signing in as a test user, or as an existing user whose credentials you have. Sessions that were active before you changed the setting aren't affected, so you can test without interrupting other users.

**To test user re-authentication**

1. Open your AWS access portal URL (for example, `https://d-xxxxxxxxxx.awsapps.com/start`) and sign in through your external IdP.

1. On the navigation bar of the AWS access portal, choose **Sign out**.

1. On the same page, choose **Sign in**.

Expected result: Your IdP's sign-in page opens and asks you to authenticate, even though you have an active IdP session.

If you aren't prompted to authenticate, see [Users are not prompted to re-authenticate after you require re-authentication](troubleshooting.md#issue-force-reauthentication) before you contact AWS Support.

## Considerations for requiring user re-authentication
<a name="require-user-reauthentication-considerations"></a>

Review the following before you change this setting.
+ External IdP compatibility – This setting works only if your external identity provider (IdP) honors the `ForceAuthn` attribute in the SAML requests that IAM Identity Center sends. Check your IdP's documentation to confirm that it supports `ForceAuthn`, and turn it on if your IdP requires it. For known IdP-specific issues, including Okta and Google Workspace, see [Users are not prompted to re-authenticate after you require re-authentication](troubleshooting.md#issue-force-reauthentication).
+ This setting applies only to sign-ins that start from the AWS access portal – If your users start from your IdP's own portal or application dashboard, that's an IdP-initiated sign-in. IAM Identity Center doesn't send a SAML request for those sign-ins, so this setting has no effect on them.
+ More sign-in prompts – Your users enter credentials, and complete multi-factor authentication if your IdP requires it, each time their IAM Identity Center session expires. Your session duration determines how often that happens, so review it at the same time you change this setting. See [Configure the session duration in IAM Identity Center](configure-user-session.md). Changing this setting doesn't interrupt sessions that are already active; to end those, see [View and end active sessions for your workforce users](end-active-sessions.md).