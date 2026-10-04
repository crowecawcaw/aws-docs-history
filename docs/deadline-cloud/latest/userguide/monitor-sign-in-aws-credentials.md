

# Sign in to the desktop monitor with the AWS Management Console or an AWS profile
<a name="monitor-sign-in-aws-credentials"></a>

You usually sign in to the AWS Deadline Cloud monitor desktop application with a monitor URL and an AWS IAM Identity Center user. If you access Deadline Cloud with AWS Identity and Access Management (IAM) credentials instead of a monitor URL, you can use two more sign-in methods. These methods require the desktop application version 1.3.0 or later:

[Sign in with the AWS Management Console](#monitor-sign-in-console)  
The monitor opens your web browser so that you can approve the sign-in with your console identity, and then creates a profile from the resulting credentials.

[Sign in with an existing AWS profile](#monitor-sign-in-local-profile)  
The monitor lists the profiles from your AWS config file. Sign in with a profile that you already use with the AWS Command Line Interface (AWS CLI) or other tools.

With either method, the monitor shows the farms, queues, and fleets that your IAM identity has permission to access. You don't need a monitor URL or an IAM Identity Center user.

For the Deadline Cloud tools that can use a console sign-in profile, see [Tool support for console sign-in profiles](#monitor-console-tool-support).

## Sign in with the AWS Management Console
<a name="monitor-sign-in-console"></a>

Before you begin, make sure that your IAM role or user has the `signin:AuthorizeOAuth2Access` and `signin:CreateOAuth2Token` permissions. To grant both, attach the [SignInLocalDevelopmentAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/SignInLocalDevelopmentAccess.html) managed policy. Without these permissions, the browser shows an error page instead of an approval prompt and the sign-in can't complete.

If you plan to submit jobs from inside a host application such as Maya or Blender, use the latest version of that submitter.

**To sign in with the AWS Management Console**

1. Open the Deadline Cloud monitor desktop application. If the sign-in page shows a list of profiles, choose **Create new Profile**.

1. For **Select Login Method**, choose **Login with AWS Console**.  
![The Select Login Method page with Login with AWS Console selected instead of Monitor URL.](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/images/monitor/monitor-console-select-login-method.png)

1. For **AWS Region**, select the Region that contains your farm, and then choose **Next**.

1. Enter a profile name or keep the default, and then choose **Next**.

1. Review the profile details. To make Deadline Cloud tools such as the Deadline CLI and the submitters use this profile, select **Set this profile as default for Deadline Cloud tools**. Then choose **Create and launch**.

1. Your default web browser opens the AWS authorization page. If you aren't signed in to the AWS Management Console in that browser, sign in first. Approve the request, and then return to the monitor. The monitor creates the profile and opens.

If you sign in to an existing profile name with a different AWS identity, the monitor shows both identities. It then asks you to confirm before overwriting the stored credentials. To keep both identities, cancel and create a second profile with a different name instead.

## Tool support for console sign-in profiles
<a name="monitor-console-tool-support"></a>

The monitor, the Deadline client that the monitor bundles, the `deadline` command-line client that the Deadline Cloud submitter installer installs, and the Deadline Cloud submitters all support console sign-in profiles.

Use the latest version of each submitter. An older submitter reports that sign-in is needed even though the monitor is signed in, and signing in again through the monitor doesn't change the result. If you see that, update the submitter.

If you installed the Deadline CLI into your own Python environment, add the required dependency with `pip install "deadline[console]"`.

## How console sign-in credentials work
<a name="monitor-console-credentials"></a>

When you sign in with the AWS Management Console, the monitor writes the profile to your AWS config file (`~/.aws/config` on Linux and macOS, `%USERPROFILE%\.aws\config` on Windows) and caches the credentials under `~/.aws/login/cache/`. The monitor uses the same locations as the `aws login` command, so other AWS tools can use the profile by name. For the Deadline Cloud tools that support these profiles, see [Tool support for console sign-in profiles](#monitor-console-tool-support).

If you set the profile as the default for Deadline Cloud tools, the monitor also records the profile name in `~/.deadline/config`, so the Deadline CLI and the Deadline Cloud submitters use it without a `--profile` option.

The credentials are short-term. While the monitor is running, it automatically renews them before they expire. The renewal happens about every 15 minutes and exchanges a stored refresh token. The renewal doesn't depend on your browser session, so it continues after you sign out of the AWS Management Console. When the monitor isn't running, the credentials expire. When you open the monitor again, it renews them from the stored refresh token, or opens your browser to sign in again if the session can no longer be renewed.

When you sign out of a console profile in the monitor, the monitor deletes the cached credentials for that profile.

## Sign in with an existing AWS profile
<a name="monitor-sign-in-local-profile"></a>

The sign-in page of the desktop monitor lists the profiles from your AWS config file, including profiles that you created with the `aws configure` command or other tools. You can sign in with any listed profile whose credentials can access Deadline Cloud.

A profile must meet the following requirements to be used:
+ The profile appears in the AWS config file. A profile that exists only in the shared credentials file (`~/.aws/credentials`) isn't listed.
+ The profile sets a `region`. A profile without a Region appears in the list but can't be selected until you add one.

**To sign in with an existing AWS profile**

1. Open the Deadline Cloud monitor desktop application.

1. On the sign-in page, under **Select a profile to continue**, choose your profile from the list. Profiles that the monitor didn't create are labeled **Local Profile**.  
![The sign-in page profile list, each entry labeled as a monitor profile, an AWS Console Profile, or a Local Profile.](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/images/monitor/monitor-local-profile-list.png)

1. Choose **Next**.

The monitor resolves the profile's credentials through the standard AWS credential provider chain, the same way the AWS CLI does. The monitor only reads the profile and doesn't change it, so credential renewal and expiry work the same as they do for your other tools.