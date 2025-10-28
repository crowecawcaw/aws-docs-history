# Using the AMS console

The AMS console is available for you to interact with ECO. The console behaves similarly to other AWS consoles. However, only
EDI on AWS enabled accounts can access the AMS console for EDI. After EDI is deployed in your account, you can search for
**Managed Services** in the uniﬁed search bar to access the AMS console.

The console is account speciﬁc. So, if you're in a "Test" account for your organization, you can't see resources in the "Prod" account
for the organization.

When you authenticate, the console applies an IAM policy that determines which console you can access and what you can do there. Your administrator might
apply additional statements to the default policy to restrict what you can see and do in the console.

The console has the following features:

- Opening page – Has information and a **Get started** text box with a link to the **Dashboard** that
  includes the following information:
  - **Incidents on your resources** – Has a button to open an incident case in AWS Support Center, and shows how many incident cases are
    open, waiting for approval and require your attention
  - **Compliance status** – Links to the **Rules and Resources** page that shows are noncompliant and compliant
    rules and resources
  - **Service requests** – Has a button to open a service request case in AWS Support Center, and shows how many cases are open,
    waiting for approval and require your attention
  - **Account-level security** – Links to details on real-time threat detection findings from GuardDuty and data security and privacy
    findings from Macie
  - **Quick actions** – Links to **Go to backup vaults** and **Create patch maintenance window**

- Feature pages in the left-hand navigation pane:
  - **Dashboard** – Includes the preceding information
  - **Reports** – Opens a page with links to your current ECO reports
  - **Configuration** – Opens a page with links to common AMS configuration tasks
  - **Documentation** – Opens the [AWS Managed Services Documentation landing page](../../../managedservices.md "../../../managedservices.md")
