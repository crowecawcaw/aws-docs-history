# Working with EMR Notebooks

###### Note

EMR Notebooks are available as EMR Studio Workspaces in the console. The **Create Workspace** button in the console lets you create new notebooks. To access or create Workspaces, EMR Notebooks users need additional IAM role permissions. For more information, see [Amazon EMR Notebooks are Amazon EMR Studio Workspaces in the console](emr-managed-notebooks-migration.md "emr-managed-notebooks-migration.md") and [Amazon EMR console](whats-new-in-console.md "whats-new-in-console.md").

After you create an EMR notebook, the notebook takes a short time to start.
The **Status** in the **Notebooks** list shows
**Starting**. You can open a notebook when its status is
**Ready**. It might take a bit longer for a notebook to be
**Ready** if you created a cluster along with it.

###### Tip

Refresh your browser or choose the refresh icon above the notebooks list to
refresh notebook status.

## Understanding Notebook status

An EMR notebook can have the following for **Status** in
the **Notebooks** list.

| Status   | Meaning                                                                                                                                                                                                                                                                                                                               |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Ready    | You can open the notebook using the notebook editor. While a<br>notebook has a **Ready\*<br>• status, you can stop<br>or delete it. To change clusters, you must stop the notebook<br>first. If a notebook in the **Ready\*<br>• status is<br>idle for a long period of time, it is stopped<br>automatically.                         |
| Starting | The notebook is being created and attached to the cluster.<br>While a notebook is starting, you cannot open the notebook<br>editor, stop it, delete it, or change clusters.                                                                                                                                                           |
| Pending  | The notebook has been created, and is waiting for integration<br>with the cluster to complete. The cluster may still be<br>provisioning resources or responding to other requests. You can<br>open the notebook editor with the notebook in _local<br>mode_. Any code that relies on cluster processes<br>does not execute and fails. |
| Stopping | The notebook is shutting down, or the cluster that the<br>notebook is attached to is terminating. While a notebook is<br>stopping, you can't open the notebook editor, stop it, delete<br>it, or change clusters.                                                                                                                     |
| Stopped  | The notebook has shut down. You can start the notebook on the<br>same cluster, as long as the cluster is still running. You can<br>change clusters, and delete the cluster.                                                                                                                                                           |
| Deleting | The cluster is being removed from the list of available<br>clusters. The notebook file,<br>``NotebookName`.ipynb` remains in Amazon S3 and continues to accrue applicable<br>storage charges.                                                                                                                                         |

## Working with the Notebook

editor

An advantage of using an EMR notebook is that you can launch the notebook
in Jupyter or JupyterLab directly from the console.

With EMR Notebooks, the notebook editor you access from the Amazon EMR console is the
familiar open-source Jupyter Notebook editor or JupyterLab. Because the notebook
editor is launched within the Amazon EMR console, it's more efficient to configure access
than it is with a notebook hosted on an Amazon EMR cluster. You don't need to configure a
user's client to have web access through SSH, security group rules, and proxy
configurations. If a user has sufficient permissions, they can simply open the
notebook editor within the Amazon EMR console.

Only one user can have an EMR notebook open at a time from within Amazon EMR.
If another user tries to open an EMR notebook that is already open, an error
occurs.

###### Important

Amazon EMR creates a unique pre-signed URL for each notebook editor session, which
is valid only for a short time. We recommend that you do not share the notebook
editor URL. Doing this creates a security risk because recipients of the URL
adopt your permissions to edit the notebook and run notebook code for the
lifetime of the URL. If others need access to a notebook, provide permissions to
their a user through permissions policies and ensure that the service role for
EMR Notebooks has access to the Amazon S3 location. For more information, see [EMR notebooks security and
access control](emr-managed-notebooks-security.md "emr-managed-notebooks-security.md") and [Service role for
EMR Notebooks](emr-managed-notebooks-service-role.md "emr-managed-notebooks-service-role.md").

###### To open the notebook editor for an EMR notebook

1. Select a notebook with a **Status** of
   **Ready** or **Pending** from the
   **Notebooks** list.
2. Choose **Open in JupyterLab** or **Open in
   Jupyter**.

A new browser tab opens to the JupyterLab or Jupyter Notebook
editor. 3. From the **Kernel** menu, choose **Change
kernel** and then select the kernel for your programming
language.

You are now ready to write and run code from within the notebook
editor.

### Saving the contents of a

Notebook

When you work in the notebook editor, the contents of notebook cells and
output are saved automatically to the notebook file periodically in Amazon S3. A
notebook that has no changes since the last time a cell was edited shows
**(autosaved)** next to the notebook name in the editor. If
changes have not yet been saved, **unsaved changes**
appears.

You can save a notebook manually. From the **File** menu,
choose **Save and Checkpoint** or press CTRL+S. This creates a
file named ``NotebookName`.ipynb`in a
 **checkpoints** folder within the notebook folder in Amazon S3.
 For example,
`s3://`amzn-s3-demo-bucket`/`MyNotebookFolder`/`NotebookID`/checkpoints/`NotebookName`.ipynb`.
Only the most recent checkpoint file is saved in this location.

## Changing clusters

You can change the cluster that an EMR notebook is attached to without
changing the contents of the notebook itself. You can change clusters for only those
notebooks that have a **Stopped** status.

###### To change the cluster of an EMR notebook

1. If the notebook that you want to change is running, select it from the
   **Notebooks** list and choose
   **Stop**.
2. When the notebook status is **Stopped**, select the
   notebook from the **Notebooks** list, and then choose
   **View details**.
3. Choose **Change cluster**.
4. If you have an active cluster running Hadoop, Spark, and Livy to which you
   want to attach the notebook, leave the default, and select a cluster from
   the list. Only clusters that meet the requirements are listed.

—or—

Choose **Create a cluster** and then choose the cluster
options. For more information, see [Cluster requirements](emr-managed-notebooks-considerations.md#considerations-limitations "emr-managed-notebooks-considerations.md#considerations-limitations"). 5. Choose an option for **Security groups**, and then choose
**Change cluster and start notebook**.

## Deleting Notebooks and Notebook

files

When you delete an EMR notebook using the Amazon EMR console, you delete the
notebook from the list of available notebooks. However, notebook files remain in
Amazon S3 and continue to accrue storage charges.

###### To delete a notebook and remove associated files

1. Open the Amazon EMR console at
   [https://console.aws.amazon.com/elasticmapreduce/](https://console.aws.amazon.com/elasticmapreduce/ "https://console.aws.amazon.com/elasticmapreduce/").
2. Choose **Notebooks**, select your notebook from the list,
   and then choose **View details**.
3. Choose the folder icon next to **Notebook location** and
   copy the **URL**, which is in the pattern
   `s3://`MyNotebookLocationPath`/`NotebookID`/`.
4. Choose **Delete**.

The notebook is removed from the list, and notebook details can no longer
be viewed. 5. Follow the instructions for [How do I delete folders from an S3 bucket?](../../../AmazonS3/latest/userguide/delete-folders.md "../../../AmazonS3/latest/userguide/delete-folders.md") in the
Amazon Simple Storage Service User Guide. Navigate to the bucket and folder from step 3.

—or—

If you have the AWS CLI installed, open a command prompt and type the
command at the end of this paragraph. Replace the Amazon S3 location with the
location that you copied above. Make sure that the AWS CLI is configured with
the access keys of a user with permissions to delete the Amazon S3 location. For
more information, see [Configuring the
AWS CLI](../../../AmazonS3/latest/userguide/cli-chap-getting-started.md "../../../AmazonS3/latest/userguide/cli-chap-getting-started.md") in the _AWS Command Line Interface User Guide_.

```
aws s3 rm s3://`MyNotebookLocationPath`/`NotebookID`
```

## Sharing Notebook files

Each EMR notebook is saved to Amazon S3 as a file named
``NotebookName`.ipynb`. As long as a
notebook file is compatible with the same version of Jupyter Notebook that
EMR Notebooks is based on, you can open the notebook as an
EMR notebook.

The easiest way to open a notebook file from another user is to save the \*.ipynb
file from another user to your local file system, and then use the upload feature in
the Jupyter and JupyterLab editors.

You can use this process to use EMR notebooks shared by others, notebooks
shared in the Jupyter community, or to restore a notebook that was deleted from the
console when you still have the notebook file.

###### To use a different notebook file as the basis for an

EMR notebook

1. Before proceeding, close the notebook editor for any notebooks that you
   will work with, and then stop the notebook if it's an
   EMR notebook.
2. Create an EMR notebook and enter a name for it. The name that you
   enter for the notebook will be the name of the file you need to replace. The
   new file name must match this file name exactly.
3. Make a note of the location in Amazon S3 that you choose for the notebook. The
   file that you replace is in a folder with a path and file name like the
   following pattern:
   `s3://`MyNotebookLocation`/`NotebookID`/`MyNotebookName`.ipynb`.
4. Stop the notebook.
5. Replace the old notebook file in the Amazon S3 location with the new one, using
   exactly the same name.

The following AWS CLI command for Amazon S3 replaces a file saved to a local
machine called `SharedNotebook.ipynb` for an EMR notebook
with the name **MyNotebook**, an ID of
`e-12A3BCDEFJHIJKLMNO45PQRST`, and created with
`amzn-s3-demo-bucket/MyNotebooksFolder` specified in Amazon S3. For
information about using the Amazon S3 console to copy and replace files, see
[Uploading,
downloading, and managing objects](../../../AmazonS3/latest/userguide/upload-download-objects.md "../../../AmazonS3/latest/userguide/upload-download-objects.md") in the
_Amazon Simple Storage Service User Guide_.

```
aws s3 cp SharedNotebook.ipynb s3://amzn-s3-demo-bucket/MyNotebooksFolder/-12A3BCDEFJHIJKLMNO45PQRST/MyNotebook.ipynb
```
