# Create a notebook job in Studio

###### Note

The notebook scheduler is built from the Amazon EventBridge, SageMaker Training, and Pipelines services.
If your notebook jobs fail, you might see errors related to these services. The following
provides information on how to create a notebook job in the Studio UI.

SageMaker Notebook Jobs gives you the tools to create and manage your noninteractive notebook
jobs using the Notebook Jobs widget. You can create jobs, view the jobs you created, and
pause, stop, or resume existing jobs. You can also modify notebook schedules.

When you create your scheduled notebook job with the widget, the scheduler tries to
infer a selection of default options and automatically populates the form to help you get
started quickly. If you are using Studio, at minimum you can submit an on-demand job
without setting any options. You can also submit a (scheduled) notebook job definition
supplying just the time-specific schedule information. However, you can customize other
fields if your scheduled job requires specialized settings. If you are running a local Jupyter
notebook, the scheduler extension provides a feature for you to specify your own defaults
(for a subset of options) so you don't have to manually insert the same values every
time.

When you create a notebook job, you can include additional files such as datasets,
images, and local scripts. To do so, choose **Run job with input folder**. The Notebook Job will now have access to all files under the input file's folder. While the notebook job is running the file structure of directory remains unchanged.

To schedule a notebook job, complete the following steps.

1. Open the **Create Job** form.

In local JupyterLab environments, choose the **Create a notebook
job** icon (
![Blue icon of a calendar with a checkmark, representing a scheduled task or event.](images/icons/notebook-schedule.png)
) in the taskbar. If you don't see the icon, follow the instructions
in [Installation guide](scheduled-notebook-installation.md "scheduled-notebook-installation.md") to install it.

In Studio, open the form in one of two ways:

    * Using the **File Browser**



    	1. In the **File Browser** in the left panel, right-click on
    	 the notebook you want to run as a scheduled job.
    	2. Choose **Create Notebook Job**.
    * Within the Studio notebook



    	+ Inside the Studio notebook you want to run as a scheduled job, choose
    	 the **Create a notebook job** icon (
    	![Blue icon of a calendar with a checkmark, representing a scheduled task or event.](images/icons/notebook-schedule.png)
    	) in the Studio toolbar.

2. Complete the popup form. The form displays the following fields:
   - **Job name**: A descriptive name you specify for your
     job.
   - **Input file**: The name of the notebook which you are
     scheduling to run in noninteractive mode.
   - **Compute type**: The type of Amazon EC2 instance in which you want
     to run your notebook.
   - **Parameters**: Custom parameters you can optionally specify as
     inputs to your notebook. To use this feature, you might optionally want to tag a
     specific cell in your Jupyter notebook with the `parameters` tag
     to control where your parameters are applied. For more details, see [Parameterize your notebook](notebook-auto-run-troubleshoot-override.md "notebook-auto-run-troubleshoot-override.md").
   - (Optional)**Run job with input folder**: If selected the scheduled job will have access to all the files found in the same folder as the **Input file**.
   - **Additional Options**: You can specify additional
     customizations for your job. For example, you can specify an image or kernel, input
     and output folders, job retry and timeout options, encryption details, and custom
     initialization scripts. For the complete listing of customizations you can apply,
     see [Available options](create-notebook-auto-execution-advanced.md "create-notebook-auto-execution-advanced.md").

3. Schedule your job. You can run your notebook on demand or on a fixed
   schedule.
   - To run the notebook on demand, complete the following steps:
     - Select **Run Now**.
     - Choose **Create**.
     - The **Notebook Jobs** tab appears. Choose
       **Reload** to load your job into the dashboard.

   - To run the notebook on a fixed schedule, complete the following steps:
     - Choose **Run on a schedule**.
     - Choose the **Interval** dropdown list and select an
       interval. The intervals range from every minute to monthly. You can also select
       **Custom schedule**.
     - Based on the interval you choose, additional fields appear to help you
       further specify your desired run day and time. For example, if you select
       **Day** for a daily run, an additional field appears for you
       to specify the desired time. Note that any time you specify is in UTC format.
       Note also that if you choose a small interval, such as one minute, your jobs
       overlap if the previous job is not complete when the next job starts.

     If you select a custom schedule, you use cron syntax in the expression box
     to specify your exact run date and time. The cron syntax is a space-separated
     list of digits, each of which represent a unit of time from seconds to years.
     For help with cron syntax, you can choose **Get help with cron
     syntax** under the expression box.
     - Choose **Create**.
     - The **Notebook Job Definitions** tab appears. Choose
       **Reload** to load your job definition into the
       dashboard.
