

# Create a conda build recipe for Autodesk Maya
<a name="create-conda-recipe-maya"></a>

Commercial applications like Autodesk Maya introduce additional packaging requirements compared to open source applications like Blender. The [Blender recipe](create-conda-recipe-blender.md) packages a simple relocatable archive under an open source license. Commercial applications are often distributed through installers and require license management configuration.

## Considerations for commercial applications
<a name="maya-commercial-considerations"></a>

The following considerations apply when packaging commercial applications. The details illustrate how each applies to Maya.
+ **Licensing** – Understand the licensing rights and restrictions of the application. You might need to configure a license management system. Read the [Autodesk Subscription Benefits FAQ about Cloud Rights](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Subscription-Benefits-FAQ-Cloud-Rights.html) and [Thin Client Licensing for Maya and MotionBuilder](https://www.autodesk.com/support/technical/article/caas/tsarticles/ts/2zqRBCuGDrcPZDzULJQ27p.html) on the Autodesk website to understand the cloud rights for Maya. Autodesk products rely on a `ProductInformation.pit` file that typically requires administrator access to configure. Product features for thin clients provide a relocatable alternative.
+ **System library dependencies** – Some applications depend on libraries not installed on service-managed fleet worker hosts. Maya depends on libraries including freetype and fontconfig. When these libraries are available in the system package manager, such as `dnf` for AL2023, you can use the package manager as a source. Because RPM packages are not built to be relocatable, you need to use tools such as `patchelf` to resolve dependencies within the Maya installation prefix.
+ **Administrator access for installation** – Some installers require administrator access. Service-managed fleets do not provide administrator access, so you need to install the application on a separate system and create an archive of the files for the package build. The Windows installer for Maya requires this approach. The [README.md](https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/conda_recipes/maya-2025/README.md) in the maya-2025 recipe on the GitHub website documents a repeatable procedure using a freshly launched Amazon Elastic Compute Cloud (Amazon EC2) instance.
+ **Plugin integration** – The sample Maya package defines `MAYA_NO_HOME=1` to isolate the application from user-level configuration, and adds module search paths to `MAYA_MODULE_PATH` so that plugin packages can place `.mod` files within the virtual environment. See the [Maya 2026 sample recipe](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/maya-2026#instructions-for-maya-plugin-packages) on the GitHub website for the full plugin integration convention.

## Understanding the recipe
<a name="maya-recipe-structure"></a>

The [recipe.yaml](https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/conda_recipes/maya-2026/recipe/recipe.yaml) file on the GitHub website defines the package metadata in [rattler-build template syntax](https://rattler-build.prefix.dev/latest/reference/recipe_file/#spec-reference) on the prefix.dev website. Review the following sections of the file:
+ **source** – References the installer archives, including the sha256 hash. On Linux, the source is the Autodesk installer archive. On Windows, the source includes both the installer archive and a `cleanMayaForCloud.py` script from Autodesk that prepares Maya for cloud deployment. Update the hashes when you change the source files, for example when packaging a new version.
+ **build** – Turns off the default binary relocation and DSO linking checks because the automatic mechanisms do not work correctly for the library and binary directories that Maya uses. On Linux, the recipe includes `patchelf` as a build dependency to manually set relative RPATHs.
+ **about** – Metadata about the application for browsing or processing the contents of a conda channel.

The build scripts ([build.sh](https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/conda_recipes/maya-2026/recipe/build.sh) for Linux, [build\_win.sh](https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/conda_recipes/maya-2025/recipe/build_win.sh) in the maya-2025 recipe for Windows) on the GitHub website include comments explaining each step. The scripts perform the following key tasks:
+ **Extract the installer** – Extracts the Maya installation files into the conda prefix. The Linux and Windows scripts handle this differently due to the installer formats. See the build scripts for details.
+ **Install system library dependencies** – On Linux, the script downloads and extracts system libraries that Maya needs but that are not present on service-managed fleet hosts. The script copies these libraries into the Maya `lib` directory so they are available within the conda environment.
+ **Set relative RPATHs with patchelf** – On Linux, the script uses `patchelf --add-rpath` to add `$ORIGIN`-relative paths to the shared libraries. This approach follows the conda recommendation to never use `LD_LIBRARY_PATH` in conda environments. The script patches libraries at multiple directory levels (`lib`, `lib/python*/site-packages`, `lib/python*/lib-dynload`) so that each library can find its dependencies relative to its own location. The recipe follows the best practice of setting `DT_RUNPATH` instead of `DT_RPATH`, which allows `LD_LIBRARY_PATH` to override the search path when needed for debugging.
+ **Configure thin client licensing** – The script sets up thin client licensing so that the `ProductInformation.pit` file can be located within the conda environment rather than requiring system-level administrator access. For more information, see [Thin Client Licensing for Maya and MotionBuilder](https://www.autodesk.com/support/technical/article/caas/tsarticles/ts/2zqRBCuGDrcPZDzULJQ27p.html) on the Autodesk website.
+ **Set up activation scripts** – The scripts create activate and deactivate scripts that set environment variables including `MAYA_LOCATION`, `MAYA_VERSION`, `MAYA_NO_HOME`, and `MAYA_MODULE_PATH`. On Windows, the scripts produce both `.sh` and `.bat` activation files because the Deadline Cloud sample queue environments use `bash` to activate environments on Windows.

## Building the Maya package
<a name="maya-build-package"></a>

Before you build the Maya package, download the Maya installer from your Autodesk account. For Linux, place the archive directly into the `conda_recipes/archive_files` directory. For Windows, follow the procedure in the [maya-2025 README.md](https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/conda_recipes/maya-2025/README.md) on the GitHub website to create the archive.

Use `rattler-build publish` to build and publish the package. The Maya recipe requires `patchelf` as a build dependency on Linux, which is available from [conda-forge](https://conda-forge.org/) on the conda-forge website. Add `-c conda-forge` to make the dependency available during the build. From the `conda_recipes` directory, run the following command.

```
rattler-build publish maya-2026/recipe/recipe.yaml \
    --to file://$HOME/my-conda-channel \
    --build-number=+1 \
    -c conda-forge
```

For other publishing options:
+ To publish to an Amazon S3 channel, see [Publish packages to an S3 conda channel](publish-packages-s3-channel.md).
+ To automate builds using a Deadline Cloud package building queue, see [Automate package builds with Deadline Cloud](automate-package-builds.md). To build both Linux and Windows packages, use the `--all-platforms` option with the `submit-package-job` script.

To render the turntable sample with Maya and Arnold, build both the [MtoA plugin](create-conda-recipe-mtoa-plugin.md) and [Maya adaptor](create-conda-recipe-maya-openjd.md) packages. After you publish all three packages, you can submit a test render job using the [turntable with Maya/Arnold job bundle](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/turntable_with_maya_arnold) from the Deadline Cloud samples repository on the GitHub website. See [Test your packages with a Maya render job](submit-render-maya-mtoa.md).