# Updating LF-Tag expressions

Only data lake administrators, the LF-Tag expression creator, and principals that have
`Alter` or `Super` permission on the LF-Tag expression can
update an LF-Tag expression. In addition to `Alter` permission, you also
need the `lakeformation:UpdateLFTagExpression` IAM permission and `Grant
 with LF-Tag` permission on all underlying keys-values on the new expression body to
update expressions.

You update an LF-Tag expression by updating the description, expression body and
permissions granted on the expression. You can't change the name of the LF-Tag
expression. To change the name, delete the LF-Tag expression and add one with the
required parameters.

You can update an LF-Tag expression by using the AWS Lake Formation console, the API, or the
AWS Command Line Interface (AWS CLI).

Console

###### To update an LF-Tag expression

1. Open the Lake Formation console at
   [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/").

Sign in as a data lake administrator, the LF-Tag creator or a principal
with `Alter` permission on the LF-Tag. 2. In the navigation pane, under permissions, choose **LF-Tags and permissions**. 3. Choose **LF-Tag expressions** tab. 4. On the **LF-Tag expressions** section, select an
LF-Tag expression, and then choose **Edit**. 5. In the **Edit LF-Tag expression** dialog box, update
the description and update the expression body by adding or removing keys and
values.

To add multiple values, in the **Values** field, choose the values from the drop down. 6. Choose **Save**.

AWS CLI

The update-lf-tag-expression command in Lake Formation allows you to update an existing LF-Tag expression.

```
aws lakeformation update-lf-tag-expression \
-- name `expression_name`\
-- description `new_description` \
-- catalog-id `catalog_id` \
-- expression '{"Expression": [{"TagKey": "`tag_key`", "TagValues": ["`tag_value1`", "`tag_value2`", ...]}]}'

```

Here's what the parameters in the provided command mean:

- name – The name of the existing named tag expression that you want to
  update.
- description – A new description for the expression.

catalog-id – The ID of the Data Catalog where the named tag expression
resides.

- expression – The new tag expression string that you want to update the
  expression with.
