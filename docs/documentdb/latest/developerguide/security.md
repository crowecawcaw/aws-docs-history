# Managing Amazon DocumentDB users

In Amazon DocumentDB, users authenticate to a cluster in conjunction with a password.
Each cluster has primary sign-in credentials that are established during cluster creation.

###### Note

All new users created before **March 26,
2020** have been granted the `dbAdminAnyDatabase`,
`readWriteAnyDatabase`, and `clusterAdmin`
roles. It is recommended that you reevaluate all users and modify
the roles as necessary to enforce least privilege for all users in
your clusters.

For more information, see [Database access using Role-Based
Access Control](role_based_access_control.md "role_based_access_control.md").

## Primary and `serviceadmin` user

A newly created Amazon DocumentDB cluster has two users: the primary user and the `serviceadmin` user.

The _primary user_ is a single, privileged user
that can perform administrative tasks and create additional users with
roles. When you connect to an Amazon DocumentDB cluster for the first time, you
must authenticate using the primary sign-in credentials. The primary
user receives these administrative permissions for an Amazon DocumentDB cluster
when that cluster is created, and is granted the role of `root`.

The `serviceadmin` user is created implicitly when the
cluster is created. Every Amazon DocumentDB cluster has a `serviceadmin`
user that provides AWS the ability to manage your cluster. You cannot
log in as, drop, rename, change the password, or change the permissions
for `serviceadmin`. Any attempt to do so results in an error.

###### Note

The primary and `serviceadmin` users for an Amazon DocumentDB
cluster cannot be deleted and the role of `root` for the
primary user cannot be revoked.

If you forget your primary user password, you can reset it using
the AWS Management Console or the AWS CLI.

## Creating additional users

After you connect as the primary user (or any user that has the role
`createUser`), you can create a new user, as shown below.

```
db.createUser(
    {
        user: "sample-user-1",
        pwd: "password123",
        roles:
            [{"db":"admin", "role":"dbAdminAnyDatabase" }]
    }
)

```

To view user details, you can use the `show users` command
as follows. You can additionally remove users with the
`dropUser` command. For more information, see [Common commands](role_based_access_control.md#role_based_access_control-common_commands "role_based_access_control.md#role_based_access_control-common_commands").

```
show users
{
    "_id" : "serviceadmin",
    "user" : "serviceadmin",
    "db" : "admin",
    "roles" : [
    	{
            "role" : "root",
            "db" : "admin"
        }
    ]
},

{
    "_id" : "myPrimaryUser",
    "user" : "myPrimaryUser",
    "db" : "admin",
    "roles" : [
    	{
            "role" : "root",
            "db" : "admin"
        }
    ]
},

{
    "_id" : "sample-user-1",
    "user" : "sample-user-1",
    "db" : "admin",
    "roles" : [
    	{
            "role" : "dbAdminAnyDatabase",
            "db" : "admin"
    	}
    ]
}

```

In the example above, the new user `sample-user-1` is
attributed to the `admin` database. This is always the case
for a new user. Amazon DocumentDB does not have the concept of an
`authenticationDatabase` and thus all authentication is
performed in the context of the `admin` database.

When creating users, if you omit the `db` field when
specifying the role, Amazon DocumentDB will implicitly attribute the role to the
database in which the connection is being issued against. For example,
if your connection is issued against the database `sample-database`
and you run the following command, the user `sample-user-2`
will be created in the `admin` database and will have
`readWrite` permissions to the database `sample-database`.

```
db.createUser(
    {
        user: "sample-user-2",
        pwd: "password123",
        roles:
            ["readWrite"]
    }
)

```

Creating users with roles that are scoped across all databases (for
example, `readInAnyDatabase`) require that you are either in
the context of the `admin` database when creating the user
or you explicitly state the database for the role when creating the user.

To switch the context of your database, you can use the following
command.

```
use admin
```

To learn more about Role Based Access Control and enforcing least
privilege amongst the users in your cluster, see [Database access using Role-Based
Access Control](role_based_access_control.md "role_based_access_control.md").

## Automatically rotating passwords for Amazon DocumentDB

With AWS Secrets Manager, you can replace hardcoded credentials in your code (including passwords)
with an API call to Secrets Manager to retrieve the secret programmatically. This helps ensure
that the secret can't be compromised by someone examining your code, because the secret
simply isn't there. Also, you can configure Secrets Manager to automatically rotate the secret
for you according to a schedule that you specify. This enables you to replace long-term
secrets with short-term ones, which helps to significantly reduce the risk of
compromise.

Using Secrets Manager, you can automatically rotate your Amazon DocumentDB passwords (that is,
_secrets_) using an AWS Lambda function that Secrets Manager
provides.

For more information about AWS Secrets Manager and native integration with Amazon DocumentDB, see the
following:

- [Blog: How to rotate Amazon DocumentDB and Amazon Redshift credentials in AWS
  Secrets Manager](https://aws.amazon.com/blogs/security/how-to-rotate-amazon-documentdb-and-amazon-redshift-credentials-in-aws-secrets-manager/ "https://aws.amazon.com/blogs/security/how-to-rotate-amazon-documentdb-and-amazon-redshift-credentials-in-aws-secrets-manager/")
- [What is AWS Secrets Manager?](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md")
- [Rotate
  AWS Secrets Manager secrets](../../../secretsmanager/latest/userguide/rotating-secrets-documentdb.md "../../../secretsmanager/latest/userguide/rotating-secrets-documentdb.md")
- [Amazon DocumentDB
  credentials in Secrets Manager](../../../secretsmanager/latest/userguide/reference_secret_json_structure.md#reference_secret_json_structure_docdb "../../../secretsmanager/latest/userguide/reference_secret_json_structure.md#reference_secret_json_structure_docdb")
