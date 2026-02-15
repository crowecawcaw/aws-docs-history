# Deleting LF-Tag expressions

You can delete LF-Tag expressions that are no longer in use. If you have granted permissions to principals on
Data Catalog resources using the LF-Tag expression, they will no longer have the permissions.

Only data lake administrators, the LF-Tag expression creator, or a principal with
`Drop` permission on the LF-Tag expression can delete an LF-Tag
expression. In addition to the `Drop` permission, the principal also needs
`lakeformation:DeleteLFTagExpression` IAM permission to delete an
LF-Tag expression.

You can delete an LF-Tag expression by using the AWS Lake Formation console, the API, or the
AWS Command Line Interface (AWS CLI).

Console

###### To delete an LF-Tag expression (console)

1. Open the Lake Formation console at
   [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/").

Sign in as a data lake administrator, the LF-Tag expression creator, or a principal
that has permissions to delete the expression. 2. In the navigation pane, under **Permissions**, choose
**LF-Tags and permissions**. 3. Choose the
**LF-Tag expression** tab. 4. On the **LF-Tag expressions** section, select an
LF-Tag expression, and then choose **Delete**. 5. In the **Delete LF-Tag expression?** dialog box, to confirm the
deletion, enter the LF-Tag expression name in the designated field and then choose
**Delete**.

AWS CLI

###### To delete an LF-Tag (AWS CLI)

- Enter a `delete-lf-tag-expression` command. Provide the expression name and catalog ID to
  delete.

###### Example

The following example deletes the LF-Tag expression with the name
`my-tag-expression` from the Data Catalog with ID `123456789012`. The
`catalog-id` parameter is optional if you're using the same account as your AWS CLI configuration. After deleting an LF-Tag expression, Lake Formation cleans
up the associated permission records for that expression. This includes both
individual permission records and aggregate permission records that contain the
deleted expression.

```
aws lakeformation delete-lf-tag-expression \
--name "`my-tag-expression`" \
--catalog-id "`123456789012`"
```
