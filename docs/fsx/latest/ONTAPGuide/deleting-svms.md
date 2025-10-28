# Deleting storage virtual machines (SVM)

You can only delete an FSx for ONTAP SVM by using the Amazon FSx console, the AWS CLI, and
API. Before you can delete an SVM, you must delete all non-root volumes attached to the
SVM first.

###### Important

You cannot delete an SVM by using the NetApp ONTAP CLI or API.

###### Note

Before you delete a storage virtual machine, make sure that no applications
are accessing the data in the SVM, and that you have deleted all non-root volumes
attached to the SVM.

###### To delete a storage virtual machine (console)

1.  Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2.  Choose the SVM that you want to delete as follows:

        * In the left navigation pane, choose **File systems**, and then choose the
         ONTAP file system for which you want to delete an SVM.
        * Choose the **Storage virtual machines**
         tab.


        –Or–
        * To display a list of all the SVMs available, expand **ONTAP** and
         choose **Storage virtual machines**.

    Select the SVM that you want to delete from the list.

3.  In the **Volumes** tab, view the list of volumes attached to the SVM. If
    there are any non-root volumes attached to the SVM, you must delete them before
    you can delete the SVM. See [Deleting volumes](deleting-volumes.md "deleting-volumes.md") for more information.
4.  Choose **Delete storage virtual machine** from the
    **Actions** menu.
5.  In the delete confirmation dialog box, choose **Delete
    storage virtual machine**.

###### To delete a storage virtual machine

(CLI)

- To delete an FSx for ONTAP storage virtual machine, use the [delete-storage-virtual-machine](../../../cli/latest/reference/fsx/delete-storage-virtual-machine.md "../../../cli/latest/reference/fsx/delete-storage-virtual-machine.md") CLI command (or the
  equivalent [DeleteStorageVirtualMachine](../APIReference/API_DeleteStorageVirtualMachine.md "../APIReference/API_DeleteStorageVirtualMachine.md") API operation), as shown in
  the following example.

```
`aws fsx delete-storage-virtual-machine --storage-virtual-machine-id svm-abcdef0123456789d`
```
