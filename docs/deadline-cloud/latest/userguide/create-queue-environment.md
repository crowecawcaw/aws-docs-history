# Create a queue environment

A queue environment is a set of environment variables and commands that set up fleet
 workers. You can use queue environments to provide software applications, environment
 variables, and other resources to jobs in the queue.

When you create a queue, you have the option of creating a default
 Conda queue environment. This environment provides service-managed
 fleets access to packages for partner DCC applications and renderers. The default
 environment For more information, see [Default Conda queue
 environment](#conda-queue-environment "#conda-queue-environment").

You can add queue environments using the console, or by editing the json or YAML
 template directly. This procedure describes how to create an environment with the
 console.

1. To add a queue environment to a queue, navigate to the queue and select the
 **Queue environments tab**.
2. Choose **Actions**, then **Create new with
 form**.
3. Enter a name and description for the queue environment.
4. Choose **Add new environment variable**, and then enter a
 name and value for each variable you add.
5. (Optional) Enter a priority for the queue environment. The priority indicates
 the order that this queue environment will run on the worker. Higher priority
 queue environments will run first.
6. Choose **Create queue environment**.

## Default Conda queue
 environment


When you create a queue associated with a service-managed fleet, you have the
 option of adding a default queue environment that supports [Conda](https://docs.conda.io/en/latest/ "https://docs.conda.io/en/latest/") to download
 and install packages in a virtual environment for your jobs.


If you add a default queue environment with the Deadline Cloud [console](https://console.aws.amazon.com/deadlinecloud/home "https://console.aws.amazon.com/deadlinecloud/home"), the environment is
 created for you. If you add a queue another way, such as the AWS CLI or with AWS CloudFormation,
 you'll need to create the queue environment yourself. To ensure you have the correct
 contents for the environment, you can refer to queue environment template YAML files
 on GitHub. For the contents of the default queue environment, see the [default queue environment YAML file](https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/queue_environments/conda_queue_env_from_console.yaml "https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/queue_environments/conda_queue_env_from_console.yaml") on GitHub.


There are other [queue environment templates](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/queue_environments#the-sample-queue-environments "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/queue_environments#the-sample-queue-environments") available on GitHub that you can use as a
 starting point for your own needs.


Conda provides packages from *channels*. A
 channel is a location where packages are stored. Deadline Cloud provides a channel,
 `deadline-cloud`, that hosts Conda packages that
 support partner DCC applications and renderers. Select each tab below to view the
 available packages for Linux or Windows.



Linux

* Blender




	+ `blender=3.6`
	+ `blender=4.2`
	+ `blender=4.5`
	+ `blender-openjd`
* Cinema 4D




	+ `cinema4d=2025`
	+ `cinema4d-openjd`
* Houdini




	+ `houdini=19.5`
	+ `houdini=20.0`
	+ `houdini=20.5`
	+ `houdini=21.0`
	+ `houdini-openjd`
* Maya




	+ `maya=2024`
	
	
	`maya=2025`
	
	
	`maya=2026`
	+ `maya-mtoa=2024.5.3`
	
	
	`maya-mtoa=2025.5.4`
	
	
	`maya-mtoa=2026.5.5`
	+ `maya-openjd`
	+ `maya-redshift=2025.4`
	+ `maya-vray=2025.7`
	+ `maya-vray=2026.7`
* Nuke




	+ `nuke=15`
	+ `nuke=16`
	+ `nuke-openjd`
* VRED




	+ `vredcore=2025`
	+ `vredcore=2026`


Windows

* After Effects




	+ `aftereffects=24.6`
	+ `aftereffects=25.1`
	+ `aftereffects=25.2`
* Cinema 4D




	+ `cinema4d=2024`
	+ `cinema4d=2025`
	+ `cinema4d-openjd`
* KeyShot




	+ `keyshot=2024`
	+ `keyshot-openjd`
* Unreal Engine




	+ `unrealengine=5.4`
	+ `unrealengine=5.5`
	+ `unrealengine=5.6`
	+ `unrealengine-openjd`



###### Note

For **Cinema 4D 2025**, the Linux Conda package does not 
 support substance 3D materials. Jobs with this material will fail with the following message:


```
Commandline: ./modules/io_substance/source/substance_framework/src/details/detailsengine.cpp:794: SubstanceAir::Details::Engine::Context::Context(SubstanceAir::Details::Engine&, SubstanceAir::RenderCallbacks*): Assertion `res==0' failed.
```
We recommend that you submit those jobs to Windows instead. For 
 **Cinema 4D OpenJD,** to prevent any timeout issues, 
 we recommend you set task run timeouts to double their expected render time, 
 instead of using the default 2 day timeout.


When you submit a job to a queue with the default Conda
 environment, the environment adds two parameters to the job. These parameters
 specify the Conda packages and channels to use to configure the job's
 environment before tasks are processed. The parameters are:



* `CondaPackages` – a space-separated list of [package match specifications](https://docs.conda.io/projects/conda-build/en/stable/resources/package-spec.html#package-match-specifications "https://docs.conda.io/projects/conda-build/en/stable/resources/package-spec.html#package-match-specifications"), such as `blender=3.6`
 or `numpy>1.22`. The default is empty to skip creating a virtual
 environment.
* `CondaChannels` – a space separated list of [Conda channels](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/channels.html "https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/channels.html") such as
 `deadline-cloud`, `conda-forge`, or
 `s3://`amzn-s3-demo-bucket`/conda/channel`.
 The default is `deadline-cloud`, a channel available to
 service-managed fleets that provides partner DCC applications and renderers.

When you use an integrated submitter to send a job to Deadline Cloud from your DCC, the
 submitter populates the value of the `CondaPackages` parameter based on
 the DCC application and submitter. For example, if you are using Blender the
 `CondaPackage` parameter is set to `blender=3.6.*
 blender-openjd=0.4.*`.


We recommend you pin any submissions to only the versions listed in the table
 above, for example blender=3.6. This is because patch releases affect the available
 packages. For example, when we release Blender 3.6.17, we will no
 longer distribute Blender 3.6.16. Any submissions pinned to
 blender=3.6.16 will fail. If you pin to blender=3.6, then you will get the latest
 distributed patch version and jobs will not be impacted. By default, the DCC
 submitters pin to the current versions listed in the table above, excluding the
 patch number, such as blender=3.6.
