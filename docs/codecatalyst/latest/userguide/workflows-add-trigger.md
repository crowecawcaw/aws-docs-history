Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Starting a workflow run automatically using

triggers

You can start an Amazon CodeCatalyst workflow run automatically with a workflow trigger.

A _workflow trigger_, or simply a _trigger_, allows
you to start a workflow run automatically when certain events occur, like a code push. You might
want to configure triggers to free your software developers from having to start workflow runs
manually through the CodeCatalyst console.

You can use three types of trigger:

- **Push** – A code push trigger causes a workflow run
  to start whenever a commit is pushed.
- **Pull request** – A pull request trigger causes a
  workflow run to start whenever a pull request is either created, revised, or closed.
- **Schedule** – A schedule trigger causes a workflow
  run to start on a schedule that you define. Consider using a schedule trigger to run nightly
  builds of your software so that the latest build is ready for your software developers to
  work on the next morning.
  You can use push, pull request, and schedule triggers alone or in combination in the same
  workflow.

Triggers are optional—if you don't configure any, you can only start a workflow
manually.

###### Tip

To see a trigger in action, launch a project with a blueprint. Most blueprints contain
a workflow with a trigger. Look for the `Trigger` property in the blueprint's
workflow definition file. For more information about blueprints, see [Creating a project with a
blueprint](projects-create.md#projects-create-console-template "projects-create.md#projects-create-console-template").

###### Topics

- [Examples: Triggers in workflows](workflows-add-trigger-examples.md "workflows-add-trigger-examples.md")
- [Usage guidelines for triggers and
  branches](workflows-add-trigger-considerations.md "workflows-add-trigger-considerations.md")
- [Adding triggers to workflows](workflows-add-trigger-add.md "workflows-add-trigger-add.md")
