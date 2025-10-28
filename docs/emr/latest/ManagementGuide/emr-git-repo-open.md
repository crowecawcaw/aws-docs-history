# Use Git repositories in an EMR Studio Notebook

###### Note

EMR Notebooks are available as EMR Studio Workspaces in the console. The **Create Workspace** button in the console lets you create new notebooks. To access or create Workspaces, EMR Notebooks users need additional IAM role permissions. For more information, see [Amazon EMR Notebooks are Amazon EMR Studio Workspaces in the console](emr-managed-notebooks-migration.md "emr-managed-notebooks-migration.md") and [Amazon EMR console](whats-new-in-console.md "whats-new-in-console.md").

You can choose to **Open in JupyterLab** or **Open in
Jupyter** when you open a notebook.

If you choose to open the notebook in Jupyter, a list of expandable files and
folders within the notebook are displayed. You can manually run Git commands like
the following in a notebook cell.

```
!git pull origin primary
```

To open any of the additional repositories, navigate to other folders.

If you choose to open the notebook with a JupyterLab interface, you can use the
pre-installed JupyterLab Git extension. For information about the extension, see
[jupyterlab-git](https://github.com/jupyterlab/jupyterlab-git "https://github.com/jupyterlab/jupyterlab-git").
