# Sharing an AWS Glue resource using hybrid

access mode

Share data with another AWS account or a principal in another AWS account enforcing
Lake Formation permissions without interrupting existing Data Catalog users' IAM based access.

Scenario description - The producer account has a Data Catalog database that has access
controlled using IAM principal policies for Amazon S3 and AWS Glue actions. The data location of
the database is not registered with Lake Formation. The `IAMAllowedPrincipals` group, by
default, has `Super` permissions on the database and all its tables.

###### Granting cross-account Lake Formation permissions in hybrid access mode

1. ###### Producer account set up
   1. Sign in to the Lake Formation console using a role that has `lakeformation:PutDataLakeSettings` IAM permission.
   2. Go to **Data Catalog settings**, and
      choose `Version 4` for the **Cross account version
      settings**.

   If you're currently using version 1 or 2, see [Updating cross-account data sharing version settings](optimize-ram.md "optimize-ram.md") instructions on updating to version 3.

   There are no permission policy changes required when upgrading from version 3 to 4. 3. Register the Amazon S3 location of the database or table that you're planning to share in hybrid access mode. 4. Verify that `Super` permission to the `IAMAllowedPrincipals`
   group exists on the databases and tables of which you registered the data location
   in hybrid access mode in the above step. 5. Grant Lake Formation permissions to AWS organizations, organizational units (OUs), or directly with an IAM principal in another account. 6. If you're granting permissions directly to an IAM principal, opt in the
   principal from the consumer account to enforce Lake Formation permissions in hybrid access
   mode by enabling the option **Make Lake Formation permissions effective
   immediately**.

   If you're granting cross-account permissions to another AWS account, when you
   opt in the account, Lake Formation permissions are enforced only for the admins of that
   account. The recipient account data lake administrator need to cascade down the
   permissions and opt in the principals in the account to enforce Lake Formation permissions for
   the shared resources that are in hybrid access mode.

   If you choose **Resources matched by LF-Tags** option to grant cross-account permissions, you need to first complete granting permissions step.
   You can opt in principals and resources to hybrid access mode as a separate step by choosing **Hybrid access mode** under Permissions on the left-navigation bar of the Lake Formation console.
   Then choose **Add** to add the resources and principals that you want to enforce Lake Formation permissions.

2. ###### Consumer account set up
   1. Sign in to the Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/") as a data lake administrator.
   2. Go to [https://console.aws.amazon.com/ram/home](https://console.aws.amazon.com/ram/home "https://console.aws.amazon.com/ram/home"), and accept the resource share invitation. The
      **Shared with me** tab in the AWS RAM console displays the database
      and tables that are shared with your account.
   3. Create a resource link to the shared database and/or table in Lake Formation.
   4. Grant `Describe` permission on resource link and `Grant on target` permission (on the
      original shared resource) to the IAM principals in your (consumer) account.
   5. Grant Lake Formation permissions on the database or table shared with you to the
      principals in your account. Opt in the principals and resources to enforce Lake Formation
      permissions in hybrid access mode by enabling the option **Make Lake
      Formation permissions effective immediately**.
   6. Test the principal's Lake Formation permissions by running sample Athena queries. Test the existing access
      of your AWS Glue users with IAM principal policies for Amazon S3 and AWS Glue actions.

   (Optional) Remove the Amazon S3 bucket policy for data access and IAM principal policies for AWS Glue
   and Amazon S3 data access for the principals that you configured to use Lake Formation
   permissions.
