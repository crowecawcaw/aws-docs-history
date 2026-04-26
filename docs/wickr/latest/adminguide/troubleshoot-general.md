This guide documents the new AWS Wickr administration console, released on
March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic
Administration Guide](../adminguide-classic/what-is-wickr.md "../adminguide-classic/what-is-wickr.md").

# Troubleshoot general issues for AWS Wickr

The following are troubleshooting tips to help you solve general issues for
AWS Wickr.

###### Topics

- [Prerequisites](#prerequisites-general "#prerequisites-general")
- [Collect diagnostic information](#diagnostic-info "#diagnostic-info")
- [Common error messages](#general-error-messages "#general-error-messages")

## Prerequisites

Before troubleshooting AWS Wickr issues, verify the following:

- You are using AWS Wickr with a current, supported client version.
- Your device meets [System
  requirements for AWS Wickr](../userguide/system-requirements.md "../userguide/system-requirements.md").
- Your network allows required [Ports and
  domains for your Wickr network](allow-list-ports-domains.md "allow-list-ports-domains.md").

## Collect diagnostic information

**Client logs**

Client logs are essential for troubleshooting most AWS Wickr issues.

Complete the following procedure to collect client logs.

1. Sign in to the Wickr client.
2. In the navigation pane, choose the menu (three lines or dots), and then choose **Support**.
3. Choose **Support Logging**.
4. Choose **Save Logs**.
5. Note the location where logs are saved.

**Log locations by platform:**

- **Windows**: `C:\Users\<USERNAME>\AppData\Local\Wickr, LLC\Wickr Pro\logs\`
- **macOS**: `~/Library/Application Support/Wickr, LLC/Wickr Pro/logs/`
- **Linux**: `~/.local/share/Wickr, LLC/Wickr Pro/logs/`
- **iOS**: Export through Support Logging menu
- **Android**: Export through Support Logging menu

**Information to collect**

When troubleshooting or contacting support, collect:

- **Device information**: Model, OS version
- **Client version**: Found in Settings, under **About**
- **Network ID**: Found in Admin Console under **Network Settings**
- **Error message**: Exact text or screenshot
- **Timestamp**: When the issue occurred
- **Reproduction steps**: How to recreate the issue
- **Client logs**: From Support Logging menu

## Common error messages

**Unable to connect to Wickr servers.**

Possible causes:

- Network connectivity issue
- Firewall blocking Wickr traffic
- VPN or proxy interference

**Resolution**

1. Test on cellular data vs corporate WiFi to isolate network issues.
2. Review network requirements.
3. Contact your IT team to allowlist required domains and ports.

**This user belongs to a different network.**

Possible cause: User account exists on a different Wickr network

**Resolution**

1. Verify you're using the correct AWS Wickr client version.
2. Contact your network administrator.
3. If issue persists, contact AWS Support with user email and Network ID.

**Account suspended**

Possible cause: Multiple failed login attempts or administrator action

**Resolution**

1. Contact your network administrator to lift potential suspension.
2. If you are the only administrator, contact AWS Support.

**Email verification required**

Possible cause: Email verification not completed during registration.

**Resolution**

1. Check spam/junk folders for verification email.
2. Verify email address is correct.
3. Check with your IT team about email filtering.
4. Request new verification email from login screen.
