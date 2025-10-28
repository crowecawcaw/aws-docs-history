# Viewing the resources that a LF-Tag is

assigned to

You can view all the Data Catalog resources that a particular LF-Tag key is assigned to. To
do so, you need the following Lake Formation permissions:

- `Describe` or `Associate` on the LF-Tag.
- `Describe` or any other Lake Formation permission on the resource.
  In addition, you need the following AWS Identity and Access Management (IAM) permissions:

- `lakeformation:SearchDatabasesByLFTags`
- `lakeformation:SearchTablesByLFTags`

Console

###### To view the resources that a LF-Tag is assigned to (console)

1. Open the Lake Formation console at
   [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/").

Sign in as a data lake administrator or as a user who meets the requirements
listed earlier. 2. In the navigation pane, under **Permissions** and
**LF-Tags and permissions**, choose
**LF-Tags**. 3. Choose a LF-Tag key (not the option button next to the key name).

The LF-Tag details page displays a list of resources that the LF-Tag has
been assigned to.

![The image is a screenshot of the LF-Tag detail page for the key "module". The LF-Tag detail page has two sections. The top section displays the LF-Tag key and values. The bottom section displays the resources associated with that LF-Tag in a table with the following columns: Key, Values, Resource type, and Resource. The table has 12 rows, but only 7 are shown in the screenshot. The table rows show that the LF-Tag is assigned to a database, two of the tables in the database, and by inheritance, the columns of those tables.](images/resources-on-tags-2.png)

AWS CLI

###### To view the resources that a LF-Tag is assigned to

- Run a `search-tables-by-lf-tags` or
  `search-databases-by-lf-tags` command.

The following example lists tables and columns that have the
`level=vp` LF-Tag assigned. For each table and column listed, all
assigned LF-Tags for the table or column are output, not just the search
expression.

```
aws lakeformation search-tables-by-lf-tags --expression TagKey=level,TagValues=vp
```

For more information about the required permissions, see [Lake Formation personas and IAM permissions reference](permissions-reference.md "permissions-reference.md").
