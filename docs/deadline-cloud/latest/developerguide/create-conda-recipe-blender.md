# Create a conda build recipe for
 Blender

You can use different applications to create a conda build recipe. Blender is free to
 use and is simple to package with conda. The Blender Foundation provides  [application archives](https://download.blender.org/release/Blender4.2/ "https://download.blender.org/release/Blender4.2/") for
 multiple operating systems. We created a sample conda build recipe that uses the Windows
 .zip and the Linux .tar.xz files. In this section, learn how to use the [Blender 4.2 conda build recipe](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/blender-4.2 "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/blender-4.2"). 

The  [deadline-cloud.yaml](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/blender-4.2 "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/blender-4.2") file specifies the conda platforms and other metadata for
 submitting package jobs to Deadline Cloud. This recipe includes local source archive information to
 demonstrate how that works. The linux-64 conda platform is set to build in a default job
 submission to match the most common configuration. The deadline-cloud.yaml looks similar to
 the following: 


```
condaPlatforms:
  - platform: linux-64
    defaultSubmit: true
    sourceArchiveFilename: blender-4.2.1-linux-x64.tar.xz
    sourceDownloadInstructions: 'Run "curl -LO https://download.blender.org/release/Blender4.2/blender-4.2.1-linux-x64.tar.xz"'
  - platform: win-64
    defaultSubmit: false
    sourceArchiveFilename: blender-4.2.1-windows-x64.zip
    sourceDownloadInstructions: 'Run "curl -LO https://download.blender.org/release/Blender4.2/blender-4.2.1-windows-x64.zip"'

```
Review the files in the `recipe` directory. The metadata for the recipe is in
  [recipe/meta.yaml](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/blender-4.2/recipe/meta.yaml "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/blender-4.2/recipe/meta.yaml"). You can also read the conda build [meta.yaml](https://docs.conda.io/projects/conda-build/en/latest/resources/define-metadata.html "https://docs.conda.io/projects/conda-build/en/latest/resources/define-metadata.html") documentation to learn more, such as how the file is a template to
 generate YAML. The template is used to specify the version number just once, and to provide
 different values based on the operating system. 

You can review the build options selected in `meta.yaml` to turn off various
 binary relocation and dynamic shared object (DSO) linking checks. These options control how
 the package works when it's installed into a conda virtual environment at any directory
 prefix. The default values simplify packaging every dependency library into a separate
 package, but when binary repackaging an application, you need to change them. 

If the application you're packaging requires additional dependency libraries or you are
 packaging plugins for an application separately, you may encounter DSO errors. These errors
 occur when the dependency is not in the library search path for the executable or library
 that needs it. Applications rely on libraries being in globally defined paths, like
 `/lib` or `/usr/lib`, when installed on a system. However, since
 conda virtual environments can be placed anywhere, there is no absolute path to use. Conda
 uses relative RPATH features, which both Linux and macOS support, to handle this. 
 Refer to the conda build documentation on  [Making packages relocatable](https://docs.conda.io/projects/conda-build/en/latest/resources/make-relocatable.html "https://docs.conda.io/projects/conda-build/en/latest/resources/make-relocatable.html") for more information.

Blender does not require any RPATH adjustment, as the application archives were built
 with this in mind. For applications that do require it, you can use the same tools that
 conda build does: `patchelf` on Linux and `install_name_tool` on
 macOS.

During the package build, the [build.sh](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/blender-4.2/recipe/build.sh "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/blender-4.2/recipe/build.sh") or [build\_win.sh](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/blender-4.2/recipe/build_win.sh "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/blender-4.2/recipe/build_win.sh") (called by `bld.bat`) script runs to install files into
 an environment prepared with the package dependencies. These scripts copy the installation
 files, create symlinks from `$PREFIX/bin`, and set up the activation scripts. On
 Windows, it does not create symlinks but instead adds the Blender directory to the PATH in
 the activation script.

We use `bash` instead of a `cmd.exe` .bat
 file for the Windows part of the conda build recipe, as this provides more consistency
 across the build scripts. Refer to the  [Deadline Cloud developer guide's](what-is-a-deadline-cloud-workload.md#workload-portability "what-is-a-deadline-cloud-workload.md#workload-portability") recommendation on workload portability for tips on using
 `bash` on Windows. If you've installed [git for Windows](https://gitforwindows.org/ "https://gitforwindows.org/") to clone the [deadline-cloud-samples](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/ "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/") git repository, you already have access to
 `bash`. 

The  [conda build environment variables](https://docs.conda.io/projects/conda-build/en/latest/user-guide/environment-variables.html "https://docs.conda.io/projects/conda-build/en/latest/user-guide/environment-variables.html") documentation lists the values available for
 use in the build script. These values include `$SRC_DIR` for the source archive
 data, `$PREFIX` for the installation directory, `$RECIPE_DIR` to
 access other files from the recipe, `$PKG_NAME` and `$PKG_VERSION` for
 package name and version, and `$target_platform` for the target conda platform.
 


## Submit the Blender 4.2 package job


You can build your own Blender 4.2 conda package to render jobs, by downloading the
 Blender archive and then submitting a job to the package building queue. The queue sends the
 job to the associated fleet to build the package and reindex the conda channel.


These instructions use git from a bash-compatible shell to get an OpenJD package build
 job and some conda recipes from the [Deadline Cloud samples GitHub
 repository](https://github.com/aws-deadline/deadline-cloud-samples "https://github.com/aws-deadline/deadline-cloud-samples"). You also need the following:



* If you are using Windows, a version of bash, git BASH, is installed when you
 install git.
* You must have the [Deadline Cloud
 CLI](https://github.com/aws-deadline/deadline-cloud "https://github.com/aws-deadline/deadline-cloud") installed.
* You must be logged into the [Deadline Cloud monitor](../userguide/working-with-deadline-monitor.md "../userguide/working-with-deadline-monitor.md").

1. Open the Deadline Cloud configuration GUI using the following command and set the default
 farm and queue to your package building queue.



```
deadline config gui
```
2. Use the following command to clone the Deadline Cloud samples GitHUb repository.



```
git clone https://github.com/aws-deadline/deadline-cloud-samples.git
```
3. Change to the `conda_recipes` directory in the
 `deadline-cloud-samples` directory.



```
cd deadline-cloud-samples/conda_recipes
```
4. Run the script called `submit-package-job`. The script provides
 instructions for downloading Blender the first time that you run the script.



```
./submit-package-job blender-4.2/
```
5. Follow the instructions for downloading Blender. When you have the archive, run the
 `submit-package-job` script again.



```
./submit-package-job blender-4.2/
```

After you submit the job, use the Deadline Cloud monitor to view the progress and status of the job as
 it runs.


The lower left of the monitor shows the two steps of the job, building the package and
 then reindexing. The lower right shows the individual steps for each task. In this example,
 there is one step for each task.



![The Deadline Cloud monitor showing the progress and status of a job building the Blender package.](../../../images/deadline-cloud/latest/developerguide/images/Conda-Figure3.png)

In the lower left of the monitor are the two steps of the job, building the package and
 then reindexing the conda channel. In the lower right are the individual tasks for each
 step. In this example there is only one task for each step.


When you right click on the task for the package building step and choose **View
 logs**, the monitor shows a list of session actions that show how the task is
 scheduled on the worker. The actions are:



* **Sync attachments** – This action copies the
 input job attachments or mounts a virtual file system, depending on the setting used for
 the job attachments file system.
* **Launch Conda** – This action is from the queue
 environment added by default when you created the queue. The job doesn't specify any
 conda packages, so it finishes quickly and doesn't create a conda virtual
 environment.
* **Launch CondaBuild Env** – This action creates a
 custom conda virtual environment that includes the software needed to build a conda
 package and reindex a channel. It installs from the [conda-forge](https://conda-forge.org/ "https://conda-forge.org/") channel.
* **Task run** – This action builds the Blender
 package and uploads the results to Amazon S3.

As the actions run, they send logs in a structured format to Amazon CloudWatch. When a job is
 complete, select **View logs for all tasks** to see additional logs about
 the set up and tear down of the environment that the job runs in.
