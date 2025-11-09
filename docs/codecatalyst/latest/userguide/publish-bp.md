Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Publishing a custom blueprint to a space

Before you can add a custom blueprint to your space's blueprints catalog, you must publish it to the space. You
can also view the blueprint in the CodeCatalyst console before publishing. You can publish a preview version or a normal
version of your blueprint.

###### Important

If you want to use blueprint packages from external sources, consider the risks that may come
with those packages. You're responsible for the custom blueprints that you add to your space
and the code they generate.

###### Important

To publish a custom blueprint to your CodeCatalyst space, you must be signed in with
an account that has the **Space administrator** or **Power user**
role in the space.

###### Topics

- [Viewing and publishing a preview version of a custom blueprint](#publish-preview-bp "#publish-preview-bp")
- [Viewing and publishing a normal version of a custom blueprint](#publish-normal-bp "#publish-normal-bp")
- [Publishing and adding a custom blueprint in specified spaces and projects](#publish-preview-existing-project-bp "#publish-preview-existing-project-bp")

## Viewing and publishing a preview version of a custom blueprint

You can publish a preview version of your custom blueprint to your space if you want to add it to your space's blueprints catalog. This allows
you to view the blueprint as a user before adding the non-preview version to the catalog. The preview version allows you to publish without taking up
an actual version. For example, if you work on a `0.0.1` version, you can publish and add a preview version, so new updates for a second version
can be published and added as `0.0.2`.

After making changes, rebuild your custom blueprint's package by running the `package.json` file,
and preview your changes.

**To view and publish a preview version of a custom blueprint**

1. Resume your Dev Environment. For more information, see [Resuming a Dev Environment](devenvironment-resume.md "devenvironment-resume.md")
2. Open a working terminal in your Dev Environment.
3. (Optional) In a working terminal, install necessary dependencies for your project if you didn't install them already. Use the following command:

```
yarn
```

4. (Optional) If you made changes to the `.projenrc.ts` file, regenerate the
   configuration of your project before building and previewing your blueprint. Use the following command:

```
yarn projen
```

5. Rebuild and preview your custom blueprint using the following command. Use the following command:

```
yarn blueprint:preview
```

Navigate to the `See this blueprint at:` link provided to preview your custom blueprint.
Check that the UI, including text, appears as you expected based on your configuration. If you
want to change your custom blueprint, you can edit the `blueprint.ts` file,
resynthesize the blueprint, and then publish a preview version again. For more information,
see [Resynthesis](custom-bp-concepts.md#resynthesis-concept "custom-bp-concepts.md#resynthesis-concept"). 6. (Optional) You can publish a preview version of your custom blueprint, which can then be added to your
space's blueprints catalog. Navigate to the `Enable version `[preview version number]` at:`
link to publish a preview version to your space.

You can emulate project creation without having to create a project in CodeCatalyst. To synthesize
your project, use the following command:

```
yarn blueprint:synth
```

A blueprint is generated in the `synth/synth.`[options-name]`/proposed-bundle/` folder.
For more information, see [Synthesis](custom-bp-concepts.md#synthesis-concept "custom-bp-concepts.md#synthesis-concept").

If you're updating your custom blueprint, instead, use the following command to resynthesize your project:

```
yarn blueprint:resynth
```

A blueprint is generated in the `synth/synth.`[options-name]`/proposed-bundle/` folder.
For more information, see [Resynthesis](custom-bp-concepts.md#resynthesis-concept "custom-bp-concepts.md#resynthesis-concept").

After publishing your preview version, you can then add the blueprint so space members can use it to create new projects or add
in existing projects. For more information, see [Adding a custom blueprint to a space blueprints catalog](add-bp.md "add-bp.md").

## Viewing and publishing a normal version of a custom blueprint

After you're done developing and previewing your custom blueprint, you can view and publish the new version that you want to
add to your space's blueprints catalog. The release workflow generated when creating a project automatically publishes changes that are pushed.
If you turned off the workflow generation when creating the blueprint, your blueprint isn't automatically made available to be added to your
space's blueprints catalog. You can still publish your custom blueprint to your space after running a `yarn` command.

**To view and publish a custom blueprint**

1. Resume your Dev Environment. For more information, see [Resuming a Dev Environment](devenvironment-resume.md "devenvironment-resume.md")
2. Open a working terminal in your Dev Environment.
3. - If you opted out of the release workflow generation when creating your blueprint, use the following command:

   ```
   yarn blueprint:release
   ```

   You can still navigate to the `See this blueprint at:` link provided to view your custom blueprint.

   Publish the updated version of your custom blueprint, which can then be added to your space's blueprints catalog. Navigate to
   the `Enable version `[release version number]` at:` link to publish the latest version to your space.
   - If you opted in for a release workflow when creating your blueprint, the latest blueprint version is automatically published when
     changes are pushed. Use the following commands:

   ```
   git add .
   ```

   ```
   git commit -m "`commit message`"
   ```

   ```
   git push
   ```

After publishing your normal version, you can then add the blueprint so space members can use it to create new projects or add
in existing projects. For more information, see [Adding a custom blueprint to a space blueprints catalog](add-bp.md "add-bp.md").

## Publishing and adding a custom blueprint in specified spaces and projects

By default, the `blueprint:preview` and `blueprint:release` commands publish into the CodeCatalyst space you created
the blueprint in. If you have multiple Enterprise spaces, you can preview and publish the same blueprint in those spaces as well. You can also add a blueprint
to an existing project of another space.

**To publish or add a custom blueprint in a specified space**

1. Resume your Dev Environment. For more information, see [Resuming a Dev Environment](devenvironment-resume.md "devenvironment-resume.md").
2. Open a working terminal in your Dev Environment.
3. (Optional) Install necessary dependencies for your project if you didn't install them already. Use the following command:

```
yarn
```

4.  Use the `--space` tag to publish a preview or normal version to a specified space. For example:

        * ```
        yarn blueprint:preview --space my-awesome-space # publishes under a "preview" version tag to 'my-awesome-space'
        ```

        Example output:



        ```
        Enable version 0.0.1-preview.0 at: https://codecatalyst.aws/spaces/my-awesome-space/blueprints
        Blueprint applied to [NEW]: https://codecatalyst.aws/spaces/my-awesome-space/blueprints/%40amazon-codecatalyst%2Fmyspace.my-blueprint/publishers/1524817d-a69b-4abe-89a0-0e4a9a6c53b2/versions/0.0.1-preview.0/projects/create
        ```
        * ```
        yarn blueprint:release --space my-awesome-space # publishes normal version to 'my-awesome-space'
        ```

        Example output:



        ```
        Enable version 0.0.1 at: https://codecatalyst.aws/spaces/my-awesome-space/blueprints
        Blueprint applied to [NEW]: https://codecatalyst.aws/spaces/my-awesome-space/blueprints/%40amazon-codecatalyst%2Fmyspace.my-blueprint/publishers/1524817d-a69b-4abe-89a0-0e4a9a6c53b2/versions/0.0.1/projects/create
        ```

    Use the `--project` to add a preview version of a custom blueprint to an existing project in a specified space. For example:

```
yarn blueprint:preview --space my-awesome-space --project my-project # previews blueprint application to an existing project
```

Example output:

```
Enable version 0.0.1-preview.1 at: https://codecatalyst.aws/spaces/my-awesome-space/blueprints
Blueprint applied to [my-project]: https://codecatalyst.aws/spaces/my-awesome-space/projects/my-project/blueprints/%40amazon-codecatalyst%2FmySpace.my-blueprint/publishers/1524817d-a69b-4abe-89a0-0e4a9a6c53b2/versions/0.0.1-preview.1/add
```
