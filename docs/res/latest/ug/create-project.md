

# Create a project
<a name="create-project"></a>

1. Choose **Create Project**.

1. Enter project details.

   The Project ID is a resource tag that can be used to track cost allocation in AWS Cost Explorer Service. For more information, see [Activating user-defined cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/activating-tags.html).
**Important**  
The project ID cannot be changed after creation.

   For information on **Advanced Options**, see [Add a launch template](project-launch-template.md).

1. (Optional) Turn on budgets for the project. For more information on budgets, see [Cost monitoring and control](cost-management.md). 

1. The home directory filesystem may either use the Shared Home Filesystem (default), EFS, FSx for Lustre, FSx NetApp ONTAP, or EBS volume storage.

   The shared home filesystem, EFS, FSx for Lustre, and FSx NetApp ONTAP can be shared across multiple projects and VDIs. However, the EBS volume storage option will require every VDI in that project to have their own home directory that is not shared between other VDIs or projects. You can also onboard multiple volumes from a single FSx NetApp ONTAP file system.  
![Create a new project with resource configurations](http://docs.aws.amazon.com/res/latest/ug/images/res-create-new-project.png)

1. Assign users, groups, or both the appropriate role ("Project Member" or "Project Owner"). See [Default permissions profiles](permission-matrix.md) for the actions each role can take.

1. Choose **Submit**. 