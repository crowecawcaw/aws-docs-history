# Create a conda package for an application or plugin

You can combine an entire application, including dependencies, into a conda package. The
packages Deadline Cloud provides in the [deadline-cloud channel](../userguide/create-queue-environment.md#conda-queue-environment "../userguide/create-queue-environment.md#conda-queue-environment") for service-managed fleets use this binary repackaging
approach. This organizes the same files as an installation to fit the conda virtual
environment.

When repackaging an application for conda, there are two goals:

- Most files for the application should be separate from the primary conda virtual
  environment structure. Environments can then mix the application with packages from other
  sources like [conda-forge](https://conda-forge.org/ "https://conda-forge.org/").
- When a conda virtual environment is activated, the application should be available
  from the PATH environment variable.

###### To repackage an application for conda

1. To repackage an application for conda, write conda build recipes that install the
   application into a subdirectory like
   `$CONDA_PREFIX/opt/`<application-name>``.
This separates it from the standard prefix directories like `bin`and`lib`.
2. Then, add symlinks or launch scripts to `$CONDA_PREFIX/bin` to run the
   application binaries.

Alternatively, create activate.d scripts that the `conda activate` command
will run to add the application binary directories to the PATH. On Windows, where symlinks
are not supported everywhere environments can be created, use application launch or
activate.d scripts instead. 3. Some applications depend on libraries not installed by default on Deadline Cloud
service-managed fleets. For example, the X11 window system is usually unnecessary for
non-interactive jobs, but some applications still require it to run without a graphical
interface. You must provide those dependencies within the package you create. 4. Ensure you follow the copyright and license agreements for the applications you
package. We recommend using a private Amazon S3 bucket for your conda channel to control
distribution and limit package access to your farm.
Sample recipes for all the packages in the deadline-cloud channel are available
in the [Deadline Cloud Samples GitHub repository](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes").

###### To package a plugin for conda

- Application plugins can be packaged as their own conda packages. When creating a plugin package:
  - Include the host application package as both a build and a run dependency in the build recipe `meta.yaml`
    and `recipe.yaml`. Use a version constraint so that the build recipe is only installed with compatible packages.
  - Follow the host application package conventions for registering the plugin.
