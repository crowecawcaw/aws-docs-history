# Amazon EC2 spot fleet role

If you create a managed compute environment that uses Amazon EC2 Spot Fleet Instances, you must
create the `AmazonEC2SpotFleetTaggingRole` policy. This policy grants Spot Fleet
permission to launch, tag, and terminate instances on your behalf. Specify the role in your Spot
Fleet request. You must also have the **AWSServiceRoleForEC2Spot** and
**AWSServiceRoleForEC2SpotFleet** service-linked roles for Amazon EC2 Spot and Spot
Fleet. Use the following instruction to create all of these roles. For more information, see
[Using
Service-Linked Roles](../../../IAM/latest/UserGuide/using-service-linked-roles.md "../../../IAM/latest/UserGuide/using-service-linked-roles.md") and [Creating a Role to Delegate
Permissions to an AWS Service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the
_IAM User Guide_.

###### Topics

- [Create Amazon EC2 spot fleet roles in the
  AWS Management Console](spot-fleet-roles-console.md "spot-fleet-roles-console.md")
- [Create Amazon EC2 spot fleet roles with the AWS CLI](spot-fleet-roles-cli.md "spot-fleet-roles-cli.md")
