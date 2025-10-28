# Lake Formation tag-based access control best

practices and considerations

You can create, maintain, and assign LF-Tags to control access to Data Catalog databases, tables,
and columns.

Consider the following best practices when using Lake Formation tag-based access control:

- All LF-Tags must be predefined before they can be assigned to Data Catalog resources or
  granted to principals.

The data lake administrator can delegate tag management tasks by creating _LF-Tag creators_ with the required IAM permissions. Data
engineers and analysts decide on the characteristics and relationships for LF-Tags. The
LF-Tag creators then creates and maintains the LF-Tags in Lake Formation.

- You can assign multiple LF-Tags to Data Catalog resources. Only one value for a particular key
  can be assigned to a particular resource.

For example, you can assign `module=Orders`, `region=West`,
`division=Consumer`, and so on to a database, table, or column. You can't
assign `module=Orders,Customers`.

- You can't assign LF-Tags to resources when you create the resource. You can only add LF-Tags
  to existing resources.
- You can grant LF-Tag expressions, not just single LF-Tags, to a principal.

A LF-Tag expression looks something like the following (in pseudo-code).

```
module=sales AND division=(consumer OR commercial)
```

A principal that is granted this LF-Tag expression can access only Data Catalog resources
(databases, tables, and columns) that are assigned `module=sales`
_and_ either `division=consumer` or
`division=commercial`. If you want the principal to be able to access
resources that have `module=sales`
_or_
`division=commercial`, don't include both in the same grant. Make two grants,
one for `module=sales` and one for `division=commercial`.

The simplest LF-Tag expression consists of just one LF-Tag, such as
`module=sales`.

- A principal that is granted permissions on a LF-Tag with multiple values can access
  Data Catalog resources with either of those values. For example, if a user is granted a LF-Tag
  with key=`module` and values=`orders,customers`, the user has access
  to resources that are assigned either `module=orders` or
  `module=customers`.
- You need to have `Grant with LF-Tag expressions` permission to grant data
  permissions on Data Catalog resources by using the LF-TBAC method. The data lake administrator
  and the LF-Tag creator implicitly receive this permission. A principal that has the
  `Grant with LFTag expressions` permission can grant data permissions on the
  resources using:
  - the named resource method
  - the LF-TBAC method, but only using the same LF-Tag expression

  For example, assume that the data lake administrator makes the following grant (in
  pseudo-code).

  ```
  GRANT (SELECT ON TABLES) ON TAGS module=customers, region=west,south TO user1 WITH GRANT OPTION
  ```

  In this case, `user1` can grant `SELECT` on tables to other
  principals by using the LF-TBAC method, but only with the complete LF-Tag expression
  `module=customers, region=west,south`.

- If a principal is granted permissions on a resource with both the LF-TBAC method and the
  named resource method, the permissions that the principal has on the resource is the union
  of the permissions granted by both methods.
- Lake Formation supports granting `DESCRIBE` and `ASSOCIATE` on LF-Tags across
  accounts, and granting permissions on Data Catalog resources across accounts using the LF-TBAC
  method. In both cases, the principal is an AWS account ID.

###### Note

Lake Formation supports cross-account grants to organizations and organizational units
using LF-TBAC method. To use this capability, you need to update **Cross account version settings** to **Version 3**.

For more information, see [Cross-account data sharing in Lake Formation](cross-account-permissions.md "cross-account-permissions.md").

- Data Catalog resources created in one account can only be tagged using LF-Tags created in the same account.
  LF-Tags created in one account can't be associated with shared resources from another account.
- Using Lake Formation tag-based access control (LF-TBAC) to grant cross-account access to Data Catalog
  resources requires additions to the Data Catalog resource policy for your AWS account. For
  more information, see [Prerequisites](cross-account-prereqs.md "cross-account-prereqs.md").
- LF-Tag keys and LF-Tag values can't exceed 50 characters in length.
- The maximum number of LF-Tags that can be assigned to a Data Catalog resource is 50.
- The following limits are soft limits:
  - The maximum number of LF-Tags that can be created is 1000.
  - The maximum number of values that can be defined for a LF-Tag is 1000.

- Tags keys and values are converted to all lower case when they are stored.
- Only one value for a LF-Tag can be assigned to a particular resource.
- If multiple LF-Tags are granted to a principal with a single grant, the principal can
  access only Data Catalog resources that have all of the LF-Tags.
- If a LF-Tag expression evaluation results in access to only a subset of table columns,
  but the Lake Formation permission granted when there is a match is one of the permissions that
  required full column access, namely `Alter`, `Drop`,
  `Insert`, or `Delete`, then none of those permissions is granted.
  Instead, only `Describe` is granted. If the granted permission is
  `All` (`Super`), then only `Select` and
  `Describe` are granted.
- Wildcards are not used with LF-Tags. To assign a LF-Tag to all columns of a
  table, you assign the LF-Tag to the table, and all columns in the table inherit
  the LF-Tag. To assign a LF-Tag to all tables in a database, you assign the
  LF-Tag to the database, and all tables in the database inherit that
  LF-Tag.
- You can create up to 1000 LF-Tag expressions in an account.
- You can use up to 50 LF-Tag expressions to grant permissions to a principal on the Data Catalog resources.
- When granting or revoking permissions on an inline LF-Tag expression, the size of the LF-Tag expression can not exceed 900 bytes.
  To grant permissions on larger LF-Tag expressions, use the saved LF-Tag expressions. For more information, see [Creating LF-Tag expressions](TBAC-creating-tag-expressions.md "TBAC-creating-tag-expressions.md").
- To add LF-Tag to existing Redshift federated catalogs that were created before
  the general availability release of LF-Tag support for federated catalogs, you need to
  contact the AWS support team for assistance.
