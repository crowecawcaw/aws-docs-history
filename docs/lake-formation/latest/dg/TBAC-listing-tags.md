# Listing LF-Tags

You can list the LF-Tags that you have the `Describe` or
`Associate` permissions on. The values listed with each LF-Tag key are the
values that you have permissions on.

LF-Tag creator has implicit permissions to see the LF-Tags they have created.

Data lake administrators can see all LF-Tags that are defined in the local AWS
account and all LF-Tags for which the `Describe` and `Associate`
permissions have been granted to the local account from external accounts. The data lake
administrator can see all values for all LF-Tags.

You can list LF-Tags by using the AWS Lake Formation console, the API, or the AWS Command Line Interface
(AWS CLI).

Console

###### To list LF-Tags (console)

1. Open the Lake Formation console at
   [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/").

Sign in as the LF-Tag creator, as a data lake administrator, or as a principal that has been granted
permissions on LF-Tags and that has the `lakeformation:ListLFTags`
IAM permission. 2. In the navigation pane, under **Permissions**,
**LF-Tags and permissions**, choose
**LF-Tags**.

The **LF-Tags** page appears.

![The page has a 3-column table with column headings Key, Values, and Owner account ID. The table has 2 rows. Above the table are 4 buttons arranged horizontally: Reload page, Delete (dimmed), Edit (dimmed), and Add tag. The page also has a search field with the placeholder text "Find tag". To the right of the search field is a page selector, showing the value "1" between left and right buttons, and a Settings icon.](images/policy-tags-page-2.png)

Check the **Owner account ID** column to determine the
LF-Tags that were shared with your account from an external account.

AWS CLI

###### To list LF-Tags (AWS CLI)

- Run the following command as a data lake administrator or as a principal that
  has been granted permissions on LF-Tags and that has the
  `lakeformation:ListLFTags` IAM permission.

```
aws lakeformation list-lf-tags
```

The output is similar to the following.

```
{
    "LFTags": [
        {
            "CatalogId": "111122223333",
            "TagKey": "level",
            "TagValues": [
                "director",
                "vp",
                "c-level"
            ]
        },
        {
            "CatalogId": "111122223333",
            "TagKey": "module",
            "TagValues": [
                "Orders",
                "Sales",
                "Customers"
            ]
        }
    ]
}

```

To also see LF-Tags that were granted from external accounts, include the
command option `--resource-share-type ALL`.

```
aws lakeformation list-lf-tags --resource-share-type ALL
```

The output is similar to the following. Note the `NextToken` key,
which indicates that there is more to list.

```
{
    "LFTags": [
        {
            "CatalogId": "111122223333",
            "TagKey": "level",
            "TagValues": [
                "director",
                "vp",
                "c-level"
            ]
        },
        {
            "CatalogId": "111122223333",
            "TagKey": "module",
            "TagValues": [
                "Orders",
                "Sales",
                "Customers"
            ]
        }
    ],
    "NextToken": "eyJleHBpcmF0aW...ZXh0Ijp0cnVlfQ=="
}

```

Repeat the command, and add the `--next-token` argument to view any
remaining local LF-Tags and LF-Tags that were granted from external accounts.
LF-Tags from external accounts are always on a separate page.

```
aws lakeformation list-lf-tags --resource-share-type ALL
--next-token eyJleHBpcmF0aW...ZXh0Ijp0cnVlfQ==
```

```
{
    "LFTags": [
        {
            "CatalogId": "123456789012",
            "TagKey": "region",
            "TagValues": [
                "central",
                "south"
            ]
        }
    ]
}
```

API
You can use the SDKs available for Lake Formation to lists the tags that the requester has
permission to view.

```
import boto3

client = boto3.client('lakeformation')
...

response = client.list_lf_tags(
    CatalogId='`string`',
    ResourceShareType='ALL',
    MaxResults=50'
)
```

This command returns a `dict` object with the following structure:

```
{
    'LFTags': [
        {
            'CatalogId': 'string',
            'TagKey': 'string',
            'TagValues': [
                'string',
            ]
        },
    ],
    'NextToken': 'string'
}
```

For more information about the required permissions, see [Lake Formation personas and IAM permissions reference](permissions-reference.md "permissions-reference.md").
