

# Use Amplify backends across apps (Gen 1 apps only)
<a name="reuse-backends"></a>

**Note**  
The information in this section is for Gen 1 apps only. If you want to share backend resources for a Gen 2 app, see [Share resources across branches](https://docs.amplify.aws/nextjs/deploy-and-host/fullstack-branching/share-resources/) in the *Amplify docs*

Amplify enables you to reuse existing backend environments across all of your Gen 1 apps in a given region. You can do this when you create a new app, connect a new branch to an existing app, or update an existing frontend to point to a different backend environment.

## Reuse backends when creating a new app
<a name="reuse-backends-create-connect"></a>

**To reuse a backend when creating a new Amplify app**

1. Sign in to the AWS Management Console and open the [Amplify console](https://console.aws.amazon.com/amplify/).

1. To create a new backend to use for this example, do the following:

   1. In the navigation pane, choose **All apps**.

   1. Choose **New app**, **Build an app**.

   1. Enter a name for your app, such as **Example-Amplify-App**.

   1. Choose **Confirm deployment**.

1. To connect a frontend to your new backend, choose the **Hosting environments** tab.

1. Choose your git provider, and then choose **Connect branch**.

1. On the **Add repository branch** page, for **Recently updated repositories**, choose your repository name. For **Branch**, select the branch from your repository to connect.

1. On the **Build settings**, page do the following:

   1. For **App name**, select the app to use for adding a backend environment. You can choose the current app or any other app in the current region.

   1. For **Environment**, select the name of the backend environment to add. You can use an existing environment or create a new one.

   1. By default, full-stack CI/CD is turned off. Turning off full-stack CI/CD causes the app to run in *pull only* mode. At build time, Amplify will automatically generate the `aws-exports.js` file only, without modifying your backend environment.

   1. Select an existing service role to give Amplify the permissions it requires to make changes to your app backend. If you need to create a service role, choose **Create new role**. For more information about creating a service role, see [Adding a service role with permissions to deploy backend resources](amplify-service-role.md).

   1. Choose **Next**.

1. Choose **Save and deploy**.

## Reuse backends when connecting a branch to an existing app
<a name="reuse-backends-connect-branch"></a>

**To reuse a backend when connecting a branch to an existing Amplify app**

1. Sign in to the AWS Management Console and open the [Amplify console](https://console.aws.amazon.com/amplify/).

1. Choose the app to connect a new branch to.

1. In the navigation pane, choose **App Settings**, **General**.

1. In the **Branches** section, choose **Connect a branch**.

1. On the **Add repository branch** page, for **Branch**, select the branch from your repository to connect.

1. For **App name**, select the app to use for adding a backend environment. You can choose the current app or any other app in the current region.

1. For **Environment**, select the name of the backend environment to add. You can use an existing environment or create a new one.

1. If you need to set up a service role to give Amplify the permissions it requires to make changes to your app backend, the console prompts you to perform this task. For more information about creating a service role, see [Adding a service role with permissions to deploy backend resources](amplify-service-role.md).

1. By default, full-stack CI/CD is turned off. Turning off full-stack CI/CD causes the app to run in *pull only* mode. At build time, Amplify will automatically generate the `aws-exports.js` file only, without modifying your backend environment.

1. Choose **Next**.

1. Choose **Save and deploy**.

## Edit an existing frontend to point to a different backend
<a name="reuse-backends-edit-existing"></a>

**To edit a frontend Amplify app to point to a different backend**

1. Sign in to the AWS Management Console and open the [Amplify console](https://console.aws.amazon.com/amplify/).

1. Choose the app to edit the backend for.

1. Choose the **Hosting environments** tab.

1. Locate the branch to edit and choose **Edit**.  
![The location of the Edit link for a branch in the Amplify console.](http://docs.aws.amazon.com/amplify/latest/userguide/images/amplify_edit_backend.png)

1. On the **Select a backend environment to use with this branch** page, for **App name**, select the frontend app that you want to edit the backend environment for. You can choose the current app or any other app in the current region.

1. For **Backend environment**, select the name of the backend environment to add.

1. By default, full-stack CI/CD is enabled. Uncheck this option to turn off full-stack CI/CD for this backend. Turning off full-stack CI/CD causes the app to run in *pull only* mode. At build time, Amplify will automatically generate the `aws-exports.js` file only, without modifying the backend environment.

1. Choose **Save**. Amplify applies these changes the next time you build the app.