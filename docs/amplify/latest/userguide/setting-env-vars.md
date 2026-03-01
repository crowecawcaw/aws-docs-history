# Setting environment variables

Use the following instructions to set environment variables for an application in the Amplify console.

###### Note

**Environment variables** is visible in the Amplify console’s
**App settings** menu only when an app is set up for continuous
deployment and connected to a git repository. For instructions on this type of deployment,
see [Getting started with existing code](getting-started.md "getting-started.md").

###### To set environment variables

1. Sign in to the AWS Management Console and open the [Amplify console](https://console.aws.amazon.com/amplify/ "https://console.aws.amazon.com/amplify/").
2. In the Amplify console, choose **Hosting**, and then choose
   **Environment variables**.
3. On the **Environment variables** page, choose **Manage
   variables**.
4. For **Variable**, enter your key. For **Value**,
   enter your value. By default, Amplify applies the environment variables across all
   branches, so you don’t have to re-enter variables when you connect a new
   branch.
5. (Optional) To customize an environment variable specifically for a branch, add a
   branch override as follows:
   1. Choose **Actions** and then choose **Add variable
      override**.
   2. You now have a set of environment variables specific to your branch.

6. Choose **Save**.

## Create a new backend environment with authentication parameters for social sign-in

###### To connect a branch to an app

1. Sign in to the AWS Management Console and open the [Amplify
   console](https://console.aws.amazon.com/amplify/ "https://console.aws.amazon.com/amplify/").
2. The procedure for connecting a branch to an app varies depending on whether you
   are connecting a branch to a new app or an existing app.
   - **Connecting a branch to a new app**
     1. On the **Build settings** page, locate the
        **Select a backend environment to use with this
        branch** section. For **Environment**,
        choose **Create new environment**, and enter the name of
        your backend environment. The following screenshot shows the
        **Select a backend environment to use with this
        branch** section of the **Build settings**
        page with `backend` entered for the backend
        environment name.

     ![The Select a backend environment to use with this branch section of the Build settings page.](images/amplify-newenvironment-1.png) 2. Expand the **Advanced settings** section on the
     **Build settings** page and add environment variables
     for social sign-in keys. For example,
     `AMPLIFY_FACEBOOK_CLIENT_SECRET` is a valid
     environment variable. For the list of Amplify system environment
     variables that are available by default, see the table in [Amplify environment variable reference](environment-variables.md#amplify-console-environment-variables "environment-variables.md#amplify-console-environment-variables").

   - **Connecting a branch to an existing
     app**
     1. If you are connecting a new branch to an existing app, set the social
        sign-in environment variables before connecting the branch. In the
        navigation pane, choose **App Settings**,
        **Environment variables**.
     2. In the **Environment variables** section, choose
        **Manage variables**.
     3. In the **Manage variables** section, choose
        **Add variable**.
     4. For **Variable** (key), enter your client ID. For
        **Value**, enter your client secret.
     5. Choose, **Save**.
