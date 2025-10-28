Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Developing a custom action

You can develop a custom action to use in your workflows using the CodeCatalyst Action
Development Kit (ADK). You can then publish the action to the CodeCatalyst actions catalog, so
that other CodeCatalyst users can view and use it in their workflows.

**To develop, test, and publish an action (high-level tasks)**

1. Install the required tools and packages necessary to develop an action.
2. Create a CodeCatalyst repository to store your action code.
3. Initialize the action. This lays down the source files required by the action,
   including an action definition file (`action.yml`) that you
   can update with your own code.
4. Bootstrap the action code to get the necessary tools and libraries to build,
   test, and release the action project.
5. Build the action on your local computer, and push the changes to your CodeCatalyst
   repository.
6. Test the action with unit tests locally, and run the ADK-generated workflow in
   CodeCatalyst.
7. Publish the action to the CodeCatalyst actions catalog by choosing the
   **Publish** button in the CodeCatalyst console.
   For detailed steps, see the [Amazon CodeCatalyst Action Development Kit Developer Guide](../adk/what-is-action-development-kit.md "../adk/what-is-action-development-kit.md").
