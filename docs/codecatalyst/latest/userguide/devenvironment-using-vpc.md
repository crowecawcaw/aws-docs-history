

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Associating a VPC connection to a Dev Environment
<a name="devenvironment-using-vpc"></a>

A *VPC connection* is a CodeCatalyst resource which contains all of the configurations needed for your workflow to access a VPC. Space administrators can add their own VPC connections in the Amazon CodeCatalyst console on behalf of space members. By adding a VPC connection, space members can run workflow actions and create Dev Environments that adhere to network rules and can access resources in the associated VPC.

**Important**  
Dev Environments with a VPC connection do not support [third-party source repositories linked to CodeCatalyst](source-repositories-link.md).

You can only associate a Dev Environment to a VPC connection upon Dev Environment creation. You can't change the VPC connection associated to your Dev Environment after you create it. If you'd like to use a different VPC connection, you have to delete your current Dev Environment and create new one.

**Note**  
Dev Environments can only be associated to a VPC connection with an AWS account that has access to your project. For more information, see [ Configuring project-restricted account connections](https://docs.aws.amazon.com/codecatalyst/latest/adminguide/managing-accounts-restriction.html) in the *Amazon CodeCatalyst Administrator Guide*.

Note that Dev Environments utilize several AWS resources and services upon creation. This means that Dev Environments connect to the following AWS services:
+ Amazon CodeCatalyst
+ AWS SSM
+ AWS KMS
+ Amazon ECR
+ Amazon CloudWatch
+ Amazon ECS

**Note**  
AWS Toolkit doesn't support Dev Environments creation with an associated VPC connection. Also note that if you use an IDE other than AWS Cloud9, you may experience loading times of about five minutes.

You must have the **Space administrator** role or **Power user** role to manage VPC connections at the space level. For more information about VPCs, see [ Managing Amazon VPCs in CodeCatalyst](https://docs.aws.amazon.com/codecatalyst/latest/adminguide/managing-vpcs.html) in the *CodeCatalyst Administrator Guide*.