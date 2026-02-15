# Upgrading AWS Glue data permissions to

the AWS Lake Formation model

AWS Lake Formation permissions enable fine-grained access control for data in your data lake. You can
use the Lake Formation permissions model to manage your existing AWS Glue Data Catalog objects and data locations in
Amazon Simple Storage Service (Amazon S3).

The Lake Formation permissions model uses coarse-grained AWS Identity and Access Management (IAM) permissions for API
service access. Lake Formation uses [Data filtering and cell-level security in Lake Formation](data-filtering.md "data-filtering.md")
functionality to restrict table access at the column, row, and cell-level for users and their
applications. By comparison, the AWS Glue model grants data access via [Identity based and resource based IAM policies](../../../glue/latest/dg/security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies "../../../glue/latest/dg/security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies").

To make the switch, follow the steps in this guide.

For more information, see [Overview of Lake Formation permissions](lf-permissions-overview.md "lf-permissions-overview.md") .

## About default permissions

To maintain backward compatibility with AWS Glue, by default, AWS Lake Formation grants the
`Super` permission to the `IAMAllowedPrincipals` group on all existing
AWS Glue Data Catalog resources, and grants the `Super` permission on new Data Catalog resources
if the **Use only IAM access control** settings are enabled. This effectively
causes access to Data Catalog resources and Amazon S3 locations to be controlled solely by AWS Identity and Access Management
(IAM) policies. The `IAMAllowedPrincipals` group includes any IAM users and
roles that are allowed access to your Data Catalog objects by your IAM policies. The
`Super` permission enables a principal to perform every supported Lake Formation operation
on the database or table on which it is granted.

You can start using Lake Formation to manage access to your data by registering the locations of
existing Data Catalog resources in Lake Formation or by using hybrid access mode. When you register Amazon S3 location in hybrid
access mode, you can enable Lake Formation permissions by opting in principals for
databases and tables under that location.

To ease the transition of data lake permissions from an IAM and Amazon S3 model to Lake Formation
permissions, we recommend you to use hybrid access mode for Data Catalog. With the hybrid access
mode, you have an incremental path where you can enable Lake Formation permissions for a specific set of
users without interrupting other existing users or workloads.

For more information, see [Hybrid access mode](hybrid-access-mode.md "hybrid-access-mode.md").

Disable the default Data Catalog settings to move all existing users of a table to Lake Formation in a single step.

To start using Lake Formation permissions with your existing AWS Glue Data Catalog databases
and tables, you must do the following:

1. Determine your users’ existing IAM permissions for each database and table.
2. Replicate these permissions in Lake Formation.
3. For each Amazon S3 location that contains data:
   1. Revoke the `Super` permission from the
      `IAMAllowedPrincipals` group on each Data Catalog resource that references
      that location.
   2. Register the location with Lake Formation.

4. Clean up existing fine-grained access control IAM policies.

###### Important

To add new users while in the process of transitioning your Data Catalog, you must set up
granular AWS Glue permissions in IAM as before. You also must replicate those permissions in
Lake Formation as described in this section. If new users have the coarse-grained IAM policies that
are described in this guide, they can list any databases or tables that have the
`Super` permission granted to `IAMAllowedPrincipals`. They can also
view the metadata for those resources.

Follow the steps in this section to upgrade to the Lake Formation permissions model.

###### Topics

- [Step 1: List users' and roles' existing
  permissions](#upgrade-glue-lake-formation-step1 "#upgrade-glue-lake-formation-step1")
- [Step 2: Set up equivalent Lake Formation
  permissions](#upgrade-glue-lake-formation-step2 "#upgrade-glue-lake-formation-step2")
- [Step 3: Give users IAM permissions to
  use Lake Formation](#upgrade-glue-lake-formation-step3 "#upgrade-glue-lake-formation-step3")
- [Step 4: Switch your data stores to the
  Lake Formation permissions model](#upgrade-glue-lake-formation-step4 "#upgrade-glue-lake-formation-step4")
- [Step 5: Secure new Data Catalog
  resources](#upgrade-glue-lake-formation-step5 "#upgrade-glue-lake-formation-step5")
- [Step 6: Give users a new IAM policy for
  future data lake access](#upgrade-glue-lake-formation-step6 "#upgrade-glue-lake-formation-step6")
- [Step 7: Clean up existing IAM
  policies](#upgrade-glue-lake-formation-step7 "#upgrade-glue-lake-formation-step7")

## Step 1: List users' and roles' existing

permissions

To start using AWS Lake Formation permissions with your existing AWS Glue databases and tables, you
must first determine your users’ existing permissions.

###### Important

Before you begin, ensure that you have completed the tasks in [Getting started with Lake Formation](getting-started-setup.md "getting-started-setup.md").

###### Topics

- [Using the API operation](#upgrade-glue-lake-formation-step1-api "#upgrade-glue-lake-formation-step1-api")
- [Using the AWS Management Console](#upgrade-glue-lake-formation-step1-console "#upgrade-glue-lake-formation-step1-console")
- [Using AWS CloudTrail](#upgrade-glue-lake-formation-step1-ct "#upgrade-glue-lake-formation-step1-ct")

### Using the API operation

Use the AWS Identity and Access Management (IAM) [ListPoliciesGrantingServiceAccess](../../../IAM/latest/APIReference/API_ListPoliciesGrantingServiceAccess.md "../../../IAM/latest/APIReference/API_ListPoliciesGrantingServiceAccess.md") API operation to determine the IAM policies
attached to each principal (user or role). From the policies returned in the results, you
can determine the IAM permissions that are granted to the principal. You must invoke the
API for each principal separately.

###### Example

The following AWS CLI example returns the policies attached to user
`glue_user1`.

```
aws iam list-policies-granting-service-access --arn arn:aws:iam::111122223333:user/glue_user1 --service-namespaces glue
```

The command returns results similar to the following.

```
{
    "PoliciesGrantingServiceAccess": [
        {
            "ServiceNamespace": "glue",
            "Policies": [
                {
                    "PolicyType": "INLINE",
                    "PolicyName": "GlueUserBasic",
                    "EntityName": "glue_user1",
                    "EntityType": "USER"
                },
                {
                    "PolicyType": "MANAGED",
                    "PolicyArn": "arn:aws:iam::aws:policy/AmazonAthenaFullAccess",
                    "PolicyName": "AmazonAthenaFullAccess"
                }
            ]
        }
    ],
    "IsTruncated": false
}

```

### Using the AWS Management Console

You can also see this information on the AWS Identity and Access Management (IAM) console, in the
**Access Advisor** tab on the user or role **Summary**
page:

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Users** or
   **Roles**.
3. Choose a name in the list to open its **Summary** page, and choose
   the **Access Advisor** tab.
4. Inspect each of the policies to determine the combination of databases, tables, and
   actions that each user has permissions for.

Remember to inspect roles in addition to users during this process because your data
processing jobs might be assuming roles to access data.

### Using AWS CloudTrail

Another way to determine your existing permissions is to look in AWS CloudTrail for AWS Glue API
calls where the `additionaleventdata` field of the logs contains an
`insufficientLakeFormationPermissions` entry. This entry lists the database and
table that the user needs Lake Formation permissions on to take the same action.

These are data access logs, so they are not guaranteed to produce a comprehensive list
of users and their permissions. We recommend choosing a wide time range to capture most of
your users’ data access patterns, for example, several weeks or months.

For more information, see [Viewing
Events with CloudTrail Event History](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md") in the
_AWS CloudTrail User Guide_.

Next, you can set up Lake Formation permissions to match the AWS Glue permissions. See [Step 2: Set up equivalent Lake Formation
permissions](#upgrade-glue-lake-formation-step2 "#upgrade-glue-lake-formation-step2").

## Step 2: Set up equivalent Lake Formation

permissions

Using the information collected in [Step 1: List users' and roles' existing
permissions](#upgrade-glue-lake-formation-step1 "#upgrade-glue-lake-formation-step1"), grant AWS Lake Formation permissions to match the
AWS Glue permissions. Use any of the following methods to performs the grants:

- Use the Lake Formation console or the AWS CLI.

See [Granting permissions on Data Catalog resources](granting-catalog-permissions.md "granting-catalog-permissions.md").

- Use the `GrantPermissions` or `BatchGrantPermissions` API
  operations.

See [Permissions APIs](aws-lake-formation-api-aws-lake-formation-api-permissions.md "aws-lake-formation-api-aws-lake-formation-api-permissions.md").

For more information, see [Overview of Lake Formation permissions](lf-permissions-overview.md "lf-permissions-overview.md") .

After setting up Lake Formation permissions, proceed to [Step 3: Give users IAM permissions to
use Lake Formation](#upgrade-glue-lake-formation-step3 "#upgrade-glue-lake-formation-step3").

## Step 3: Give users IAM permissions to

use Lake Formation

To use the AWS Lake Formation permissions model, principals must have AWS Identity and Access Management (IAM) permissions on
the Lake Formation APIs.

Create
the following policy in IAM and attach it to every user who needs access to your data lake. Name the
policy `LakeFormationDataAccess`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "LakeFormationDataAccess",
 "Effect": "Allow",
 "Action": [
 "lakeformation:GetDataAccess"
 ],
 "Resource": "*"
 }
 ]
}`

```

Next, upgrade to Lake Formation permissions one data location at a time. See [Step 4: Switch your data stores to the
Lake Formation permissions model](#upgrade-glue-lake-formation-step4 "#upgrade-glue-lake-formation-step4").

## Step 4: Switch your data stores to the

Lake Formation permissions model

Upgrade to Lake Formation permissions one data location at a time. To do that, repeat this entire
section until you have registered all Amazon Simple Storage Service (Amazon S3) paths that are referenced by your
Data Catalog.

###### Topics

- [Verify Lake Formation permissions](#identify-catalog-resources "#identify-catalog-resources")
- [Secure existing Data Catalog resources](#upgrade-secure-resources "#upgrade-secure-resources")
- [Turn on Lake Formation permissions
  for your Amazon S3 location](#upgrade-glue-lake-formation-turn-on-permissions "#upgrade-glue-lake-formation-turn-on-permissions")

### Verify Lake Formation permissions

Before registering a location, perform a verification step to ensure that the correct
principals have the required Lake Formation permissions, and that no Lake Formation permissions are granted to
principals that should not have them. Using the Lake Formation
`GetEffectivePermissionsForPath` API operation, identify the Data Catalog resources
that reference the Amazon S3 location, along with the principals that have permissions on those
resources.

The following AWS CLI example returns the Data Catalog databases and tables that reference the
Amazon S3 bucket `products`.

```
aws lakeformation get-effective-permissions-for-path --resource-arn arn:aws:s3:::products --profile datalake_admin
```

Note the `profile` option. We recommend that you run the command as a data
lake administrator.

The following is an excerpt from the returned results.

```
{
        "PermissionsWithGrantOption": [
            "SELECT"
        ],
        "Resource": {
            "TableWithColumns": {
                "Name": "inventory_product",
                "ColumnWildcard": {},
                "DatabaseName": "inventory"
            }
        },
        "Permissions": [
            "SELECT"
        ],
        "Principal": {
            "DataLakePrincipalIdentifier": "arn:aws:iam::111122223333:user/datalake_user1",
            "DataLakePrincipalType": "IAM_USER"
        }
 },...

```

###### Important

If your AWS Glue Data Catalog is encrypted, `GetEffectivePermissionsForPath`
returns only databases and tables that were created or modified after Lake Formation general
availability.

### Secure existing Data Catalog resources

Next, revoke the `Super` permission from `IAMAllowedPrincipals` on
each table and database that you identified for the location.

###### Warning

If you have automation in place that creates databases and tables in the Data Catalog, the
following steps might cause the automation and downstream extract, transform, and load
(ETL) jobs to fail. Proceed only after you have either modified your existing processes or
granted explicit Lake Formation permissions to the required principals. For information about Lake Formation
permissions, see [Lake Formation permissions reference](lf-permissions-reference.md "lf-permissions-reference.md").

###### To revoke `Super` from `IAMAllowedPrincipals` on a

table

1. Open the AWS Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/"). Sign in as a data lake
   administrator.
2. In the navigation pane, choose **Tables**.
3. On the **Tables** page, select the radio button next to the desired
   table.
4. On the **Actions** menu, choose **Revoke**.
5. In the **Revoke permissions** dialog box, in the **IAM
   users and roles** list, scroll down to the **Group**
   heading, and choose **IAMAllowedPrincipals**.
6. Under **Table permissions**, ensure that **Super**
   is selected, and then choose **Revoke**.

###### To revoke `Super` from `IAMAllowedPrincipals` on a

database

1. Open the AWS Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/"). Sign in as a data lake
   administrator.
2. In the navigation pane, choose **Databases**.
3. On the **Databases** page, select the radio button next to the
   desired database.
4. On the **Actions** menu, choose **Edit**.
5. On the **Edit database** page, clear **Use only IAM access
   control for new tables in this database**, and then choose
   **Save**.
6. Back on the **Databases** page, ensure that the database is still
   selected, and then on the **Actions** menu, choose
   **Revoke**.
7. In the **Revoke permissions** dialog box, in the **IAM
   users and roles** list, scroll down to the **Group**
   heading, and choose **IAMAllowedPrincipals**.
8. Under **Database permissions**, ensure that
   **Super** is selected, and then choose
   **Revoke**.

### Turn on Lake Formation permissions

for your Amazon S3 location

Next, register the Amazon S3 location with Lake Formation. To do this, you can use the process
described in [Adding an Amazon S3 location to your data lake](register-data-lake.md "register-data-lake.md"). Or,
use the `RegisterResource` API operation as described in [Credential vending APIs](aws-lake-formation-api-credential-vending.md "aws-lake-formation-api-credential-vending.md").

###### Note

If a parent location is registered, you don't need to register child locations.

After you finish these steps and test that your users can access their data, you have
successfully upgraded to Lake Formation permissions. Continue with the next step, [Step 5: Secure new Data Catalog
resources](#upgrade-glue-lake-formation-step5 "#upgrade-glue-lake-formation-step5").

## Step 5: Secure new Data Catalog

resources

Next, secure all new Data Catalog resources by changing the default Data Catalog settings. Turn off
the options to use only AWS Identity and Access Management (IAM) access control for new databases and tables.

###### Warning

If you have automation in place that creates databases and tables in the Data Catalog,
the following steps might cause the automation and downstream extract, transform, and load (ETL) jobs to fail. Proceed only after
you have either modified your existing processes or granted explicit Lake Formation permissions to the
required principals. For information
about Lake Formation permissions, see [Lake Formation permissions reference](lf-permissions-reference.md "lf-permissions-reference.md").

###### To change the default Data Catalog settings

1. Open the AWS Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/"). Sign in as an IAM
   administrative user (the user `Administrator` or another user with the
   `AdministratorAccess` AWS managed policy).
2. In the navigation pane, choose **Settings**.
3. On the **Data catalog settings** page, clear both check boxes, and
   then choose **Save**.

The next step is to grant users access to additional databases or tables in the future.
See [Step 6: Give users a new IAM policy for
future data lake access](#upgrade-glue-lake-formation-step6 "#upgrade-glue-lake-formation-step6").

## Step 6: Give users a new IAM policy for

future data lake access

To grant your users access to additional Data Catalog databases or tables in the future, you
must give them the coarse-grained AWS Identity and Access Management (IAM) inline policy that follows. Name the
policy `GlueFullReadAccess`.

###### Important

If you attach this policy to a user before revoking `Super` from
`IAMAllowedPrincipals` on every database and table in your Data Catalog, that user
can view all metadata for any resource on which `Super` is granted to
`IAMAllowedPrincipals`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "GlueFullReadAccess",
 "Effect": "Allow",
 "Action": [
 "lakeformation:GetDataAccess",
 "glue:GetTable",
 "glue:GetTables",
 "glue:SearchTables",
 "glue:GetDatabase",
 "glue:GetDatabases",
 "glue:GetPartitions"
 ],
 "Resource": "*"
 }
 ]
}`

```

###### Note

The inline policies designated in this step and previous steps contain minimal IAM
permissions. For suggested policies for data lake administrators, data analysts, and other
personas, see [Lake Formation personas and IAM permissions reference](permissions-reference.md "permissions-reference.md").

Next, proceed to [Step 7: Clean up existing IAM
policies](#upgrade-glue-lake-formation-step7 "#upgrade-glue-lake-formation-step7").

## Step 7: Clean up existing IAM

policies

After you set up the AWS Lake Formation permissions and you create and attach the coarse-grained
access control AWS Identity and Access Management (IAM) policies, complete the following final step:

- Remove from users, groups, and roles the old [fine-grained access control](../../../glue/latest/dg/using-identity-based-policies.md#glue-identity-based-policy-limitations.html "../../../glue/latest/dg/using-identity-based-policies.md#glue-identity-based-policy-limitations.html") IAM policies that you replicated in Lake Formation.

By doing this, you ensure that those principals no longer have direct access to the data
in Amazon Simple Storage Service (Amazon S3). You can then manage data lake access for those principals entirely through
Lake Formation.
