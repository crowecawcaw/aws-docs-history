# Configuring role-based visibility of pages

You can create roles within an App Studio app and configure the visbility of pages based on those roles. For example, you can create
roles based on user needs or access levels, such as administrator, manager, or user for apps that provide features such as project approvals or claims processing and make certain
pages visible to specific roles. In this example, administrators may
have full access, managers might have access to view reporting dashboards, and users may have access to tasks pages with input forms.

Use the following procedure to configure role-based visbility of pages in your App Studio app.

1. If necessary, navigate to the application studio of your application. From the left-side navigation menu, choose **My applications**, find
   your application and choose **Edit**.
2. Create app level roles in the application studio.
   1. Choose the **App settings** tab at the top of the application studio.
   2. Choose **+ Add Role**
   3. In **Role name**, provide a name to identify your role. We recommend using a name that is descriptive of the group's access level or duties, as you'll
      use the name to set up the page visibility.
   4. Optionally, in **Description**, add a description for the role.
   5. Repeat these steps to create as many roles as needed.

3. Configure the visiblity of your pages
   1. Choose the **Pages** tab at the top of the application studio.
   2. From the left-side **Pages** menu, choose the page for which you want to configure role-based visibility.
   3. In the right-side menu, choose the **Properties** tab.
   4. In **Visibility**, disable **Open to all end users**.
   5. Keep **Role** selected to choose from a list of the roles you created in the previous step. Choose **Custom** to write a
      JavaScript expression for more complex visibility configurations.
      1. With **Role** selected, check the boxes of the app roles for which the page will be visible.
      2. With **Custom** selected, enter a JavaScript expression that resolves to true or false. Use the following
         example to check if the current user has the role of _manager_: `{{currentUser.roles.includes('manager')}}`.

4. Now that your visibility is configured, you can test the page visiblity by previewing your app.
   1. Choose **Preview** to open a preview of your app.
   2. In the top right of the preview, choose the **Previewing as** menu and check the boxes of the roles you want to test. The
      visible pages should reflect the roles selected.

5. Now, assign groups to app roles for a published app. Group and role assignments must be configured separately for each environment. For more information about
   app environments, see [Application environments](applications-publish.md#application-environments "applications-publish.md#application-environments").

###### Note

Your app must be published to either the Testing or Production environments to assign App Studio groups to the roles you've created and configured. If necessary,
publish your app to assign groups to the roles. For more information about publishing, see [Publishing applications](applications-publish.md "applications-publish.md").

    1. In the top right of the application studio, choose **Share**.
    2. Choose the tab for the environment of which you want to configure page visibility.
    3. Choose the **Search groups** input box and choose the group with which to share the app version. You can enter text to search for groups.
    4. In the dropdown menu, choose the roles to assign to the group. You can choose **No role** to share the app version and not assign a role to the group. Only
     pages that are visible to all users will be visible to groups with no role.
    5. Choose **Share**. Repeat these steps to add as many group as needed.
