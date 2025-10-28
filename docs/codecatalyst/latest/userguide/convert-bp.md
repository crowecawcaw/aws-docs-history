Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Converting source repositories to custom blueprints

Custom blueprints allow you to incorporate best practices or new options across multiple
projects in a CodeCatalyst space. While you can create and develop a new custom blueprint from scratch,
you can also convert an existing CodeCatalyst or third-party source repository with code and established
best practices into a blueprint project. You can avoid copying relevant artifacts from that existing
repository into a blueprint project. After converting a source repository into a custom blueprint,
you can update, publish, and add the blueprint just like any other custom blueprint.

After converting a source repository into a custom blueprint, the source repository is
restructured to be a blueprint project, the contents of the repository are moved into a
`static-assets` folder within the repository, and relevant assets needed for a
blueprint are added into the repository. When the custom blueprint is used to create projects or
added to an existing project, workflow definitions stored in the converted source repository is also
added to projects by the blueprint.

###### Note

Resources such as environments and secrets aren't included when converting a source
repository into a custom blueprint. You need to manually copy or add those resources after
converting a source repository into a custom blueprint.

###### Important

To convert a source repository into a custom blueprint, you must be signed in with
an account that has the **Project administrator**, **Space administrator**,
or **Power user** role in the space.

###### To convert a source repository into a custom blueprint from the source repository list

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. In the CodeCatalyst console, navigate to the space, and then choose the project where you
   want to convert a source repository into a custom blueprint.
3. In the navigation pane, choose **Code**, choose **Source
   repositories**, and then choose the radio button of the source repository you want to convert
   into a custom blueprint.
4. Choose **Convert to blueprint** to convert your source repository into a custom
   blueprint.
   You can also convert CodeCatalyst repositories into custom blueprints from the source repository page in
   the CodeCatalyst console.

###### To convert a source repository into a custom blueprint from the source repository page

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. In the CodeCatalyst console, navigate to the space, and then choose the project where you
   want to convert a source repository into a custom blueprint.
3. In the navigation pane, choose **Code**, choose **Source
   repositories**, and then choose the name of the CodeCatalyst source repository you want to convert into a
   custom blueprint.
4. Choose the **More** dropdown menu, and then choose **Convert to
   blueprint** to convert your source repository into a custom blueprint.
   Once your source repository is converted into a custom blueprint, a release workflow is automatically
   run. After the run is successfully complete, the custom blueprint is published to your space's custom
   blueprints list. From there, you can add your converted custom blueprint to your space's catalog to create
   new projects or to be added to existing projects. For more information, see [Publishing a custom blueprint to a space](publish-bp.md "publish-bp.md") and [Adding a custom blueprint to a space blueprints catalog](add-bp.md "add-bp.md").

###### Important

To add a custom blueprint to your space's blueprints catalog, you must be signed in with
an account that has the **Space administrator** or **Power user** role
in the space.
