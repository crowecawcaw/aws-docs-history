# Using the AMS consoles

The AMS consoles in the AWS Management Console are available for you to interact
with AMS and operate your AMS Advanced-managed and AMS Accelerate resources. The AMS consoles generally behave
like any AWS console; however, because AMS is a private organization, only accounts
enabled for AMS can access the console. Once AMS is enabled in your account, you can
access the console by searching for "Managed Services" in the unified search bar.

###### Note

Depending on your account role, you access the AMS Advanced console or the AMS Accelerate console.

When using the AMS consoles, be aware of the following caveats:

- The AMS console is account specific. So, if you are in a "Test" account for your
  organization, you won't be able to see resources in the "Prod" account for that
  organization. Likewise, you must have an AMS Advanced role to access the AMS Advanced console.
- The AMS consoles apply an IAM policy when you authenticate that determines which console
  you can access and what you can do there. Your administrator may apply
  additional polices to the default AMS policy to restrict what you can see and
  do in the console.
  The AMS Accelerate console has these features:

- Opening page: The opening page has information boxes and links to facilitate your access
  to your incidents, service request, and reports.
- Feature pages, links in the left-hand navigation pane:
  - **Dashboard**: Provides an overview of the current status of your
    account including:
    - **Incidents on your resources**: A button for opening an incident case
      in AWS Support Center, plus how many incident cases are **Awaiting approval**
      and require your attention and how many are **Open**
    - **Compliance status**: Links to **Rules** and
      **Resources** that are noncompliant or compliant
    - **Service requests**: A button for opening a service request case
      in AWS Support Center, plus how many are **Awaiting approval**
      and require your attention and how many are **Open**
    - **Account-level security**: Links to details on
      **Real time threat detection** GuardDuty findings and
      **Data security and privacy** Macie findings
    - **Quick actions**: Open your **Backup vaults** or
      **Patch instances** configuration pages

  - **Reports**: Opens the **Reports** page and the default reports,
    **Daily Backup** and **Daily Patch** and
    **Monthly Billling**
  - **Configuration**: Ensure your resources are being managed successfully and
    according to your specifications.
    - **Install SSM agent**: The SSM agent is required
    - **Configure tagging rules**: Opens AMS Resource Tagger
    - **Configure alarms**: Opens AMS CloudWatch alarm configuration
    - **Configure patch schedule**: Opens the AWS Systems Manager console
    - **Configure patch baselines**: Opens the AWS Patch Manager console
    - **Configure backup plans**: Opens the AWS Backup console

- **Feature spotlight**: Information on the latest updates to the console
- **Documentation**: The AWS Managed Services documentation landing page
