# Set up an EMR Studio

Complete the following steps to set up an EMR Studio.

**Before you start**

###### Note

If you plan to use EMR Studio with Amazon EMR on EKS, we recommend that you first set up
Amazon EMR on EKS for EMR Studio before you set up a Studio.

Before you set up an EMR Studio, make sure you have the following items:

- An AWS account. For instructions, see [Before you set up Amazon EMR](emr-setting-up.md "emr-setting-up.md").
- Permissions to create and manage an EMR Studio. For more information, see [Administrator permissions to create and manage
  an EMR Studio](emr-studio-admin-permissions.md "emr-studio-admin-permissions.md").
- An Amazon S3 bucket where EMR Studio can back up the Workspaces
  and notebook files in your Studio. For instructions, see [Creating a bucket](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md") in the _Amazon Simple Storage Service (S3) User
  Guide_.
- If you want to attach to an Amazon EMR on EC2 or Amazon EMR on EKS cluster, or use Git
  repositories, you need an Amazon Virtual Private Cloud (VPC) for the Studio, and a maximum of five
  subnets. You don't need a VPC to use EMR Studio with EMR Serverless. For tips on how
  to configure networking, see [VPC and subnet best practices for EMR Studio](emr-studio-vpc-subnet-best-practices.md "emr-studio-vpc-subnet-best-practices.md").

###### To set up an EMR Studio

1. [Choose an authentication mode for
   Amazon EMR Studio](emr-studio-authentication.md "emr-studio-authentication.md")
2. Create the following Studio resources.
   - [Create an EMR Studio service role](emr-studio-service-role.md "emr-studio-service-role.md")
   - [Configure EMR Studio user permissions for
     Amazon EC2 or Amazon EKS](emr-studio-user-permissions.md "emr-studio-user-permissions.md")
   - (Optional) [Define security groups to control EMR Studio
     network traffic](emr-studio-security-groups.md "emr-studio-security-groups.md").

3. [Create an EMR Studio](emr-studio-create-studio.md "emr-studio-create-studio.md")
4. [Assign a user or group to an
   EMR Studio](emr-studio-manage-users.md#emr-studio-assign-users-groups "emr-studio-manage-users.md#emr-studio-assign-users-groups")
   After you complete the setup steps, you can [Use an Amazon EMR Studio](use-an-emr-studio.md "use-an-emr-studio.md").
