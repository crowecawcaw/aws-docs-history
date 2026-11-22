

# Get started with Kiro Crew on Lightsail

Kiro Crew is a persistent, open source development workspace that remembers your context, learns how you work, and coordinates across your unique tools and workflows, so you come back to progress instead of another workflow to restart. You can set up scheduled jobs, orchestrate multiple agents at the same time, and connect to messaging platforms such as Slack, Telegram, and Discord. Kiro Crew is configured to use Amazon Bedrock as its default model provider. Use Kiro Crew when you want artificial intelligence (AI) agents that keep working on your tasks on a server that you control, even after you close your browser.

This tutorial includes the following steps:
+ [Step 1: Create a Kiro Crew instance](#amazon-lightsail-kiro-crew-create-instance)
+ [Step 2: Sign in to the Kiro Crew dashboard](#amazon-lightsail-kiro-crew-sign-in-dashboard)
+ [Step 3: Sign in to Kiro](#amazon-lightsail-kiro-crew-sign-in-kiro)
+ [Step 4: Create a snapshot of your instance (optional)](#amazon-lightsail-kiro-crew-create-snapshot)
+ [Step 5: Clean up resources](#amazon-lightsail-kiro-crew-clean-up)

**Note**  
The resources that you create in this tutorial incur charges to your AWS account until you delete them. For information about Lightsail plan prices, see [Lightsail pricing](https://aws.amazon.com/lightsail/pricing/).

## Prerequisites
<a name="amazon-lightsail-kiro-crew-prerequisites"></a>

Before you begin, make sure that you have the following:
+ An AWS account with access to the Lightsail console.
+ A web browser on the device that you use to access the Kiro Crew dashboard.

## Step 1: Create a Kiro Crew instance
<a name="amazon-lightsail-kiro-crew-create-instance"></a>

In this step, you create a Lightsail instance running Kiro Crew. The instance is the server that hosts Kiro Crew and its dashboard.

**To create a Lightsail instance with Kiro Crew**

1. Open the [Lightsail console](https://lightsail.aws.amazon.com/).

1. In the **Instances** section of the Lightsail home page, choose **Create instance**.

1. Choose the AWS Region and Availability Zone for your instance.

1. Choose the image for your instance as follows:
   + Under **Select a platform**, choose **Linux/Unix**.
   + Under **Select a blueprint**, choose **Kiro Crew**.  
![Select the Kiro Crew blueprint.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/kiro-crew/blueprint_selection.png)

1. Under **Choose your instance plan**, select an instance plan with at least 8 GB of memory. If you select a plan with less than 8 GB of memory, Kiro Crew shows memory capacity warnings.
**Note**  
Kiro Crew requires an instance plan with 4 GB of memory or more.  
![Select an instance plan. The console warns that a plan smaller than 8 GB can cause memory capacity warnings.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/kiro-crew/plan_selection.png)

1. For the instance name, enter a name for your instance, or use the default name provided.
**Note**  
Instance names must be unique within your Lightsail account, 2 to 255 characters, start and end with an alphanumeric character, and contain only alphanumeric characters, periods, dashes, or underscores.

1. Choose **Create instance**.

Your instance is in a **Starting** state for a few minutes while it starts up. Wait until the status shows **Running** before you continue to the next step.

## Step 2: Sign in to the Kiro Crew dashboard
<a name="amazon-lightsail-kiro-crew-sign-in-dashboard"></a>

You manage Kiro Crew from a web dashboard. Your instance serves the dashboard over HTTPS on port 443 at the public IP address of the instance. To sign in, you generate a sign-in link from a Secure Shell (SSH) session on your instance, and then open the link in your browser.

When you connect using SSH, the terminal displays a **Getting Started** welcome message with the one-time setup steps for your instance and the URL of your dashboard. If the welcome message says that the service is still starting up, wait about a minute, and then run `lightsail-login` to display the welcome message again.

![The Kiro Crew Getting Started welcome message in the SSH terminal.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/kiro-crew/motd_welcome_message.png)


**To sign in to the Kiro Crew dashboard**

1. Open the [Lightsail console](https://lightsail.aws.amazon.com/).

1. In the **Instances** section, choose the name of your Kiro Crew instance to open the instance management page.

1. On the instance management page, choose **Connect using SSH**. A browser-based SSH terminal opens.  
![The Getting started tab of a Kiro Crew instance.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/kiro-crew/getting_started_tab.png)

1. In the SSH terminal, run the following Kiro Crew command to generate your dashboard sign-in link:

   ```
   kirocrew token
   ```

   The following example shows the format of the sign-in URL that the command prints. In the example, {{instance-public-ip}} is the public IP address of your instance, and {{access-token}} is your dashboard access token.

   ```
   https://{{instance-public-ip}}/?token={{access-token}}
   ```  
![The kirocrew token command prints the dashboard sign-in URL.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/kiro-crew/kirocrew_token.png)

1. Copy the URL.

1. Paste the URL into a new browser tab.

If the page shows a **KiroCrew is starting up** message, wait until the dashboard loads.

After you sign in, your browser keeps a session for the Kiro Crew dashboard, so you don't need to repeat these steps each time you open the dashboard. To sign in from another browser, or to get a new sign-in link at any time, connect to your instance using SSH and run `kirocrew token` again.

The default public IP address of your instance changes when you stop and start the instance. A static IP address stays the same when you stop and start the instance. For more information about IP addresses, see [View and manage IP addresses for Lightsail resources](understanding-public-ip-and-private-ip-addresses-in-amazon-lightsail.md).

## Step 3: Sign in to Kiro
<a name="amazon-lightsail-kiro-crew-sign-in-kiro"></a>

Kiro Crew uses the Kiro command line interface (CLI) to run its AI agents. The Kiro CLI is preinstalled on your instance, and you run it with the `kiro-cli` command. Kiro Crew can't run AI agents until you sign in to the Kiro CLI, so complete this step before you start working in the dashboard.

**To sign in to Kiro**

1. On the instance management page of your Kiro Crew instance, choose **Connect using SSH**. A browser-based SSH terminal opens.

1. In the SSH terminal, run the following Kiro CLI command. Your instance doesn't have a web browser, so the command uses the `--use-device-flow` option to sign you in without opening one on the instance:

   ```
   kiro-cli login --use-device-flow
   ```

1. Select a login method.  
![The Kiro CLI login method menu.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/kiro-crew/kiro_cli_login_method.png)

1. The terminal displays a code and a URL. Open the URL in a browser, confirm that the code matches the code in the terminal, and then follow the prompts in the browser to complete the sign-in.  
![The Kiro CLI device code and sign-in URL.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/kiro-crew/kiro_cli_login_code.png)

After you sign in, open the Kiro Crew dashboard to start working with your AI agents.

## Step 4: Create a snapshot of your instance (optional)
<a name="amazon-lightsail-kiro-crew-create-snapshot"></a>

Create a snapshot of your Kiro Crew instance after you complete the setup, and before you make major changes to the instance. Snapshots are point-in-time backups that let you restore your instance to a known good state. You can also create new instances of your desired plan from a snapshot.

**To create a manual snapshot**

1. Open the [Lightsail console](https://lightsail.aws.amazon.com/).

1. In the **Instances** section, choose the name of your Kiro Crew instance.

1. Choose the **Snapshots** tab.

1. Under **Manual snapshots**, choose **Create snapshot**.

1. Enter a name for your snapshot.

1. Choose **Create**.

Creating the snapshot might take a few minutes, depending on the size of your instance.

Manual snapshots incur storage charges until you delete them. For more information about snapshot charges, see [Delete unused Lightsail snapshots to avoid monthly charges](amazon-lightsail-deleting-snapshots.md).

**Did you know?**  
 Lightsail stores seven daily snapshots and automatically replaces the oldest with the newest when you enable automatic snapshots for your instance. For more information, see [ Configure automatic snapshots for Lightsail instances and disks ](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-configuring-automatic-snapshots.html) . 

For more information about snapshots, see [Back up Linux/Unix Lightsail instances with snapshots](lightsail-how-to-create-a-snapshot-of-your-instance.md).

## Step 5: Clean up resources
<a name="amazon-lightsail-kiro-crew-clean-up"></a>

When you no longer need your Kiro Crew instance, delete it and its snapshots to stop incurring charges for them. You can't undo deleting an instance or snapshot.

For instructions on deleting your resources, see the following topics:
+ For instructions on deleting your instance, see [Delete Lightsail instances](delete-an-amazon-lightsail-instance.md).
+ For instructions on deleting your snapshots, see [Delete unused Lightsail snapshots to avoid monthly charges](amazon-lightsail-deleting-snapshots.md).

## Upgrade Kiro Crew
<a name="amazon-lightsail-kiro-crew-upgrade"></a>

When a new version of Kiro Crew is available, the dashboard shows an **Update available** message. The new version installs beside the current version and switches over atomically. To approve the update, you run one command in an SSH session on your instance. The following procedure shows an update to version 0.13.0.

**To upgrade Kiro Crew**

1. Sign in to the Kiro Crew dashboard. For instructions, see [Step 2: Sign in to the Kiro Crew dashboard](#amazon-lightsail-kiro-crew-sign-in-dashboard).

1. In the **Update available** message, choose **Update to v0.13.0**.  
![The Update available message in the Kiro Crew dashboard.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/kiro-crew/upgrade_update_prompt.png)

1. The message shows the approval command, `kirocrew update approve`, and the time that remains to approve the update. The time starts at about 10 minutes. After you approve the update, its progress appears in the same message.  
![The approval command and the approval time remaining.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/kiro-crew/upgrade_approval_command.png)

1. Connect to your instance using SSH. For instructions, see [Connect to Linux or Unix instances on Lightsail](lightsail-how-to-connect-to-your-instance-virtual-private-server.md).

1. In the SSH terminal, run the following command:

   ```
   kirocrew update approve
   ```

   The command prints a message that the update is approved and that the gateway is applying the new version.  
![The output of the kirocrew update approve command.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/kiro-crew/upgrade_approve_output.png)

1. Return to the dashboard. The **Update available** message shows the progress while Kiro Crew builds the environment for the new version and installs the components that the new version needs. The message states that the dashboard keeps working while the update installs. Wait for the installation to finish, which takes a few minutes.  
![The progress of the update in the Update available message.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/kiro-crew/upgrade_progress.png)

1. When the message says that the new version is already installed, choose **Restart to update**.  
![The Restart to update button.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/kiro-crew/upgrade_restart.png)

   The dashboard shows **Updating and restarting** and then reloads. After the dashboard reloads, a dialog shows what's new in the new version and confirms that you are on the latest version.  
![The what's new dialog for version 0.13.0, which shows that you are on the latest version.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/kiro-crew/upgrade_whats_new.png)

If you aren't ready to update, choose **Remind me tomorrow** in the message. You can also start an update at any time from **Settings**, then **About**.

## Frequently asked questions (FAQ)
<a name="amazon-lightsail-kiro-crew-faq"></a>

**How do I get a new dashboard sign-in link?**

On the instance management page in the Lightsail console, choose **Connect using SSH**, and then run `kirocrew token`. The command prints a new sign-in URL that you can open in any browser.

**How do I display the setup instructions again?**

Connect to your instance using SSH and run `lightsail-login`. This command displays the **Getting Started** welcome message again, including the setup steps and your dashboard URL. To see all Kiro Crew commands, run `kirocrew --help`.

**What does running Kiro Crew on Lightsail cost?**

The following costs apply:
+ **Lightsail instance**: You pay for the instance plan that you selected (for example, the 4 GB plan). Lightsail bills plans at an on-demand hourly rate, so you pay only for what you use, up to the maximum monthly plan cost. For more information about plans, see [Lightsail instance plans](amazon-lightsail-bundles.md).
+ **Data transfer overages**: Each Lightsail plan includes a monthly data transfer allowance. If your Kiro Crew instance transfers more data out than your plan includes, you pay overage charges. For more information about data transfer allowances, see [Data transfer in Lightsail](amazon-lightsail-faq-data-transfer-allowance.md).
+ **Snapshots**: You pay for manual and automatic snapshots of your instance based on the amount of storage that they use.

For current prices, see [Lightsail pricing](https://aws.amazon.com/lightsail/pricing/).

**How does HTTPS work with my Kiro Crew instance?**

Your Kiro Crew instance serves the dashboard over HTTPS on port 443, and redirects HTTP requests on port 80 to HTTPS. When your instance is created, a built-in certificate management daemon (`lightsail-manage-certd`) issues a Let's Encrypt certificate for the public IPv4 address of your instance. You don't need to set up the certificate yourself.

**What happens when my instance's IP address changes?**

The certificate management daemon monitors the public IP address of your instance. When the IP address changes, for example when you attach or detach a static IP address, the daemon issues a new Let's Encrypt certificate for the new IP address and updates the Kiro Crew dashboard URL to match.

Kiro Crew then restarts so that the dashboard accepts connections at the new address. The welcome message also checks the dashboard URL each time you connect using SSH, and updates it if the IP address has changed.

To get a sign-in link for the new address, see [Step 2: Sign in to the Kiro Crew dashboard](#amazon-lightsail-kiro-crew-sign-in-dashboard).

**Is my dashboard access token automatically rotated?**

No. Your Kiro Crew instance doesn't rotate the dashboard access token on a schedule. When you sign in with a link from `kirocrew token`, your browser stores a cookie that keeps you signed in for up to 30 days. To sign in from another browser, or after the cookie expires, connect to your instance using SSH and run `kirocrew token` to get a new sign-in link.

**How do I check whether Kiro Crew is running?**

Connect to your instance using SSH and run the following shell command:

```
systemctl status kirocrew
```

Kiro Crew runs as the `kirocrew` system service. An Apache web server (`apache2`) on your instance receives HTTPS requests and forwards them to Kiro Crew.

**How do I restart Kiro Crew?**

Connect to your instance using SSH and run the following shell command:

```
sudo systemctl restart kirocrew
```

The dashboard is unavailable for a few moments while Kiro Crew restarts.

**Note**  
Don't use `kirocrew restart` to restart the service. On your instance, that command prompts for a password and doesn't restart Kiro Crew.

**How do I restore a Kiro Crew instance from a snapshot?**

1. Create a new instance from an existing Kiro Crew snapshot. For instructions, see [Create Lightsail instances from snapshots](lightsail-how-to-create-instance-from-snapshot.md).

1. Connect to your new instance using SSH. The welcome message updates the dashboard URL to the public IP address of the new instance.

1. Run `kirocrew token` to get a sign-in link for the new instance.

## Related resources
<a name="amazon-lightsail-kiro-crew-related-resources"></a>
+ [Back up Linux/Unix Lightsail instances with snapshots](lightsail-how-to-create-a-snapshot-of-your-instance.md)
+ [Connect to Linux or Unix instances on Lightsail](lightsail-how-to-connect-to-your-instance-virtual-private-server.md)
+ [View and manage IP addresses for Lightsail resources](understanding-public-ip-and-private-ip-addresses-in-amazon-lightsail.md)