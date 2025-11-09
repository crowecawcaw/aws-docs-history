Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Integrating with GitHub Actions

A _GitHub Action_ is a lot like a [CodeCatalyst action](workflows-actions.md#workflows-actions-types-cc "workflows-actions.md#workflows-actions-types-cc"), except that it was developed for
use with GitHub workflows. For details about GitHub Actions, see the [GitHub Actions](https://docs.github.com/en/actions "https://docs.github.com/en/actions") documentation.

You can use GitHub Actions alongside native CodeCatalyst actions in a CodeCatalyst workflow.

There are two ways to add a GitHub Action to a CodeCatalyst workflow:

- You can select the GitHub Action from a curated list in the CodeCatalyst console. Several
  popular GitHub Actions are available. For more information, see [Adding a curated GitHub Action](integrations-github-action-add-curated.md "integrations-github-action-add-curated.md").
- If the GitHub Action that you want to use is not available in the CodeCatalyst console, you
  can add it using a **GitHub Actions** action.

A **_GitHub Actions_** action is a _CodeCatalyst action_ that
wraps a GitHub Action and makes it compatible with CodeCatalyst workflows.

Here is an example of a **GitHub Actions** action wrapping the [Super-Linter](https://github.com/marketplace/actions/super-linter "https://github.com/marketplace/actions/super-linter") GitHub
Action:

```
Actions:
  GitHubAction:
    Identifier: aws/github-actions-runner@v1
    Configuration:
      Steps:
        - name: Lint Code Base
          uses: github/super-linter@v4
          env:
            VALIDATE_ALL_CODEBASE: "true"
            DEFAULT_BRANCH: main
```

In the previous code, the CodeCatalyst **GitHub Actions** action (identified
by `aws/github-actions-runner@v1`) wraps the Super-Linter action (identified
by `github/super-linter@v4`), making it work in a CodeCatalyst workflow.

For more information, see [Adding the 'GitHub Actions' action](integrations-github-action-add.md "integrations-github-action-add.md").
All GitHub Actions—both curated and not—must be wrapped inside a
**GitHub Actions** action (`aws/github-actions-runner@v1`), as
shown in the previous example. The wrapper is required for the action to function properly.

###### Topics

- [How are GitHub Actions different
  from CodeCatalyst actions?](#integrations-github-actions-how-different "#integrations-github-actions-how-different")
- [Can GitHub Actions interact with
  other CodeCatalyst actions in the workflow?](#integrations-github-actions-interactions.title "#integrations-github-actions-interactions.title")
- [Which GitHub Actions can I
  use?](#integrations-github-actions-supported "#integrations-github-actions-supported")
- [Limitations of GitHub Actions in
  CodeCatalyst](#integrations-github-actions-limitations "#integrations-github-actions-limitations")
- [How do I add a GitHub Action (high-level
  steps)?](#integrations-github-actions-how-to "#integrations-github-actions-how-to")
- [Does the GitHub Action run in
  GitHub?](#integrations-github-actions-where-it-runs "#integrations-github-actions-where-it-runs")
- [Can I use GitHub workflows
  too?](#integrations-github-actions-workflows-support.title "#integrations-github-actions-workflows-support.title")
- [Runtime image used by the 'GitHub Actions'
  action](#integrations-github-actions-runtime "#integrations-github-actions-runtime")
- [Tutorial: Lint code using a GitHub
  Action](integrations-github-action-tutorial.md "integrations-github-action-tutorial.md")
- [Adding the 'GitHub Actions' action](integrations-github-action-add.md "integrations-github-action-add.md")
- [Adding a curated GitHub Action](integrations-github-action-add-curated.md "integrations-github-action-add-curated.md")
- [Exporting GitHub output parameters](integrations-github-action-export.md "integrations-github-action-export.md")
- [Referencing GitHub output
  parameters](integrations-github-action-referencing.md "integrations-github-action-referencing.md")
- ['GitHub Actions' action YAML](github-action-ref.md "github-action-ref.md")

## How are GitHub Actions different

from CodeCatalyst actions?

GitHub Actions that are used inside a CodeCatalyst workflow do not have the same level of access
and integration with AWS and CodeCatalyst features (such as [environments](deploy-environments.md "deploy-environments.md") and [issues](issues.md "issues.md"))
that CodeCatalyst actions do.

## Can GitHub Actions interact with

other CodeCatalyst actions in the workflow?

Yes. For example, GitHub Actions can use variables produced by other CodeCatalyst actions as
input, and can also share output parameters and artifacts with CodeCatalyst actions. For more
information, see [Exporting GitHub output parameters](integrations-github-action-export.md "integrations-github-action-export.md") and [Referencing GitHub output
parameters](integrations-github-action-referencing.md "integrations-github-action-referencing.md").

## Which GitHub Actions can I

use?

You can use any GitHub Action available through the CodeCatalyst console, and any GitHub Action
available in the [GitHub
Marketplace](https://github.com/marketplace/actions "https://github.com/marketplace/actions"). If you decide to use a GitHub Action from the Marketplace, keep in mind
the following [limitations](#integrations-github-actions-limitations "#integrations-github-actions-limitations").

## Limitations of GitHub Actions in

CodeCatalyst

- GitHub Actions cannot be used with the CodeCatalyst [Lambda
  compute type](workflows-working-compute.md#compute.types "workflows-working-compute.md#compute.types").

- GitHub Actions run on the [November 2022](build-images.md#build.previous-image "build-images.md#build.previous-image")
  runtime environment Docker image, which includes older tooling. For more information
  about the image and tooling, see [Specifying runtime environment images](build-images.md "build-images.md").

- GitHub Actions that internally rely on the [`github` context](https://docs.github.com/en/actions/learn-github-actions/contexts#github-context "https://docs.github.com/en/actions/learn-github-actions/contexts#github-context") or that reference GitHub-specific resources won't
  work in CodeCatalyst. For example, the following actions won't work in CodeCatalyst:
  - Actions that attempt to add, change, or update GitHub resources. Examples include
    actions that update pull requests, or create issues in GitHub.
  - Almost all actions listed in [https://github.com/actions](https://github.com/actions "https://github.com/actions").

- GitHub Actions that are [Docker container actions](https://docs.github.com/en/actions/creating-actions/about-custom-actions#docker-container-actions "https://docs.github.com/en/actions/creating-actions/about-custom-actions#docker-container-actions") will work, but they must be run by the default Docker
  user (root). Do not run the action as user 1001. (At the time of writing, user 1001 works
  in GitHub, but not in CodeCatalyst.) For more information, see the [USER](https://docs.github.com/en/actions/creating-actions/dockerfile-support-for-github-actions#user "https://docs.github.com/en/actions/creating-actions/dockerfile-support-for-github-actions#user") topic in [Dockerfile support for GitHub Actions](https://docs.github.com/en/actions/creating-actions/dockerfile-support-for-github-actions "https://docs.github.com/en/actions/creating-actions/dockerfile-support-for-github-actions").

For a list of GitHub Actions available through the CodeCatalyst console, see [Adding a curated GitHub Action](integrations-github-action-add-curated.md "integrations-github-action-add-curated.md").

## How do I add a GitHub Action (high-level

steps)?

The high-level steps to add a GitHub Action to a CodeCatalyst workflow are as follows:

1. In your CodeCatalyst project, you **create a workflow**. The workflow is
   where you define how to build, test, and deploy your application. For more information,
   see [Getting started with workflows](workflows-getting-started.md "workflows-getting-started.md").
2. In the workflow, you **add a curated GitHub Action** or you
   **add the GitHub Actions** action.
3. You do one of the following:
   - If you chose to add a curated action, configure it. For more information, see
     [Adding a curated GitHub Action](integrations-github-action-add-curated.md "integrations-github-action-add-curated.md").
   - If you chose to add a non-curated action, within the **GitHub
     Actions** action, you **paste the GitHub Action’s YAML
     code**. You can find this code on the details page of your chosen GitHub
     Action in the [GitHub
     Marketplace](https://github.com/marketplace/actions "https://github.com/marketplace/actions"). You will likely need to modify the code slightly to have it
     work in CodeCatalyst. For more information, see [Adding the 'GitHub Actions' action](integrations-github-action-add.md "integrations-github-action-add.md").

4. (Optional) Within the workflow, **you add other actions** like the
   build and test actions. For more information, see [Build, test, and deploy with workflows](workflow.md "workflow.md").
5. You **start the workflow** either manually or automatically through a
   trigger. The workflow runs the GitHub Action and any other actions in the workflow. For
   more information, see [Starting a workflow run manually](workflows-manually-start.md "workflows-manually-start.md").

For detailed steps, see:

- [Adding a curated GitHub Action](integrations-github-action-add-curated.md "integrations-github-action-add-curated.md").
- [Adding the 'GitHub Actions' action](integrations-github-action-add.md "integrations-github-action-add.md").

## Does the GitHub Action run in

GitHub?

No. The GitHub Action runs in CodeCatalyst, using CodeCatalyst’s [runtime environment image](workflows-working-compute.md "workflows-working-compute.md").

## Can I use GitHub workflows

too?

No.

## Runtime image used by the 'GitHub Actions'

action

The CodeCatalyst **GitHub Actions** action runs on a [November 2022 image](build-images.md#build.previous-image "build-images.md#build.previous-image"). For more information, see [Active images](build-images.md#build-curated-images "build-images.md#build-curated-images").
