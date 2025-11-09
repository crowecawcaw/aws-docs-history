Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Developing a custom blueprint to meet project requirements

Before publishing a custom blueprint, you can develop the blueprint to meet specific
requirements. You can develop your custom blueprint and test the blueprint by creating a project
when previewing. You can develop the custom blueprint to include project components, such as
specific source code, account connections, workflows, issues, or any other component that can be
created in CodeCatalyst.

###### Important

If you want to use blueprint packages from external sources, consider the risks that may come
with those packages. You're responsible for the custom blueprints that you add to your space
and the code they generate.

###### Important

To develop a custom blueprint in your CodeCatalyst space, you must be signed in with
an account that has the **Space administrator** or **Power user**
role in the space.

**To develop or update a custom blueprint**

1. Resume your Dev Environment. For more information, see [Resuming a Dev Environment](devenvironment-resume.md "devenvironment-resume.md").

If you don't have a Dev Environment, you must first create one. For more information, see [Creating a Dev Environment](devenvironment-create.md "devenvironment-create.md"). 2. Open a working terminal in your Dev Environment. 3. If you opted in for a release workflow when creating your blueprint, the latest blueprint version is
automatically published. Pull the changes to make sure the `package.json` file has the
incremented version. Use the following command:

```
git pull
```

4. In the `src/blueprint.ts` file, edit the options of your custom
   blueprint. The `Options` interface is interpreted by the CodeCatalyst wizard
   dynamically to generate a selection user interface (UI). You can develop your custom
   blueprint by adding components and supported tags. For more information, see [Modifying blueprint features with a front-end wizard](wizard-bp.md "wizard-bp.md"), [Adding environment components to a blueprint](comp-env-bp.md "comp-env-bp.md"), [Adding region components to a blueprint](region-comp-bp.md "region-comp-bp.md"),
   [Adding repository and source code components to a blueprint](comp-repo-source-bp.md "comp-repo-source-bp.md"), [Adding workflow components to a blueprint](comp-workflow-bp.md "comp-workflow-bp.md"), and
   [Adding Dev Environments components to a blueprint](comp-dev-env-bp.md "comp-dev-env-bp.md").

You can also view the blueprints SDK and sample blueprints for additional support when developing your custom blueprint. For more information, see the
[open-source GitHub repository](https://github.com/aws/codecatalyst-blueprints "https://github.com/aws/codecatalyst-blueprints").
Custom blueprints provide preview bundles as a result of a successful synthesis. The project
bundle represents the source code, configuration, and resources in a project, and it's used by
CodeCatalyst deployment API operations to deploy into a project. If you want to continue developing
your custom blueprint, rerun the blueprint synthesis process. For more information, see [Custom blueprints concepts](custom-bp-concepts.md "custom-bp-concepts.md").
