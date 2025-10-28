# Sharing a Lake Formation resource using hybrid access mode

Allow new Data Catalog users in an external account to access Data Catalog databases and tables
using IAM based policies without interrupting the existing Lake Formation cross-account sharing
permissions.

Scenario description - The producer account has Lake Formation managed database and tables that
are shared with an external (consumer) account at account-level or IAM principal-level.
The data location of the database is registered with Lake Formation. The
`IAMAllowedPrincipals` group does not have `Super` permissions on
the database and its tables.

###### Granting cross-account access to new Data Catalog users via IAM based policies

without interrupting existing Lake Formation permissions

1.  ###### Producer account set up
    1. Sign in to the Lake Formation console using a role that `lakeformation:PutDataLakeSettings`.
    2. Under **Data Catalog settings**,
       choose `Version 4` for the **Cross account version
       settings**.

    If you're currently using version 1 or 2, see [Updating cross-account data sharing version settings](optimize-ram.md "optimize-ram.md") instructions on updating to version 3.

    There are no permission policy changes required to upgrade from version 3 to 4. 3. List the permissions you’ve granted to principals on databases and tables. For more information, see [Viewing database and table permissions in Lake Formation](viewing-permissions.md "viewing-permissions.md"). 4. Regrant existing Lake Formation cross- account permissions by opting in principals
    and resources.

    ###### Note

    Before updating a data location registration to hybrid access mode to grant cross-account
    permissions, you need to regrant at least one cross-account data share per
    account. This step is necessary to update the AWS RAM managed permissions attached
    to the AWS RAM resource share.

    In July 2023, Lake Formation has updated the AWS RAM managed permissions used for
    sharing databases and tables:

        * `arn:aws:ram::aws:permission/AWSRAMLFEnabledGlueAllTablesReadWriteForDatabase`
         (database-level share policy)
        * `arn:aws:ram::aws:permission/AWSRAMLFEnabledGlueTableReadWrite`
         (table-level share policy)The cross-account permission grants made before July 2023 don't have these

    updated AWS RAM permissions.

    If you've granted cross-account permissions directly to principals, you
    need to individually regrant those permissions to the principals. If you skip this
    step, the principals accessing the shared resource might get an illegal
    combination error. 5. Go to [https://console.aws.amazon.com/ram/home](https://console.aws.amazon.com/ram/home "https://console.aws.amazon.com/ram/home"). 6. The **Shared by me** tab in the AWS RAM console displays the
    database and table names that you've shared with an external account or
    principal.

    Ensure that the permissions attached to the shared resource has the
    correct ARN. 7. Verify the resources in the AWS RAM share are in `Associated` status.
    If the status shows as `Associating`, wait until they go into
    `Associated` state. If the status becomes `Failed`, stop and
    contact Lake Formation service team. 8. Choose **Hybrid access mode** under **Permissions** from the left navigation bar, and choose **Add**. 9. The **Add principals and resources** page shows the databases, and/or tables and the principals that have access. You can make the required updates by adding or removing principals and resources. 10. Choose the principals with Lake Formation permissions for the database and tables that
    you want to change to hybrid access mode. Choose the databases and tables. 11. Choose **Add** to opt in the principals to enforce Lake Formation permissions in hybrid access mode. 12. Grant `Super` permission to the virtual group
    `IAMAllowedPrincipals` on your database and selected
    tables. 13. Edit the Amazon S3 location Lake Formation registration to hybrid access mode. 14. Grant permissions for the AWS Glue users in the external (consumer) account
    using IAM permission policies for Amazon S3 AWS Glue actions.

2.  ######

    Consumer account set up
    1. Sign in to the Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/") as a data lake administrator.
    2. Go to [https://console.aws.amazon.com/ram/home](https://console.aws.amazon.com/ram/home "https://console.aws.amazon.com/ram/home") and accept the resource share invitation. The **Resources
       shared with me** tab in the AWS RAM page displays the database and table names that
       are shared with your account.

    For the AWS RAM share, ensure that the attached permission has the correct ARN of the shared AWS RAM invite.
    Check if the resources in the AWS RAM share are in `Associated` status. If the status shows as `Associating`, wait until they go into `Associated` state. If the status becomes `Failed`,
    stop and contact Lake Formation service team. 3. Create a resource link to the shared database and/or table in Lake Formation. 4. Grant `Describe` permission on resource link and `Grant on target` permission (on the
    original shared resource) to the IAM principals in your (consumer) account. 5. Next, set up Lake Formation permissions for principals in your account on the shared database or table.

    On the left navigation bar, under **Permissions**, choose
    **Hybrid access mode**. 6. Choose **Add** in the lower section of the
    **Hybrid access mode** page to opt in the principals and the
    database or table shared with you from the producer account. 7. Grant permissions for the AWS Glue users in your account using IAM permission policies for Amazon S3 AWS Glue actions. 8. Test users' Lake Formation permissions and AWS Glue permissions by running separate sample queries on the table using Athena

    (Optional) Clean up IAM permission policies for Amazon S3 for the principals that are in the hybrid access mode.
