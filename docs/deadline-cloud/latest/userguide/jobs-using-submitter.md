

# Using a Deadline Cloud submitter
<a name="jobs-using-submitter"></a>

A *submitter* is a tool that integrates with your digital content creation (DCC) application so that you can send render jobs directly to Deadline Cloud without switching between applications or manually transferring files.

Submitters are available for many popular DCC applications. Installing a submitter adds Deadline Cloud specific options to your application's interface, typically in the render settings or export menu.

With a Deadline Cloud submitter you can:
+ Configure render job parameters in your familiar DCC environment
+ Submit jobs to Deadline Cloud without leaving your application
+ Reduce the potential for errors associated with manual file transfers
+ Save time by switching between applications less often

To find a submitter for your DCC application and instructions for installing it, see the [Set up your workstation](submitter.md) page. 

If your application doesn't have a supported submitter, you can still run jobs for your application. There might be a sample job bundle available for it, or you can construct a simple submitter for the application's render CLI command. For more information, see [Open Job Description (OpenJD) templates for Deadline Cloud](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/build-job-bundle.html) in the *Deadline Cloud Developer Guide*.

The examples in this topic use the Blender submitter, but the steps for using other submitters are similar.

**Note**  
To use a submitter, you must be signed in to the Deadline Cloud monitor.

The submitter has four tabs.

**Topics**
+ [Shared job settings tab](#submiter-shared)
+ [Job-specific settings tab](#submiter-job-settings)
+ [Job attachments tab](#submiter-attachments)
+ [Host requirements tab](#submiter-host)

## Shared job settings tab
<a name="submiter-shared"></a>

![The shared job settings tab of the Blender submitter. The settings in the tab are the defaults.](http://docs.aws.amazon.com/deadline-cloud/latest/userguide/images/submitter-shared.png)


The shared job settings tab contains the settings that are common to all jobs sent to Deadline Cloud using the submitter. The three sections are:
+ Job properties – Sets the overall properties of the job. These properties are present in submitters for all DCC applications.
+ Deadline Cloud settings – Shows the farm and queue that the job is sent to. To change the farm and queue, use the **Settings...** button at the bottom of the submitter.
+ Queue environment – Sets the parameter values defined in the queue environment. Deadline Cloud adds the default parameter values for your DCC application, you can add additional values if necessary.

## Job-specific settings tab
<a name="submiter-job-settings"></a>

![The job-specific settings tab of the Blender submitter.](http://docs.aws.amazon.com/deadline-cloud/latest/userguide/images/submitter-job-settings.png)


The job-specific settings tab contains the settings specific to your DCC application. Specify these settings based on the options available in your application.

## Job attachments tab
<a name="submiter-attachments"></a>

![The shared job attachments tab of the Blender submitter.](http://docs.aws.amazon.com/deadline-cloud/latest/userguide/images/submitter-attachments.png)


The job attachments tab shows all of the files needed to complete a render. The submitter tries to find all of the files required for the render. The files that it identifies appear in the lists in italics.

You can add additional input files and directories that contain other assets required for the render that were not automatically detected.

If your job writes files to multiple output directories, you must specify the directories here so that they are part of the job download.

## Host requirements tab
<a name="submiter-host"></a>

![The shared host requirements tab of the Blender submitter.](http://docs.aws.amazon.com/deadline-cloud/latest/userguide/images/submitter-host.png)


The host requirements tab sets the fleet capabilities required to process the job. Capabilities are specified for the entire fleet, not individual workers in the fleet.

If your queue has associated resource limits, use the **Add amount** button to specify the limit. For more information, see [ Create resource limits for jobs ](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/build-job-limits.html) 