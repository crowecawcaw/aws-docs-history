

# Create a conda build recipe for Autodesk Maya to Arnold (MtoA) plugin
<a name="create-conda-recipe-mtoa-plugin"></a>

The Maya to Arnold (MtoA) plugin adds the Arnold renderer as an option within Maya. The [MtoA sample recipe](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/maya-mtoa-2026) on the GitHub website demonstrates how to package a plugin as a separate conda package that integrates with the host application package.

## Understanding the recipe
<a name="mtoa-recipe-structure"></a>

The [recipe.yaml](https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/conda_recipes/maya-mtoa-2026/recipe/recipe.yaml) on the GitHub website specifies a dependency on the `maya` package for both build and run requirements. The dependency uses a version constraint so that the plugin is only installed with a compatible Maya version.

The recipe uses the same source archives as the Maya recipe. The build script installs MtoA and creates a `mtoa.mod` file in the `$PREFIX/usr/autodesk/maya$MAYA_VERSION/modules` directory that the Maya package configures in `MAYA_MODULE_PATH`. Arnold and Maya use the same licensing technology, so the Maya package already includes the licensing information that Arnold needs.

## Building the MtoA package
<a name="mtoa-build-package"></a>

Build the Maya package before you build the MtoA package, because MtoA depends on Maya at build time. Use `rattler-build publish` to build and publish the package. From the `conda_recipes` directory, run the following command.

```
rattler-build publish maya-mtoa-2026/recipe/recipe.yaml \
    --to file://$HOME/my-conda-channel \
    --build-number=+1
```

The `rattler-build publish` command uses the target channel as the highest priority channel when resolving dependencies, so the `maya` package you published earlier is available automatically.

For other publishing options:
+ To publish to an Amazon S3 channel, see [Publish packages to an S3 conda channel](publish-packages-s3-channel.md).
+ To automate builds using a Deadline Cloud package building queue, see [Automate package builds with Deadline Cloud](automate-package-builds.md).