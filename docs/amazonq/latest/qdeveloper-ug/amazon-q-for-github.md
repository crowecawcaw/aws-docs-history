# Amazon Q Developer for GitHub (Preview)

###### Note

Amazon Q Developer for GitHub is in preview release and is subject to change.

[Amazon Q Developer for GitHub or GitHub
Enterprise Cloud](https://github.com/marketplace/amazon-q-developer "https://github.com/marketplace/amazon-q-developer") allows you to leverage Amazon Q Developer capabilities for your software
development workflows. With specialized development agents, you can implement new ideas, review
code for quality issues, address vulnerabilities with unit tests, and modernize legacy Java
applications. Once the agent completes a task, you can provide feedback, and the agent iterates
on the previous solution. For more information, see [Amazon Q Developer agents](#github-agents "#github-agents").

You can access the Amazon Q Developer integration through [GitHub](https://github.com/marketplace/amazon-q-developer "https://github.com/marketplace/amazon-q-developer")
and authorize it to provide access to your organization's
repositories. To get started with Amazon Q Developer for GitHub, see [Quickstart: Installing, using features in GitHub, and
increasing usage limits](github-quickstart.md "github-quickstart.md").

###### Important

To install the Amazon Q Developer app and authorize access to GitHub repositories, you must meet the
requirements for the GitHub organization. For more information, see [Requirements to install a GitHub App](https://docs.github.com/en/enterprise-cloud@latest/apps/using-github-apps/installing-a-github-app-from-a-third-party#requirements-to-install-a-github-app "https://docs.github.com/en/enterprise-cloud@latest/apps/using-github-apps/installing-a-github-app-from-a-third-party#requirements-to-install-a-github-app") and [Roles in organization](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization "https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization") in the _GitHub documentation_.

###### Note

The Amazon Q Developer integration with GitHub processes data in the United States. For more
information, see [Cross-region processing in Amazon Q Developer](cross-region-processing.md "cross-region-processing.md").

###### Note

Amazon Q Developer for GitHub (Preview) does not currently use your content for service improvement.
If we enable this in the future, we will provide you with adequate notice and a way for you to
opt out of such use.

###### Topics

- [Installing Amazon Q Developer app and authorizing
  access](#github-concepts-set-up "#github-concepts-set-up")
- [Amazon Q Developer agents](#github-agents "#github-agents")
- [Registering app installation](#github-concepts-register-app-install "#github-concepts-register-app-install")
- [Using browser extensions in GitHub](#github-concepts-extensions "#github-concepts-extensions")
- [Using slash commands in GitHub issues and pull
  requests](#github-slash-commands "#github-slash-commands")
- [Quickstart: Installing, using features in GitHub, and
  increasing usage limits](github-quickstart.md "github-quickstart.md")
- [Developing features and iterating with Amazon Q Developer
  in GitHub](github-feature-development.md "github-feature-development.md")
- [Reviewing code with Amazon Q Developer in GitHub](github-code-reviews.md "github-code-reviews.md")
- [Transforming code with Amazon Q Developer in GitHub](github-code-transformation.md "github-code-transformation.md")
- [Customizing a workflow for code
  transformation](github-code-transformation-workflow.md "github-code-transformation-workflow.md")
- [Increasing usage limits and configuring details
  in Amazon Q Developer console](github-register-app-install.md "github-register-app-install.md")
- [Configuring registered installation details](github-configuration.md "github-configuration.md")
- [Troubleshooting issues for Amazon Q Developer for
  GitHub](github-troubleshooting.md "github-troubleshooting.md")

## Installing Amazon Q Developer app and authorizing

access

As a GitHub organization administrator, you can install and configure the Amazon Q Developer app
from [GitHub](https://github.com/apps/amazon-q-developer "https://github.com/apps/amazon-q-developer") for free without the need to set up an AWS account
to get started. During the installation process, you choose to provide access to all or
selected repositories in your GitHub organization. After installing and authorizing, you have
access to free usage for the Amazon Q Developer features in GitHub. You can increase
free usage by registering the app installation in the [Amazon Q Developer
console](https://us-east-1.console.aws.amazon.com/amazonq/developer/home#/github "https://us-east-1.console.aws.amazon.com/amazonq/developer/home#/github"). For more information, see [Quickstart: Installing, using features in GitHub, and
increasing usage limits](github-quickstart.md "github-quickstart.md").

###### Important

To install the Amazon Q Developer app and authorize access to GitHub repositories, you must meet
the requirements for the GitHub organization. For more information, see [Requirements to install a GitHub App](https://docs.github.com/en/enterprise-cloud@latest/apps/using-github-apps/installing-a-github-app-from-a-third-party#requirements-to-install-a-github-app "https://docs.github.com/en/enterprise-cloud@latest/apps/using-github-apps/installing-a-github-app-from-a-third-party#requirements-to-install-a-github-app") and [Roles in organization](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization "https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization") in the _GitHub documentation_.

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

## Amazon Q Developer agents

Amazon Q Developer agents provide support across the software development lifecycle from coding,
testing, and deploying to troubleshooting and modernizing applications.

- **Amazon Q development agent** – After creating an issue and
  adding the feature development label, Amazon Q Developer automatically implements your new
  features and bug fixes. Amazon Q Developer creates a pull request with the changes and a summary
  of the changes. Instead of applying a label, you can also initiate feature development
  with the `/q dev` slash command in a comment of the issue. For more
  information, see [Developing features and iterating with Amazon Q Developer
  in GitHub](github-feature-development.md "github-feature-development.md").
- **Amazon Q code review agent** – When a new pull request is
  created or a closed pull request is reopened, Amazon Q Developer automatically performs a code
  review and provides feedback on code quality, potential issues, and security concerns.
  Amazon Q Developer also generates fixes for the identified issues, which you can review and choose
  to commit to the pull request. The code review includes a code review summary with
  threaded findings. You can interact with Amazon Q Developer by using the `/q` command
  in pull request comments to ask questions about the code review findings.

Automatic code reviews are not triggered by subsequent commits made within an existing
pull request. You can initiate additional code reviews within pull requests with the
`/q review` slash command. For more information, see [Reviewing code with Amazon Q Developer in GitHub](github-code-reviews.md "github-code-reviews.md").

- **Amazon Q transform agent** – After creating an issue and
  adding the code transformation label, Amazon Q Developer transforms your code from Java version 8
  or 11 to version 17. Amazon Q Developer creates a pull request with the changes and summary of the
  changes. Instead of applying a label, you can also initiate code transformation with the
  `/q transform` slash command in a comment of the issue. For more information,
  see [Transforming code with Amazon Q Developer in GitHub](github-code-transformation.md "github-code-transformation.md").

###### Important

The Amazon Q Developer app attempts to automatically create the **Amazon Q development
agent** and the **Amazon Q transform agent** labels in GitHub
repositories you authorize access to. If the labels are not automatically created, or if
they're unintentionally deleted, you can manually create them in GitHub. The labels must be
named as **Amazon Q development agent** and **Amazon Q transform
agent** in order for them to be recognized and processed as Amazon Q Developer labels.
For more information, see [Creating a label](https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/managing-labels#creating-a-label "https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/managing-labels#creating-a-label") in the _GitHub documentation_.

## Registering app installation

The Amazon Q Developer integration for GitHub is available for free without the need to set up an
AWS account to get started. You're provided with limited invocations per month for feature
development and code transformation, as well as limited number of lines for code reviews per
month. You can increase free usage by registering your Amazon Q Developer app installation with your
AWS account. For more information, see [Increasing usage limits and configuring details
in Amazon Q Developer console](github-register-app-install.md "github-register-app-install.md").

###### Important

To register the app installation in the Amazon Q Developer console, you must meet the
requirements for the GitHub organization. For more information, see [Requirements to install a GitHub App](https://docs.github.com/en/enterprise-cloud@latest/apps/using-github-apps/installing-a-github-app-from-a-third-party#requirements-to-install-a-github-app "https://docs.github.com/en/enterprise-cloud@latest/apps/using-github-apps/installing-a-github-app-from-a-third-party#requirements-to-install-a-github-app") and [OAuth apps and organizations](https://docs.github.com/en/apps/oauth-apps/using-oauth-apps/authorizing-oauth-apps#oauth-apps-and-organizations "https://docs.github.com/en/apps/oauth-apps/using-oauth-apps/authorizing-oauth-apps#oauth-apps-and-organizations") in the _GitHub
documentation_.

## Using browser extensions in GitHub

You can use the Amazon Q Developer extension in a supported browser to quickly add a label for
feature development or code transformation in GitHub issues without having to search through
label menus.

The Amazon Q Developer extension is available for the following browsers:

- [Google Chrome](https://chromewebstore.google.com/detail/amazon-q-github-issue-hel/oefafjbablenakmhacfllkmpaeabnnfi "https://chromewebstore.google.com/detail/amazon-q-github-issue-hel/oefafjbablenakmhacfllkmpaeabnnfi")
- [Mozilla Firefox](https://addons.mozilla.org/en-US/firefox/addon/amazon-q-github-issue-helper "https://addons.mozilla.org/en-US/firefox/addon/amazon-q-github-issue-helper")
- [Microsoft Edge](https://microsoftedge.microsoft.com/addons/detail/amazon-q-github-issue-helper/poghackjbfhejeppjaegbnblangjbmmc "https://microsoftedge.microsoft.com/addons/detail/amazon-q-github-issue-helper/poghackjbfhejeppjaegbnblangjbmmc")

## Using slash commands in GitHub issues and pull

requests

You can use slash commands in comments within GitHub issues or pull requests to invoke
Amazon Q Developer to perform development tasks or provide support.

- `/q dev` - Invokes Amazon Q Developer in a GitHub issue to automatically implement
  new features and bug fixes. Amazon Q Developer creates a pull request with the changes and a
  summary of the changes.
- `/q review` - Invokes Amazon Q Developer to automatically perform code reviews when
  pull requests are created or reopened. Code reviews provide feedback on code quality,
  potential issues, and security concerns, along with suggested fixes and code review
  summaries with threaded findings. Use `/q` in pull request comments to interact
  with findings. Automatic reviews are not triggered by subsequent commits to existing pull
  requests.
- `/q transform` - Invokes Amazon Q Developer to automatically transform Java 8 or 11
  code to Java 17 when an issue is created with the code transformation label. Amazon Q Developer
  creates a pull request with the changes and a summary of the modifications.
- `/q help` - Provides information about Amazon Q Developer for GitHub, including slash
  comannds, features, customization details, as well as a link to the [Amazon Q Developer for GitHub (Preview)](amazon-q-for-github.md "amazon-q-for-github.md") documentation in the
  _Amazon Q Developer Developer Guide_.
