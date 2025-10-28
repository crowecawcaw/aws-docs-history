# Federate an event data store

Federating an event data store lets you view the metadata associated with the event data store in the AWS Glue
[Data Catalog](../../../glue/latest/dg/components-overview.md#data-catalog-intro "../../../glue/latest/dg/components-overview.md#data-catalog-intro"),
registers the Data Catalog with AWS Lake Formation, and lets you run SQL queries against your event data using Amazon Athena. The table metadata stored in the AWS Glue Data Catalog
lets the Athena query engine know how to find, read, and process the data that you want to query.

You can enable federation by using the CloudTrail console, AWS CLI, or
[EnableFederation](../APIReference/API_EnableFederation.md "../APIReference/API_EnableFederation.md") API operation. When you enable Lake query federation, CloudTrail
creates a managed database named `aws:cloudtrail` (if the database doesn't already exist) and a managed federated table in
the AWS Glue Data Catalog. The event data store ID is used for the table name. CloudTrail registers the federation role ARN and event data store in
[AWS Lake Formation](query-federation-lake-formation.md "query-federation-lake-formation.md"), the service responsible for allowing
fine-grained access control of the federated resources in the AWS Glue Data Catalog.

To enable Lake query federation, you must create a new IAM role or choose an
existing role. Lake Formation uses this role to manage permissions for the federated event
data store. When you create a new role using the CloudTrail console, CloudTrail automatically
creates the required permissions for the role. If you choose an existing role, be
sure that the role provides the [minimum permissions](#query-federation-permissions-role "#query-federation-permissions-role").

You can disable federation by using the CloudTrail console, AWS CLI, or
[DisableFederation](../APIReference/API_DisableFederation.md "../APIReference/API_DisableFederation.md") API operation. When you disable federation, CloudTrail
disables the integration with AWS Glue, AWS Lake Formation, and Amazon Athena.
After disabling Lake query federation, you can no longer query your event data in Athena.
No CloudTrail Lake data is deleted when you disable federation and you can continue to run queries in CloudTrail Lake.

There are no CloudTrail charges for federating a CloudTrail Lake event data store. There are costs for running queries in Amazon Athena.
For more information about Athena pricing, see [Amazon Athena Pricing](https://aws.amazon.com/athena/pricing/ "https://aws.amazon.com/athena/pricing/").

###### Topics

- [Considerations](#query-federation-considerations "#query-federation-considerations")
- [Required permissions for federation](#query-federation-permissions "#query-federation-permissions")
- [Enable Lake query federation](query-enable-federation.md "query-enable-federation.md")
- [Disable Lake query federation](query-disable-federation.md "query-disable-federation.md")
- [Managing CloudTrail Lake federation resources with AWS Lake Formation](query-federation-lake-formation.md "query-federation-lake-formation.md")

## Considerations

Consider the following factors when federating an event data store:

- There are no CloudTrail charges for federating a CloudTrail Lake event data store. There are costs for running queries in Amazon Athena.
  For more information about Athena pricing, see [Amazon Athena Pricing](https://aws.amazon.com/athena/pricing/ "https://aws.amazon.com/athena/pricing/").
- Lake Formation is used to manage permissions for the federated resources. If you
  delete the federation role, or revoke permissions to the resources from
  Lake Formation or AWS Glue, you can't run queries from Athena. For more information about working with Lake Formation, see
  [Managing CloudTrail Lake federation resources with AWS Lake Formation](query-federation-lake-formation.md "query-federation-lake-formation.md").
- Anyone using Amazon Athena to query data registered with Lake Formation must have an IAM permissions policy
  that allows the `lakeformation:GetDataAccess` action. The AWS managed policy: [AmazonAthenaFullAccess](../../../athena/latest/ug/managed-policies.md#amazonathenafullaccess-managed-policy "../../../athena/latest/ug/managed-policies.md#amazonathenafullaccess-managed-policy")
  allows this action. If you use inline policies, be sure to update permissions policies to allow this action. For more information, see
  [Managing Lake Formation and Athena user permissions](../../../athena/latest/ug/lf-athena-user-permissions.md "../../../athena/latest/ug/lf-athena-user-permissions.md").
- To create views on federated tables in Athena, you need a destination database other than `aws:cloudtrail`. This is because the `aws:cloudtrail` database is managed by CloudTrail.
- To create a dataset in Amazon Quick Suite, you must choose the **Use
  custom SQL** option. For more information, see [Creating
  a dataset using Amazon Athena data](../../../quicksight/latest/user/create-a-data-set-athena.md "../../../quicksight/latest/user/create-a-data-set-athena.md").
- If federation is enabled, you can't delete an event data store. To
  delete a federated event data store, you must first [disable federation](query-disable-federation.md "query-disable-federation.md") and
  [termination
  protection](query-eds-termination-protection.md "query-eds-termination-protection.md") if it's enabled.
- The following considerations apply to organization event data
  stores:
  - Only a single delegated administrator account or the
    management account can enable federation on an organization event
    data store. Other delegated administrator accounts can still query
    and share information using the [Lake Formation data sharing feature](../../../lake-formation/latest/dg/data-sharing-overivew.md "../../../lake-formation/latest/dg/data-sharing-overivew.md").
  - Any delegated administrator account or the organization's
    management account can disable federation.

## Required permissions for federation

Before federating an event data store, be sure that you have all the required
permissions for the federation role and for enabling and disabling federation.
You only need to update the federation role permissions if you choose an
existing IAM role to enable federation. If you choose to create a new IAM
role using the CloudTrail console, CloudTrail provides all necessary permissions for the
role.

###### Topics

- [IAM permissions for federating an event data store](#query-federation-permissions-role "#query-federation-permissions-role")
- [Required permissions for enabling
  federation](#query-federation-permissions-enable "#query-federation-permissions-enable")
- [Required permissions for disabling
  federation](#query-federation-permissions-disable "#query-federation-permissions-disable")

### IAM permissions for federating an event data store

When you enable federation, you have the option to create a new IAM role, or use an existing IAM role.
When you choose a new IAM role, CloudTrail creates an IAM role with the required permissions and no further action is required on your part.

If you choose an existing role, ensure the IAM role's policies provide
the required permissions to enable federation. This section provides
examples of the required IAM role permission and trust policies.

The following example provides the permissions policy for the federation role. For the first statement
provide the full ARN of your event data store for the `Resource`.

The second statement in this policy allows Lake Formation to decrypt
data for an event data store encrypted with a KMS key. Replace `key-region`, `account-id`, and `key-id` with the values for your KMS key. You can omit this statement if your
event data store does not use a KMS key for encryption.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "LakeFederationEDSDataAccess",
 "Effect": "Allow",
 "Action": "cloudtrail:GetEventDataStoreData",
 "Resource": "arn:aws:cloudtrail:`us-east-1`:`111111111111`:eventdatastore/`eds-id`"
 },
 {
 "Sid": "LakeFederationKMSDecryptAccess",
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt",
 "kms:GenerateDataKey"
 ],
 "Resource": "arn:aws:kms:`us-east-1`:`111111111111`:key/`key-id`"
 }
 ]
}`

```

The following example provides the IAM trust policy, which allows
AWS Lake Formation to assume an IAM role to manage permissions for the federated event data store.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "lakeformation.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

### Required permissions for enabling

federation

The following example policy provides the minimum required permissions to enable federation on an event data store. This policy allows CloudTrail to enable federation
on the event data store, AWS Glue to create the federated resources in the AWS Glue Data Catalog, and AWS Lake Formation to manage resource registration.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "CloudTrailEnableFederation",
 "Effect": "Allow",
 "Action": "cloudtrail:EnableFederation",
 "Resource": "arn:aws:cloudtrail:`us-east-1`:`111111111111`:eventdatastore/`eds-id`"
 },
 {
 "Sid": "FederationRoleAccess",
 "Effect": "Allow",
 "Action": [
 "iam:PassRole",
 "iam:GetRole"
 ],
 "Resource": "arn:aws:iam::`111122223333`:role/`federation-role-name`"
 },
 {
 "Sid": "GlueResourceCreation",
 "Effect": "Allow",
 "Action": [
 "glue:CreateDatabase",
 "glue:CreateTable",
 "glue:PassConnection"
 ],
 "Resource": [
 "arn:aws:glue:`us-east-1`:`111111111111`:catalog",
 "arn:aws:glue:`us-east-1`:`111111111111`:database/aws:cloudtrail",
 "arn:aws:glue:`us-east-1`:`111111111111`:table/aws:cloudtrail/`eds-id`",
 "arn:aws:glue:`us-east-1`:`111111111111`:connection/aws:cloudtrail"
 ]
 },
 {
 "Sid": "LakeFormationRegistration",
 "Effect": "Allow",
 "Action": [
 "lakeformation:RegisterResource",
 "lakeformation:DeregisterResource"
 ],
 "Resource": "arn:aws:lakeformation:`region`:`111111111111`:catalog:`111111111111`"
 }
 ]
}`

```

### Required permissions for disabling

federation

The following example policy provides the minimum required resources to disable federation on an event data store. This policy
allows CloudTrail to disable federation on the event data store, AWS Glue to delete the managed federated table in the AWS Glue Data Catalog, and Lake Formation to deregister the
federated resource.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "CloudTrailDisableFederation",
 "Effect": "Allow",
 "Action": "cloudtrail:DisableFederation",
 "Resource": "arn:aws:cloudtrail:`us-east-1`:`111111111111`:eventdatastore/`eds-id`"
 },
 {
 "Sid": "GlueTableDeletion",
 "Effect": "Allow",
 "Action": "glue:DeleteTable",
 "Resource": [
 "arn:aws:glue:`us-east-1`:`111111111111`:catalog",
 "arn:aws:glue:`us-east-1`:`111111111111`:database/aws:cloudtrail",
 "arn:aws:glue:`us-east-1`:`111111111111`:table/aws:cloudtrail/`eds-id`"
 ]
 },
 {
 "Sid": "LakeFormationDeregistration",
 "Effect": "Allow",
 "Action": "lakeformation:DeregisterResource",
 "Resource": "arn:aws:lakeformation:`us-east-1`:`111111111111`:catalog:`111111111111`"
 }
 ]
}`

```
