Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Adding issues components to a blueprint

In CodeCatalyst, you can monitor features, tasks, bugs, and any other work involved in your project.
Each piece of work is kept in a distinct recordcalled an issue. Each issue can have a description, assignee,
status, and other properties, which you can search for, group and filter on. You can view your issues using
the default views, or you can create your own views with custom filtering, sorting, or grouping. For more
information about concepts related to issues, see [Issues concepts](issues-concepts.md "issues-concepts.md")
and [Quotas for issues in CodeCatalyst](issues-quotas.md "issues-quotas.md").

The issue component generates a JSON representation of an issue. The component takes in an ID field and issue
definition as input.

**To import Amazon CodeCatalyst blueprints issues components**

In your `blueprint.ts` file, add the following:

```
import {...} from '@amazon-codecatalyst/blueprint-component.issues'
```

###### Topics

- [Issues components examples](#comp-issues-examples-bp "#comp-issues-examples-bp")

## Issues components examples

### Creating an issue

```
import { Issue } from '@amazon-codecatalyst/blueprint-component.issues';
...
new Issue(this, 'myFirstIssue', {
  title: 'myFirstIssue',
  content: 'This is an example issue.',
});
```

### Creating a high-priority issue

```
import { Workflow } from '@amazon-codecatalyst/codecatalyst-workflows'
...
const repo = new SourceRepository
const blueprint = this;
const workflowDef = workflowBuilder.getDefinition()

// Creates a workflow.yaml at .aws/workflows/${workflowDef.name}.yaml
new Workflow(blueprint, repo, workflowDef);

// Can also pass in any object and have it rendered as a yaml. This is unsafe and may not produce a valid workflow
new Workflow(blueprint, repo, {... some object ...});
```

### Creating a low-priority issue with labels

```
import { Issue } from '@amazon-codecatalyst/blueprint-component.issues';
...
new Issue(this, 'myThirdIssue', {
  title: 'myThirdIssue',
  content: 'This is an example of a low priority issue with a label.',
  priority: 'LOW',
  labels: ['exampleLabel'],
});
```
