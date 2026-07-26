# Conda recipe examples for Deadline Cloud

The
[conda\_recipes](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes")
directory in the deadline-cloud-samples repository contains sample tools
for creating an Amazon S3 conda channel and building packages into it. The
recipes use
[rattler-build](https://prefix-dev.github.io/rattler-build/ "https://prefix-dev.github.io/rattler-build/")
or, in some cases, the older
[conda-build](https://docs.conda.io/projects/conda-build/ "https://docs.conda.io/projects/conda-build/").

Each recipe directory includes a
`deadline-cloud.yaml` metadata file that lists the conda
platforms the recipe builds for and configures how the recipe is submitted
to Deadline Cloud. The `submit-package-job` command in the
`conda_recipes` directory submits a recipe to a queue whose
name starts with `Package` and uses the queue's job attachments
bucket as the conda channel.

For setup, see
[Create
a conda channel using S3](configure-jobs-s3-channel.md "configure-jobs-s3-channel.md"). For the underlying packaging concepts,
see
[Create
a conda package for an application or plugin](conda-package.md "conda-package.md").

To submit a Blender 4.5 build job, run the following from the
`conda_recipes` directory of the samples repository:

```
./submit-package-job blender-4.5
```

To submit a build for both Linux and Windows:

```
./submit-package-job blender-4.5 -p linux-64 -p win-64
```

To submit a build for every platform listed in
`deadline-cloud.yaml`:

```
./submit-package-job blender-4.5 --all-platforms
```

The
[conda\_build\_linux\_package](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/conda_build_linux_package "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/conda_build_linux_package")
job bundle in the directory is the Open Job Description template that
`submit-package-job` submits. It runs `conda-build`
or `rattler-build` on a worker, takes a recipe directory and
optional source archives as input, and writes the built package to your
queue's conda channel.

Source archives that recipes pull in by URL go in the
[archive\_files](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/archive_files "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/archive_files")
directory. Recipes that require an installer or redistributable archive
you have to download manually (such as Maya, Cinema 4D, or Nuke) read
from this directory at build time.

The repository also includes recipes that package the Deadline Cloud client
libraries themselves so that jobs can call Deadline Cloud APIs from inside a
queue:

- [deadline](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/deadline "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/deadline"): The Deadline Cloud Python client (`deadline` CLI and
  `deadline.job_attachments`), packaged for Linux, Windows,
  Linux ARM, and macOS.
- [openjd-adaptor-runtime](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/openjd-adaptor-runtime "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/openjd-adaptor-runtime"): The runtime that the DCC Open Job Description adaptors build on top of, packaged
  for Linux and Windows with Python 3.13.
  The following sections describe the recipe families available in the
  samples repository.

###### Topics

- [Build a Blender conda package for Deadline Cloud](examples-conda-blender.md "examples-conda-blender.md")
- [Build an Autodesk Maya conda package for Deadline Cloud](examples-conda-maya.md "examples-conda-maya.md")
- [Build a SideFX Houdini conda package for Deadline Cloud](examples-conda-houdini.md "examples-conda-houdini.md")
- [Build a Maxon Cinema 4D conda package for Deadline Cloud](examples-conda-cinema4d.md "examples-conda-cinema4d.md")
- [Build a Foundry Nuke conda package for Deadline Cloud](examples-conda-nuke.md "examples-conda-nuke.md")
- [Build an Autodesk 3ds Max conda package for Deadline Cloud](examples-conda-3dsmax.md "examples-conda-3dsmax.md")
- [Build an Adobe After Effects conda package for Deadline Cloud](examples-conda-aftereffects.md "examples-conda-aftereffects.md")
- [Build a KeyShot conda package for Deadline Cloud](examples-conda-keyshot.md "examples-conda-keyshot.md")
- [Build an Autodesk VRED Core conda package for Deadline Cloud](examples-conda-vred.md "examples-conda-vred.md")
- [Build an Epic Unreal Engine conda package for Deadline Cloud](examples-conda-unreal-engine.md "examples-conda-unreal-engine.md")
- [Build a V-Ray Standalone conda package for Deadline Cloud](examples-conda-vray.md "examples-conda-vray.md")
- [Build a NeRF Studio conda package for Deadline Cloud](examples-conda-nerfstudio.md "examples-conda-nerfstudio.md")
- [Build an Infinigen conda package for Deadline Cloud](examples-conda-infinigen.md "examples-conda-infinigen.md")
- [Build an AutoDock Vina conda package for Deadline Cloud](examples-conda-autodock-vina.md "examples-conda-autodock-vina.md")
- [Build an AYON Launcher conda package for Deadline Cloud](examples-conda-ayon.md "examples-conda-ayon.md")
