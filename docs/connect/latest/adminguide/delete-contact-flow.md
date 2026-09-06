

# Archive, delete, and restore flows in Connect Customer
<a name="delete-contact-flow"></a>

Flows and modules must be archived before you can delete them from your Connect Customer instance. Archived flows and modules can be restored.

**Warning**  
Deleted flows and modules cannot be restored. They are permanently deleted from your Connect Customer instance.

## Important things to know
<a name="important-archive-flow"></a>
+ **Use caution when archiving flows or modules**. Connect Customer does not validate whether the flow or module you are archiving is being used in other published flows. It does not warn you that the flow is in use. 
+ Default flows cannot be archived or deleted. If you attempt to archive a default flow, you'll get message similar to the following image.  
![The Archive option in the dropdown menu.](http://docs.aws.amazon.com/connect/latest/adminguide/images/flow-archive-error.png)
+ Flows and modules that are associated with queues, quick connects, or phone numbers cannot be archived. You need to disassociate the resources from the flows before you can archive them.
+ Archived flows and modules count towards your **Flows per instance** and **Modules per instance** service quotas. You must delete them to not have them counted. For more information about quotas, see [Connect Customer service quotas](amazon-connect-service-limits.md).

## Archive a flow or module
<a name="archive-flow"></a>

There are two ways you can archive flows or modules.

**Option 1: Open the flow or module and then archive it**

1. Log in to Connect Customer with a user account that has the **Numbers and flows** - **Flows** - **Edit** permission in its security profile. If you are archiving a flow module, you need **Flow modules** - **Edit** permission.

1. On the navigation menu, choose **Routing**, **Flows**.

1. Open the flow or module you want to archive.

1. On the flow designer page, choose the dropdown menu, and then choose **Archive**, as shown in the following image.  
![The Archive option in the dropdown menu.](http://docs.aws.amazon.com/connect/latest/adminguide/images/contact-flow-archive.png)

1. Confirm you want to archive the flow or module.

1. To locate the archived flow or module, choose **View archive**.

**Option 2: Search for flow or module and then archive it**
+ On the **Flows** page, search for the flow or module you want archive, and then choose **Archive** from the **...** menu, as shown in the following image.  
![The Archive option in the dropdown menu.](http://docs.aws.amazon.com/connect/latest/adminguide/images/flow-archive-option2.png)

## Restore an archived flow or module
<a name="restore-flow"></a>

There are two ways you can restore flows or modules.

**Option 1: View list of archived flows or modules, and choose Restore**

1. Log in to the Connect Customer admin website with a user account that has the **Numbers and flows** - **Flows** - **Edit** permission in its security profile. If you are restoring a flow module, you need **Flow modules** - **Edit** permission.

1. On the navigation menu, choose **Routing**, **Flows**.

1. On the **Flows** page, choose **View archive**.

   1. To restore archived modules, on the **Flows** page, choose the **Modules** tab, and then choose **View archive**.

1. On the **Flows Archive** page, next to the flow or module you want to restore, under **Actions**, choose **...** and then choose **Restore**. This option is shown in the following image.  
![The Amazon Connect Flows Archive page showing the restore option in the Actions menu for an archived flow.](http://docs.aws.amazon.com/connect/latest/adminguide/images/flow-restorearchive1.png)

**Option 2: Restore the archived flow or module from the flow designer**

1. Open the archived flow or module in the flow designer.

1. From the dropdown menu, choose **Restore**, as shown in the following image.  
![The Amazon Connect flow designer dropdown menu showing the Restore option for an archived flow.](http://docs.aws.amazon.com/connect/latest/adminguide/images/flow-restorearchive.png)

## Delete an archived flow or module
<a name="delete-flow"></a>

You can delete archived flows and modules manually by using the Connect Customer admin website, or programmatically by using the [DeleteContactFlow](https://docs.aws.amazon.com/connect/latest/APIReference/API_DeleteContactFlow.html) API. 

**Warning**  
Deleted flows and modules cannot be restored. They are permanently deleted from your Connect Customer instance.

**Option 1: View list of archived flows or modules, and choose Delete**

1. Log in to the Connect Customer admin website with a user account that has the **Numbers and flows** - **Flows** - **Remove** permission in its security profile. If you are deleting a flow module, you need **Flow modules** - **Remove** permission.

1. On the navigation menu, choose **Routing**, **Flows**.

1. On the **Flows** page, choose **View archive**.

   1. To delete modules, on the **Flows** page, choose the **Modules** tab, and then choose **View archive**.

1. On the **Flows Archive** page, next to the flow or module you want to delete, under **Actions**, choose **...** and then choose **Delete**. 

1. Confirm that you want to delete the flow or module.

**Option 2: Delete the archived flow or module from the flow designer**

1. Open the archived flow or module in the flow designer.

1. From the dropdown menu, choose **Delete**.

1. Confirm that you want to delete the flow or module.