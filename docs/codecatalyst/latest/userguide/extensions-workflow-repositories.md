

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Automatically starting a workflow run after third-party repository events
<a name="extensions-workflow-repositories"></a>

You can use a linked GitHub repository, Bitbucket repository, or GitLab project repository as the source for a workflow, where changes to a specified branch in a linked GitHub repository, Bitbucket repository, or GitLab project repository automatically start a workflow run.

A *workflow* is an automated procedure that describes how to build, test, and deploy your code as part of a continuous integration and continuous delivery (CI/CD) system. A workflow defines a series of steps, or *actions*, to take during a workflow run. A workflow also defines the events, or *triggers*, that cause the workflow to start. To set up a workflow, you create a *workflow definition file* using the CodeCatalyst console's [visual or YAML editor](https://docs.aws.amazon.com/codecatalyst/latest/userguide/flows.html#workflow.editors).

**Tip**  
For a quick look at how you might use workflows in a project, [create a project with a blueprint](https://docs.aws.amazon.com/codecatalyst/latest/userguide/projects-create.html#projects-create-console-template). Each blueprint deploys a functioning workflow that you can review, run, and experiment with.

When you configure a workflow to use a linked GitHub repository, Bitbucket repository, or GitLab project repository, the workflow configuration file is stored in that GitHub repository, Bitbucket repository, or GitLab project repository. The workflow configuration is a YAML file that defines the workflow name, triggers, resources, artifacts, and actions. For more information about the workflow configuration file, see [Workflow YAML definition](workflow-reference.md).

The workflow configuration file must be in the `./codecatalyst/workflows/` directory in your GitHub repository, Bitbucket repository, or GitLab project repository.

You can use the workflow editor to create and configure workflows. For more information see [Getting started with workflows](workflows-getting-started.md) and [Connecting source repositories to workflows](workflows-sources.md).

## Adding triggers to start workflow runs
<a name="extensions-workflow-trigger-repositories"></a>

You can configure a CodeCatalyst workflow to automatically start a run when code is pushed to the specified branch of your GitHub or Bitbucket repository. To start a workflow run automatically, add a trigger to the `Triggers` section of the workflow configuration file.

### Example: A simple code push trigger
<a name="extensions-workflows-add-trigger-examples-push-simple"></a>

The following example shows a trigger that starts a workflow run whenever code is pushed to any branch in your source repository.

```
Triggers:
  - Type: PUSH
```

### Example: A simple pull request trigger
<a name="extensions-workflows-add-trigger-examples-push-simple"></a>

The following example shows a trigger that starts a workflow run whenever a pull request is created against any branch in your source repository.

```
Triggers:
  - Type: PULLREQUEST
    Events:
      - OPEN
```

For more information, see [Starting a workflow run automatically using triggers](workflows-add-trigger.md).