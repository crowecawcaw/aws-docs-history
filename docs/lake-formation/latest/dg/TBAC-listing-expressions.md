# Listing LF-Tag expressions

You can list the LF-Tag expressions that you have the Describe permissions on.
Data lake administrators, LF-Tag expression creators, and Read-only administrators implicitly can see all tag expressions
in their account.

You can list LF-Tag expressions by using the AWS Lake Formation console, the API, or the AWS Command Line Interface
(AWS CLI).

Console

###### To list LF-Tag expressions (console)

1. Open the Lake Formation console at
   [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/").

Sign in as the LF-Tag expression creator, as a data lake administrator,
or as a principal that has been granted permissions on LF-Tag expressions
and that has the `lakeformation:ListLFTagExpressions` IAM
permission. 2. In the navigation pane, under **Permissions**,
**LF-Tags and permissions**. 3. Choose **LF-Tag expressions** tab to see the
expressions. This section shows the information about the existing LF-Tag
expressions, including the expression name, the expression itself with links to the
included tags, and options to create, edit, or delete expressions.

AWS CLI

###### To list LF-Tags (AWS CLI)

- To list LF-Tag expressions using the AWS CLI, you can use the
  list-lf-tag-expressions command. The request syntax is:

```
aws lakeformation list-lf-tag-expressions \
-- catalog-id "123456789012" \
-- max-items "100" \
-- next-token "next-token"
```

Where:

    + `catalog-id` is the AWS account ID of the Data Catalog you want to list tag expressions for .
    + `max-items` specifies the maximum number of tag expressions to return. If this
     parameter is not used, the default value is 100.
    + `next-token` is a continuation token if the results were truncated in a previous
     request.

The response will include a list of
LF-Tag expressions and a next token if applicable.
