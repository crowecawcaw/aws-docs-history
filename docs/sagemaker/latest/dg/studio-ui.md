# Amazon SageMaker Studio Classic UI Overview

###### Important

As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named
Amazon SageMaker Studio Classic. The following section is specific to using the Studio Classic application. For
information about using the updated Studio experience, see [Amazon SageMaker Studio](studio-updated.md "studio-updated.md").

Studio Classic is still maintained for existing
workloads but is no longer available for onboarding. You can only stop or delete existing Studio Classic
applications and cannot create new ones. We recommend that you [migrate your workload to the new Studio experience](studio-updated-migrate.md "studio-updated-migrate.md").

Amazon SageMaker Studio Classic extends the capabilities of JupyterLab with custom resources that can speed
up your Machine Learning (ML) process by harnessing the power of AWS compute. Previous users
of JupyterLab will notice the similarity of the user interface. The most prominent additions are
detailed in the following sections. For an overview of the original JupyterLab interface, see
[The JupyterLab
Interface](https://jupyterlab.readthedocs.io/en/latest/user/interface.html "https://jupyterlab.readthedocs.io/en/latest/user/interface.html").

The following image shows the default view upon launching Amazon SageMaker Studio Classic. The _left navigation_ panel displays all top-level categories of features,
and a _[Amazon SageMaker Studio Classic home page](#studio-ui-home "#studio-ui-home")_ is open in the _main working area_. Come back to
this central point of orientation by choosing the **Home** icon (
![Black square icon representing a placeholder or empty image.](images/studio/icons/house.png)
) at any time, then selecting the **Home** node in the
navigation menu.

Try the **Getting started notebook** for an in-product
hands-on guide on how to set up and get familiar with Amazon SageMaker Studio Classic features.
On the **Quick actions** section of the Studio Classic Home page, choose **Open the Getting started notebook**.

![SageMaker Studio Classic home page.](images/studio/studio-home.png)

###### Note

This chapter is based on Studio Classic's updated user interface (UI) available on version `v5.38.x` and above on JupyterLab3.

- To retrieve your version of Studio Classic UI, from the [Studio Classic Launcher](studio-launcher.md "studio-launcher.md"),
  open a System Terminal, then
  1.  Run `conda activate studio`
  2.  Run `jupyter labextension list`
  3.  Search for the version displayed after `@amzn/sagemaker-ui version` in the output.

- For information about updating Amazon SageMaker Studio Classic, see [Shut Down and Update Amazon SageMaker Studio Classic](studio-tasks-update-studio.md "studio-tasks-update-studio.md").

###### Topics

- [Amazon SageMaker Studio Classic home page](#studio-ui-home "#studio-ui-home")
- [Amazon SageMaker Studio Classic layout](#studio-ui-layout "#studio-ui-layout")

## Amazon SageMaker Studio Classic home page

The Home page provides access to common tasks and workflows. In particular, it includes a
list of **Quick actions** for common tasks such as **Open
Launcher** to create notebooks and other resources and **Import &
prepare data visually** to create a new flow in Data Wrangler.The **Home**
page also offers tooltips on key controls in the UI.

The **Prebuilt and automated solutions** help you get started quickly
with SageMaker AI's low-code solutions such as Amazon SageMaker JumpStart and Autopilot.

In **Workflows and tasks**, you can find a list of relevant tasks for
each step of your ML workflow that takes you to the right tool for the job. For example,
**Transform, analyse, and export data** takes you to Amazon SageMaker Data Wrangler and opens the
workflow to create a new data flow, or **View all experiments** takes you to
SageMaker Experiments and opens the experiments list view.

Upon Studio Classic launch, the **Home** page is open in the main working
area. You can customize your SageMaker AI **Home** page by choosing
the **Customize Layout** icon
(
![Black square icon representing a placeholder or empty image.](images/studio/icons/layout.png)
) at the top right of the
**Home** tab.

## Amazon SageMaker Studio Classic layout

The Amazon SageMaker Studio Classic interface consists of a _menu bar_ at
the top, a collapsible _left sidebar_ displaying a variety of
icons such as the **Home** icon and the **File Browser**, a
_status bar_ at the bottom of the screen, and a _central area_ divided horizontally into two panes. The left pane is
a collapsible _navigation panel_. The right pane, or main
working area, contains one or more tabs for resources such as launchers, notebooks, terminals,
metrics, and graphs, and can be further divided.

**Report a bug** in Studio Classic or choose the notification icon (
![Red circle icon with white exclamation mark, indicating an alert or warning.](images/icons/Notification.png)
) to view notifications from Studio Classic, such as new Studio Classic versions
and new SageMaker AI features, on the right corner of the menu bar. To update to a new version of
Studio Classic, see [Shut Down and Update Amazon SageMaker Studio Classic and Apps](studio-tasks-update.md "studio-tasks-update.md").

The following sections describe the Studio Classic main user interface areas.

### Left sidebar

The _left sidebar_ includes the following icons. When
hovering over an icon, a tooltip displays the icon name. A single click on an icon opens up
the left navigation panel with the described functionality.
A
double click minimizes the left navigation panel.

| Icon                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The Home icon.                          | **Home**<br>Choose the **Home*<br>• icon to open a top-level<br>navigation menu in the *left navigation\*<br>panel.<br>Using the **Home*<br>• navigation menu, you can discover and<br>navigate to the right tools for each step of your ML workflow. The menu also<br>provides shortcuts to quick-start solutions and learning resources such as<br>documentation and guided tutorials.<br>The menu categories group relevant features together. Choosing<br>**Data**, for example, expands the relevant SageMaker AI capabilities<br>for your data preparations tasks. From here, you can prepare your data with Data Wrangler,<br>create and store ML features with Amazon SageMaker Feature Store, and manage Amazon EMR clusters for<br>large-scale data processing. The categories are ordered following a typical ML<br>workflow from preparing data, to building, training, and deploying ML models<br>(data, pipelines, models, and deployments).<br>When you choose a specific node (such as Data Wrangler), a corresponding page opens in<br>the main working area.<br>Choose \*\*Home*<br>• in the navigation menu to open the [Amazon SageMaker Studio Classic home page](#studio-ui-home "#studio-ui-home")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| The File Browser icon.                  | **File Browser**<br>The **File Browser\*<br>• displays lists of your notebooks,<br>experiments, trials, trial components, endpoints, and low-code solutions.<br>Whether you are in a personal or shared space determines who has access to<br>your files. You can identify which type of space you are in by looking at the top<br>right corner. If you are in a personal app, you see a user icon followed by<br>`[user_name]` **/ Personal Studio**<br>and if you are in a collaborative space, you see a globe icon followed by<br>"`[user_name]` **/**<br>`[space_name].`"<br>• **Personal Studio Classic app:** A private Amazon EFS<br>directory that only you can access.<br>• **Collaborative space:** A shared Amazon EFS<br>directory with other members of your team for group access to notebooks and<br>resources. Working in a shared space allows for real-time team collaboration<br>on notebooks.<br>• **Studio Classic launcher:** Choose the plus<br>(**+**) sign on the menu at the top of the file browser to<br>open the [Amazon SageMaker Studio Classic Launcher](studio-launcher.md "studio-launcher.md").<br>• **Upload files:** Choose the **Upload<br>Files\*<br>• icon (<br>Black square icon representing a placeholder or empty image.<br>) to add files to Studio Classic or drag and drop them from<br>your desktop.<br>• **Open files:** Double-click a file to open<br>the file in a new tab or right-click and select<br>**Open**.<br>• **Panel management:** To work in adjacent<br>files, choose a tab that contains a notebook, Python, or text file, then<br>choose **New View for File**.<br>For hierarchical entries, a selectable breadcrumb at the top of the browser<br>shows your location in the hierarchy. |
| The Property Inspector icon.            | **Property Inspector**<br>The Property Inspector is a notebook cell tools inspector which displays<br>contextual property settings when open.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| The Running Terminals and Kernels icon. | **Running Terminals and Kernels**<br>You can check the list of all the _kernels_<br>and \*terminals<br>• currently running across all<br>notebooks, code consoles, and directories. You can shut down individual resources,<br>including notebooks, terminals, kernels, apps, and instances. You can also shut<br>down all resources in one of these categories at the same time.<br>For more information, see [Shut Down Resources from<br>Amazon SageMaker Studio Classic](notebooks-run-and-manage-shut-down.md "notebooks-run-and-manage-shut-down.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| The Git icon.                           | **Git**<br>You can connect to a Git repository and then access a full range of Git tools<br>and operations.<br>For more information, see [Clone a Git Repository in Amazon SageMaker Studio Classic](studio-tasks-git.md "studio-tasks-git.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| The Table of Contents icon.             | **Table of Contents**You can<br>navigate the structure of a document when a notebook or Python files are open.<br>A table of contents is auto-generated in the left navigation panel when you<br>have a notebook, Markdown files, or Python files opened. The entries are clickable<br>and scroll the document to the heading in question.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| The Extensions icon.                    | **Extensions**<br>You can turn on and manage third-party JupyterLab extensions. You can check<br>the already installed extensions and search for extensions by typing the name in<br>the search bar. When you have found the extension you want to install, choose<br>**Install**. After installing your new extensions, be sure to<br>restart JupyterLab by refreshing your browser. For more information,<br>see [JupyterLab Extensions documentation](https://jupyterlab.readthedocs.io/en/stable/user/extensions.html "https://jupyterlab.readthedocs.io/en/stable/user/extensions.html").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

### Left navigation panel

The left navigation panel content varies with the Icon selected in the left
sidebar.

For example, choosing the **Home** icon displays the navigation menu.
Choosing **File browser** lists all the files and directories available in
your workspace (notebooks, experiments, data flows, trials, trial components, endpoints, or
low-code solutions).

In the navigation menu, choosing a node brings up the corresponding feature page in the
main working area. For example, choosing **Data Wrangler** in the
**Data** menu opens up the **Data Wrangler** tab listing all
existing flows.

### Main working area

The main working area consists of multiple tabs that contain your open notebooks,
terminals, and detailed information about your experiments and endpoints. In the main working
area, you can arrange documents (such as notebooks and text files) and other activities
(such as terminals and code consoles) into panels of tabs that you can resize or subdivide.
Drag a tab to the center of a tab panel to move the tab to the panel. Subdivide a tab panel
by dragging a tab to the left, right, top, or bottom of the panel. The tab for the current
activity is marked with a colored top border (blue by default).

###### Note

All feature pages provide in-product contextual help. To access help, choose
**Show information**. The help interface provides a brief introduction
to the tool and links to additional resources, such as videos, tutorials, or blogs.
