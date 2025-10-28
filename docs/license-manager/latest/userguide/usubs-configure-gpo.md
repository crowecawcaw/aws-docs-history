# Configure Active Directory GPO for more active

remote user sessions

By default, Microsoft RDS allows a maximum of two user sessions at the same time on an EC2
Windows instance that provides user-based subscription products. After you've configured your
RDS License Server endpoints, you can configure Microsoft RDS to allow more than two user sessions
at the same time with an Active Directory Group Policy Object (GPO), as follows.

###### Prerequisite

You must have created a license server in your environment. To create a license
server, see [Step 3: Configure RDS license
server](user-based-subscriptions-getting-started.md#usubs-configure-rds "user-based-subscriptions-getting-started.md#usubs-configure-rds").

1. The tool that you use to configure your GPO depends on where you run it from,
   as follows:

Central configuration from your domain controller

Log into your Active Directory domain controller as an administrator,
and open the Windows Group Policy Management Console.

Configure group policy on the session host

Log into your License Server as an administrator, and open the
Local Group Policy Editor. 2. From the management console or policy editor, edit the group policy to specify
the session hosts that connect through Microsoft RDS. You can find the endpoint
for your RDS License Server in the License Manager product details page, or with the
[list-license-server-endpoints](../../../cli/latest/reference/license-manager-user-subscriptions/list-license-server-endpoints.md "../../../cli/latest/reference/license-manager-user-subscriptions/list-license-server-endpoints.md") command in the AWS CLI. 3. Set the licensing mode for the Remote Desktop Session Host to `Per User`,
and save.
For more information about configuring your RDS License Server for License Manager, see
[Step 3: Configure RDS license
server](user-based-subscriptions-getting-started.md#usubs-configure-rds "user-based-subscriptions-getting-started.md#usubs-configure-rds") in the Get
started topic. For more information about configuration for Microsoft RDS session hosts, see
[License Remote Desktop session hosts](https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/rds-license-session-hosts "https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/rds-license-session-hosts").
