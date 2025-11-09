# Lake Formation personas and IAM permissions reference

This section lists some suggested Lake Formation personas and their suggested AWS Identity and Access Management
(IAM) permissions. For information about Lake Formation permissions, see [Lake Formation permissions reference](lf-permissions-reference.md "lf-permissions-reference.md").

## AWS Lake Formation personas

The following table lists the suggested AWS Lake Formation personas.

| Lake Formation Personas       | Persona                                                                                                                                                                                                                                                                                                                                                          | Description |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| IAM administrator (superuser) | (Required) User who can create IAM users and roles. Has the<br>`AdministratorAccess` AWS managed policy. Has all<br>permissions on all Lake Formation resources. Can add data lake administrators.<br>Cannot grant Lake Formation permissions if not also designated a data lake<br>administrator.                                                               |
| Data lake administrator       | (Required) User who can register Amazon S3 locations, access the Data Catalog, create databases,<br>create and run workflows, grant Lake Formation permissions to other users, and<br>view AWS CloudTrail logs. Has fewer IAM permissions than the IAM<br>administrator, but enough to administer the data lake. Cannot add other<br>data lake administrators.   |
| Read only administrator       | (Optional) User who can view principals, Data Catalog resources, permissions, and<br>AWS CloudTrail logs, without the permissions to make updates.                                                                                                                                                                                                               |
| Data engineer                 | (Optional) User who can create databases, create and run crawlers and workflows, and<br>grant Lake Formation permissions on the Data Catalog tables that the crawlers and<br>workflows create. We recommend that you make all data engineers database<br>creators. For more information, see [Creating a database](creating-database.md "creating-database.md"). |
| Data analyst                  | (Optional) User who can run queries against the data lake using, for example,<br>Amazon Athena. Has only enough permissions to run queries.                                                                                                                                                                                                                      |
| Workflow role                 | (Required) Role that runs a workflow on behalf of a user. You specify this role when<br>you create a workflow from a blueprint.                                                                                                                                                                                                                                  |

###### Note

In Lake Formation, data lake administrators added after database creation can grant permissions
but don't automatically have data access permissions such as SELECT or DESCRIBE.
Administrators who create databases receive `SUPER` permissions on those
databases. This behavior is intentional—while all administrators can grant
themselves necessary permissions, these permissions aren't automatically applied to
pre-existing resources. Therefore, administrators must explicitly grant themselves
access to databases that existed before they were assigned admin privileges.

## AWS managed policies for Lake Formation

You can grant the AWS Identity and Access Management (IAM) permissions that are required to work with AWS Lake Formation by
using AWS managed policies and inline policies. The following AWS managed policies are
available for Lake Formation.

### AWS managed policy:AWSLakeFormationDataAdmin

[AWSLakeFormationDataAdmin](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSLakeFormationDataAdmin "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSLakeFormationDataAdmin") policy
grants administrative access to AWS Lake Formation and related services such as AWS Glue to manage data lakes.

You can attach `AWSLakeFormationDataAdmin` to your users, groups, and roles.

**Permission details**

- `CloudTrail` – Allows principals to view AWS CloudTrail logs. This
  is required to review any errors in the set up of the data lake.
- `Glue` – Allows principals to view, create, and update
  metadata tables and databases in Data Catalog. This includes API operations that
  start with `Get`, `List`, `Create`,
  `Update`, `Delete`, and `Search`. This
  is required to manage the metadata of the data lake tables.
- `IAM` – Allows principals to retrieve information about IAM users, roles,
  and policies attached to the roles. This is required for the data admin to
  review and list IAM users and roles to grant Lake Formation
  permissions.
- `Lake Formation` – Grants data lake admins required Lake Formation permissions to
  manage data lakes.
- `S3` – Allows principals to retrieve information about Amazon S3 buckets and their locations in order to set up the data location for data lakes.

```
"Statement": [
        {
            "Sid": "AWSLakeFormationDataAdminAllow",
            "Effect": "Allow",
            "Action": [
                "lakeformation:*",
                "cloudtrail:DescribeTrails",
                "cloudtrail:LookupEvents",
                "glue:CreateCatalog",
		"glue:UpdateCatalog",
                "glue:DeleteCatalog",
		"glue:GetCatalog",
	        "glue:GetCatalogs",
                "glue:GetDatabase",
                "glue:GetDatabases",
                "glue:CreateDatabase",
                "glue:UpdateDatabase",
                "glue:DeleteDatabase",
                "glue:GetConnections",
                "glue:SearchTables",
                "glue:GetTable",
                "glue:CreateTable",
                "glue:UpdateTable",
                "glue:DeleteTable",
                "glue:GetTableVersions",
                "glue:GetPartitions",
                "glue:GetTables",
                "glue:ListWorkflows",
                "glue:BatchGetWorkflows",
                "glue:DeleteWorkflow",
                "glue:GetWorkflowRuns",
                "glue:StartWorkflowRun",
                "glue:GetWorkflow",
                "s3:ListBucket",
                "s3:GetBucketLocation",
                "s3:ListAllMyBuckets",
                "s3:GetBucketAcl",
                "iam:ListUsers",
                "iam:ListRoles",
                "iam:GetRole",
                "iam:GetRolePolicy"
            ],
            "Resource": "*"
        },
        {
            "Sid": "AWSLakeFormationDataAdminDeny",
            "Effect": "Deny",
            "Action": [
                "lakeformation:PutDataLakeSettings"
            ],
                "Resource": "*"
        }
    ]
}

```

###### Note

The `AWSLakeFormationDataAdmin` policy does not grant every required
permission for data lake administrators. Additional permissions are needed to create and run
workflows and register locations with the service linked role
`AWSServiceRoleForLakeFormationDataAccess`. For more information, see [Create a data lake administrator](initial-lf-config.md#create-data-lake-admin "initial-lf-config.md#create-data-lake-admin") and [Using service-linked roles for Lake Formation](service-linked-roles.md "service-linked-roles.md").

### AWS managed policy:AWSLakeFormationCrossAccountManager

[AWSLakeFormationCrossAccountManager](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSLakeFormationCrossAccountManager "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSLakeFormationCrossAccountManager") policy provides cross account access to AWS Glue resources via Lake Formation,
and grants read access to other required services such as AWS Organizations and AWS RAM.

You can attach `AWSLakeFormationCrossAccountManager` to your users, groups, and roles.

**Permission details**

This policy includes the following permissions.

- `Glue` – Allows principals to set or delete the Data Catalog resource policy for access control.
- `Organizations` – Allows principals to retrieve account and organizational
  unit (OU) information for an organization.
- `ram:CreateResourceShare` – Allows principals to create a resource share.
- `ram:UpdateResourceShare` –Allows principals to modify some properties of the specified resource share.
- `ram:DeleteResourceShare` – Allows principals to delete the specified resource share.
- `ram:AssociateResourceShare` – Allows principals to add the specified list of principals and list of resources to a resource share.
- `ram:DisassociateResourceShare` – Allows principals to remove the specified principals or resources from participating in the specified resource share.
- `ram:GetResourceShares`– Allows principals to retrieve details about the resource shares that you own or that are shared with you.
- `ram:RequestedResourceType` – Allows principals to retrieve the resource type (database, table or catalog).
- `AssociateResourceSharePermission` – Allows principals to add or replace the AWS RAM permission for a resource type included in a resource share. You can have exactly one permission associated with each resource type in the resource share.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Sid": "AllowCreateResourceShare",
 "Effect": "Allow",
 "Action": [
 "ram:CreateResourceShare"
 ],
 "Resource": "*",
 "Condition": {
 "StringLikeIfExists": {
 "ram:RequestedResourceType": [
 "glue:Table",
 "glue:Database",
 "glue:Catalog"
 ]
 }
 }
 },
 {
 "Sid": "AllowManageResourceShare",
 "Effect": "Allow",
 "Action": [
 "ram:UpdateResourceShare",
 "ram:DeleteResourceShare",
 "ram:AssociateResourceShare",
 "ram:DisassociateResourceShare",
 "ram:GetResourceShares"
 ],
 "Resource": "*",
 "Condition": {
 "StringLike": {
 "ram:ResourceShareName": [
 "LakeFormation*"
 ]
 }
 }
 },
 {
 "Sid": "AllowManageResourceSharePermissions",
 "Effect": "Allow",
 "Action": [
 "ram:AssociateResourceSharePermission"
 ],
 "Resource": "*",
 "Condition": {
 "ArnLike": {
 "ram:PermissionArn": [
 "arn:aws:ram::aws:permission/AWSRAMLFEnabled*"
 ]
 }
 }
 },
 {
 "Sid": "AllowXAcctManagerPermissions",
 "Effect": "Allow",
 "Action": [
 "glue:PutResourcePolicy",
 "glue:DeleteResourcePolicy",
 "organizations:DescribeOrganization",
 "organizations:DescribeAccount",
 "ram:Get*",
 "ram:List*"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowOrganizationsPermissions",
 "Effect": "Allow",
 "Action": [
 "organizations:ListRoots",
 "organizations:ListAccountsForParent",
 "organizations:ListOrganizationalUnitsForParent"
 ],
 "Resource": "*"
 }
 ]
}`

```

### AWS managed policy:AWSGlueConsoleFullAccess

[AWSGlueConsoleFullAccess](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AWSGlueConsoleFullAccess "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AWSGlueConsoleFullAccess") policy grants full access to AWS Glue resources when an identity that the policy is attached to uses the AWS Management Console.
If you follow the naming convention for resources specified in this policy, users have full console capabilities. This policy is typically attached to users of the AWS Glue console.

In addition, AWS Glue and Lake Formation assume the service role `AWSGlueServiceRole` to
allow access to related services, including Amazon Elastic Compute Cloud (Amazon EC2), Amazon Simple Storage Service (Amazon S3), and
Amazon CloudWatch.

### AWS managed

policy:LakeFormationDataAccessServiceRolePolicy

This policy is attached to a service-linked role named
`ServiceRoleForLakeFormationDataAccess` that allows the service
to perform actions on resources at your request. You can't attach this policy to
your IAM identities.

This policy allows the Lake Formation integrated AWS services such as Amazon Athena or Amazon Redshift to use the service-linked role to discover Amazon S3 resources.

For more information see, [Using service-linked roles for Lake Formation](service-linked-roles.md "service-linked-roles.md").

**Permission details**

This policy includes the following permission.

- `s3:ListAllMyBuckets` – Returns a list of all buckets
  owned by the authenticated sender of the request.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "LakeFormationDataAccessServiceRolePolicy",
 "Effect": "Allow",
 "Action": [
 "s3:ListAllMyBuckets"
 ],
 "Resource": [
 "arn:aws:s3:::*"
 ]
 }
 ]
}`

```

###### Lake Formation updates to AWS managed policies

View details about updates to AWS managed policies for Lake Formation since this service began tracking these changes.

| Change                                                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Date           |
| ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| Lake Formation updated `AWSLakeFormationCrossAccountManager`<br>policy.      | Lake Formation enhanced the [AWSLakeFormationCrossAccountManager](https://us-east-1.console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSLakeFormationCrossAccountManager "https://us-east-1.console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSLakeFormationCrossAccountManager") policy by replacing the `StringLike` condition operator<br>with the `ArnLike` operator that allows IAM to perform the ARN format check.                                                                                                                                                                                                            | January, 2025  |
| Lake Formation updated `AWSLakeFormationDataAdmin` policy.                   | Lake Formation enhanced the [AWSLakeFormationDataAdmin](https://us-east-1.console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSLakeFormationDataAdmin "https://us-east-1.console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSLakeFormationDataAdmin") policy by adding the following<br>AWS Glue Data Catalog CRUD APIs as part of the multi-catalog feature.<br>• glue:CreateCatalog<br>• glue:UpdateCatalog<br>• glue:DeleteCatalog<br>• glue:GetCatalog<br>• glue:GetCatalogs<br>This managed policy change is to ensure that the Lake Formation<br>administrator persona by default has IAM permission on these new<br>operations. | December, 2024 |
| Lake Formation updated `AWSLakeFormationCrossAccountManager`<br>policy.      | Lake Formation enhanced the [AWSLakeFormationCrossAccountManager](https://us-east-1.console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSLakeFormationCrossAccountManager "https://us-east-1.console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSLakeFormationCrossAccountManager") policy by adding Sid<br>elements to the policy statement.                                                                                                                                                                                                                                                                                          | March, 2024    |
| Lake Formation updated `AWSLakeFormationDataAdmin`<br>policy.                | Lake Formation enhanced the [AWSLakeFormationDataAdmin](https://us-east-1.console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSLakeFormationDataAdmin "https://us-east-1.console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSLakeFormationDataAdmin") policy by adding a Sid element to<br>the policy statement and removing a redundant action.                                                                                                                                                                                                                                                                                       | March, 2024    |
| Lake Formation updated `LakeFormationDataAccessServiceRolePolicy`<br>policy. | Lake Formation enhanced the [LakeFormationDataAccessServiceRolePolicy](https://us-east-1.console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/LakeFormationDataAccessServiceRolePolicy "https://us-east-1.console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/LakeFormationDataAccessServiceRolePolicy") policy by adding a<br>Sid element to the policy statement.                                                                                                                                                                                                                                                                          | February, 2024 |
| Lake Formation updated `AWSLakeFormationCrossAccountManager` policy.         | Lake Formation enhanced the [AWSLakeFormationCrossAccountManager](https://us-east-1.console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSLakeFormationCrossAccountManager "https://us-east-1.console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSLakeFormationCrossAccountManager") policy by adding a new<br>permission to enable cross-account data sharing in hybrid access<br>mode.                                                                                                                                                                                                                                                | October, 2023  |
| Lake Formation updated `AWSLakeFormationCrossAccountManager` policy.         | Lake Formation enhanced the [AWSLakeFormationCrossAccountManager](https://us-east-1.console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSLakeFormationCrossAccountManager "https://us-east-1.console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSLakeFormationCrossAccountManager") policy to create only one resource<br>share per recipient account when the a resource is first shared. All resources shared<br>thereafter with the same account are attached to the same resource share.                                                                                                                                           | May 6, 2022    |
| Lake Formation started tracking changes.                                     | Lake Formation started tracking changes for its AWS managed policies.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | May 6, 2022    |

## Personas suggested permissions

The following are the suggested permissions for each persona. The IAM administrator is not
included because that user has all permissions on all resources.

###### Topics

- [Data lake administrator permissions](#persona-dl-admin "#persona-dl-admin")
- [Read only administrator permissions](#persona-read-only-admin "#persona-read-only-admin")
- [Data engineer permissions](#persona-engineer "#persona-engineer")
- [Data analyst permissions](#persona-user "#persona-user")
- [Workflow role permissions](#persona-workflow-role "#persona-workflow-role")

### Data lake administrator permissions

###### Important

In the following policies, replace `<account-id>` with
a valid AWS account number, and replace `<workflow_role>`
with the name of a role that has permissions to run a workflow, as defined in
[Workflow role permissions](#persona-workflow-role "#persona-workflow-role").

| Policy Type                                                                                                                                                                                                                                                                                                                                                                                                                  | Policy                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AWS managed policies                                                                                                                                                                                                                                                                                                                                                                                                         | • `AWSLakeFormationDataAdmin`<br>• `LakeFormationDataAccessServiceRolePolicy`<br>(service-linked role policy)<br>• `AWSGlueConsoleFullAccess`<br>(Optional)<br>• `CloudWatchLogsReadOnlyAccess`<br>(Optional)<br>• `AWSLakeFormationCrossAccountManager`<br>(Optional)<br>• `AmazonAthenaFullAccess` (Optional)<br>For information about the optional AWS managed policies, see<br>[Create a data lake administrator](initial-lf-config.md#create-data-lake-admin "initial-lf-config.md#create-data-lake-admin"). |
| Inline policy (for creating the Lake Formation service-linked role)                                                                                                                                                                                                                                                                                                                                                          | ``<br>{<br>"Version": "2012-10-17",<br>"Statement": [<br>{<br>"Effect": "Allow",<br>"Action": "iam:CreateServiceLinkedRole",<br>"Resource": "*",<br>"Condition": {<br>"StringEquals": {<br>"iam:AWSServiceName": "lakeformation.amazonaws.com"<br>}<br>}<br>},<br>{<br>"Effect": "Allow",<br>"Action": [<br>"iam:PutRolePolicy"<br>],<br>"Resource": "arn:aws:iam::`<account-id>`:role/aws-service-role/lakeformation.amazonaws.com/AWSServiceRoleForLakeFormationDataAccess"<br>}<br>]<br>}<br>``                |
| (Optional) Inline policy (passrole policy for the workflow role).<br>This is required only if the data lake administrator creates and<br>runs workflows.                                                                                                                                                                                                                                                                     | ``<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Sid": "PassRolePermissions",<br>"Effect": "Allow",<br>"Action": [<br>"iam:PassRole"<br>],<br>"Resource": [<br>"arn:aws:iam::`111122223333`:role/`<workflow_role>`"<br>]<br>}<br>]<br>}`<br>``                                                                                                                                                                                                                                                      |
| (Optional) Inline policy (if your account is granting or<br>receiving cross-account Lake Formation permissions). This policy is for<br>accepting or rejecting AWS RAM resource share invitations, and for<br>enabling the granting of cross-account permissions to organizations.<br>`ram:EnableSharingWithAwsOrganization` is required<br>only for data lake administrators in the AWS Organizations<br>management account. | ``<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Effect": "Allow",<br>"Action": [<br>"ram:AcceptResourceShareInvitation",<br>"ram:RejectResourceShareInvitation",<br>"ec2:DescribeAvailabilityZones",<br>"ram:EnableSharingWithAwsOrganization"<br>],<br>"Resource": "*"<br>}<br>]<br>}`<br>``                                                                                                                                                                                                      |

### Read only administrator permissions

| Policy type           | Policy                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Inline policy (basic) | ``<br>`{<br>"Version":"2012-10-17",<br>"Statement":[<br>{<br>"Effect":"Allow",<br>"Action":[<br>"lakeformation:GetEffectivePermissionsForPath",<br>"lakeformation:ListPermissions",<br>"lakeformation:ListDataCellsFilter",<br>"lakeformation:GetDataCellsFilter",<br>"lakeformation:SearchDatabasesByLFTags",<br>"lakeformation:SearchTablesByLFTags",<br>"lakeformation:GetLFTag",<br>"lakeformation:ListLFTags",<br>"lakeformation:GetResourceLFTags",<br>"lakeformation:ListLakeFormationOptins",<br>"cloudtrail:DescribeTrails",<br>"cloudtrail:LookupEvents",<br>"glue:GetDatabase",<br>"glue:GetDatabases",<br>"glue:GetConnections",<br>"glue:SearchTables",<br>"glue:GetTable",<br>"glue:GetTableVersions",<br>"glue:GetPartitions",<br>"glue:GetTables",<br>"glue:GetWorkflow",<br>"glue:ListWorkflows",<br>"glue:BatchGetWorkflows",<br>"glue:GetWorkflowRuns",<br>"glue:GetWorkflow",<br>"s3:ListBucket",<br>"s3:GetBucketLocation",<br>"s3:ListAllMyBuckets",<br>"s3:GetBucketAcl",<br>"iam:ListUsers",<br>"iam:ListRoles",<br>"iam:GetRole",<br>"iam:GetRolePolicy"<br>],<br>"Resource":"*"<br>},<br>{<br>"Effect":"Deny",<br>"Action":[<br>"lakeformation:PutDataLakeSettings"<br>],<br>"Resource":"*"<br>}<br>]<br>}`<br>`` |

### Data engineer permissions

###### Important

In the following policies, replace `<account-id>` with
a valid AWS account number, and replace `<workflow_role>`
with the name of the workflow role.

| Policy Type                                                                                                       | Policy                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AWS managed policy                                                                                                | `AWSGlueConsoleFullAccess`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Inline policy (basic)                                                                                             | ``<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Effect": "Allow",<br>"Action": [<br>"lakeformation:GetDataAccess",<br>"lakeformation:GrantPermissions",<br>"lakeformation:RevokePermissions",<br>"lakeformation:BatchGrantPermissions",<br>"lakeformation:BatchRevokePermissions",<br>"lakeformation:ListPermissions",<br>"lakeformation:AddLFTagsToResource",<br>"lakeformation:RemoveLFTagsFromResource",<br>"lakeformation:GetResourceLFTags",<br>"lakeformation:ListLFTags",<br>"lakeformation:GetLFTag",<br>"lakeformation:SearchTablesByLFTags",<br>"lakeformation:SearchDatabasesByLFTags",<br>"lakeformation:GetWorkUnits",<br>"lakeformation:GetWorkUnitResults",<br>"lakeformation:StartQueryPlanning",<br>"lakeformation:GetQueryState",<br>"lakeformation:GetQueryStatistics"<br>],<br>"Resource": "*"<br>}<br>]<br>}`<br>`` |
| Inline policy (for operations on governed tables, including<br>operations within transactions)                    | ``<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Effect": "Allow",<br>"Action": [<br>"lakeformation:StartTransaction",<br>"lakeformation:CommitTransaction",<br>"lakeformation:CancelTransaction",<br>"lakeformation:ExtendTransaction",<br>"lakeformation:DescribeTransaction",<br>"lakeformation:ListTransactions",<br>"lakeformation:GetTableObjects",<br>"lakeformation:UpdateTableObjects",<br>"lakeformation:DeleteObjectsOnCancel"<br>],<br>"Resource": "*"<br>}<br>]<br>}`<br>``                                                                                                                                                                                                                                                                                                                                                  |
| Inline policy (for metadata access control using the Lake Formation tag-based<br>access control (LF-TBAC) method) | ``<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Effect": "Allow",<br>"Action": [<br>"lakeformation:AddLFTagsToResource",<br>"lakeformation:RemoveLFTagsFromResource",<br>"lakeformation:GetResourceLFTags",<br>"lakeformation:ListLFTags",<br>"lakeformation:GetLFTag",<br>"lakeformation:SearchTablesByLFTags",<br>"lakeformation:SearchDatabasesByLFTags"<br>],<br>"Resource": "*"<br>}<br>]<br>}`<br>``                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Inline policy (passrole policy for the workflow role)                                                             | ``<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Sid": "PassRolePermissions",<br>"Effect": "Allow",<br>"Action": [<br>"iam:PassRole"<br>],<br>"Resource": [<br>"arn:aws:iam::`111122223333`:role/`<workflow_role>`"<br>]<br>}<br>]<br>}`<br>``                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

### Data analyst permissions

| Policy Type                                                                                               | Policy                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| AWS managed policy                                                                                        | `AmazonAthenaFullAccess`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Inline policy (basic)                                                                                     | `<br>{<br>"Version": "2012-10-17",<br>"Statement": [<br>{<br>"Effect": "Allow",<br>"Action": [<br>"lakeformation:GetDataAccess",<br>"glue:GetTable",<br>"glue:GetTables",<br>"glue:SearchTables",<br>"glue:GetDatabase",<br>"glue:GetDatabases",<br>"glue:GetPartitions",<br>"lakeformation:GetResourceLFTags",<br>"lakeformation:ListLFTags",<br>"lakeformation:GetLFTag",<br>"lakeformation:SearchTablesByLFTags",<br>"lakeformation:SearchDatabasesByLFTags"<br>],<br>"Resource": "*"<br>}<br>]<br>}<br>` |
| (Optional) Inline policy (for operations on governed tables,<br>including operations within transactions) | ``<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Effect": "Allow",<br>"Action": [<br>"lakeformation:StartTransaction",<br>"lakeformation:CommitTransaction",<br>"lakeformation:CancelTransaction",<br>"lakeformation:ExtendTransaction",<br>"lakeformation:DescribeTransaction",<br>"lakeformation:ListTransactions",<br>"lakeformation:GetTableObjects",<br>"lakeformation:UpdateTableObjects",<br>"lakeformation:DeleteObjectsOnCancel"<br>],<br>"Resource": "*"<br>}<br>]<br>}`<br>``       |

### Workflow role permissions

This role has the permissions required to run a workflow. You specify a role with
these permissions when you create a workflow.

###### Important

In the following policies, replace `<region>` with a
valid AWS Region identifier (for example `us-east-1`),
`<account-id>` with a valid AWS account number,
`<workflow_role>` with the name of the workflow role,
and `<your-s3-cloudtrail-bucket>` with the Amazon S3 path to
your AWS CloudTrail logs.

| Policy Type                                                                                   | Policy                                                                                                                                                                                                                                                       |
| --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| AWS managed policy                                                                            | `AWSGlueServiceRole`                                                                                                                                                                                                                                         |
| Inline policy (data access)                                                                   | `<br>{<br>"Version": "2012-10-17",<br>"Statement": [<br>{<br>"Sid": "Lakeformation",<br>"Effect": "Allow",<br>"Action": [<br>"lakeformation:GetDataAccess",<br>"lakeformation:GrantPermissions"<br>],<br>"Resource": "*"<br>}<br>]<br>}<br>`                 |
| Inline policy (passrole policy for the workflow role)                                         | ``<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Sid": "PassRolePermissions",<br>"Effect": "Allow",<br>"Action": [<br>"iam:PassRole"<br>],<br>"Resource": [<br>"arn:aws:iam::`111122223333`:role/`<workflow_role>`"<br>]<br>}<br>]<br>}`<br>`` |
| Inline policy (for ingesting data outside the data lake, for<br>example, AWS CloudTrail logs) | ``<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Effect": "Allow",<br>"Action": ["s3:GetObject", "s3:ListBucket"],<br>"Resource": ["arn:aws:s3:::`<your-s3-cloudtrail-bucket>`/*"]<br>}<br>]<br>}`<br>``                                       |
