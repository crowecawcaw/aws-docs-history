Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Custom blueprints concepts

Here are some concepts and terms that you should know when working with custom blueprints in
CodeCatalyst.

###### Topics

- [Blueprint project](#blueprint-project-concept "#blueprint-project-concept")
- [Space blueprints](#space-blueprints-concept "#space-blueprints-concept")
- [Space blueprints catalog](#blueprint-catalog-concept "#blueprint-catalog-concept")
- [Synthesis](#synthesis-concept "#synthesis-concept")
- [Resynthesis](#resynthesis-concept "#resynthesis-concept")
- [Partial options](#partial-options-concept "#partial-options-concept")
- [Projen](#projen-concept "#projen-concept")

## Blueprint project

A blueprint project gives you the ability to develop and publish blueprints to your space. A source
repository is created during the project creation process, and the name of the repository is the one you
chose when entering the **Project resources** details. During the blueprint creation
process, if you choose to generate a workflow release, a publishing workflow is created in your
blueprint with the **Blueprint Builder** blueprint. The workflow automatically publishes
your latest version.

## Space blueprints

You can view and manage all blueprints from the **Space blueprints** table when you
navigate to the **Blueprints** section of your space. After blueprints are published to
your space, they are made available as a space blueprint to be added and removed from your space's blueprints
catalog. You can also manage publishing permissions and delete blueprints from in the **Blueprints**
section of your space. For more information, see [Viewing details, versions, and projects of a custom blueprint](view-bp.md "view-bp.md").

## Space blueprints catalog

You can view all added custom blueprints from a space's blueprints catalog. This is where a space member
can choose your custom blueprint to create a new project. This catalog is different to the CodeCatalyst catalog, which
already has available blueprints for all space members. For more information, see [Creating a comprehensive project with CodeCatalyst blueprints](project-blueprints.md "project-blueprints.md").

## Synthesis

Synthesis is the process of generating a CodeCatalyst project bundle that represents the source
code, configuration, and resources in a project. The bundle is then used by CodeCatalyst deployment API
operations to deploy into a project. The process can be run locally while developing your custom
blueprint to emulate project creation without having to create a project in CodeCatalyst. The following
commands can be used to perform synthesis:

```
yarn blueprint:synth             # fast mode
yarn blueprint:synth --cache     # wizard emulation mode
```

The blueprint starts itself by
calling the main `blueprint.ts` class with that option merged on
`defaults.json`. A new project bundle is generated under the
`synth/synth.`[options-name]`/proposed-bundle/`
folder. The output includes the project bundle that a custom blueprint generates, given the
options you set, including the [partial options](#partial-options-concept "#partial-options-concept") that you may have configured.

## Resynthesis

Resynthesis is the process of regenerating a blueprint with different blueprint options or
blueprint versions of existing projects. As a blueprint author, you can define custom merge
strategies in the custom blueprint code. You can also define ownership boundaries in an
`.ownership-file` to specify in which parts of the codebase a blueprint is
permitted to be updated. While the custom blueprint can propose updates to the
`.ownership-file`, project developers using the custom blueprint can
determine ownership boundaries for their projects. You can run resynthesis locally, and test and
update before publishing your custom blueprint. Use the following commands to perform
resynthesis:

```
yarn blueprint:resynth             # fast mode
yarn blueprint:resynth --cache     # wizard emulation mode
```

The blueprint starts itself by
calling the main `blueprint.ts` class with that option merged on
`defaults.json`. A new project bundle is generated under the
`synth/resynth.`[options-name]`/` folder. The
output includes the project bundle that a custom blueprint generates, given the options you set,
including the [partial options](#partial-options-concept "#partial-options-concept") that you may have configured.

The following contents are created after the synthesis and resynthesis processes:

- **proposed-bundle** - The output of synthesis when it is run with new options
  for the target blueprint version.
- **existing-bundle** - A mock of your existing project. If there's nothing in
  this folder, it's generated with the same output as he
  `proposed-bundle`.
- **ancestor-bundle** - A mock of what your blueprint would generate when run
  with either a prior version, prior options, or a combination. If there's nothing in this
  folder, it's generated with the same output as the `proposed-bundle`.
- **resolved-bundle** - The bundle is always regenerated and defaults to a
  three-way merge between the `proposed-bundle`,
  `existing-bundle`, and the `ancestor-bundle`. This
  bundle provides an emulation of what a resynthesis would output locally.

To learn more about blueprint output bundles, see [Generating files with resynthesis](merge-strategies-lm.md#three-way-merge-lm "merge-strategies-lm.md#three-way-merge-lm").

## Partial options

You can add option variations under `src/wizard-configuration/` that don't have to
enumerate the entirety of the `Options` interface, and the options are merged on top of the
`defaults.json` file. That allows you to tailor test cases across particular options.

**Example:**

`Options` interface:

```
{
  language: "Python" | "Java" | "Typescript",
  repositoryName: string
  ...
}
```

`defaults.json` file:

```
{
  language: "Python",
  repositoryName: "Myrepo"
  ...
}
```

Additional configuration tests:

- ```
  #wizard-config-typescript-test.json
  {
    language: "Typescript",
  }
  ```

````
* ```
#wizard-config-java-test.json
{
  language: "Java",
}
````

## Projen

Projen is an open-source tool that custom blueprints use to keep themselves updated and
consistent. Blueprints come as Projen packages because this framework provides you with the
ability to build, bundle, and publish projects, and you can use the interface to manage a
project's configurations and settings.

You can use Projen to update blueprints at scale, even after they're created. The Projen
tool is the underlying technology behind the blueprint synthesis that generates a project bundle.
Projen owns the configuration for a project, and it shouldn't impact you as a blueprint
author. You can run `yarn projen` to regenerate the configuration of your project
after adding dependencies, or you can change options in the `projenrc.ts`
file. Projen is also the underlying generation tool for custom blueprints to synthesize a
project. For more information, see the [projen
GitHub page](https://github.com/projen/projen "https://github.com/projen/projen"). To learn more about working with Projen, see the [Projen documentation](http://projen.io/ "http://projen.io/").
