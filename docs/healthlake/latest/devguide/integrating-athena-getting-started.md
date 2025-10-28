# Getting started with Amazon Athena

To integrate HealthLake with Amazon Athena, you must set up permissions. To do this, you'll create an Athena user, group or role, and grant
them access to FHIR resources located within a HealthLake data store.

- [Granting a user, group, or role
  access to a HealthLake data store (AWS Lake Formation Console)](#getting-started-athena-admin "#getting-started-athena-admin")
- [Setting up an Athena
  account](#getting-started-athena-user "#getting-started-athena-user")

## Granting a user, group, or role access to

a HealthLake data store (AWS Lake Formation Console)

###### Persona: HealthLake administrator

The HealthLake administrator persona is a data lake administrator in AWS Lake Formation. They
grant access to HealthLake data stores in Lake Formation.

For each data store created, there are two entries visible in the AWS Lake Formation console.
One entry is a _resource link_. Resource link names are always
displayed in _italics_. Each resource link is displayed with the name
and owner of its linked shared resource. For all HealthLake data stores, the shared resource
owner is the HealthLake service account. The other entry is the HealthLake data store in the HealthLake
service account. The steps in this procedure use the data store that is the resource
link.

To learn more about resource links, see [How resource links work in
Lake Formation](../../../lake-formation/latest/dg/resource-links-about.md "../../../lake-formation/latest/dg/resource-links-about.md") in the _AWS Lake Formation Developer
Guide_.

For a user, group, or role to be able to query data in Athena, you must grant
**Describe** permission on the resource database. Then, you must
grant **Select** and **Describe** on the
tables.

###### STEP 1: To grant **DESCRIBE** permissions on a HealthLake data store

resource link database

1. Open the AWS Lake Formation console: [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation "https://console.aws.amazon.com/lakeformation")
2. In the primary navigation bar, choose **Databases**.
3. On the **Databases** page, choose the radio button next to
   the name of the data store that is in italics.
4. Choose **Actions (▼)**.
5. Choose **Grant**.
6. On the **Grant data permissions** page, under
   **Principals**, choose **IAM users or
   roles**.
7. Under **IAM users or roles**, use the **down arrow
   (▼)**, or search for the IAM user, role, or group that you
   want to be able to make queries on in Athena.
8. Under **LF-Tags or catalog resources** card, choose the
   **Named data catalog resources** option.
9. Under **Databases**, use the **down arrow
   (▼)** to choose the HealthLake data store database that you want
   to share access to.
10. In the **Resource link permissions** card, under
    **Resource link permissions**, choose
    **Describe**.

When the grant is successful, the **Grant permission success** banner
appears. To view the permission you just granted, choose **Data lake
permissions**. Find the user, group, and role in the table. Under the
**Permissions** column, you will see **Describe**
listed.

Now you must use **Grant on target** to grant
**Select** and **Describe** on all tables in the
database.

###### STEP 2: Grant access to all tables in a HealthLake data store resource link

1. Open the AWS Lake Formation console: [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation "https://console.aws.amazon.com/lakeformation")
2. In the primary navigation bar, choose **Databases**.
3. On the **Databases** page, choose the radio button next to
   the name of the data store that is in italics.
4. Choose **Actions (▼)**.
5. Choose **Grant on target**.
6. On the **Grant data permissions** page, under
   **Principals**, choose **IAM users or
   roles**.
7. Under **IAM users or roles**, use the **down arrow
   (▼)** or search for the IAM user, group, or role that you
   want to be able to make queries on in Athena.
8. Under **LF-Tags or catalog resources** card, choose the
   **Named data catalog resources** option.
9. Under **Databases**, use the **down arrow
   (▼)** to choose the HealthLake data store database that you want
   to grant access to.
10. Under **Tables**, choose **All tables** to
    share all tables with a HealthLake user.
11. In the **Table permissions** card, under **Table
    permissions**, choose **Describe** and
    **Select**.
12. Choose **Grant**.

After choosing grant,a **Grant permissions success** banner appears.
The specified user can now make queries on a HealthLake data store in Athena.

## Getting started with Athena

###### HealthLake user

The HealthLake user will use the Athena console, AWS CLI, or AWS SDKs to query a HealthLake
data store shared with them by the HealthLake administrator.

To query a data store using Athena, you must do the following three things.

- Grant the IAM user or role access to the HealthLake data store via Lake Formation. To learn
  more, see [Granting a user, group, or role access to
  a HealthLake data store (AWS Lake Formation Console)](#getting-started-athena-admin "#getting-started-athena-admin").
- Create a workgroup for your HealthLake data store.
- Designate an Amazon S3 bucket to store your query results.

To get started with Athena, add the **AmazonAthenaFullAccess** and **AmazonS3FullAccess** AWS managed policies to your user, group or role.
Using an AWS managed policy is great way to get started using a new service. Keep in
mind that AWS managed policies might not grant least-privilege permissions for your
specific use cases because they are available for use by all AWS customers. When you set
permissions with IAM policies, grant only the permissions required to perform a task.
To learn more about IAM and applying least-privilege, see [Apply
least-privilege permissions](../../../IAM/latest/UserGuide/best-practices.md#bp-use-aws-defined-policies "../../../IAM/latest/UserGuide/best-practices.md#bp-use-aws-defined-policies") in the
_IAM User Guide_.

###### Important

To query a HealthLake data store in Athena, you must use **Athena engine version
3**.

Workgroups are resources, and therefore you can use IAM-based policies to control
access to specific workgroups. To learn more, see [Using
workgroups to control query access and costs](../../../athena/latest/ug/manage-queries-control-costs-with-workgroups.md "../../../athena/latest/ug/manage-queries-control-costs-with-workgroups.md") in the _Athena User
Guide_.

To learn more about setting up workgroups, see [https://docs.aws.amazon.com/athena/latest/ug/workgroups-procedure.html](../../../athena/latest/ug/workgroups-procedure.md "../../../athena/latest/ug/workgroups-procedure.md") in the _Athena User
Guide_.

###### Note

The region your Amazon S3 bucket is in and the Athena console must match.

Before you can run a query, a query result bucket location in Amazon S3 must be specified,
or you must use a workgroup that has specified a bucket and whose configuration
overrides client settings. Output files are saved automatically for every query that
runs.

For more details on specifying query result locations in the Athena console, see [Specifying a query result location using the Athena console](../../../athena/latest/ug/querying.md#query-results-specify-location-console "../../../athena/latest/ug/querying.md#query-results-specify-location-console") in the
_Amazon Athena User Guide_.

To see examples of how to query your HealthLake data store in Athena, see [Querying HealthLake data with SQL](integrating-athena-query-sql.md "integrating-athena-query-sql.md").
