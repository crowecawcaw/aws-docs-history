Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Accessing Amazon Redshift Serverless

database objects with database-role permissions

This procedure shows how to grant permission to query a table through an [Amazon Redshift database role](../dg/t_Roles.md "../dg/t_Roles.md"). The role is assigned by
means of a tag that's attached to a user in IAM and passed to Amazon Redshift when they sign in.
It's an explanation by example of the concepts in [Defining database
roles to grant to federated users in Amazon Redshift Serverless](redshift-iam-access-federated-db-roles.md "redshift-iam-access-federated-db-roles.md"). The benefit of
completing these steps is that you can associate a user with a database role and avoid
setting their permissions for each database object. It simplifies managing the user's
ability to query, modify, or add data to tables and to perform other actions.

The procedure assumes you have already set up an Amazon Redshift Serverless database and you
have the ability to grant permissions in the database. It also assumes you have
permissions to create an IAM user in the AWS console, to create an IAM role, and
to assign policy permissions.

1. Create an IAM user, using the IAM console. Later, you will connect to the
   database with this user.
2. Create a Redshift database role, using query editor v2 or another SQL client. For more
   information on creating database roles, see [CREATE ROLE](../dg/r_CREATE_ROLE.md "../dg/r_CREATE_ROLE.md").

```
CREATE ROLE urban_planning;
```

Query the [SVV_ROLES](../dg/r_SVV_ROLES.md "../dg/r_SVV_ROLES.md") system
view to check that your role is created. It also returns system roles.

```
SELECT * from SVV_ROLES;
```

3. Grant the database role you created permission to select from a table. (The
   IAM user you created will eventually sign in and select records from the table
   by means of the database role.) The role name and table name in the following
   code example are samples. Here, permission is granted to select from a table
   named `cities`.

```
GRANT SELECT on TABLE cities to ROLE urban_planning;
```

4. Use the AWS Identity and Access Management console to create an IAM role. This role grants permission
   to use query editor v2. Create a new IAM role and, for the trusted entity type, choose
   **AWS account**. Then choose **This
   account**. Give the role the following policy
   permissions:
   - `AmazonRedshiftReadOnlyAccess`
   - `tag:GetResources`
   - `tag:GetTagKeys`
   - All actions for sqlworkbench, including
     `sqlworkbench:ListDatabases` and
     `sqlworkbench:UpdateConnection`.

5. In the IAM console, add a tag with the **Key**
   `RedshiftDbRoles` to the IAM user you created previously. The tag's
   value should match the database role you created in the first step. It's
   `urban_planning` in the sample.
   After you complete these steps, assign the IAM role to the user you created in the
   IAM console. When the user signs in to the database with query editor v2, their database role
   name in the tag is passed to Amazon Redshift and associated with them. Thus, they can query the
   appropriate tables by means of the database role. To illustrate, the user in this sample
   can query the `cities` table through the `urban_planning` database
   role.
