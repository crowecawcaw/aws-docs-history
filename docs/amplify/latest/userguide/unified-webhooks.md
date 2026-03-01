# Unified webhooks for Git repositories

Amplify Hosting uses webhooks to automatically initiate a build after a new commit to
your Git repository. The unified webhooks feature improves Amplify's
integrations with Git providers and enables you to connect more Amplify applications to a
single repository. With unified webhooks, Amplify now uses a single webhook per Region
for all associated applications in your repository. For example, if your repository is
connected to applications in both the US East (N. Virginia) and US West (Oregon) Regions,
you will have two unified webhooks.

Before this release, Amplify created a new webhook for each app associated with a
repository. If you had multiple apps in a single repository, you could reach the webhook
limits enforced by individual Git providers and be prevented from adding more apps. This
was especially challenging for teams working in monorepos, where multiple projects exist in
a single repository.

Unified webhooks provide the following benefits:

- **Overcome Git provider webhook limits**: You can
  connect as many Amplify apps as you need to a single repository.
- **Enhanced monorepo support**: You have more
  flexibility and efficiency when working with monorepos, where multiple projects share
  a single repository.
- **Simplified management**: Managing multiple
  Amplify apps with a single repository webhook reduces complexity and potential
  points of failure.
- **Improved workflow integration**: You can use the
  webhooks allocated by your Git provider for other essential workflows in your
  development process.

## Getting started with unified webhooks

**Creating a new app**

When you deploy a new application to Amplify Hosting from a Git repository, the
unified webhooks feature is automatically implemented for your repository. For
instructions on creating a new application, see [Getting started with deploying an app to Amplify Hosting](getting-started.md "getting-started.md").

**Updating an existing app**

For existing Amplify applications, you must reconnect your Git repository to your
application to replace the existing webhooks with a unified webhook. If you've already
reached the maximum number of webhooks allowed by your Git provider, migrating to the
unified webhook might not succeed. In this case, manually remove at least one existing
webhook before reconnecting.

You can have multiple applications in a repository that are deployed to different
AWS Regions. Since Amplify operations are Region based, the migration to a unified
webhook only occurs for the webhooks in the Region where you reconnected your Amplify
app. As a result, you might see both application id-based webhooks and Region-based
unified webhooks in your repository.

Use the following instructions to migrate an existing Amplify app to a unified
webhook.

###### To migrate an existing Amplify app to a unified webhook

1. Sign in to the AWS Management Console and open the [Amplify console](https://console.aws.amazon.com/amplify/ "https://console.aws.amazon.com/amplify/").
2. Choose the app that you want to migrate to a unified webhook.
3. In the navigation pane, choose **App settings**, then choose
   **Branch settings**.
4. On the **Branch settings** page, choose **Reconnect
   repository**.
5. To verify successful migration to the unified webhook, navigate to the webhook
   settings in your Git repository. You should see a single webhook URL in the format
   `https://amplify-webhooks.`Region`.amazonaws.com/`git-provider``.
