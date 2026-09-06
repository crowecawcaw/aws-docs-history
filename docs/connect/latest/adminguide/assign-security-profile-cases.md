

# Security profile permissions for Connect Customer Cases
<a name="assign-security-profile-cases"></a>

This topic describes the security profiles permissions that are required to access and use Connect Customer Cases. For a list of Cases permissions and their API name, see [List of security profile permissions in Connect Customer](security-profile-list.md).

## Required Cases permissions
<a name="required-cases-permissions"></a>

The following image shows the security permissions used to manage access to [Connect Customer Cases](cases.md) functionality:

![Cases security profile permissions.](http://docs.aws.amazon.com/connect/latest/adminguide/images/SecurityProfile_cloudscape_cases.png)


## Required Customer Profiles permissions
<a name="required-cases-cp-permissions"></a>

To use Connect Customer Cases, your users also need permissions to Customer Profiles permissions, as shown in the following image.

![Customer Profiles security profile permissions.](http://docs.aws.amazon.com/connect/latest/adminguide/images/cases-customer-profiles-permissions.png)


## Required queue, quick connect, and user view permissions
<a name="required-cases-queue-permissions"></a>

To be able to assign case ownership to users or queues, agents need permissions to view queues, quick connects, and users. To be able to view the author name on comments, agents need permission to view users. These permissions are shown in the following two images. 

![Queue and quick connect View permissions.](http://docs.aws.amazon.com/connect/latest/adminguide/images/cases-security-queue-permissions.png)


![User View permissions.](http://docs.aws.amazon.com/connect/latest/adminguide/images/cases-security-user-permissions.png)


## Description of Cases permissions
<a name="case-permissions-description"></a>
+ **Audit History**: Manage who can access the audit history of cases in the agent application.
  + **View Audit History**: Allows the user to view the audit history of cases in the agent application.
+ **Cases**: Manage who can access cases by using the agent application.
  + **View case**: Allows the user to view and search cases in the agent application. This includes viewing case data (for example, status, title, summary), contact history (for example, calls, chats, tasks with information such as start time, end time, duration), and comments.
  + **Edit case**: Allows the user to edit cases, which includes editing case data (for example, update case status), add comments, and associate contacts to cases.
  + **Create case**: Allows the user to create new cases, and associate contacts to cases.
  + **Delete case**: Allows the user to delete any case in the domain.
+ **My Cases**: Manage if the user can delete cases that they created.
  + **Delete case**: Allows the user to delete cases that they created.
+ **Case Fields**: Manage who can configure case fields by using the Connect Customer admin website.
  + **View Case Fields**: Allows users to view the case fields page and all of the existing case fields (could be system or custom).
  + **Edit Case Fields**: Allows users to edit any of the case fields (for example, change title, description, single-select options).
  + **Create Case Fields**: Allows users to create new case fields.
+ **Case Templates**: Manage who can configure case templates by using the Connect Customer admin website.
  + **View Case Templates**: Allows users to view the case templates page and all of the existing case templates.
  + **Edit Case Templates**: Allows users to edit any of the case templates.
  + **Create Case Templates**: Allows users to create new case templates.
+ **Case Comments**: Manage who can edit or delete comments on any case, regardless of who authored them.
  + **Edit Case Comment**: Allows the user to edit any comment on a case.
  + **Delete Case Comment**: Allows the user to delete any comment on a case.
+ **My Case Comments**: Manage if the user can edit or delete comments that they authored.
  + **Edit Case Comment**: Allows the user to edit comments that they authored.
  + **Delete Case Comment**: Allows the user to delete comments that they authored.
+ **Case Custom Related Items**: Manage who can edit or delete custom related items on any case, regardless of who created them.
  + **Edit Case Custom Related Item**: Allows the user to edit any custom related item on a case.
  + **Delete Case Custom Related Item**: Allows the user to delete any custom related item from a case.
+ **My Case Custom Related Items**: Manage if the user can edit or delete custom related items that they created.
  + **Edit Case Custom Related Item**: Allows the user to edit custom related items that they created.
  + **Delete Case Custom Related Item**: Allows the user to delete custom related items that they created.
+ **Case Contacts**: Manage who can remove contact associations (calls, chats, tasks, emails) from any case, regardless of who associated the contact.
  + **Delete Case Contact**: Allows the user to remove any contact associated with a case.
+ **My Case Contacts**: Manage if the user can remove contact associations that they created.
  + **Delete Case Contact**: Allows the user to remove contact associations that they created.
+ **Cases Export**: Manage who can export cases from the agent workspace.
  + **Export** (`Cases.Export`): Allows the user to select cases in the case search view and download them as a CSV file. Enabling this permission automatically grants **View case** if it is not already granted.
+ **Case Files**: Manage who can remove files attached to cases.
  + **Delete Case File**: Allows the user to delete any file attached to a case.

When users have permissions to **View Case Fields** and **View Case Templates**, they will see the **Case fields** and **Case templates** options in their left navigation menu, as shown in the following image: 

![The navigation menu, the agent applications option.](http://docs.aws.amazon.com/connect/latest/adminguide/images/cases-agent-application-case-fields-menu.png)


## Required Agent Application permissions
<a name="required-agent-application-permissions"></a>

To be able to generate a summary for a case in the agent application, agents need permission to view AI agents in the agent application, as shown in the following image.

![Screenshot showing AI agent permissions in security profile.](http://docs.aws.amazon.com/connect/latest/adminguide/images/case-summary-ai-agent-permissions.png)


## Required Cases and Agent Applications permissions to generate AI-powered case summarization
<a name="required-cases-agent-app-ai-summary-permissions"></a>

To generate an AI-powered case summary, agents need View permissions on Cases and Audit History, and View permissions on Connect Assistant under Agent Applications.

**To save an AI-powered case summary, agents additionally need Edit permission on Cases.**

![Cases permissions.](http://docs.aws.amazon.com/connect/latest/adminguide/images/cases-permissions.png)


![Agent Applications permissions.](http://docs.aws.amazon.com/connect/latest/adminguide/images/agent-applications-permissions.png)
