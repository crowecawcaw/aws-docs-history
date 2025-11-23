# Identity and access management for Data

Exports

AWS Identity and Access Management (IAM) is an AWS service that helps an administrator
securely control access to AWS resources. IAM administrators control who can be _authenticated_ (signed in) and _authorized_ (have permissions) to use Billing resources. IAM is an AWS service
that you can use with no additional charge.

To use Data Exports, an IAM user needs to be given access to actions in the `bcm-data-exports
 namespace` in IAM. See the following table for the available actions.

| Data Exports action | Description                                                                                                                           | Access level | Resource types  | Condition keys                                                       |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------ | --------------- | -------------------------------------------------------------------- |
| CreateExport        | Allows user to create an Export and specifies query, delivery configurations,<br>schedule configurations, and content configurations. | Write        | export<br>table | aws:RequestTag/${TagKey}<br>aws:TagKeys                              |
| UpdateExport        | Allows user to update an existing Export.                                                                                             | Write        | export<br>table | aws:ResourceTag/${TagKey}                                            |
| DeleteExport        | Allows user to delete an existing Export.                                                                                             | Write        | export          | aws:ResourceTag/${TagKey}                                            |
| GetExport           | Allows user to view an existing Export.                                                                                               | Read         | export          | aws:ResourceTag/${TagKey}                                            |
| ListExports         | Allows user to list all existing Exports.                                                                                             | Read         |                 |                                                                      |
| GetExecution        | Allows user to see details of the given Execution, including metadata and schema<br>of the exported data.                             | Read         | export          | aws:ResourceTag/${TagKey}                                            |
| ListExecutions      | Allows user to list all Executions of the provided Export identifier.                                                                 | Read         | export          | aws:ResourceTag/${TagKey}                                            |
| GetTable            | Allows user to get the schema of the given table.                                                                                     | Read         | table           |                                                                      |
| ListTables          | Allows user to list all available tables.                                                                                             | Read         |                 |                                                                      |
| TagResource         | Allows user to tag an existing Export.                                                                                                | Write        | export          | aws:ResourceTag/${TagKey}<br>aws:RequestTag/${TagKey}<br>aws:TagKeys |
| UntagResource       | Allows user to untag an existing Export.                                                                                              | Write        | export          | aws:ResourceTag/${TagKey}<br>aws:TagKeys                             |
| ListTagsForResource | Allows user to list tags associated with an existing Export.                                                                          | Read         | export          | aws:ResourceTag/${TagKey}                                            |

For more information about how to use these context keys, see [Controlling access to AWS
resources using tags](../../../IAM/latest/UserGuide/access_tags.md "../../../IAM/latest/UserGuide/access_tags.md") in the _IAM User Guide_.

The following table describes the resource types that are available in Data Exports.

| Resource type | Description                                                                                                                                                                  | ARN                                                                                |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| export        | An export is the resource created by the CreateExport API. An export generates a<br>billing and cost management query output on a recurring basis.                           | arn:${Partition}:bcm-data-exports:${Region}:${Account}:export/${exportName}-{UUID} |
| table         | A table is data in a row-column format that a user queries with an export. Tables<br>are created and managed by AWS for customers. Tables cannot be deleted by<br>customers. | arn:${Partition}:bcm-data-exports:${Region}:${Account}:table/${TableName}          |

To create exports of the COST_AND_USAGE_REPORT or COST_AND_USAGE_DASHBOARD table resources
in Data Exports, IAM users must also have permissions for the respective `cur` action in
IAM. This means that if an IAM user is blocked from using `cur` actions for any
reason, such as lacking an explicit allow on `cur` or a service control policy
(SCP) providing an explicit deny on `cur`, that IAM user will be blocked from
creating or updating exports of these two tables.

The following table shows which `cur` action is required for which
`bcm-data-exports` actions in Data Exports for these two tables.

| Data Exports action           | Table resources                                   | Additional required actions in IAM |
| ----------------------------- | ------------------------------------------------- | ---------------------------------- |
| bcm-data-exports:CreateExport | COST_AND_USAGE_REPORT<br>COST_AND_USAGE_DASHBOARD | cur:PutReportDefinition            |

## Sample policy

Allow IAM user to have full access to CUR 2.0 exports in Data Exports.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ViewDataExportsTablesAndExports",
 "Effect": "Allow",
 "Action": [
 "bcm-data-exports:ListTables",
 "bcm-data-exports:ListExports",
 "bcm-data-exports:GetExport"
 ],
 "Resource": "*"
 },
 {
 "Sid": "CreateCurExports",
 "Effect": "Allow",
 "Action": "bcm-data-exports:*",
 "Resource": [
 "arn:aws:bcm-data-exports:*:*:table/COST_AND_USAGE_REPORT",
 "arn:aws:bcm-data-exports:*:*:export/*"
 ]
 },
 {
 "Sid": "CurDataAccess",
 "Effect": "Allow",
 "Action": "cur:PutReportDefinition",
 "Resource": "*"
 }
 ]
}`

```

For more information on access control and IAM permissions to use Data Exports in Billing and
Cost Management, see [Overview of managing access permissions](../../../awsaccountbilling/latest/aboutv2/control-access-billing.md "../../../awsaccountbilling/latest/aboutv2/control-access-billing.md").

### Create a pro forma AWS CUR 2.0

To create a pro forma CUR 2.0, you will need to include the following IAM policy:

Allow IAM user to have full access to CUR 2.0 and Billing Group Billing View.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowCreateCur20AnyBillingView",
 "Effect": "Allow",
 "Action": "bcm-data-exports:CreateExport",
 "Resource": [
 "arn:aws:bcm-data-exports:*:*:table/COST_AND_USAGE_REPORT",
 "arn:aws:bcm-data-exports:*:*:export/*",
 "arn:aws:billing::*:billingview/*"
 ]
 },{
 "Sid": "CurDataAccess",
 "Effect": "Allow",
 "Action": "cur:PutReportDefinition",
 "Resource": "*"
 }
 ]
}`

```

If you want an IAM role to have access to a specific billing group, you can add the Billing View ARN the role is allowed to access.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowCreateSpecificBillingViewCur20",
 "Effect": "Allow",
 "Action": "bcm-data-exports:CreateExport",
 "Resource": [
 "arn:aws:bcm-data-exports:*:*:table/COST_AND_USAGE_REPORT",
 "arn:aws:bcm-data-exports:*:*:export/*",
 "arn:aws:billing::444455556666:billingview/billing-group-111122223333"
 ]
 },{
 "Sid": "CurDataAccess",
 "Effect": "Allow",
 "Action": "cur:PutReportDefinition",
 "Resource": "*"
 }
 ]
}`

```
