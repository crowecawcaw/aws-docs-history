

# Software Stacks (AMIs)
<a name="software-stacks"></a>

From the Software Stacks page, you can configure Amazon Machine Images (AMIs) or manage existing ones.

![Software stacks admin console page with numbered annotations](http://docs.aws.amazon.com/res/latest/ug/images/res-softwarestackspage-2026.06.png)


1. To search for an existing software stack, use the operating system drop-down to filter by OS. 

1. Select the name of a software stack to view details about the stack.

1. Choose the radio button next to a software stack, then use the **Actions** menu to edit the stack and assign the stack to a project. 

1. Choose the **Register Software Stack** button to create a new stack.

## Register a new software stack
<a name="register-stack-project"></a>

The **Register Software Stack** button lets you create a new stack: 

**Note**  
You can use an unencrypted Systems Manager parameter as an alias for the software stack ID.  
The Systems Manager parameter will require the following tags for RES to access them:  
key: `res:EnvironmentName`, value: `{{<your RES environment name>}}`
key: `res:ModuleName`, value: `virtual-desktop-controller`

1. Choose **Register Software Stack**. 

1. Enter details for the new software stack, including name, description, AMI ID, and operating system.

1. (Optional) Use the **Allowed Instance Types** field to specify the instance families or types that are permitted for this software stack. You can enter instance families (for example, `t3`) or specific instance sizes (for example, `t3.xlarge`).

1. Choose **Submit**.   
![Admin console pop-out page that lets you register a new software stack](http://docs.aws.amazon.com/res/latest/ug/images/res-register-new-software-stack.png)

## Assign a software stack to a project
<a name="assign-stack-project"></a>

When you create a new software stack, you can assign the stack to projects. But, if you need to add the stack to a project after the initial creation, do the following: 

**Note**  
You can only assign software stacks to projects of which you are a member.

1. On the **Software Stacks** page, select the radio button for the software stack that you want to add to a project.

1. Choose **Actions**.

1. Choose **Edit**. 

1. Use the **Projects** drop-down to select the project.  
![Admin console showing fields to update a software stack for a project](http://docs.aws.amazon.com/res/latest/ug/images/res-update-software-stack.png)

1. Choose **Submit**.

You can also edit the software stack from the stack details page.

## Modify the software stack's VDI instance list
<a name="software-stack-vdi-instance-list"></a>

For each registered software stack, you can choose the allowed instance families and types. The list of the options for each software stack is filtered by the options defined in the **Desktop settings**. You can find and modify the global **Allowed Instance Families and Types** there. 

![Admin console page showing desktop settings under session management](http://docs.aws.amazon.com/res/latest/ug/images/res-vdi-instance-list1.png)


**To edit the **Allowed Instance Families and Types** attribute of a software stack:**

1. On the **Software Stacks** page, choose the radio button for the software stack.

1. Choose **Actions**, then select **Edit Stack**.

1. Choose the desired instance families and types from the drop-down list under **Allowed Instance Families and Types**.  
![Update software stack pop-out that lets you edit allowed instance families and types](http://docs.aws.amazon.com/res/latest/ug/images/res-vdi-instance-list2.png)

1. Select **Submit**.

**Note**  
If the global set of **Allowed Instance Families and Types** includes an instance family and an instance type within that family (for example `t3` and `t3.large`), the available options for the **Allowed Instance Families and Types** attribute of a software stack will only include the instance family. 

**Important**  
When an instance type/family is deleted from the Allow list at the environment level it should automatically be removed from all software stacks.
Instance types/families that are added at the environment level are not automatically added to software stacks.

## View software stack details
<a name="view-stack-details"></a>

From the **Software Stacks** page, select the software stack name to view its details. You can also select the radio button for a software stack, choose **Actions** and select **Edit** to edit the software stack.

## VDI tenancy support
<a name="vdi-tenancy-support"></a>

When you register a new software stack or edit an existing software stack, you can select the tenancy for the VDIs launched from this software stack. The following three tenancies are supported:
+ Shared (Default) - Run VDIs with shared hardware instances 
+ Dedicated Instance - Run VDIs with dedicated instances 
+ Dedicated Host - Run VDIs with a dedicated host 

![Admin console pop-out page that lets you select tenancy type for launched VDIs](http://docs.aws.amazon.com/res/latest/ug/images/res-vdi-tenancy-support1.png)


When you select the dedicated host tenancy type, you must also select the tenancy affinity and the target host type. The following target host types are supported: 
+ Host Resource Group - Host resource group created in AWS License Manager 
+ Host ID - A specific host ID 

![Admin console pop-out page that lets you select tenancy affinity for launched VDIs](http://docs.aws.amazon.com/res/latest/ug/images/res-vdi-tenancy-support2.png)


![Admin console pop-out page that lets you select target host type for launched VDIs](http://docs.aws.amazon.com/res/latest/ug/images/res-vdi-tenancy-support3.png)


To specify any self-managed licenses required by your VDIs when you launch them with the dedicated host tenancy, associate the licenses with your AMI following [ Associating self-managed licenses and AMIs](https://docs.aws.amazon.com/license-manager/latest/userguide/license-rules.html#ami-associations) in the *AWS License Manager User Guide*.

## Adding a Rocky Linux 9 software stack
<a name="add-rocky-linux9-stack"></a>

RES does not have a default software stack for Rocky Linux 9, so this section offers a recommendation on which Rocky AMI to use and how to use it.

1. Sign in to the AWS Management Console, and go to the [AMI Catalog page](https://console.aws.amazon.com/ec2/home#AMICatalog) within the EC2 Console.

1. Search for AMIs under the **AWS Marketplace** tab with the name **Rocky Linux 9**.

1. Select the AMI named **Rocky Linux 9 (Official) - x86\_64** from **Rocky Linux**.  
![Screenshot showing Rocky Linux 9 AMI search results in the AMI Catalog](http://docs.aws.amazon.com/res/latest/ug/images/res-rocky-linux9.png)

1. Once selected, choose **Subscribe now**.

1. Scroll up, and copy the AMI Id for **Selected AMI**.  
![Screenshot showing the AMI Catalog with the selected AMI ID](http://docs.aws.amazon.com/res/latest/ug/images/res-ami-catalog.png)

1. Go to the RES portal, and register a new Software Stack under the **Software Stacks** page using this AMI.