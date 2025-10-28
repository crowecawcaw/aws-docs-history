# Assigning LF-Tags to Data Catalog resources

You can assign LF-Tags to Data Catalog resources (databases, tables, and columns) to control
access to those resources. Only principals that are granted matching LF-Tags (and principals
that are granted access with the named resource method) can access the resources.

If a table inherits a LF-Tag from a database or a column inherits a LF-Tag from a
table, you can override the inherited value by assigning a new value to the LF-Tag
key.

The maximum number of LF-Tags that you can assign to a resource is 50.

###### Topics

- [Requirements for managing tags assigned to
  resources](#manage-tags-reqs "#manage-tags-reqs")
- [Assign LF-Tags to a table column](#assign-tag-column "#assign-tag-column")
- [Assign LF-Tags to a Data Catalog resource](#assign-tag-catalog-resource "#assign-tag-catalog-resource")
- [Updating LF-Tags for a resource](#update-tags "#update-tags")
- [Removing LF-Tag from a resource](#remove-tag "#remove-tag")

## Requirements for managing tags assigned to

resources

To assign a LF-Tag to a Data Catalog resource, you must:

- Have the Lake Formation `ASSOCIATE` permission on the LF-Tag.
- Have the IAM `lakeformation:AddLFTagsToResource` permission.
- Have glue:GetDatabase permission on a Glue database.
- Be the resource owner (creator), have the `Super` Lake Formation permission on the
  resource with the `GRANT` option, or have the following permissions with the
  `GRANT` option:
  - For databases in the same AWS account: `DESCRIBE`, `CREATE_TABLE`,
    `ALTER`, and `DROP`
  - For databases in an external account: `DESCRIBE`, `CREATE_TABLE` and
    `ALTER`
  - For tables (and columns): `DESCRIBE`, `ALTER`, `DROP`,
    `INSERT`, `SELECT`, and `DELETE`

In addition, the LF-Tag and the resource that it is being assigned to must be in the
same AWS account.

To remove a LF-Tag from a Data Catalog resource, you must meet these requirements, and also
have the `lakeformation:RemoveLFTagsFromResource` IAM permission.

## Assign LF-Tags to a table column

###### To assign LF-Tags to a table column (console)

1. Open the Lake Formation console at
   [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/").

Sign in as a user who meets the requirements listed above. 2. In the navigation pane, choose **Tables**. 3. Choose a table name (not the option button next to the table name). 4. On the table details page, in the **Schema** section, choose
**Edit schema**. 5. On the **Edit schema** page, select one or more columns, and then
choose **Edit LF-Tags**.

###### Note

If you intend to add or delete columns and save a new version, do that first. Then
edit the LF-Tags.

The **Edit LF-Tags** dialog box appears, and displays any
LF-Tags that are inherited from the table.

![The image is a screenshot of the Edit LF-Tags dialog window. The top part of the windows shows two inherited keys. The first inherited key has the key "level" and the value "director (inherited)". The second inherited key has the key "module" and the value "Orders (inherited)". Below those fields is an "Assign new LF-Tag" button. Below and to the right are the Cancel and Save buttons.](images/edit-policy-tags-for-columns-2a.png) 6. (Optional) For the **Values** list next to an **Inherited
keys** field, choose a value to override the inherited value. 7. (Optional) Choose **Assign new LF-Tag**. Then for
**Assigned keys**, choose a key, and for **Values**,
choose a value for the key.

![The image is a screenshot of the Edit LF-Tags dialog window. The top part of the windows shows two inherited keys. The first inherited key has the key "level" and the value "director (inherited)". The second inherited key has the key "module" and the value "Orders (inherited)". Below this section, aligned horizontally, are these fields and controls : "Assigned keys" field, "Values" field, and a Remove button. The Assigned keys field contains the text "environment". The Values field is a drop-down list, with the values "Production" (highlighted) and "Customers". An "Assign new LF-Tag" button appears below the Assigned keys field. In the bottom right of the window are the Cancel and Save buttons.](images/edit-policy-tags-for-columns-2b.png) 8. (Optional) Choose **Assign new LF-Tag** again to add
another LF-Tag. 9. Choose **Save**.

## Assign LF-Tags to a Data Catalog resource

Console

###### To assign LF-Tags to a Data Catalog database or table

1. Open the Lake Formation console at
   [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/").

Sign in as a user who meets the requirements listed earlier. 2. In the navigation pane, under **Data catalog**, do one of the
following:

    * To assign LF-Tags to databases, choose
     **Databases**.
    * To assign LF-Tags to tables, choose **Tables**.

3. Choose a database or table, and on the **Actions** menu,
   choose **Edit LF-Tags**.

The **Edit LF-Tags:
`resource-name`** dialog box appears.

If a table inherits LF-Tags from its containing database, the window
displays the inherited LF-Tags. Otherwise, it displays the text "There are no
inherited LF-Tags associated with the resource."

![The image is a screenshot of the "Edit LF-Tags: inventory" dialog window. At the top are the fields "Inherited keys" (dimmed) and "Values". The Inherited keys field has the value "level" and the Values field has the value "director (inherited)". Below this section, aligned horizontally, are these fields and controls : "Assigned keys" field, "Values" field, and a Remove button. The Assigned keys field contains the text "module". The Values field is a drop-down list, with the values "Orders", "Sales", and "Customers" (highlighted). An "Assign new LF-Tag" button is below the Assigned keys field. In the bottom right of the window are Cancel and Save buttons.](images/edit-policy-tags-for-tables-2.png) 4. (Optional) If a table has inherited LF-Tags, for the
**Values** list next to an **Inherited keys**
field, you can choose a value to override the inherited value. 5. To assign new LF-Tags, perform these steps:

    1. Choose **Assign new LF-Tag**.
    2. In the **Assigned keys** field, choose a LF-Tag key,
     and in the **Values** field, choose a value.
    3. (Optional) Choose **Assign new LF-Tag** again to
     assign an additional LF-Tag.

6. Choose **Save**.

AWS CLI

###### To assign LF-Tags to a Data Catalog resource

- Run the `add-lf-tags-to-resource` command.

The following example assigns the LF-Tag `module=orders` to the
table `orders` in the database `erp`. It uses the shortcut
syntax for the `--lf-tags` argument. The `CatalogID`
property for `--lf-tags` is optional. If not provided, the catalog ID
of the resource (in this case, the table) is assumed.

```
aws lakeformation add-lf-tags-to-resource --resource '{ "Table": {"DatabaseName":"erp", "Name":"orders"}}' --lf-tags  CatalogId=111122223333,TagKey=module,TagValues=orders
```

The following is the output if the command succeeds.

```
{
    "Failures": []
}

```

This next example assigns two LF-Tags to the `sales` table, and
uses the JSON syntax for the `--lf-tags` argument.

```
aws lakeformation add-lf-tags-to-resource --resource '{ "Table": {"DatabaseName":"erp", "Name":"sales"}}' --lf-tags '[{"TagKey": "module","TagValues": ["sales"]},{"TagKey": "environment","TagValues": ["development"]}]'
```

This next example assigns the LF-Tag `level=director` to the
`total` column of the table `sales`.

```
aws lakeformation add-lf-tags-to-resource --resource '{ "TableWithColumns": {"DatabaseName":"erp", "Name":"sales", "ColumnNames":["total"]}}' --lf-tags TagKey=level,TagValues=director
```

## Updating LF-Tags for a resource

###### To update a LF-Tag for a Data Catalog resource (AWS CLI)

- Use the `add-lf-tags-to-resource` command, as described in the previous
  procedure.

Adding a LF-Tag with the same key as an existing LF-Tag, but with a different
value updates the existing value.

## Removing LF-Tag from a resource

###### To remove a LF-Tag for a Data Catalog resource (AWS CLI)

- Run the `remove-lf-tags-from-resource` command.

If a table has a LF-Tag value that overrides the value that is inherited from the
parent database, removing that LF-Tag from the table restores the inherited value. This
behavior also applies to a column that overrides key values inherited from the table.

The following example removes the LF-Tag `level=director` from the
`total` column of the `sales` table. The `CatalogID`
property for `--lf-tags` is optional. If not provided, the catalog ID of the
resource (in this case, the table) is assumed.

```
aws lakeformation remove-lf-tags-from-resource
--resource ' { "TableWithColumns":
{ "DatabaseName": "erp",  "Name": "sales",  "ColumnNames":[ "total"]}}'
--lf-tags  CatalogId=111122223333,TagKey=level,TagValues=director
```
