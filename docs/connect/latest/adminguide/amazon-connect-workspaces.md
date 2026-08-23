# Set up workspaces for your business users

## What are workspaces?

A workspace is a collection of user interface (UI) configurations that include:

- Customized page layouts, created with the UI builder
- Custom pages
- Custom visual themes

## Create a workspace

###### Note

Prerequisite: Security profile permission is required. From a Security profile, go to **Users and Permissions** to give access to the workspace resource.

To create a new workspace:

1. Open the Connect Customer admin website.
2. Navigate to **UI Management** > **Workspaces**.
3. Choose **Add new workspace**.
4. Provide a name and description for your workspace.
5. Identify the pages included in this workspace.

   1. Use existing Connect page – Choose from the list of eligible Connect pages, which will grow as more UIs are powered by views.

   ###### Note

   Connect Customer provides a default home page, which displays to all users who do not have a workspace with an alternative. 2. Set page with custom page slug – Identify a page name for the menu, a unique, user-friendly identifier (slug) for the URL, and the view that contains the desired page contents.

   ###### Note

   You can set up to 17 custom pages for each instance.

6. Assign the workspace to the desired audience.

   1. Visible to all users – Provide organization-wide access.
   2. Visible to assigned users – Restrict to one or more users or routing profiles.
   3. Visible to no users – Hide the workspace for testing, preparation, or retirement.

7. (Optional) Customize theme and branding elements.

   1. Update the logo, font, and color scheme to match your branding.

## How workspaces relate to other assignments

Workspaces can result in changes to the left navigation menu and the contents that render on certain pages.

The settings that cause pages and contents to differ from user to user are:

- **Workspace assignment** – This determines whether pages powered by views appear in the left navigation menu. Custom UIs and the home page are not listed in Security profiles, and therefore are not shown or hidden based on those settings.

###### Note

Views might contain components, such as third-party applications, that require Security profile permission. If a view opens but individual components do not render, check their configuration.

- **Security profile assignment** – This is the traditional way to determine which Connect Customer managed pages appear in the left navigation menu. This applies to user interfaces that are not powered by views.

###### Note

To determine if a page is powered by views or not, open a workspace and initiate the addition of a page. The list of eligible pages only includes those powered by views.

Other considerations to keep in mind:

- **Page contents** can vary if the page is powered by views. For example, the home page can show different contents to Sales than it does to IT.

###### Note

All Connect Customer pages do not support multiple Views. Connect Customer managed pages have the same layout and components, with only slight variations based on user permissions, for example, an **Add** button that appears only to entitled users.

- **Granular access control** – You can apply this to workspaces using tag-based access control (TBAC). This is useful if access needs to be restricted to certain records but not others, for example, the workspace used by the Security team should not be visible to any other team member.

## Employ best practices

Always preview changes in a limited-access workspace before deploying to large groups of users.

###### Note

After saving a workspace, refresh to see the changes.

###### Note

To minimize disruption to users, you can delete a workspace only if it is not assigned to any user.

## Access a workspace

After you assign a workspace to a user, it is visible in their header. If a user has only one workspace assigned, it opens automatically. If no custom workspace has been created or assigned, users see the default Connect Customer experience. Users **assigned to more than one** workspace can switch between assigned workspaces from the header control. Their last-used workspace opens by default in the next session.
