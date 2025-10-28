Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Handling dependencies, mismatches, and tooling

Incorrect dependency management can lead to build failures and runtime issues for those using your
custom blueprints. Outdated tooling and components may prevent blueprint users from accessing the latest
features and bug fixes. You can manage dependencies, handle dependency mismatches, as well as upgrade
toolings and components to ensure all dependencies rely on the same component versions and components are
synchornized.

###### Topics

- [Adding dependencies](#add-dependencies "#add-dependencies")
- [Handling dependency type mismatches](#handle-dependency-mismatches "#handle-dependency-mismatches")
- [Using yarn and npm](#use-yarn-npm "#use-yarn-npm")
- [Upgrading tooling and components](#upgrade-tooling-components "#upgrade-tooling-components")

## Adding dependencies

As a blueprint author, you might need to add packages to your blueprint, such as
`@amazon-codecatalyst/blueprint-component.environments`. You need to update the
`projen.ts` file with that package, and then regenerate the configuration of
your project with [Projen](https://github.com/projen/projen "https://github.com/projen/projen"). Projen acts as the
project model for each blueprint codebase, which provides the ability to push backwards-compatible
tooling updates by changing the way that the model renders configuration files. The
`package.json` file is a file that is partially owned by the Projen model. Projen
acknowledges dependency versions included in the package.json file, but other options need to
originate from the model.

**To add a dependency and update a `projenrc.ts` file**

1. In the `projen.ts` file, navigate to the deps section.
2. Add the dependency you want to use in your blueprint.
3. Use the following command to regenerate the configuration of your project:

```
yarn projen && yarn
```

## Handling dependency type mismatches

After a [Yarn](https://yarnpkg.com/ "https://yarnpkg.com/") update, you might get the following
error regarding a repository parameter:

```
Type 'SourceRepository' is missing the following properties from type 'SourceRepository': synthesisSteps, addSynthesisStep
```

The error is due a dependency mismatch that happens when one component relies on a newer version
of another component, but the relying component is pinned to an older version. The error can be fixed
by making all your components rely on the same version so that the version synchronized between them.
It’s best to keep al blueprint-vended packages under the same latest version (`0.0.x`),
unless you’re certain about how you’re handling the versions. The following example shows how the
`package.json` file can be configured so all the dependencies rely on the same
version:

```
...
"@caws-blueprint-component/caws-environments": "^0.1.12345",
"@caws-blueprint-component/caws-source-repositories": "^0.1.12345",
"@caws-blueprint-component/caws-workflows": "^0.1.12345",
"@caws-blueprint-component/caws-workspaces": "^0.1.12345",
"@caws-blueprint-util/blueprint-utils": "^0.1.12345",
...
"@caws-blueprint/blueprints.blueprint": "*",
```

After configuring the versions for all dependencies, use the following command:

```
yarn install
```

## Using yarn and npm

Blueprints use [Yarn](https://yarnpkg.com/ "https://yarnpkg.com/") for tooling. Using
[npm](https://www.npmjs.com/ "https://www.npmjs.com/") and Yarn will cause tooling problems because the way
that dependency trees are resolved by each is different. To avoid such issues, it’s best to use Yarn
only.

If you accidentally installed dependencies using npm, you can remove the generated
`package-lock.json` file, and make sure your `.projenrc.ts`
file is updated with the dependencies you need. You regenerate the configuration of your project with
Projen.

Use the following to regenerate from the model:

```
yarn projen
```

After making sure your .projenrc.ts file is updated with the necessary dependencies, use the following
command:

```
yarn
```

## Upgrading tooling and components

Occasionally, you might want to upgrade your tooling and components to bring in new features available.
You’re recommended to keep all the components on the same version unless you’re certain about how you’re
handling the versions. Versions are synchronized between components, so the same versions for all components
ensures proper dependency between them.

### Using Yarn workspace monorepo

Use the following command to upgrade utils and components from the root of a custom blueprint’s
repository:

```
yarn upgrade @amazon-codecatalyst/*
```

Use the following command if you’re not using a monorepo:

```
yarn upgrade —pattern @amazon-codecatalyst/*
```

Other options you can use to upgrade tooling and components:

- Use npm view `@caws-blueprint-component/<some-component>` to get the latest
  version.
- Manually increase to the latest version by setting the version in your package.json file and using
  the following command:`yarn`. All components and utils should have the same version.
