Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Getting started with custom blueprints

During the process of creating a blueprint, you can configure the blueprint and generate a preview of the project
resources. Each custom blueprint is managed by a CodeCatalyst project, which contains a workflow by default for publishing to the
space's blueprints catalog.

While configuring your custom blueprint's details, you can also choose to store your blueprint's source code in a third-party repository,
where you can still manage the custom blueprint and utilize the lifecycle management capabilities to keep your space's projects synchronized
when the custom blueprint is modified. For more information, see [Add functionality to projects with extensions in CodeCatalyst](extensions.md "extensions.md") and
[Working with lifecycle management as a blueprint author](lifecycle-management-dev.md "lifecycle-management-dev.md").

If you already have a source repository with standardization and best practices in place,
you can choose to convert that source repository into a custom blueprint. For more information,
see [Converting source repositories to custom blueprints](convert-bp.md "convert-bp.md").

###### Topics

- [Prerequisites](#prerequisites-bp "#prerequisites-bp")
- [Step 1: Create a custom blueprint in CodeCatalyst](#getting-started-create-bp "#getting-started-create-bp")
- [Step 2: Develop a custom blueprint with components](#getting-started-develop-bp "#getting-started-develop-bp")
- [Step 3: Preview a custom blueprint](#getting-started-publish-bp "#getting-started-publish-bp")
- [(Optional) Step 4: Publish a custom blueprint preview version](#getting-started-add-bp "#getting-started-add-bp")

## Prerequisites

Before creating a custom blueprint, consider the following requirements:

- Your CodeCatalyst space must be the **Enterprise** tier. For more information, see [Managing billing](../adminguide/managing-billing-view-plan.md "../adminguide/managing-billing-view-plan.md") in the Amazon CodeCatalyst Administrator Guide.
- You need to have the **Space administrator** or the **Power user** role to create custom blueprints. For more
  information, see [Granting access with user roles](ipa-roles.md "ipa-roles.md").

## Step 1: Create a custom blueprint in CodeCatalyst

When you create a custom blueprint from your space's settings, a repository is created for
you. The repository includes all the required resources that you must have to develop your
blueprint before publishing it to the space's blueprints catalog.

**To create a custom blueprint**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. In the CodeCatalyst console, navigate to the space where you want to create a custom blueprint.
3. On the space dashboard, choose the **Settings** tab, and then choose
   **Blueprints**.
4. Choose **Create blueprint**.
5. Under **Name your blueprint**, enter the name that you want to assign to your project and its
   associated resource names. The name must be unique within your space.
6. (Optional) By default, the source code created by the blueprint is stored in a CodeCatalyst
   repository. Alternatively, you can choose to store the blueprint's source code in a third-party
   repository. For more information, see [Add functionality to projects with extensions in CodeCatalyst](extensions.md "extensions.md").

Do one of the following depending on the third-party repository provider you want to use:

    * **GitHub repositories**: Connect a GitHub account.


    Choose the **Advanced** dropdown menu, choose GitHub
     as the repository provider, and then choose the GitHub account where you want to store the
     source code created by the blueprint.


    ###### Note

    If you're using a connection to a GitHub account, you must create a personal
     connection to establish identity mapping between your CodeCatalyst identity and your GitHub identity.
     For more information, see [Personal connections](concepts.md#personal-connection-concept "concepts.md#personal-connection-concept") and [Accessing GitHub resources with personal
     connections](ipa-settings-connections.md "ipa-settings-connections.md").
    * **Bitbucket repositories**: Connect a Bitbucket workspace.


    Choose the **Advanced** dropdown menu, choose Bitbucket
     as the repository provider, and then choose the Bitbucket workspace where you want to store the
     source code created by the blueprint.
    * **GitLab repositories**: Connect a GitLab user.


    Choose the **Advanced** dropdown menu, choose GitLab
     as the repository provider, and then choose the GitLab user where you want to store the
     source code created by the blueprint.

7. Under **Blueprint details**, do the following:
   1. In the **Blueprint display name** text input field, enter a name that will appear in your space's
      blueprints catalog.
   2. In the **Description** text input field, enter a description for your custom blueprint.
   3. In the **Author name** text input field, enter an author name for your custom blueprint.
   4. (Optional) Choose the **Advanced settings**.
      1. Choose **+ Add** to add tags that are added to the `package.json` file.
      2. Choose the **License** dropdown menu, and then choose a license for your custom blueprint.
      3. In the **Blueprint package name** text input field, enter a name to identify your blueprint package.
      4. By default, a release workflow is generated using a publishing blueprint within your project called **Blueprint
         Builder**. The workflow publishes the latest blueprint version to your space when you push changes since publishing
         permissions are enabled by the release workflow. To turn off the workflow generation, uncheck the **Release
         workflow** checkbox.

8. (Optional) A blueprint project comes with predefined code to support the publishing of the
   blueprint to the space's blueprints catalog. To view definition files with updates based on the project
   parameter selections you made, choose **View code** or **View
   workflow** from **Generate blueprint preview**.
9. Choose **Create blueprint**.

If you didn't turn off the workflow generation for your custom blueprint, the workflow automatically begins to run when your blueprint
is created. When the workflow run is complete, your custom blueprint is available to be added to your space's blueprints catalog by default.
You can turn off publishing permissions if you don't want the latest blueprint version to be published automatically to your space. For more
information, see [Setting publishing permissions for a custom blueprint](manage-permissions-bp.md "manage-permissions-bp.md") and
[Running a workflow](workflows-working-runs.md "workflows-working-runs.md").

Since the publishing workflow called `blueprint-release` is created using a blueprint, the blueprint can be found as an
applied blueprint in your project. For more information, see [Adding a blueprint in a project to integrate resources](apply-bp.md "apply-bp.md") and
[Disassociating a blueprint from a project to stop updates](disassociate-bp.md "disassociate-bp.md").

## Step 2: Develop a custom blueprint with components

A blueprint wizard is generated when you create a custom blueprint, and it can be modified with components when developing the custom
blueprint. You can update the `src/blueprints.js` and `src/defaults.json` files to modify the wizard.

###### Important

If you want to use blueprint packages from external sources, consider the risks that may come
with those packages. You're responsible for the custom blueprints that you add to your space and
the code they generate.

Create a Dev Environment in your CodeCatalyst project with a supported integrated development environment (IDE) before configuring your blueprint code.
A Dev Environment is necessary to work with the required tools and packages.

**To create a Dev Environment**

1. In the navigation pane, do one of the following:
   1. Choose **Overview**, and then navigate to the **My Dev Environments** section.
   2. Choose **Code**, and then choose **Dev Environments**.
   3. Choose **Code**, choose **Source repositories**, and choose
      the repository that you created when creating your blueprint.

2. Choose **Create Dev Environment**.
3. Choose a supported IDE from the dropdown menu. See [Supported integrated development environments for Dev Environments](devenvironment-create.md#devenvironment-supported-ide "devenvironment-create.md#devenvironment-supported-ide") for more
   information.
4. Choose **Work in existing branch**, and from the **Existing branch** dropdown menu, choose the feature branch you created.
5. (Optional) In the **Alias - _optional_** text input field, enter an alias to identify the
   Dev Environment.
6. Choose **Create**. While your Dev Environment is being created, the Dev
   Environment status column displays **Starting**, and the status column
   displays **Running** when the Dev Environment has been created.

For more information, see [Write and modify code with Dev Environments in CodeCatalyst](devenvironment.md "devenvironment.md").

**To develop your custom blueprint**

1. In a working terminal, use the following `yarn` command to install dependencies:

```
yarn
```

The required tools and packages are made available through the CodeCatalyst Dev Environment, including Yarn. If you're working on a custom blueprint
without a Dev Environment, install Yarn to your system first. For more information, see
[Yarn's installation documentation](https://classic.yarnpkg.com/en/docs/install#mac-stable "https://classic.yarnpkg.com/en/docs/install#mac-stable"). 2. Develop your custom blueprint so that it's configured to your preferences. You can modify your
blueprint's wizard by adding components. For more information, see [Developing a custom blueprint to meet project requirements](develop-bp.md "develop-bp.md"), [Modifying blueprint features with a front-end wizard](wizard-bp.md "wizard-bp.md"), and
[Publishing a custom blueprint to a space](publish-bp.md "publish-bp.md").

## Step 3: Preview a custom blueprint

After setting up and developing your custom blueprint, you can preview and publish the preview
version of your blueprint to your space. A preview version gives you the ability
to check that the blueprint is what you want before it's used to create new projects or applied to
existing projects.

**To preview a custom blueprint**

1. In a working terminal, use the following `yarn` command:

```
yarn blueprint:preview
```

2. Navigate to the `See this blueprint at:` link provided to preview your custom blueprint.
3. Check that the UI, including text, appears as you expected based on your configuration. If you
   want to change your custom blueprint, you can edit the `blueprint.ts` file,
   resynthesize the blueprint, and then publish a preview version again. For more information,
   see [Resynthesis](custom-bp-concepts.md#resynthesis-concept "custom-bp-concepts.md#resynthesis-concept").

## (Optional) Step 4: Publish a custom blueprint preview version

You can publish a preview version of your custom blueprint to your space if you want to add it to your space's blueprints catalog. This allows
you to view the blueprint as a user before adding the non-preview version to the catalog. The preview version allows you to publish without taking up
an actual version. For example, if you work on a `0.0.1` version, you can publish and add a preview version, so new updates for a second version
can be published and added as `0.0.2`.

**To publish a preview version of a custom blueprint**

Navigate to the `Enable version `[version number]` at:`
link provided to enable your custom blueprint. This link is provided when running the `yarn` command in [Step 3: Preview a custom blueprint](#getting-started-publish-bp "#getting-started-publish-bp").

After creating, developing, previewing, and publishing your custom blueprint, you can publish and add the final blueprint version to your space's
blueprints catalog. For more information, see [Publishing a custom blueprint to a space](publish-bp.md "publish-bp.md") and [Adding a custom blueprint to a space blueprints catalog](add-bp.md "add-bp.md").
