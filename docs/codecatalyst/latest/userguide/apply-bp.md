Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Adding a blueprint in a project to integrate resources

You can add multiple blueprints in a project to incorporate functional components,
resources, and governance. Your projects can support various elements that are managed
independently in separate blueprints. Adding blueprints to a project reduces the need
to manually create resources and make software components functional. Your projects can
also stay current as requirements evolve. To learn more
about adding blueprints in your project, see [Working with lifecycle management as a blueprint user](lifecycle-management-user.md "lifecycle-management-user.md").

While configuring a blueprint's details, you can also choose to store the blueprint's
source code in a preferred third-party repository, where you can still manage the blueprint
and utilize the lifecycle management capabilities to keep your project up to date. For more
information, see [Add functionality to projects with extensions in CodeCatalyst](extensions.md "extensions.md") and
[Working with lifecycle management as a blueprint user](lifecycle-management-user.md "lifecycle-management-user.md").

###### Important

To add a blueprint in your CodeCatalyst project, you must be signed in with
an account that has the **Space administrator**, **Power user**, or
**Project administrator** role in the space.

###### Tip

After adding a blueprint to your project, you can configure your email and Slack notifications
to provide updates for the latest changes to the blueprint. For more information, see
[Sending notifications from CodeCatalyst](notifications.md "notifications.md").

**To add a blueprint to your project**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. In the CodeCatalyst console, navigate to the space, and then choose the project where you
   want to add a blueprint.
3. In the navigation pane, choose **Blueprints**, and then choose
   **Add blueprint**.

###### Tip

You can choose to add a blueprint by giving **Amazon Q** your
project requirements to have Amazon Q suggest a blueprint to you. For more information,
see [Using Amazon Q to choose
a blueprint when creating a project or adding functionality](getting-started-project-assistance.md#getting-started-project-assistance-create-apply-bp "getting-started-project-assistance.md#getting-started-project-assistance-create-apply-bp") and [Best practices when using Amazon Q to create projects
or add functionality with blueprints](projects-create.md#projects-create-amazon-q "projects-create.md#projects-create-amazon-q"). This feature is only available in
the US West (Oregon) Region.

This functionality requires that generative AI features are enabled for the space.
For more information, see [Managing
generative AI features](../adminguide/managing-generative-ai-features.md "../adminguide/managing-generative-ai-features.md"). 4. Choose a blueprint from the **CodeCatalyst blueprints** tab or a custom
blueprint from the **Space blueprints** tab, and then choose
**Next**. 5. Under **Blueprint details**, choose a blueprint version from the
**Target version** dropdown menu. The latest catalog version is automatically
selected. 6. (Optional) By default, the source code created by the blueprint is stored in a CodeCatalyst
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

7. Under **Configure blueprint**, configure the blueprint parameters. Depending
   on the blueprint, you may have the option to name the source repository.
8. Review the differences between the current blueprint version and your updated version. The
   difference displayed in a pull request shows the changes between the current version and the
   latest version, which is the desired version at the time the pull request was created. If no
   changes display, the versions might be identical, or you might have chosen the same version for
   both the current version and the desired version.
9. When you’re satisfied that the pull request contains the code and changes that you want
   reviewed, choose **Add blueprint**. After you create the pull request,
   you can add comments. Comments can be added to the pull request or to individual lines in files
   as well as to the overall pull request. You can add links to resourcesuch as filesby using the
   `@` sign, followed by the name of the file.

###### Note

The blueprint won’t be applied until the pull request is approved and merged. For more information, see
[Reviewing a pull request](pull-requests-review.md "pull-requests-review.md") and
[Merging a pull request](pull-requests-merge.md "pull-requests-merge.md").
Blueprint authors can also add a custom blueprint to projects in specified spaces that
don't have the blueprint available to create new projects or add to existing projects. For more information,
see [Publishing and adding a custom blueprint in specified spaces and projects](publish-bp.md#publish-preview-existing-project-bp "publish-bp.md#publish-preview-existing-project-bp").

If you no longer want to receive updates for a blueprint, you can disassociate the blueprint from your
project. For more information, see [Disassociating a blueprint from a project to stop updates](disassociate-bp.md "disassociate-bp.md").
