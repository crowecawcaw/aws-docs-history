

# Amazon SageMaker Studio Lab UI overview
<a name="studio-lab-use-ui"></a>

**Note**  
Amazon SageMaker Studio Lab is no longer open to new customers. Existing customers can continue to use the service as normal. AWS continues to invest in security and availability improvements for Studio Lab, but we do not plan to introduce new features. For more information, see [Studio Lab availability change](studio-lab-availability-change.md). 

Amazon SageMaker Studio Lab extends the JupyterLab interface. Previous users of JupyterLab will notice similarities between the JupyterLab and Studio Lab UI, including the workspace. For an overview of the basic JupyterLab interface, see [The JupyterLab Interface](https://jupyterlab.readthedocs.io/en/latest/user/interface.html).

The following image shows Studio Lab with the file browser open and the Studio Lab Launcher displayed.

![The layout of the project user interface.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/studio-lab-ui.png)


You will find the *menu bar* at the top of the screen. The *left sidebar* contains icons to open file browsers, resource browsers, and tools. The *status bar* is located at the bottom-left corner of Studio Lab.

The main work area is divided horizontally into two panes. The left pane is the *file and resource browser*. The right pane contains one or more tabs for resources, such as notebooks and terminals.

**Topics**
+ [Left sidebar](#studio-lab-use-ui-nav-bar)
+ [File and resource browser](#studio-lab-use-ui-browser)
+ [Main work area](#studio-lab-use-ui-work)

## Left sidebar
<a name="studio-lab-use-ui-nav-bar"></a>

The left sidebar includes the following icons. When you hover over an icon, a tooltip displays the icon name. When you choose an icon, the file and resource browser displays the described functionality. For hierarchical entries, a selectable breadcrumb at the top of the browser shows your location in the hierarchy.


| Icon | Description | 
| --- | --- | 
|  ![The File Browser icon.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/icons/File_browser_squid@2x.png)  | **File Browser**<br />Choose the **Upload Files** icon (![Black square icon representing a placeholder or empty image.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/icons/File_upload_squid.png)) to add files to Studio Lab.<br />Double-click a file to open the file in a new tab.<br />To have adjacent files open, choose a tab that contains a notebook, Python, or text file, and then choose **New View for File**.<br />Choose the plus (**\+**) sign on the menu at the top of the file browser to open the Studio Lab Launcher. | 
|  ![The Running Terminals and Kernels icon.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/icons/Running_squid@2x.png)  | **Running Terminals and Kernels**<br />You can see a list of all of the running terminals and kernels in your project. For more information, see [Shut down Studio Lab resources](studio-lab-use-shutdown.md). | 
|  ![The Git icon.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/icons/Git_squid@2x.png)  | **Git**<br />You can connect to a Git repository and then access a full range of Git tools and operations. For more information, see [Use external resources in Amazon SageMaker Studio Lab](studio-lab-use-external.md). | 
|  ![The Table of Contents icon.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/icons/studio-lab-toc.png)  | **Table of Contents**<br />You can access the Table of Contents for your current Jupyter notebook. | 
|  ![The Extension Manager icon.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/icons/studio-lab-extension.png)  | **Extension Manager**<br />You can enable and manage third-party JupyterLab extensions. | 

## File and resource browser
<a name="studio-lab-use-ui-browser"></a>

The file and resource browser shows lists of your notebooks and files. On the menu at the top of the file browser, choose the plus (**\+**) sign to open the Studio Lab Launcher. The Launcher allows you to create a notebook or open a terminal.

## Main work area
<a name="studio-lab-use-ui-work"></a>

The main work area has multiple tabs that contain your open notebooks and terminals.