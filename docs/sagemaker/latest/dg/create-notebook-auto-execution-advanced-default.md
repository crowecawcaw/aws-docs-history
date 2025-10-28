# Set up default options

for local notebooks

###### Important

As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named
Amazon SageMaker Studio Classic. The following section is specific to using the Studio Classic application. For
information about using the updated Studio experience, see [Amazon SageMaker Studio](studio-updated.md "studio-updated.md").

Studio Classic is still maintained for existing
workloads but is no longer available for onboarding. You can only stop or delete existing Studio Classic
applications and cannot create new ones. We recommend that you [migrate your workload to the new Studio experience](studio-updated-migrate.md "studio-updated-migrate.md").

You can set up default options when you create a notebook job. This can save you
time if you plan to create multiple notebook jobs with different options than the
provided defaults. The following provides information on how to set up the default
options for local notebooks.

If you have to manually type (or paste in) custom values in the **Create
Job** form, you can store new default values and the scheduler extension
inserts your new values every time you create a new job definition. This feature is
available for the following options:

- **Role ARN**
- **S3 Input Folder**
- **S3 Output Folder**
- **Output encryption KMS key** (if you turn on
  **Configure Job Encryption**)
- **Job instance volume encryption KMS key** (if you turn on
  **Configure Job Encryption**)
  This feature saves you time if you insert different values than the provided defaults
  and continue to use those values for future job runs. Your chosen user settings are stored
  on the machine that runs your JupyterLab server and are retrieved with the help of native
  API. If you provide new default values for one or more but not all five options, the
  previous defaults are taken for the ones you don’t customize.

The following instructions show you how to preview the existing default values, set
new default values, and reset your default values for your notebook jobs.

###### To preview existing default values for your notebook jobs, complete the following

steps:

1. Open the Amazon SageMaker Studio Classic console by following the instructions in [Launch Amazon SageMaker Studio Classic](studio-launch.md "studio-launch.md").
2. In the **File Browser** in the left panel, right-click on the
   notebook you want to run as a scheduled job.
3. Choose **Create Notebook Job**.
4. Choose **Additional options** to expand the tab of notebook job
   settings. You can view the default settings here.

###### To set new default values for your future notebook jobs, complete the following

steps:

1. Open the Amazon SageMaker Studio Classic console by following the instructions in [Launch Amazon SageMaker Studio Classic](studio-launch.md "studio-launch.md").
2. From the top menu in Studio Classic, choose **Settings**, then choose
   **Advanced Settings Editor**.
3. Choose **Amazon SageMaker Scheduler** from the list below
   **Settings**. This may already be open by default.
4. You can update the default settings directly in this UI page or by using the JSON
   editor.
   - In the UI you can insert new values for **Role ARN**,
     **S3 Input Folder**, **S3 Output Folder**,
     **Output encryption KMS key**, or **Job instance
     volume encryption KMS key**. If you change these values, you will see
     the new defaults for these fields while you create your next notebook job under
     **Additional options**.
   - (Optional) To update the user defaults using the **JSON Settings
     Editor**, complete the following steps:
     1. In the top right corner, choose **JSON Settings
        Editor**.
     2. In the **Settings** left sidebar, choose
        **Amazon SageMaker AI Scheduler**. This may already be open by
        default.

     You can see your current default values in the **User
     Preferences** panel.

     You can see the system default values in the **System
     Defaults** panel. 3. To update your default values, copy and paste the JSON snippet from the
     **System Defaults** panel to the **User
     Preferences** panel, and update the fields. 4. If you updated the default values, choose the **Save User
     Settings** icon (
     ![Icon of a cloud with an arrow pointing upward, representing cloud upload functionality.](images/icons/Notebook_save.png)
     ) in the top right corner. Closing the editor does not
     save the changes.

###### If you previously changed and now want to reset the user-defined default values,

complete following steps:

1. From the top menu in Studio Classic, choose **Settings**, then choose
   **Advanced Settings Editor**.
2. Choose **Amazon SageMaker Scheduler** from the list below
   **Settings**. This may already be open by default.
3. You can restore the defaults by directly using this UI page or using the JSON
   editor.
   - In the UI you can choose **Restore to Defaults** in the top
     right corner. Your defaults are restored to empty strings. You only see this
     option if you previously changed your default values.
   - (Optional) To restart the default settings using the **JSON Settings
     Editor**, complete the following steps:
     1. In the top right corner, choose **JSON Settings
        Editor**.
     2. In the **Settings** left sidebar, choose
        **Amazon SageMaker AI Scheduler**. This may already be open by
        default.

     You can see your current default values in the **User
     Preferences** panel.

     You can see the system default values in the **System
     Defaults** panel. 3. To restore your current default settings copy the content from the
     **System Defaults** panel to the **User
     Preferences** panel. 4. Choose the **Save User Settings** icon (
     ![Icon of a cloud with an arrow pointing upward, representing cloud upload functionality.](images/icons/Notebook_save.png)
     ) in the top right corner. Closing the editor does not
     save the changes.
