# Quickstart: Installing, using features in GitHub, and increasing usage limits

###### Note

Amazon Q Developer for GitHub is in preview release and is subject to change.

This tutorial provides a walkthrough of the following tasks:

1. Install the Amazon Q Developer app from the GitHub Marketplace and provide access to your
   repositories.
2. Get started with Amazon Q Developer in an issue by adding a label for feature
   development, or by creating a new pull request for code review.
   Alternatively, you can use slash commands in issues to initiate feature development.
   You can also initiate additional code reviews within pull requests
   with a slash command.
3. (Optional) Register your Amazon Q Developer app installation with your AWS account to
   increase your usage limits.

## Step 1: Install Amazon Q Developer in GitHub and authorize access

You can use Amazon Q Developer in GitHub free without the need to set up an AWS account to get
started. The first step to using Amazon Q Developer in GitHub is to install the app from [GitHub](https://github.com/marketplace/amazon-q-developer "https://github.com/marketplace/amazon-q-developer")
. During this process, you can provide Amazon Q Developer access to all
your GitHub repositories or selected repositories.

###### Important

To install the Amazon Q Developer app and authorize access to GitHub repositories, you must meet
the requirements for the GitHub organization. For more information, see [Requirements to install a GitHub App](https://docs.github.com/en/enterprise-cloud@latest/apps/using-github-apps/installing-a-github-app-from-a-third-party#requirements-to-install-a-github-app "https://docs.github.com/en/enterprise-cloud@latest/apps/using-github-apps/installing-a-github-app-from-a-third-party#requirements-to-install-a-github-app") and [Roles in organization](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization "https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization") in the _GitHub documentation_.

**To install Amazon Q Developer and authorize access**

1. Navigate to the [Amazon Q Developer for GitHub app](https://github.com/marketplace/amazon-q-developer "https://github.com/marketplace/amazon-q-developer") page.
2. If necessary, sign in to your [GitHub](https://github.com/ "https://github.com/") account
   using your GitHub credentials.
3. Review the Amazon Q Developer app's overview and features, and then choose
   **Install**.
4. Do one of the following to configure access to your GitHub repositories:
   1. To provide access to all current and future repositories, choose **All
      repositories**.
   2. To provide access to specific repositories, choose **Only select
      repositories**, choose the **Select repositories**
      dropdown, and then choose a repository you want to allow to access to.

5. Choose **Install** to complete installing Amazon Q Developer in GitHub and
   authorizing it to access your repositories.

After installing the app in GitHub and authorizing access, you're redirected to the
Amazon Q Developer overview page in GitHub. You can navigate to your GitHub repository to begin using
the Amazon Q Developer features.

###### Note

If your GitHub enterprise organization has enabled IP allowlisting, you must accept the
allowed IP addresses on the GitHub app. You can also choose to automatically add the IP
addresses to your allow list. For more information, see [Allowing access by GitHub Apps](https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization#allowing-access-by-github-apps "https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization#allowing-access-by-github-apps") and [Enabling allowed IP addresses](https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization#enabling-allowed-ip-addresses "https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization#enabling-allowed-ip-addresses") in the _GitHub
documentation_.

The following IP addresses are used to access your GitHub resources:

```
34.228.181.128
44.219.176.187
54.226.244.221
```

## Step 2: Using Amazon Q Developer features in GitHub

After installing the Amazon Q Developer app in GitHub and authorizing access to your repositories,
you can begin using the Amazon Q Developer agents for support across the software development
lifecycle from coding, testing, and deploying to troubleshooting
applications. For more information, see one of the following:

###### Important

The Amazon Q Developer app attempts to automatically create the **Amazon Q development
agent** label in GitHub
repositories you authorize access to. If the label is not automatically created, or if
it's unintentionally deleted, you can manually create it in GitHub. The label must be
named as **Amazon Q development agent** in order for it to be recognized and processed as a Amazon Q Developer label.
For more information, see [Creating a label](https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/managing-labels#creating-a-label "https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/managing-labels#creating-a-label") in the _GitHub documentation_.

- [Developing features and iterating with Amazon Q Developer in GitHub](github-feature-development.md "github-feature-development.md")
- [Reviewing code with Amazon Q Developer in GitHub](github-code-reviews.md "github-code-reviews.md")

## Step 3: Increase free usage limits and configure details

You can use Amazon Q Developer agents in GitHub for free without the need to set up an AWS
account to get started. You're provided with limited invocations per month for feature
development and code review. You can increase your free usage at any time by registering your Amazon Q Developer app
installation with your AWS account. Registering also provides with the ability to
configure details such as disabling code reviews and adding tags for searching and
filtering. For more information, see [Increasing usage limits and configuring details in Amazon Q Developer console](github-register-app-install.md "github-register-app-install.md").

###### Important

To register the app installation in the Amazon Q Developer console, you must meet the
requirements for the GitHub organization. For more information, see [Requirements to install a GitHub App](https://docs.github.com/en/enterprise-cloud@latest/apps/using-github-apps/installing-a-github-app-from-a-third-party#requirements-to-install-a-github-app "https://docs.github.com/en/enterprise-cloud@latest/apps/using-github-apps/installing-a-github-app-from-a-third-party#requirements-to-install-a-github-app") and [OAuth apps and organizations](https://docs.github.com/en/apps/oauth-apps/using-oauth-apps/authorizing-oauth-apps#oauth-apps-and-organizations "https://docs.github.com/en/apps/oauth-apps/using-oauth-apps/authorizing-oauth-apps#oauth-apps-and-organizations") in the _GitHub
documentation_.
