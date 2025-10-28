# Viewing LF-Tags assigned to a

resource

You can view the LF-Tags that are assigned to a Data Catalog resource. You must have the
`DESCRIBE` or `ASSOCIATE` permission on a LF-Tag to view it.

Console

###### To view the LF-Tags that are assigned to a resource (console)

1. Open the Lake Formation console at
   [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/").

Sign in as the data lake administrator, the resource owner, or a user who has
been granted Lake Formation permissions on the resource. 2. In the navigation pane, under the heading **Data catalog**, do
one of the following:

    * To view LF-Tags assigned to a database, choose
     **Databases**.
    * To view LF-Tags assigned to a table, choose
     **Tables**.

3. On the **Tables** or **Databases** page,
   choose the name of the database or table. Then on the details page, scroll down to
   the **LF-Tags** section.

The following screenshot shows the LF-Tags assigned to a
`customers` table, which is contained in the `retail`
database. The `module` LF-Tag is inherited from the database. The
`credit_limit` column has the `level=vp` LF-Tag
assigned.

![The image is a screenshot of the LF-Tags section of the customers table detail page. The LF-Tags section contains a table with the following columns: Resource, Key, Value, and Inherited from. The table has 3 rows. Above the table is a text entry field with the "Find tags" placeholder text, and an Edit tags button. The paragraph that precedes the image describes the table values shown in the screenshot.](images/tags-for-resource-2.png)

AWS CLI

###### To view the LF-Tags that are assigned to a resource (AWS CLI)

- Enter a command similar to the following.

```
aws lakeformation get-resource-lf-tags --show-assigned-lf-tags --resource '{ "Table": {"CatalogId":"111122223333", "DatabaseName":"erp", "Name":"sales"}}'
```

The command returns the following output.

```
{
    "TableTags": [
        {
            "CatalogId": "111122223333",
            "TagKey": "module",
            "TagValues": [
                "sales"
            ]
        },
        {
            "CatalogId": "111122223333",
            "TagKey": "environment",
            "TagValues": [
                "development"
            ]
        }
    ],
    "ColumnTags": [
        {
            "Name": "total",
            "Tags": [
                {
                    "CatalogId": "111122223333",
                    "TagKey": "level",
                    "TagValues": [
                        "director"
                    ]
                }
            ]
        }
    ]
}
```

This output shows only LF-Tags that are explicitly assigned, not inherited. If
you want to see all LF-Tags on all columns, including inherited LF-Tags, omit
the `--show-assigned-lf-tags` option.
