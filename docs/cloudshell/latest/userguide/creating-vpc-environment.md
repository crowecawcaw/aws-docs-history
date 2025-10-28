# Creating a CloudShell VPC environment

This topic walks you through the steps to create a VPC environment in
CloudShell.

**Prerequisites**

Your administrator must provide the necessary IAM permissions for you to be able to
create VPC environments. For more information about enabling permissions to create
CloudShell VPC environments, see [Required IAM permissions for creating and
using CloudShell VPC environments](aws-cloudshell-vpc-permissions-1.md "aws-cloudshell-vpc-permissions-1.md").

###### To create a CloudShell VPC environment

1. On the CloudShell console page, choose the **+** icon and then
   choose **Create VPC environment** from the dropdown menu.
2. On the **Create a VPC environment** page, enter a name for your VPC
   environment in the **Name** box.
3. From the **Virtual private cloud (VPC)** dropdown list, choose a VPC.
4. From the **Subnet** dropdown list, choose a subnet.
5. From the **Security** group dropdown list, choose one or more
   security groups that you want to assign to your VPC environment.

###### Note

You can choose a maximum of five security groups. 6. Choose **Create** to create your VPC environment. 7. (Optional) Choose **Actions**, and then choose **View
details** to review the details of the newly created VPC environment. The IP
address of your VPC environment is displayed in the command line prompt.
For information about using VPC environments, see [Getting started with AWS CloudShell](getting-started.md "getting-started.md").
