Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Sequencing actions

By default, when you add actions to a workflow, they are added side by side in the
[visual editor](workflow.md#workflow.editors "workflow.md#workflow.editors"). This means that the actions
will run in parallel when you start a workflow run. If you want actions to run in
sequential order (and appear vertically in the visual editor), you must set up
dependencies between them. For example, you might set up a `Test` action to
depend on the `Build` action so that the test action runs after the build
action.

You can set up dependencies between actions and action groups. You can also configure
one-to-many dependencies so that one action depends on several others in order to start.
Consult the guidelines in [Setting up dependencies between
actions](workflows-depends-on-set-up.md "workflows-depends-on-set-up.md") to ensure your dependency setup
conforms with the workflow's YAML syntax.

###### Topics

- [Examples of how to configure
  dependencies between actions](workflows-depends-on-examples.md "workflows-depends-on-examples.md")
- [Setting up dependencies between
  actions](workflows-depends-on-set-up.md "workflows-depends-on-set-up.md")
