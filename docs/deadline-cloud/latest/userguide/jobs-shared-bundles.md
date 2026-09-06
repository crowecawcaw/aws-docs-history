

# Load and submit shared job bundles
<a name="jobs-shared-bundles"></a>

With AWS Deadline Cloud, you can share ready-to-use job bundles on a queue. If you can submit jobs to the queue, you can browse and preview the bundles shared on it. You can also submit them as jobs. You use the job bundle browser for each of these tasks. The job bundle browser is a graphical tool that you open from the Deadline Cloud command line. You don't need to know where the bundle files are stored or copy them manually.

The job bundle browser shows bundles from three sources:
+ **Queue** – Bundles your team shared on the selected queue.
+ **Local** – Bundles in folders on your workstation.
+ **History** – Bundles from jobs you submitted before, so you can submit a previous job again with different settings.

For information about how to share a job bundle on your queue, see [Share job bundles on your queue](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/share-job-bundles.html) in the *Deadline Cloud Developer Guide*.

## Prerequisites
<a name="jobs-shared-bundles-prerequisites"></a>

Before you begin, make sure that you have the Deadline Cloud command line interface (CLI) installed and configured, including its graphical components. You open the job bundle browser from the CLI. For installation and configuration steps, see [Getting started](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/getting-started.html) in the *Deadline Cloud Developer Guide*.

## Submit a shared job bundle
<a name="jobs-shared-bundles-submit"></a>

1. From a terminal, run the following command to open the job bundle browser:

   ```
   deadline bundle gui-submit --browse
   ```

   The job bundle browser opens, as shown in the following image:  
![The Browse Job Bundles window with Source set to Queue, a bundle list, and a preview pane showing parameters and steps.](http://docs.aws.amazon.com/deadline-cloud/latest/userguide/images/bundles/job-bundle-browser.png)

1. For **Source**, choose **Queue**.

1. Select a bundle from the list. The preview shows the bundle's description, its parameters, and the steps it runs, so you can confirm it's the right one. To narrow a long list, enter part of a name in the filter box.

1. Choose **Select**. The bundle downloads and opens in the job submission dialog.  
![The Deadline Cloud job submission dialog's Shared job settings tab, showing job name, priority, state, farm, and queue.](http://docs.aws.amazon.com/deadline-cloud/latest/userguide/images/bundles/job-submission-dialog.png)

1. Set the parameter values for your job, then choose **Submit**. To go back and pick a different bundle instead, choose **Load Bundle**.

To look inside a bundle without submitting it, choose **Download bundle** in the preview. The bundle downloads and opens in your file explorer so that you can inspect its files.

## Hide shared bundles you don't use
<a name="jobs-shared-bundles-hide"></a>

As a queue accumulates shared bundles, you can hide the ones you don't use. Open the context menu for a bundle, then choose **Hide bundle**. Hiding a bundle only changes your own view on your workstation. The bundle stays on the queue and your teammates still see it.

![The job bundle browser with a bundle selected and its context menu showing the Hide bundle option.](http://docs.aws.amazon.com/deadline-cloud/latest/userguide/images/bundles/hide-bundle.png)


To bring a bundle back, select the **Show hidden** checkbox. Then open the context menu for the bundle and choose **Unhide bundle**.

![The job bundle browser with the Show hidden checkbox selected, revealing hidden bundles in the list.](http://docs.aws.amazon.com/deadline-cloud/latest/userguide/images/bundles/unhide-bundle.png)
