# Creating LF-Tags

All LF-Tags must be defined in Lake Formation before they can be used. A LF-Tag consists of a
key and one or more possible values for the key.

After the data lake administrator has setup the required IAM permissions and Lake Formation
permissions for the LF-Tag creator role, the principal can create a LF-Tag. The
LF-Tag creator gets implicit permission to update or remove any tag value from the
LF-Tag and delete the LF-Tag.

You can create LF-Tags by using the AWS Lake Formation console, the API, or the AWS Command Line Interface
(AWS CLI).

Console

###### To create a LF-Tag

1. Open the Lake Formation console at
   [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/").

Sign in as a principal with LF-Tag creator permissions or as data lake administrator. 2. In the navigation pane, under **Permissions**, **LF-Tags and permissions**, choose
**LF-Tags**.

The **LF-Tags** page appears.

![The page has a 4-column table with column headings Key, Values, Owner account ID, and LF-Tag permissions. The table has 2 rows. Above the table are 4 buttons arranged horizontally: Delete (dimmed), Edit (dimmed), Grant permissions (dimmed) and Add tag. The page also has a search field with the placeholder text "Find tag". To the right of the search field is a page selector, showing the value "1" between left and right buttons, and a Settings icon.](images/policy-tags-page-2.png) 3. Choose **Add LF-Tag**. 4. In the **Add LF-Tag** dialog box, enter a key and one
or more values.

Each key must have at least one value. To enter multiple values, either enter a
comma-delimited list and then press **Enter**, or enter one value
at a time and choose **Add** after each one. The maximum number of
values permitted is 1000. 5. Choose **Add tag**.

AWS CLI

###### To create a LF-Tag

- Enter a `create-lf-tag` command.

The following example creates a LF-Tag with key `module` and values
`Customers` and `Orders`.

```
aws lakeformation create-lf-tag --tag-key module --tag-values Customers Orders
```

As tag creator , the principal gets `Alter` permission on this LF-Tag and can
update or remove any tag value from this LF-Tag. The LF-Tag creator principal
can also grant `Alter` permission to another principal to update and remove tag
values on this LF-Tag.
