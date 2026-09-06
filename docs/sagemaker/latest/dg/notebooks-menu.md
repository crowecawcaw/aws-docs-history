

# Use the Studio Classic Notebook Toolbar
<a name="notebooks-menu"></a>

**Note**  
As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named Amazon SageMaker Studio Classic. The following section is specific to using the Studio Classic application. For information about using the updated Studio experience, see [Amazon SageMaker Studio](studio-updated.md).  
Studio Classic is still maintained for existing workloads but is no longer available for onboarding. You can only stop or delete existing Studio Classic applications and cannot create new ones. We recommend that you [migrate your workload to the new Studio experience](studio-updated-migrate.md).

Amazon SageMaker Studio Classic notebooks extend the JupyterLab interface. For an overview of the original JupyterLab interface, see [The JupyterLab Interface](https://jupyterlab.readthedocs.io/en/latest/user/interface.html).

The following image shows the toolbar and an empty cell from a Studio Classic notebook.

![SageMaker Studio Classic notebook menu.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/studio/studio-notebook-menu.png)


When you pause on a toolbar icon, a tooltip displays the icon function. Additional notebook commands are found in the Studio Classic main menu. The toolbar includes the following icons:


| Icon | Description | 
| --- | --- | 
|  ![The Save and checkpoint icon.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/studio/icons/notebook-save-and-checkpoint.png)  | **Save and checkpoint**<br />Saves the notebook and updates the checkpoint file. For more information, see [Get the Difference Between the Last Checkpoint](notebooks-diff.md#notebooks-diff-checkpoint). | 
|  ![The Insert cell icon.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/studio/icons/notebook-insert-cell.png)  | **Insert cell**<br />Inserts a code cell below the current cell. The current cell is noted by the blue vertical marker in the left margin. | 
|  ![The Cut, copy, and paste cells icons.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/studio/icons/notebook-cut-copy-paste.png)  | **Cut, copy, and paste cells**<br />Cuts, copies, and pastes the selected cells. | 
|  ![The Run cells icon.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/studio/icons/notebook-run.png)  | **Run cells**<br />Runs the selected cells and then makes the cell that follows the last selected cell the new selected cell. | 
|  ![The Interrupt kernel icon.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/studio/icons/notebook-interrupt-kernel.png)  | **Interrupt kernel**<br />Interrupts the kernel, which cancels the currently running operation. The kernel remains active. | 
|  ![The Restart kernel icon.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/studio/icons/notebook-restart-kernel.png)  | **Restart kernel**<br />Restarts the kernel. Variables are reset. Unsaved information is not affected. | 
|  ![The Restart kernel and run all cells icon.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/studio/icons/notebook-restart-kernel-run-all-cells.png)  | **Restart kernel and run all cells**<br />Restarts the kernel, then run all the cells of the notebook. | 
|  ![The Cell type icon.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/studio/icons/notebook-cell-type.png)  | **Cell type**<br />Displays or changes the current cell type. The cell types are:+  Code – Code that the kernel runs. <br />+  Markdown – Text rendered as markdown. <br />+  Raw – Content, including Markdown markup, that's displayed as text.  | 
|  ![The Launch terminal icon.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/studio/icons/notebook-launch-terminal.png)  | **Launch terminal**<br />Launches a terminal in the SageMaker image hosting the notebook. For an example, see [Get App Metadata](notebooks-run-and-manage-metadata.md#notebooks-run-and-manage-metadata-app). | 
|  ![The Checkpoint diff icon.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/studio/icons/notebook-checkpoint-diff.png)  | **Checkpoint diff**<br />Opens a new tab that displays the difference between the notebook and the checkpoint file. For more information, see [Get the Difference Between the Last Checkpoint](notebooks-diff.md#notebooks-diff-checkpoint). | 
|  ![The Git diff icon.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/studio/icons/notebook-git-diff.png)  | **Git diff**<br />Only enabled if the notebook is opened from a Git repository. Opens a new tab that displays the difference between the notebook and the last Git commit. For more information, see [Get the Difference Between the Last Commit](notebooks-diff.md#notebooks-diff-git). | 
| **2 vCPU \+ 4 GiB** | **Instance type**<br />Displays or changes the instance type the notebook runs in. The format is as follows:<br />`number of vCPUs + amount of memory + number of GPUs`<br />`Unknown` indicates the notebook was opened without specifying a kernel. The notebook runs on the SageMaker Studio instance and doesn't accrue runtime charges. You can't assign the notebook to an instance type. You must specify a kernel and then Studio assigns the notebook to a default type.<br />For more information, see [Create or Open an Amazon SageMaker Studio Classic Notebook](notebooks-create-open.md) and [Change the Instance Type for an Amazon SageMaker Studio Classic Notebook](notebooks-run-and-manage-switch-instance-type.md). | 
|  ![The Cluster icon.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/studio/icons/notebook-cluster.png)  | **Cluster**<br />Connect your notebook to an Amazon EMR cluster and scale your ETL jobs or run large-scale model training using Apache Spark, Hive, or Presto.<br />For more information, see [Data preparation using Amazon EMR](studio-notebooks-emr-cluster.md). | 
| **Python 3 (Data Science)** | **Kernel and SageMaker Image**<br />Displays or changes the kernel that processes the cells in the notebook. The format is as follows:<br />`Kernel (SageMaker Image)`<br />`No Kernel` indicates the notebook was opened without specifying a kernel. You can edit the notebook but you can't run any cells.<br />For more information, see [Change the Image or a Kernel for an Amazon SageMaker Studio Classic Notebook](notebooks-run-and-manage-change-image.md). | 
|  ![The Kernel busy status icon.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/studio/icons/notebook-kernel-status.png)  | **Kernel busy status**<br />Displays the busy status of the kernel. When the edge of the circle and its interior are the same color, the kernel is busy. The kernel is busy when it is starting and when it is processing cells. Additional kernel states are displayed in the status bar at the bottom-left corner of SageMaker Studio. | 
|  ![The Share notebook icon.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/studio/icons/notebook-share.png)  | **Share notebook**<br />Shares the notebook. For more information, see [Share and Use an Amazon SageMaker Studio Classic Notebook](notebooks-sharing.md). | 

To select multiple cells, click in the left margin outside of a cell. Hold down the `Shift` key and use `K` or the `Up` key to select previous cells, or use `J` or the `Down` key to select following cells.