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
  The AMS Advanced console has these features:

- Opening page: The opening page has information boxes and links to facilitate your access
  to your existing RFCs, incidents, service request, and reports.
- Feature pages, links in the left-hand navigation pane:
  - **Dashboard**: Provides an overview of the current status of your
    account including:
    - **Requests for change**: See how many RFCs are
      **Awaiting your response**, and jump to the RFC list page with that filter active.
      See how many RFCs are **Awaiting your approval**, and jump to the RFC list page with that
      filter active. See how many RFCs are **Open**, and jump to the RFC list page with that
      filter active. Open the list page for RFCs by clicking the **View all**
      link.
    - **Incidents**: See how many incident cases are
      **Awaiting your response**, and jump to the incident list page with that filter active.
      See and how many are **Open**, and jump to the incident list page with that filter
      active. Open the incident list page by clicking the **View all** link.
    - **Service requests**: See how many service requests are
      **Awaiting your response**, and jump to the service request list page with that filter
      active. See and how many are **Open**, and jump to the service request list page with
      that filter active. Open the service request list page by clicking the **View all**
      link.
    - **Recently updated RFCs**: Date, link to the RFC details, and status
    - **Recently created incidents and service requests**:
      Date, link to the case details, and type (incident or service request)

  - **RFCs**: Opens a list of the existing RFCs for the account
  - **Incidents**: Opens a list of the open incidents for the account
  - **Service requests**: Opens a list of the open service requests for the
    account
  - **Reports**: Opens the Reports page and the default reports,
    **Daily Backup** and **Daily Patch** and
    **Monthly Billling**
  - **Resources**:
    - **VPCs**: Opens a list of the existing VPCs for the account
    - **Stacks**: Opens a list of existing stacks for the account
    - **AMIs**: Opens a list of available AMS AMIs

- **Feature spotlight**: Information on the latest updates to the console
- **Developer's Resources**: A page of downloadable files, including the
  AMS Advanced change management SDK and more
- **Documentation**: The AWS Managed Services documentation landing page
