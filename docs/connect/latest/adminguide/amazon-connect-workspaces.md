# Set up workspaces for your admin website users

###### What are workspaces?

A workspace is a collection of UI configurations that include:

- Customized page layouts, created with the View designer
- Custom pages
- Custom visual themes
  **Creating workspaces**

###### Note

Pre-requisite: Security profile permission is required. From a Security profile, go to **Users and Permissions** to give access to the workspace resource.

To create a new workspace:

1. Open the Amazon Connect admin website.
2. Navigate to **UI Management** > **Workspaces**.
3. Click **Add new workspace**.
4. Provide a name and description for your workspace.
5. Identify the pages that are provided in this workspace.
   1. Use existing Connect page — choose from the list of eligible Connect pages, which will grow as more UIs are supported by Views.

   ###### Note

   Connect provides a default home dashboard page, which will display to all users that do not have a workspace with an alternative. 2. Set page with custom page slug — identify a page name for the menu, a unique, user-friendly identifier (slug) for the URL, and the view that contains the desired page contents.

   ###### Note

   Up to 17 custom pages can be set up per instance.

6. Assign the workspace to the desired audience.
   1. Visible to all users — provide organization-wide access.
   2. Visible to assigned users — restrict to one or more users and/or routing profiles.
   3. Visible to no users — for testing and preparation, or retiring a workspace.

7. Optionally customize theme and branding elements.
   1. Logo, font and color scheme can be updated to match your branding.

###### How workspaces relate to other assignments

Workspaces can result in changes to the left navigation menu, and the contents that render on certain pages.

The settings that cause pages and contents to differ from user to user are:

- **Workspace assignment** — this determines if pages supported by Views are included in the left navigation menu. Custom UIs and the home dashboard page are not listed in Security profiles, and therefore are not shown or hidden based on those settings.

###### Note

Views may contain components, such as third party applications, that require Security profile permission. If a View opens but individual components do not render, check their configuration.

- **Security Profile assignment** — this is the traditional way to determine which Amazon Connect managed pages appear in the left navigation menu. This applies to user interfaces that are not powered by Views.

###### Note

To determine if a page is powered by Views or not, open a workspace and initiate the addition of a page. The list of eligible pages only includes those powered by Views.
Other considerations to keep in mind:

- **Page contents** can vary if the page is powered by Views. For example the home dashboard page can show different contents to Sales than it does to IT.

###### Note

All Amazon Connect pages do not support multiple Views. Amazon Connect managed pages have the same layout and components, with only slight variations based on user permissions, for example an **Add** button that appears only to entitled users.

- **Granular access control** can be applied to workspaces using tag-based access control (TBAC). This is useful if access needs to be restricted to certain records but not others, for example the workspace used by the Security team should not be visible to any other team member.

###### Employ best practices

Always preview changes in a limited-access workspace before deploying to large groups of users.

###### Note

After saving a workspace, refresh to see the changes.

###### Note

To minimize disruption to users, a workspace can only be deleted if it is not assigned to any user.

###### Accessing a workspace

After a workspace has been assigned to a user, it is visible in their header. If a user only has one workspace assigned, it opens automatically. If no custom workspace has been created or assigned, users will see the default Amazon Connect experience. Users **assigned to more than one** workspace can switch between assigned workspaces from the header control. Their last-used workspace will open by default in the next session.
