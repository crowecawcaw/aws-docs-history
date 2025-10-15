# Create a conda build recipe for Autodesk Maya

You can package commercial applications as conda packages. In [Create a conda build recipe for Blender](conda-package.md#create-conda-recipe-blender "conda-package.md#create-conda-recipe-blender"), you learned how to package an 
 application that is available as a simple relocatable archive file and under open source license terms.
 Commercial applications are often distributed via installers and may have a license management 
 system to work with.

The following list builds on the basics covered in [Create a conda package for an application](conda-package.md "conda-package.md") with requirements commonly involved with 
 packaging commercial applications. The details in sub-bullets illustrate how you can apply 
 the guidelines to Maya.


* Understand the licensing rights and restrictions of the application. You might need 
 to configure a license management system. Where the application does not include 
 enforcement, you will need to configure your farm according to your rights.




	+ Read the [Autodesk Subscription Benefits FAQ about Cloud Rights](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Subscription-Benefits-FAQ-Cloud-Rights.html "https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Subscription-Benefits-FAQ-Cloud-Rights.html") 
	 to understand the cloud rights for Maya that might apply to you. 
	 Configure your Deadline Cloud farm as necessary.
	+ Autodesk products rely on a file called `ProductInformation.pit`.
	 Most configuration of this file requires administrator access to the system, 
	 which is not available on service-managed fleets. Product features for thin 
	 clients provide a relocatable way to handle this. See 
	 [Thin Client Licensing for Maya and MotionBuilder](https://www.autodesk.com/support/technical/article/caas/tsarticles/ts/2zqRBCuGDrcPZDzULJQ27p.html "https://www.autodesk.com/support/technical/article/caas/tsarticles/ts/2zqRBCuGDrcPZDzULJQ27p.html") to learn more.
* Some applications depend on libraries not installed on service-managed fleet worker hosts, 
 so the package will have to provide them. This could be within the application package directly, 
 or placed in a separate dependency package. 
 




	+ Maya depends on a number of such libraries, including freetype and fontconfig. 
	 When these libraries are available in the system package manager, such as in `dnf` for 
	 AL2023, you can use it as a source for the application. Because these RPM packages are not built
	 to be relocatable, you will need to use tools such as `patchelf` to ensure dependencies 
	 are resolved within the Maya installation prefix.
* Installation might require administrator access. Since service-managed fleets do not provide administrator
 access, you will need to perform an installation on a system with this access. Then, create an archive 
 of the files needed for the package build job to use. 
 




	+ The Windows installer for Maya requires administrator access, so building the
	 conda package for it involves a manual process to first create such an archive.
* The application configuration, including how plugins register with it, can be defined at the operating
 system or user level. When placed in a conda virtual environment, plugins need a way to integrate with 
 the application in a way that is contained and never writes files or other data outside the virtual 
 environment prefix. We suggest you set this up from the application's conda package. 
 




	+ The sample Maya package defines the environment variable `MAYA_NO_HOME=1` 
	 to isolate it from user level configuration, and adds module search paths to `MAYA_MODULE_PATH`
	 so that plugins packaged separately can integrate from within the virtual environment. The sample 
	 MtoA package places a .mod file in one of these directories to load at 
	 Maya startup.
###### Write the recipe metada

1. Open the GitHub [deadline-cloud-samples/conda\_recipes/maya-2025](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/maya-2025 "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/maya-2025") directory in your browser or in a text editor in your
 local clone of the repository.


The file `deadline-cloud.yaml` describes the conda build platforms to build packages for and where 
 to get the application from. The recipe sample specifies both Linux and Windows builds, and that 
 only Linux is submitted by default.
2. Download the full Maya installers from your Autodesk login. For Linux, the 
 package build can use the archive directly, so place it directly into the `conda_recipes/archive_files` 
 directory. For Windows, the installer requires administrator access to run. You will need to run the 
 installer and collect the necessary files into an archive for the package recipe you want to use. The 
 [README.md](https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/conda_recipes/maya-2025/README.md "https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/conda_recipes/maya-2025/README.md") file in the recipe documents a repeatable procedure to create this artifact. The procedure uses
 a freshly launched Amazon EC2 instance to provide a clean environment for installation that you can then terminate 
 after saving the result. To package other applications that require administrator access, you can follow 
 a similar procedure once you determine the set of files the application needs.
3. Open the [recipe/recipe.yaml](https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/conda_recipes/maya-2025/recipe/recipe.yaml "https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/conda_recipes/maya-2025/recipe/recipe.yaml") and [recipe/meta.yaml](https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/conda_recipes/maya-2025/recipe/meta.yaml "https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/conda_recipes/maya-2025/recipe/meta.yaml") files to review or edit the settings for rattler-build and for conda-build. You can 
 set the package name and version for the application you are packaging.


The **source** section includes a reference to the archives, including the sha256 hash of the files. Whenever
 you change these files, for example to a new version, you will need to calculate and update these values.


The **build** section mainly contains options to turn off the default binary relocation options, as the automatic
 mechanisms will not work correctly for the particular library and binary directories the package uses.


Finally, the **about** section lets you enter some metadata about the application that can be used when 
 browsing or processing the contents of a conda channel.
###### Write the package build script

1. The package build scripts in the Maya sample conda build recipe include comments explaining the steps
 the scripts perform. Read through the comments and commands to discover the following:




	* How the recipe handles the RPM file from Autodesk
	* The changes the recipe applies to make the installation relocatable to the conda virtual environments that the 
	 recipe is installed in
	* How the recipe sets utility variables such as `MAYA_LOCATION` and `MAYA_VERSION` that 
	 your software can use to understand the Maya it is running.
2. For Linux, open the [recipe/build.sh](https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/conda_recipes/maya-2025/recipe/build.sh "https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/conda_recipes/maya-2025/recipe/build.sh") file to review or edit the package build script. 


For Windows, open the [recipe/build\_win.sh](https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/conda_recipes/maya-2025/recipe/build_win.sh "https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/conda_recipes/maya-2025/recipe/build_win.sh") file to review or edit the package build script.
###### Submit a job that builds the Maya packages

1. Enter the `conda_recipes` directory in your clone of the GitHub [deadline-cloud-samples](https://github.com/aws-deadline/deadline-cloud-samples "https://github.com/aws-deadline/deadline-cloud-samples") repository.
2. Make sure that your Deadline Cloud farm is configured for your Deadline Cloud CLI. If you followed the steps to 
 [Create a conda channel using Amazon S3](configure-jobs-s3-channel.md "configure-jobs-s3-channel.md") then your farm should be configured for your CLI.
3. Run the following command to submit a job that builds both Linux and Windows packages.


 `./submit-package-job maya-2025 --all-platforms`
