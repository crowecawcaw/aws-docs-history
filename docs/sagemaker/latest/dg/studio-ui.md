

# Amazon SageMaker Studio Classic UI Overview
<a name="studio-ui"></a>

**Note**  
As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named Amazon SageMaker Studio Classic. The following section is specific to using the Studio Classic application. For information about using the updated Studio experience, see [Amazon SageMaker Studio](studio-updated.md).  
Studio Classic is still maintained for existing workloads but is no longer available for onboarding. You can only stop or delete existing Studio Classic applications and cannot create new ones. We recommend that you [migrate your workload to the new Studio experience](studio-updated-migrate.md).

Amazon SageMaker Studio Classic extends the capabilities of JupyterLab with custom resources that can speed up your Machine Learning (ML) process by harnessing the power of AWS compute. Previous users of JupyterLab will notice the similarity of the user interface. The most prominent additions are detailed in the following sections. For an overview of the original JupyterLab interface, see [The JupyterLab Interface](https://jupyterlab.readthedocs.io/en/latest/user/interface.html). 

The following image shows the default view upon launching Amazon SageMaker Studio Classic. The *left navigation* panel displays all top-level categories of features, and a *[Amazon SageMaker Studio Classic home page](#studio-ui-home)* is open in the *main working area*. Come back to this central point of orientation by choosing the **Home** icon (![Black square icon representing a placeholder or empty image.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/studio/icons/house.png)) at any time, then selecting the **Home** node in the navigation menu.

Try the **Getting started notebook** for an in-product hands-on guide on how to set up and get familiar with Amazon SageMaker Studio Classic features. On the **Quick actions** section of the Studio Classic Home page, choose **Open the Getting started notebook**.

![SageMaker Studio Classic home page.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/studio/studio-home.png)


**Note**  
This chapter is based on Studio Classic's updated user interface (UI) available on version `v5.38.x` and above on JupyterLab3.  
To retrieve your version of Studio Classic UI, from the [Studio Classic Launcher](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-launcher.html), open a System Terminal, then  
Run `conda activate studio`
Run `jupyter labextension list`
Search for the version displayed after `@amzn/sagemaker-ui version` in the output.
For information about updating Amazon SageMaker Studio Classic, see [Shut Down and Update Amazon SageMaker Studio Classic](studio-tasks-update-studio.md).

**Topics**
+ [Amazon SageMaker Studio Classic home page](#studio-ui-home)
+ [Amazon SageMaker Studio Classic layout](#studio-ui-layout)

## Amazon SageMaker Studio Classic home page
<a name="studio-ui-home"></a>

The Home page provides access to common tasks and workflows. In particular, it includes a list of **Quick actions** for common tasks such as **Open Launcher** to create notebooks and other resources and **Import & prepare data visually** to create a new flow in Data Wrangler.The **Home** page also offers tooltips on key controls in the UI.

The **Prebuilt and automated solutions** help you get started quickly with SageMaker AI's low-code solutions such as Amazon SageMaker JumpStart and Autopilot.

In **Workflows and tasks**, you can find a list of relevant tasks for each step of your ML workflow that takes you to the right tool for the job. For example, **Transform, analyse, and export data** takes you to Amazon SageMaker Data Wrangler and opens the workflow to create a new data flow, or **View all experiments** takes you to SageMaker Experiments and opens the experiments list view.

Upon Studio Classic launch, the **Home** page is open in the main working area. You can customize your SageMaker AI **Home** page by choosing the **Customize Layout** icon (![Black square icon representing a placeholder or empty image.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/studio/icons/layout.png)) at the top right of the **Home** tab.

## Amazon SageMaker Studio Classic layout
<a name="studio-ui-layout"></a>

The Amazon SageMaker Studio Classic interface consists of a *menu bar* at the top, a collapsible *left sidebar* displaying a variety of icons such as the **Home** icon and the **File Browser**, a *status bar* at the bottom of the screen, and a *central area* divided horizontally into two panes. The left pane is a collapsible *navigation panel*. The right pane, or main working area, contains one or more tabs for resources such as launchers, notebooks, terminals, metrics, and graphs, and can be further divided.

**Report a bug** in Studio Classic or choose the notification icon (![Red circle icon with white exclamation mark, indicating an alert or warning.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/icons/Notification.png)) to view notifications from Studio Classic, such as new Studio Classic versions and new SageMaker AI features, on the right corner of the menu bar. To update to a new version of Studio Classic, see [Shut Down and Update Amazon SageMaker Studio Classic and Apps](studio-tasks-update.md).

The following sections describe the Studio Classic main user interface areas.

### Left sidebar
<a name="studio-ui-nav-bar"></a>

The *left sidebar* includes the following icons. When hovering over an icon, a tooltip displays the icon name. A single click on an icon opens up the left navigation panel with the described functionality. A double click minimizes the left navigation panel.


| Icon | Description | 
| --- | --- | 
|  ![The Home icon.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/studio/icons/house@2x.png)  | **Home**<br />Choose the **Home** icon to open a top-level navigation menu in the *left navigation* panel.<br />Using the **Home** navigation menu, you can discover and navigate to the right tools for each step of your ML workflow. The menu also provides shortcuts to quick-start solutions and learning resources such as documentation and guided tutorials.<br />The menu categories group relevant features together. Choosing **Data**, for example, expands the relevant SageMaker AI capabilities for your data preparations tasks. From here, you can prepare your data with Data Wrangler, create and store ML features with Amazon SageMaker Feature Store, and manage Amazon EMR clusters for large-scale data processing. The categories are ordered following a typical ML workflow from preparing data, to building, training, and deploying ML models (data, pipelines, models, and deployments).<br />When you choose a specific node (such as Data Wrangler), a corresponding page opens in the main working area.<br />Choose **Home** in the navigation menu to open the [Amazon SageMaker Studio Classic home page](#studio-ui-home) | 
|  ![The File Browser icon.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/studio/icons/folder@2x.png)  | **File Browser**<br />The **File Browser** displays lists of your notebooks, experiments, trials, trial components, endpoints, and low-code solutions.<br />Whether you are in a personal or shared space determines who has access to your files. You can identify which type of space you are in by looking at the top right corner. If you are in a personal app, you see a user icon followed by {{[user\_name]}}** / Personal Studio** and if you are in a collaborative space, you see a globe icon followed by "{{[user\_name] }}**/** {{[space\_name].}}"+  **Personal Studio Classic app:** A private Amazon EFS directory that only you can access. +  **Collaborative space:** A shared Amazon EFS directory with other members of your team for group access to notebooks and resources. Working in a shared space allows for real-time team collaboration on notebooks. +  **Studio Classic launcher:** Choose the plus (**\+**) sign on the menu at the top of the file browser to open the [Amazon SageMaker Studio Classic Launcher](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-launcher.html).  +  **Upload files:** Choose the **Upload Files** icon (![Black square icon representing a placeholder or empty image.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/icons/File_upload_squid.png)) to add files to Studio Classic or drag and drop them from your desktop. +  **Open files:** Double-click a file to open the file in a new tab or right-click and select **Open**. +  **Panel management:** To work in adjacent files, choose a tab that contains a notebook, Python, or text file, then choose **New View for File**. <br />For hierarchical entries, a selectable breadcrumb at the top of the browser shows your location in the hierarchy. | 
|  ![The Property Inspector icon.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/studio/icons/gears@2x.png)  | **Property Inspector**<br />The Property Inspector is a notebook cell tools inspector which displays contextual property settings when open. | 
|  ![The Running Terminals and Kernels icon.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/studio/icons/running-terminals-kernels@2x.png)  | **Running Terminals and Kernels**<br />You can check the list of all the *kernels* and *terminals* currently running across all notebooks, code consoles, and directories. You can shut down individual resources, including notebooks, terminals, kernels, apps, and instances. You can also shut down all resources in one of these categories at the same time.<br />For more information, see [Shut Down Resources from Amazon SageMaker Studio Classic](notebooks-run-and-manage-shut-down.md). | 
|  ![The Git icon.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/studio/icons/git@2x.png)  | **Git**<br />You can connect to a Git repository and then access a full range of Git tools and operations.<br />For more information, see [Clone a Git Repository in Amazon SageMaker Studio Classic](studio-tasks-git.md). | 
|  ![The Table of Contents icon.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/studio/icons/table-of-contents@2x.png)  | **Table of Contents**<br />You can navigate the structure of a document when a notebook or Python files are open. A table of contents is auto-generated in the left navigation panel when you have a notebook, Markdown files, or Python files opened. The entries are clickable and scroll the document to the heading in question. | 
|  ![The Extensions icon.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/studio/icons/extensions@2x.png)  | **Extensions**<br />You can turn on and manage third-party JupyterLab extensions. You can check the already installed extensions and search for extensions by typing the name in the search bar. When you have found the extension you want to install, choose **Install**. After installing your new extensions, be sure to restart JupyterLab by refreshing your browser. <br />For more information, see [JupyterLab Extensions documentation](https://jupyterlab.readthedocs.io/en/stable/user/extensions.html). | 

### Left navigation panel
<a name="studio-ui-browser"></a>

The left navigation panel content varies with the Icon selected in the left sidebar.

For example, choosing the **Home** icon displays the navigation menu. Choosing **File browser** lists all the files and directories available in your workspace (notebooks, experiments, data flows, trials, trial components, endpoints, or low-code solutions).

In the navigation menu, choosing a node brings up the corresponding feature page in the main working area. For example, choosing **Data Wrangler** in the **Data** menu opens up the **Data Wrangler** tab listing all existing flows.

### Main working area
<a name="studio-ui-work"></a>

The main working area consists of multiple tabs that contain your open notebooks, terminals, and detailed information about your experiments and endpoints. In the main working area, you can arrange documents (such as notebooks and text files) and other activities (such as terminals and code consoles) into panels of tabs that you can resize or subdivide. Drag a tab to the center of a tab panel to move the tab to the panel. Subdivide a tab panel by dragging a tab to the left, right, top, or bottom of the panel. The tab for the current activity is marked with a colored top border (blue by default).

**Note**  
All feature pages provide in-product contextual help. To access help, choose **Show information**. The help interface provides a brief introduction to the tool and links to additional resources, such as videos, tutorials, or blogs.