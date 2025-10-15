# Using a Deadline Cloud submitter

A *submitter* is a tool that integrates with your digital content
 creation so that you can send render jobs directly to Deadline Cloud. This integration streamlines your
 workflow by eliminating the need to switch between applications or manually transfer files.
 This saves time and reduces the potential for errors. 

Submitters are available for many popular DCC applications. Installing a submitter, adds
 Deadline Cloud specific options to your application's interface, typically in the render settings or
 export menu.

With a Deadline Cloud submitter you can:


* Configure render job parameters in your familiar DCC environment
* Submit jobs to Deadline Cloud without leaving your application
* Reduce the potential for errors associated with manual file transfers
* Save time because you don't need to switch between applications
To find a submitter for your DCC application, check the [supported submitters](supported-submitters.md "supported-submitters.md") list. Then follow the
 instructions in [Set up Deadline Cloud submitters](submitter.md "submitter.md") to install the
 submitter. 

If your application doesn't have a supported submitter, you can still run jobs for your
 application. There may be a sample job bundle available for it, or you can construct a simple
 submitter for the application's render CLI command. For more information, see [Open
 Job Description (OpenJD) templates for Deadline Cloud](../developerguide/build-job-bundle.md "../developerguide/build-job-bundle.md") in the *Deadline Cloud Developor
 Guide*.

The examples in this topic use the Blender submitter, but the steps for
 using other submitters are similar.

###### Note

To use a submitter, you must be signed in to the Deadline Cloud monitor.

The submitter has four tabs:

###### Topics

* [Shared job settings tab](#submiter-shared "#submiter-shared")
* [Job-specific settings tab](#submiter-job-settings "#submiter-job-settings")
* [Job attachments tab](#submiter-attachments "#submiter-attachments")
* [Host requirements tab](#submiter-host "#submiter-host")

## Shared job settings tab



![The shared job settings tab of the Blender submitter. The settings in the tab are the defaults.](/images/deadline-cloud/latest/userguide/images/submitter-shared.png)

The shared job settings tab contains the settings that are common to all jobs sent to
 Deadline Cloud using the submitter. The three sections are:



* *Job properties* â Sets the overall properties of the
 job. These properties are present in submitters for all DCC applications.
* *Deadline Cloud settings* â Shows the farm and queue that the job
 is sent to. To change the farm and queue, use the **Settings...**
 button at the bottom of the submitter.
* *Queue environment* â Sets the parameter values defined
 in the queue environment. Deadline Cloud adds the default parameter values for your DCC
 application, you can add additional values if necessary.

## Job-specific settings tab



![The job-specific settings tab of the Blender submitter.](/images/deadline-cloud/latest/userguide/images/submitter-job-settings.png)

The job-specific settings tab contains the setting specific to your DCC application.
 Specify these settings based on the options available in your application.



## Job attachments tab



![The shared job attachments tab of the Blender submitter.](/images/deadline-cloud/latest/userguide/images/submitter-attachments.png)

The job attachments tab shows all of the files needed to complete a render. The
 submitter tries to find all of the files required for the render. The files that it
 identifies appear in the lists in italics.


You can add additional input files and directories that contain other assets required
 for the render that were not automatically detected.


If your job writes files to multiple output directories, you must specify the
 directories here so that the are part of the job download.


## Host requirements tab



![The shared host requirements tab of the Blender submitter.](/images/deadline-cloud/latest/userguide/images/submitter-host.png)

The host requirements tabs sets the fleet capabilities required to process the job.
 Capabilities are specified for the entire fleet, not individual workers in the fleet.

If your queue has associated resource limits, use the **Add amount**
 button to specify the limit. For more information, see  [Create resource limits for jobs](build-job-limits.md "build-job-limits.md")
