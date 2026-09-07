

This guide documents the new AWS Wickr administration console, released on March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide-classic/what-is-wickr.html).

# Troubleshoot login and registration issues
<a name="troubleshoot-enduser"></a>

This section helps you troubleshoot login and registration issues with AWS Wickr. If the steps in this section don't resolve your issue, open a case in the [AWS Support Center](https://console.aws.amazon.com/support/home).

**Topics**
+ [Before you begin](#troubleshoot-enduser-before)
+ [Common login issues](#troubleshoot-enduser-common)
+ [Registration issues](#troubleshoot-enduser-registration)
+ [Password reset](#troubleshoot-enduser-password-reset)
+ [Account suspension](#troubleshoot-enduser-suspension)
+ [Collecting logs](#troubleshoot-enduser-logs)

## Before you begin
<a name="troubleshoot-enduser-before"></a>

Verify the following before troubleshooting login or registration issues:
+ You are using the correct Wickr product for your organization: **AWS Wickr**, **AWS WickrGov** (GovCloud), or **Wickr Enterprise** (self-hosted). If you're unsure, contact your network administrator.
+ You are running a supported client version. AWS Wickr supports the current version and the previous 2–3 versions. To check your version, open Wickr and choose **Settings**, **About**. To update, see [Check for updates](https://docs.aws.amazon.com/wickr/latest/userguide/updates.html).
+ You have the correct authentication method for your organization (SSO or non-SSO).
+ You have saved your user password and Wickr recovery key in a secure location.
+ Your network allows communication with required [Wickr domains and ports](https://docs.aws.amazon.com/wickr/latest/adminguide/allow-list-ports-domains.html).
+ Your device meets [system requirements](https://docs.aws.amazon.com/wickr/latest/userguide/system-requirements.html).

**Tip**  
If you encounter an error during login or registration, capture a screenshot of the error message before troubleshooting. This helps your administrator or AWS Support diagnose the issue faster.

## Common login issues
<a name="troubleshoot-enduser-common"></a>

When login fails, the error message determines the troubleshooting path. Start by identifying which error you see.

### "Incorrect password" or credentials rejected
<a name="troubleshoot-enduser-password"></a>

1. Verify you are entering the correct password. Check for typos, extra spaces, and caps lock.

1. If you use SSO (Okta, Microsoft Entra ID, , Amazon Cognito), reset your password through your identity provider — not through Wickr.

1. If you use Wickr-managed credentials, see [Password reset](#troubleshoot-enduser-password-reset).

### "Cannot reach server" or connection errors
<a name="troubleshoot-enduser-connection"></a>

This indicates a network issue, not an account issue.

1. Verify your internet connection is active.

1. Switch networks — try cellular data instead of WiFi, or vice versa.

1. If on a corporate network, ask your IT team to verify that [required Wickr domains and ports](https://docs.aws.amazon.com/wickr/latest/adminguide/allow-list-ports-domains.html) are allowed.

1. If on VPN, try disconnecting temporarily.

1. If the issue persists, [collect logs](#troubleshoot-enduser-logs) and contact your network administrator.

### "Account not found" or "User not found"
<a name="troubleshoot-enduser-not-found"></a>

1. Verify you are signing in to the correct Wickr product (AWS Wickr vs. WickrGov vs. Enterprise).

1. Verify your username or email is entered correctly.

1. Your account may have been removed from the network. Contact your network administrator.

### "Account suspended"
<a name="troubleshoot-enduser-suspended-ref"></a>

See [Account suspension](#troubleshoot-enduser-suspension).

### "This user belongs to a different network"
<a name="troubleshoot-enduser-different-network-ref"></a>

1. You may have accidentally created an account on a different Wickr network (see [Guest user issue](#troubleshoot-enduser-guest)).

1. Verify you are using the correct Wickr client for your organization.

1. Contact your network administrator. The administrator may need to contact AWS Support with your email address and Network ID to resolve the conflict.

### Login fails on mobile but works on desktop
<a name="troubleshoot-enduser-mobile"></a>

1. Verify you are entering the correct password.

1. Test on cellular data — disable WiFi and try again. If cellular works but WiFi doesn't, the issue is your network configuration. Contact your IT team.

1. Check that the Wickr app has necessary device permissions.

1. Uninstall and reinstall AWS Wickr from your app store.

**Note**  
Reinstalling deletes local message history.

### Other login errors
<a name="troubleshoot-enduser-other"></a>

If your error is not listed above:

1. Verify you are entering the correct password.

1. Capture a screenshot of the error message.

1. [Collect logs](#troubleshoot-enduser-logs) for your platform.

1. Contact your network administrator with the screenshot and logs.

## Registration issues
<a name="troubleshoot-enduser-registration"></a>

### Guest user issue
<a name="troubleshoot-enduser-guest"></a>

**Symptom:** After signing up, you see a "Guest Network" screen and cannot see other users in your organization's contacts.

**Cause:** You initiated sign-up directly instead of completing registration through an invitation from your administrator. This creates a guest user account instead of joining your organization's network.

**Resolution:**

1. Contact your network administrator.

1. The administrator must delete the guest user account, then re-invite you to the correct network.

1. Complete registration using the invitation link or code from your administrator.

### "This user belongs to a different network"
<a name="troubleshoot-enduser-different-network"></a>

**Cause:** You accidentally created an account on a different Wickr network, or you are using the wrong client.

1. Verify you are using the correct client: **AWS Wickr** for commercial networks, **WickrGov** for GovCloud, or **Wickr Enterprise** for self-hosted.

1. Download the correct client from the [AWS Wickr downloads page](https://aws.amazon.com/wickr/download/).

1. Contact your network administrator. The administrator may need to contact AWS Support with your email address and Network ID.

### Username format errors
<a name="troubleshoot-enduser-username"></a>

Usernames in AWS Wickr have the following requirements:
+ Usernames are **permanent** — they cannot be changed after creation.
+ The email address is the primary identifier for registration.
+ Usernames must not contain unsupported special characters. Alphanumeric characters, periods, hyphens, and underscores are generally supported.
+ For SSO-enabled networks, user creation is handled by the identity provider (IdP). Users must exist on the identity side before signing in to the Wickr client.

### Email verification not received
<a name="troubleshoot-enduser-email-verification"></a>

1. Check your spam or junk folder.

1. Verify the email address you entered is correct.

1. Contact your IT team to ensure emails from AWS Wickr are not blocked by email filters.

1. Return to the login screen and choose the option to resend the verification email.

### Invitation link expired
<a name="troubleshoot-enduser-invite-expired"></a>

**Symptom:** You choose the registration link in your invitation email, but the link does not work or registration fails.

**Cause:** Invitation links expire 21 days after your administrator sends them. If you did not register within that time, the link is no longer valid.

**Resolution:** To resolve this issue, complete the following steps.

1. Contact your network administrator and ask them to resend the invitation from the **Team directory** tab in the AWS Management Console for Wickr.

1. Complete registration within 21 days of receiving the new invitation.

## Password reset
<a name="troubleshoot-enduser-password-reset"></a>

**Note**  
For SSO-enabled accounts, password reset is managed through your identity provider (Microsoft Entra ID, Okta, Amazon Cognito, or ) — not through Wickr.

**Password reset flow (non-SSO):**

**Important**  
Resetting a Wickr password is a **full account reset**. This permanently deletes all local message history, removes the user from all rooms, and clears device registration. The user must be re-invited to rooms they previously participated in. This cannot be undone. Advise users to exhaust all other options (verify caps lock, check saved passwords, try another device) before proceeding.

1. On the Wickr login screen, choose **Forgot password?**

1. Enter the email address associated with your AWS Wickr account.

1. Check your inbox for a password reset email. Check spam/junk folders if not received within a few minutes.

1. Choose the password reset link in the email. Password reset links expire after 24 hours.

1. Enter and confirm your new password. Your password must meet the complexity requirements configured by your network administrator.

**Password complexity requirements**

Password requirements are configured by your administrator in the Admin Console under Security Group settings. Requirements can include:
+ Minimum length (at least 8 characters; admin may set higher)
+ Required count of lowercase letters
+ Required count of uppercase letters
+ Required count of numbers
+ Required count of special characters

You manage password complexity settings in the AWS Management Console for Wickr. By default, Wickr requires a minimum 8-character password with no additional character type requirements. If users experience issues, share your network's specific settings with them.

## Account suspension
<a name="troubleshoot-enduser-suspension"></a>

**Symptom:** You see an "Account suspended" error on login.

**For regular users:**

1. Contact your network administrator.

1. The administrator can lift the suspension in **Admin Console** > **Team Directory** > locate user > **Unsuspend**.

**For a single administrator (no other admin to unsuspend):**

Contact AWS Support with your email address, Network ID, and verification of administrator status.

**Account lockout due to failed login attempts:**
+ Wait 24 hours for automatic unlock, or
+ Contact your network administrator to manually unlock your account, or
+ Use the [Password reset](#troubleshoot-enduser-password-reset) flow to reset your credentials and unlock your account.

**If you cannot sign in after suspension is lifted:**

Contact AWS Support with your email address, Network ID, client version (Wickr > **Settings** > **About**), and OS version.

## Collecting logs
<a name="troubleshoot-enduser-logs"></a>

Log collection methods differ by platform. Collect logs before contacting your administrator or AWS Support.

### Desktop
<a name="troubleshoot-enduser-logs-desktop"></a>

If you can access the Wickr menu:

1. Open Wickr and choose the hamburger menu (☰), then **Support**, **Support Logging**.

1. Toggle on **Allow Support Logging**. For investigations, also enable **Extended Logging Detail**.

1. Reproduce the issue.

1. Return to **Support** and choose **Save Logs**. Share the file with your administrator.

If you cannot access the Wickr menu (for example, the client crashes at the login screen), launch the client with the `-logging` flag to generate logs:
+ **macOS:** Open Terminal and run:

  ```
  /Applications/AWS\ Wickr.app/Contents/MacOS/AWS\ Wickr -logging
  ```

  Logs are saved to `~/Library/Application Support/Wickr, LLC/Wickr Pro/logs/`.
+ **Windows:** Open the context menu for the AWS Wickr shortcut, choose **Properties**, then the **Shortcut** tab. Append `-logging` to the **Target** path (outside the quotation marks). Launch the shortcut.

  Logs are saved to `C:\Users\<USERNAME>\AppData\Local\Wickr, LLC\Wickr Pro\logs\`.
+ **Linux:** Launch from terminal with the `-logging` flag.

  Logs are saved to `~/.local/share/Wickr, LLC/Wickr Pro/logs/`.

### Mobile
<a name="troubleshoot-enduser-logs-mobile"></a>

1. Open Wickr and choose **Settings**, **About**, **Export All Logs**.

1. Share the exported log file with your administrator.

If you cannot access Settings (for example, you are stuck on the login screen):
+ **iOS:** Connect your device to a Mac, open Console.app, filter for "Wickr", and reproduce the issue.
+ **Android:** Enable USB debugging, connect to a computer, and run `adb logcat | grep -i wickr`.