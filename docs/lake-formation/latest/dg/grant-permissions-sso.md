

# Granting permissions to users and groups
<a name="grant-permissions-sso"></a>

Your data lake administrator can grant permissions to IAM Identity Center users and groups on Data Catalog resources (databases, tables, and views) to allow easy data access. To grant or revoke data lake permissions, the grantor requires permissions for the following IAM Identity Center actions.
+ [DescribeUser](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_DescribeUser.html)
+ [DescribeGroup](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_DescribeGroup.html)
+ [DescribeInstance](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DescribeInstance.html)

You can grant permissions by using the Lake Formation console, the API, or the AWS CLI.

For more information on granting permissions, see [Granting permissions on Data Catalog resources](granting-catalog-permissions.md). 

**Note**  
You can only grant permissions on resources in your account. To cascade permissions to users and groups on resources shared with you, you must use AWS RAM resources shares.

------
#### [ AWS Management Console ]

**To grant permissions to users and groups**

1. Sign in to the AWS Management Console, and open the Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/).

1. Select **Data lake permissions** under **Permissions** in the Lake Formation console. 

1. Select **Grant**.

1. On the **Grant data lake permissions** page, choose, **IAM Identity Center** users and groups. 

1. Select **Add** to choose the users and groups to grant permissions.  
![Grant data lake permissions screen with IAM Identity Center users and groups selected.](http://docs.aws.amazon.com/lake-formation/latest/dg/images/identity-center-grant-perm.png)

1. On the **Assign users and groups** screen, choose the users and/or groups to grant permissions.

   Select **Assign**.  
![Grant data lake permissions screen with IAM Identity Center users and groups selected.](http://docs.aws.amazon.com/lake-formation/latest/dg/images/identity-center-assign-users-groups.png)

1. Next, choose the method to grant permissions.

   For instructions on granting permissions using named resources method, see [Granting data permissions using the named resource method](granting-cat-perms-named-resource.md).

   For instructions on granting permission using LF-Tags, see [Granting data lake permissions using the LF-TBAC method](granting-catalog-perms-TBAC.md).

1. Choose the Data Catalog resources on which you want to grant permissions.

1. Choose the Data Catalog permissions to grant.

1. Select **Grant**.

------
#### [ AWS CLI ]

The following example shows how to grant IAM Identity Center user `SELECT` permission on a table.

```
aws lakeformation grant-permissions \
--principal DataLakePrincipalIdentifier=arn:aws:identitystore:::user/{{<UserId>}} \
--permissions "SELECT" \
--resource '{ "Table": { "DatabaseName": "retail", "TableWildcard": {} } }'
```

To retrieve `UserId` from IAM Identity Center, see [GetUserId](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_GetUserId.html) operation in the IAM Identity Center API Reference.

------