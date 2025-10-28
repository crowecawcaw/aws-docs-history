# Prerequisites

Before your AWS account can share Data Catalog resources (catalogs, databases and tables)
with another account or principals in another account, and before you can access the resources
shared with your account, the following prerequisites must be met.

###### General cross-account data sharing requirements

- To share Data Catalog databases and tables in hybrid access mode and share objects in the federated catalogs, you need to update the **Cross account version settings** to **Version 4**.
- Before granting cross-account permissions on a Data Catalog resource, you must revoke all
  Lake Formation permissions from the `IAMAllowedPrincipals` group for the resource. If
  the calling principal has cross account permissions to access a resource and the
  `IAMAllowedPrincipals` permission exists on the resource, then Lake Formation throws
  `AccessDeniedException`.

This requirement is applicable only when you register the underlying data location in
Lake Formation mode. If you register the data location in hybrid mode, the
`IAMAllowedPrincipals` group permissions can exist on the shared database or
table.

- For databases that contain tables that you intend to share, you must prevent new
  tables from having a default grant of `Super` to
  `IAMAllowedPrincipals`. On the Lake Formation console, edit the database and turn off
  **Use only IAM access control for new tables in this database** or
  enter the following AWS CLI command, replacing `database` with the name of the
  database. If the underlying data location is registered in hybrid access mode, you don't
  need to change this default setting. In hybrid access mode, Lake Formation allows you to selectively
  enforce Lake Formation permissions and IAM permissions policies for Amazon S3 and AWS Glue on the same
  resource.

```

aws glue update-database --name `database` --database-input '{"Name":"`database`","CreateTableDefaultPermissions":[]}'

```

- To grant cross-account
  permissions, the grantor must have the required AWS Identity and Access Management (IAM) permissions on
  AWS Glue and AWS RAM service. The AWS managed policy
  `AWSLakeFormationCrossAccountManager` grants the required
  permissions.

Data lake administrators in accounts that receive resource shares using AWS RAM must have
the following additional policy. It allows the administrator to accept AWS RAM resource
share invitations. It also allows the administrator to enable resource sharing with
organizations.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ram:AcceptResourceShareInvitation",
 "ram:RejectResourceShareInvitation",
 "ec2:DescribeAvailabilityZones",
 "ram:EnableSharingWithAwsOrganization"
 ],
 "Resource": "*"
 }
 ]
}`

```

- If you want to share Data Catalog resources with AWS Organizations or organizational units,
  sharing with organizations must be enabled in AWS RAM.

For information on how to enable sharing with organizations, see [Enable sharing with AWS organizations](../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-orgs "../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-orgs") in the
_AWS RAM User Guide_.

You must have the `ram:EnableSharingWithAwsOrganization` permission to
enable sharing with organizations.

- To share resources directly with an IAM principal in another account, you need to
  update the **Cross account version settings** to **Version
  3**. This setting is available on the **Data catalog
  settings** page. If you are using **Version 1**, see
  instructions to update the setting [Updating cross-account data sharing version settings](optimize-ram.md "optimize-ram.md").
- You cannot share Data Catalog resources encrypted with AWS Glue service managed key with
  another account. You can share only Data Catalog resources encrypted with customer's
  encryption key, and the account receiving the resource share must have permissions on
  the Data Catalog encryption key to decrypt the objects.

###### Cross-account data sharing using LF-TBAC requirements

- To share Data Catalog resources with AWS Organizations and organizational units
  (OUs), you need to update the **Cross account version settings** to
  **Version 3**or above.
- To share Data Catalog resources with version 3 of the **Cross account version
  settings**, the grantor requires to have the IAM permissions defined in the
  AWS managed policy `AWSLakeFormationCrossAccountManager` in your
  account.
- If you are using version 1 or version 2 of the **Cross account version
  settings**, you must have a Data Catalog resource policy
  (`glue:PutResourcePolicy`) that enables LF-TBAC. For more
  information, see [Managing cross-account permissions using both
  AWS Glue and Lake Formation](hybrid-cross-account.md "hybrid-cross-account.md").
- If you're currently using an AWS Glue Data Catalog resource policy to share
  resources, and you want to grant cross-account permissions using version 3 of the
  **Cross account version settings**, you must add the
  `glue:ShareResource` permission in the Data Catalog Settings using the
  `glue:PutResourcePolicy` API operation as shown in the [Managing cross-account permissions using both
  AWS Glue and Lake Formation](hybrid-cross-account.md "hybrid-cross-account.md") section. This
  policy is not required if your account has made no cross-account grants using the
  AWS Glue Data Catalog resource policy (version 1 and version 2 use
  `glue:PutResourcePolicy` permission) to grant cross-account access.

```
{
      "Effect": "Allow",
      "Action": [
        "glue:ShareResource"
      ],
      "Principal": {"Service": [
        "ram.amazonaws.com"
      ]},
      "Resource": [
        "arn:aws:glue:<region>:<account-id>:table/*/*",
        "arn:aws:glue:<region>:<account-id>:database/*",
        "arn:aws:glue:<region>:<account-id>:catalog"
      ]
    }

```

- If your account has made cross-account shares using AWS Glue Data Catalog
  resource policy, and you are currently using named resource method or LF-TBAC with
  **Cross account settings** version 3 to share resources, which uses
  AWS RAM to share resources, you must set the `EnableHybrid` argument to
  `'true'` when you invoke the `glue:PutResourcePolicy` API
  operation. For more information, see [Managing cross-account permissions using both
  AWS Glue and Lake Formation](hybrid-cross-account.md "hybrid-cross-account.md").

###### Setup required in each account that accesses the shared resource

- If you are sharing resources with AWS accounts, at least one user in the consumer account must be a data lake administrator to
  view shared resources. For information on how to create a data lake administrator, see
  [Create a data lake administrator](initial-lf-config.md#create-data-lake-admin "initial-lf-config.md#create-data-lake-admin").

The data lake administrator can grant Lake Formation permissions on the shared resources to other principals in the account. Other principals can't access shared resources until the data lake administrator grants them permissions on the resources.

- Integrated services such as Athena and Redshift Spectrum require resource links to be able to include shared resources in queries. Principals need to create a resource link in their Data Catalog to a shared resource from another AWS account. For more information about resource links, see [How resource links work in Lake Formation](resource-links-about.md "resource-links-about.md").
- When a resource is shared directly with an IAM principal, to query the table using
  Athena, the principal needs to create a resource link. To create a resource link, the principal needs the Lake Formation `CREATE_TABLE` or `CREATE_DATABASE` permission, and the
  `glue:CreateTable` or `glue:CreateDatabase` IAM permission.

If the producer account shares a different table under the same database with the same or another principal, that principal can immediately query the table.

###### Note

For the data lake administrator and for principals whom the data lake administrator has granted permissions to, shared resources appear in the Data Catalog as if they are local (owned) resources.
Extract, transform, and load (ETL) jobs can access the underlying data of shared resources.

For shared resources, the **Tables** and **Databases** pages on the Lake Formation console display the owner's account ID.

When the underlying data of a shared resource is accessed, CloudTrail log events are generated in both the shared resource recipient's account and the resource owner's account.
The CloudTrail events can contain the ARN of the principal that accessed the data, but only if the recipient account opts in to include the principal ARN in the logs. For more information, see [Cross-account CloudTrail logging](cross-account-logging.md "cross-account-logging.md").
