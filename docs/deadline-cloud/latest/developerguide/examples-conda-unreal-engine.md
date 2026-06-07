# Build an Epic Unreal Engine conda package for Deadline Cloud

The
[unreal-engine](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/unreal-engine "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/unreal-engine")
conda recipe builds an Epic Unreal Engine conda package.

Unlike other recipes in this repository, this one is designed to be
built _locally_ on a machine where Unreal Engine is
already installed. Unreal Engine packages are large (UE 5.6 is approximately
20 GiB across about 80,000 files), so submitting them to a queue as a job
attachment is impractical.

To use the recipe:

1. Install Unreal Engine on your Windows machine. The default source
   path in the recipe is the Epic Games Launcher path
   `C:\Program Files\Epic Games\UE_5.6`. Adjust
   `recipe/recipe.yaml` for your version or custom source build
   location.
2. Install
   [rattler-build](https://rattler-build.prefix.dev/ "https://rattler-build.prefix.dev/") and
   enable Windows long path support.
3. Build and publish the package to your conda channel:

```
rattler-build publish `path-to-recipe-file` --to `publish-conda-channel`
```

The recipe README includes step-by-step instructions for adapting it to
your Unreal Engine version, including custom source builds.
