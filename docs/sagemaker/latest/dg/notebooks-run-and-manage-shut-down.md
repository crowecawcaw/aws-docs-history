# Shut Down Resources from

Amazon SageMaker Studio Classic

###### Important

As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named
Amazon SageMaker Studio Classic. The following section is specific to using the Studio Classic application. For
information about using the updated Studio experience, see [Amazon SageMaker Studio](studio-updated.md "studio-updated.md").

Studio Classic is still maintained for existing
workloads but is no longer available for onboarding. You can only stop or delete existing Studio Classic
applications and cannot create new ones. We recommend that you [migrate your workload to the new Studio experience](studio-updated-migrate.md "studio-updated-migrate.md").

You can shut down individual Amazon SageMaker AI resources, including notebooks, terminals,
kernels, apps, and instances from Studio Classic. You can also shut down all of the resources in
one of these categories at the same time. Amazon SageMaker Studio Classic does not support shutting down
resources from within a notebook.

###### Note

When you shut down a Studio Classic notebook instance, additional resources that you
created in Studio Classic are not deleted. For example, additional resources can include SageMaker AI
endpoints, Amazon EMR clusters, and Amazon S3 buckets. To stop the accrual of charges, you must
manually delete these resources. For information about finding resources that are accruing
charges, see [Analyzing your costs with
AWS Cost Explorer](../../../cost-management/latest/userguide/ce-what-is.md "../../../cost-management/latest/userguide/ce-what-is.md").

The following topics demonstrate how to delete these SageMaker AI resources.

###### Topics

- [Shut down an open
  notebook](#notebooks-run-and-manage-shut-down-notebook "#notebooks-run-and-manage-shut-down-notebook")
- [Shut down resources](#notebooks-run-and-manage-shut-down-sessions "#notebooks-run-and-manage-shut-down-sessions")

## Shut down an open

notebook

When you shut down a Studio Classic notebook, the notebook is not deleted. The kernel that
the notebook is running on is shut down and any unsaved information in the notebook is
lost. You can shut down an open notebook from the Studio Classic **File**
menu or from the Running Terminal and Kernels pane. The following procedure shows how to
shut down an open notebook from the Studio Classic **File** menu.

###### To shut down an open notebook from the File menu

1. Launch Studio Classic by following the steps in [Launch Amazon SageMaker Studio Classic](studio-launch.md "studio-launch.md").
2. (Optional) Save the notebook contents by choosing **File**, then
   **Save Notebook**.
3. Choose **File**.
4. Choose **Close and Shutdown Notebook**. This opens a pop-up
   window.
5. From the pop-up window, choose **OK**.

## Shut down resources

You can reach the **Running Terminals and Kernels** pane of
Amazon SageMaker Studio Classic by selecting the **Running
Terminals and Kernels** icon (
![Black square icon representing a placeholder or empty image.](images/studio/icons/running-terminals-kernels.png)
). The **Running Terminals and Kernels** pane
consists of four sections. Each section lists all the resources of that type. You can shut
down each resource individually or shut down all the resources in a section at the same
time.

When you choose to shut down all resources in a section, the following occurs:

- **RUNNING INSTANCES/RUNNING APPS** – All instances, apps,
  notebooks, kernel sessions, consoles/shells, and image terminals are shut down. System
  terminals aren't shut down.
- **KERNEL SESSIONS** – All kernels, notebooks and
  consoles/shells are shut down.
- **TERMINAL SESSIONS** – All image terminals and system
  terminals are shut down.

###### To shut down resources

1. Launch Studio Classic by following the steps in [Launch Amazon SageMaker Studio Classic](studio-launch.md "studio-launch.md").
2. Choose the **Running Terminals and Kernels** icon.
3. Do either of the following:
   - To shut down a specific resource, choose the **Shut Down**
     icon on the same row as the resource.

   For running instances, a confirmation dialog box lists all of the resources
   that SageMaker AI will shut down. A confirmation dialog box displays all running apps. To
   proceed, choose **Shut down all**.

   ###### Note

   A confirmation dialog box isn't displayed for kernel sessions or terminal
   sessions.
   - To shut down all resources in a section, choose the **X** to
     the right of the section label. A confirmation dialog box is displayed. Choose
     **Shut down all** to proceed.

   ###### Note

   When you shut down these Studio Classic resources, any additional resources
   created from Studio Classic, such as SageMaker AI endpoints, Amazon EMR clusters, and Amazon S3
   buckets are not deleted. You must manually delete these resources to stop the
   accrual of charges. For information about finding resources that are accruing
   charges, see [Analyzing your costs
   with AWS Cost Explorer](../../../cost-management/latest/userguide/ce-what-is.md "../../../cost-management/latest/userguide/ce-what-is.md").
