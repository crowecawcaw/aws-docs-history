# What is a Deadline Cloud workload

 With AWS Deadline Cloud, you can submit jobs to run your applications in the cloud and process data
 for the production of content or insights crucial to your business. Deadline Cloud uses [Open Job Description](https://github.com/OpenJobDescription/openjd-specifications "https://github.com/OpenJobDescription/openjd-specifications")
 (OpenJD) as the syntax for job templates, a specification designed for the needs of visual
 compute pipelines but applicable to many other use cases. Some example workloads include
 computer graphics rendering, physics simulation, and photogrammetry. 

Workloads scale from simple job bundles that users submit to a queue with either the CLI or
 an automatically generated GUI, to integrated submitter plugins that dynamically generate a job
 bundle for an application-defined workload. 


## How workloads arise from
 production


 To understand workloads in production contexts and how to support them with Deadline Cloud,
 consider how they come to be. Production may involve creating visual effects, animation,
 games, product catalog imagery, 3D reconstructions for building information modeling (BIM),
 and more. This content is typically created by a team of artistic or technical specialists
 running a variety of software applications and custom scripting. Members of the team pass data
 between each other using a production pipeline. Many tasks performed by the pipeline involve
 intensive computations that would take days if run on a user’s workstation. 


 Some examples of tasks in these production pipelines include: 



* Using a photogrammetry application to process photographs taken of a movie set to
 reconstruct a textured digital mesh.
* Running a particle simulation in a 3D scene to add layers of detail to an explosion
 visual effect for a television show.
* Cooking data for a game level into the form needed for external release and applying
 optimization and compression settings.
* Rendering a set of images for a product catalog including variations in color,
 background, and lighting.
* Running a custom-developed script on a 3D model to apply a look that was custom-built
 and approved by a movie director.

 These tasks involve many parameters to adjust to get an artistic result or to fine tune
 the output quality. Often there is a GUI to select those parameter values with a button or
 menu to run the process locally within the application. When a user runs the process, the
 application and possibly the host computer itself cannot be used to perform other operations
 because it uses the application state in memory and may consume all of the host computer’s CPU
 and memory resources. 


 In many cases the process is quick. During the course of production, the speed of the
 process slows down when the requirements for quality and complexity go up. A character test
 that took 30 seconds during development can easily turn into 3 hours when it is applied to the
 final production character. Through this progression, a workload that began life inside a GUI
 can grow too large to fit. Porting it to Deadline Cloud can boost the productivity of users running
 these processes because they get back full control of their workstation and can keep track of
 more iterations from the Deadline Cloud monitor. 


 There are two levels of support to aim for when developing support for a workload in
 Deadline Cloud: 



* Offloading the workload from the user workstation to a Deadline Cloud farm with no parallelism
 or speed-up. This may under-utilize the available compute resources in the farm, but the
 ability to shift long operations to a batch processing system enables users to get more
 done with their own workstation.
* Optimizing the parallelism of the workload so that it utilizes the Deadline Cloud farm's
 horizontal scale to complete quickly.

 There are times that it is obvious how to make a workload run in parallel. For example,
 each frame of a computer graphics render can be done independently. It’s important not to get
 stuck on this parallelism, however. Instead, understand that offloading a long-running
 workload to Deadline Cloud provides significant benefits, even when there is no obvious way to split
 the workload up. 


## The ingredients of a workload


 To specify a Deadline Cloud workload, implement a job bundle that users submit to a queue with the
 [Deadline Cloud CLI](https://github.com/aws-deadline/deadline-cloud "https://github.com/aws-deadline/deadline-cloud"). Much of the
 work in creating a job bundle is to write the job template, but there are more factors like
 how to provide the applications that the workload requires. Here are the essential things to
 consider when defining a workload for Deadline Cloud: 



* **The application to run**. The job must be able to launch
 application processes, and therefore needs an installation of the application available as
 well as any licensing the application uses, such as access to a floating license server.
 This is typically part of the farm configuration, and not embedded in the job bundle
 itself. 




	+ [Configure jobs using queue environments](configure-jobs.md "configure-jobs.md")
	+ [Connect customer-managed fleets to a license endpoint](../userguide/cmf-ubl.md "../userguide/cmf-ubl.md")
* **Job parameter definitions**. The user experience of
 submitting the job is affected greatly by the parameters it provides. Example parameters
 include data files, directories, and application configuration. 




	+ [Parameter values elements for job
	 bundles](build-job-bundle-parameters.md "build-job-bundle-parameters.md")
* **File data flow**. When a job runs, it reads input from
 files provided by the user, then writes its output as new files. To work with the job
 attachments and path mapping features, the job must specify the paths of the directories
 or specific files for these inputs and outputs. 




	+ [Using files in your jobs](using-files-in-your-jobs.md "using-files-in-your-jobs.md")
* **The step script**. The step script runs the application
 binary with the right command-line options to apply the provided job parameters. It also
 handles details like path mapping if the workload data files include absolute instead of
 relative path references. 




	+ [Job template elements for job bundles](build-job-bundle-template.md "build-job-bundle-template.md")

## Workload portability


 A workload is portable when it can run in multiple different systems without changing it
 each time you submit a job. For example, it might run on different render farms that have
 different shared file systems mounted, or on different operating systems like Linux or
 Windows. When you implement a portable job bundle, it's easier for users to run the job on
 their specific farm, or to adapt it for other use cases. 


 Here are some ways you can make your job bundle portable. 



* Fully specify the input data files needed by a workload, using `PATH` job
 parameters and asset references in the job bundle. This makes the job portable to farms
 based on shared file systems and to farms that make copies of the input data, like the
 Deadline Cloud job attachments feature.
* Make file path references for the input files of the job relocatable and usable on
 different operating systems. For example when users submit jobs from Windows
 workstations to run on a Linux fleet. 




	+ Use relative file path references, so if the directory containing them is moved
	 to a different location, references still resolve. Some applications, like [Blender](https://docs.blender.org/manual/en/latest/files/blend/open_save.html#files-blend-relative-paths "https://docs.blender.org/manual/en/latest/files/blend/open_save.html#files-blend-relative-paths"), support a choice between relative and absolute paths.
	+ If you can't use relative paths, support OpenJD [path mapping metadata](https://github.com/OpenJobDescription/openjd-specifications/wiki/How-Jobs-Are-Run#path-mapping "https://github.com/OpenJobDescription/openjd-specifications/wiki/How-Jobs-Are-Run#path-mapping") and translate the absolute paths according to how
	 Deadline Cloud provides the files to the job.
* Implement commands in a job using portable scripts. Python and bash are two examples
 of scripting languages that can be used this way. You should consider providing them both
 on all the worker hosts of your fleets. 




	+ Use the script interpreter binary, like `python` or `bash`,
	 with the script file name as an argument. This works on all operating systems
	 including Windows, compared to using a script file with its execute bit set on
	 Linux.
	+ Write portable bash scripts by applying these practices: 
	
	
	
	
		- Expand template path parameters in single quotes to handle paths with spaces
		 and Windows path separators.
		- When running on Windows, watch for issues related to MinGW automatic path
		 translation. For example, it transforms an AWS CLI command like `aws logs tail
		 /aws/deadline/...` into a command similar to `aws logs tail
		 "C:/Program Files/Git/aws/deadline/..."` and won't tail a log
		 correctly. Set the variable `MSYS_NO_PATHCONV=1` to turn this behavior
		 off.
		- In most cases, the same code works on all operating systems. When the code
		 needs to be different use an `if/else` construct to handle the cases. 
		
		
		
		```
		if [[ "$(uname)" == MINGW* || "$(uname -s)" == MSYS_NT* ]]; then
		    # Code for Windows
		elif [[ "$(uname)" == Darwin ]]; then
		    # Code for MacOS
		else
		    # Code for Linux and other operating systems
		fi
		```
	+ You can write portable Python scripts using `pathlib` to handle file
	 system path differences and avoid operating-specific features. The Python
	 documentation includes annotations for this, for example in the [signal library
	 documentation](https://docs.python.org/3/library/signal.html "https://docs.python.org/3/library/signal.html"). Linux-specific feature support is marked as “Availability:
	 Linux.”
* Use job parameters to specify application requirements. Use consistent conventions
 that the farm administrator can apply in [queue
 environments](configure-jobs.md "configure-jobs.md"). 




	+ For example, you can use the `CondaPackages` and/or
	 `RezPackages` parameters in your job, with a default parameter value that
	 lists the application package names and versions the job requires. Then, you can use
	 one of the [sample Conda or Rez queue environments](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/queue_environments "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/queue_environments") to provide a virtual environment for
	 the job.
