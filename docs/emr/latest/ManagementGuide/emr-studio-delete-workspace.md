# Delete a Workspace and notebook files in EMR Studio

When you delete a notebook file from an EMR Studio Workspace, you delete
the file from the **File browser**, and EMR Studio removes its backup
copy in Amazon S3. You do not have to take any further steps to avoid storage charges when you
delete a file from a Workspace.

When you delete _an entire Workspace_, its
notebook files and folders will remain in the Amazon S3 storage location. The files continue to
accrue storage charges. To avoid storage charges, remove all backed-up files and folders
that are associated with your deleted Workspace from Amazon S3.

###### To delete a notebook file from an EMR Studio Workspace

1. Select the **File browser** panel from the left sidebar in the
   Workspace.
2. Select the file or folder you want to delete. Right-click your selection and choose
   **Delete**. The file disappears from the list. EMR Studio removes
   the file or folder from Amazon S3 for you.

From the Workspace UI

###### Delete a Workspace and its associated backup files from

EMR Studio

1. Log in to your EMR Studio with your Studio access URL and
   choose **Workspaces** from the left
   navigation.
2. Find your Workspace in the list, then select the check box next
   to its name. You can select multiple Workspaces to delete at the
   same time.
3. Choose **Delete** in the upper right of the
   **Workspaces** list and confirm that you want
   to delete the selected Workspaces. Choose
   **Delete** to confirm.
4. If you want to remove the notebook files that were associated with the
   deleted Workspace from Amazon S3, follow the instructions for [Deleting
   objects](../../../AmazonS3/latest/user-guide/delete-objects.md "../../../AmazonS3/latest/user-guide/delete-objects.md") in the _Amazon Simple Storage Service_
   _Console User Guide_. If you did not create
   the Studio, consult your Studio administrator to determine
   the Amazon S3 backup location for the deleted Workspace.

From the Workspaces list

###### Delete a Workspace and its associated backup files from the

Workspaces list

1. Navigate to the **Workspace**s list in the
   console.
2. Select the Workspace that you want to delete from the list and
   then choose **Actions**.
3. Choose **Delete**.
4. If you want to remove the notebook files that were associated with the
   deleted Workspace from Amazon S3, follow the instructions for [Deleting
   objects](../../../AmazonS3/latest/user-guide/delete-objects.md "../../../AmazonS3/latest/user-guide/delete-objects.md") in the _Amazon Simple Storage Service_
   _Console User Guide_. If you did not create
   the Studio, consult your Studio administrator to determine
   the Amazon S3 backup location for the deleted Workspace.
