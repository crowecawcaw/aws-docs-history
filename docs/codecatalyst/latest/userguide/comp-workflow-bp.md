Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Adding workflow components to a blueprint

A workflow is used by Amazon CodeCatalyst projects to run actions based on triggers. You can use workflow components to
build and put together workflow YAML files. For more information, see [Workflow YAML definition](workflow-reference.md "workflow-reference.md").

**To import Amazon CodeCatalyst blueprints workflows components**

In your `blueprint.ts` file, add the following:

```
import { WorkflowBuilder, Workflow } from '@amazon-codecatalyst/codecatalyst-workflows'
```

###### Topics

- [Workflow components examples](#comp-workflows-examples-bp "#comp-workflows-examples-bp")
- [Connecting to an environment](#comp-workflows-connect-env-bp "#comp-workflows-connect-env-bp")

## Workflow components examples

### WorkflowBuilder component

You can use a class to build a workflow definition. The definition can be given to a workflow
component for rendering in a repository.

```
import { WorkflowBuilder } from '@amazon-codecatalyst/codecatalyst-workflows'

const workflowBuilder = new WorkflowBuilder({} as Blueprint, {
  Name: 'my_workflow',
});

// trigger the workflow on pushes to branch 'main'
workflowBuilder.addBranchTrigger(['main']);

// add a build action
workflowBuilder.addBuildAction({
  // give the action a name
  actionName: 'build_and_do_some_other_stuff',

  // the action pulls from source code
  input: {
    Sources: ['WorkflowSource'],
  },

  // the output attempts to autodiscover test reports, but not in the node modules
  output: {
    AutoDiscoverReports: {
      Enabled: true,
      ReportNamePrefix: AutoDiscovered,
      IncludePaths: ['**/*'],
      ExcludePaths: ['*/node_modules/**/*'],
    },
  },
  // execute some arbitrary steps
  steps: [
    'npm install',
    'npm run myscript',
    'echo hello-world',
  ],
  // add an account connection to the workflow
  environment: convertToWorkflowEnvironment(myEnv),
});
```

### Workflow Projen component

The following example shows how a Projen component can be used to write a workflow YAML to a repository:

```
import { Workflow } from '@amazon-codecatalyst/codecatalyst-workflows'

...

const repo = new SourceRepository
const blueprint = this;
const workflowDef = workflowBuilder.getDefinition()

// creates a workflow.yaml at .aws/workflows/${workflowDef.name}.yaml
new Workflow(blueprint, repo, workflowDef);

// can also pass in any object and have it rendered as a yaml. This is unsafe and may not produce a valid workflow
new Workflow(blueprint, repo, {... some object ...});
```

## Connecting to an environment

Many workflows need to run in an AWS account connection. Workflows handle this by allowing actions
to connect to environments with account and role name specifications.

```
import { convertToWorkflowEnvironment } from '@amazon-codecatalyst/codecatalyst-workflows'


const myEnv = new Environment(...);

// can be passed into a workflow constructor
const workflowEnvironment = convertToWorkflowEnvironment(myEnv);


// add a build action
workflowBuilder.addBuildAction({
  ...
  // add an account connection to the workflow
  environment: convertToWorkflowEnvironment(myEnv),
});
```
