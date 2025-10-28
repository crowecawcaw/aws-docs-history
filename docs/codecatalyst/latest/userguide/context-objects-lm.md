Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Accessing context objects for project details

As a blueprint author, you can access context from the blueprint’s project during synthesis to get information like space and project names,
or existing files in a project’s source repository. You can also get details like the phase of resynthesis that the blueprint is generating. For
example, you can access context to know if you’re resynthesizing to generate an ancestor bundle or proposed bundle. Existing code context can then
be used to transform your code in your repository. For example, you can write your own resynthesis strategy to set specific code standards. The
strategy can be added to the `blueprint.ts` file for small blueprints, or you can create a separate file for strategies.

The following example shows how you can find files in a project's context, set a workflow builder, and set a blueprint-vended resynthesis
strategy for a particular file:

```
const contextFiles = this.context.project.src.findAll({
      fileGlobs: ['**/package.json'],
    });

    // const workflows = this.context.project.src.findAll({
    //   fileGlobs: ['**/.codecatalyst/**.yaml'],
    // });

    const security = new WorkflowBuilder(this, {
      Name: 'security-workflow',
    });
    new Workflow(this, repo, security.getDefinition());
    repo.setResynthStrategies([
      {
        identifier: 'force-security',
        globs: ['**/.codecatalyst/security-workflow.yaml'],
        strategy: MergeStrategies.alwaysUpdate,
      },
    ]);


    for (const contextFile of contextFiles) {
      const packageObject = JSON.parse(contextFile.buffer.toString());
      new SourceFile(internalRepo, contextFile.path, JSON.stringify({
        ...packageObject,
      }, null, 2));
    }
  }
```
