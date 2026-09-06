# Create a conda package for an application or plugin

A conda package is a compressed archive of software written in any language. Conda
supports a variety of operating system and architecture combinations, so you can package
full applications like Blender, Maya, and
Nuke alongside libraries for Python and other languages. For more
information about conda packages, see the [Packages](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/packages.html "https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/packages.html") documentation on the conda website.

To use a conda package, you install it into a virtual environment. A conda virtual
environment has a _prefix directory_ where packages
are installed. Installing a package uses hardlinking or reflinking of files when supported,
so creating multiple environments with the same packages does not use significant additional
disk space. To use a virtual environment, you activate it to set environment variables.
Activation runs scripts that packages provide, giving each package the opportunity to modify
PATH or other environment variables. Conda packages typically contain applications or
libraries, but the flexible activation means they can also point to applications installed
on a shared filesystem.

Making a custom package involves three stages: a _recipe_ contains the build
instructions, a _package_ is the built artifact (`.conda` or
`.tar.bz2` file), and a _channel_ hosts packages for
installation. The `rattler-build publish` command handles all three steps—it
can build a recipe into a package and publish to a channel, or it can take a package
artifact directly to publish it.

The [conda-forge](https://conda-forge.org/ "https://conda-forge.org/") community maintains
package recipes for a broad set of open source software, and hosts package artifacts in the
`conda-forge` channel on the conda-forge website. You can configure your
queue to include
`conda-forge` as a package source, and then build custom packages that depend on
conda-forge packages to run. For Linux, conda-forge hosts a full compiler toolchain
including CUDA support, with consistent compiling and linking options selected. You can use
conda-forge packages as dependencies in your own recipes, or install them alongside your
custom packages in the same environment.

You can combine an entire application, including dependencies, into a conda package. The
packages Deadline Cloud provides in the [deadline-cloud channel](../userguide/create-queue-environment.md#conda-queue-environment "../userguide/create-queue-environment.md#conda-queue-environment") for service-managed fleets use this binary repackaging
approach. This organizes the same files as an installation to fit the conda virtual
environment.

###### Note

Large applications can require tens of GB of free disk space for the source archive,
extracted files, and build output. Make sure that you use a disk with enough available space
for the package build output.

## Package an application

When repackaging an application for conda, there are two goals:

- Most files for the application should be separate from the primary conda virtual
  environment structure. Environments can then mix the application with packages from other
  sources like [conda-forge](https://conda-forge.org/ "https://conda-forge.org/") on the
  conda-forge website.
- When a conda virtual environment is activated, the application should be available
  from the PATH environment variable.

###### To repackage an application for conda

1. Write conda build recipes that install the application into a subdirectory like
   `$CONDA_PREFIX/opt/`<application-name>``.
   This separates it from the standard prefix directories like `bin` and
   `lib`.
2. Add symlinks or launch scripts to `$CONDA_PREFIX/bin` to run the
   application binaries.

Alternatively, create activate.d scripts that the `conda activate` command
will run to add the application binary directories to the PATH. On Windows, where symlinks
are not supported everywhere environments can be created, use application launch or
activate.d scripts instead. 3. Some applications depend on libraries not installed by default on Deadline Cloud
service-managed fleets. For example, the X11 window system is usually unnecessary for
non-interactive jobs, but some applications still require it to run without a graphical
interface. You must provide those dependencies within the package you create. 4. If the application supports plugins, provide a clear convention that plugin packages
should follow to integrate with the application in a virtual environment. For example,
the [Maya 2026 sample recipe](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/maya-2026#instructions-for-maya-plugin-packages "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/maya-2026#instructions-for-maya-plugin-packages") on the GitHub website documents conventions for
Maya plugins. 5. Ensure you follow the copyright and license agreements for the applications you
package. We recommend using a private Amazon S3 bucket for your conda channel to control
distribution and limit package access to your farm.

Sample recipes for the packages in the `deadline-cloud` channel are
available in the [Deadline Cloud samples repository](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes#readme "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes#readme") on the GitHub website.

## Package a plugin

Application plugins can be packaged as their own conda packages. When creating a
plugin package, follow these guidelines:

- Include the host application package as both a build and a run dependency in the
  build recipe `recipe.yaml`. Use a version
  constraint so that the build recipe is only installed with compatible packages.
- Follow the host application package conventions for registering the plugin.

## Adaptor packages

Some Deadline Cloud application integrations use an _adaptor_ that extends the application
interface to simplify [writing job templates](building-jobs.md "building-jobs.md"). An
adaptor is a command-line interface with support for running a background daemon,
reporting status, and applying path mapping. For example, the
[deadline-cloud-for-maya](https://github.com/aws-deadline/deadline-cloud-for-maya/ "https://github.com/aws-deadline/deadline-cloud-for-maya/")
repository on the GitHub website includes an integrated job submission GUI and a
Maya adaptor that is available as the
`maya-openjd` package on service-managed fleets. For more information about adaptors and the adaptor runtime, see the [Open Job Description Adaptor Runtime](https://github.com/OpenJobDescription/openjd-adaptor-runtime-for-python#readme "https://github.com/OpenJobDescription/openjd-adaptor-runtime-for-python#readme") on the GitHub website.

Job submissions from Deadline Cloud submitter GUIs include a `CondaPackages`
parameter value that specifies the conda packages to include in a virtual environment for
running the job. The `CondaPackages` parameter value for Maya
typically looks like `maya=2026.* maya-openjd=0.15.* maya-mtoa` and might
contain alternative entries for plugin packages. When the queue environment sets up a
conda virtual environment for running the job, it resolves these package names and version
constraints to be compatible and adds all the dependency packages they need to run. Each
adaptor and plugin package specifies what it is compatible with, including which versions
of Maya, which versions of Python, and other dependencies.

To build your own adaptor packages, you can use sample recipes such as the [maya-openjd recipe](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/maya-openjd "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/maya-openjd") on the GitHub website. Build on the packages for
Python and other dependencies provided by [conda-forge](https://conda-forge.org/ "https://conda-forge.org/") on the conda-forge website. You might need to build the [deadline](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/deadline "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/deadline") and [openjd-adaptor-runtime](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/openjd-adaptor-runtime "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/openjd-adaptor-runtime") recipes on the GitHub website first to satisfy
dependencies.
