

# Deploy a Next.js app to Amplify Hosting
<a name="getting-started-next"></a>

This tutorial walks you through building and deploying a Next.js application from a Git repository.

Before you begin this tutorial, complete the following prerequisites.

**Create an application**  
Create a basic Next.js application to use for this tutorial, using the [create-next-app](https://nextjs.org/docs/app/api-reference/create-next-app) instructions in the *Next.js documentation*.

**Create a Git repository**  
Amplify supports GitHub, Bitbucket, GitLab, and AWS CodeCommit. Push your `create-next-app` application to your Git repository.

## Step 1: Connect a Git repository
<a name="step-1-connect-repository"></a>

In this step, you connect your Next.js application in a Git repository to Amplify Hosting.

**To connect an app in a Git repository**

1. Open the [Amplify console](https://console.aws.amazon.com/amplify/).

1. If you are deploying your first app in the current Region, by default you will start from the **AWS Amplify** service page.

   Choose **Deploy an app** at the top of the page.

1. On the **Start building with Amplify** page, choose your Git repository provider, then choose **Next**.

   For GitHub repositories, Amplify uses the GitHub Apps feature to authorize Amplify access. For more information about installing and authorizing the GitHub App, see [Setting up Amplify access to GitHub repositories](setting-up-GitHub-access.md).
**Note**  
After you authorize the Amplify console with Bitbucket, GitLab, or AWS CodeCommit, Amplify fetches an access token from the repository provider, but it *doesn’t store the token* on the AWS servers. Amplify accesses your repository using deploy keys installed in a specific repository only.

1. On the **Add repository branch** page do the following:

   1. Select the name of the repository to connect.

   1. Select the name of the repository branch to connect.

   1. Choose **Next**.

## Step 2: Confirm the build settings
<a name="step-2a-confirm-build-settings-for-the-front-end"></a>

Amplify automatically detects the sequence of build commands to run for the branch you are deploying. In this step you review and confirm your build settings.

**To confirm the build settings for an app**

1. On the **App settings** page, locate the **Build settings** section.

   Verify that the **Frontend build command** and **Build output directory** are correct. For this Next.js example app, the **Build output directory** is set to `.next`.

1. The procedure for adding a service role varies depending on whether you want to create a new role or use an existing one.
   + To create a new role:

     1. Choose **Create and use a new service role**.
   + To use an existing role:

     1. Choose **Use an existing role**.

     1. In the service role list, select the role to use.

1. Choose **Next**.

## Step 3: Deploy the application
<a name="step-3-save-and-deploy"></a>

In this step you deploy your app to the AWS global content delivery network (CDN).

**To save and deploy an app**

1. On the **Review** page, confirm that your repository details and app settings are correct.

1. Choose **Save and deploy**. Your front end build typically takes 1 to 2 minutes, but can vary based on the size of the app.

1. When the deployment is complete, you can view your app using the link to the `amplifyapp.com` default domain.

**Note**  
To augment the security of your Amplify applications, the *amplifyapp.com* domain is registered in the [Public Suffix List (PSL)](https://publicsuffix.org/). For further security, we recommend that you use cookies with a `__Host-` prefix if you ever need to set sensitive cookies in the default domain name for your Amplify applications. This practice will help to defend your domain against cross-site request forgery attempts (CSRF). For more information see the [Set-Cookie](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#cookie_prefixes) page in the Mozilla Developer Network.

## Step 4: (Optional) clean up resources
<a name="step-4-clean-up"></a>

If you no longer need the app you deployed for the tutorial, you can delete it. This step helps ensure that you aren't charged for resources that you aren't using.

**To delete an app**

1. From the **App settings** menu in the navigation pane, choose **General settings**.

1. On the **General settings** page, choose **Delete app**.

1. In the confirmation window, enter **delete**. Then choose **Delete app**.

## Add features to your app
<a name="next-steps"></a>

Now that you have an app deployed to Amplify, you can explore some of the following features that are available to your hosted application.

**Environment variables**  
Applications often need configuration information at runtime. These configurations can be database connection details, API keys, or parameters. Environment variables provide a way to expose these configurations at build time. For more information, see [Environment variables](environment-variables.md).

**Custom domains**  
In this tutorial, Amplify hosts your app for you on the default `amplifyapp.com` domain with a URL such as `https://branch-name.d1m7bkiki6tdw1.amplifyapp.com`. When you connect your app to a custom domain, users see that your app is hosted on a custom URL, such as `https://www.example.com`. For more information, see [Setting up custom domains](custom-domains.md).

**Pull request previews**  
Web pull request previews offer teams a way to preview changes from pull requests (PRs) before merging code to a production or integration branch. For more information, see [Web previews for pull requests](pr-previews.md).

**Manage multiple environments**  
To learn how Amplify works with feature branches and GitFlow workflows to support multiple deployments, see [Feature branch deployments and team workflows](multi-environments.md).