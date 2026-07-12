This guide provides documentation for AWS Wickr. For Wickr
Enterprise, which is the on-premises version of Wickr, see [Enterprise Administration Guide](../enterpriseadminguide/what-is-wickr.md "../enterpriseadminguide/what-is-wickr.md").

# Troubleshoot login and registration issues

This section helps you troubleshoot common login and registration issues
with AWS Wickr. If the steps below don't resolve your issue, contact your
Wickr network administrator.

###### Topics

- [Before you begin](#troubleshoot-enduser-before "#troubleshoot-enduser-before")
- [Common login issues](#troubleshoot-enduser-common "#troubleshoot-enduser-common")
- [Registration issues](#troubleshoot-enduser-registration "#troubleshoot-enduser-registration")
- [Reset your password](#troubleshoot-enduser-password-reset "#troubleshoot-enduser-password-reset")
- [Collect logs for your administrator](#troubleshoot-enduser-logs "#troubleshoot-enduser-logs")
- [Desktop keychain or secure store errors](#troubleshoot-enduser-keychain "#troubleshoot-enduser-keychain")

## Before you begin

Verify the following before troubleshooting:

- You are using the correct Wickr product for your organization:
  **AWS Wickr**,
  **AWS WickrGov** (GovCloud), or
  **Wickr Enterprise** (self-hosted).
  Ask your administrator if you're not sure.
- You are running a supported client version. To check, open Wickr
  and choose **Settings**,
  **About**. To update, see
  [Check for
  updates](updates.md "updates.md").
- Your device meets
  [system
  requirements](system-requirements.md "system-requirements.md").
- Your internet connection is active.

## Common login issues

### "Incorrect password" or credentials rejected

1. Check for typos, extra spaces, and caps lock.
2. If your organization uses SSO (Okta, Microsoft Entra ID, or
   another identity provider), reset your password through your
   SSO portal – not through Wickr.
3. If you don't use SSO, see
   [Reset your password](#troubleshoot-enduser-password-reset "#troubleshoot-enduser-password-reset").
4. If the issue persists, contact your Wickr network
   administrator.

### "Cannot reach server" or connection errors

1. Verify your internet connection is active.
2. Try switching networks – use cellular data instead of
   WiFi, or vice versa.
3. If you are on VPN, try disconnecting temporarily.
4. Restart the Wickr app.
5. If the issue persists on a corporate network, contact your
   network administrator – Wickr may be blocked by a
   firewall or proxy.

### "Account not found" or "User not found"

1. Verify you are signing in to the correct Wickr product
   (AWS Wickr vs. WickrGov vs. Enterprise).
2. Verify your username or email is entered correctly.
3. Contact your Wickr network administrator – your
   account may need to be re-added to the network.

### "Account suspended"

Your account has been suspended, either by your administrator or due
to multiple failed login attempts.

- If suspended due to failed login attempts, wait 24 hours for
  automatic unlock, or try resetting your password (see
  [Reset your password](#troubleshoot-enduser-password-reset "#troubleshoot-enduser-password-reset")).
- Contact your Wickr network administrator to lift the
  suspension.

### Login fails on mobile but works on desktop

1. Verify you are entering the correct password.
2. Try cellular data – disable WiFi and try again. If
   cellular works but WiFi doesn't, the issue is your network
   configuration.
3. Check that Wickr has necessary device permissions.
4. Uninstall and reinstall AWS Wickr from your app store.

###### Note

Reinstalling deletes local message history.

## Registration issues

### "This user belongs to a different network"

1. Verify you are using the correct client:
   **AWS Wickr** for commercial,
   **WickrGov** for GovCloud, or
   **Wickr Enterprise** for
   self-hosted.
2. Download the correct client from the
   [AWS Wickr
   downloads page](https://aws.amazon.com/wickr/download/ "https://aws.amazon.com/wickr/download/").
3. If you're not sure which product your organization uses,
   contact your administrator.

### Email verification not received

1. Check your spam or junk folder.
2. Verify the email address you entered is correct.
3. Return to the login screen and choose the option to resend
   the verification email.
4. If you still don't receive it, contact your administrator
   – your organization's email filters may be blocking
   emails from AWS Wickr.

## Reset your password

###### Note

If your organization uses SSO (Okta, Microsoft Entra ID, or another
identity provider), reset your password through your SSO portal –
not through Wickr.

###### Important

Resetting your Wickr password is a **full
account reset**. This action permanently deletes all local
message history, removes you from all rooms, and clears your device
registration. You will need to be re-invited to any rooms you
previously participated in. This action cannot be undone. Only reset
your password if you have exhausted all other options (verify caps
lock, check saved passwords, try another device). If you are unsure,
contact your network administrator before proceeding.

For Wickr-managed accounts (non-SSO):

1. On the Wickr login screen, choose
   **Forgot password?**
2. Enter the email address associated with your account.
3. Check your inbox for a password reset email. Check spam/junk
   folders if not received within a few minutes.
4. Choose the password reset link in the email. The link expires
   after 24 hours.
5. Enter and confirm a new password that meets your organization's
   complexity requirements.

Your Wickr network administrator manages password complexity settings. By
default, Wickr requires a minimum 8-character password with no additional
character type requirements. If you experience issues, contact your network
administrator for your network's specific settings.

## Collect logs for your administrator

Your administrator or AWS Support may ask you to collect logs. Follow
the steps for your platform.

### Desktop

If you can access the Wickr menu:

1. Open Wickr and choose the menu (☰), then
   **Support**,
   **Support Logging**.
2. Toggle on **Allow Support Logging**.
3. Reproduce the issue.
4. Return to **Support** and choose
   **Save Logs**. Send the file to your
   administrator.

If you can't reach the menu – for example, if the issue occurs
before sign-in completes – launch the client with the
`-logging` flag:

- **macOS:** Open Terminal and
  run:

```
"/Applications/WickrPro.app/Contents/MacOS/WickrPro" -logging
```

- **Windows:** Open the context menu for the
  AWS Wickr shortcut, choose **Properties**,
  then the **Shortcut** tab. Append
  `-logging` to the **Target** path
  (outside the quotation marks). Launch the shortcut.
- **Linux:** Open a terminal and
  run:

```
/opt/AWS\ Wickr/AWS\ Wickr -logging
```

### Mobile

1. Open Wickr and choose **Settings**,
   **About**,
   **Export All Logs**.
2. Send the exported log file to your administrator.

## Desktop keychain or secure store errors

Wickr uses your operating system's secure credential store (Credential
Manager on Windows, Keychain on macOS, or Secret Service on Linux) to protect
your login credentials. If you see errors related to the keychain, secure store,
or saved credentials, try the following steps in order.

1. **Restart the Wickr client.** Close
   Wickr completely and reopen it. This resolves most one-time keychain
   access failures, including "SYSTEM SECURITY DELAY" prompts.
2. **Sign out of and back into your operating
   system.** Log out of your OS user session (not Wickr) and
   log back in. This resolves issues caused by password changes,
   OS updates, sleep/wake cycles, or fast user switching.
3. **Restart your device.** A full restart
   clears transient session state that can prevent Wickr from accessing
   the secure store.

If the issue persists after all three steps, the problem is with your
device's credential store rather than Wickr. Contact your IT team or refer
to your platform's documentation.

###### Note

If other applications on your device also have trouble accessing saved
credentials, the issue is with your operating system's credential store
or an enterprise policy — not with Wickr. Contact your IT
administrator.
