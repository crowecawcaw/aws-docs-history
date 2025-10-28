# Restricting access to an Amplify app's branches

If you are working on unreleased features, you can password protect feature branches to restrict access to specific users. When access control is set on a branch, users are
prompted for a user name and password when they attempt to access the URL for the
branch.

You can set a password that applies to an individual branch or globally to all connected
branches. When access control is enabled at both the branch and global level, the branch level
password takes precedence over a global (application) level password.

Amplify throttles failed requests that are attempting to access password protected resources. This behavior protects applications against dictionary attacks or other attempts to read data behind access controls.

Use the following procedure to set a password to restrict access to an Amplify app's branches.

###### To set passwords on feature branches

1. Sign in to the AWS Management Console and open the [Amplify
   console](https://console.aws.amazon.com/amplify/ "https://console.aws.amazon.com/amplify/").
2. Choose the app you want to set feature branch passwords on.
3. In the navigation pane, choose **Hosting**, and then choose
   **Access control**.
4. In the **Access control settings** section, choose **Manage
   access**.
5. On the **Manage access control** page, do one of the following.
   - To set a username and password that applies to all connected branches
     1. Turn on **Manage access for all branches**. For example, if you have
        **main**, **dev**,
        and **feature** branches connected, you can apply the same username and password for all branches.

   - To set a a username and password that applies to an individual branch
     1. Turn off **Manage access for all branches**.
     2. Locate the branch that you want to manage. For **Access
        settings** choose **Restricted-password
        required**.
     3. For **Username**, enter a username.
     4. For **Password**, enter a password.

   - Choose **Save**.

6. If you are managing access control for a server-side rendered (SSR) app, redeploy the
   app by performing a new build from your Git repository. This step is required to enable
   Amplify to apply your access control settings.
