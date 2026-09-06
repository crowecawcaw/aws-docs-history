

# Use the Amazon SageMaker Studio Lab notebook toolbar
<a name="studio-lab-use-menu"></a>

**Note**  
Amazon SageMaker Studio Lab is no longer open to new customers. Existing customers can continue to use the service as normal. AWS continues to invest in security and availability improvements for Studio Lab, but we do not plan to introduce new features. For more information, see [Studio Lab availability change](studio-lab-availability-change.md). 

Amazon SageMaker Studio Lab notebooks extend the JupyterLab interface. For an overview of the basic JupyterLab interface, see [The JupyterLab Interface](https://jupyterlab.readthedocs.io/en/latest/user/interface.html).

The following image shows the toolbar and an empty cell from a Studio Lab notebook.

![The layout of the notebook toolbar, including the toolbar icons.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/studio-lab-menu.png)


When you hover over a toolbar icon, a tooltip displays the icon function. You can find additional notebook commands in the Studio Lab main menu. The toolbar includes the following icons:


| Icon | Description | 
| --- | --- | 
|  ![The Save and checkpoint icon.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/icons/studio-lab-save-and-checkpoint.png)  | **Save and checkpoint**<br />Saves the notebook and updates the checkpoint file. | 
|  ![The Insert cell icon.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/icons/studio-lab-insert-cell.png)  | **Insert cell**<br />Inserts a code cell below the current cell. The current cell is noted by the blue vertical marker in the left margin. | 
|  ![The Cut, copy, and paste cells icon.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/icons/studio-lab_cut_copy_paste.png)  | **Cut, copy, and paste cells**<br />Cuts, copies, and pastes the selected cells. | 
|  ![The Run cells icon.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/icons/studio-lab-run.png)  | **Run cells**<br />Runs the selected cells. The cell that follows the last-selected cell becomes the new-selected cell. | 
|  ![The Interrupt kernel icon.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/icons/studio-lab-interrupt-kernel.png)  | **Interrupt kernel**<br />Interrupts the kernel, which cancels the currently-running operation. The kernel remains active. | 
|  ![The Restart kernel icon.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/icons/studio-lab-restart-kernel.png)  | **Restart kernel**<br />Restarts the kernel. Variables are reset. Unsaved information is not affected. | 
|  ![The Restart kernel and re-run notebook icon.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/icons/studio-lab-restart-rerun-kernel.png)  | **Restart kernel and re-run notebook**<br />Restarts the kernel. Variables are reset. Unsaved information is not affected. Then re-runs the entire notebook. | 
|  ![The Cell type icon.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/icons/studio-lab_cell.png)  | **Cell type**<br />Displays or changes the current cell type. The cell types are:+  Code – Code that the kernel runs. <br />+  Markdown – Text rendered as markdown. <br />+  Raw – Content, including Markdown markup, that's displayed as text.  | 
|  ![The Checkpoint diff icon.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/icons/studio-lab-checkpoint-diff.png)  | **Checkpoint diff**<br />Opens a new tab that displays the difference between the notebook and the checkpoint file. For more information, see [Get notebook differences](studio-lab-use-diff.md). | 
|  ![The Git diff icon.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/icons/studio-lab-git-diff.png)  | **Git diff**<br />Only enabled if the notebook is opened from a Git repository. Opens a new tab that displays the difference between the notebook and the last Git commit. For more information, see [Get notebook differences](studio-lab-use-diff.md). | 
| **default** | **Kernel**<br />Displays or changes the kernel that processes the cells in the notebook.<br />`No Kernel` indicates that the notebook was opened without specifying a kernel. You can edit the notebook, but you can't run any cells. | 
|  ![The Kernel busy status icon.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/icons/studio-lab-kernel.png)  | **Kernel busy status**<br />Displays a kernel's busy status by showing the circle's edge and its interior as the same color. The kernel is busy when it is starting and when it is processing cells. Additional kernel states are displayed in the status bar at the bottom-left corner of Studio Lab. | 