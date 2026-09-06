

# Feature branch deployments and team workflows
<a name="multi-environments"></a>

Amplify Hosting is designed to work with feature branch and GitFlow workflows. Amplify uses Git branches to create a new deployment each time you connect a new branch in your repository. After you connect your first branch, you create additional feature branches.

**To add a branch to an app**

1. Choose the app you want to add a branch to.

1. Choose **App settings**, then **Branch settings**.

1. On the **Branch settings** page, choose **Add branch**.

1. Select a branch from your repository.

1. Choose **Add branch.**

1. Redeploy your app.

After you add a branch, your app has two deployments available at the Amplify default domains, such as *https://main.appid.amplifyapp.com* and *https://dev.appid.amplifyapp.com*. This may vary from team-to-team, but typically the **main branch** tracks release code and is your production branch. The **develop branch** is used as an integration branch to test new features. This enables beta testers to test unreleased features on the develop branch deployment, without affecting any of the production end users on the main branch deployment.

**Topics**
+ [Team workflows with fullstack Amplify Gen 2 apps](team-workflows-gen2.md)
+ [Team workflows with fullstack Amplify Gen 1 apps](team-workflows-with-amplify-cli-backend-environments.md)
+ [Pattern-based feature branch deployments](pattern-based-feature-branch-deployments.md)
+ [Automatic build-time generation of Amplify config (Gen 1 apps only)](amplify-config-autogeneration.md)
+ [Conditional backend builds (Gen 1 apps only)](conditional-backends.md)
+ [Use Amplify backends across apps (Gen 1 apps only)](reuse-backends.md)