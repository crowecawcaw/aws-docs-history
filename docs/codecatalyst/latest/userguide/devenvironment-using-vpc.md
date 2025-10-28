Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Associating a VPC connection to a Dev Environment

A _VPC connection_ is a CodeCatalyst resource which contains all of the configurations
needed for your workflow to access a VPC. Space administrators can add their own VPC connections in the
Amazon CodeCatalyst console on behalf of space members. By adding a VPC connection, space members can run
workflow actions and create Dev Environments that adhere to network rules and can access resources in the associated VPC.

###### Important

Dev Environments with a VPC connection do not support
[third-party source repositories linked to CodeCatalyst](source-repositories-link.md "source-repositories-link.md").

You can only associate a Dev Environment to a VPC connection upon
Dev Environment creation. You can't change the VPC connection associated to your Dev Environment after you create it. If you'd like
to use a different VPC connection, you have to delete your current Dev Environment and create new one.

###### Note

Dev Environments can only be associated to a VPC connection with an AWS account that has access to your project.
For more information, see [Configuring project-restricted account connections](../adminguide/managing-accounts-restriction.md "../adminguide/managing-accounts-restriction.md") in the _Amazon CodeCatalyst Administrator Guide_.

Note that Dev Environments utilize several AWS resources and services upon creation. This means that Dev Environments
connect to the following AWS services:

- Amazon CodeCatalyst
- AWS SSM
- AWS KMS
- Amazon ECR
- Amazon CloudWatch
- Amazon ECS

###### Note

AWS Toolkit doesn't support Dev Environments creation with an associated VPC connection. Also note that if you
use an IDE other than AWS Cloud9, you may experience loading times of about five minutes.

You must have the **Space administrator** role or **Power user** role to
manage VPC connections at the space level. For more information about VPCs, see
[Managing Amazon VPCs in CodeCatalyst](../adminguide/managing-vpcs.md "../adminguide/managing-vpcs.md") in the _CodeCatalyst Administrator Guide_.
